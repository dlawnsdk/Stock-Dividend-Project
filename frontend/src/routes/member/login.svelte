<script>
  import fastapi from "../../lib/api.js"
  import { link } from 'svelte-spa-router'

  window.Kakao.init('21a44baa64e55564eb933d9bf7046417'); // 사용하려는 앱의 JavaScript 키 입력
  function loginWithKakao() {
    window.Kakao.Auth.authorize({
      redirectUri: 'http://localhost:8000/auth/kakao/callback',
    });
  }

  // 아래는 데모를 위한 UI 코드입니다.
  displayToken()
  function displayToken() {
    var token = getCookie('authorize-access-token');

    if(token) {
     window.Kakao.Auth.setAccessToken(token);
      window.Kakao.Auth.getStatusInfo()
        .then(function(res) {
          if (res.status === 'connected') {
            document.getElementById('token-result').innerText
              = 'login success, token: ' + window.Kakao.Auth.getAccessToken();
          }
        })
        .catch(function(err) {
          window.Kakao.Auth.setAccessToken(null);
        });
    }
  }

  function getCookie(name) {
    var parts = document.cookie.split(name + '=');
    if (parts.length === 2) { return parts[1].split(';')[0]; }
  }
</script>

<a id="kakao-login-btn" on:click="{loginWithKakao}">
  <img src="https://k.kakaocdn.net/14/dn/btroDszwNrM/I6efHub1SN5KCJqLm1Ovx1/o.jpg" width="222"
    alt="카카오 로그인 버튼" />
</a>
<p id="token-result"></p>

