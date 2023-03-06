from fastapi import APIRouter
import requests
from requests import Response
from requests.models import Response
resp = Response()


router = APIRouter(prefix="/api/stock")


@router.get('/list')
def stock_list(keyword: str = ''):
    url = 'http://apis.data.go.kr/1160100/service/GetStocDiviInfoService/getDiviInfo'
    params = {'serviceKey': 'X3EjOtLbzPsZO0sDXdwImY5+EfRe0rrb7O8XtPHRhvjzFNghyIHx+41YK8EZETVdI5qMID3aww6/KDrwAFg9fA==', 'pageNo' : '1', 'numOfRows' : '1', 'resultType' : 'json', 'stckIssuCmpyNm' : keyword }

    stock_list: Response = requests.get(url, params=params) # requests.models.response

    result_length = len(stock_list.json().get('response').get('body').get('items').get('item'))

    result = {}

    for i in range(result_length):
        result[i] = stock_list.json().get('response').get('body').get('items').get('item')[i]

    return result
