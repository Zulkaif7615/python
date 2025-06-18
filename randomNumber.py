    
import random

while True:
    guess = random.randint(1,10)
    num = int(input("Guess Rnadom number between 1 to 10:\n"))


    if (num == guess):
      print("Congrats! you guess a correct number")
    elif (num > guess):
      print("you number is so high")
    elif (num < guess):
       print("your number is low")
    print(f"Random number is: {guess} and your number is:{num}")
    
    