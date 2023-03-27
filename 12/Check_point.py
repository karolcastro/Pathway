people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

#criar as variaveis
min_age = 9999
min_name = ""

#percorrer as linhas e limpar os espacos brancos e separar com virgula
for item in people:
    
    line_strip = item.split()
    
    name = line_strip[0]
    age = int(line_strip[1])
    
    if age <  min_age:
        min_age = age
        min_name = name

print()
print(f" The youngest person is: {min_name} with an age of {min_age}")
print()

    