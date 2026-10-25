

# Generated at 2026-10-24 11:05:46.568602
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

# Generated at 2026-10-24 11:05:53.098391
# Unit test for function get_odd_collatz
def test_get_odd_collatz():
    assert module_0.get_odd_collatz(1) == [1]
    assert module_0.get_odd_collatz(2) == [1]
    assert module_0.get_odd_collatz(6) == [1, 3, 5]
    assert module_0.get_odd_collatz(3) == [1, 3, 5]
    assert module_0.get_odd_collatz(7) == [1, 5, 11, 13, 17]
    assert module_0.get_odd_collatz(14) == [1, 5, 11, 13, 17]
    assert module_0.get_odd_collatz(5) == [1, 5]

# Generated at 2026-10-24 11:05:55.631403
# Unit test for function get_odd_collatz

# Generated at 2026-10-24 11:05:58.051234
# Unit test for function get_odd_collatz

# Generated at 2026-10-24 11:06:00.486830
# Unit test for function get_odd_collatz

# Generated at 2026-10-24 11:06:03.009209
# Unit test for function get_odd_collatz

# Generated at 2026-10-24 11:06:05.545144
# Unit test for function get_odd_collatz

# Generated at 2026-10-24 11:06:07.973786
# Unit test for function get_odd_collatz

# Generated at 2026-10-24 11:06:10.390302
# Unit test for function get_odd_collatz

# Generated at 2026-10-24 11:06:12.808451
# Unit test for function get_odd_collatz

# Generated at 2026-10-24 11:06:15.232112
# Unit test for function get_odd_collatz

# Generated at 2026-10-24 11:06:17.649389
# Unit test for function get_odd_collatz

# Generated at 2026-10-24 11:06:20.066940
# Unit test for function get_odd_collatz

# Generated at 2026-10-24 11:06:22.645561
# Unit test for function get_odd_collatz