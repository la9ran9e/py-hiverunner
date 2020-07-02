from typing import List

from py_hiverunner.core.jvm import JVMEntryPoint
from py_hiverunner.core.type import HQL, array_cast


class HiveRunnerApi:
    def __init__(self, jvm: JVMEntryPoint, basedir: str = "py-hiverunner-"):
        self._jvm = jvm
        self._basedir = basedir

    def start(self):
        self._jvm.start()
        self._instance = self._jvm.get_hiverunner(self._basedir)
        self._instance.setup()

    def stop(self):
        self._instance.stop()
        self._jvm.stop()

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop()

    def execute_query(self, query: HQL) -> List[str]:
        ret = self._instance.executeQuery(query)
        return array_cast(ret, str)
