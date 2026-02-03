# Task 1
person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person
print(name, last_name, city, phone, country)


# Task 2
text1 = 'результат операции: 42'
text2 = 'результат операции: 514'
text3 = 'результат работы программы: 9'

index1 = text1.index(':') + 2
result1 = text1[index1:]
number1 = int(result1)
sum1 = number1 + 10
print(sum1)

index2 = text2.index(':') + 2
result2 = text2[index2:]
number2 = int(result2)
sum2 = number2 + 10
print(sum2)

index3 = text3.index(':') + 2
result3 = text3[index3:]
number3 = int(result3)
sum3 = number3 + 10
print(sum3)


# Task 3
students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']
print('Students', ', '.join(students), 'study these subjects:', ', '.join(subjects))
