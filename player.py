from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.lives_number = 3
        self.show_lives()



    #Let's create lives to make it harder
    def show_lives(self):

        self.clear()

        self.goto(x=-280, y=-180)

        self.write(arg=f"Lives: {self.lives_number}", align="left", font=('Courier', 15, 'normal'))

