from tkinter import *
import pandas as pd
from random import choice

new_word = {}
to_learn = {}
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def new_card():
    global new_word, flip_timer
    window.after_cancel(flip_timer)
    new_word = choice(to_learn)
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(word, fill="black", text=new_word["French"])
    canvas.itemconfig(image, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def is_known():
    to_learn.remove(new_word)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    new_card()


def flip_card():
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word, fill="white", text=new_word["English"])
    canvas.itemconfig(image, image=card_back_img)


BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

card_back_img = PhotoImage(file="images/card_back.png")
card_front_img = PhotoImage(file="images/card_front.png")
canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
image = canvas.create_image(400, 268, image=card_front_img)
language = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Arial", 60, "normal"))
canvas.grid(column=0, row=0, columnspan=2)

button_wrong_img = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=button_wrong_img,
                      highlightthickness=0,
                      command=new_card)
button_wrong.grid(column=0, row=1)

button_right_img = PhotoImage(file="images/right.png")
button_right = Button(image=button_right_img,
                      background=BACKGROUND_COLOR,
                      highlightthickness=0, command=is_known)
button_right.grid(column=1, row=1)

new_card()

window.mainloop()
