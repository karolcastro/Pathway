carts = []
print("""
Please select one of the following: 
1. Add item
2. View cart
3. Remove item
4. Compute total
5. Quit
""")

action = int(input("Please enter an action:"))

while action != 5:
    if action == 1:
        add_item = input("What item would you like to add? " ).lower()
        price = float(input(f"What is the price of {add_item}? " ))
        carts.append(add_item)
        carts.append(price)
        print(f"'{add_item}' has been added to the cart.")
        
        
    else:
        action == 5
        action = int(input("Please enter an action:"))
        

#view
    if action == 2:
        print()
        print("cart")
        break
    