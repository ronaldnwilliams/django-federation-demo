from typing import List

import strawberry
from strawberry.federation.schema_directives import Key

from reviews.models import Review


@strawberry.django.type(model=Review)
class ReviewType:
    id: strawberry.auto
    body: strawberry.auto


def get_reviews(root: "BookType") -> List[ReviewType]:
    return [
        ReviewType(id=root.id, body=f"A review for {root.id}")
    ]


@strawberry.federation.type(extend=True, directives=[Key('id')])
class BookType:
    id: strawberry.ID = strawberry.federation.field(external=True)
    reviews: List[ReviewType] = strawberry.django.field(resolver=get_reviews)

    @classmethod
    def resolve_reference(cls, id: strawberry.ID):
        return BookType(id=id)
