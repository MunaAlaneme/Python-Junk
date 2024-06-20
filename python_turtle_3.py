# import module
import turtle
import time

# Create a turtle screen object
sc = turtle.Screen()

# initiate pen
pen = turtle.Turtle()

""" Define a method to form a semicircle
with a dynamic radius and color """
def semi_circle(col, rad, val):

    # Set the fill color of the semicircle
    pen.color(col)

    # Draw a circle
    pen.circle(rad, -180)

    # Move the turtle to air
    pen.up()

    # Move the turtle to a given position
    pen.setpos(val, 0)

    # Move the turtle to the ground
    pen.down()

    pen.right(180)


# Set the colors for drawing
col = ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']

# Setup the screen features
sc.setup(600, 600)

# Set the screen color to black
sc.bgcolor('white')

# Setup the turtle features
pen.right(90)
pen.width(10)
pen.speed(7)

# Loop to draw 7 semicircles
for i in range(7):
    semi_circle(col[i], 10*(i+8), -10*(i+1))

# Draw text
pen.up()
pen.color('black')
pen.forward(100)
pen.down()
turtle.write("Rainbow", font=("Verdana", 40, "normal"))


# Hide the turtle
time.sleep(10)
pen.hideturtle()

# https://www.geeksforgeeks.org/draw-rainbow-using-turtle-graphics-in-python/
# https://www.geeksforgeeks.org/turtle-write-function-in-python/