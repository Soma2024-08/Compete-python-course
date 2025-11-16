# Dictionary: 
# it is a built-in data type used in python to data in key-value pairs
# it is unordet, mutable(changable)
# Each key is unique and maps to value
# If we create a dictionary with duplicate key with multiple times , the last occcurance of that key and its associated value will overwrite
# 



Student= { "name": "Soma Samanta",
          "city" :"Tamluk",
          "roll No":"2411mc18",
          "age":25,
          "name":"Sumi" # last occurance will store
          }

print(type(Student))
print(Student)

Student["favSubject"]="Deep Learning"
print(Student)

# update existing value
Student["city"]="West Bengal"  
print(Student["city"])

# removing item
Student.pop("city")
print(Student)

# methods
print(Student.keys())
print(Student.values())
print(Student.items())
print(Student.get("name"))
Student.update({"Country": "India","Hobby":"Photography"})
print(Student)
