from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        self.level = 0
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-200, -280)
        self.level_up()

    def level_up(self):
        self.clear()
        self.level += 1
        self.write(f"Level:{self.level}", align='center', font=FONT)












