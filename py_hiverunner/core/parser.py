from abc import ABC, abstractmethod
from typing import Optional, Tuple

from py_hiverunner.core.type import Deserialized


class Parser(ABC):
    @abstractmethod
    def parse_string(self, string: str) -> Tuple[Optional[Deserialized], ...]:
        ...
