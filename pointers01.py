num1 = 11


num2 = num1

print("Beofre num2 value is updated:")
print("num1:", num1)
print("num2:", num2)

print("\nnum1 pointing to:", id(num1))
print("num2 pointing to:", id(num2)) # num2 is a copy of num1, so it has the same id, 
# pointing to the same memory location


num2 = 22
print("\nAfter num2 value is updated:")
print("num1:", num1)
print("num2:", num2)


print("\nnum1 pointing to:", id(num1))
print("num2 pointing to:", id(num2)) # num2 is now a new object, so it has a different id

# integers are immutable in Python, so when we assign num2 = 22,
# it creates a new integer object with the value 22, and num2 now points to this new object.
# num1 still points to the original integer object with the value 11.
# This is why the value of num1 remains unchanged after updating num2.
# In Python, integers are immutable, meaning that when you change the value of an integer,
# you are actually creating a new integer object rather than modifying the original one.
# This is different from mutable objects like lists or dictionaries,
# where changes to the object will reflect in all references to that object.