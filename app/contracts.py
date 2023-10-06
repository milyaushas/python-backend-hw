from pydantic import BaseModel, Field


class Member(BaseModel):
    """Contract for library member"""

    name: str
    surname: str


class Book(BaseModel):
    """Contract for book"""

    title: str
    author: str
    holder_id: int = Field(default=0)  # holder_id==0 means book in the library
