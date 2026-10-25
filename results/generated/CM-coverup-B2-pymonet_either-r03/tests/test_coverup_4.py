# file: project/pymonet/either.py:59-68
# asked: {"lines": [66, 68], "branches": []}
# gained: {"lines": [66, 68], "branches": []}

import pytest

from pymonet.either import Left, Right
from pymonet.monad_try import Try


@pytest.mark.parametrize(
    ("either", "expected_value", "expected_success"),
    [
        (Right("success"), "success", True),
        (Left("failure"), "failure", False),
    ],
)
def test_to_try_preserves_value_and_success_state(
    either, expected_value, expected_success
):
    result = either.to_try()

    assert isinstance(result, Try)
    assert result.value == expected_value
    assert result.is_success is expected_success
