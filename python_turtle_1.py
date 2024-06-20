# import module
import turtle

# initiate pen
pen = turtle.Turtle()

# loop
for loop in range(2):
    pen.dot(50)
    pen.pensize(25)

    # draw something
    i1 = 100
    pen.setposition(60,180)
    while i1 > -1:
        pen.color("#123456")
        pen.circle(i1-100, 5)
        i1 -= 1
        pen.color("#ABCDEF")
        pen.circle(i1-100, 5)
        i1 -= 1
        pen.color("#098765")
        pen.circle(i1-100, 5)
        i1 -= 1

    pen.color("yellow")
    pen.setpos(360,360)
    pen.up()
    pen.circle(180, 200)
    pen.down()

    pen.setpos(200, -180)
    pen.up()
    pen.down()

    pen.setpos(150,360)
    pen.setpos(200,180)

    pen.circle(360,360)

input("Press enter to quit.")