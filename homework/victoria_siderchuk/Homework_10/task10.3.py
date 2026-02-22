def select_operation(func):

    def wrapper(first, second):
        if first < 0 or second < 0:
            return func(first, second, '*')
        elif first == second:
            return func(first, second, '+')
        elif first > second:
            return func(first, second, '-')
        elif first < second:
            return func(first, second, '/')

    return(wrapper)


@select_operation
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return first / second
    elif operation == '*':
        return first * second


first = int(input('Enter first number: '))
second = int(input('Enter second number: '))

print(calc(first, second))
