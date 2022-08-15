import strawberry

from books.schema import Query as BooksQuery


class Query(BooksQuery):
    """
    This is the top level query which inherits from other app's queries
    """


# class Mutation():
#     """
#     This is the top level query which inherits from other app's queries
#     """


schema = strawberry.federation.Schema(query=Query)
