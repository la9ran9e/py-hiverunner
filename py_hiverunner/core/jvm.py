from abc import ABC, abstractmethod

from py_hiverunner.core.type import JHiveRunner


class JVMEntryPoint(ABC):
    @abstractmethod
    def start(self):
        ...

    @abstractmethod
    def stop(self):
        ...

    @abstractmethod
    def get_hiverunner(self, *args, **kwargs) -> JHiveRunner:
        ...
