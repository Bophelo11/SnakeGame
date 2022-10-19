from turtle import Turtle
START_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class The_Snake:


    def __init__(self):
        self.segments = []
        self.make_snake()
        self.head = self.segments[0]

    def make_snake(self):
        for position in START_POS:
            self.make_snake_body(position)

    def make_snake_body(self, position):
        new_seg = Turtle("square")
        new_seg.color("black")
        new_seg.penup()
        new_seg.goto(position)
        self.segments.append(new_seg)

    def make_snake_body_longer(self):
        self.make_snake_body(self.segments[-1].position())


    def make_snake_move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_xcor = self.segments[seg_num - 1].xcor()
            new_ycor = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_xcor, new_ycor)
        self.head.forward(MOVE_DIST)

    def Go_Left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


    def Go_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def Go_Up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def Go_Down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    #def move_the_snake(self):
    #    new_xcor =
    #    self.goto(new_xcor)


