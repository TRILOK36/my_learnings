
while True:
    
     
    a = int(input("Enter the no.:\n"))
   
    print(f"The square of {a} is: {a ** 2}")

    A = input("Do you want to continue? (y/n):\n").capitalize
    if A != "Y":
        print("Thank you for using the program.")
        break
