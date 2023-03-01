<script>
    import fastapi from "../../lib/api.js"
    import { link, push } from 'svelte-spa-router'

    export let params = {}
    let board_id = params.board_id
    let board = {}

    function get_question() {
        fastapi("get", "/api/board/view/" + board_id, {}, (json) => {
            board = json
        })
    }

    let delete_board = (event) => {
        event.preventDefault()
        let params = {
            board_id: board_id
        }
        fastapi("delete", "/api/board/delete", params, (json) => {
            push("/board/list/")
        })
    }

    get_question()
</script>

<h1>{board.subject}</h1>
<div>
    {board.content}
</div>
<div class="my-3">
    <a use:link href="/board/edit/{board.board_id}" class="btn btn-sm btn-outline-secondary">수정</a>
    <button on:click={delete_board} class="btn btn-sm btn-outline-secondary">삭제</button>
</div>
