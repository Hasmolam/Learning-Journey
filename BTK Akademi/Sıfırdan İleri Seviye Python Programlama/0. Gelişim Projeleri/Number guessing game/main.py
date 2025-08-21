from random import randint

try:
    minNumber = int(input("Min: "))
    maxNumber = int(input("Max: "))
    if minNumber >= maxNumber:
        print("Invalid input. By default, input between 0-100 will be accepted!")
        minNumber = 0
        maxNumber = 100
    myNumber = int(randint(minNumber, maxNumber))
except ValueError:
    print("Please enter a number!")




guess = int()
guessIndex = 1
print(f"Your total number of chances 7".center(50, "*"))
try:
    while guess != myNumber and guessIndex < 8:
        guess = int(input(f"Guess {guessIndex}: "))
        if guess == myNumber:
            print("Correct!")
            print(f"Total Guesses: {guessIndex}")
            break
        elif guess < myNumber:   
            print("Too low") 
        elif guess > myNumber:   
            print("Too high")
        guessIndex += 1  
    else:
        print(f"You're out of guesses. The answer was {myNumber} .Better Luck Next Time!")      
except ValueError:
    print("Please enter a number!")
