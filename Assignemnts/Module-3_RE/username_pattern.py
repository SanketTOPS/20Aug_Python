import re

username=input("Enter an Username:")

u_pattern="[A-Z]+[a-z]+[0-9]"

x=re.findall(u_pattern,username)

if x:
    print("Username is valid!")
else:
    print("Error!Invalid Username...")