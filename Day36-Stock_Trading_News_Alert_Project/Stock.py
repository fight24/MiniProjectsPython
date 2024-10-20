import requests
from requests.exceptions import HTTPError, Timeout, RequestException
from Constant_Enum import Constant_Val
from Key_Api import Key_Api
class Stock:
    """Summary:
    Using request of HTTP to Get API of stock

    Returns:
        dict: return infomation to know price close of stock
    """
    def __init__(self,symbol=None, link_val = Constant_Val['STOCK'].value, func = Constant_Val['FUNC'].value, api_key = Key_Api['KEY_ALPHA_VANTAGE'].value):
        self.__symbol = symbol
        self.__func = func
        self.__link = link_val
        self.__api_key = api_key
        self.__query = None
        self.__header = None
        print("Check: "+self.__link)
       
    def get_url(self):
        # print(f"{self.__link}?function={self.__func}&symbol={self.__symbol}&apikey={self.__api_key}")
        return f"{self.__link}?function={self.__func}&symbol={self.__symbol}&apikey={self.__api_key}"

    @property
    def symbol(self):
        return self.__symbol
    @symbol.setter
    def symbol(self, symbol_val):
        if isinstance(symbol_val, str):
            self.__symbol = symbol_val
        else:
            raise ValueError("Symbol must be a string")
        

    @property
    def func(self):
        return self.__func
    @symbol.setter
    def func(self, func_val):
        if isinstance(func_val, str):
            self.__symbol = func_val
        else:
            raise ValueError("func must be a string")
        
    
    @property
    def api_key(self):
        return self.__api_key
    @symbol.setter
    def api_key(self, api_key_val):
        if isinstance(api_key_val, str):
            self.__api_key = api_key_val
        else:
            raise ValueError("api_key must be a string")
    
        
    def get_response(self):
        return requests.get(self.get_url(), params=self.__query, headers=self.__header)
    
    def get_data_time_series(self):
        return self.get_response().json()["Time Series (Daily)"]
        
    def get_value_2_days_ago(self, lst_date):
        lst = []
        for date in lst_date:
            #print(date)
            lst.append(self.get_data_time_series()[date])
        return lst
    
    def handle_value_close(self, close_a, close_b):
        return["🔺", round(100*((float(close_a) - float(close_b)) / float(close_a)), 2) ] if float(close_a) > float(close_b) else ["🔻", round(100*((float(close_b) - float(close_a)) / float(close_b)), 2) ]
    
    def display_price_close_2_days_ago(self, lst_date):
        """_summary_
            Show price close and status
        Args:
            lst_date (list): _two_ _days_ _ago_
        """
        lst_date_2_days_ago = self.get_value_2_days_ago(lst_date)
        print(self.handle_value_close(lst_date_2_days_ago[0]['4. close'], lst_date_2_days_ago[1]['4. close']))
    
    def get_status_and_price_close_2_days_ago(self, lst_date):
        lst_date_2_days_ago = self.get_value_2_days_ago(lst_date)
        return self.handle_value_close(lst_date_2_days_ago[0]['4. close'], lst_date_2_days_ago[1]['4. close'])
    

    def set_query(self, outputsize = "compact", data_type = "json"):
        self.__query = {
            "function":self.__func,"symbol":self.__symbol,"outputsize":outputsize,"datatype":data_type
            }
    
    def set_header(self, key = Key_Api["KEY_RAPIDAPI"].value, host = Constant_Val["HOST_RAP"].value):
        self.__header = {
            "x-rapidapi-key": key,
	        "x-rapidapi-host": host
        }