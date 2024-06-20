# import module
import turtle

# number of sides
n = input(" Number of sides >> ")
dl = input(" Distance between the lines >> ")

# initiate pen
pen = turtle.Turtle()
pen.pensize(input(" Pen Size >> "))

# loop to draw a side
for i in range(int(n)):
    # drawing side of length i*10
    pen.forward(i * int(dl))

    # changing direction of pen by 144 degrees in clockwise
    pen.right(144)

# closing the instance
turtle.done

# https://www.geeksforgeeks.org/draw-spiraling-star-using-turtle-in-python/