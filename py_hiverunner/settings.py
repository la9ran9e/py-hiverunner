import os

from dotenv import load_dotenv

load_dotenv()

HIVERUNNER_CLASS_PATH = os.environ.get("HIVERUNNER")
BASEDIR = os.environ.get("BASEDIR", "py-hiverunner-")
DEFAULT_SEP = "\t"
DEFAULT_NULL = "NULL"