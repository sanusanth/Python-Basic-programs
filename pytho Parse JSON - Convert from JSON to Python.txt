import json

# some JSON:
x = '{ "name":"sanu", "age":24, "city":"batticaloa"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])
