# file: project/blib2to3/pgen2/literals.py:25-44
# asked: {"lines": [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 40, 41, 42, 43, 44], "branches": [[29, 30], [29, 31], [31, 32], [31, 40], [33, 34], [33, 35]]}
# gained: {"lines": [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 40, 41, 42, 43, 44], "branches": [[29, 30], [29, 31], [31, 32], [31, 40], [33, 34], [33, 35]]}

"""Coverage tests for blib2to3.pgen2.literals.escape (previously uncovered lines 26-44).

literals.escape() is a pure function: it only reads the module-level
``simple_escapes`` mapping (via ``dict.get``) and creates no side effects,
so no monkeypatching/teardown is required to avoid state pollution.
"""

import re

import pytest

from blib2to3.pgen2 import literals


def _match(raw):
    """Build a real ``re.Match`` shaped like the one evalstr's regex produces.

    ``raw`` must start with a backslash; group(1) captures the escape
    "tail" (everything after the backslash) that literals.escape inspects,
    so ``m.group(0, 1)`` behaves exactly as inside the tokenizer.
    """
    assert raw.startswith("\\")
    m = re.match(r"\\(.+)", raw)
    assert m is not None
    return m


def test_escape_simple_escape_returns_mapping_value():
    # Lines 26-30: a known simple escape is looked up in simple_escapes.
    assert literals.escape(_match("\\n")) == "\n"
    assert literals.escape(_match("\\t")) == "\t"
    assert literals.escape(_match("\\\\")) == "\\"


def test_escape_hex_escape_success():
    # Lines 31-32, 35-36, 44: a valid \xHH escape decodes through chr().
    assert literals.escape(_match("\\x41")) == "A"
    assert literals.escape(_match("\\x7a")) == "z"


def test_escape_octal_escape_success():
    # Lines 40-41, 44: a valid octal escape decodes through chr().
    assert literals.escape(_match("\\101")) == "A"
    assert literals.escape(_match("\\0")) == "\x00"


def test_escape_hex_escape_needs_two_digits():
    # Lines 33-34: \x followed by fewer than two hex digits is rejected.
    with pytest.raises(ValueError) as excinfo:
        literals.escape(_match("\\x1"))
    assert "invalid hex string escape" in str(excinfo.value)
    assert "\\x1" in str(excinfo.value)


def test_escape_hex_escape_rejects_non_hex_digits():
    # Lines 37-38: \x followed by non-hexadecimal digits is rejected.
    with pytest.raises(ValueError) as excinfo:
        literals.escape(_match("\\xzz"))
    assert "invalid hex string escape" in str(excinfo.value)
    assert "\\xzz" in str(excinfo.value)


def test_escape_octal_escape_rejects_non_octal_digits():
    # Lines 42-43: a non-octal tail is rejected with the octal message.
    with pytest.raises(ValueError) as excinfo:
        literals.escape(_match("\\9"))
    assert "invalid octal string escape" in str(excinfo.value)
    assert "\\9" in str(excinfo.value)


def test_escape_does_not_mutate_simple_escapes():
    # Postcondition guard: escape() must leave the module state untouched.
    before = dict(literals.simple_escapes)
    literals.escape(_match("\\n"))
    literals.escape(_match("\\x41"))
    literals.escape(_match("\\101"))
    assert literals.simple_escapes == before
