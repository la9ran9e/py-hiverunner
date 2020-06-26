import pytest

from py_hiverunner.parser import RegexParser


@pytest.fixture
def parser():
    return RegexParser()


@pytest.mark.parametrize(
    "_input,expected",
    [
        ("1", (1,)),
        ("0", (0,)),
        ("", ("",)),
        ("NULL", (None,)),
        ("3.14", (3.14,)),
        ("-1", (-1,)),
        ("-3.14", (-3.14,)),
        ("[]", ([], )),
        ("[\"\"]", ([""],)),
        ("[\"test\",\"\"]", (["test", ""],)),
        ("[\"test\", \"\"]", ("[\"test\", \"\"]",)),
        ("[\"\\\"test\\\"\"]", (["\\\"test\\\""],)),
        ("[1]", ("[1]",)),
        ("{\"test\": \"json\"}", ("{\"test\": \"json\"}",)),
        ("true\tfalse\t[\"a\",\"b\",\"c\"]\t8800\t3.14\ttest\tNULL\t",
         (True, False, ["a", "b", "c"], 8800, 3.14, "test", None, "")),
    ]
)
def test_parse_string_positive(parser, _input, expected):
    assert parser.parse_string(_input) == expected
