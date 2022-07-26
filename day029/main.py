from tkinter import *
from tkinter import messagebox
from password import generate_password
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def gen_password():
	input3.delete(0, END)
	password = generate_password()
	input3.insert(0, password)
	pyperclip.copy(password)


# ---------------------------- SEARCH TOOL ------------------------------- #

def search():
	website = input1.get()
	try:
		with open("data.json", mode="r") as file:
			data = json.load(file)
	except FileNotFoundError:
		messagebox.showinfo(title="ERROR", message="No Data File Found!")
	else:
		if website in data:
			password = data[website]["password"]
			email = data[website]["email"]
			messagebox.showinfo(title=f"Search result for {website}", message=f"Email: {email}\nPassword: {password}")
		else:
			messagebox.showinfo(title="ERROR", message="No details for the website exists.")


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
	website = input1.get()
	email = input2.get()
	password = input3.get()
	new_data = {
		website: {
			"email": email,
			"password": password,
		}
	}

	if len(website) == 0 or len(email) == 0 or len(password) == 0:
		messagebox.showerror(title=website, message="Please don't leave any fields empty!")
	else:
		try:
			with open("data.json", mode="r") as file:
				# Reading old data
				data = json.load(file)
		except FileNotFoundError:
			with open("data.json", mode="w") as file:
				json.dump(new_data, file, indent=4)
		else:
			# Updating old data with new data
			data.update(new_data)
			# Saving updated data
			with open("data.json", mode="w") as file:
				json.dump(data, file, indent=4)
		finally:
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

input1 = Entry(width=24)
input1.grid(column=1, row=1)
input1.focus()

search_button = Button(text="Search", width=16, command=search)
search_button.grid(column=2, row=1)

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
