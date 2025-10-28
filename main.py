import requests
import json

#store a api
url = "https://jsonplaceholder.typicode.com/users/1"

#get a request
response= requests.get(url)

print(response.json())