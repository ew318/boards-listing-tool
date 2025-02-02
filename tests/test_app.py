import os
from pathlib import Path

from boards_listing_tool.app import (
    check_file_boards,
    join_board_data,
    load_json_file,
    validate_board_schema,
)

# TODO Test Cases
#   No directory set
#   Finds all the json files in directory (nested etc)


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


def test_whole_happy_path(mocker):
    cwd = Path.cwd()
    expected_data = {
        "boards": [
            {
                "name": "B7-400X",
                "vendor": "Boards R Us",
                "core": "Cortex-M7",
                "has_wifi": True,
            },
            {
                "name": "D4-200S",
                "vendor": "Boards R Us",
                "core": "Cortex-M4",
                "has_wifi": False,
            },
            {
                "name": "Low_Power",
                "vendor": "Tech Corp.",
                "core": "Cortex-M0+",
                "has_wifi": False,
            },
        ],
        "_metadata": {"total_vendors": 2, "total_boards": 3},
    }
    get_json_file_paths_mock = mocker.patch(
        "boards_listing_tool.app.get_json_file_paths"
    )
    boards1 = Path(os.path.join(cwd, "data", "boards-1.json"))
    boards2 = Path(os.path.join(cwd, "data", "boards-2.json"))
    get_json_file_paths_mock.return_value = [boards1, boards2]
    actual_data = join_board_data()
    assert actual_data == expected_data
