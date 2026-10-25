# file: project/f028/__init__.py:4-6
# asked: {"lines": [6], "branches": []}
# gained: {"lines": [6], "branches": []}

from f028 import concatenate


def test_concatenate_joins_strings() -> None:
    assert concatenate(["foo", "bar", "baz"]) == "foobarbaz"
