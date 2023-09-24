from pydantic import BaseModel


class Person(BaseModel):
    """
    Contract for person data
    """
    name: str
    age: int
