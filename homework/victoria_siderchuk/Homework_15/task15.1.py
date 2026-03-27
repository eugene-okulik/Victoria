import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)

cursor.execute("INSERT INTO students (name, second_name) VALUES ('Bob', 'White')")
student_id = cursor.lastrowid
cursor.execute("SELECT * from students where id = %s", (student_id,))
print(cursor.fetchone())


books = [
    ('Hamlet', student_id),
    ('The Hobbit', student_id)
]
cursor.executemany("INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)", books)
cursor.execute("SELECT * from books where taken_by_student_id = %s", (student_id,))
print(cursor.fetchall())


groups = ('Grade 10A', '2026-01-01', '2026-12-31')
cursor.execute("INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)", groups)
group_id = cursor.lastrowid
cursor.execute("SELECT * FROM `groups` WHERE id = %s", (group_id,))
print(cursor.fetchone())


cursor.execute("UPDATE students SET group_id = %s WHERE id = %s", (group_id, student_id))


subjects = [
    ('Biology',),
    ('Foreign Languages',)
]
cursor.executemany("INSERT INTO subjects (title) VALUES (%s)", subjects)
cursor.execute("SELECT * FROM subjects ORDER BY id DESC LIMIT 2")
all_subjects = (cursor.fetchall())
print(all_subjects)
foreign_id, biology_id = [row['id'] for row in all_subjects]
print(foreign_id, biology_id)


lessons = [
    ('Animals', biology_id),
    ('Flowers', biology_id),
    ('English', foreign_id),
    ('French', foreign_id)
]
cursor.executemany("INSERT INTO lessons (title, subject_id) VALUES (%s, %s)", lessons)
cursor.execute("SELECT * FROM lessons ORDER BY id DESC LIMIT 4")
all_lessons = (cursor.fetchall())
print(all_lessons)
french_id, english_id, flowers_id, animals_id = [row['id'] for row in all_lessons]
print(french_id, english_id, flowers_id, animals_id)


marks = [
    (5, animals_id, student_id),
    (4, flowers_id, student_id),
    (3, english_id, student_id),
    (2, french_id, student_id)
]
cursor.executemany("INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)", marks)


cursor.execute("SELECT * FROM marks WHERE student_id = %s", (student_id,))
print(cursor.fetchall())


cursor.execute("SELECT * FROM books WHERE taken_by_student_id = %s", (student_id,))
print(cursor.fetchall())

query = '''
SELECT
    s.id,
    s.name AS 'First Name',
    s.second_name AS 'Second Name',
    g.title AS 'Group Title',
    b.title AS 'Book Title',
    m.value AS 'Mark',
    l.title AS 'Lesson',
    sb.title AS 'Subject
FROM students s
JOIN `groups` g ON s.group_id = g.id
JOIN books b ON s.id = b.taken_by_student_id
JOIN marks m ON s.id = m.student_id
JOIN lessons l ON l.id = m.lesson_id
JOIN subjects sb ON sb.id = l.subject_id
WHERE s.id = %s
'''
cursor.execute(query, (student_id,))
print(cursor.fetchall())


db.close()
