# Import tkinter
import tkinter
from tkinter import *
from tkinter import ttk
import pygame
from decimal import *

# Globally declare the expression variable
expression = ""

# Function to update expression in the text entry box
def press(num):
    # Point out the global expression variable
    global expression
    # concatenation of string
    expression = expression + str(num)
    # Update the expression by using set method
    equation.set(expression)
    pygame.mixer.Sound.play(clickSound)

def backspace():
    # Point out the global expression variable
    global expression
    # concatenation of string
    expression = expression[:len(expression)-1]
    # Update the expression by using set method
    equation.set(expression)
    pygame.mixer.Sound.play(clickSound)

# Function to evaluate the final expression
def equalpress():
    # Try and except statement is used for handling the errors like zero division error etc.
    # Put that code inside the try block which may generate the error
    try:
        # Point out the global expression variable
        global expression
        # Evaluate the expression
        getcontext().prec = 20
        total = Decimal(eval(expression))
        # Update the expression by using set method
        equation.set(str(total))
        # Clear the expression
        expression = str(total)
        pygame.mixer.Sound.play(clickSound)
    except ZeroDivisionError:
        # Update the expression by using set method
        equation.set("Error: Division by zero")
        # Clear the expression
        expression = ""
        pygame.mixer.Sound.play(errorSound)
    except SyntaxError:
        # Update the expression by using set method
        equation.set("Error: Syntax Error")
        # Clear the expression
        expression = ""
        pygame.mixer.Sound.play(errorSound)
    except NameError:
        # Update the expression by using set method
        equation.set("Error: Name Error")
        # Clear the expression
        expression = ""
        pygame.mixer.Sound.play(errorSound)
    except:
        # Update the expression by using set method
        equation.set("Error: Unknown Error")
        # Clear the expression
        expression = ""
        pygame.mixer.Sound.play(errorSound)

# Function to clear the contents of text entry box
def clear():
    global expression
    expression = ""
    equation.set("")
    pygame.mixer.Sound.play(clickSound)

pygame.init()
clickSound = pygame.mixer.Sound("GameLauncher/assets/apps/GUICalculator/assets/audio/Mouse Click - Sound Effect (HD)2.wav")
errorSound = pygame.mixer.Sound("GameLauncher/assets/apps/GUICalculator/assets/audio/423169__plasterbrain__pc-game-ui-error.wav")

# Driver code
# Create a GUI Window
gui = Tk()
# Set the background color of GUI window
gui.configure(background="dark green")
# Set the title of GUI Window
gui.title("MunaAlaneme's Simple GUI Calculator")
# Set the geometry of GUI Window
gui.geometry("520x650")
# StringVar() is the variable class.
# We create an instance of this class.
equation = StringVar()

# Create the text entry box for showing the expression
expression_field = Entry(gui, textvariable=equation, font=('Dosis 30'))
# Grid method is used for placing the widgets at respective positions in table like structure
expression_field.grid(columnspan=5, row=10, ipady=10, ipadx=50)
# Create buttons and place at a particular location inside the root window.
# When user presses the button, the command or function affiliated to that button is executed.
button1 = Button(gui, text='1', fg='black', bg='green', command=lambda: press(1), height=1, width=6, font=('Dosis 30'))
button1.grid(row=2, column=0)
button2 = Button(gui, text='2', fg='black', bg='green', command=lambda: press(2), height=1, width=6, font=('Dosis 30'))
button2.grid(row=2, column=1)
button3 = Button(gui, text='3', fg='black', bg='green', command=lambda: press(3), height=1, width=6, font=('Dosis 30'))
button3.grid(row=2, column=2)
button4 = Button(gui, text='4', fg='black', bg='green', command=lambda: press(4), height=1, width=6, font=('Dosis 30'))
button4.grid(row=3, column=0)
button5 = Button(gui, text='5', fg='black', bg='green', command=lambda: press(5), height=1, width=6, font=('Dosis 30'))
button5.grid(row=3, column=1)
button6 = Button(gui, text='6', fg='black', bg='green', command=lambda: press(6), height=1, width=6, font=('Dosis 30'))
button6.grid(row=3, column=2)
button7 = Button(gui, text='7', fg='black', bg='green', command=lambda: press(7), height=1, width=6, font=('Dosis 30'))
button7.grid(row=4, column=0)
button8 = Button(gui, text='8', fg='black', bg='green', command=lambda: press(8), height=1, width=6, font=('Dosis 30'))
button8.grid(row=4, column=1)
button9 = Button(gui, text='9', fg='black', bg='green', command=lambda: press(9), height=1, width=6, font=('Dosis 30'))
button9.grid(row=4, column=2)
button0 = Button(gui, text='0', fg='black', bg='green', command=lambda: press(0), height=1, width=6, font=('Dosis 30'))
button0.grid(row=5, column=0)
buttonplus = Button(gui, text='+', fg='white', bg='green', command=lambda: press("+"), height=1, width=6, font=('Dosis 30'))
buttonplus.grid(row=2, column=3)
buttonminus = Button(gui, text='-', fg='white', bg='green', command=lambda: press("-"), height=1, width=6, font=('Dosis 30'))
buttonminus.grid(row=3, column=3)
buttonmultiply = Button(gui, text='*', fg='white', bg='green', command=lambda: press("*"), height=1, width=6, font=('Dosis 30'))
buttonmultiply.grid(row=4, column=3)
buttondivide = Button(gui, text='÷', fg='white', bg='green', command=lambda: press("/"), height=1, width=6, font=('Dosis 30'))
buttondivide.grid(row=5, column=3)
buttonpow = Button(gui, text='^', fg='white', bg='green', command=lambda: press("**"), height=1, width=6, font=('Dosis 30'))
buttonpow.grid(row=6, column=0)
buttonfloordivide = Button(gui, text='Floor ÷', fg='white', bg='green', command=lambda: press("//"), height=1, width=6, font=('Dosis 30'))
buttonfloordivide.grid(row=6, column=1)
buttonmod = Button(gui, text='mod', fg='white', bg='green', command=lambda: press("%"), height=1, width=6, font=('Dosis 30'))
buttonmod.grid(row=6, column=2)
buttonequal = Button(gui, text='=', fg='white', bg='green', command=lambda: equalpress(), height=1, width=6, font=('Dosis 30'))
buttonequal.grid(row=5, column=1)
buttonclear = Button(gui, text='Clear', fg='white', bg='green', command=lambda: clear(), height=1, width=6, font=('Dosis 30'))
buttonclear.grid(row=5, column=2)
buttondecimal = Button(gui, text='.', fg='white', bg='green', command=lambda: press("."), height=1, width=6, font=('Dosis 30'))
buttondecimal.grid(row=6, column=3)
buttonBracketOpen = Button(gui, text='(', fg='white', bg='green', command=lambda: press("("), height=1, width=6, font=('Dosis 30'))
buttonBracketOpen.grid(row=7, column=0)
buttonBracketClose = Button(gui, text=')', fg='white', bg='green', command=lambda: press(")"), height=1, width=6, font=('Dosis 30'))
buttonBracketClose.grid(row=7, column=1)
buttonBackspace = Button(gui, text='←', fg='white', bg='green', command=lambda: backspace(), height=1, width=6, font=('Dosis 30'))
buttonBackspace.grid(row=7, column=2)

for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_1:
            press(1)
        if event.key == pygame.K_2:
            press(2)
        if event.key == pygame.K_3:
            press(3)
        if event.key == pygame.K_4:
            press(4)
        if event.key == pygame.K_5:
            press(5)
        if event.key == pygame.K_6:
            press(6)
        if event.key == pygame.K_7:
            press(7)
        if event.key == pygame.K_8:
            press(8)
        if event.key == pygame.K_9:
            press(9)
        if event.key == pygame.K_0:
            press(0)
        if event.key == pygame.K_PLUS:
            press("+")
        if event.key == pygame.K_MINUS:
            press("-")
        if event.key == pygame.K_SLASH:
            press("/")
        if event.key == pygame.K_ASTERISK:
            press("*")
        if event.key == pygame.K_POWER:
            press("^")
        if event.key == pygame.K_BACKSLASH:
            press("//")
        if event.key == pygame.K_PERCENT:
            press("%")
        if event.key == pygame.K_EQUALS or event.key == pygame.K_ENTER:
            equalpress()
        if event.key == pygame.K_DELETE:
            clear()
        if event.key == pygame.K_BACKSPACE:
            backspace()
        if event.key == pygame.K_PERIOD:
            press(".")
        if event.key == pygame.K_LEFTBRACKET:
            press("(")
        if event.key == pygame.K_RIGHTBRACKET:
            press(")")
        

# Start the GUI
gui.mainloop()


# https://www.tutorialspoint.com/how-to-set-the-font-size-of-entry-widget-in-tkinter#:~:text=The%20Entry%20widget%20in%20tkinter,define%20an%20inline%20widget%20constructor.
# https://www.geeksforgeeks.org/python-simple-gui-calculator-using-tkinter/
