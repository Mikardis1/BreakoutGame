from turtle import Screen
from paddle import Paddle
from bricks import Bricks
from scoreboard import Scoreboard
from ball import Ball
from player import Player
import time
import random
#To imsert a background music to the game
import pygame

# Initialize mixer (add this at the start of your game)
pygame.mixer.init()

# 600 * 400 is the default screen. Each square is 20 px
screen = Screen()
screen.setup(width=600, height=400)
screen.title("Breakout Game")
screen.bgcolor("black")

background_music = pygame.mixer.Sound("sounds/Theme_Song.ogg")
# Play background music on loop (add before game loop)
background_music.play(loops=-1)  # -1 = infinite loop


screen.tracer(0) #Pause the code and runs it after using the screen.update() prompt command

paddle = Paddle()
bricks = Bricks()
ball = Ball()
scoreboard = Scoreboard()
player = Player()


#Allows to use the control(left and Right)
screen.listen()
#It will execute that function everytime it is clickes up button
screen.onkey(paddle.go_right, key="Right")
screen.onkey(paddle.go_left, "Left")

# Without the loop cicle the screen.onkey won't work
game_is_on = True



while game_is_on:
    # 0.1 seconds to start running the program with all settled. The important movement is the ball speed, while it's looped
    time.sleep(ball.move_speed)
    # bettween screen.tracer(0) and screen.update the turltes need will be prepared.Giving a break for the preparation
    screen.update()



    ball.move()

    #let's make the ball bouncing and deleting the brick
    deleted_bricks = []
    total_bricks_at_beginning = len(bricks.all_bricks)

    for brick in bricks.all_bricks:
        # Try -15 distance after
        if ball.distance(brick) < 25 and brick not in deleted_bricks:
            ball.bounce_y()

            # Let's make a creative way to speed up the ball. When it bricks a brick it can possibly increase the speed the ball
            if random.randint(1, 6) == 2:
                ball.move_speed *= 0.9

            # ADDING HERE THE SCOREBOARD OF THE BRICK ACCORDING TO THE COLOR OF THE brick
            if brick.fillcolor() == "green":
                scoreboard.score_number += 10
                scoreboard.show_score()

            elif brick.fillcolor() == "yellow":
                scoreboard.score_number += 50
                scoreboard.show_score()

            elif brick.fillcolor() == "orange":
                scoreboard.score_number += 100
                scoreboard.show_score()

            elif brick.fillcolor() == "red":
                scoreboard.score_number += 80
                scoreboard.show_score()

            # Deleting the brick from the game
            bricks.delete_brick(brick)


            # Adding to the list of deleted_bricks to not delete that brick if it's in there
            deleted_bricks.append(brick)

            # Lets make it a bit more difficult from times to time lets make it bounce_x WHEN HIT THE BRICK
            if random.randint(1, 3) == 2:
                ball.bounce_x()

            #If there's no more bricks on board you won the game
            if len(deleted_bricks) == total_bricks_at_beginning:
                scoreboard.victory()
                game_is_on = False

    # Let's make first the ball moving and bouncing into the walls
    if ball.ycor() > 180:
        ball.bounce_y()


    elif ball.distance(paddle) < 120 and ball.ycor() < -100: #To detect the paddle
        ball.bounce_y()

        #Lets make it a bit more difficult from times to time lets make it bounce_x WHEN HIT THE PADDLE
        if random.randint(1, 3) == 2:
            ball.bounce_x()


    elif abs(ball.xcor()) > 280: # it's simply math: xcor() > 280 or xcor < -280, it will bounces
        ball.bounce_x()



    elif ball.ycor() < -130: #Remove this option  when you're trying to figure the rest of the code and finally you can add

        player.lives_number -= 1
        player.show_lives()

        time.sleep(2)
        ball.reset_ball()

        if player.lives_number < 0:
            scoreboard.game_over()
            game_is_on = False





screen.exitonclick()

