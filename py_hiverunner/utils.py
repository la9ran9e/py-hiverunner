import pkg_resources

from typing import Any, List


def list_string(string_array: str) -> List[Any]:
    return [item.strip("\"") for item in string_array.strip("][").split(",")]


def default_classpath():
    return pkg_resources.resource_filename(__name__, "bin/hiverunner.jar")
