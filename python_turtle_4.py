# Import module
import turtle

# Initiate pen
pen = turtle.Turtle()
heartsize = input(" Enter heart size >> ")

# Define a method to draw curve
def curve():
    for i in range(200):
        
        # Define step by step curve motion
        pen.right(1)
        pen.forward(float(heartsize))

# Define method to draw a full heart
def heart():

    # Set the fill color to red
    pen.color('red')

    # Start filling the color
    pen.begin_fill()

    # Draw the left line
    pen.left(140)
    pen.forward(float(heartsize)*113)

    # Draw the left curve
    curve()
    pen.left(120)

    # Draw the right curve
    curve()

    # Draw the right line
    pen.forward(float(heartsize)*112)

    # End the filling of the color
    pen.end_fill()

# Define method to write text
def txt():

    # Move turtle to air
    pen.up()

    # Move turtle to a given position
    pen.down()

    # Set the text color to lightgreen
    pen.color('lightgreen')

    """ Write the specified text in
    specified font style and size"""
    pen.write(input(" Text >> "), font=("Verdana", 30, "bold"))

# Draw a heart
heart()

# Write text
txt()

# To hide turtle
input(" Press enter to quit.")
pen.ht()

# https://www.geeksforgeeks.org/draw-heart-using-turtle-graphics-in-python/