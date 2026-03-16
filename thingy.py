import json

with open("config.json") as f:
    config = json.load(f)

apikey = config["api-key"]
print(apikey)
