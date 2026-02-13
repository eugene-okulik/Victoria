import datetime

test_date = "Jan 15, 2023 - 12:05:33"
python_date = datetime.datetime.strptime(test_date, '%b %d, %Y - %H:%M:%S')

human_month = python_date.strftime('%B')
print(human_month)

human_date = python_date.strftime('%d.%m.%Y, %H:%M')
print(human_date)
