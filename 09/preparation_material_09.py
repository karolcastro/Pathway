#list

#/clients = []

# clients.append("Emily ")
# clients.append("Sara ")

# for client in clients:
#     print(client)
    
    
#put all the names in the same list

# clients = ["Sara", "Emily", "Brian"]

# for client in clients:
#     print(client)

#perguntando e adicionando o que o ususario inputar

clients = []

new_client = ""

while new_client != "quit":
    new_client = input("What is the name of the client? ")
    clients.append(new_client)

for client in clients:
    print(client)
    