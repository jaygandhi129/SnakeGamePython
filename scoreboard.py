from turtle import Turtle
from playsound import *


ALIGNMENT = "center"
FONT = ("Arial", 18, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x=0, y=260)
        self.write(arg=f"Score = {self.score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(arg=f"Score = {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.color("red")
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        playsound("gameover.wav")


    def increment_score(self):
        self.score += 1
        self.update_score()
