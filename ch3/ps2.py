#double space detection
sentence = "hello, your  are selected  for  this  job"

print(sentence.find("  ")) #finds the index of double space
print(sentence.replace("  "," "))# repalce "  " (double space with) " "single space