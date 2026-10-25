
while True:
    
     
    a = int(input("Enter the 1st no.:\n"))
    b = int(input("Enter the 2nd no.:\n"))
    print(f"The sum of the two no. is: {a + b}")
    
    A = input("Do you want to continue? (y/n):\n").capitalize
    if A != "Y":
        break
