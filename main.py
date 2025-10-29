import requests
import json
import os

#store a url
URL = "https://uselessfacts.jsph.pl/random.json?language=en"

def catch(url):
    #get fact
    response = requests.get(url)
    if response.status_code == 200:
        #load the fact_list or create a empty fact_list
        if(os.path.exists("fact.json")):
            with open("fact.json", "r") as file:
                fact=json.load(file)
        else:
            fact={"fact_list":[]}
        data =response.json()
        #check if new fact has exist
        have_exist= data["text"] in fact["fact_list"]
        #if new has not exist in fact_list, then add in it
        if  not have_exist:
            with open("fact.json", "w") as file:
                fact["fact_list"].append(data["text"])
                json.dump(fact, file)
            print("Successfully add a fact to fact_list!")
            print("Include:", data["text"])
    else:
        print(f"Error: {response.status_code}")
for x in range(3):
    catch(URL)