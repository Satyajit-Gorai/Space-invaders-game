import turtle as tr
import random
import math
import os

# canvas
window = tr.Screen()
#window = tr.screensize(650,550,"black")
window.bgcolor("black")
#window = tr.title("Space Invaders")
window.title("Space Invaders")
window.bgpic("bgr.gif")

#enemy and player shape
tr.register_shape("player.gif")
tr.register_shape("enemy.gif")

#canvas border
pen = tr.Turtle()
pen.speed(0)
pen.color("pink")
pen.penup()
pen.setposition(-300,-300)
pen.pendown()
pen.pensize(3)
for i in range(4):
    pen.forward(600)
    pen.left(90)
pen.hideturtle()
pen.penup()

#GAME SCORE
score = 0
scr_pen = tr.Turtle()
scr_pen.color("white")
scr_pen.speed(0)
scr_pen.penup()
scr_pen.setposition(-290,280)
scr_pen.pendown()
score_str = "Score : %s" %score
scr_pen.write(score_str, False, align="left", font=("Arial", 14, "normal"))
scr_pen.hideturtle()
#PLAYER
#player description
player = tr.Turtle()
player.color("green")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0,-275)
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

#damage checking
def is_hit(e , w):
    dist = math.sqrt(math.pow(e.xcor() - w.xcor(),2) + math.pow(e.ycor() - w.ycor(),2))
    if dist < 20:
        return True
    else:
        return False
#ENEMY
#make multiple enemies
no_of_enemies = 6
enemies = []

#enemy generation
for i in range(no_of_enemies):
    enemies.append(tr.Turtle())

    #enemy description
for enemy in enemies:
    enemy.color("yellow")
    enemy.shape("enemy.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-205, 205)
    y = random.randint(105,255)
    enemy.setposition(x, y)

enemy_speed = 2

#keyboard connection
tr.listen()
tr.onkey(move_left, "Left")
tr.onkey(move_right, "Right")
tr.onkey(fire_wepon, "space")

#GAME PRINCIPLE
while True:
    for enemy in enemies:
        x = enemy.xcor()
        x += enemy_speed
        enemy.setx(x)
        #enemy movement side and down
        if enemy.xcor() > 280:
        #move all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 20
                e.sety(y)
        #change enemies direction
            enemy_speed *= -1

        if enemy.xcor() < -280:
        #move all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 20
                e.sety(y)
        #change enemies direction
            enemy_speed *= -1

#collision check between enemy and wepon
        if is_hit(wepon , enemy):
        #reset wepon
            wepon.hideturtle()
            wepon_state = "ready"
            wepon.setposition(0,-400)
        #reset enemy
            x = random.randint(-205, 205)
            y = random.randint(105,255)
            enemy.setposition(x, y)
        #score update
            score += 10
            score_str = "Score : %s" %score
            scr_pen.clear()
            scr_pen.write(score_str, False, align="left", font=("Arial", 14, "normal"))
#collision check between enemy and player
        if is_hit(player , enemy):
            player.hideturtle()
            enemy.hideturtle()
            print("GAME OVER!!!!!!!!!!")
            break

#wepon movement
    if wepon_state == "fired":
        y = wepon.ycor()
        y += wepon_speed
        wepon.sety(y)
#wepon collision check with boundary
    if wepon.ycor() > 280:
        wepon.hideturtle()
        wepon_state = "ready"

delay = input("press any key to finish :- ")
