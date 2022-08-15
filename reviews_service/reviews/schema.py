from typing import List

import strawberry

from reviews.types import ReviewType


@strawberry.type
class Query:
    all_reviews: List[ReviewType] = strawberry.django.field()
    # pass
