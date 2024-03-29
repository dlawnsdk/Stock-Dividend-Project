from fastapi import APIRouter, Depends, HTTPException
from starlette import status
from starlette.status import HTTP_400_BAD_REQUEST

from database import get_async_db
from sqlalchemy.orm import Session
from domain.board import board_schema, board_crud

# APIRouter 클래스로 생성한 router 객체를 생성하여 FASTApi 앱에 등록해야만 라우팅 기능이 동작한다.
router = APIRouter(prefix="/api/board")


# response_model? pydantic 적용 해당 함수의 리턴 값은 해당 스키마로 구성된 리스트임을 의미
# -> 함수로도 사용 가능( -> list[board_schema.BoardList])
@router.get("/list", response_model=board_schema.BoardList)
async def board_list(db: Session = Depends(get_async_db)):
    board_list = await board_crud.get_board_list(db)
    return {"board_list": board_list}


@router.get("/view/{board_id}", response_model=board_schema.Board)
async def board_view(board_id: int, db: Session = Depends(get_async_db)):
    board = await board_crud.get_board(db, board_id=board_id)
    return board


@router.post("/create", status_code=status.HTTP_204_NO_CONTENT)
async def board_create(params: board_schema.BoardCreate, db: Session = Depends(get_async_db)):
    await board_crud.create_board(db, board_create=params)


@router.put("/update", status_code=status.HTTP_204_NO_CONTENT)
async def board_update(params: board_schema.BoardUpdate, db: Session = Depends(get_async_db)):
    now_board = await board_crud.get_board(db, board_id=params.board_id)
    if not now_board:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="해당 게시글을 찾을 수 없습니다.")

    await board_crud.update_board(db, now_board=now_board, new_board=params)


@router.delete("/delete", status_code=status.HTTP_204_NO_CONTENT)
async def board_delete(params: board_schema.BoardDelete, db: Session = Depends(get_async_db)):
    now_board = await board_crud.get_board(db, board_id=params.board_id)
    if not now_board:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="해당 게시글을 찾을 수 없습니다.")

    await board_crud.delete_board(db, now_board=now_board)
