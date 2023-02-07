from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 55
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 25
reps = 0
check = ""
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    global check
    global reps
    window.after_cancel(timer)
    label1.config(text="Timer")
    canvas.itemconfig(time_text, text="00:00")
    check = ""
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    global check
    label3.config(text=check)
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 4 == 0:
        label1.config(text="Break",
                      fg=RED,
                      font=(FONT_NAME, 50, "bold"))
        count_down(long_break_sec)
    elif reps % 2 == 0:
        label1.config(text="Break",
                      fg=PINK,
                      font=(FONT_NAME, 50, "bold"))
        count_down(short_break_sec)
    else:
        label1.config(text="WORK",
                      fg=GREEN,
                      font=(FONT_NAME, 50, "bold"))
        count_down(work_sec)
        check += "✔"
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    if count >= 60:
        count_min = int(count // 60)
    else:
        count_min = 0
    count_sec = int(count % 60)
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(time_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
time_text = canvas.create_text(100, 130, text="00:00",
                               fill="white",
                               font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

label1 = Label(text="Timer", font=(FONT_NAME, 50, "bold"),
               bg=YELLOW, fg=GREEN)
label1.grid(column=1, row=0)

button_start = Button(text="Start", bg=YELLOW,
                      highlightthickness=0, command=start_timer)
button_start.grid(column=0, row=2)

button_reset = Button(text="Reset", bg=YELLOW,
                      highlightthickness=0,
                      command=reset_timer)
button_reset.grid(column=2, row=2)

label3 = Label(text="", font=(FONT_NAME, 25, "bold"),
               bg=YELLOW, fg=GREEN, highlightthickness=0)
label3.grid(column=1, row=4)

window.mainloop()
