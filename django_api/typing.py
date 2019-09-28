from typing import Generic, Iterator, TypeVar, Union

from django.db.models import QuerySet

T = TypeVar("T")


class QuerySetType(Generic[T]):
    def __iter__(self) -> Iterator[Union[T, QuerySet]]:
        pass
