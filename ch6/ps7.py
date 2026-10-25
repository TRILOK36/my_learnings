name_list = ["trilok", "rohan", "soham", "ashay", "siddharth", "pranav", "aditya", "shubham", "ankit", "rahul"]
a = input("Enter a name: ").lower()
if any(name in a for name in name_list):
    print("The name is present in the list.")
else:
    print("The name is not present in the list.")