import turtle
win = turtle.Screen()
win.title('Pongo')
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# paleta A
paleta_A = turtle.Turtle()
paleta_A.speed(0)
paleta_A.shape("square")
paleta_A.color("white")
paleta_A.penup()
paleta_A.goto(-350, 0)
paleta_A.shapesize(stretch_wid=5, stretch_len=1)
# paleta B
paleta_B = turtle.Turtle()
paleta_B.speed(0)
paleta_B.shape("square")
paleta_B.color("white")
paleta_B.penup()
paleta_B.goto(350, 0)
paleta_B.shapesize(stretch_wid=5, stretch_len=1)

# bola
bola = turtle.Turtle()
bola.speed(0)
bola.shape("square")
bola.color("white")
bola.penup()
bola.goto(0, 0)
bola.dx = .2
bola.dy = .2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Score
score_a = 0
score_b = 0


# Funciones de movimiento
def paleta_A_up():
    y = paleta_A.ycor()
    y += 20
    paleta_A.sety(y)


def paleta_A_down():
    y = paleta_A.ycor()
    y -= 20
    paleta_A.sety(y)


def paleta_B_up():
    y = paleta_B.ycor()
    y += 20
    paleta_B.sety(y)


def paleta_B_down():
    y = paleta_B.ycor()
    y -= 20
    paleta_B.sety(y)


win.listen()
win.onkeypress(paleta_A_up, "w")
win.onkeypress(paleta_A_down, "s")
win.onkeypress(paleta_B_up, "Up")
win.onkeypress(paleta_B_down, "Down")

# Main game loop
while True:
    win.update()

    # Movimiento de pelota
    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)

    # Esquinas
    if bola.ycor() > 290:
        bola.sety(290)
        bola.dy *= -1

    if bola.ycor() < -290:
        bola.sety(-290)
        bola.dy *= -1

    if bola.xcor() > 390:
        bola.goto(0, 0)
        bola.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if bola.xcor() < -390:
        bola.goto(0, 0)
        bola.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    #bote
    if (bola.xcor() > 340 and bola.xcor() < 350) and (bola.ycor() < paleta_B.ycor() + 50 and bola.ycor() > paleta_B.ycor() -50):
        bola.setx(340)
        bola.dx *= -1

    if (bola.xcor() < -340 and bola.xcor() > -350) and (bola.ycor() < paleta_A.ycor() + 50 and bola.ycor() > paleta_A.ycor() -50):
        bola.setx(-340)
        bola.dx *= -1

    if score_b == 5 or score_a == 5:
        exit()
