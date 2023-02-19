from fastapi import APIRouter, Depends
from database import SessionLocal, get_db, get_async_db
from model import Board
from sqlalchemy.orm import Session
from domain.board import board_schema, board_crud


# APIRouter 클래스로 생성한 router 객체를 생성하여 FASTApi 앱에 등록해야만 라우팅 기능이 동작한다.
router = APIRouter(prefix="/api/board")


# response_model? pydantic 적용 해당 함수의 리턴 값은 해당 스키마로 구성된 리스트임을 의미
# -> 함수로도 사용 가능
@router.get("/list")
async def board_list(db: Session = Depends(get_async_db)):
    board_list = await board_crud.get_board_list(db)
    return {'board_list': board_list}
