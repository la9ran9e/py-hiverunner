from typing import Any, List


def list_string(string_array: str) -> List[Any]:
    return [item.strip("\"") for item in string_array.strip("][").split(",")]
