import pytest

from py_hiverunner.jvm import Py4JEntryPoint
from py_hiverunner.parser import RegexParser
from py_hiverunner.hiverunner_api import HiveRunnerApi
from py_hiverunner.hiverunner import HiveRunner
from py_hiverunner.settings import DEFAULT_SEP, DEFAULT_NULL


@pytest.fixture
def hiverunner():
    _jvm = Py4JEntryPoint()
    _api = HiveRunnerApi(jvm=_jvm, basedir="py-hiverunner-test-")
    _parser = RegexParser(sep=DEFAULT_SEP, null_presentation=DEFAULT_NULL)
    with HiveRunner(_api, _parser) as hive:
        yield hive


@pytest.fixture
def empty_table(hiverunner):
    hiverunner.execute_query("create table empty_table(a int)")


@pytest.mark.usefixtures("empty_table")
@pytest.mark.parametrize(
    "query,expected",
    [
        ("select * from empty_table", []),
        ("select 3.14", [(3.14,)]),
        ("select array('a', 'b', 'c')", [(["a", "b", "c"],)]),
        ("select array()", [([],)]),
    ]
)
def test_execute_query(hiverunner, query, expected):
    assert hiverunner.execute_query(query) == expected
