<script>
  import fastapi from "../../lib/api.js"

  let stock_list = {}
  let content


  let search = () => {
      let params = {
          keyword: document.getElementById("keyword").value
      }
      fastapi('get', '/api/stock/list', params, (json) => {
          if(json[0] != undefined){
              content.style.display = 'block'
              stock_list = json[0]
          }else{
              content.style.display = 'none'
          }
      })
  }

</script>

<input type="text" id="keyword"><button on:click={search}>검색</button>
    <!-- Object 반복문 -->
    <!-- {#each Object.entries(stock_list) as [key, value], idx}-->
    <!--     <div>{key}: {value}</div> &lt;!&ndash; 키와 값 출력 &ndash;&gt;-->
    <!--{/each}-->
<div bind:this={content}>
{#if stock_list.isinCdNm != undefined}
    <table>
        <tr>
            <th>종목 이름</th>
            <td>{stock_list.stckIssuCmpyNm}</td>
        </tr>
        <tr>
            <th>보통주/우선주</th>
            <td>{stock_list.scrsItmsKcdNm}</td>
        </tr>
        <tr>
            <th>배당금</th>
            <td>{stock_list.stckGenrDvdnAmt}</td>
        </tr>
        <tr>
            <th>발행기관</th>
            <td>{stock_list.trsnmDptyDcdNm}</td>
        </tr>
        <tr>
            <th>법인 등록번호</th>
            <td>{stock_list.crno}</td>
        </tr>
        <tr>
            <th>주식배당사유코드</th>
            <td>{stock_list.stckDvdnRcdNm}</td>
        </tr>
    </table>
{/if}
    </div>