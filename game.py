from turtle import Screen
from snake import Snake
from time import sleep
from food import Food
from score import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scores = Scoreboard()

screen.listen()

screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")
screen.onkey(snake.left, "a") 

snake_move_on = True

while snake_move_on:
    screen.update()
    sleep(0.1)
    snake.move()
    if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        snake.game_over()
        snake_move_on=False
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scores.increase_score()
    for segment in snake.snake_list[1:]:
        if snake.head.distance(segment) < 10:
            snake.game_over()
            snake_move_on=False

        
    
    

        

        



screen.exitonclick()
