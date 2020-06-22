# py-hiverunner
Library provides python API for [Klarna's HiveRunner](https://github.com/klarna/HiveRunner).

## Usage
Before using you should set `HIVERUNNER` environment variable to classpath of original HiveRunner jar.
To compile original HiveRunner API try build from [here](https://github.com/la9ran9e/hiverunner)
```python
from py_hiverunner import create_hiverunner
from pprint import pprint


with create_hiverunner() as hive:
    hive.execute_query("create schema meh")
    hive.execute_query("create table meh.nonsub(a int, b string, c array<string>)")
    hive.execute_query("insert into meh.nonsub select 1, 'la9ran9e', array('1', 'a', 'b', '6')")
    hive.execute_query("insert into meh.nonsub select 2, 'la9ran9e', array('1', 'b', 'b', '6')")
    hive.execute_query("insert into meh.nonsub select 3, 'la9ran9e', array('1', 'c', 'b', '6')")
    hive.execute_query("insert into meh.nonsub select 4, '', array('1', 'd', 'b', '6')")
    print("RESULT:")
    pprint(hive.execute_query("select * from meh.nonsub where b = 'la9ran9e'"))
```