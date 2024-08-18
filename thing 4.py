import time

# July 2-3, 2024

print("NOBODY CARES!")
x=0
y=1
z=0.15
while True:
    x+=y
    print(x)
    time.sleep(z)
    if (x >= 40):
        y = 2
        z=0.13
    if (x == 100):
        person=input('What is your name? ')
        print("Hello, ", person)
    if (x >= 100):
        y = 3
        z=0.11
    if (x >= 250):
        y = 4
        z=0.1
    if (x >= 450):
        y = 5
        z=0.09
    if (x >= 750):
        y = 8
        z=0.08
    if (x >= 1150):
        y = 9
        z=0.075
    if (x >= 1600):
        y = 10
        z=0.065
    if (x >= 2100):
        y = 12
        z=0.05
    if (x >= 2700):
        y = 15
        z=0.04
    if (x >= 3600):
        y = 20
        z=0.03
    if (x >= 6000):
        y = 50
        z=0.025