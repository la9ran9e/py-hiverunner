import pytest

from py_hiverunner.jvm import Py4JEntryPoint


@pytest.fixture
def py4j_entry_point():
    jvm = Py4JEntryPoint()
    jvm.start()
    yield jvm
    jvm.stop()


def test_py4j_entry_point(py4j_entry_point):
    hive = py4j_entry_point.get_hiverunner("py-hiverunner-test-")
    hive.setup()
    assert hive.executeQuery("select 1")