import pandas

data = pandas.read_csv("weather_data.csv")
# print(data)
# print(type(data))
# print(data["temp"])
# data_dict = data.to_dict()
# print(data_dict)
#
temp_list = data["temp"].to_list()
# print(temp_list)
print(len(temp_list))
#
# # for average of temperature
# avg = sum(temp_list)/len(temp_list)
# print(avg)
# print(data["temp"].mean())
#
# # for max temp
# print(data["temp"].max())
#
# # get data in column
# print(data["condition"])
# print(data.condition)

# get data in row
# print(data[data.day == "Monday"])

# get the row where temp is max
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)
# monday_temp = monday.temp
# print(monday_temp)
# monday_temp_f = monday_temp * 9/5 + 32
# print(monday_temp_f)