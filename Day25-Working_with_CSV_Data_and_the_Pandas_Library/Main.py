# with open("weather_data.csv") as weather_data:
#     print(weather_data.readlines())

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         print(row)
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)
#
#
import pandas

data = pandas.read_csv("weather_data.csv")
# print(data["temp"])
# data_dict = data.to_dict()
# print(data_dict)
# temp_list = data["temp"].to_list()
# print(temp_list)
# # print(sum(temp_list)/len(temp_list))
# print(data["temp"].mean())
# print(data["temp"].max())
# print(data["temp"].min())
#
# # get data in Columns
# # data.temp
# print(data.temp)
# # get data in row
# print(data[data.day == "Monday"])
#
# print(data[data.temp == data.temp.max()])
# monday = data[data.day == "Monday"]
# print(monday.condition)
# print(monday.temp[0] * 9/5 + 32)
# Create a dataframe from scratch
data_dict_stu_score = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data_stu_score = pandas.DataFrame(data_dict_stu_score)
print(data_stu_score)
data_stu_score.to_csv("students_scores_data.csv")
