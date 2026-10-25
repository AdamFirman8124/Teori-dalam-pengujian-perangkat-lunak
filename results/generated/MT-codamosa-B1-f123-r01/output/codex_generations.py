

# Generated at 2026-10-24 11:55:20.651064
# Unit test for function get_odd_collatz
def test_get_odd_collatz():
    assert module_0.get_odd_collatz(1) == [1]
    assert module_0.get_odd_collatz(2) == [1]
    assert module_0.get_odd_collatz(3) == [1, 3, 5]
    assert module_0.get_odd_collatz(4) == [1]
    assert module_0.get_odd_collatz(5) == [1, 5]
    assert module_0.get_odd_collatz(6) == [1, 3, 5]
    assert module_0.get_odd_collatz(7) == [1, 5, 7, 11, 13, 17]

    # general properties for positive n
    for n in range(1, 20):
        result = module_0.get_odd_collatz(n)
        assert 1 in result
        assert result == sorted(result)

# Generated at 2026-10-24 11:55:23.068856
# Unit test for function get_odd_collatz

# Generated at 2026-10-24 11:55:24.447936
# Unit test for function get_odd_collatz
def test_get_odd_collatz():
    assert module_0.get_odd_collatz(1) == [1]
    assert module_0.get_odd_collatz(2) == [1]
    assert module_0.get_odd_collatz(6) == [1, 3, 5]
    assert module_0.get_odd_collatz(3) == [1, 3, 5]
    assert module_0.get_odd_collatz(7) == [1, 5, 11, 13, 17]
    assert module_0.get_odd_collatz(14) == [1, 5, 11, 13, 17]
    assert module_0.get_odd_collatz(5) == [1, 5]

# Generated at 2026-10-24 11:55:40.894974
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

# Generated at 2026-10-24 11:55:42.373736
# Unit test for function get_odd_collatz
def test_get_odd_collatz():
    assert module_0.get_odd_collatz(1) == [1]
    assert module_0.get_odd_collatz(2) == [1]
    assert module_0.get_odd_collatz(6) == [1, 3, 5]
    assert module_0.get_odd_collatz(3) == [1, 3, 5]
    assert module_0.get_odd_collatz(7) == [1, 5, 11, 13, 17]
    assert module_0.get_odd_collatz(14) == [1, 5, 11, 13, 17]
    assert module_0.get_odd_collatz(5) == [1, 5]

# Generated at 2026-10-24 11:55:58.874522
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

# Generated at 2026-10-24 11:56:00.294364
# Unit test for function get_odd_collatz
def test_get_odd_collatz():
    assert module_0.get_odd_collatz(1) == [1]
    assert module_0.get_odd_collatz(2) == [1]
    assert module_0.get_odd_collatz(6) == [1, 3, 5]
    assert module_0.get_odd_collatz(3) == [1, 3, 5]
    assert module_0.get_odd_collatz(7) == [1, 5, 11, 13, 17]
    assert module_0.get_odd_collatz(14) == [1, 5, 11, 13, 17]
    assert module_0.get_odd_collatz(5) == [1, 5]

# Generated at 2026-10-24 11:56:01.654659
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

# Generated at 2026-10-24 11:56:02.967505
# Unit test for function get_odd_collatz
def test_get_odd_collatz():
    assert module_0.get_odd_collatz(1) == [1]
    assert module_0.get_odd_collatz(2) == [1]
    assert module_0.get_odd_collatz(6) == [1, 3, 5]
    assert module_0.get_odd_collatz(3) == [1, 3, 5]
    assert module_0.get_odd_collatz(7) == [1, 5, 11, 13, 17]
    assert module_0.get_odd_collatz(14) == [1, 5, 11, 13, 17]
    assert module_0.get_odd_collatz(5) == [1, 5]