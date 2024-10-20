import requests
from Key_Api import Key_Api
from Constant_Enum import Constant_Val
class News:
    def __init__(self, query, from_date, to_date='', sort_by = 'publishedAt', api_key = Key_Api['KEY_NEW'].value):
        self.__q = query
        self.__from = from_date
        if len(to_date) == 0:
            self.__to = from_date
        else:
            self.__to = to_date
        self.__sort = sort_by
        self.__api_key = api_key

    @property
    def query(self):
        return self.__q
    
    @query.setter
    def query(self, q_val):
        if isinstance(q_val, str):
            self.__q = q_val
        else:
            raise ValueError("query must be a string")
    
    def get_sort(self):
        return self.__sort
    
    def set_sort(self, by_value):
        if len(by_value) > 0:
            self.__sort = by_value
        else:
            raise ValueError("The sort value cannot be empty")


    @property
    def from_date(self):
        return self.__from
    
    @from_date.setter
    def from_date(self, from_val):
        if isinstance(from_val, str):
            self.__from = from_val
        else:
            raise ValueError("The date must be a string")
    

    @property
    def to_date(self):
        return self.__to
    
    @to_date.setter
    def to_date(self, to_val):
        if isinstance(to_val, str):
            self.__to = to_val
        else:
            raise ValueError("The date must be a string")


    @property
    def api_key(self):
        return self.__api_key
    
    @api_key.setter
    def api_key(self, api_key_val):
        if isinstance(api_key_val, str):
            self.__to = api_key_val
        else:
            raise ValueError("The Api key must be a string")
    

    def get_request_api(self):
        return requests.get(f"{Constant_Val['NEWS'].value}qInTitle={self.__q}&from={self.__from}&to={self.__to}&sortBy={self.__sort}&apiKey={self.__api_key}").json()
    
    def get_article(self):
        return self.get_request_api()['articles']
    
    def get_three_news_lastest(self):
        return {
                'title': [self.get_article()[i]['title'] for i in range(3)],
                'description': [self.get_article()[i]['description'] for i in range(3)]
                }
    

    
