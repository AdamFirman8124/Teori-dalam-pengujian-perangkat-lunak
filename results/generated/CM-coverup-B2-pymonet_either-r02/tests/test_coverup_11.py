# file: project/pymonet/either.py:37-46
# asked: {"lines": [46], "branches": []}
# gained: {"lines": [46], "branches": []}

from unittest.mock import Mock

from pymonet.either import Either


def test_either_ap_maps_its_value_over_applicative():
    mapper = lambda value: value * 2
    expected = object()
    applicative = Mock()
    applicative.map.return_value = expected

    result = Either(mapper).ap(applicative)

    assert result is expected
    applicative.map.assert_called_once_with(mapper)
