import numpy as np
from matplotlib import pyplot as plt
from requests.models import Response
import requests


class stock_info:
    def __init__(self, keyword: str, s_date: str, e_date: str):
        self.keyword = keyword
        self.s_date = s_date
        self.e_date = e_date

    def stock_dividend(self):
        url = 'http://apis.data.go.kr/1160100/service/GetStocDiviInfoService/getDiviInfo'
        params = {
            'serviceKey': 'X3EjOtLbzPsZO0sDXdwImY5+EfRe0rrb7O8XtPHRhvjzFNghyIHx+41YK8EZETVdI5qMID3aww6/KDrwAFg9fA==',
            'pageNo': '1', 'resultType': 'json', 'stckIssuCmpyNm': self.keyword
        }

        stock_list: Response = requests.get(url, params=params)  # requests.models.response

        print(stock_list)

        result_length = len(stock_list.json().get('response').get('body').get('items').get('item'))

        result = []
        for i in range(result_length):
            result.append(stock_list.json().get('response').get('body').get('items').get('item')[i])
        return result

    def stock_price(self):

        url = "http://apis.data.go.kr/1160100/service/GetStockSecuritiesInfoService/getStockPriceInfo"
        params = {
            'serviceKey': 'X3EjOtLbzPsZO0sDXdwImY5+EfRe0rrb7O8XtPHRhvjzFNghyIHx+41YK8EZETVdI5qMID3aww6/KDrwAFg9fA==',
            'resultType': 'json', 'itmsNm': self.keyword, 'beginBasDt' : self.s_date, 'endBasDt' : self.e_date
        }

        stock_list: Response = requests.get(url, params=params)  # requests.models.response

        result_length = len(stock_list.json().get('response').get('body').get('items').get('item'))

        result = []
        dataframe = []
        labels = []

        for i in range(result_length):
            result.append(stock_list.json().get('response').get('body').get('items').get('item')[i])
            dataframe.append(stock_list.json().get('response').get('body').get('items').get('item')[i].get('clpr'))
            labels.append(stock_list.json().get('response').get('body').get('items').get('item')[i].get('basDt'))

        print(dataframe)
        dataframe = np.array(dataframe)
        plt.bar(dataframe, height=100, width=1, tick_label=labels, color="darkorange")
        plt.show()

        return result
