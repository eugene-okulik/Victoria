import os
import datetime

base_path = os.path.dirname(__file__)
print(base_path)

vs_path = os.path.dirname(base_path)
print(vs_path)

homework_path = os.path.dirname(vs_path)
print(homework_path)

eugene_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')
print(eugene_path)

with open(eugene_path, encoding='utf-8') as eugene_file:
    for line in eugene_file:
        before_dash = line.split(' - ')[0]
        date_string = before_dash.split(' ', 1)[1]
        date = datetime.datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S.%f')

        after_dash = line.split(' - ')[1]

        if 'на неделю позже' in after_dash:
            print(date + datetime.timedelta(days=7))

        if 'день недели' in after_dash:
            print(date.strftime('%A'))

        elif 'сколько дней назад' in after_dash:
            print((datetime.datetime.now() - date).days)
