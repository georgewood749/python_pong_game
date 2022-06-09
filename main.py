from turtle import Screen
import paddle
import ball
import time
import scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
p2_paddle = paddle.Paddle((350, 0))
p1_paddle = paddle.Paddle((-350, 0))
ball = ball.Ball()
scoreboard = scoreboard.Scoreboard()

screen.listen()
screen.onkey(p2_paddle.go_up, "Up")
screen.onkey(p2_paddle.go_down, "Down")
screen.onkey(p1_paddle.go_up, "w")
screen.onkey(p1_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.xcor() > 350:
        ball.setpos(0, 0)
        scoreboard.increase_player1_score()

    if ball.xcor() < -350:
        ball.setpos(0, 0)
        scoreboard.increase_player2_score()

    if ball.distance(p2_paddle) < 50 and ball.xcor() > 330 or ball.distance(p1_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    if scoreboard.player1_score >= 11 or scoreboard.player2_score >= 11:
        scoreboard.game_over()
        game_is_on = False


screen.exitonclick()
