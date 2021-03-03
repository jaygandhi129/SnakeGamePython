from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self, color):
        self.color = color
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color(self.color)
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def opposite_heading(self, opposite_angle):
        if self.head.heading() == opposite_angle:
            return True
        else:
            return False

    def up(self):
        if not self.opposite_heading(DOWN):
            self.head.setheading(UP)

    def down(self):
        if not self.opposite_heading(UP):
            self.head.setheading(DOWN)

    def left(self):
        if not self.opposite_heading(RIGHT):
            self.head.setheading(LEFT)

    def right(self):
        if not self.opposite_heading(LEFT):
            self.head.setheading(RIGHT)

    def does_hit_with_wall(self):
        """Return True if snake hits with wall"""
        if self.head.xcor() > 285 or self.head.xcor() < -285 or self.head.ycor() > 285 or self.head.ycor() < -285:
            return True
        else:
            return False

    def extend(self):
        """Adds one segment at end"""
        # add new segment to snake
        last_segment = self.segments[-1]
        self.add_segment(last_segment.position())
