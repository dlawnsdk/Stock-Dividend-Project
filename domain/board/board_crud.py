from domain.board.board_schema import BoardUpdate
from model import Board
from sqlalchemy.orm import Session
from sqlalchemy import select
from datetime import datetime


async def get_board_list(db: Session):
    board_list = await db.execute(
        select(Board.board_id, Board.subject, Board.content, Board.create_date).order_by(Board.create_date.desc())
    )
    return board_list.all()


async def get_board(db: Session, board_id: int):
    board = await db.execute(
        select(Board.board_id, Board.subject, Board.content, Board.create_date).filter(Board.board_id == board_id)
    )
    return board.all()[0]


async def create_board(db: Session, board_create: Board):
    db_board = Board(subject=board_create.subject, content=board_create.content, create_date=datetime.now())
    db.add(db_board)
    await db.commit()


async def update_board(db: Session, now_board: Board, board_update: BoardUpdate):
    now_board.subject = board_update.subject
    now_board.content = board_update.content
    now_board.update_date = datetime.now()
    db.add(now_board)
    await db.commit()
