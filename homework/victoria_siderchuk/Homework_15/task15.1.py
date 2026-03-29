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
subject_ids = []
for subject in subjects:
    cursor.execute("INSERT INTO subjects (title) VALUES (%s)", subject)
    subject_ids.append(cursor.lastrowid)
biology_id, foreign_id = subject_ids
print(biology_id, foreign_id)


lessons = [
    ('Animals', biology_id),
    ('Flowers', biology_id),
    ('English', foreign_id),
    ('French', foreign_id)
]
lesson_ids = []
for lesson in lessons:
    cursor.execute("INSERT INTO lessons (title, subject_id) VALUES (%s, %s)", lesson)
    lesson_ids.append(cursor.lastrowid)
animals_id, flowers_id, english_id, french_id = lesson_ids
print(animals_id, flowers_id, english_id, french_id)


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
    sb.title AS 'Subject'
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

db.commit()
db.close()
