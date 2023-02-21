<script>
  import fastapi from "../lib/api"

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
    <li>{list.id}</li>
    <li>{list.subject}</li>
    <li>{list.create_date}</li>
  {/each}
</ul>