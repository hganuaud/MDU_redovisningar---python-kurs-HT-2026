import random

num = random.randint(0,99)
amount = 0 

while True:
    amount += 1
    guess = int(input("Guess a number:"))
    if guess > num:
        print("Lower, skill issues bro.")
    elif guess < num:
        print("Higher, skill issues my dude.")
    elif num == guess:
        print("Correct!!")
        print("Amount of guesses:", amount)
        break 

