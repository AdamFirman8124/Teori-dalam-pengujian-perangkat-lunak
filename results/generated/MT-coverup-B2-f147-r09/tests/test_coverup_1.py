# file: project/f147/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10], "branches": [[5, 6], [5, 10], [6, 5], [6, 7], [7, 6], [7, 8], [8, 7], [8, 9]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10], "branches": [[5, 6], [5, 10], [6, 5], [6, 7], [7, 6], [7, 8], [8, 7], [8, 9]]}

import pytest

from f147 import get_max_triples


def test_get_max_triples_zero():
    assert get_max_triples(0) == 0


def test_get_max_triples_too_few_elements():
    assert get_max_triples(1) == 0
    assert get_max_triples(2) == 0


def test_get_max_triples_no_valid_triple():
    # A = [1, 3, 7]; 1 + 3 + 7 = 11, 11 % 3 != 0
    assert get_max_triples(3) == 0


def test_get_max_triples_one_valid_triple():
    # A = [1, 3, 7, 13]; only (1, 7, 13) sums to a multiple of 3
    assert get_max_triples(4) == 1


@pytest.mark.parametrize(
    ("n", "expected"),
    [
        (5, 1),
        (6, 4),
        (7, 10),
        (8, 11),
    ],
)
def test_get_max_triples_larger_inputs(n, expected):
    result = get_max_triples(n)
    assert isinstance(result, int)
    assert result == expected
