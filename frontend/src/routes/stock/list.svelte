<script>
  import fastapi from "../../lib/api.js"

  let stock_dividend = {}
  let stock_list = {}
  let content
  let keyword

  let search = () => {
      keyword = document.getElementById("keyword").value
      let params = {
          keyword: keyword
      }
      if(keyword === ''){
          alert("키워드를 입력해주세요")
          return false
      }
      fastapi('get', '/api/stock/list', params, (json) => {
          console.log(json[0][0])
          console.log(json[1][0])
          if(json[0] != undefined){

              content.style.display = 'block'
              stock_dividend = json[0][0]
              stock_list = json[1][0]
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
    {#if stock_dividend.stckIssuCmpyNm != undefined}
        <table>
            <tr>
                <th>종목 이름</th>
                <td>{stock_dividend.stckIssuCmpyNm}</td>
            </tr>
            <tr>
                <th>보통주/우선주</th>
                <td>{stock_dividend.scrsItmsKcdNm}</td>
            </tr>
            <tr>
                <th>배당금</th>
                <td>{stock_dividend.stckGenrDvdnAmt}</td>
            </tr>
            <tr>
                <th>발행기관</th>
                <td>{stock_dividend.trsnmDptyDcdNm}</td>
            </tr>
            <tr>
                <th>법인 등록번호</th>
                <td>{stock_dividend.crno}</td>
            </tr>
            <tr>
                <th>주식배당사유코드</th>
                <td>{stock_dividend.stckDvdnRcdNm}</td>
            </tr>
        </table>
    {/if}

    {#if stock_list.itmsNm != undefined}
        <table>
            <tr>
                <th>종목 이름</th>
                <td>{stock_list.itmsNm}</td>
            </tr>
            <tr>
                <th>시장구분</th>
                <td>{stock_list.mrktCtg}</td>
            </tr>
            <tr>
                <th>종가</th>
                <td>{stock_list.clpr}</td>
            </tr>
            <tr>
                <th>시가</th>
                <td>{stock_list.mkp}</td>
            </tr>
            <tr>
                <th>거래량</th>
                <td>{stock_list.trqu}</td>
            </tr>
            <tr>
                <th>시가총액</th>
                <td>{stock_list.mrktTotAmt}</td>
            </tr>
            <tr>
                <th>기준일</th>
                <td>{stock_list.basDt}</td>
            </tr>
        </table>
    {/if}
</div>