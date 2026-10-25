

# Generated at 2026-10-24 11:25:15.161735
# Unit test for function get_odd_collatz
def test_get_odd_collatz():import pytest
from solution import get_odd_collatz  # adjust import to your file

@pytest.mark.parametrize("n, expected", [
    (1, [1]),
    (2, [1]),
    (3, [1, 3, 5]),
    (5, [1, 5]),
    (6, [1, 3, 5]),
    (7, [1, 5, 7, 11, 13, 17]),
])
def test_get_odd_collatz(n, expected):
    assert module_0.get_odd_collatz(n) == expected


def test_result_is_sorted_and_all_odd():
    result = module_0.get_odd_collatz(27)
    assert result == sorted(result)
    assert all(x % 2 == 1 for x in result)
    assert result[0] == 1  # Collatz always reaches 1

# Generated at 2026-10-24 11:25:17.680904
# Unit test for function get_odd_collatz

# Generated at 2026-10-24 11:25:20.211336
# Unit test for function get_odd_collatz

# Generated at 2026-10-24 11:25:22.823243
# Unit test for function get_odd_collatz

# Generated at 2026-10-24 11:25:25.243106
# Unit test for function get_odd_collatz

# Generated at 2026-10-24 11:25:27.663234
# Unit test for function get_odd_collatz

# Generated at 2026-10-24 11:25:30.083494
# Unit test for function get_odd_collatz

# Generated at 2026-10-24 11:25:32.506980
# Unit test for function get_odd_collatz

# Generated at 2026-10-24 11:25:34.924556
# Unit test for function get_odd_collatz

# Generated at 2026-10-24 11:25:37.344496
# Unit test for function get_odd_collatz

# Generated at 2026-10-24 11:25:39.767249
# Unit test for function get_odd_collatz

# Generated at 2026-10-24 11:25:42.183717
# Unit test for function get_odd_collatz

# Generated at 2026-10-24 11:25:57.121157
# Unit test for function get_odd_collatz

# Generated at 2026-10-24 11:25:58.428849
# Unit test for function get_odd_collatz
def test_get_odd_collatz():
    assert module_0.get_odd_collatz(1) == [1]
    assert module_0.get_odd_collatz(2) == [1]
    assert module_0.get_odd_collatz(6) == [1, 3, 5]
    assert module_0.get_odd_collatz(3) == [1, 3, 5]
    assert module_0.get_odd_collatz(7) == [1, 5, 11, 13, 17]
    assert module_0.get_odd_collatz(14) == [1, 5, 11, 13, 17]
    assert module_0.get_odd_collatz(5) == [1, 5]