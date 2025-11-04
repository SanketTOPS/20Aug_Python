x=5

print("X:",x)

def getvalue():
    global x #reassign
    x+=10
    print("X:",x)

getvalue()
    
