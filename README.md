# boards-listing-tool



### Developer Instructions

#### Setup and installation
Clone the repository. 
Create a Python venv (virtual environment) - currently tested on Python 3.12 using macOS.
Within a terminal, navigate to the `boards-listing-tool` directory.

Copy `boards-listing-tool/.env.template` and name it `boards-listing-tool/.env`. Update the `BOARDS_DIRECTORY` value to point to the full directory containing the json files. e.g. in this project, they are stored in the `<MY PATH>/boards-listing-tool/data` folder.

Within the venv, run ```pip install -r requirements.txt```

#### To run app as CLI
To generate the list of boards, run a python shell ```python```

Within the shell,

```
from app import join_board_data

join_board_data()
```

#### To run app as Flask Server
```flask --app boards_listing_tool.main run```

#### To run tests
```pytest tests```

### Tools used
* Stack Overflow
* Library docs (Pydantic, Dotenv)
* Copilot


### Planned extensions
* Complete test cases.
* Handle duplicates - what counts as a duplicate? Case insensitive, all 4 fields the same?
* Containerise the app (likely using Docker) to ensure portability between operating systems.
* Scale: instead of reading from directory each time, load data to DB and read from there
* API docs
