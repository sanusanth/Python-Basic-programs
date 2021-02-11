import json

# a Python object (dict):
x = {
  "name": "sanu",
  "age": 24,
  "city": "batticaloa"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)
