__version__ = '0.1.0'

from py_hiverunner.core.jvm import JVM
from py_hiverunner.parser import RegexParser
from py_hiverunner.hiverunner_api import HiveRunnerApi
from py_hiverunner.hiverunner import HiveRunner
from py_hiverunner.settings import HIVERUNNER_CLASS_PATH, BASEDIR, DEFAULT_SEP, DEFAULT_NULL


def create_hivrunner() -> HiveRunner:
    """
    Creates hiverunner instance.

    :return: hiverunner
    :rtype: HiveRunner
    """
    _jvm = JVM(HIVERUNNER_CLASS_PATH)
    _api = HiveRunnerApi(jvm=_jvm, basedir=BASEDIR)
    _parser = RegexParser(sep=DEFAULT_SEP, null_presentation=DEFAULT_NULL)
    return HiveRunner(_api, _parser)
