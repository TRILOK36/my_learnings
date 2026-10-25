d = {
   " trilok": 100,
   #"rishu": None
}
d.setdefault("rishu", 30)
#d.update({"rishu": 40})
d.update({"aryan": 50})
print(d.get("shaksh"))
print(d.get("rishu"))