<script>
    import fastapi from "../lib/api"

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