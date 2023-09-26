from typing import List

from fastapi import APIRouter

from app import contracts

router = APIRouter()
people = []


@router.get("/", description="Root entrypoint")
async def root() -> str:
    """
    Root entrypoint

    :return: empty string
    """
    return ""


@router.get(
    "/hello", description="Method without params that returns greeting message."
)
async def hello() -> str:
    """
    Method without parameters that returns greeting message.

    :return: greeting message
    """
    return "Hello, world!"


@router.get(
    "/hello/{name}", description="Method that returns personal greeting message"
)
async def hello_name(name: str) -> str:
    """
    Method that validate name and returns personal greeting message

    :param name: user's name
    :return: greeting message or "Invalid name"
    """
    if not name:
        return "Invalid name"
    return f"Hello, {name}!"


@router.post("/person/", description="Method that saves person's data")
async def create_person(person: contracts.Person) -> str:
    """
    "Method that validates and saves person's data"

    :param person: name(str) and age(integer)
    :return: greeting message specified on person's age
    """
    if person.name is None:
        return "Invalid name"
    if person.age is None or person.age < 0:
        return "Invalid age"
    people.append(person)
    if person.age <= 25:
        return f"Hiiii, {person.name} :3"
    return f"Hello, {person.name}!"


@router.get("/people/all", description="Method that returns info about all people")
async def all_people() -> List[contracts.Person]:
    """
    Method that returns info about all people stored in database

    :return: list of people
    """
    return people
