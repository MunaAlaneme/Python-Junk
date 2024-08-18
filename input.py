# July 5-8, 2024
import decimal
from decimal import *
lunch = input("What do you want for lunch? ")
if lunch == "pizza": print("eat pizza")
elif lunch == "chicken finger": print("eat chicken fingers")
elif lunch == "mac and cheese": print("eat mac and cheese")
elif lunch == "chicken nugget": print("eat chicken nuggets")
else: print("SKIP LUNCH!")

money_made = Decimal(input("How much money do you make? "))
print("$"+str(Decimal(money_made)))
