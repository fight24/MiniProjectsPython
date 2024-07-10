import pandas
data = pandas.read_csv("Central-Park-Squirrel-Census-Squirrel-Data-2018.csv")
data_gray = data[data["Primary Fur Color"] == "Gray"]
data_cinnamon = data[data["Primary Fur Color"] == "Cinnamon"]
data_black = data[data["Primary Fur Color"] == "Black"]
print(len(data_gray))
print(len(data_cinnamon))
print(len(data_black))
fur_color_count_dict = {
    "fur color": ["Gray", "Black", "Cinnamon"],
    "Count": [len(data_gray), len(data_black), len(data_cinnamon)]
}
new_data = pandas.DataFrame(fur_color_count_dict)
print(new_data)
new_data.to_csv("squirrel_count.csv")
