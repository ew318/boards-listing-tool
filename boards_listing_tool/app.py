import json
import logging
import os
from operator import itemgetter
from pathlib import Path

from dotenv import load_dotenv
from pydantic import ValidationError

from boards_listing_tool.models import Board

# Configure logging
logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)

# Unset the environment variable to avoid conflicts with the .env file
del os.environ["BOARDS_DIRECTORY"]
load_dotenv()  # take environment variables from .env.


def get_json_file_paths():
    directory = os.getenv("BOARDS_DIRECTORY")
    if not directory:
        raise ValueError("BOARDS_DIRECTORY environment variable is not set.")
    directory_path = Path(directory)
    json_file_paths = [file for file in directory_path.rglob("*.json")]
    return json_file_paths


def load_json_file(json_file_path):
    try:
        return json.loads(json_file_path.read_text())
    except json.JSONDecodeError:
        logger.warning(f"Error in file, invalid json: {json_file_path}")
        return None


def check_file_boards(json_file, json_file_path):
    if json_file.get("boards", None) is None:
        logger.warning(f"File does not contain boards, discarding: {json_file_path}")
        return False
    file_boards = json_file["boards"]
    if not isinstance(file_boards, list):
        logger.warning(f"Error in file, boards is not a list: {json_file_path}")
        return False
    return True


def validate_board_schema(board, json_file_path):
    try:
        return Board(**board)
    except ValidationError:
        logger.warning(
            f"Invalid board schema in file: {json_file_path}, skipping board {board}"
        )
        return None


def join_board_data():
    json_file_paths = get_json_file_paths()
    boards = []
    combined_boards = dict()
    for json_file_path in json_file_paths:

        json_file = load_json_file(json_file_path)
        if not json_file:
            continue

        contains_boards = check_file_boards(json_file, json_file_path)
        if not contains_boards:
            continue
        file_boards = json_file["boards"]

        for board in file_boards:
            # Keep only valid boards from file
            valid_board = validate_board_schema(board, json_file_path)
            if valid_board:
                boards.append(board)

    # Order boards
    combined_boards["boards"] = sorted(boards, key=itemgetter("vendor", "name"))

    # Generate metadata
    unique_vendors = set([x["vendor"] for x in combined_boards["boards"]])
    combined_boards["_metadata"] = {
        "total_vendors": len(unique_vendors),
        "total_boards": len(combined_boards["boards"]),
    }

    return combined_boards
