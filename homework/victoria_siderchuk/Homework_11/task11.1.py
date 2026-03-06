class Book:
    page_material = 'Paper'
    has_text = True
    is_reserved = False

    def __init__(self, title, author, page_number, ISBN):
        self.title = title
        self.author = author
        self.page_number = page_number
        self.ISBN = ISBN


first_book = Book('The Hobbit', 'Tolkien', 310, 1)
first_book.is_reserved = True
second_book = Book('To Kill a Mockingbird', 'Harper Lee', 281, 2)
third_book = Book('Pride and Prejudice', 'Jane Austen', 432, 3)
fourth_book = Book('White Fang', 'Jack London', 298, 4)
fifth_book = Book('The Financier', 'Theodore Dreiser', 512, 5)

books = [first_book, second_book, third_book, fourth_book, fifth_book]


for book in books:
    if book.is_reserved:
        print(
    f'Title: {book.title}, '
    f'Author: {book.author}, '
    f'Number of pages: {book.page_number}, '
    f'Material: {book.page_material}, '
    f'Reserved'
)
    else:
        print(
    f'Title: {book.title}, '
    f'Author: {book.author}, '
    f'Number of pages: {book.page_number}, '
    f'Material: {book.page_material}'
)


class SchoolBook(Book):
    def __init__(self, title, author, page_number, ISBN, subject, school_group, has_tasks):
        super().__init__(title, author, page_number, ISBN)
        self.subject = subject
        self.school_group = school_group
        self.has_tasks = has_tasks

school_book1 = SchoolBook('Algebra', 'Ivanov', 50, 1, 'Math', '1A', True)
school_book1.is_reserved = True
school_book2 = SchoolBook('Roman Empire', 'Sokolov', 32,2, 'History', '2A', False)
school_book3 = SchoolBook('Africa', 'Johnson', 21, 3, 'Geography', '3A', False)

school_books = [school_book1, school_book2, school_book3]


for school_book in school_books:
    if school_book.is_reserved:
        print(
    f'Title: {school_book.title}, '
    f'Author: {school_book.author}, '
    f'Number of pages: {school_book.page_number}, '
    f'Subject: {school_book.subject}, '
    f'Reserved'
)
    else:
        print(
    f'Title: {school_book.title}, '
    f'Author: {school_book.author}, '
    f'Number of pages: {school_book.page_number}, '
    f'Subject: {school_book.subject}'
)
