print()
grade_percentage = float(input("What is the grade percentage ? "))

if grade_percentage >= 90:
    letter_grade = "A"
    
elif grade_percentage >= 80:
    letter_grade = "B"
    
elif grade_percentage >= 70:
    letter_grade = "C"
    
elif grade_percentage >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"
    
sign = ""

last_digit = grade_percentage % 10

if last_digit >= 7:
    sign = "+"
elif last_digit < 3:
    sign = "-"
else:
    sign = ""
    
if grade_percentage >= 93:
    sign = ""

if grade_percentage == 70:
    sign = ""

print()
print(f"Your letter grade is: {letter_grade}{sign}.")

if grade_percentage >= 70:
    print("Congratulations! You passed the class!")
    print()
else:
    print("You must have at least a 70 to pass the class. Stay focused and you'll get it next time!")
    print()
