from turtle import Turtle

STARTING_POSITION = (0, -270)


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.go_origin()

    def go_origin(self):
        self.goto(STARTING_POSITION)

    def go_up(self):
        self.forward(20)

    def is_at_finish_line(self):
        if self.ycor() > 280:
            return True
        else:
            return False