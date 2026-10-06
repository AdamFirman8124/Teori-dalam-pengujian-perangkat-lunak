# file: script_147.py:1-22
# asked: {"lines": [15, 16, 17, 18, 19, 20, 21, 22], "branches": [[17, 18], [17, 22], [18, 17], [18, 19], [19, 18], [19, 20], [20, 19], [20, 21]]}
# gained: {"lines": [15, 16, 17, 18, 19, 20, 21, 22], "branches": [[17, 18], [17, 22], [18, 17], [18, 19], [19, 18], [19, 20], [20, 19], [20, 21]]}

import pytest
from script_147 import get_max_triples


def test_get_max_triples_n5():
    result = get_max_triples(5)
    assert result == 1
    assert isinstance(result, int)


def test_get_max_triples_n1():
    result = get_max_triples(1)
    assert result == 0
    assert isinstance(result, int)


def test_get_max_triples_n2():
    result = get_max_triples(2)
    assert result == 0
    assert isinstance(result, int)


def test_get_max_triples_n3():
    result = get_max_triples(3)
    assert result >= 0
    assert isinstance(result, int)


def test_get_max_triples_n6():
    result = get_max_triples(6)
    assert result >= 0
    assert isinstance(result, int)


def test_get_max_triples_n10():
    result = get_max_triples(10)
    assert result >= 0
    assert isinstance(result, int)
