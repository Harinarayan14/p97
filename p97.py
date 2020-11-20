# import random for finding a random number
import random;

# Random Number 
number = random.randint(1,100);

# Text
print("Number Guessing Game");
print("Guess from 1 to 100");
print("You have 10 chances.");

#Chances
chances =0;

# While Loop
while chances < 10:

    # Input
    guess = int(input("Enter your guess "))

    # Game win
    if (guess == number):
        print("Congratulation YOU WON!!!")
        print("Chances Taken: ")
        print(chances)
        break

    # Game Continue
    elif (guess < number):
        print("Your guess was low: Guess a number higher than", guess)
    else:
        print("Your guess was high: Guess a number lower than", guess)
    chances += 1

    # Score
    print("Chances Taken: ")
    print(chances)
    print("Chances Left: ")
    print(10-chances)

# Game Over
if chances >= 10:
    print("YOU LOSE!!! The number is", number)