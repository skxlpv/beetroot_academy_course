import json

import requests

url = "https://piano-chords.p.rapidapi.com/chords/csharp"

headers = {
	"x-rapidapi-key": "ecab43ea83msh943f182faeebb41p1a8721jsn2998ecb71566",
	"x-rapidapi-host": "piano-chords.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(json.dumps(response.json(), indent=4))