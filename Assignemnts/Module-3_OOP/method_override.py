class master:
    #Method Overriding
    def header(self,pname):
        print(f"This is {pname}")
    
class home(master):
    def header(self, pname):
        return super().header(pname)

class about(master):
    def header(self, pname):
        return super().header(pname)
        
h=home()
h.header("HOME")

a=about()
a.header("ABOUT")