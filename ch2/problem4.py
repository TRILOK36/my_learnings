
while True:
    
     
    a = int(input("Enter the 1st no.:\n"))
    b = int(input("Enter the 2nd no.:\n"))
    print(f"The average of {a} and {b} is: {(a + b) / 2}")

    A = input("Do you want to continue? (y/n):\n").capitalize
    if A != "Y":
        print("Thank you for using the program.")
        break
