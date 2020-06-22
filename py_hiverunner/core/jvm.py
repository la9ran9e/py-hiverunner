import jpype


class JVM:
    def __init__(self, classpath: str):
        self._classpath = classpath

    def start(self):
        jpype.addClassPath(self._classpath)
        jpype.startJVM(convertStrings=False)

    def stop(self):
        jpype.shutdownJVM()

    def get_class(self, import_path: str):  # real signature unknown
        return jpype.JClass(import_path)
