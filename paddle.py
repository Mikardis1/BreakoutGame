from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, -120)
        self.fillcolor("purple")
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=12)
        self.showturtle()


    def go_right(self):
        self.forward(20)

    def go_left(self):
        self.backward(20)

