from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()

        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

        # Define screen boundaries for the paddles
        self.screen_top = 260
        self.screen_bottom = -260

    def go_up(self):
        new_y = self.ycor() + 20
        if new_y < self.screen_top:
            self.sety(new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        if new_y > self.screen_bottom:
            self.sety(new_y)
