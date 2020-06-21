from typing import Any, Callable, List

HQL = str


def array_cast(array: Any, cast: Callable[[Any], Any]) -> List[Any]:
    _list = []
    for item in array:
        _list.append(cast(item))
    return _list
