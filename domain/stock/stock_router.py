from fastapi import APIRouter

from domain.stock.stock_info import stock_info
from domain.stock.stock_info import stock_dividend2

router = APIRouter(prefix="/api/stock")


@router.get('/list')
def stock_information(keyword: str = '', s_date : str = '', e_date : str = ''):
    s_date = s_date.replace('-', '')
    e_date = e_date.replace('-', '')
    print(keyword, s_date, e_date)

    stockInfo = stock_info(keyword, s_date, e_date)
    result = stockInfo.stock_price()

    return result


@router.get('/graph')
def stock_information(keyword: str = '', s_date : str = '', e_date : str = ''):
    s_date = s_date.replace('-', '')
    e_date = e_date.replace('-', '')
    print(keyword, s_date, e_date)

    stockInfo = stock_info(keyword, s_date, e_date)
    result = stockInfo.stock_graph()

    return result


@router.get('/view')
def stock_dividend(keyword: str = '', baseDt : str = ''):
    print(keyword, baseDt)

    sotckDividend = stock_dividend2(keyword, baseDt)
    result = sotckDividend.stock_info()
    print(result)
    return result



