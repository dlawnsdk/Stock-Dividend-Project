from fastapi import APIRouter

from domain.stock.stock_info import stock_info

router = APIRouter(prefix="/api/stock")


@router.get('/list')
def stock_list(keyword: str = ''):
    final = []
    sotckInfo = stock_info()
    result = sotckInfo.stock_dividend(keyword)

    stockPrice = stock_info()
    result2 = stockPrice.stock_price(keyword)

    final.append(result)
    final.append(result2)

    return final
