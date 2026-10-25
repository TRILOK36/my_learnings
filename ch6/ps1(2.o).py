while True:
    a= []
    d = int(input("Enter the number of elements you want to enter in list:\n"))
    for i in range(d):
        b = int(input("Enter a no.:\n"))
        a.append(b)
    if len(a) == 0:
        print("The list is empty.")
    else:    
        largest = max(a)
    
        if a.count(largest) > 1:
            print("There is a tie for the largest number in list.\n", largest)
        else:
            print("The largest no. is", largest)
    c = input("Do you want to continue? (y/n):\n").capitalize()
    if c != "Y":
        print("Thank you for using my program.")
        break    