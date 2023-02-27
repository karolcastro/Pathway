loan = int(input("How large is the loan (1 to 10) ? "))
credit_history = int(input("How good is your credit history (1 to 10) ? "))
income = int(input("How high is your income (1 to 10) ? "))
payment = int(input("How large is your down payment (1 to 10) ? "))
result = False

if loan >= 5:
    if credit_history >= 7 and income >= 7:
        result = True
    elif credit_history >= 7 or income >= 7:
        if payment >= 5:
            result = True          
        else:
            result = False
    else:
        result = False
else:
    if credit_history < 4:
        result = False
    else:
        if income >= 7 or payment >= 7:
                result = True
        elif income >= 4 and payment >= 4:
            result = True
        else:
            result = False
if result:
    print("You have a good loan. ")
else:
    print("You have a bad loan. ")