from model import Board
from sqlalchemy.orm import Session
from sqlalchemy import select


async def get_board_list(db: Session):
    board_list = await db.execute(
        select(Board.id, Board.subject, Board.content, Board.create_date).order_by(Board.create_date.desc())
    )
    return board_list.all()


async def get_board(db: Session, board_id: int):
    print('1 ', board_id)
    board = await db.execute(
        select(Board.id, Board.subject, Board.content, Board.create_date).filter(Board.id == board_id)
    )
    return board.all()[0]
