class Student:
    #data member
    stid=12
    stnm="Sanket"
    
    def myfunc(self): #member function
        print("This is member function!")
        
#Object of class
st=Student()
"""print(st.stid)
print(st.stnm)"""

print("ID:",st.stid)
print("Name:",st.stnm)

st.myfunc()
    