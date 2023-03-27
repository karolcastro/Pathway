#outra maneira de abrir o arquivo sem precisar colcoar a linha de comando para fechar o arquivo
#year_interest = input("Enter the year of interest: ")
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
        life_expectancy = line_parts[3]
        
        max_life = -1
        min_life = min(life_expectancy)
        
        max_country = ""
        max_year = max(country_year)
        min_country = min(country_fisrt)
        min_year = min(country_year)
        
        chosen_year = ""
        
year_interest = int(input("Enter the year of interest: "))
        
if chosen_year == year_interest:
    chosen_year = year_interest
    

    print()
    print(f"For the year {year_interest}:")
    #print(f"The average life expectancy across all countries was {list_len}")
    print(f"The max life expectancy was in {max_country} with {max_life} ")
    print(f"The min life expectancy was in {min_country} with {min_life}")
    
    if life_expectancy > max_life:
        max_life = life_expectancy
        max_country = country_fisrt
        
    print()
    print(f"The overall max life expectancy is: {max_life[3]} from {max_country} in {max_year}")
    print(f"The overall min life expectancy is: {min_life[3]} from {min_country} in {min_year}")
