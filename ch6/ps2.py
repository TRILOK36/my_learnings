while True:
    a = int(input("Enter a no.:\n"))
    
    #if-else ladder to check if the number is positive, negative or zero and even or odd
    if a > 0:
        print("The number is positive and")
    elif a < 0:
        print("The number is negative and")
    else:
        print("The number is zero and")
   # if-else ladder to check if the number is even or odd
    if a%2 == 0:
        print("it is an even number.")
    else:
        print("it is an odd number.")
    
    if a%5 == 0:
        print("The number is divisible by 5.")
    elif (a%5 == 0 and a%3 == 0):
        print("The number is divisible by 5 and 3.")
    elif a%3 == 0:
        print("The number is divisible by 3.")
    else:
        print("The number is not divisible by 5 or 3.")

    c = input("Do you want to continue? (y/n):\n").capitalize()
    if c != "Y":
        print("Thank you for using my program.")
        break