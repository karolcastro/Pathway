
#print("This is line one.", end="")

#print("This is line two.")

    
word = "Commitment"
number_of_letters = input("What is your favorite letter?")

for index in word:
    if index.lower() == number_of_letters:
        print(index.upper(),end="")
    else:
        print(index.lower(),end="")
print()

for index in word:
    if index.lower() == number_of_letters:
        print("_", end="")
    else:
        print(index.lower(),end="")
        
        
#ex 2
word = "In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost."
number_of_letters = int(input("Please enter a number: "))

for i, index in enumerate(word):
    if i % number_of_letters == 0:
        print(index.upper(), end="")
    else:
        print(index.lower(), end="")
print()
        
