import requests
import datetime
import pytz

timezone_japan = pytz.timezone("asia/tokyo")
# * post sign up acc
TOKEN = "Your_Token"
USERNAME = "Your_name"
habit_pixela_endpoint = 'https://pixe.la/v1/users'
user_params ={
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=habit_pixela_endpoint, json=user_params)
# print(response.text)

# * post: create graph
graph_endpoint = f"{habit_pixela_endpoint}/{USERNAME}/graphs"

graph_header = {
    "X-USER-TOKEN" : TOKEN
}
graph_body_config = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "Hour",
    "type": "int",
    "color": "ajisai",

}
# response = requests.post(url=graph_endpoint, json=graph_body_config, headers=graph_header)
# print(response.text)
# * get a pixel 
# * post: create pixel
pixel_graph_endpoint = f"{graph_endpoint}/{graph_body_config['id']}"

date = datetime.datetime.now(timezone_japan).strftime('%Y%m%d')
print(date)
pixel_body = {
    "date":date,
    "quantity":"5"
    }

# response = requests.post(url=pixel_graph_endpoint, headers=graph_header, json=pixel_body)
# print(response.text)
# * put : update pixel
# * delete: delete pixel
response = requests.delete(url=pixel_graph_endpoint+f"/{date}", headers=graph_header)
print(response.text)