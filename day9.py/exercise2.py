travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visited":12
    },
    {
        "country": "Germany", 
        "cities_visited": ["Berlin","Hamburg","Stuttgart"],
        "total_visited":12
    },
]

'''Without touching above code we have to add a dictionary in the above code.'''
'''add_new_country("Russia",2,["moscow", "saint_petersburg"]
print(travel_log)  '''

def add_new_country (country_visited, times_visited, cities_visited ):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visited"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)


add_new_country("Russia",2,["moscow", "saint_petersburg"])
print(travel_log)
    
    