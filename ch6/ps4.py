
a = {}
d= int(input("Enter the number of subjects:\n"))


for i in range(d):
    subject = input("Enter subject name: ")
    mark = int(input("Enter marks: "))
    a[subject] = mark

if any(mark < 0 or mark > 100 for mark in a.values()):
    print("Invalid marks! Marks must be between 0 and 100.")
else:
    T_P = sum(a.values()) / len(a)
    print("Percentage:", T_P)
    print("Highest marks:",max(a, key=a.get), max(a.values()))
    print("Lowest marks:",min(a, key=a.get), min(a.values()))
    if all(mark >= 40 for mark in a.values()):
        print("You have passed in all subjects.")

        if T_P >= 91:
            print("Grade: O, WOW you are a genius.")
        elif T_P >= 81:
            print("Grade: A+, Excellent work.")
        elif T_P >= 71:
            print("Grade: A, Good work.")
        elif T_P >= 61:
            print("Grade: B+, Keep it up.")
        elif T_P >= 55:
            print("Grade: B, You can do better.")
        elif T_P >= 50:
            print("Grade: C+, Keep practising.")
        elif T_P >= 40:
            print("Grade: C, At least you passed.")
    else:
        print("You have failed in some subjects.")
        for subject, mark in a.items():
         if mark < 40:
             print(subject, "Failed:", mark)
    