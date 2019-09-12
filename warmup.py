def find_first_match(items, name, default=None):
    return next((item for item in items if item["name"] == name), default)

items = [
    {"id": 33, "name": "bob"},
    {"id": 44, "name": "uncle"},
    {"id": 55, "name": "joe"},
    {"id": 66, "name": "uncle"},
]
print(find_first_match(items, "uncle"))
print(find_first_match(items, "jim"))
