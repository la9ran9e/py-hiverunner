# py-hiverunner
[![Build Status](https://travis-ci.com/la9ran9e/py-hiverunner.svg?branch=master)](https://travis-ci.com/la9ran9e/py-hiverunner)
[![Code Coverage Status](https://codecov.io/gh/la9ran9e/py-hiverunner/branch/master/graph/badge.svg)](https://codecov.io/gh/la9ran9e/py-hiverunner)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/py-hiverunner)](https://pypi.org/project/py-hiverunner/)
[![Docker Build Status](https://img.shields.io/docker/cloud/build/la9ran9e/py-hiverunner)](https://hub.docker.com/r/la9ran9e/py-hiverunner)

Library provides python API for [Klarna's HiveRunner](https://github.com/klarna/HiveRunner).

## Install

Install `py-hiverunner` package with [pip](https://pypi.org/project/py-hiverunner/):

```bash
$ python -m pip install py-hiverunner
```

## Usage
Before using `py-hiverunner` you need start JVM with facade service based on original Klarna's `HiveRunner` - 
[java-hiverunner](./java-hiverunner).
This repo provides [docker container for Py4J Java Gateway for HiveRunner](https://hub.docker.com/r/la9ran9e/py-hiverunner).

You can pull this:
```bash
$ docker pull la9ran9e/py-hiverunner
```
and then run the container:
```bash
$ docker run -ti -p 25333:25333 -p 25334:25334 la9ran9e/py-hiverunner
```
After that you will have working server with Java HiveRunner.

Try this:

```python
from py_hiverunner import hiverunner
from pprint import pprint


with hiverunner() as hive:
    hive.execute_query("create schema meh")
    hive.execute_query("create table meh.nonsub(a int, b string, c array<string>)")
    hive.execute_query("insert into meh.nonsub select 1, 'la9ran9e', array('1', 'a', 'b', '6')")
    hive.execute_query("insert into meh.nonsub select 2, 'la9ran9e', array('1', 'b', 'b', '6')")
    hive.execute_query("insert into meh.nonsub select 3, 'la9ran9e', array('1', 'c', 'b', '6')")
    hive.execute_query("insert into meh.nonsub select 4, '', array('1', 'd', 'b', '6')")

    hive.execute_query("create table meh.sub(a int, b string, c boolean)")
    hive.execute_query("insert into meh.sub select 1, 'la9ran9e', true")

    print("RESULT:")
    pprint(hive.execute_query("""
        select
            *
        from
            meh.sub as sub
        inner join
            meh.nonsub as nonsub
        on
            sub.b = nonsub.b
    """))
```