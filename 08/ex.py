word = "In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost."
number_of_letters = int(input("Please enter a number: "))

for i, index in enumerate(word):
    if i % number_of_letters == 0:
        print(index.upper(), end="")
    else:
        print(index.lower(), end="")
print()

