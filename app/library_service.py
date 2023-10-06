from app.contracts import Member, Book


class LibraryService:
    def __init__(self):
        self.members = {}  # id -> member
        self.books = {}  # id -> book

    def new_member(self, member: Member) -> (bool, str):
        if not member.name:
            return False, "Empty name"
        if not member.surname:
            return False, "Empty surname"
        id = len(self.members) + 1
        self.members[id] = member
        return True, "New member added successfully"

    def new_book(self, book: Book) -> (bool, str):
        if not book.title:
            return False, "Empty title"
        if not book.author:
            return False, "Empty author"
        id = len(self.books) + 1
        self.books[id] = book
        return True, "New book added successfully"

    def give_book_to_member(self, book_id: int, member_id: int) -> (bool, str):
        if book_id not in self.books:
            return False, "Invalid book_id"
        if member_id not in self.members:
            return False, "Invalid member_id"
        if self.books[book_id].holder_id > 0:
            return False, "Book is already taken"
        self.books[book_id].holder_id = member_id
        return True, "Request completed successfully"

    def return_book(self, book_id: int) -> (bool, str):
        if book_id not in self.books:
            return False, "Invalid book_id"
        if self.books[book_id].holder_id == 0:
            return True, "Book already in the library"
        self.books[book_id].holder_id = 0
        return True, "Book returned to the library successfully"

    def get_all_books_taken_by_member(self, member_id):
        if member_id not in self.members:
            return None
        result = []
        for book in self.books.values():
            if book.holder_id == member_id:
                result.append(book)
        return result
