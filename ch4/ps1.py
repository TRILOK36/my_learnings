#for "list" use [] it is mutable(can be changed)
#for "tuple" use () it is immutable(cannot be changed)

fruits = []


while True:
    a = input("Enter name of some fruits:\n")
    fruits.append(a)
    want = input("Want to add more fruits? (yes/no)\n").lower()
    if want == "no":
        break
    
    
b = input("Want to see the list of fruits? (yes/no)\n")
if b == "yes":
    print(fruits)
else:
    print("ok, bye")