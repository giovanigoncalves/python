from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.xcor()
        self.x_move = 10
        self.y_move = 10
        self.goto(0, 0)
        self.speed(1)
        self.move_speed = .1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.x_move *= -1

    def increase_speed(self):
        new_speed = self.speed() + 1
        self.speed(new_speed)
