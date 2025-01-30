# Demonstrates requests. Create code to connect to API like yoa browzer yourself
import json # Demonstrates JSON
import sys
import requests

if len(sys.argv) != 2:
    sys.exit()

response = requests.get(
    "https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1]
)
o = response.json()
for result in o ["results"]:
    print(result["trackName"])

# print(json.dumps(response.json(), indent=2)) #print data in redable format!!!
