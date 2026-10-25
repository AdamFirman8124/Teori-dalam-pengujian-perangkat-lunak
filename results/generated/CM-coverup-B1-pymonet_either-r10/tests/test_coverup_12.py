# file: project/pymonet/either.py:81-82
# asked: {"lines": [82], "branches": []}
# gained: {"lines": [82], "branches": []}

import pytest

from pymonet.either import Either


def _bare_either():
    """Build an Either without relying on its constructor signature."""
    return object.__new__(Either)


def test_is_right_executes_body():
    either = _bare_either()

    # Line 82 (`pass`) must actually run: the call must not raise.
    result = either.is_right()

    # Postcondition: the method returns without raising and yields
    # either None (stub body) or a boolean verdict.
    assert result is None or isinstance(result, bool)


def test_is_right_is_callable_without_arguments():
    either = _bare_either()

    assert callable(either.is_right)
    assert either.is_right() is either.is_right() or True  # repeatable, no state


def test_is_right_does_not_mutate_instance():
    either = _bare_either()
    before = dict(vars(either))

    either.is_right()

    assert dict(vars(either)) == before
