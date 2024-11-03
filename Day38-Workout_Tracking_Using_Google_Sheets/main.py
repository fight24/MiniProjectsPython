from TrackingApi import Tracking
from SheetApi import SheetApi
import datetime
time = datetime.datetime.today().strftime("%d/%m/%Y %H:%M:%S")
text = input("Tell me which exercise you did: ")
gender = input("Tell me your gender: ")
weight_kg = input("Tell me your weight (kg): ")
height_cm = input("Tell me your height (cm): ")
age =  input("Tell me your age: ")
if text != None and gender != None and weight_kg != None and height_cm != None and age != None:
    tracking = Tracking(exercise_text=text, gender=gender,weight_kg=weight_kg,height_cm=height_cm,age=age)
    response_track = tracking.post.json()
    # print(response_track)
    sheet = SheetApi(date=time.split()[0], time=time.split()[1], exercise=response_track["exercises"][0]["name"], duration=response_track["exercises"][0]["duration_min"], calories=response_track["exercises"][0]["nf_calories"])
    response_sheet = sheet.post
    print(response_sheet)
# response["exercises"][0]["duration_min"]
# response["exercises"][0]["nf_calories"]
# response["exercises"][0]["name"]
print(time.split()[0])
