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