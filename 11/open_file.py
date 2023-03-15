
#Localizar o arquivo
file_to_open = open('/Users/karolinydecastro/Documents/Python-Curso/11/exemplo_file.txt')

#abrir o arquivo
for line in file_to_open:
    print(line)

#sempre fechar o arquivo 
file_to_open.close()

################################################################
#outra maneira de abrir o arquivo sem precisar colcoar a linha de comando para fechar o arquivo

with open('/Users/karolinydecastro/Documents/Python-Curso/11/exemplo_file.txt') as file_to_open:
    for line in file_to_open:
        print(line)
        
    print('GoodBye')
print()
print('The file is closed now')