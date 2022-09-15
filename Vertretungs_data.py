# Imports
from datetime import date
import dsbapi
import json

# Get configuration.json
with open("configuration.json", "r") as config:
    data = json.load(config)
    username = data["username"]
    password = data["password"]
    
# Get API Data
dsbclient = dsbapi.DSBApi(username, password)
entries = dsbclient.fetch_entries()

# Data Sorting


# Output
for entry in entries:
    for item in entry:
        #new_teacher = 
        Klasse = item['type']
        Datum = item['date']
        Tag = item['day']
        output = Tag + ', den', Datum, ': ', Klasse
        print(output)
# '---' means None

