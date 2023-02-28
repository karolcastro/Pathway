friends = ["Luc", "Cris", "Ted"]
tips = [12.25, 13.95, 8.50]

#declarar a variavel fora do loop
running_total = 0

for tip_amount in tips:
    #sera iniciado com 0 e depois ira somar com os valores dentro da lista
    running_total = running_total + tip_amount
    #mesma coisa que a linha de cima 
    running_total += tip_amount

print(f"The total is: {running_total:.2f}")