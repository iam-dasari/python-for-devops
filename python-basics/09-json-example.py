import json

person_json = '{"name":"dasari","age":30,"city":"Guntur"}'

#parse
person_object = json.loads(person_json)
print("Person's age is ",person_object["age"])

#Covert Python Dictionary to JSON string
person_object["age"] = 45
new_person_json = json.dumps(person_object)
print("New Person JSON string: ",new_person_json)
print("Datatype of JSON Dump: ",type(json.dumps(new_person_json)))

x = {
    "name": "Dasari Bullaiah",
    "age": 30,
    "married": True,
    "children": ("Coming soon",),
    "pets": None,
    "cars": [
        {"model": "Maruti Dzire"},
    ]
}
print(json.dumps(x["cars"][0]))
