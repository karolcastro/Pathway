numbers = [42, 25, 18, 83, 23, 85, 38, 2]

largest_number = numbers[0]

#localizar o maior numero percorrendo a lista 
for number in numbers:
    if number > largest_number:
        largest_number = number

#mostrar o maior numero da lista
print()      
print(f"The largest number is: {largest_number}")
print()