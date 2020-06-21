from abc import ABC, abstractmethod
from typing import Any, Optional, Tuple


class Parser(ABC):
    @abstractmethod
    def parse_string(self, string: str) -> Tuple[Optional[Any]]:
        ...
