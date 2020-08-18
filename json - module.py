import json

# json.loads
data = '{"var1":"anindo", "var2": 24}'
parsed = json.loads(data)

print(parsed)
print(parsed['var1'])

# json.dumps
data2 = {
    "Name": "Anindo Dey",
    "Cars": ["BMW", "Audi", "Ferrari"],
    "fridge": ("Rice", 480),
    "isbad": False
}

jscomp = json.dumps(data2)
print(data2)
print(jscomp)