#outra maneira de abrir o arquivo sem precisar colcoar a linha de comando para fechar o arquivo
import math


with open('/Users/karolinydecastro/Documents/Python-Curso/11/life-expectancy.csv') as file_to_open:
    next(file_to_open)
    output = []
    for line in file_to_open:
        #limpar os espacos
        clean_line = line.strip()
        line_parts = clean_line.split(",")
        
        
        #acessar cada index de acordo com a entidade
        country_fisrt = line_parts[0].strip()
        country_code = line_parts[1]
        country_year = line_parts[2]
        life_expectancy = float(line_parts[3])
        
        
        output.append([country_fisrt, country_code, country_year, life_expectancy])

max_life_expectancy = max(output, key=lambda x: x[3])
min_life_expectancy = min(output, key=lambda x: x[3])

print(f"The overall max life expectancy is {max_life_expectancy[3]} in {max_life_expectancy[0]}")
print(f"The overall min life expectancy is {min_life_expectancy[3]} in {min_life_expectancy[0]}")
         

        