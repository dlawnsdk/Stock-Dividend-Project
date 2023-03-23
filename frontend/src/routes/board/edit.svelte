<script>
    import fastapi from "../../lib/api.js"
    import { link } from 'svelte-spa-router'
    import { push } from 'svelte-spa-router'

    export let params = {}
    let board_id = params.board_id
    let subject = ''
    let content = ''

    if(board_id != 'new'){
        fastapi("get", "/api/board/view/" + board_id, {}, (json) => {
            subject = json.subject
            content = json.content

        })
    }

    // 글 생성
    let create_board = (event) => {
        event.preventDefault()
        let params = {
            subject: subject,
            content: content,
        }
        fastapi("POST", "/api/board/create", params, (json) => {
            push('/board/list/')
        }, (json_error) => {
            alert("서버 에러 입니다.")
        })
    }

    // 글 수정
    let update_board = (event) => {
         event.preventDefault()
        let params = {
                board_id: board_id,
                subject: subject,
                content: content,
            }
        fastapi("put", "/api/board/update", params, (json) => {
            push('/board/view/'+board_id)
        }, (json_error) => {
            alert("서버 에러 입니다.")
        })
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
        {#if board_id != 'new'}
            <button class="btn btn-primary" on:click="{update_board}">수정하기</button>
        {:else}
            <button class="btn btn-primary" on:click="{create_board}">등록하기</button>
        {/if}
    </form>
</div>