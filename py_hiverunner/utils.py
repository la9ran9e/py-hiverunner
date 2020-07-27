import pkg_resources

from typing import Any, Callable, List, Iterable

from py_hiverunner.core.type import JString, Deserialized


def array_cast(array: Iterable[JString], cast: Callable[[JString], Deserialized]) -> List[Deserialized]:
    _list = []
    for item in array:
        _list.append(cast(item))
    return _list


def list_string(string_array: str) -> List[Any]:
    if string_array == "[]":
        return []
    return [item for item in string_array.strip("][")[1:-1].split("\",\"")]


def boolean_string(string_bool: str) -> bool:
    return string_bool == "true"


def default_classpath() -> str:
    return pkg_resources.resource_filename(__name__, "bin/hiverunner.jar")
