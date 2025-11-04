import tkinter
from tkinter import ttk,messagebox

tk=tkinter.Tk()
tk.title("MyApp")
tk.geometry("400x500")
tk.config(background="lightblue")

lbl1=tkinter.Label(text="Firstname",bg='lightblue',fg='red',font='Corbel 15 bold')
#lbl1.pack()
#lbl1.place(x=0,y=0)
lbl1.grid(row=0,column=0,sticky='w')

lbl2=tkinter.Label(text="Lastname",bg='lightblue',fg='red',font='Corbel 15 bold')
#lbl2.pack()
#lbl2.place(x=0,y=30)
lbl2.grid(row=1,column=0,sticky='w')

txt1=tkinter.Entry()
#txt1.place(x=100,y=0)
txt1.grid(row=0,column=1,sticky='w')

txt2=tkinter.Entry()
txt2.grid(row=1,column=1,sticky='w')

rd1=tkinter.Radiobutton(text="Male",value=0,bg='lightblue',fg='red',font='Corbel 15 bold')
rd1.grid(row=2,column=0,sticky='w')

rd2=tkinter.Radiobutton(text="Female",value=1,bg='lightblue',fg='red',font='Corbel 15 bold')
rd2.grid(row=2,column=1,sticky='w')

ch1=tkinter.Checkbutton(text="Gujarati",bg='lightblue',fg='red',font='Corbel 15 bold')
ch1.grid(row=3,column=0,sticky='w')

ch2=tkinter.Checkbutton(text="Hindi",bg='lightblue',fg='red',font='Corbel 15 bold')
ch2.grid(row=4,column=0,sticky='w')

ch3=tkinter.Checkbutton(text="English",bg='lightblue',fg='red',font='Corbel 15 bold')
ch3.grid(row=5,column=0,sticky='w')


city=['Rajkot','Morbi','Surat','Junagadh','Jamnagar']
dd=ttk.Combobox(values=city)
dd.grid(row=6,column=0,sticky='w')

def btnClick():
    #print("Button Clicked!")
    fnm=txt1.get()
    lnm=txt2.get()
    print("FirstName:",fnm)
    print("LastName:",lnm)
    
    #Messagebox
    #messagebox.showerror("Error","Something went wrong...Try again!")
    #messagebox.showinfo("Success","Your account has been created!")
    messagebox.showwarning("Warning","Your C drive is full!")

btn=tkinter.Button(text="Submit",fg='red',font='Corbel 15 bold',command=btnClick)
btn.place(x=170,y=250)
tk.mainloop()
