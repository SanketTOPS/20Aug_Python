import re

mystr="This is Python!"

x=re.search("This",mystr)
print(x)

if x:
    print("Success!")
else:
    print("Error!")