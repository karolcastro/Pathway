
word = "In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost."


#Pergunta ao usuario a posicao
# number_of_letters = int(input("Please enter a number: "))
# print()

# #nesta parte ele faz para cada letra(i) na posicao (index) dentro da palavra(word) em letra maiuscula 
# for i, index in enumerate(word):
#     if i % number_of_letters == 0:
#         print(index.upper(), end="")
#     else:
#         print(index.lower(), end="")
# print()


#receipts list

receipts = [12.24, 18.50, 4.99, 21.75]

running_total = 0

for receipt in receipts:
    running_total = running_total + receipt

# Display the total
print(f"The total is: {running_total:.2f}") # This displays: The total is: 57.48

