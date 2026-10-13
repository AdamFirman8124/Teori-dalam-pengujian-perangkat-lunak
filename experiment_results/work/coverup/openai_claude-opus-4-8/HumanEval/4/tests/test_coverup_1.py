# file: script_4.py:4-14
# asked: {"lines": [13, 14], "branches": []}
# gained: {"lines": [13, 14], "branches": []}

import pytest

try:
    import script_4
except ImportError:  # pragma: no cover
    script_4 = pytest.importorskip("script_4")


@pytest.fixture()
def mad():
    return script_4.mean_absolute_deviation


def test_documented_example(mad):
    assert mad([1.0, 2.0, 3.0, 4.0]) == 1.0


def test_symmetric_dataset(mad):
    assert mad([2.0, 4.0, 6.0]) == pytest.approx(4.0 / 3.0)


def test_identical_values_gives_zero(mad):
    assert mad([5.0, 5.0, 5.0]) == 0.0


def test_single_value_gives_zero(mad):
    assert mad([7.5]) == 0.0


def test_integer_inputs(mad):
    assert mad([1, 2, 3, 4, 5]) == pytest.approx(1.2)
