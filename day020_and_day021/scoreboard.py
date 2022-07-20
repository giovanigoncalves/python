from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 20, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.score = 0
        with open("snake_high_score.txt", mode="r") as file:
            self.high_score = int(file.read())
        # self.high_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("snake_high_score.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_score()



