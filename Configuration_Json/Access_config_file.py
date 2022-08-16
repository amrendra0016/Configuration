import json

# Reading Json File
with open("config.json", "r") as jsonfile:
    data = json.load(jsonfile)


# Accessing values from config.json file
print(data)
print(data['kafka_project'])
print("Kafka Project Path =", data['kafka_project'])

# Updating values of json file
data['age']=27

myJson=json.dumps(data)
with open("config.json", "w") as jsonfile:
    jsonfile.write(myJson)

with open("config.json", "r") as jsonfile:
    data = json.load(jsonfile)

data["NRI"]="False"
data["Salary"]=21.46

"""Here, unlike json.dumps(), we need not serialize python object to JSON string.
Instead, json.dump() method directly stores the python object as a JSON formatted data into the JSON file."""
with open("config.json", "w") as jsonfile:
    json.dump(data,jsonfile)

with open("config.json", "r") as jsonfile:
    data = json.load(jsonfile)
print(data['NRI'])