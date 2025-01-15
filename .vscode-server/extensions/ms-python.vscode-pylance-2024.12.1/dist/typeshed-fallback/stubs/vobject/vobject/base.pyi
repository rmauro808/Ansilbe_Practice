import logging
from _typeshed import Incomplete, SupportsWrite
from collections.abc import Iterable, Iterator
from typing import Any, Literal, TypeVar, overload

logger: logging.Logger
DEBUG: bool
CR: str
LF: str
CRLF: str
SPACE: str
TAB: str
SPACEORTAB: str

_V = TypeVar("_V", bound=VBase)
_W = TypeVar("_W", bound=SupportsWrite[bytes])

class VBase:
    group: Incomplete | None
    behavior: Incomplete | None
    parentBehavior: Incomplete | None
    isNative: bool
    def __init__(self, group: Incomplete | None = None) -> None: ...
    def copy(self, copyit: VBase) -> None: ...
    def validate(self, *args, **kwds) -> bool: ...
    def getChildren(self) -> list[Any]: ...
    def clearBehavior(self, cascade: bool = True) -> None: ...
    def autoBehavior(self, cascade: bool = False) -> None: ...
    def setBehavior(self, behavior, cascade: bool = True) -> None: ...
    def transformToNative(self): ...
    def transformFromNative(self): ...
    def transformChildrenToNative(self) -> None: ...
    def transformChildrenFromNative(self, clearBehavior: bool = True) -> None: ...
    # Use Any because args and kwargs are passed to the behavior object
    @overload
    def serialize(
        self,
        buf: None = None,
        lineLength: int = 75,
        validate: bool = True,
        behavior: Incomplete | None = None,
        *args: Any,
        **kwargs: Any,
    ) -> str: ...
    @overload
    def serialize(
        self, buf: _W, lineLength: int = 75, validate: bool = True, behavior: Incomplete | None = None, *args: Any, **kwargs: Any
    ) -> _W: ...

def toVName(name, stripNum: int = 0, upper: bool = False): ...

class ContentLine(VBase):
    name: Any
    encoded: Any
    params: Any
    singletonparams: Any
    isNative: Any
    lineNumber: Any
    value: Any
    def __init__(
        self,
        name,
        params,
        value,
        group: Incomplete | None = None,
        encoded: bool = False,
        isNative: bool = False,
        lineNumber: Incomplete | None = None,
        *args,
        **kwds,
    ) -> None: ...
    @classmethod
    def duplicate(cls, copyit): ...
    def copy(self, copyit) -> None: ...
    def __eq__(self, other): ...
    def __getattr__(self, name: str): ...
    def __setattr__(self, name: str, value) -> None: ...
    def __delattr__(self, name: str) -> None: ...
    def valueRepr(self): ...
    def __unicode__(self) -> str: ...
    def prettyPrint(self, level: int = 0, tabwidth: int = 3) -> None: ...

class Component(VBase):
    contents: dict[str, list[VBase]]
    name: Any
    useBegin: bool
    def __init__(self, name: Incomplete | None = None, *args, **kwds) -> None: ...
    @classmethod
    def duplicate(cls, copyit): ...
    def copy(self, copyit) -> None: ...
    def setProfile(self, name) -> None: ...
    def __getattr__(self, name: str): ...
    normal_attributes: Any
    def __setattr__(self, name: str, value) -> None: ...
    def __delattr__(self, name: str) -> None: ...
    def getChildValue(self, childName, default: Incomplete | None = None, childNumber: int = 0): ...
    @overload
    def add(self, objOrName: _V, group: str | None = None) -> _V: ...
    @overload
    def add(self, objOrName: Literal["vevent"], group: str | None = None) -> Component: ...
    @overload
    def add(
        self, objOrName: Literal["uid", "summary", "description", "dtstart", "dtend"], group: str | None = None
    ) -> ContentLine: ...
    @overload
    def add(self, objOrName: str, group: str | None = None) -> Any: ...  # returns VBase sub-class
    def remove(self, obj) -> None: ...
    def getChildren(self) -> list[Any]: ...
    def components(self) -> Iterable[Component]: ...
    def lines(self): ...
    def sortChildKeys(self): ...
    def getSortedChildren(self): ...
    def setBehaviorFromVersionLine(self, versionLine) -> None: ...
    def transformChildrenToNative(self) -> None: ...
    def transformChildrenFromNative(self, clearBehavior: bool = True) -> None: ...
    def prettyPrint(self, level: int = 0, tabwidth: int = 3) -> None: ...

class VObjectError(Exception):
    msg: Any
    lineNumber: Any
    def __init__(self, msg, lineNumber: Incomplete | None = None) -> None: ...

class ParseError(VObjectError): ...
class ValidateError(VObjectError): ...
class NativeError(VObjectError): ...

patterns: Any
param_values_re: Any
params_re: Any
line_re: Any
begin_re: Any

def parseParams(string): ...
def parseLine(line, lineNumber: Incomplete | None = None): ...

wrap_re: Any
logical_lines_re: Any
testLines: str

def getLogicalLines(fp, allowQP: bool = True) -> None: ...
def textLineToContentLine(text, n: Incomplete | None = None): ...
def dquoteEscape(param): ...
def foldOneLine(outbuf, input, lineLength: int = 75) -> None: ...
def defaultSerialize(obj, buf, lineLength): ...

class Stack:
    stack: Any
    def __len__(self) -> int: ...
    def top(self): ...
    def topName(self): ...
    def modifyTop(self, item) -> None: ...
    def push(self, obj) -> None: ...
    def pop(self): ...

def readComponents(
    streamOrString, validate: bool = False, transform: bool = True, ignoreUnreadable: bool = False, allowQP: bool = False
) -> Iterator[Component]: ...
def readOne(stream, validate: bool = False, transform: bool = True, ignoreUnreadable: bool = False, allowQP: bool = False): ...
def registerBehavior(behavior, name: Incomplete | None = None, default: bool = False, id: Incomplete | None = None) -> None: ...
def getBehavior(name, id: Incomplete | None = None): ...
def newFromBehavior(name, id: Incomplete | None = None): ...
def backslashEscape(s): ...
