#while loops. 


#Items - each item of a collection or a list
items = ["crayon", "scissors", "paper", "glitter glue", "markers", "pens"]

for item in items:
    print(f"The item is: {item}")

#Numbers - list of numbers
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8]
numbers = range(10)

for number in range(10):
    print(number)

#range - using range.
for i in range(100, 200):
    print(i)
    
#range 2
for i in range(100, 200, 10):
    print(i)
   
#range 3 - por 4 vezes ela vai printar (--10)
for i in range(5):
    print(i)
    for j in range(10, 13):
        print(f"--{j}")
        
#letters - each letter of a string//  vai printar cada letra do nome uma embaixo da outra      
first_name = "Brigham"
for letter in first_name:
    print(f"The letter is: {letter}")

#letters 2 - vai printar a posicao de cada letra uma embaixo da outra
word = "book"
number_of_letters = 4

for index in range(number_of_letters):
    letter = word[index]
    print(f"Index: {index} Letter: {letter}")
    
#dog -  vai perguntar no nome do cachorro e vai contar quantos letras ele tem 
dog_name = input("What is your dog's name? ")
letter_count = len(dog_name)

print(f"Your dog's name has {letter_count} letters")

#book
word = "book"
number_of_letters = len(word) # Notice this can now work for any string

for index in range(number_of_letters):
    letter = word[index]
    print(f"Index: {index} Letter: {letter}")
    

# Notice by using enumerate, we specify both i and letter //  vai prinatr cada letra e a posicao dela
first_name = "Brigham"
for i, letter in enumerate(first_name):
    print(f"The letter {letter} is at position {i}")