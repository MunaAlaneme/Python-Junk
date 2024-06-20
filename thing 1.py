import math
import time
from decimal import *
import datetime as dt

datetimer = dt.datetime.now()
print("Date/Time: ", datetimer) # datetime shows milliseconds.
timer = time.ctime()
print("The time is ",timer) # time shows the day of the week.

countdown = input(" enter countdown >> ")
var = Decimal(countdown)
print(round(Decimal(var)*10)/10)
while var >= 0.01:
    time.sleep(1)
    var = var - 1
    print(round(Decimal(var)*10)/10)

loop = 1
while loop == 1:
    var1 = input(" enter a number  >> ")
    var2 = input(" enter a sign  >> ")
    var3 = input(" enter another number  >> ")

    if var2 == "/":
        print(Decimal(var1) / Decimal(var3))
    elif var2 == "*":
        print(Decimal(var1) * Decimal(var3))
    elif var2 == "+":
        print(Decimal(var1) + Decimal(var3))
    elif var2 == "-":
        print(Decimal(var1) - Decimal(var3))
    elif var2 == "**":
        print(Decimal(var1) ** Decimal(var3))
    elif var2 == "%":
        print(Decimal(var1) % Decimal(var3))
    elif var2 == "//":
        print(Decimal(var1) // Decimal(var3))
    elif var2 == "pow":
        print(pow(Decimal(var1), Decimal(var3)))