# file: project/pymonet/either.py:70-79
# asked: {"lines": [77, 79], "branches": []}
# gained: {"lines": [77, 79], "branches": []}

from pymonet.either import Either
from pymonet.lazy import Lazy


def test_either_to_lazy_returns_lazy_containing_value():
    either = Either("value")

    lazy = either.to_lazy()

    assert isinstance(lazy, Lazy)
    assert lazy.is_evaluated is False
    assert lazy.get() == "value"
    assert lazy.is_evaluated is True
