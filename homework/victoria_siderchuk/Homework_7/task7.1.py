lucky_number = 8

while True:
    user_input = int(input('Enter a number: '))
    if user_input == lucky_number:
        print('Поздравляю! Вы угадали!')
        break
    else:
        print('попробуйте снова')
