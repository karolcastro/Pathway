#outra maneira de abrir o arquivo sem precisar colcoar a linha de comando para fechar o arquivo
#year_interest = input("Enter the year of interest: ")
with open('/Users/karolinydecastro/Documents/Python-Curso/11/life-expectancy.csv') as file_to_open:
    
    year_interest = int(input("Enter the year of interest: "))
    next(file_to_open)
    output = []
    
    for line in file_to_open:
        #limpar os espacos
        clean_line = line.strip()
        line_parts = clean_line.split(",")
        
        #acessar cada index de acordo com a entidade
        country_fisrt = line_parts[0].strip()
        country_code = line_parts[1]
        country_year = int(line_parts[2])
        life_expectancy = float(line_parts[3])
        
        
        output.append([country_fisrt, country_code, country_year, life_expectancy])

max_life_expectancy = max(output, key=lambda x: x[3])
min_life_expectancy = min(output, key=lambda x: x[3])
maxYear_expectancy = max(output, key=lambda x: x[2])
minYear_expectancy = min(output, key=lambda x: x[2])
max_country = max(output, key=lambda x: x[0])
min_country = min(output, key=lambda x: x[0])
#list_len = len(output)
#list_average = reduce(operator.add, output) / list_len

 
print()
print(f"The overall max life expectancy is: {max_life_expectancy[3]} from {max_life_expectancy[0]} in {maxYear_expectancy[2]}")
print(f"The overall min life expectancy is: {min_life_expectancy[3]} from {min_life_expectancy[0]} in {minYear_expectancy[2]}")

if year_interest == country_year:
    if year_interest > max_life_expectancy[3]:
        year_interest = max_life_expectancy[3]
        max_new_coutry = country_fisrt
    
    
    if year_interest < min_life_expectancy[3]:
        year_interest = min_life_expectancy[3]
        min_new_coutry = country_fisrt

print()
print(f"For the year {year_interest}:")
#print(f"The average life expectancy across all countries was {list_len}")
print(f"The max life expectancy was in {max_country[0]} with {max_life_expectancy[3]} ")
print(f"The min life expectancy was in {min_country[0]} with {min_life_expectancy[3]}")

    
         

        