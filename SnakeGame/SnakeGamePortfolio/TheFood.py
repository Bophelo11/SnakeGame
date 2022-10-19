import turtle
from turtle import Turtle
import random

Your_image = "Asset 1@4x.gif"
turtle.addshape(Your_image)
class Foods(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(Your_image)
        self.speed("fastest")
        self.penup()
        self.redo()


    def redo(self):
        random_xcor = random.randint(-280, 280)
        random_ycor = random.randint(-280, 280)
        self.goto(random_xcor, random_ycor)


