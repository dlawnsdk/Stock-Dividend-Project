<script>
  import fastapi from "../../lib/api.js"
  import { link } from 'svelte-spa-router'

  let stock_list = []
  let content
  let keyword
  let s_date
  let e_date

  let search = () => {
      keyword = document.getElementById("keyword").value
      s_date = document.getElementById("s_date").value
      e_date = document.getElementById("e_date").value
      let params = {
          keyword: keyword,
          s_date : s_date,
          e_date : e_date
      }
      if(keyword === ''){
          alert("키워드를 입력해주세요")
          return false
      }
      fastapi('get', '/api/stock/list', params, (json) => {

          if(json[0] != undefined){

              // content.style.display = 'block'
               stock_list = json
          }
      })
  }

  let graph = () => {
       let params = {
          keyword: keyword,
          s_date : s_date,
          e_date : e_date
      }
      fastapi('get', '/api/stock/graph', params, (json) => {

      })
  }

</script>

<input type="text" id="keyword"><button on:click={search}>검색</button>
    <!-- Object 반복문 -->
    <!-- {#each Object.entries(stock_list) as [key, value], idx}-->
    <!--     <div>{key}: {value}</div> &lt;!&ndash; 키와 값 출력 &ndash;&gt;-->
    <!--{/each}-->
<input type='date' name='s_date' id="s_date"/>
<input type='date' name='e_date' id="e_date"/>
<div bind:this={content}>
    <table>
      <colgroup>
        <col width="70%"/>
        <col width="10%"/>
        <col width="20%"/>
      </colgroup>
        <thead>
            <tr>
                <th>
                    종목이름
                </th>
                <th>
                    종가
                </th>
                <th>
                    기준일
                </th>
            </tr>
        </thead>
        {#each stock_list as list}
            <tr>
                <td><a use:link href="/stock/view/{list.itmsNm}/{list.basDt}">{list.itmsNm}</a></td>
                <td>{list.clpr}</td>
                <td>{list.basDt}</td>
            </tr>
        {/each}

        {#if stock_list.length != 0}
            <button on:click={graph}>그래프 보기</button>
        {/if}
    </table>
</div>