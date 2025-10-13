class studinfo:
    stid=101
    stnm="Sanket"
    
    def getdata(self):
        print("This is getdata from studinfo!")

#Object of class
st=studinfo()
print("ID:",st.stid)
print("Name:",st.stnm)

st.getdata()