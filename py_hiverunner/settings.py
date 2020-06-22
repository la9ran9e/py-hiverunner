import os

from dotenv import load_dotenv

from py_hiverunner.utils import default_classpath

load_dotenv()

HIVERUNNER_CLASS_PATH = os.environ.get("PYHIVERUNNER_HOME", default_classpath())
BASEDIR = os.environ.get("PYHIVERUNNER_BASEDIR", "py-hiverunner-")
DEFAULT_SEP = "\t"
DEFAULT_NULL = "NULL"
