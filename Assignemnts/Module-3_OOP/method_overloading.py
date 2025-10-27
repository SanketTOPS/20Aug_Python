class stud:
    #Method Overloading
    def getdata(self,id):
        print("ID:",id)
        
    def getdata(self,name):
        print("Name:",name)
    
st=stud()
st.getdata("Sanket")
st.getdata(101)