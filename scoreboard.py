from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.score_number = 0
        self.show_score()




    def game_over(self):
        self.goto(x=0, y=-100)

        self.write(arg="Game Over!", align="center", font=('Courier', 50, 'normal'))

    def victory(self):

        self.goto(x=0, y=-100)

        self.write(arg="Congratulations!\nYou Beat The Game!", align="center", font=('Courier', 30, 'normal'))



    def show_score(self):

        self.clear()  # To not print again it's needed to clear all the records to not print again

        self.goto(x=160, y=-180)

        self.write(arg=f"Points: {self.score_number}", align="left", font=('Courier', 15, 'normal'))




