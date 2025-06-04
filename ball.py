from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape("circle")
        self.penup()
        self.goto(-100, -100)
        self.fillcolor("white")
        self.showturtle()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move


        # Clamp position to screen bounds.
        if new_x > 280:
            new_x = 280
            self.x_move *= -1
        elif new_x < -280:
            new_x = -280
            self.x_move *= -1

        if new_y > 180:
            new_y = 180
            self.y_move *= -1
        elif new_y < -180:
            new_y = -180
            self.y_move *= -1

        self.goto(new_x,new_y)

    # returning down if up or vice versa. Passing the screen limits or bricks
    def bounce_y(self):
        self.y_move *= -1


    # returning left if right or vice versa. Passing through the screen limits or bricks
    def bounce_x(self):
        self.x_move *= -1


    def reset_ball(self):

        self.goto(-100, -100)

        #To not start so slow
        self.move_speed = 0.1 * 0.9

        # Make it going into opposite direction
        self.bounce_x()
        self.bounce_y()

