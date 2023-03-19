from requests.models import Response
import requests


class stock_info:
    def __init__(self, keyword: str):
        self.keyword = keyword

    def stock_dividend(self):
        url = 'http://apis.data.go.kr/1160100/service/GetStocDiviInfoService/getDiviInfo'
        params = {
            'serviceKey': 'X3EjOtLbzPsZO0sDXdwImY5+EfRe0rrb7O8XtPHRhvjzFNghyIHx+41YK8EZETVdI5qMID3aww6/KDrwAFg9fA==',
            'pageNo': '1', 'resultType': 'json', 'stckIssuCmpyNm': self.keyword
        }

        stock_list: Response = requests.get(url, params=params)  # requests.models.response

        result_length = len(stock_list.json().get('response').get('body').get('items').get('item'))

        result = []
        for i in range(result_length):
            result.append(stock_list.json().get('response').get('body').get('items').get('item')[i])
        return result

    def stock_price(self):

        url = "http://apis.data.go.kr/1160100/service/GetStockSecuritiesInfoService/getStockPriceInfo"
        params = {
            'serviceKey': 'X3EjOtLbzPsZO0sDXdwImY5+EfRe0rrb7O8XtPHRhvjzFNghyIHx+41YK8EZETVdI5qMID3aww6/KDrwAFg9fA==',
            'pageNo': '1', 'resultType': 'json', 'likeItmsNm': self.keyword
        }

        stock_list: Response = requests.get(url, params=params)  # requests.models.response

        result_length = len(stock_list.json().get('response').get('body').get('items').get('item'))
        result = []
        for i in range(result_length):
            result.append(stock_list.json().get('response').get('body').get('items').get('item')[i])

        return result
