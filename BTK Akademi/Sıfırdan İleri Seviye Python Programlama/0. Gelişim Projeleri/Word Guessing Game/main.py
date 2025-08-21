import random

name = input("What is your name: ")

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board']
word = random.choice(words)

guesses = ''
turns = 12

while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char,end="")
        else:
            print("-", end="")
            failed += 1 
    guess = input("\nGuess a character:")
    guesses += guess        
    print("\n"+"*"*20)         
    if failed == 0:
        print(f"\nYou Win {name}!")
        print("The word is: ", word)
        break        
    if guess not in word:
        turns -= 1
        print("\nWrong")
        print("You have", turns, 'more guesses')
else:
    print(f"\nYou Lose {name}")
    print("The word is: ", word)