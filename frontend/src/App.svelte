<script>
  let board_list = []

  let get_board_list = () => {
    fetch("http://127.0.0.1:8000/api/board/list").then((response) => {
      response.json().then((json) => {

        board_list = json.board_list
      });
    });
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