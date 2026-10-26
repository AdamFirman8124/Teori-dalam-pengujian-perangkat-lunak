# file: project/pysnooper/utils.py:81-87
# asked: {"lines": [82, 83, 85, 86, 87], "branches": [[82, 83], [82, 85]]}
# gained: {"lines": [82, 83, 85, 86, 87], "branches": [[82, 83], [82, 85]]}

from pysnooper import utils


class TestTruncate(object):
    def test_truncate_string_shorter_than_max_length(self):
        result = utils.truncate('hello', 10)
        assert result == 'hello'

    def test_truncate_string_equal_to_max_length(self):
        result = utils.truncate('hello', 5)
        assert result == 'hello'

    def test_truncate_string_longer_than_max_length(self):
        result = utils.truncate('hello world', 8)
        # left = (8 - 3) // 2 = 2, right = 8 - 3 - 2 = 3
        assert result == 'he...rld'

    def test_truncate_with_max_length_none(self):
        result = utils.truncate('hello world', None)
        assert result == 'hello world'

    def test_truncate_with_max_length_three(self):
        result = utils.truncate('hello', 3)
        # left = 0, right = 0, string[-0:] == string[0:] == full string
        assert result == '...hello'

    def test_truncate_with_max_length_four(self):
        result = utils.truncate('hello', 4)
        # left = 0, right = 1
        assert result == '...o'
