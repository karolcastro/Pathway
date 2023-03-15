colors = "red green blue yellow"

color_parts = colors.split()
print(colors) #escrita normal
print(color_parts)#escrita com o split usando a virgula 

#definindo a variavel que sera impressa no index que deseja
second = color_parts[1]
print(second)

# usando o split para separar as palavras pela letra que escolher 
color_parts = colors.split("e")
print(colors) #escrita normal
print(color_parts)#separando de acordo com a letra "e"

#separando quando ja tem virgula
colors = "red, green, blue, yellow"

color_parts = colors.split(",")
print(colors) #escrita normal
print(color_parts)#