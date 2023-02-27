print("You need to make a choice of what to do.  Will you do CHOICEA or CHOICEB")
responseAB = input("What will you do?")
if responseAB.lower() == "choicea":
    print("You picked choicea now what will you do. Will you CHOICEC or CHOICED or CHOICEE")
    responseCDE = input("What will you do?")
    if responseCDE.lower() == "choicec":
        print("You picked choicec.  Now what will you do CHOICEH or CHOICEI")
        responseHI = input("What will you do?")
        if responseHI.lower() == "choiceh":
            print("You picked choiceh")
        elif responseHI.lower() == "choicei":
            print("You picked choicei")
        else:
            print("Invalid choice")
    elif responseCDE.lower() == "choiced":
        print("You picked choiced")
    elif responseCDE.lower() == "choicee":
        print("You picked choicee")
    else:
        print("Invalid choice")
elif responseAB.lower() == "choiceb":
    print("You picked choiceb now what will you do. Will you CHOICEF or CHOICEG")
    responseFG = input("What will you do?")
    if responseFG.lower() == "choiceF":
        print("You picked choicef")
    elif responseFG.lower() == "choiceg":
        print("You picked choiceg")
    else:
        print("Invalid choice")
else:
    print("Invalid choice")