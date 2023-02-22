<script>
  import Router from 'svelte-spa-router'
  import Home from "./routes/Home.svelte"
  import Detail from "./routes/Detail.svelte"

  const routes = {
    '/': Home,
    '/view/:board_id': Detail
  }
</script>
<Router {routes}/>