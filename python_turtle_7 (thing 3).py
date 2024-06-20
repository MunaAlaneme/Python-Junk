# display the text "hello world" ✔️
# create a list to store 3 variables ✔️ ✔️
# print 6 emojis ✔️
# using a conditional statement .. display the text "successfull" if 6 != 6 else display "not successful" ✔️

import turtle
import time

pen = turtle.Turtle()

pen.color('darkgreen')
pen.write("hello world", font=("Dosis", 35, "bold"))
var1 = input(" Enter variable 1 >> ")
var2 = input(" Enter variable 2 >> ")
var3 = input(" Enter variable 3 >> ")
list1 = [var1, var2, var3]
list2 = f"{var1}{var2}{var3}"
print(list1)
print(list2)
var4 = input(" Enter variable 4 >> ")
var5 = input(" Enter variable 5 >> ")
list3 = [var1, var2, var3, var4, var5]
list4 = f"{var1}{var2}{var3}{var4}{var5}"
print(list3)
print(list4)

print("\U0001F429 429 poodle")
print("\U0001F690 690 bus")
print("\N{nerd face} nerd!")
print("\U0001F420 420 fish")
print("\U0001F999 999 llama")
print("\U0001F6F9 6F9 skateboard")

time.sleep(3)

pen.clear()

pen.write("6 != 6", font=("Dosis", 35, "bold"))
time.sleep(2)
pen.clear()
if 6 != 6:
    pen.write("Successful! 6 != 6.", font=("Dosis", 35, "bold"))
else:
    pen.write("Not successful 6 == 6.", font=("Dosis", 35, "bold"))
time.sleep(2)