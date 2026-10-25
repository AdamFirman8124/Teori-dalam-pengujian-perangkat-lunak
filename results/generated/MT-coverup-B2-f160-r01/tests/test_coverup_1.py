# file: project/f160/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": [[4, 5], [4, 6]]}
# gained: {"lines": [3, 4, 5, 6], "branches": [[4, 5], [4, 6]]}

import builtins

import pytest

from f160 import do_algebra


def test_do_algebra_single_operand_skips_loop():
    # Loop body (lines 4-5) must not run when there is only one operand.
    assert do_algebra([], [7]) == 7


def test_do_algebra_addition():
    assert do_algebra(["+", "+"], [1, 2, 3]) == 6


def test_do_algebra_mixed_operators_respect_precedence():
    # "2+3*4-5" -> 2 + 12 - 5 == 9
    assert do_algebra(["+", "*", "-"], [2, 3, 4, 5]) == 9


def test_do_algebra_power_operator():
    # "2**3+1" -> 8 + 1 == 9
    assert do_algebra(["**", "+"], [2, 3, 1]) == 9


def test_do_algebra_builds_expected_expression(monkeypatch):
    captured = {}

    def fake_eval(expression):
        captured["expression"] = expression
        return "sentinel"

    monkeypatch.setattr(builtins, "eval", fake_eval)

    result = do_algebra(["+", "*", "-"], [2, 3, 4, 5])

    assert result == "sentinel"
    assert captured["expression"] == "2+3*4-5"


def test_do_algebra_does_not_mutate_inputs():
    operator = ["+", "*"]
    operand = [2, 3, 4]

    assert do_algebra(operator, operand) == 14
    assert operator == ["+", "*"]
    assert operand == [2, 3, 4]
