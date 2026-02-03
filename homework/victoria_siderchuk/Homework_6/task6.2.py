numbers = list(range(1, 101))

numbers_new = []

for number in numbers:
    if number % 3 == 0 and number % 5 == 0:
        numbers_new.append('FuzzBuzz')
    elif number % 3 == 0:
        numbers_new.append('Fuzz')
    elif number % 5 == 0:
        numbers_new.append('Buzz')
    else:
        numbers_new.append(number)

print(numbers_new)
