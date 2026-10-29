# reqeust user to input their age
age = int(input("please enter your age\n"))
if age > 100:
    print("Sorry, you are dead")
elif age >= 40 and age < 65:
    print("You're over the hill")
elif age >= 65:
    print(" Enjoy your retirement")
elif age < 13:
    print(" “You qualify for the kiddie discount")
elif age == 21:
    print("Congrates on your 21st")
else:
    print("Age is just a number")      
