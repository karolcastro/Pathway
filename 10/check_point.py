print("Please enter the items of the shopping list (type: quit to finish):")
print()

cart_items = []
list_items = None

#preparar a lista 
while list_items != "quit":
    list_items = input("Item: ")
   
    #adiciono os items na lista
    if list_items != "quit":
        cart_items.append(list_items)
        
#mostro a minha
print()
print("The shopping list is: ")
for list_items in cart_items:
    print(list_items)

#mostro a lista com o index de cada produto
print()
print("The shopping list with indexes is: ")
for index in range(len(cart_items)):
    list_items = cart_items[index]
    print(f"{index}. {list_items}")
    
#alterar o item na lista
print()
change_item_list = int(input("Which item would you like to change? "))
input_new_item = input("What is the new item: ")

cart_items[change_item_list] = input_new_item

#Mostrar a nova lista com o item alterado
print()
print("The shopping list with indexes is: ")
for index in range(len(cart_items)):
    list_items = cart_items[index]
    print(f"{index}. {list_items}")