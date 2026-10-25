# file: project/pysnooper/utils.py:62-64
# asked: {"lines": [64], "branches": []}
# gained: {"lines": [64], "branches": []}

import types
import inspect
import re

import pysnooper.utils as utils_module


def _resolve_normalize_repr():
    direct = getattr(utils_module, "normalize_repr", None)
    if callable(direct):
        return direct
    # Fallback: nested definition — rebuild function from its code object
    # so the original file/line is executed.
    for _, obj in inspect.getmembers(utils_module, inspect.isfunction):
        codes = [obj.__code__]
        seen = set()
        while codes:
            code = codes.pop()
            if id(code) in seen:
                continue
            seen.add(id(code))
            for const in code.co_consts:
                if inspect.iscode(const):
                    if const.co_name == "normalize_repr":
                        return types.FunctionType(const, obj.__globals__)
                    codes.append(const)
    for _, cls in inspect.getmembers(utils_module, inspect.isclass):
        for _, meth in inspect.getmembers(cls, inspect.isfunction):
            for const in meth.__code__.co_consts:
                if inspect.iscode(const) and const.co_name == "normalize_repr":
                    return types.FunctionType(const, meth.__globals__)
    raise AssertionError("normalize_repr not found in pysnooper.utils")


def test_normalize_repr_removes_memory_address():
    normalize_repr = _resolve_normalize_repr()
    item_repr = "<object object at 0x7f8b8c0d5a90>"
    result = normalize_repr(item_repr)
    assert result == "<object object>"
    assert "0x" not in result
    assert isinstance(result, str)


def test_normalize_repr_leaves_plain_repr_unchanged():
    normalize_repr = _resolve_normalize_repr()
    item_repr = "<Foo bar=baz>"
    result = normalize_repr(item_repr)
    assert result == "<Foo bar=baz>"
    item_repr2 = "just a string"
    assert normalize_repr(item_repr2) == "just a string"
    assert normalize_repr("") == ""


def test_normalize_repr_hex_length_boundary():
    normalize_repr = _resolve_normalize_repr()
    # Exactly 4 hex digits -> removed ({4,})
    assert normalize_repr("<Foo at 0x1234>") == "<Foo>"
    assert normalize_repr("<Foo at 0xABCD>") == "<Foo>"
    assert normalize_repr("<Foo at 0xabcd>") == "<Foo>"
    # 3 or fewer hex digits -> not removed
    assert normalize_repr("<Foo at 0x123>") == "<Foo at 0x123>"
    assert normalize_repr("<Foo at 0xAB>") == "<Foo at 0xAB>"
    # Longer mixed-case address -> removed
    assert normalize_repr("<Foo at 0xAbCdEf123456>") == "<Foo>"


def test_normalize_repr_multiple_addresses_and_non_address_0x():
    normalize_repr = _resolve_normalize_repr()
    item_repr = "a at 0x123456 b at 0xABCDEF"
    result = normalize_repr(item_repr)
    assert result == "a b"
    assert "0x" not in result
    # 0x without leading ' at ' must be left alone
    assert normalize_repr("value 0x123456") == "value 0x123456"
    # 'at' without 0x must be left alone
    assert normalize_repr("<Foo at somewhere>") == "<Foo at somewhere>"


def test_normalize_repr_matches_default_repr_re(monkeypatch):
    normalize_repr = _resolve_normalize_repr()
    # Verify postcondition against the actual regex object, no state pollution.
    pattern = getattr(utils_module, "DEFAULT_REPR_RE", re.compile(" at 0x[a-f0-9A-F]{4,}"))
    cases = [
        "<object object at 0x7F8B8C0D5A90>",
        "<threading.Lock at 0x10a1b2c3d>",
        "no address here",
    ]
    for case in cases:
        expected = pattern.sub("", case)
        assert normalize_repr(case) == expected
