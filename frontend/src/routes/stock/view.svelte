<script>
    import fastapi from "../../lib/api.js"

    export let params = {}
    let keyword = params.keyword
    let stock_view = {}

    function get_stock_dividend() {
        params = {
            keyword: keyword
        }
        fastapi('get', '/api/stock/view', params, (json) => {
          if(json[0] != undefined){
                stock_view = json[0]
          }
        })
    }
    get_stock_dividend()
</script>

 {#if stock_view.stckIssuCmpyNm != undefined}
        <table>
            <tr>
                <th>종목 이름</th>
                <td>{stock_view.stckIssuCmpyNm}</td>
            </tr>
            <tr>
                <th>보통주/우선주</th>
                <td>{stock_view.scrsItmsKcdNm}</td>
            </tr>
            <tr>
                <th>배당금</th>
                <td>{stock_view.stckGenrDvdnAmt}</td>
            </tr>
            <tr>
                <th>발행기관</th>
                <td>{stock_view.trsnmDptyDcdNm}</td>
            </tr>
            <tr>
                <th>법인 등록번호</th>
                <td>{stock_view.crno}</td>
            </tr>
            <tr>
                <th>주식배당사유코드</th>
                <td>{stock_view.stckDvdnRcdNm}</td>
            </tr>
        </table>
    {/if}