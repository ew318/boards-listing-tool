from flask import Flask

from boards_listing_tool.app import join_board_data

app = Flask(__name__)


@app.route("/")
def board_list():
    return join_board_data()
