import datetime
from pydantic import BaseModel, validator


# pydantic을 활용하여 데이터 체크를 위한 스키마


class Board(BaseModel):
    board_id: int
    subject: str
    content: str
    create_date: datetime.datetime
    update_date: datetime.datetime | None = None

    # DB Model의 항목들이 자동으로 Schema로 매핑된다.
    class Config:
        orm_mode = True


class BoardCreate(BaseModel):
    subject: str
    content: str

    @validator('subject', 'content')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v


class BoardUpdate(BoardCreate):
    board_id: int


class BoardList(BaseModel):
    board_list: list[Board] = []
