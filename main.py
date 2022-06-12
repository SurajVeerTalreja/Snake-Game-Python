from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()

# Set up the 600x600 screen and change the background color to black
screen.setup(width=600, height=600)
screen.bgcolor("black")

# Set the Title
screen.title("Snake Game")
screen.tracer(0)    # It will stop showing anything on screen unless "update" function is called

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

is_game_on = True

while is_game_on:
    screen.update()     # update function updates screen with whatever code written above it
    time.sleep(0.1)

    snake.move()
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with the wall
    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -290 or\
            snake.segments[0].ycor() > 290 or snake.segments[0].ycor() < -290:
        scoreboard.reset_score()
        food.reset_food()
        snake.reset_snake()

    # Detect collision of snake head with any part of the segment
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            scoreboard.reset_score()
            food.reset_food()
            snake.reset_snake()


screen.exitonclick()
