from typing import List

import strawberry

from books.types import BookType


@strawberry.type
class Query:
    all_books: List[BookType] = strawberry.django.field()
