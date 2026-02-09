import sys
sys.set_int_max_str_digits(100000)


def fibonacci(limit):
    a = 0
    b = 1
    count = 1
    while count < limit:
        yield a
        c = a + b
        a = b
        b = c
        count += 1


count = 1
for number in fibonacci(1000000):
    if count == 5:
        print(number)
    elif count == 200:
        print(number)
    elif count == 1000:
        print(number)
    elif count == 100000:
        print(number)
        break
    count += 1
