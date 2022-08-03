from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,
                           pady=20,
                           width=300,
                           height=250,
                           background=THEME_COLOR)

        self.score_label = Label(text="Score: 0",
                                 background=THEME_COLOR,
                                 fg="white")
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125,
                                                     text="Question here",
                                                     fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"),
                                                     width=280)
        self.canvas.grid(column=0, columnspan=2, row=1, pady=50)

        true_picture = PhotoImage(file="images/true.png")
        self.true = Button(image=true_picture,
                           highlightthickness=0,
                           command=self.right_button)
        self.true.grid(column=0, row=2)

        false_picture = PhotoImage(file="images/false.png")
        self.false = Button(image=false_picture,
                            highlightthickness=0,
                            command=self.wrong_button)
        self.false.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true.config(state="disabled")
            self.false.config(state="disabled")

    def right_button(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def wrong_button(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1500, func=self.get_next_question)
