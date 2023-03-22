import requests
import json

from starlette.responses import RedirectResponse

# HTTP / 1.1
# Host: kauth.kakao.com

REST_API_KEY = 'eec0b007a1d0f71c05c99e3130b08d0b'
REDIRECT_URI = 'http://localhost:5173/api/member/tryLogin'


class Oauth:

    def __init__(self):
        print("test")

    def agreeList(self):
        url = 'https://kauth.kakao.com/oauth/authorize'
        rest_api_key = 'eec0b007a1d0f71c05c99e3130b08d0b'
        redirect_uri = 'http://localhost:5173/api/member/tryLogin'  # APP에서 등록한 redirect_url
        # authorize_code = 'D-Ov8OvTfjXO89juxIwFUZPd4URawIZ9RLQqc_jVlnpGbeGIa3wE8qwt1H3HdNYXQygSlQoqJZEAAAGG94TxPg#/member/login'

        data = {
            # 'grant_type': 'authorization_code',
            'client_id': rest_api_key,
            'redirect_uri': redirect_uri,
            'response_type': 'code'
            # 'code': authorize_code
        }

        RedirectResponse(f'https://kauth.kakao.com/oauth/authorize?response_type=code&client_id=eec0b007a1d0f71c05c99e3130b08d0b&redirect_uri=http://localhost:8000/auth/kakao/callback')
        # tokens = response.json()
        # print(tokens)
