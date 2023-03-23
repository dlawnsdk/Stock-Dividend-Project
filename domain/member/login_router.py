import requests
from fastapi import APIRouter

router = APIRouter(prefix="/auth")


@router.get('/kakao/callback')
def trylogin(code: str):
    url = "https://kauth.kakao.com/oauth/token"

    data = {
        "grant_type": "authorization_code",
        "client_id": "21a44baa64e55564eb933d9bf7046417",
        "redirect_uri": "http://localhost:8000/auth/kakao/callback",
        "code": code
    }
    response = requests.post(url, data=data)

    tokens = response.json()

    test = requests.get('https://kapi.kakao.com/v2/user/me?data=e82932696d90d6236dfcc88b8976bf76')
    print('test', test.json())

