import datetime
from pydantic import BaseModel


# pydantic을 활용하여 데이터 체크를 위한 스키마


class Board(BaseModel):
    id: int
    subject: str
    content: str
    create_date: datetime.datetime

    # DB Model의 항목들이 자동으로 Schema로 매핑된다.
    class Config:
        orm_mode = True


class BoardList(BaseModel):
    board_list: list[Board] = []
