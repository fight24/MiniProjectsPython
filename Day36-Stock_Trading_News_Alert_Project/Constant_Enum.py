from enum import Enum

class Constant_Val(Enum):
    HOST_STOCK = "www.alphavantage.co"
    STOCK = "https://"+HOST_STOCK+"/query"
    FUNC = "TIME_SERIES_DAILY"
    NEWS = "https://newsapi.org/v2/everything?"
    STOCK_2 = "https://alpha-vantage.p.rapidapi.com/query"
    HOST_RAP = "alpha-vantage.p.rapidapi.com"


