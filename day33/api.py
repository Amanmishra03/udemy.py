import requests

response = requests.get('http://api.open-notify.org/iss-now.json')
# print(response.status_code)
# print(response)

if response.status_code != 200:
    # print('There was an error')
    raise Exception('Bad response from ISS API')