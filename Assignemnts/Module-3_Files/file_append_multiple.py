file=open("stdata.txt","a")

n=int(input("Enter number of studens:"))

for i in range(n):

    id=input("Enter an ID:")
    name=input("Enter a Name:")
    file.write(f"ID:{id}\nName:{name}\n-------------\n")
