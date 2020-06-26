import re
from typing import Any, Callable, Optional, Tuple

from py_hiverunner.core.parser import Parser
from py_hiverunner.utils import list_string, boolean_string
from py_hiverunner.core.type import Deserialized


class RegexParser(Parser):
    TYPE_EXPRESSIONS = [
        r"(?P<list>^\[(\"[^\"\\]*(?:\\.[^\"\\]*)*\",*)*\]$)",   # list
        r"(?P<float>^-*\d*\.\d+$)",                             # float
        r"(?P<int>^-*\d+$)",                                    # int
        r"(?P<boolean>^(true|false)$)",                         # boolean
    ]
    _regex = re.compile("|".join(TYPE_EXPRESSIONS))
    _types = {
        "list": list_string,
        "int": int,
        "float": float,
        "boolean": boolean_string,
    }

    def __init__(self, sep: str = "\t", null_presentation: str = "NULL"):
        self._sep = sep
        self._null_presentation = null_presentation

    def parse_string(self, string: str) -> Tuple[Optional[Deserialized], ...]:
        parsed = []
        parts = string.split(self._sep)
        for item in parts:
            if item == self._null_presentation:
                parsed_item = None
            else:
                cast = self._typeof(item)
                parsed_item = cast(item)
            parsed.append(parsed_item)
        return tuple(parsed)

    def _typeof(self, string: str) -> Callable[[Any], Any]:
        res = self._regex.search(string)
        if res:
            return self._types[res.lastgroup]
        return str
