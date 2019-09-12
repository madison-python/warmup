items = [
    {"id": 33, "name": "bob"},
    {"id": 44, "name": "uncle"},
    {"id": 55, "name": "joe"},
    {"id": 66, "name": "uncle"},
]
print(next((item for item in items if item["name"] == "uncle"), None))
print(next((item for item in items if item["name"] == "jim"), None))
