shopping_cart = [
    ["Chips", 2.99],
    ["Bread", 2.50],
    ["Milk", 3.19],
    ["Ice Cream", 6.99],
    ["Cheese", 5.99],
    ["Candy bar", 0.99]
]

max_price = -1
max_product = ""

for item in shopping_cart:
    product_name = item[0] #o produto esta na primeira posicao
    price = item[1] #o preco esta na segunda posicao da lista
    
    #se meu preco for igual ao meu preco maximo entao o preco maximo vai ser o meu preco
    if price > max_price:
        max_price = price
        max_product = product_name

#mostrar o preco maximo
print()        
print(f"The maximum price is: {max_price}")
print(f"The product with the maximum price is: {max_product}")
print()