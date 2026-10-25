a = []
b = input("Enter username text: ").strip().replace(" ", "")

if len(b) < 8:
    print("Username is too short. It must be at least 8 characters long.")
else:
    if b.isalnum():
        if b.isalpha():
            print("Username must contain at least one number.")
        elif b.isdigit():
            print("Username must contain at least one letter.")
        else:
            print("Username is valid.")
            a.append(b) 
    else:
        print("Username must contain only alphanumeric characters.")
        
print("username database:", a)        