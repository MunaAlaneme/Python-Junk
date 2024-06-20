# draw a car using turtle

# Python program to draw car in turtle programming

# Import required libraries
import turtle
import time

car = turtle.Turtle()

# Below code for drawing rectangular upper body
car.color('#008000')
car.fillcolor('#008000')
car.penup()
car.goto(0,0)
car.pendown()
car.begin_fill()
car.forward(370)
car.left(90)
car.forward(50)
car.left(90)
car.forward(370)
car.left(90)
car.forward(50)
car.end_fill()

# Below code for drawing window and roof
car.penup()
car.goto(100, 50)
car.pendown()
car.setheading(45)
car.forward(70)
car.setheading(0)
car.forward(100)
car.setheading(-45)
car.forward(70)
car.setheading(90)
car.penup()
car.goto(200, 50)
car.pendown()
car.forward(49.50)

# Below code for drawing two tyres
""" I'm a tire.
    -Mario 2023 """
car.penup()
car.goto(100, -10)
car.pendown()
car.color('#000000')
car.fillcolor('#000000')
car.begin_fill()
car.circle(20)
car.end_fill()
car.penup()
car.goto(300, -10)
car.pendown()
car.color('#000000')
car.fillcolor('#000000')
car.begin_fill()
car.circle(20)
car.end_fill()

time.sleep(10)
car.hideturtle()

# https://www.geeksforgeeks.org/draw-a-car-using-turtle-in-python/