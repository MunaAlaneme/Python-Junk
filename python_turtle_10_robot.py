# July 15, 2024

import turtle as t

def rectangle(horizontal, vertical, color):
    t.pendown()
    t.pensize(1)
    t.color(color)
    t.begin_fill()
    for counter in range (1,3):
        t.forward(horizontal)
        t.right(90)
        t.forward(vertical)
        t.right(90)
    t.end_fill()
    t.penup()

def setup():
    t.penup()
    t.speed('slow')
    t.bgcolor('Dodger blue')

# Feet
def feet():
    t.goto(-100, -150)
    rectangle(50, 20, 'blue')
    t.goto(-30, -150)
    rectangle(50, 20, 'blue')

# Legs
def legs():
    t.goto(-25, -50)
    rectangle(15, 100, 'grey')
    t.goto(-55, -50)
    rectangle(-15, 100, 'grey')

# Body
def body():
    t.goto(-90, 100)
    rectangle(100, 150, 'red')

# Arms
def arms():
    t.goto(-150, 70)
    rectangle(60, 15, 'grey')
    t.goto(-150, 110)
    rectangle(15, 40, 'grey')
    t.goto(10, 70)
    rectangle(60, 15, 'grey')
    t.goto(55, 110)
    rectangle(15, 40, 'grey')

# Neck
def neck():
    t.goto(-50, 120)
    rectangle(15, 20, 'grey')

# Head
def head():
    t.goto(-80, 170)
    rectangle(80, 50, 'red')

# Eyes
def eyes():
    t.goto(-55, 160)
    rectangle(30, 10, 'white')
    t.goto(-50, 155)
    rectangle(5, 5, 'black')
    t.goto(-35, 155)
    rectangle(5, 5, 'black')

# Mouth
def mouth():
    t.goto(-60, 135)
    rectangle(40, 5, 'black')

setup()
feet()
legs()
body()
arms()
neck()
head()
eyes()
mouth()
t.hideturtle()

t.mainloop()