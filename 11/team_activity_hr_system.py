with open('/Users/karolinydecastro/Documents/Python-Curso/11/hr_system.txt') as open_file:
    
    for line in open_file:
        cleaned_line = line.strip()
        line_parts = cleaned_line.split()
        
        #print(line)
        #print(line_parts)
    
        name = line_parts[0].capitalize()
        title = line_parts[2].capitalize()
        id = line_parts[1]
        salary = float(line_parts[3])
        
        salary_amount = salary/24
        
        if title == "Engineer":
            salary_amount = salary_amount + 1000
    
        print()
        print(f"{name} (ID: {id}, {title}) - ${salary_amount:.2f}")

