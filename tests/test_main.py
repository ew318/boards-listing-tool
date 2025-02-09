from unittest.mock import patch

import pytest

from boards_listing_tool.main import app


@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client


@patch("boards_listing_tool.main.join_board_data")
def test_board_list(mock_join_board_data, client):
    # Mock the join_board_data function
    mock_join_board_data.return_value = "Mocked board data"

    # Send a GET request to the root URL
    response = client.get("/")

    # Assert the response status code and data
    assert response.status_code == 200
    assert response.data.decode() == "Mocked board data"
