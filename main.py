import requests
import json

#store a api
url = "https://uselessfacts.jsph.pl/random.json?language=en"

#get a request
response= requests.get(url)

if response.status_code==200:
    data = response.json()
    print("Here is the random fact:", data["text"])
else:
    print(f"Error: {response.status_code}")