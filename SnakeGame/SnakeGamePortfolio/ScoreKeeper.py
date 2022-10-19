from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Helivetica", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.score_update()

    def score_update(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def ojiwe(self):
        self.goto(0, 0)
        self.write("O Jiwe Ngwana Mme", align=ALIGNMENT, font=FONT)

    def add_to_score(self):
        self.score += 1
        self.clear()
        self.score_update()