text1 = 'результат операции: 42'
text2 = 'результат операции: 54'
text3 = 'результат работы программы: 209'
text4 = 'результат: 2'

numb_to_add = 10

# Using index
def calc(result):
    sum = int(result[result.index(':') + 2:]) + numb_to_add
    print(sum)

calc(text1)
calc(text2)
calc(text3)
calc(text4)

# Using split
def calc2(result2):
    sum2 = int(result2.split()[-1]) + numb_to_add
    print(sum2)

calc2(text1)
calc2(text2)
calc2(text3)
calc2(text4)
