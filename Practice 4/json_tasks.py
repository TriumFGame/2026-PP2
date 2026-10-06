import json

data = {"name": "Yerkhan", "age": 20, "city": "Almaty"}
json_string = json.dumps(data, indent=4)
print(json_string)

with open('sample-data.json', 'r', encoding='utf-8') as file:
    parsed_data = json.load(file)
    print(parsed_data)