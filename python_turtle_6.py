# Import the Turtle Module
import turtle
import time

# Start a Work Screen
sides = input(" Number of sides >> ")
ws = turtle.Screen()

# Define a Turtle Instance
pen = turtle.Turtle()
pen.up()
pen.setpos(-50,15*float(sides))
pen.down()

time.sleep(4)

# Execute loop 6 times for 6 sides.
for i in range(int(sides)):

    # Move forward by 90 units.
    pen.forward(90)

    # Turn the turtle right by 60 degrees.
    pen.right(360/float(sides))

time.sleep(100)
pen.hideturtle()