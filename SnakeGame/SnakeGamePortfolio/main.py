from turtle import Screen
from TheIzinyoka import The_Snake
from TheFood import Foods
from ScoreKeeper import Scoreboard
import time


screen = Screen()
screen.setup(width=700, height=700)
screen.title("You must be afraid of the izinyoka")
screen.bgpic("cuh-stom shoe for snake.gif")
screen.tracer(0)

snake = The_Snake()
food = Foods()
scorekeeper = Scoreboard()


screen.listen()
screen.onkey(snake.Go_Up, "Up")
screen.onkey(snake.Go_Down, "Down")
screen.onkey(snake.Go_Left, "Left")
screen.onkey(snake.Go_right, "Right")

game_is_on = True
while game_is_on:

    #Snake.move_the_snake()
    screen.update()
    time.sleep(0.1)
    snake.make_snake_move()

    #Collision with Food
    if snake.head.distance(food) < 15:
        food.redo()
        snake.make_snake_body_longer()
        scorekeeper.add_to_score()

    #collision with wall
    if snake.head.xcor() > 340 or snake.head.xcor() < -340 or snake.head.ycor() > 340 or snake.head.xcor() < -340:
        game_is_on = False
        scorekeeper.ojiwe()

    #collision with tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scorekeeper.ojiwe()





screen.exitonclick()