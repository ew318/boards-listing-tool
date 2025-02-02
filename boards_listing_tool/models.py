from typing import List

from pydantic import BaseModel


class Board(BaseModel):
    name: str
    vendor: str
    core: str
    has_wifi: bool


class Metadata(BaseModel):
    total_vendors: int
    total_boards: int


class BoardList(BaseModel):
    boards: List[Board]
    _metadata: Metadata
