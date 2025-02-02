# boards-listing-tool



### Developer Instructions

#### To run app as CLI
Create a Python venv (virtual environment) - currently tested on Python 3.12 using macOS.

Copy `boards-listing-tool/.env.template` and name it `boards-listing-tool/.env`. Update the `BOARDS_DIRECTORY` value to point to the full directory containing the json files. e.g. in this project, they are stored in the `<MY PATH>/boards-listing-tool/data` folder.

Within the venv, run ```pip install -r requirements.txt```
To generate the list of boards, run a python shell ```python```

Within the shell,

```
from app import join_board_data

join_board_data()
```

### Tools used
* Stack Overflow
* Library docs (Pydantic, Dotenv)
* Copilot


### Planned extensions
* Complete TODOs
* Complete test cases.
* Add a flask endpoint to display the data.
* Handle duplicates - what counts as a duplicate? Case insensitive, all 4 fields the same?
* Containerise the app (likely using Docker) to ensure portability between operating systems.
