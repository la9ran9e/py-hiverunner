__version__ = '0.1.2'

from py_hiverunner.jvm import Py4JEntryPoint
from py_hiverunner.parser import RegexParser
from py_hiverunner.hiverunner_api import HiveRunnerApi
from py_hiverunner.hiverunner import HiveRunner
from py_hiverunner.settings import BASEDIR, DEFAULT_SEP, DEFAULT_NULL


def hiverunner(**kwargs) -> HiveRunner:
    """
    Creates hiverunner instance.

    :param kwargs: Optional key arguments used by JVMEntryPoint
    :return: hiverunner
    :rtype: HiveRunner
    """
    _jvm = Py4JEntryPoint(**kwargs)
    _api = HiveRunnerApi(jvm=_jvm, basedir=BASEDIR)
    _parser = RegexParser(sep=DEFAULT_SEP, null_presentation=DEFAULT_NULL)
    return HiveRunner(_api, _parser)
