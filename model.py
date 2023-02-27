from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

# 데이터베이스를 처리하기 위한 모델 클래스 => 테이블 생성 역할
"""
* pip install alembic
* alembic init migrations
  1. alembic.ini 수정
  2. env.py 수정
* alembic revision --autogenerate
* alembic upgrade head
"""


class Board(Base):
    __tablename__ = "board"

    board_id = Column(Integer, primary_key=True)
    subject = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)
    update_date = Column(DateTime, nullable=True)


class Reply(Base):
    __tablename__ = "reply"

    reply_id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)
    board_id = Column(Integer, ForeignKey("board.board_id"))
    board = relationship("Board", backref="replylist")
