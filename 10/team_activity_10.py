print("Enter the names and balances of bank accounts (type: quit when done): ")
print()


#Create two lists, one for the names of the bank accounts, and one for the balances.
bank_accounts_list = []
account_none = None
balances_list = []

#Ask the user for the name of the bank account and then for it's current balance. 
#Keep looping until the user types "quit" for the name of an account. For each one, add the name and the balance to the appropriate list.

while account_none != "quit":
    account_none = input("What is the name of this account? ")
    
    #adicionando a conta e o saldo
    if account_none != "quit":
        balances_none = float(input("What is the balance? "))
        
        bank_accounts_list.append(account_none)
        balances_list.append(balances_none)
        
#mostrando a conta e o saldo       
print()
print("The accounts and balances are: ")
for account_none in bank_accounts_list:
    print(f"{account_none} - {balances_none}")
    
#inicio da soma
total_balance = 0

#mostrar as conta com o indice
print()
print("Account Information: ")
for index in range(len(bank_accounts_list)):
    account_none = bank_accounts_list[index]
    print(f"{index}. {bank_accounts_list[index]} - ${balances_list[index]}")
    
    total_balance = balances_list[index]
    
average_balance = total_balance /len(balances_list)

print()
print(f"Total Balance: ${total_balance:.2f} ")
print(f"Average: ${average_balance:.2f}")
        
