while True:
    a = int(input("Enter year: \n"))
    if (a%4 == 0 and a%100 != 0) or (a%400 == 0):
        print("The year is a leap year.")
    else:
        print("The year is not a leap year.")
    
    c = input("Do you want to continue? (y/n):\n").capitalize()
    if c != "Y":
        print("Thank you for using my program.")
        break