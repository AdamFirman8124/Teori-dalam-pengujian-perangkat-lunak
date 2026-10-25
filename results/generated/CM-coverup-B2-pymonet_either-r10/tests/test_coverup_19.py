# file: project/pymonet/either.py:164-173
# asked: {"lines": [173], "branches": []}
# gained: {"lines": [173], "branches": []}

from unittest.mock import Mock

from pymonet.either import Right


def test_right_bind_calls_mapper_with_value_and_returns_its_result():
    value = object()
    expected = object()
    mapper = Mock(return_value=expected)

    result = Right(value).bind(mapper)

    assert result is expected
    mapper.assert_called_once_with(value)
