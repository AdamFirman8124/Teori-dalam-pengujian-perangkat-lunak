# file: project/blib2to3/pgen2/literals.py:25-44
# asked: {"lines": [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 40, 41, 42, 43, 44], "branches": [[29, 30], [29, 31], [31, 32], [31, 40], [33, 34], [33, 35]]}
# gained: {"lines": [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 40, 41, 42, 43, 44], "branches": [[29, 30], [29, 31], [31, 32], [31, 40], [33, 34], [33, 35]]}

import re

import pytest

from blib2to3.pgen2 import literals


def test_escape_simple_escape() -> None:
    match = re.fullmatch(r"\\(.*)", r"\n")
    assert match is not None
    assert literals.escape(match) == "\n"


def test_escape_valid_hexadecimal() -> None:
    match = re.fullmatch(r"\\(.*)", r"\x41")
    assert match is not None
    assert literals.escape(match) == "A"


def test_escape_rejects_short_hexadecimal() -> None:
    match = re.fullmatch(r"\\(.*)", r"\x")
    assert match is not None

    with pytest.raises(ValueError) as exc_info:
        literals.escape(match)

    assert str(exc_info.value) == r"invalid hex string escape ('\x')"


def test_escape_rejects_non_hexadecimal_digits() -> None:
    match = re.fullmatch(r"\\(.*)", r"\xGG")
    assert match is not None

    with pytest.raises(ValueError) as exc_info:
        literals.escape(match)

    assert str(exc_info.value) == r"invalid hex string escape ('\xGG')"


def test_escape_valid_octal() -> None:
    match = re.fullmatch(r"\\(.*)", r"\101")
    assert match is not None
    assert literals.escape(match) == "A"


def test_escape_rejects_non_octal_digits() -> None:
    match = re.fullmatch(r"\\(.*)", r"\9")
    assert match is not None

    with pytest.raises(ValueError) as exc_info:
        literals.escape(match)

    assert str(exc_info.value) == r"invalid octal string escape ('\9')"


def test_escape_requires_leading_backslash() -> None:
    match = re.fullmatch(r"(.*)", "n")
    assert match is not None

    with pytest.raises(AssertionError):
        literals.escape(match)
