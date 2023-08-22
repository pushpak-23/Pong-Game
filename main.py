import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


class PongGame:
    def __init__(self):
        self.screen = Screen()
        self.screen.bgcolor("black")
        self.screen.setup(width=800, height=600)
        self.screen.title("Pong")
        self.screen.tracer(200)

        self.r_paddle = Paddle((350, 0))
        self.l_paddle = Paddle((-350, 0))
        self.ball = Ball()
        self.scoreboard = Scoreboard()

        self.screen.listen()
        self.screen.onkeypress(self.r_paddle.go_up, "Up")
        self.screen.onkeypress(self.r_paddle.go_down, "Down")
        self.screen.onkeypress(self.l_paddle.go_up, "w")
        self.screen.onkeypress(self.l_paddle.go_down, "s")

        self.game_is_on = True

    def run_game(self):
        while self.game_is_on:
            time.sleep(self.ball.move_speed)
            self.screen.update()
            self.ball.move()

            # Detect collisions
            if self.ball.ycor() > 280 or self.ball.ycor() < -280:
                self.ball.bounce_y()

            if self.ball.distance(self.r_paddle) < 50 and self.ball.xcor() > 320:
                self.ball.bounce_x()
            else:
                # Detect collisions with paddles
                if self.ball.distance(self.l_paddle) < 50 and self.ball.xcor() < -320:
                    self.ball.bounce_x()
                else:
                    pass

            # Check if the ball goes out of bounds on the right side
            if self.ball.xcor() > 400:
                self.ball.reset_position()
                self.scoreboard.l_point()

            # Check if the ball goes out of bounds on the left side
            if self.ball.xcor() < -400:
                self.ball.reset_position()
                self.scoreboard.r_point()

        self.screen.exitonclick()


if __name__ == "__main__":
    game = PongGame()
    game.run_game()
