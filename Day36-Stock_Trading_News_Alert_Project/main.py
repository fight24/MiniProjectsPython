from Stock import Stock
from News import News
from translate import Translator
from Twilio_Class import Twilio_Class
import pytz
import datetime
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
# date_time_now = datetime.datetime.now()
# date_time_now_string = date_time_now.strftime("%Y-%m-%d")
# * handle time
# Khởi tạo đối tượng múi giờ USA (ví dụ, Eastern Time)
usa_timezone = pytz.timezone('US/Eastern')
date_time_today= datetime.datetime.now(usa_timezone)
list_date_time_ago = [(date_time_today - datetime.timedelta(days=i)).strftime("%Y-%m-%d") for i in range(1,3)]
print(list_date_time_ago)

# * request stock api
tesla_stock = Stock(STOCK)
tesla_stock.display_price_close_2_days_ago(list_date_time_ago)
lst_status_n_price = tesla_stock.get_status_and_price_close_2_days_ago(list_date_time_ago)
# * Translage lang
translator = Translator(to_lang='vi')
# print(translator.translate("Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. "))

# * News
info_news = News(COMPANY_NAME, list_date_time_ago[0], list_date_time_ago[1])
response_news = info_news.get_three_news_lastest()
print(response_news)

twilio_obj = Twilio_Class()
twilio_obj.message = (
    f"\n[Stock]\n[TSLA] {lst_status_n_price[0]} {lst_status_n_price[1]}%"
    f"\n[Headline]: {response_news['title'][0]}"
    f"\n[Description]: {response_news['description'][0]}"
    f"\n[{translator.translate('Headline')}]: {translator.translate(response_news['title'][0])}"
    f"\n[{translator.translate('Description')}]: {translator.translate(response_news['description'][0])}"
    )
print(twilio_obj.status)

