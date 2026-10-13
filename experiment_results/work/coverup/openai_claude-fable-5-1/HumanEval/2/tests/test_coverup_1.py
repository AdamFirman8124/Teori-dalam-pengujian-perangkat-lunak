# file: script_2.py:1-10
# asked: {"lines": [10], "branches": []}
# gained: {"lines": [10], "branches": []}

def test_truncate_number_basic():
    from script_2 import truncate_number
    assert truncate_number(3.5) == 0.5
    assert truncate_number(10.25) == 0.25
    assert abs(truncate_number(2.75) - 0.75) < 1e-9
