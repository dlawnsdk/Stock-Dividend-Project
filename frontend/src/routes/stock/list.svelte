<script>
  import fastapi from "../../lib/api.js"
  import { link } from 'svelte-spa-router'

  let stock_list = {}



  let search = () => {
      let params = {
          keyword: document.getElementById("keyword").value
      }
      fastapi('get', '/api/stock/list', params, (json) => {
          if(json[0] != undefined){
              stock_list = json[0]
          }
      })
  }

</script>

<input type="text" id="keyword"><button on:click={search}>검색</button>

     {#each Object.entries(stock_list) as [key, value], idx}
         <div>{key}: {value}</div> <!-- 키와 값 출력 -->
    {/each}
