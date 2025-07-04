dict1 = {
    "value": 10,
}

dict2 = dict1

print("Before value is updated:")
print("dict1:", dict1)
print("dict2:", dict2)

print("\ndict points to", id(dict1))
print("dict2 points to", id(dict2))

dict1["value"] = 22
dict1["value"] = 44 # Even though we update the value in dict1, dict2 will reflect this change
# because dict2 is a reference to the same dictionary object as dict1.

print("\nAfter value is updated:")
print("dict1:", dict1)
print("dict2:", dict2)


print("\ndict points to", id(dict1))
print("dict2 points to", id(dict2)) # This will still be the same as before since dict2 is a reference to dict1
# Dictionaries are mutable in Python, so when we update the value of dict1,
# dict2 reflects that change because both dict1 and dict2 point to the same dictionary object in memory.
# This is why the value of dict2 also changes when we update dict1.

dict3 = { # A new dictionary object
    "value": 33
}


dict2 = dict3

print("\nAfter value is updated with dict3:")
print("dict1:", dict1)
print("dict2:", dict2)

print("\ndict points to", id(dict3))
print("dict2 points to", id(dict2)) 
# Now dict2 points to a new dictionary object (dict3), so it will not reflect changes made to dict1.

dict1 = dict2
# Now dict1 points to the same dictionary object as dict2 (which is now dict3)
print("\nAfter dict1 is updated to point to dict2:")
print("dict1:", dict1)
print("dict2:", dict2)
print("dict3:", dict3)


print("\ndict points to", id(dict1))
print("dict2 points to", id(dict2))
print("dict3 points to", id(dict3))
# GARBAGE COLLECTION
# value 22 and 44 are not reflected in dict2 anymore and it will be handeld as garbage collection
