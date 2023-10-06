from fastapi import APIRouter, status

from app import contracts
from app.library_service import LibraryService

router = APIRouter()
service = LibraryService()


@router.post("/members/new")
async def create_member(member: contracts.Member):
    """Adds new library member to database"""
    result, message = service.new_member(member)
    if result:
        code = status.HTTP_201_CREATED
    else:
        code = status.HTTP_400_BAD_REQUEST

    return {"status": code, "message": message}


@router.post("/books/new")
async def create_book(book: contracts.Book):
    """Adds new book to library database"""
    result, message = service.new_book(book)
    if result:
        code = status.HTTP_201_CREATED
    else:
        code = status.HTTP_400_BAD_REQUEST
    return {"status": code, "message": message}


@router.post("/assign/{book_id}/to/{member_id}")
async def assign_book_to_member(book_id: int, member_id: int):
    """Updates info about book's current holder"""
    result, message = service.give_book_to_member(book_id, member_id)
    if result:
        code = status.HTTP_200_OK
    else:
        code = status.HTTP_400_BAD_REQUEST
    return {"status": code, "message": message}


@router.post("/return/{book_id}")
async def return_book_to_library(book_id: int):
    """Updates info about book's current holder."""
    result, message = service.return_book(book_id)
    if result:
        code = status.HTTP_200_OK
    else:
        code = status.HTTP_400_BAD_REQUEST
    return {"status": code, "message": message}


@router.post("/books/{member_id}")
async def get_all_books_by_member_id(member_id: int):
    """Returns all books that are taken by a specific library member at this moment"""
    return {
        "status": status.HTTP_200_OK,
        "result": service.get_all_books_taken_by_member(member_id),
    }
