'''Nesting means one inside the other for example if we make a dictionary then after 
wrirting key we can write list in the place of value or we can create another dictionary'''
# GENERAL DICTIONARY
capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

# 1.  nesting a list in a dictionary
''' we can not add multiple value in a key so we use list in the dictionary 
in a list we can store multiple value . '''

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin","Hamburg","Stuttgart"],
}

# 2. nesting a dictionary in a dictionary
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"],"total_visited":12},
    "Germany": {"cities_visited": ["Berlin","Hamburg","Stuttgart"],"total_visited":12}
}

# 3. nesting a dictionary in a list  ''' we can insert multiple dictionary in a list.
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
