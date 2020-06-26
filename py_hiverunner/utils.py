import pkg_resources

from typing import Any, List


def list_string(string_array: str) -> List[Any]:
    if string_array == "[]":
        return []
    return [item[1:-1] for item in string_array.strip("][").split(",")]


def boolean_string(string_bool: str) -> bool:
    return string_bool == "true"


def default_classpath() -> str:
    return pkg_resources.resource_filename(__name__, "bin/hiverunner.jar")
