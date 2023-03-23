<script>
  import fastapi from "../../lib/api.js"
  import { link } from 'svelte-spa-router'

  window.Kakao.init('21a44baa64e55564eb933d9bf7046417'); // 사용하려는 앱의 JavaScript 키 입력
  function loginWithKakao() {
    window.Kakao.Auth.authorize({
      redirectUri: 'http://localhost:8000/auth/kakao/callback',
    });
  }
</script>

<a id="kakao-login-btn" on:click="{loginWithKakao}">
  <img src="https://k.kakaocdn.net/14/dn/btroDszwNrM/I6efHub1SN5KCJqLm1Ovx1/o.jpg" width="222"
    alt="카카오 로그인 버튼" />
</a>

