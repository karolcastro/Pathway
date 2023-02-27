secret_word = "Mormon"
chances = secret_word.__le__(secret_word)

print ("Welcome to the guessing game! ")

guess = input("What is your guess? ").lower()
print(f"You guess is = {guess} .")
print()

while guess != secret_word:
    guess = input("Sorry, the guess must have the same number of letters as the secret word. ")

print("Congratulations! You guessed it!")
print()


