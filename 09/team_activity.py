numbers = []
simple_number = None

while simple_number != 0:
    simple_number = int(input("Enter a number and in the finish put 0: "))

    if simple_number != 0:
        numbers.append(simple_number)

print()
print("Numbers are now:" )

for i in numbers:
    print(i)

#iniciando a soma dos numeros
sum = 0

for i in numbers:
    sum += i
print()
print(f"The sum of the numbers are: {sum}")
print()

#iniciando a media dos numeros
count = len(numbers)
average = sum / count

print(f"The average of the numbers is: {average:.2f}")
print()

#iniciando a localizacao do maior
maximo = -1
for i in numbers:
    if i > maximo:
        maximo = i

print(f"The maximum number is: {maximo}")
print()

#iniciando a localizacao do menor
small =  99999999999

for i in numbers:
    if i > 0 and i < small:
        small = i

print(f"The minimum number is: {small}")
print()

sorted_list = sorted(numbers)
print("The sorted list is: ")
for i in sorted_list:
    print(i)