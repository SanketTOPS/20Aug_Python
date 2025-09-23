"""stdata={
    "id":[1,2,3],
    "name":["Sanket","Nirav","Ashok"],
    "city":["Rajkot","Baroda","Surat"]
}"""

#print(stdata)
#print(stdata["name"])


"""for i in stdata.values():
    print(i[0])"""
    
# -------------------------------- #

stdata=[
    {"id":1,"name":"sanket"},
    {"id":2,"name":"nirav"},
    {"id":3,"name":"ashok"}
]

print(stdata)
print(stdata[0])
print(stdata[0]["name"])