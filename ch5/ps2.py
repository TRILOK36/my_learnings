d = {}
for i in range(4):
    name = input("enter your name:")
    lang = input("enter your favourite programming language:")
    d.update({name.capitalize(): lang.capitalize()})
    
print(d)