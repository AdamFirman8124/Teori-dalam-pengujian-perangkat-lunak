# file: project/pymonet/either.py:164-173
# asked: {"lines": [173], "branches": []}
# gained: {"lines": [173], "branches": []}

from unittest.mock import Mock

from pymonet.either import Right


def test_right_bind_calls_mapper_with_wrapped_value_and_returns_result():
    value = object()
    expected = object()
    mapper = Mock(return_value=expected)

    result = Right(value).bind(mapper)

    mapper.assert_called_once_with(value)
    assert result is expected
