a={
    "name":"EMC",
    "Tutorial":"Python",
    "District":606703

}
print(a)
print(a.keys())
print(a.values())
#Modifying the dict:
a["District"]=606709
print(a)
#Adding new key & value pair:
a["locality"]="Melpallipattu"
print(a) 
#update the dict
a.update({"District":606704})
print(a)
#delete operation in dict
a.pop("name")
print(a)
#Another Method
del a["Tutorial"]
print(a)
#To clear the dictionary
a.clear()
print(a)
#To delete the complete dictionary:
del(a)
print(a)


