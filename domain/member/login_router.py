
from fastapi import APIRouter
from domain.member import login_crud


router = APIRouter(prefix="/api/member")


@router.get('/agreeList')
def agreeList():
    agreeList = login_crud.Oauth()
    result = agreeList.agreeList()
    print(result)


@router.get('/tryLogin')
def trylogin():
    print("동의!!")