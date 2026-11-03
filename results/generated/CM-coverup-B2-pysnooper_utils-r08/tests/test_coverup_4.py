# file: project/pysnooper/utils.py:81-87
# asked: {"lines": [82, 83, 85, 86, 87], "branches": [[82, 83], [82, 85]]}
# gained: {"lines": [82, 83, 85, 86, 87], "branches": [[82, 83], [82, 85]]}

import pytest

from pysnooper import utils


class TestTruncate:
    """Tests for pysnooper.utils.truncate (lines 82-87 of utils.py)."""

    @pytest.mark.parametrize('string', ['abc', 'hello world', ''])
    def test_truncate_max_length_none_returns_string_unchanged(self, string):
        # Covers the `max_length is None` short-circuit branch of line 82
        # and the early return on line 83.
        assert utils.truncate(string, None) is string

    @pytest.mark.parametrize(
        'string, max_length',
        [
            ('abc', 10),   # shorter than max_length
            ('abc', 3),    # exactly max_length
            ('', 1),       # empty string
        ],
    )
    def test_truncate_short_enough_returns_string_unchanged(self, string, max_length):
        # Covers the `len(string) <= max_length` branch of line 82
        # and the early return on line 83.
        assert utils.truncate(string, max_length) is string

    @pytest.mark.parametrize(
        'string, max_length, expected',
        [
            # left = (7-3)//2 = 2, right = 7-3-2 = 2  ->  'ab' + '...' + 'ij'
            ('abcdefghij', 7, 'ab...ij'),
            # left = (8-3)//2 = 2, right = 8-3-2 = 3  ->  'ab' + '...' + 'hij'
            ('abcdefghij', 8, 'ab...hij'),
            # left = (9-3)//2 = 3, right = 9-3-3 = 3  ->  'abc' + '...' + 'hij'
            ('abcdefghij', 9, 'abc...hij'),
            # left = (10-3)//2 = 3, right = 10-3-3 = 4  ->  'abc' + '...' + 'wxyz'
            ('abcdefghijklmnopqrstuvwxyz', 10, 'abc...wxyz'),
        ],
    )
    def test_truncate_long_string_is_truncated(self, string, max_length, expected):
        # Covers the else branch: lines 85, 86 and 87.
        result = utils.truncate(string, max_length)
        assert result == expected
        # Postcondition: the truncated result is exactly max_length long.
        assert len(result) == max_length
        # Postcondition: the ellipsis marker is present exactly once.
        assert result.count('...') == 1
        # Postcondition: the kept characters come from the original string's
        # head and tail.
        left = (max_length - 3) // 2
        right = max_length - 3 - left
        assert result == string[:left] + '...' + string[-right:]

    def test_truncate_long_string_preserves_head_and_tail(self):
        # Sanity check that truncation keeps the original head and tail.
        # For max_length=10: left = (10-3)//2 = 3, right = 10-3-3 = 4.
        string = 'abcdefghijklmnopqrstuvwxyz'
        result = utils.truncate(string, 10)
        assert result.startswith('abc')
        assert result.endswith('wxyz')
        assert result == 'abc...wxyz'
        assert len(result) == 10
