from model import Board
from sqlalchemy.orm import Session
from sqlalchemy import select


async def get_board_list(db: Session):
    board_list = await db.execute(select(Board).order_by(Board.create_date.desc()))
    return board_list.all()