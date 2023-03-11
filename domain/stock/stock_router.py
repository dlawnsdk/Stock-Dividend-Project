from fastapi import APIRouter

from domain.stock.stock_info import stock_info

router = APIRouter(prefix="/api/stock")


@router.get('/view')
def stock_dividend(company_name: str = ''):
    sotckDividend = stock_info()
    result = sotckDividend.stock_dividend(company_name)

    return result


@router.get('/list')
def stock_information(keyword: str = ''):
    stockInfo = stock_info()
    result = stockInfo.stock_price(keyword)

    return result
