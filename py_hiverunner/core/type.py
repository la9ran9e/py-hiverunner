from typing import List, TypeVar, Iterable, Union


JClass = TypeVar("JClass")
JHiveRunner = TypeVar("JHiveRunner")
HQL = str
JString = TypeVar("JString")
SourceArray = Iterable[int]
Deserialized = Union[int, float, List[str], str, bool]
