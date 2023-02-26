from domain.board.board_schema import BoardUpdate
from model import Board
from sqlalchemy.orm import Session
from sqlalchemy import select
from datetime import datetime


async def get_board_list(db: Session):
    board_list = await db.execute(
        select(Board.id, Board.subject, Board.content, Board.create_date).order_by(Board.create_date.desc())
    )
    return board_list.all()


async def get_board(db: Session, board_id: int):
    board = await db.execute(
        select(Board.id, Board.subject, Board.content, Board.create_date).filter(Board.id == board_id)
    )
    return board.all()[0]


async def update_board(db: Session, db_board: Board, board_update: BoardUpdate):
    print("test", board_update.subject)
    print("test2", db_board.subject)
    db_board.subject = board_update.subject
    print("test3", db_board.subject)
    db_board.content = board_update.content
    db_board.update_date = datetime.now()
    db.add(db_board)
    await db.commit()
