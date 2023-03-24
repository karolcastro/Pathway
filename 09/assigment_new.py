food_list = []
price_list = []
list_items = None
total = 0

print("""
Please select one of the following: 
1. Add item
2. View cart
3. Remove item
4. Compute total
5. Quit
""")

while True:
    action = int(input("Please enter an action:"))
    if action == 5:
        print("Thank you. Goodbye.")
        break
    if action == 1 :
        add_item = input("What item would you like to add? " ).lower()
        price = int(input(f"What is the price of {add_item}?: $ " ))
        food_list.append(add_item)
        price_list.append(price)
        print(f"'{add_item}' has been added to the cart.")

    if action == 2 :      
        print()
        print(f"The Items are: ")
        for item in range(len(food_list)):
            food = food_list[item]
            price = price_list[item]
            print(f"{item}. {food} - ${price}")
    
    if action == 4 :
        for item in range(len(price_list)):
            total += price_list[item]
            
            print(f"the total is: $ {total}")