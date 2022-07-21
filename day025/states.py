from turtle import Turtle, Screen
import pandas as pd

CSV_FILE = "50_states.csv"


class States(Turtle):

    def __init__(self):
        super().__init__()
        self.data = pd.read_csv(CSV_FILE)
        self.total_states = len(self.data.state)
        self.score = 0
        self.text_title = "Guess the state"
        self.hideturtle()
        self.guessed_states = []

    def check_answer(self, answer_state):
        return answer_state in list(self.data.state)

    def update_score(self, answer_state):
        if self.check_answer(answer_state):
            self.guessed_states.append(answer_state)
            self.score += 1
        self.text_title = f"{self.score}/{self.total_states} States Correct"

    def add_state(self, answer_state):
        if self.check_answer(answer_state):
            state_name = Turtle()
            state_name.penup()
            state_name.hideturtle()
            x_cor = int(self.data[self.data["state"] == answer_state].x)
            y_cor = int(self.data[self.data["state"] == answer_state].y)
            state_name.goto(x_cor, y_cor)
            state_name.write(answer_state, align="center")
