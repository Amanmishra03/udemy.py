import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(data)
# data_dict = data.to_dict()
# gray_squirrel = data[data["Primary Fur Color"] == "Gray"]
# print(gray_squirrel)

gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
print(gray_squirrel_count)

red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(red_squirrel_count)

Black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
print(Black_squirrel_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrel_count, red_squirrel_count, Black_squirrel_count]
}
print(data_dict)
# df = pandas.DataFrame(data_dict)
# df.to_csv("squirrel_count.csv")