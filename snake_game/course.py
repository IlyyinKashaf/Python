import turtle  
from turtle import Turtle, Screen
import time 
from snake_game.snake import Snake 
from snake_game.food import Food
from snake_game.scoreboard import Score


# Screen setup
screen = Screen()
screen.setup(width=600, height=400)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)




snake = Snake()
food  = Food()
score = Score()



screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.right,'Right')
screen.onkey(snake.left,'Left')


game = True

while game:
    screen.update()
    time.sleep(0.1)
    screen.update()
    snake.snake_move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.scoreupdate()
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 195 or snake.head.ycor() < -195:
        game = False 
        score.game_over()
    



screen.exitonclick()
