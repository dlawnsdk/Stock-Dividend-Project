<script>
  import fastapi from "../../lib/api.js"
  import { link } from 'svelte-spa-router'

  let stock_list = {}

  fastapi('get', '/api/stock/list', {}, (json) => {
        console.log(json[0])
         stock_list = json
     })

</script>

<ul>
     {#each Object.entries(stock_list) as [key, value], idx}
         <li>>{idx+1}: {value}</li> <!-- 키와 값 출력 -->
    {/each}
</ul>
