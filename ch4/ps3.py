l = []
for i in range(10):
    element = input(f"Enter element {i+1}: ")
    l.append(element)
    
l.sort()
print(F"smallest element in the list is: {l[0]}")
print(F"largest element in the list is: {l[-1]}")
print(F"second largest element in the list is: {l[-2]}")