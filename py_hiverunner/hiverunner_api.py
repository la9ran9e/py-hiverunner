from typing import List

from py_hiverunner.core.jvm import JVM
from py_hiverunner.core.type import HQL, array_cast


class HiveRunnerApi:
    def __init__(
            self,
            jvm: JVM,
            basedir: str = "py-hiverunner-",
            class_path: str = "com.la9ran9e.hiverunner.HiveRunner"
    ):
        self._jvm = jvm
        self._basedir = basedir
        self._class_path = class_path
        self._class = None
        self._instance = None

    def start(self):
        self._jvm.start()
        self._class = self._jvm.get_class(self._class_path)
        self._instance = self._class(self._basedir)
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
