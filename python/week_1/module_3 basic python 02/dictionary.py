# dictionary is key value pair
# dictionary is mutable

person = {
    "name" : "sobuj",
    "age"  : 24,
    "profession" : "student"
}

print(person)
print(person["age"])
print(person.keys())
print(person.values())

# mutable
person["profession"] = "web developer"
print("after mutation: ",person)

# delete
del person["age"]
print("after age deletion: ",person)

# looping
for key,val in person.items():
    print(f"key: {key}  and val: {val}")
