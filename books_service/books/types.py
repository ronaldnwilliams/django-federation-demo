import strawberry
import strawberry_django
from strawberry.federation.schema_directives import Key

from books.models import Book


@strawberry_django.type(model=Book, directives=[Key('id')])
class BookType:
    id: strawberry.auto
    title: strawberry.auto
