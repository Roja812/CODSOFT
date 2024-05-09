#Task-5-contact book
from tkinter import *

root = Tk()
root.title("Contact Book")
root.geometry("500x600")

contacts = []

def create():
    input_name = enter_name.get()
    input_number = enter_number.get()
    input_email = enter_email.get()
    input_address = enter_address.get()
    if input_name and input_number and input_email and input_address:
        contact = f"Name: {input_name}, Phone: {input_number}, Email: {input_email}, Address: {input_address}"
        contacts.append(contact)
        output.insert(END, contact)
        enter_name.delete(0, END)
        enter_number.delete(0, END)
        enter_email.delete(0, END)
        enter_address.delete(0, END)

def delete():
    selected_index = output.curselection()
    if selected_index:
        selected_contact = output.get(selected_index)
        contacts.remove(selected_contact)
        output.delete(selected_index)

def search():
    search_query = enter_search.get().lower()
    output.delete(0, END)
    for contact in contacts:
        if search_query in contact.lower():
            output.insert(END, contact)

label1 = Label(root, text="Creating Contact", font=('Brush Script MT', 18), bg="lightblue")
label1.grid(row=0, padx=5, pady=5, column=0)

labelna = Label(root, text="Name -", font=('arial', 14))
labelna.grid(row=1, padx=(0,5), pady=5, columnspan=1)

labelno = Label(root, text="Number -", font=('arial', 14))
labelno.grid(row=2, padx=(0,5), pady=5, columnspan=1)

labelmail = Label(root, text="Email -", font=('arial', 14))
labelmail.grid(row=3, padx=5, pady=5, columnspan=1)

labeladd = Label(root, text="Address -", font=('arial', 14))
labeladd.grid(row=4, padx=5, pady=5, columnspan=1)

labelser = Label(root, text="Search box-", font=('arial', 14))
labelser.grid(row=8, padx=5, pady=5, column=0)

enter_name = Entry(root, width=20, font=('century schoolbook', 14))
enter_name.grid(row=1, column=1, padx=5, pady=5)

enter_number = Entry(root, width=20, font=('century schoolbook', 14))
enter_number.grid(row=2, column=1, padx=5, pady=5)

enter_email = Entry(root, width=20, font=('century schoolbook', 14))
enter_email.grid(row=3, column=1, padx=5, pady=5)

enter_address = Entry(root, width=20, font=('century schoolbook', 14))
enter_address.grid(row=4, column=1, padx=5, pady=5)

enter_search = Entry(root, width=20, font=('century schoolbook', 14))
enter_search.grid(row=8, column=1, padx=5, pady=5)

output = Listbox(root, height=15, width=54, font=('arial', 12))
output.grid(row=6, columnspan=5, padx=5, pady=5)

add_button = Button(root, text="Add", font=('Baskerville old face', 14), background="light Pink", command=create)
add_button.grid(row=7, column=1, padx=(0,50), pady=5, sticky="e")

delete_button = Button(root, text="Delete", font=('Baskerville Old face', 14), background="brown", command=delete)
delete_button.grid(row=7, columnspan=1, padx=5, pady=5)

search_button = Button(root, text="Search", font=('arial', 14),bg="gray",command=search)
search_button.grid(row=8, column=2, padx=5, pady=5)

root.mainloop()
