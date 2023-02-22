<script>
  import fastapi from "../lib/api"
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
    <a use:link href="/view/{list.id}"><li>{list.subject}</li></a>
  {/each}
</ul>