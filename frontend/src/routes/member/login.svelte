<script>
window.Kakao.init(import.meta.env.VITE_KAKAO_CLIENT_KEY);
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

