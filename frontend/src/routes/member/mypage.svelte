<script>
  import fastapi from "../../lib/api.js"
  import {location, querystring} from 'svelte-spa-router'


  let searchParams = new URLSearchParams($querystring);
  let user_email = searchParams.get('user_email')
  alert('로그인에 성공하였습니다.'+ user_email)
</script>


