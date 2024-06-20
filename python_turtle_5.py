# Draw a Panda using Turtle Graphics
# Import turtle package
import turtle
import time

# Creating a turtle object(pen)
PandaSize = input(" Panda Size >> ")
pen = turtle.Turtle()

""" Defining method to draw a colored circle
with a dynamic radius"""
def ring(col, rad):

    # Set the fill
    pen.fillcolor(col)

    # Start filling the color
    pen.begin_fill()

    # Draw a circle
    pen.circle(rad)

    # Ending the filling of the color
    pen.end_fill()

######################### Main Section #########################
# pen.up              --> move turtle to air
# pen.down            --> move turtle to ground
# pen.setpos          --> move turtle to given position
# ring(color, radius) --> draw a ring of specified color and radius
################################################################

##### Draw ears #####
# Draw first ear
pen.up()
pen.setpos(-7*float(PandaSize), 6*float(PandaSize))
pen.down()
ring('black', 3*float(PandaSize))

# Draw second ear
pen.up()
pen.setpos(7*float(PandaSize), 6*float(PandaSize))
pen.down()
ring('black', 3*float(PandaSize))

##### Draw face #####
pen.up()
pen.setpos(0, -6*float(PandaSize))
pen.down()
ring('white', 8*float(PandaSize))

##### Draw eyes black #####

# Draw first eye
pen.up()
pen.setpos(-3.6*float(PandaSize), 2*float(PandaSize))
pen.down()
ring('black', 1.6*float(PandaSize))

# Draw second eye
pen.up()
pen.setpos(3.6*float(PandaSize), 2*float(PandaSize))
pen.down()
ring('black', 1.6*float(PandaSize))

##### Draw eyes white #####

# Draw first eye
pen.up()
pen.setpos(-3.6*float(PandaSize), 2.4*float(PandaSize))
pen.down()
ring('white', 0.8*float(PandaSize))

# Draw second eye
pen.up()
pen.setpos(3.6*float(PandaSize), 2.4*float(PandaSize))
pen.down()
ring('white', 0.8*float(PandaSize))

##### Draw nose #####
pen.up()
pen.setpos(0, -2*float(PandaSize))
pen.down()
ring('black', float(PandaSize))

##### Draw mouth #####
pen.up()
pen.setpos(0, -2*float(PandaSize))
pen.down()
pen.right(90)
pen.circle(float(PandaSize), 180)
pen.up()
pen.setpos(0, -2*float(PandaSize))
pen.down()
pen.left(360)
pen.circle(float(PandaSize), -180)
time.sleep(100)
pen.hideturtle()

# https://www.geeksforgeeks.org/draw-panda-using-turtle-graphics-in-python/