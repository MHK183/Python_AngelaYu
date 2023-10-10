import pandas

# data = pandas.read_csv("weather_data.csv")

# temp_max = data["temp"].max()
# print(temp_max)

# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# print(monday_temp * 9/5 + 32)

# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [75, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])


data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")