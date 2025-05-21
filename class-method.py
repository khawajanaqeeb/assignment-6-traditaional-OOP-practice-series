class Book:
    total_books = 0

    def __init__(self, title, author):
        self.title=title
        self.author=author
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

book1=Book("Bale Jibreel","Allama Iqbal")
book2=Book("An Inquiry into the nature and wealth of the nation","Adam Smith")

print(f"We have total {Book.total_books} books. Title are {book1.title} and {book2.title}.")
