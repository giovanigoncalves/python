from turtle import Turtle

MOVE_DISTANCE = 20
NUMBER_OF_INITIAL_SEGMENTS = 3
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:

    def __init__(self):
        self.x_coordinate = 0
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in range(NUMBER_OF_INITIAL_SEGMENTS):
            snake = Turtle(shape="square")
            snake.color("white")
            snake.penup()
            snake.goto(x=self.x_coordinate, y=0)
            self.segments.append(snake)
            self.x_coordinate -= 20

    def add_segment(self, position):
        snake = Turtle(shape="square")
        snake.penup()
        snake.goto(x=self.x_coordinate, y=0)
        snake.color("white")
        self.segments.append(snake)
        self.x_coordinate -= 20

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):

        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

