# file: project/pymonet/either.py:70-79
# asked: {"lines": [77, 79], "branches": []}
# gained: {"lines": [77, 79], "branches": []}

from pymonet.either import Either
from pymonet.lazy import Lazy


def test_either_to_lazy_returns_deferred_memoized_value():
    initial_value = object()
    updated_value = object()
    either = Either(initial_value)

    lazy = either.to_lazy()

    assert isinstance(lazy, Lazy)
    assert lazy.is_evaluated is False

    either.value = updated_value

    assert lazy.get() is updated_value
    assert lazy.is_evaluated is True

    either.value = object()
    assert lazy.get() is updated_value
