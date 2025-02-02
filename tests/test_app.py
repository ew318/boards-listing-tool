import os
from pathlib import Path

from boards_listing_tool.app import (
    check_file_boards,
    load_json_file,
    validate_board_schema,
)

#############
# TEST PLAN #
#############

# Test Cases
#   No directory set
#   Finds all the json files in directory (nested etc)
#   Invalid json in .json file


def test_check_file_boards():
    # Boards missing from json file
    assert check_file_boards({"no_boards": []}, "test.json") == False
    # Boards is not a list
    assert check_file_boards({"boards": "I am not a list"}, "test.json") == False
    # Boards present and is a list
    assert check_file_boards({"boards": []}, "test.json") == True
    assert check_file_boards({"boards": ["I have random data"]}, "test.json") == True


valid_board = {
    "name": "D4-200S",
    "vendor": "Boards R Us",
    "core": "Cortex-M4",
    "has_wifi": False,
}
valid_board_extra_field = {
    "name": "D4-200S",
    "vendor": "Boards R Us",
    "core": "Cortex-M4",
    "has_wifi": False,
    "more": 123,
}
invalid_board_missing = {
    "name": "D4-200S",
    "vendor": "Boards R Us",
    "core": "Cortex-M4",
}
invalid_board_data = {
    "name": "D4-200S",
    "vendor": 567,
    "core": "Cortex-M4",
    "has_wifi": False,
}


def test_validate_board_schema():
    # Schema is valid
    assert validate_board_schema(valid_board, "test.json") != None
    # Additional fields in board schema
    assert validate_board_schema(valid_board_extra_field, "test.json") != None
    # Insufficient fields in board schema
    assert validate_board_schema(invalid_board_missing, "test.json") is None
    # Correct fields, wrong data type
    assert validate_board_schema(invalid_board_data, "test.json") is None


def test_load_json_file():
    cwd = Path.cwd()
    # Not a json file
    invalid_json_path = os.path.join(cwd, "tests", "data", "invalid.json")
    assert load_json_file(Path(invalid_json_path)) == None
    # Json file
    valid_json_path = os.path.join(cwd, "tests", "data", "valid.json")
    assert load_json_file(Path(valid_json_path)) != None
