class student:
    #private
    __id=12
    __name="Sanket"
    
    #private
    def __getdata(self):
        print("This is getdata!")
        print("ID:",self.__id)
        print("Name:",self.__name)
    
    def printdata(self):
        self.__getdata()


st=student()
#print("ID:",st.__id)
#print("Name:",st.__name)
#st.__getdata()

st.printdata()
