# file: project/pymonet/either.py:22-35
# asked: {"lines": [33, 34, 35], "branches": [[33, 34], [33, 35]]}
# gained: {"lines": [33, 34, 35], "branches": [[33, 34], [33, 35]]}

import pytest

from pymonet.either import Left, Right


def test_case_on_right_calls_success_handler():
    either = Right(42)
    calls = []

    def error(value):
        calls.append(('error', value))
        return 'error'

    def success(value):
        calls.append(('success', value))
        return 'success'

    result = either.case(error, success)

    assert result == 'success'
    assert calls == [('success', 42)]
    assert either.value == 42


def test_case_on_left_calls_error_handler():
    either = Left('boom')
    calls = []

    def error(value):
        calls.append(('error', value))
        return 'handled'

    def success(value):
        calls.append(('success', value))
        return 'success'

    result = either.case(error, success)

    assert result == 'handled'
    assert calls == [('error', 'boom')]
    assert either.value == 'boom'


def test_case_returns_handler_result_verbatim():
    sentinel = object()

    assert Right(1).case(lambda _: 'err', lambda _: sentinel) is sentinel
    assert Left(1).case(lambda _: sentinel, lambda _: 'ok') is sentinel


def test_case_does_not_mutate_either(monkeypatch):
    either = Right(7)
    monkeypatch.setattr(either, 'value', 7, raising=False)

    assert either.case(lambda v: v, lambda v: v * 2) == 14
    assert either.value == 7
    assert either.is_right() is True
    assert either.is_left() is False
