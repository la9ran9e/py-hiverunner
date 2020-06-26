from typing import List, Optional, Tuple

from py_hiverunner.hiverunner_api import HiveRunnerApi
from py_hiverunner.core.parser import Parser
from py_hiverunner.core.type import HQL, Deserialized


class HiveRunner:
    def __init__(self, api: HiveRunnerApi, parser: Parser):
        self._api = api
        self._parser = parser

    def execute_query(self, query: HQL) -> List[Tuple[Optional[Deserialized]]]:
        raw_result = self._api.execute_query(query)
        result = []
        for string_row in raw_result:
            result.append(self._parser.parse_string(string_row))
        return result

    def start(self):
        self._api.start()

    def stop(self):
        self._api.stop()

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop()
