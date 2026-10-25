# file: project/f067/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}

def test_fruit_distribution_handles_numeric_and_non_numeric_tokens():
    from f067 import fruit_distribution

    assert fruit_distribution("5 apples and 6 oranges", 20) == 9
    assert fruit_distribution("no fruit distributed", 20) == 20
