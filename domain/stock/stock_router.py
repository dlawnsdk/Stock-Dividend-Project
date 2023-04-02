from fastapi import APIRouter

from domain.stock.stock_info import stock_info

router = APIRouter(prefix="/api/stock")


@router.get('/view')
def stock_dividend(keyword: str = ''):
    sotckDividend = stock_info(keyword)
    result = sotckDividend.stock_dividend()

    return result


@router.get('/list')
def stock_information(keyword: str = '', s_date : str = '', e_date : str = ''):
    s_date = s_date.replace('-', '')
    e_date = e_date.replace('-', '')
    print(keyword, s_date, e_date)

    stockInfo = stock_info(keyword, s_date, e_date)
    result = stockInfo.stock_price()

    return result
