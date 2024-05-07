#Task-3 Password_generator
from tkinter import *
import random
import string

root=Tk()
root.title("Password Generator")
root.geometry("500x300")
root.configure(background="Light blue")

def generate_password():
    length=int(enter_len.get())
    char=string.ascii_letters + "!@#$%^&*><?" + string.digits
    password="" .join(random.sample(char,length))
    output.config(text="Generate password : "+password)

label1=Label(root,text="Welcome to Password Genterator!!",font=('Arial',12),background="Light blue")
label1.grid(row=0,column=1,padx=10,pady=10,columnspan=1)

len_label=Label(root,text="Enter the Length : ",font=('Arial',14),background="Light blue") 
len_label.grid(row=1,column=0,padx=10,pady=10)

enter_len=Entry(root,width=20)
enter_len.grid(row=1,column=1,padx=5,pady=5)

button=Button(text="Generate Password",font=('Arial,16'),background="light Pink",command=generate_password)
button.grid(row=2,column=1,padx=10,pady=10)

output=Label(root,text="",font=('Arial',14),background="light blue")
output.grid(row=3,column=1,padx=10,pady=10,columnspan=2)

root.mainloop()

