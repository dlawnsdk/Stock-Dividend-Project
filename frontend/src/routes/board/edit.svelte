<script>
    import fastapi from "../../lib/api.js"
    import { link } from 'svelte-spa-router'
    import { push } from 'svelte-spa-router'

    export let params = {}
    let board_id = params.board_id
    let subject = ''
    let content = ''

    fastapi("get", "/api/board/view/" + board_id, {}, (json) => {
        subject = json.subject
        content = json.content
    })

    function update_question(event) {
        event.preventDefault()
        let url = "/api/question/update"
        let params = {
            board_id: board_id,
            subject: subject,
            content: content,
        }
        fastapi('put', url, params,
            (json) => {
                push('/board/view/'+ board_id)
            }
        )
    }
</script>
<div class="container">
    <h5 class="my-3 border-bottom pb-2">질문 수정</h5>
    <form method="post" class="my-3">
        <div class="mb-3">
            <label for="subject">제목</label>
            <input type="text" class="form-control" bind:value="{subject}">
        </div>
        <div class="mb-3">
            <label for="content">내용</label>
            <textarea class="form-control" rows="10" bind:value="{content}"></textarea>
        </div>
        <button class="btn btn-primary" on:click="{update_question}">수정하기</button>
    </form>
</div>