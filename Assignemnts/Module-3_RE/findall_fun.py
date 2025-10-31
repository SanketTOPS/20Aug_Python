import re

mystr="This is Python!"

x=re.findall("is",mystr)
print(x)

if x:
    print("Success!")
else:
    print("Error!")