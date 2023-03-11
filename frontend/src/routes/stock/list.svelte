<script>
  import fastapi from "../../lib/api.js"

  let stock_list = []
  let stock_dividend = {}
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

          if(json[0] != undefined){
              // content.style.display = 'block'
              stock_list = json
          }
      })
  }

  let stock_view = (company_name) => {
      let params = {
        company_name: company_name
      }
      fastapi('get', '/api/stock/view', params, (json) => {
          console.log(json[0])
          if(json[0] != undefined){
                stock_dividend = json[0]
              console.log(stock_dividend)
          }else{

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
    <!--{#if stock_dividend.stckIssuCmpyNm != undefined}-->
    <!--    <table>-->
    <!--        <tr>-->
    <!--            <th>종목 이름</th>-->
    <!--            <td>{stock_dividend.stckIssuCmpyNm}</td>-->
    <!--        </tr>-->
    <!--        <tr>-->
    <!--            <th>보통주/우선주</th>-->
    <!--            <td>{stock_dividend.scrsItmsKcdNm}</td>-->
    <!--        </tr>-->
    <!--        <tr>-->
    <!--            <th>배당금</th>-->
    <!--            <td>{stock_dividend.stckGenrDvdnAmt}</td>-->
    <!--        </tr>-->
    <!--        <tr>-->
    <!--            <th>발행기관</th>-->
    <!--            <td>{stock_dividend.trsnmDptyDcdNm}</td>-->
    <!--        </tr>-->
    <!--        <tr>-->
    <!--            <th>법인 등록번호</th>-->
    <!--            <td>{stock_dividend.crno}</td>-->
    <!--        </tr>-->
    <!--        <tr>-->
    <!--            <th>주식배당사유코드</th>-->
    <!--            <td>{stock_dividend.stckDvdnRcdNm}</td>-->
    <!--        </tr>-->
    <!--    </table>-->
    <!--{/if}-->
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
            <tr on:click={() => stock_view(list.itmsNm)}>
                <td>{list.itmsNm}</td>
                <td>{list.clpr}</td>
                <td>{list.basDt}</td>
            </tr>
            <tr>
                {#each Object.entries(stock_dividend) as [key, value], idx}-->
                    <div>{key}: {value}</div> <!-- 키와 값 출력 -->
                {/each}
            </tr>
        {/each}
    </table>
</div>