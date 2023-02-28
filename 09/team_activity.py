numbers = []
new_numbers = ""
total_numbers = 0

while new_numbers != 0:
    new_numbers = input("Enter a list of numbers, type 0 when finished: ")
    
    if new_numbers != 0:
        numbers.append(new_numbers)
print()

for number in numbers:
    total_numbers += number
    
print("Total numbers are: " + total_numbers)
  