<script>
    import fastapi from "../../lib/api.js"
    import { link } from 'svelte-spa-router'

    export let params = {}
    let board_id = params.board_id
    let board = {}

    function get_question() {
        fastapi("get", "/api/board/view/" + board_id, {}, (json) => {
            board = json
        })
    }

    get_question()
</script>

<h1>{board.subject}</h1>
<div>
    {board.content}
</div>
<div class="my-3"><a use:link href="/board/edit/{board.board_id}" class="btn btn-sm btn-outline-secondary">수정</a></div>
<button>삭제</button>