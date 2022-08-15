import strawberry

from reviews.schema import Query as ReviewsQuery
from reviews.types import BookType


class Query(ReviewsQuery):
    """
    This is the top level query which inherits from other app's queries
    """


# class Mutation():
#     """
#     This is the top level query which inherits from other app's queries
#     """


schema = strawberry.federation.Schema(query=Query, types=[BookType])
