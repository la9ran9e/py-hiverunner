import pytest

from py_hiverunner.core.jvm import JVM
from py_hiverunner.hiverunner_api import HiveRunnerApi
from py_hiverunner.settings import HIVERUNNER_CLASS_PATH


@pytest.fixture
def jvm():
    yield JVM(HIVERUNNER_CLASS_PATH)


@pytest.fixture
def hiverunnerapi(jvm):
    with HiveRunnerApi(jvm) as api:
        yield api


@pytest.fixture
def database_test(hiverunnerapi):
    hiverunnerapi.execute_query("create database test")


@pytest.fixture
def table_with_array(hiverunnerapi):
    hiverunnerapi.execute_query("create table test.table_with_array(a int, b string, c array<string>)")
    hiverunnerapi.execute_query("insert into test.table_with_array select 1, 'meh', array('a', 'b')")


@pytest.mark.usefixtures("table_with_array")
@pytest.mark.usefixtures("database_test")
def test_return_type(hiverunnerapi):
    ret = hiverunnerapi.execute_query("SELECT a, b, c from test.table_with_array")
    assert isinstance(ret, list)
    assert isinstance(ret[0], str)
