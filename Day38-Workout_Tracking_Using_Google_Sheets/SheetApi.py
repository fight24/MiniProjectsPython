import requests

END_POINT = '[your_end_point]'
API_KEY = '[your_key]'
URL = 'https://api.sheety.co/'+ API_KEY + END_POINT
HEADER = {"[your_auth]": "[your_auth]"}

class SheetApi:
    def __init__(self, date, time, exercise, duration, calories):
        self.__body  = {
        "trangTính1": {
                "date": date,
                "time": time,
                "exercise": exercise,
                "duration": duration,
                "calories": calories
    }
}
    
    @property
    def get(self):
        return requests.get(url=URL, headers=HEADER)
    @property
    def body(self):
        return self.__body
    @body.setter
    def body(self, body_dict):
        """_summary_ Method sets value of body 
        Args:
            body_dict (_dict_): _This parameter has  date, time, exercise,Duration, calories_
        """
        if body_dict != None:
            self.__body = body_dict
    @property
    def post(self):
        response = requests.post(url=URL, headers=HEADER, json=self.__body)
        print(response.status_code)  # Kiểm tra mã lỗi
        print(response.text)         # Kiểm tra thông báo lỗi chi tiết
        return response
        
# response = requests.get(url= URL ).json()

# print(response)
