import requests
from fastapi import APIRouter
from fastapi.responses import RedirectResponse

from domain.member import login_crud


router = APIRouter(prefix="/auth")


@router.get('/kakao/login')
def agreeList():
    return RedirectResponse('https://kauth.kakao.com/oauth/authorize?response_type=code&client_id=eec0b007a1d0f71c05c99e3130b08d0b&redirect_uri=http://localhost:8000/auth/kakao/callback')


@router.get('/kakao/callback')
def trylogin():
    test=requests.get('https://kauth.kakao.com/oauth/authorize?response_type=code&client_id=eec0b007a1d0f71c05c99e3130b08d0b&redirect_uri=http://localhost:8000/auth/kakao/callback')
    print("동의!!?", test.content.code)
    return test.content