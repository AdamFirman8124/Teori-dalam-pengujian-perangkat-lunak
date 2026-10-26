# file: project/f147/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10], "branches": [[5, 6], [5, 10], [6, 5], [6, 7], [7, 6], [7, 8], [8, 7], [8, 9]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10], "branches": [[5, 6], [5, 10], [6, 5], [6, 7], [7, 6], [7, 8], [8, 7], [8, 9]]}

from f147 import get_max_triples


def test_get_max_triples_exercises_matching_and_nonmatching_triples():
    assert get_max_triples(4) == 1


def test_get_max_triples_with_too_few_values():
    assert get_max_triples(2) == 0
