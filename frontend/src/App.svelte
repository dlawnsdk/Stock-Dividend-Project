

<script>
  import Router from 'svelte-spa-router'
  import index from "./routes/index.svelte"
  import list from "./routes/board/list.svelte"
  import view from "./routes/board/view.svelte"
  import edit from "./routes/board/edit.svelte"
  import stock_list from "./routes/stock/list.svelte"
  import stock_view from "./routes/stock/view.svelte"
  import login from "./routes/member/login.svelte"

  const routes = {
    '/': index,
    '/member/login': login,
    '/board/list/': list,
    '/board/view/:board_id': view,
    '/board/edit/:board_id': edit,
    '/stock/list': stock_list,
    '/stock/view/:keyword/:baseDt': stock_view,
  }
</script>
<Router {routes}/>
