from fastapi import APIRouter
import requests


router = APIRouter(prefix="/api/stock")


@router.get('/list')
def stock_list():
    url = 'http://apis.data.go.kr/1160100/service/GetStockSecuritiesInfoService/getStockPriceInfo'
    params = {'serviceKey': 'X3EjOtLbzPsZO0sDXdwImY5+EfRe0rrb7O8XtPHRhvjzFNghyIHx+41YK8EZETVdI5qMID3aww6/KDrwAFg9fA=='}

    test = requests.get(url, params=params)
    print(test.content)
    return {"test", test.content}
