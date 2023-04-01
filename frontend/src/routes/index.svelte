<script>
    import { link } from 'svelte-spa-router'

    console.log(sessionStorage.getItem("sessionData"))

</script>
<div>
    <h1>메인페이지</h1>
    <a use:link href="/board/list/">게시판</a>
    <a use:link href="/stock/list">배당주식</a>
    <a use:link href="/member/login">로그인</a>
</div>
