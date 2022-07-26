from tkinter import *
from tkinter import messagebox
from password import generate_password
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def gen_password():
	input3.delete(0, END)
	password = generate_password()
	input3.insert(0, password)
	pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
	website = input1.get()
	email = input2.get()
	password = input3.get()

	if len(website) == 0 or len(email) == 0 or len(password) == 0:
		messagebox.showerror(title=website, message="Please don't leave any fields empty!")
	else:
		is_ok = messagebox.askokcancel(title=website, message=f"These ate the details entered: \nEmail: {email}\nPassword: {password} \nIs it ok to save?")

		if is_ok:
			with open("data.txt", mode="a") as file:
				file.write(f"{website} | {email} | {password}\n")
			input1.delete(0, END)
			input3.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
padlock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=padlock_img)
canvas.grid(column=1, row=0)

label1 = Label(text="Website:")
label1.grid(column=0, row=1)

input1 = Entry(width=44)
input1.grid(column=1, row=1, columnspan=2)
input1.focus()

label2 = Label(text="Email/Username:")
label2.grid(column=0, row=2)

input2 = Entry(width=44)
input2.grid(column=1, row=2, columnspan=2)
input2.insert(0, "giovani@gmail.com")


label3 = Label(text="Password:")
label3.grid(column=0, row=3)

input3 = Entry(width=25)
input3.grid(column=1, row=3)

button_gen = Button(text="Generate Password", command=gen_password)
button_gen.grid(column=2, row=3)

button_add = Button(text="Add", width=41, command=save_data)
button_add.grid(column=1, row=4, columnspan=2)




window.mainloop()
