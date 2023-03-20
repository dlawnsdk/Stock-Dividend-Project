<script>
  import fastapi from "../../lib/api.js"
  import { link } from 'svelte-spa-router'

  let board_list = []
  const REST_API_KEY = 'eec0b007a1d0f71c05c99e3130b08d0b'
  const REDIRECT_URI = 'http://localhost:8000/auth/kakao/callback'

  // fastapi('get', '/api/member/agreeList', {}, (json) => {
  //        board_list = json.board_list
  //    })

  // location.replace('https://accounts.kakao.com/login/?continue=https%3A%2F%2Fkauth.kakao.com%2Foauth%2Fauthorize%3Fresponse_type%3Dcode%26redirect_uri%3Dhttp%253A%252F%252Flocalhost%253A5173%252Fapi%252Fmember%252FtryLogin%26through_account%3Dtrue%26client_id%3Deec0b007a1d0f71c05c99e3130b08d0b#login')

  location.replace('https://kauth.kakao.com/oauth/authorize?response_type=code&client_id=eec0b007a1d0f71c05c99e3130b08d0b&redirect_uri=http://localhost:8000/auth/kakao/callback')
</script>