# py-hiverunner
[![Build Status](https://travis-ci.com/la9ran9e/py-hiverunner.svg?branch=master)](https://travis-ci.com/la9ran9e/py-hiverunner)
[![Code Coverage Status](https://codecov.io/gh/la9ran9e/py-hiverunner/branch/master/graph/badge.svg)](https://codecov.io/gh/la9ran9e/py-hiverunner)

Library provides python API for [Klarna's HiveRunner](https://github.com/klarna/HiveRunner).

## Usage
Before using `py-hiverunner` you need start JVM with facade service based on original Klarna's `HiveRunner` - 
[java-hiverunner](./java-hiverunner).
This repo provides [Dockerfile](./Dockerfile) to build docker image with Java HiveRunner server.

You can build this:
```bash
docker build -t py-hiverunner .
```
and then run the container:
```bash
docker run -ti -p 25333:25333 -p 25334:25334 py-hiverunner
```
After that you will have working server with Java HiveRunner.

Try this:

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