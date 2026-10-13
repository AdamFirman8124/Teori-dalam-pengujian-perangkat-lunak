# file: script_0.py:4-19
# asked: {"lines": [12, 13, 14, 15, 16, 17, 19], "branches": [[12, 13], [12, 19], [13, 12], [13, 14], [14, 13], [14, 15], [16, 13], [16, 17]]}
# gained: {"lines": [12, 13, 14, 15, 16, 17, 19], "branches": [[12, 13], [12, 19], [13, 12], [13, 14], [14, 13], [14, 15], [16, 13], [16, 17]]}

import importlib
import importlib.util
import os
import sys

import pytest


@pytest.fixture
def has_close_elements():
    try:
        module = importlib.import_module("script_0")
    except Exception:
        module = None
        candidates = [
            os.path.join(os.getcwd(), "script_0.py"),
            os.path.join(os.path.dirname(__file__), "script_0.py"),
        ]
        for path in candidates:
            if os.path.exists(path):
                spec = importlib.util.spec_from_file_location("script_0", path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                break
        if module is None:
            pytest.skip("script_0 module not available")
    return module.has_close_elements


def test_returns_true_when_pair_closer_than_threshold(has_close_elements):
    assert has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3) is True
    assert has_close_elements([1.0, 1.1], 0.5) is True


def test_returns_false_when_all_pairs_far_apart(has_close_elements):
    assert has_close_elements([1.0, 2.0, 3.0], 0.5) is False


def test_distance_equal_to_threshold_is_not_close(has_close_elements):
    assert has_close_elements([1.0, 1.5], 0.5) is False


def test_single_and_empty_elements(has_close_elements):
    assert has_close_elements([1.0], 0.1) is False
    assert has_close_elements([], 0.1) is False


def test_duplicates_are_close(has_close_elements):
    assert has_close_elements([2.0, 5.0, 2.0], 0.0001) is True
