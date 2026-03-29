import os
import csv
import mysql.connector as mysql
import dotenv


homework_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
eugene_path = os.path.join(homework_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')
print(eugene_path)


with open(eugene_path, newline='') as csv_file:
    file_data = csv.reader(csv_file)
    for row in file_data:
        print(row)


dotenv.load_dotenv()


db = mysql.connect(
    user=os.getenv("DB_USER"),
    passwd=os.getenv("DB_PASSW"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    database=os.getenv("DB_NAME")
)


cursor = db.cursor(dictionary=True)
query = '''
SELECT
    s.name AS 'name',
    s.second_name AS 'second_name',
    g.title AS 'group_title',
    b.title AS 'book_title',
    m.value AS 'mark_value',
    l.title AS 'lesson_title',
    sb.title AS 'subject_title'
FROM students s
JOIN `groups` g ON s.group_id = g.id
JOIN books b ON s.id = b.taken_by_student_id
JOIN marks m ON s.id = m.student_id
JOIN lessons l ON l.id = m.lesson_id
JOIN subjects sb ON sb.id = l.subject_id
'''
cursor.execute(query)
db_data = cursor.fetchall()
db.close()


with open(eugene_path, newline='') as csv_file:
    file_data = csv.DictReader(csv_file)
    data = []
    for row in file_data:
        data.append(row)


missing_data = []
for row in data:
    if row not in db_data:
        missing_data.append(row)

print(missing_data)
