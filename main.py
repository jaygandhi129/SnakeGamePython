import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
# Setting tracer off i.e. auto updating screen off
screen.tracer(0)

game_is_on = True
chosen_color = screen.textinput(title="Choose Snake Color", prompt="Red, Yellow, Green or White?  :  ").lower()

snake = Snake(chosen_color)
food = Food()
scoreboard = Scoreboard()

screen.listen()  # Screen starts to listen to events
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

while game_is_on:
    # Refresh Screen
    screen.update()
    # Adding 0.1 sec delay after each segment move
    time.sleep(0.1)
    snake.move()

    # Detect Collision with food
    if snake.head.distance(food) < 15:

        food.refresh()
        snake.extend()
        scoreboard.increment_score()

    # Detect Collision with wall
    if snake.does_hit_with_wall():
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    # If head collides with any segment in tail...its game over
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
screen.exitonclick()
