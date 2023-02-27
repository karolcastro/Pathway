first_name = "Karol"
last_name = "Costa"
print(first_name + last_name)
print("Hello, " + first_name + " " + last_name)

#you can use functions to modify strings

sentence = "The dog is named Sammy"
print(sentence.upper())
print(sentence.lower())
print(sentence.capitalize())
print(sentence.count("a"))

#the functions help us format strings we save to files and databases, or display to users

first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
print("Hello " + first_name.capitalize() + ' '  + last_name.capitalize() )
