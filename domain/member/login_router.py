from fastapi.responses import HTMLResponse
import requests
from fastapi import APIRouter, status
router = APIRouter(prefix="/auth")

@router.get('/kakao/callback', status_code=status.HTTP_200_OK)
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

    auth = response.json()  # 인가코드
    ACCESS_TOKEN = auth.get('access_token')
    # 인가코드로 사용자 정보 조회
    token = requests.get('https://kapi.kakao.com/v2/user/me', headers={"Authorization": f'Bearer {ACCESS_TOKEN}'})
    login_success_fail = token.status_code == 200
    print('로그인 성공여부', login_success_fail)
    print('유저 정보', token.json().get('kakao_account'))
    email = token.json().get('kakao_account').get('email')
    html_content = f"""
           <script>
               alert('로그인 성공')           
               let sessionData = "userInfo"
               sessionStorage.setItem('sessionData', '{email}')    
               console.log(sessionStorage.getItem("sessionData"))
           </script>
           <body>
            {email}님 환영합니다.
            <button><a href="/">메인화면</a></button>
           </body>
           """
    return HTMLResponse(content=html_content, status_code=200)