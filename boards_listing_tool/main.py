from flask import Flask

from boards_listing_tool.app import join_board_data

app = Flask(__name__)


@app.route("/")
def board_list():
    return join_board_data()

if __name__ == "__main__":
    # Please do not set debug=True in production
    app.run(host="0.0.0.0", port=5000, debug=True)