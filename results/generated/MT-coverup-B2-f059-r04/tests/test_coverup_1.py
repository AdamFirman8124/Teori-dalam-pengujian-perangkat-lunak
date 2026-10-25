# file: project/f059/__init__.py:1-14
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], "branches": [[4, 5], [4, 6], [6, 7], [6, 9], [7, 6], [7, 8], [11, 12], [11, 14], [12, 11], [12, 13]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], "branches": [[4, 5], [4, 6], [6, 7], [6, 9], [7, 6], [7, 8], [11, 12], [11, 14], [12, 11], [12, 13]]}

import builtins

from f059 import largest_prime_factor


def test_largest_prime_factor_results():
    assert largest_prime_factor(0) == 1
    assert largest_prime_factor(2) == 2
    assert largest_prime_factor(10) == 5
    assert largest_prime_factor(12) == 3
    assert largest_prime_factor(13) == 13


def test_is_prime_rejects_value_below_two(monkeypatch):
    function_globals = largest_prime_factor.__globals__
    sentinel = object()
    previous_range = function_globals.get("range", sentinel)

    def controlled_range(*args):
        if args == (2, 7):
            return (1, 2, 3, 4, 6)
        return builtins.range(*args)

    with monkeypatch.context() as patch:
        patch.setitem(function_globals, "range", controlled_range)
        assert largest_prime_factor(6) == 3

    if previous_range is sentinel:
        assert "range" not in function_globals
    else:
        assert function_globals["range"] is previous_range
