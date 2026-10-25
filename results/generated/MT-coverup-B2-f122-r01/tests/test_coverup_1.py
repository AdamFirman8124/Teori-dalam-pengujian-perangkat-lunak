# file: project/f122/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

def test_add_elements_executes_sum_and_filter_branches():
    from f122 import add_elements

    assert add_elements([1, -2, 100, 99], 4) == 98
