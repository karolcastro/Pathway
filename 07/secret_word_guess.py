import random

print("Welcome to the word guessing game!")
print()

secret_word_list = ["Mormon", "Church"]
word = random.choice(secret_word_list).lower()

# variables names
slach = [" _ "]*len(word)
print("Your hint is:" + " ".join(slach))
tries = 6
guessed = False
attemp = 0

# Loop
while tries > 0:
    print()
    guess = input("What is your guess? Enter a letter: ").lower()

    if len(word) == len(guess):
        if word == guess:
            guessed = True
            break
        elif word.upper() == guess:
            tries = tries-1
            print(" ".join(slach))
            print()
            print("Incorrect guess, Left only {} attempts".format(tries))
            print()

    elif len(guess) == 1:
        if guess in word:
            print("Correct guess !")
            print()
            indices = [i for i, j in enumerate(word)if guess == j]
            for index in indices:
                slach[index] = guess
            print(" ".join(slach))
            
        elif guess not in word:
            tries -= 1
            print(" ".join(slach))
            print()
            print("Incorrect guess, Left only {} attemps".format(tries))

    else:
        print()
        print("Invalid guess")
        print()
    if word == " ".join(slach):
        guessed = True
    attemp = attemp + 1
    break
    # end of Loop

if guessed:
    print()
    print("Congratulations! You guessed it !")
    print()

else:
    print()
    print("You lose")
    print()
