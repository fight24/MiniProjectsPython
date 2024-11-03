import requests
API_ID = "[your_id]"
API_KEY = "[your_key]"
END_POINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
HEADERS = {
    "Content-Type": "application/json",
    "x-app-id": API_ID,
    "x-app-key": API_KEY
}
class Tracking:
    def __init__(self, exercise_text ,gender = None, weight_kg = None, height_cm = None, age = None):
        self.__query = exercise_text
        self.__gender = gender
        self.__weight_kg = weight_kg
        self.__height_cm = height_cm
        self.__age = age
    @property
    def query(self):
        return self.__query
    @query.setter
    def query(self, text):
        if text != '':
            self.__query = text
        else:
            raise ValueError("Text is empty !!!")
    def init_body_json(self):
        return {
                "query": self.__query,
                "gender": self.__gender,
                "weight_kg": self.__weight_kg,
                "height_cm": self.__height_cm,
                "age": self.__age
        }
    
    @property
    def post(self):
        return requests.post(url=END_POINT, headers=HEADERS, json=self.init_body_json())

# if exercise_text != '':
#     try:
#         response = requests.post(url=URL+END_POINT, headers=headers, json=BODY_JSON)
#         print(response.json())
#     except:
#         print("Error")
#     else:
#         print("success!!!")
# else:
#     print("query empty!!!") 