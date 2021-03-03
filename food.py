from turtle import Turtle
import random
from playsound import playsound

SHAPES = ["circle", "square", "turtle", "triangle"]
COLORS = ["red", "green", "blue", "orange", "yellow", "lightgreen"]


# Inheriting turtle.Turtle class inside Food class
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.set_shape_color()
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(x=random_x, y=random_y)

    def set_shape_color(self):
        self.shape(random.choice(SHAPES))
        self.color(random.choice(COLORS))

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.set_shape_color()
        self.goto(x=random_x, y=random_y)
        playsound("eat.wav", False)
