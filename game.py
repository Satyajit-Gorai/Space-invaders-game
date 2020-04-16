import turtle as tr
import os

# canvas
window = tr.Screen()
#window = tr.screensize(650,550,"black")
window.bgcolor("black")
#window = tr.title("Space Invaders")
window.title("Space Invaders")

#canvas border
pen = tr.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.setposition(-300,-300)
pen.pendown()
pen.pensize(3)
for i in range(4):
    pen.forward(600)
    pen.left(90)
pen.hideturtle()
#PLAYER
#player description
player = tr.Turtle()
player.color("green")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0,-260)
player.setheading(90)

#player wepon
wepon = tr.Turtle()
wepon.color("white")
wepon.shape("triangle")
wepon.penup()
wepon.speed(0)
wepon.setheading(90)
wepon.shapesize(0.3,0.3)
wepon.hideturtle()
wepon_speed = 20

#wepon state
wepon_state = "ready"
#wepon ----- ready to launch
#wepon ----- launched
#player movement
player_speed = 10

def move_left():
    x = player.xcor()
    x -= player_speed
    if x < -285:
        x = -285
    player.setx(x)

def move_right():
    x = player.xcor()
    x += player_speed
    if x > 285:
        x = 285
    player.setx(x)
#wepon position
def fire_wepon():
    global wepon_state
    if wepon_state == "ready":
        wepon_state = "fired"
        x = player.xcor()
        y = player.ycor() + 15
        wepon.setposition(x,y)
        wepon.showturtle()

#ENEMY
#enemy description
enemy = tr.Turtle()
enemy.color("yellow")
enemy.shape("circle")
enemy.penup()
enemy.speed(0)
enemy.setposition(-205,255)
enemy_speed = 2

#keyboard connection
tr.listen()
tr.onkey(move_left, "Left")
tr.onkey(move_right, "Right")
tr.onkey(fire_wepon, "space")

#enemy movement
while True:
    x = enemy.xcor()
    x += enemy_speed
    enemy.setx(x)
    #enemy movement side and down
    if enemy.xcor() > 280:
        y = enemy.ycor()
        y -= 20
        enemy_speed *= -1
        enemy.sety(y)

    if enemy.xcor() < -280:
        y = enemy.ycor()
        y -= 20
        enemy_speed *= -1
        enemy.sety(y)
#wepon movement
    if wepon_state == "fired":
        y = wepon.ycor()
        y += wepon_speed
        wepon.sety(y)
#wepon collision check with boundary
    if wepon.ycor() > 280:
        wepon.hideturtle()
        wepon_state = "ready"

delay = input("press q to finish")
