import pytest

from app.contracts import Member, Book
from app.library_service import LibraryService


@pytest.mark.parametrize(
    "name, surname, expected_result, expected_message",
    [
        ("Milyausha", "Sabirova", True, "New member added successfully"),
        ("", "Sabirova", False, "Empty name"),
        ("Milyausha", "", False, "Empty surname"),
        # check that we can add different people with the same name
        ("Milyausha", "Sabirova", True, "New member added successfully"),
    ],
)
def test_new_member(name, surname, expected_result, expected_message):
    service = LibraryService()
    member = Member(name=name, surname=surname)
    result, message = service.new_member(member)
    assert result == expected_result
    assert message == expected_message


@pytest.mark.parametrize(
    "title, author, expected_result, expected_message",
    [
        ("Title", "Author", True, "New book added successfully"),
        ("", "Author", False, "Empty title"),
        ("Title", "", False, "Empty author"),
        ("Title", "Author", True, "New book added successfully"),
    ],
)
def test_new_book(title, author, expected_result, expected_message):
    service = LibraryService()
    book = Book(title=title, author=author)
    result, message = service.new_book(book)
    assert result == expected_result
    assert message == expected_message


@pytest.mark.parametrize(
    "book_id, member_id, expected_result, expected_message",
    [
        (1, 1, True, "Request completed successfully"),
        (42, 1, False, "Invalid book_id"),
        (1, 42, False, "Invalid member_id"),
        (2, 2, False, "Book is already taken"),
    ],
)
def test_give_book_to_member(book_id, member_id, expected_result, expected_message):
    library = LibraryService()
    library.new_member(Member(name="Milyausha", surname="Sabirova"))  # member_id = 1
    library.new_book(Book(title="Title", author="Author"))  # book_id = 1
    library.new_member(
        Member(name="NotMilyausha", surname="NotSabirova")
    )  # member_id = 2
    library.new_book(Book(title="Other title", author="Other author"))  # book_id = 2
    library.give_book_to_member(2, 1)
    result, message = library.give_book_to_member(book_id=book_id, member_id=member_id)
    assert result == expected_result
    assert message == expected_message


@pytest.mark.parametrize(
    "book_id, expected_result, expected_message",
    [
        (1, True, "Book returned to the library successfully"),
        (42, False, "Invalid book_id"),
        (2, True, "Book already in the library"),
    ],
)
def test_return_book(book_id, expected_result, expected_message):
    library = LibraryService()
    library.new_member(Member(name="Milyausha", surname="Sabirova"))  # member_id = 1
    library.new_book(Book(title="Title", author="Author"))  # book_id = 1
    library.give_book_to_member(book_id=1, member_id=1)
    library.new_book(Book(title="Other title", author="Other Author"))  # book_id = 2

    result, message = library.return_book(book_id=book_id)
    assert result == expected_result
    assert message == expected_message


def test_get_all_books_taken_by_member():
    library = LibraryService()
    library.new_member(Member(name="Milyausha", surname="Sabirova"))  # member_id = 1

    books = library.get_all_books_taken_by_member(member_id=1)
    assert len(books) == 0

    library.new_book(Book(title="1", author="1", holder_id=0))  # book_id = 1
    library.new_book(Book(title="2", author="2", holder_id=0))  # book_id = 2
    library.give_book_to_member(book_id=1, member_id=1)
    books = library.get_all_books_taken_by_member(1)
    assert len(books) == 1

    library.give_book_to_member(book_id=2, member_id=1)
    books = library.get_all_books_taken_by_member(member_id=1)
    assert len(books) == 2

    books = library.get_all_books_taken_by_member(member_id=42)
    assert not books
