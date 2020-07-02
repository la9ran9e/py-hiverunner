import jpype

from typing import Optional

from py4j.java_gateway import JavaGateway, GatewayParameters

from py_hiverunner.core.jvm import JVMEntryPoint
from py_hiverunner.core.type import JHiveRunner, JClass


class JPypeEntryPoint(JVMEntryPoint):
    def __init__(self, classpath: str, import_path: str = "com.la9ran9e.hiverunner.HiveRunner"):
        self._classpath = classpath
        self._import_path = import_path
        self._class: Optional[JClass] = None

    def start(self):
        jpype.addClassPath(self._classpath)
        jpype.startJVM(convertStrings=False)
        self._class = jpype.JClass(self._import_path)

    def stop(self):
        jpype.shutdownJVM()

    def get_hiverunner(self, *args, **kwargs) -> JHiveRunner:
        return self._class(*args, **kwargs)


class Py4JEntryPoint(JVMEntryPoint):
    def __init__(self, **kwargs):
        self._kwargs = kwargs
        self._gateway: Optional[JavaGateway] = None

    def start(self):
        self._gateway = JavaGateway(gateway_parameters=GatewayParameters(**self._kwargs))

    def stop(self):
        self._gateway.close()

    def get_hiverunner(self, *args, **kwargs) -> JHiveRunner:
        return self._gateway.entry_point.getHiveRunnerInstance(*args, **kwargs)
