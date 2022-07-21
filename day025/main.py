import turtle
import pandas as pd
from states import States

screen = turtle.Screen()
screen.title("U.S. States Game")
img = "blank_states_img.gif"
screen.addshape(img)

turtle.shape(img)
state = States()

while state.score < state.total_states:
    answer_state = screen.textinput(title=state.text_title, prompt="What's another state's name?").title()
    if answer_state == "Exit":
        print("GoodBye!")
        break
    state.update_score(answer_state)
    state.add_state(answer_state)

missed_states = []
for option in state.data.state:
    if option not in state.guessed_states:
        missed_states.append(option)
missed_s = pd.DataFrame()
missed_s["States"] = missed_states
missed_s.to_csv("states_to_learn.csv")
