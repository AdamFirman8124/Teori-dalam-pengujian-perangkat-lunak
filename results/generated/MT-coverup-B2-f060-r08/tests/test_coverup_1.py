# file: project/f060/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import f060


def test_sum_to_n_executes_return_line():
    # Calling the function executes line 3: `return sum(range(n + 1))`
    assert f060.sum_to_n(5) == 15  # 0+1+2+3+4+5
    assert f060.sum_to_n(0) == 0  # range(1) -> [0]
    assert f060.sum_to_n(-1) == 0  # range(0) -> empty
    assert f060.sum_to_n(1) == 1
