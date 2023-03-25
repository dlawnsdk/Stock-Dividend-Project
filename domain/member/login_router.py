import requests
from fastapi import APIRouter
from requests.models import Response
router = APIRouter(prefix="/auth")


@router.get('/kakao/callback')
def trylogin(code: str):
    url = "https://kauth.kakao.com/oauth/token"

    data = {
        "grant_type": "authorization_code",
        "client_id": "21a44baa64e55564eb933d9bf7046417",
        "redirect_uri": "http://localhost:8000/auth/kakao/callback",
        "code": code,
        "Content-Type": 'application/x-www-form-urlencoded'
    }
    response = requests.post(url, data=data)

    auth = response.json() # 인가코드
    print("auth", response)
    ACCESS_TOKEN = auth.get('access_token')
    APP_ADMIN_KEY = 'e82932696d90d6236dfcc88b8976bf76'
    data = {
        "Authorization": f'Bearer {ACCESS_TOKEN}',
    }
    resp = Response()
    token = requests.get('https://kapi.kakao.com/v2/user/me', data=data)

    print('test', token)

