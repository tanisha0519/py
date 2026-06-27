import random
number=random.randint(1,100)
print("===number guessing game===")
print("Guess a number between 1 and 100")
while True:
    gues=int(input("enter your guess:"))
    if gues==number:
        print("congratulations!you guessed the correct number")
        break
    elif gues < number:
     print("toolow!,try again")
    else:
     print("too high!,try again")