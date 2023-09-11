import pandas
data = pandas.read_csv("weather_data.csv")
print(type(data))
print(data["temp"])
# whole table is a dataframe and a single column is known as series
# data_dict = data.to_dict()
# print(data_dict)

# create a dataframe from scratch
data_dict = {
    "students": ["any", "james", "angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")