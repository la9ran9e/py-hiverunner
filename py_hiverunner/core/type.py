from typing import Callable, List, TypeVar, Iterable, Union


HQL = str
JString = TypeVar("JString")
SourceArray = Iterable[int]
Deserialized = Union[int, float, List[str], str, bool]


def array_cast(array: Iterable[JString], cast: Callable[[JString], Deserialized]) -> List[Deserialized]:
    _list = []
    for item in array:
        _list.append(cast(item))
    return _list
