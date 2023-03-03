<script>
  import fastapi from "../../lib/api.js"
  import { link } from 'svelte-spa-router'

  let stock_list = {}

  fastapi('get', '/api/stock/list', {}, (json) => {
         stock_list = json[0]
        console.log(stock_list)
     })

</script>

<ul>
     {#each Object.entries(stock_list) as [key, value], idx}
         <li>>{key}: {value}</li> <!-- 키와 값 출력 -->
    {/each}
</ul>
