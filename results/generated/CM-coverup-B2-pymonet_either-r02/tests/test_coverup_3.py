# file: project/pymonet/either.py:48-57
# asked: {"lines": [55, 57], "branches": []}
# gained: {"lines": [55, 57], "branches": []}

import pytest

from pymonet.box import Box
from pymonet.either import Left, Right


@pytest.mark.parametrize("either", [Left("error"), Right(42)])
def test_either_to_box_preserves_value(either):
    result = either.to_box()

    assert isinstance(result, Box)
    assert result.value == either.value
