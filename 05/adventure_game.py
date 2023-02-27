while True:
    start_game = input("Do you want to play the game (YES/NO) ?").lower()
    print("The answer must be YES or NO")

    if start_game == "yes":
        
        start_game = input("You are walking on the street, would you like to turn LEFT or RIGHT ? ").lower()
        if start_game == "left":
            print("The answer must be LEFT or RIGHT ")
            
            start_game = input("You see a monster in your front, would you like to RUN or ATTACK ?").lower()
            
            if start_game == 'attack':
                print("That was not a great idea and you lost the game ! :( ")
            else:
                print("Good choice, you are safe ! :)")
                
                start_game = input("You see a telephone in your front, would you like to CALL the police or KEEP on the way ? ").lower()
                print("The answer must be CALL the police or KEEP  ")
                if start_game == "call":
                    print("You Won the game !!")
                else:
                    print(" The monster sow you and got you")
        elif start_game == "right":
            print("That`s a good choice, but you are walking in the right direction and you fall and hurt your leg and you nedd to come back to your house. ")
            
        else:
            print("Invalid answer, you lost the game !")

    else:
        print("Thanks for playing !")
        break