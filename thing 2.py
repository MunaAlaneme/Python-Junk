import math
import time
import datetime as dt

datetimer = dt.datetime.now()
print("Date/Time: ", datetimer) # datetime shows milliseconds.
timer = time.ctime()
print("The time is ",timer) # time shows the day of the week.

var1 = input(" enter number 1 >> ")
var2 = input(" enter number 2 >> ")
print(var1,"+",var2,"=",float(var1)+float(var2)) # add
var3 = float(var1)*float(var2)
print(var1,"*",var2,"=",float(var3)) # multiply

user_text = input(" enter your message >> ")
User_Text = "5 "
User_Text += user_text
print("User Text =",User_Text) # message

# I can do this!

if 5 > -5:
    print("Successful. 5 is greater than -5.")
else:
    print("Unsuccessful. 5 > -5.")

# create 2 variables and add the values of both variables DONE
# create a new variable to store the multiplied value of the variables created above DONE
# print time DONE
# use a comment to write i can do this DONE
# use a conditional statement to figure out if 5 weighs beyond -5 print successful if yes else print unsuccessful DONE
# collect user input and store in a variable .. update the variable with 5 attached to the user's input DONE?