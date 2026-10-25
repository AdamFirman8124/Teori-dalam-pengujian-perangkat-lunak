# file: project/f022/__init__.py:4-6
# asked: {"lines": [6], "branches": []}
# gained: {"lines": [6], "branches": []}

from f022 import filter_integers


def test_filter_integers_keeps_only_integer_values():
    values = [1, "2", 3.0, None, -4, [], object()]

    result = filter_integers(values)

    assert result == [1, -4]
    assert values[:6] == [1, "2", 3.0, None, -4, []]
