# file: script_2.py:1-10
# asked: {"lines": [10], "branches": []}
# gained: {"lines": [10], "branches": []}

def test_truncate_number_basic():
    from script_2 import truncate_number

    assert truncate_number(3.5) == 0.5
    assert truncate_number(0.0) == 0.0
    assert truncate_number(2.75) == 0.75
    assert truncate_number(1.0) == 0.0
    assert truncate_number(123.456) == 123.456 % 1.0


def test_truncate_number_small_values():
    from script_2 import truncate_number

    assert truncate_number(0.125) == 0.125
    assert truncate_number(0.999999) == 0.999999
    assert truncate_number(1.5) == 0.5
