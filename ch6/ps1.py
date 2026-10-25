while True:
    a = []
    
    for i in range(4):
        b = int(input("Enter a no.:\n"))
        a.append(b)
    if a[0] > a[1] and a[0] > a[2] and a[0] > a[3]:
        print("The largest no. is", a[0])
    elif a[1] > a[0] and a[1] > a[2] and a[1] > a[3]:
        print("The largest no. is", a[1])
    elif a[2] > a[0] and a[2] > a[1] and a[2] > a[3]:
        print("The largest no. is", a[2])
    elif a[3] > a[0] and a[3] > a[1] and a[3] > a[2]:
     print("The largest no. is", a[3])
    else:
        print("There is a tie  for the largest number in list.\n", a)
    
    c = input("Do you want to continue? (y/n):\n").capitalize()
    if c != "Y":
        break