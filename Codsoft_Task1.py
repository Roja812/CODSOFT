#Task 1-To-Do-List
from tkinter import *
import tkinter.messagebox

root = Tk()
root.title("To Do List")
root.geometry("450x500")
root.configure(background="Light pink")

def add():
    input_text = enter_item.get()
    if input_text == "":
        tkinter.messagebox.showwarning(title="Warning!", message="Please Enter some Text")
    else:
        output.insert(END, input_text + "\n")
        enter_item.delete(0, END)

def deletetask(): 
    selected = output.curselection()
    if selected:
        output.delete(selected[0])

def markcompleted():
    selected = output.curselection()
    if selected:
        completed_task = output.get(selected)
        output.delete(selected)
        output.insert(selected, completed_task.strip() + " ✔")

label1 = Label(root, text="To Do List", font=('Brush Script MT', 24),fg="brown",bg="lightpink")
label1.grid(row=0, padx=20, pady=10, columnspan=3)

label2 = Label(root, text="Enter the Event To Do -", font=('Baskerville Old Face', 16), background="light pink")
label2.grid(row=1, column=0, padx=5, pady=5)

label3 = Label(root, text="Events List To Do", font=('arial', 14),bg="lightpink",fg="brown")
label3.grid(row=2, columnspan=3, padx=10, pady=10)

enter_item = Entry(root, width=20, font=('century schoolbook', 14))
enter_item.grid(row=1, column=1, padx=5, pady=5)

output = Listbox(root, height=15, width=35, font=('arial', 12))
output.grid(row=3, columnspan=2, padx=5, pady=5)

button1 = Button(root, text="Add", font=('Baskervillle old face', 14), background="light green", command=add)
button1.grid(row=2, column=1, padx=(0,50), pady=5,sticky="e")

button2 = Button(root, text="Delete", font=('Baskervelli Old face', 14), background="red", command=deletetask)
button2.grid(row=6, columnspan=1, padx=5, pady=5)

button3 = Button(root, text="Mark as Completed", font=('Baskervelli Old face', 14), background="yellow", command=markcompleted)
button3.grid(row=6, column=1, padx=(5,18), pady=5)

root.mainloop()
