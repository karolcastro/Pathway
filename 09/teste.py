print("Welcome to the Shopping cart program!")
print()

print("Please select one of the following: ")
print("1. Add item :")
print("2. View cart")
print("3. Remove item")
print("4. Compute total")
print("5. Quit")
print()

carts = []
action = ""

while action != "Quit":
    action = input("Please enter an action: ")
    if action != "Quit":
        carts.append(action)
        
        
    if action == "1":
        add_item = input("What item would you like to add? " ).lower()
        price = float(input(f"What is the price of {add_item}? " ))
        carts.append(add_item)
        carts.append(price)
        print(f"'{add_item}' has been added to the cart.")
        
    if action == "2":
        number_of_item = len(carts)
        print(f"The contents of the shopping cart are:")
        for index in range(number_of_item):
            letter = carts[index]
            print(f"{index}. item: {letter}  - ${price}")
            
    if action == "3":
        print("Which item would you like to remove? ")
        remove_item = carts.remove(carts[index])
        
    
    
    
       