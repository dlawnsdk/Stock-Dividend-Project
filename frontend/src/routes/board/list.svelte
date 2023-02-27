<script>
  import fastapi from "../../lib/api.js"
  import { link } from 'svelte-spa-router'

  let board_list = []

  let get_board_list = () => {
    fastapi('get', '/api/board/list', {}, (json) => {
           board_list = json.board_list
       })
  }

  get_board_list()
</script>

<ul>
  {#each board_list as list}
    <a use:link href="/board/view/{list.board_id}"><li>{list.subject}</li></a>
  {/each}
</ul>
<div class="my-3"><a use:link href="/board/edit/new" class="btn btn-sm btn-outline-secondary">등록</a></div>