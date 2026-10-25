

marks = []
for i in range(6):
    mark = float(input(f"Enter mark for subject {i+1}: "))
    marks.append(mark)
marks.sort()
print(f"Your marks in ascending order are: {marks}")
print(f"sum of your marks is: {sum(marks)}")
print(f"average of your marks is: {sum(marks)/len(marks)}")