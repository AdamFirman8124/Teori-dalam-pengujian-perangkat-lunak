# file: project/f097/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f097 import multiply


def test_multiply_executes_return_statement():
    assert multiply(12, 34) == 8
