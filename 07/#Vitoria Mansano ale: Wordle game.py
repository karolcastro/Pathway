#Vitoria Mansano ale: Wordle game
#play is used to turn off the program later if the user whishes
play=1
while play== 1:
 #Variables declaring
    secret_word="apple" #the word the user needs to guess
    count = 0 #counts the guesses
    play_again="" #asks the player if they want to keep playing later
    hint=''
    letter="_"
    for a in secret_word:
        hint = hint + '_ '
# start of the game
    print("Welcome to the word guessing game!")
    print(f"Your hint is:{hint}")
    print()
    guess=input("What is your guess?").lower()
    print()
#if the guess is equal to the secret word
    if guess == secret_word:
            count=count+1
            print(f"Congratulations! You guessed it! It took you {count} guesses.")
            print()
            play_again=input("Would you like to play again? y/n").lower()
            if play_again == "y":
                play=1
                print()
            elif play_again == "n":
                play=0
#if the strings differ in size
    while guess != secret_word:
        if len(guess) != len(secret_word):
            print("Sorry, the guess must have the same number of letters as the secret word.")
            print()
            count=count+1
            break
#if both strings are equal in size:
        elif len(guess) == len(secret_word):
            if guess != secret_word:
                count=count+1
                hint=''
                for i, a in enumerate(guess):
                    letter = "_ "
                    for j, b in enumerate(secret_word):
                        if(a == b and i == j):
                            letter = a.capitalize() + ' '
                            break
                        elif(a==b):
                            letter = a + ' '
                    hint = hint + letter
                print()
                print(f"Your hint is:{hint}")
                print()
                guess=input("What is your guess?").lower()
                print()
# if the guess is equal to the secret word
            if guess == secret_word:
                count=count+1
                print(f"Congratulations! You guessed it! It took you {count} guesses.")
                print()
                play_again=input("Would you like to play again? y/n").lower()
                if play_again == "y":
                    play=1
                print()
                if play_again == "n":
                    play=0
                print()