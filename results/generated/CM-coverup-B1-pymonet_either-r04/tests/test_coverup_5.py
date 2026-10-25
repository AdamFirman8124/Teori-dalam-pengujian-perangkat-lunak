# file: project/pymonet/either.py:70-79
# asked: {"lines": [77, 79], "branches": []}
# gained: {"lines": [77, 79], "branches": []}

import pytest

from pymonet.either import Left, Right
from pymonet.lazy import Lazy


@pytest.mark.parametrize("either_type", [Left, Right])
def test_either_to_lazy_returns_lazy_containing_value(either_type):
    value = object()
    either = either_type(value)

    lazy = either.to_lazy()

    assert isinstance(lazy, Lazy)
    assert lazy.is_evaluated is False
    assert lazy.get() is value
    assert lazy.is_evaluated is True
    assert lazy.value is value
