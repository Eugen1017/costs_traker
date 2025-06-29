import json

with open("expenses.json") as f:
    data = json.load(f)

print(data)