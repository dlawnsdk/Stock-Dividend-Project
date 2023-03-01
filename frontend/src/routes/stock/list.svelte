<script>
  import fastapi from "../../lib/api.js"
  import { link } from 'svelte-spa-router'

  let stock_list = ''

  fastapi('get', '/api/stock/list', {}, (json) => {
        console.log(json)
         stock_list = json
     })

</script>

<ul>
    {stock_list}
</ul>
<div class="my-3"><a use:link href="/board/edit/new" class="btn btn-sm btn-outline-secondary">등록</a></div>