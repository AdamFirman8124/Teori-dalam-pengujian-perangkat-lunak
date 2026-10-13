# file: script_0.py:4-19
# asked: {"lines": [12, 13, 14, 15, 16, 17, 19], "branches": [[12, 13], [12, 19], [13, 12], [13, 14], [14, 13], [14, 15], [16, 13], [16, 17]]}
# gained: {"lines": [12, 13, 14, 15, 16, 17, 19], "branches": [[12, 13], [12, 19], [13, 12], [13, 14], [14, 13], [14, 15], [16, 13], [16, 17]]}

import pytest
from typing import List


@pytest.fixture
def has_close_elements_func():
    import importlib
    module = None
    for name in ("script_0", "solution"):
        try:
            module = importlib.import_module(name)
            break
        except ImportError:
            continue
    if module is None:
        pytest.skip("module under test not importable")
    importlib.reload(module)
    yield module.has_close_elements


def test_doctest_false(has_close_elements_func):
    f = has_close_elements_func
    assert f([1.0, 2.0, 3.0], 0.5) is False


def test_doctest_true(has_close_elements_func):
    f = has_close_elements_func
    assert f([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3) is True


def test_empty_list(has_close_elements_func):
    f = has_close_elements_func
    assert f([], 0.1) is False


def test_single_element(has_close_elements_func):
    f = has_close_elements_func
    assert f([5.0], 0.1) is False


def test_boundary_exactly_threshold(has_close_elements_func):
    f = has_close_elements_func
    # distance == threshold, not less than -> False
    assert f([1.0, 2.0], 1.0) is False


def test_duplicates(has_close_elements_func):
    f = has_close_elements_func
    assert f([2.0, 2.0], 0.5) is True


def test_negative_numbers(has_close_elements_func):
    f = has_close_elements_func
    assert f([-1.0, -1.4, 10.0], 0.5) is True
    assert f([-1.0, -1.4, 10.0], 0.3) is False
