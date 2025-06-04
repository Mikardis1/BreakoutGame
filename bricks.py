from turtle import Turtle
import random



class Bricks:
    def __init__(self):
        self.all_bricks = []


        self.create_bricks()

    def create_bricks(self):
        # Creating on x axis the bricks to fill the width
        for a in range(-280, 300, 40):
            # Filling with bricks on the height. I want 3 lines
            for b in range(40,120,20):

                # Create Turtles to insert them on a list of turtles
                self.tim = Turtle()
                self.tim.hideturtle()
                self.tim.penup()
                self.tim.shape("square")

                if b >= 100:
                    self.tim.fillcolor("red")

                elif b >= 80:
                    self.tim.fillcolor("orange")
                elif b >= 60:
                    self.tim.fillcolor("yellow")
                else:
                    self.tim.fillcolor("green")

                self.tim.shapesize(stretch_wid=1, stretch_len=2)

                # Default is 400x300
                # 600 * 600 means x = [-260, 260] and y = [-260,260]. Level 1 [-380, 280] -> 40 len: 20px *2
                self.tim.goto(x=a, y=b)
                self.tim.showturtle()

                self.all_bricks.append(self.tim)


    # Everytime the balls hits a brick the brick needs to be deleted
    def delete_brick(self, brick):

        index = self.all_bricks.index(brick)
        self.all_bricks[index].hideturtle() # hide the brick on the Screen
        del self.all_bricks[index]
