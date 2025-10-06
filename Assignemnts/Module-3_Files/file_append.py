file=open("new.txt","a")

id=input("Enter an ID:")
name=input("Enter a Name:")


file.write(f"ID:{id}\nName:{name}\n-------------\n")
