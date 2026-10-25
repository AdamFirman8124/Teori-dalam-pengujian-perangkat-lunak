# file: project/pymonet/either.py:48-57
# asked: {"lines": [55, 57], "branches": []}
# gained: {"lines": [55, 57], "branches": []}

import pytest

from pymonet.box import Box
from pymonet.either import Left, Right


@pytest.mark.parametrize("either_type", [Left, Right])
def test_either_to_box_preserves_value(either_type):
    value = object()

    result = either_type(value).to_box()

    assert isinstance(result, Box)
    assert result.value is value
