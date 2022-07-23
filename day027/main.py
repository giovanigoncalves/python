from tkinter import *


def calculate():
    milestone = float(miles.get())
    km = milestone * 1.60934
    output.config(text=f"{km:.2f}")


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

miles = Entry(highlightbackground="blue", highlightcolor="red")
miles.config(width=7)
miles.grid(column=1, row=0)

label1 = Label(text="Miles")
label1.grid(column=2, row=0)

label2 = Label(text="is equal to")
label2.grid(column=0, row=1)
label2.config(pady=10)

output = Label(text="0")
output.grid(column=1, row=1)

label3 = Label(text="Km")
label3.grid(column=2, row=1)

button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=3)

window.mainloop()