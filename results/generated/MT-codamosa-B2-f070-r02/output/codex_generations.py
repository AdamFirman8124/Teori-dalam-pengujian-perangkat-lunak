

# Generated at 2026-10-24 21:08:20.970129
# Unit test for function strange_sort_list

# Generated at 2026-10-24 21:08:23.382580
# Unit test for function strange_sort_list

# Generated at 2026-10-24 21:08:25.815719
# Unit test for function strange_sort_list

# Generated at 2026-10-24 21:08:28.236848
# Unit test for function strange_sort_list

# Generated at 2026-10-24 21:08:30.649061
# Unit test for function strange_sort_list

# Generated at 2026-10-24 21:08:33.070295
# Unit test for function strange_sort_list

# Generated at 2026-10-24 21:08:35.487159
# Unit test for function strange_sort_list

# Generated at 2026-10-24 21:08:37.905365
# Unit test for function strange_sort_list

# Generated at 2026-10-24 21:08:41.773095
# Unit test for function strange_sort_list
def test_strange_sort_list():assert module_0.strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]

# Generated at 2026-10-24 21:08:43.093676
# Unit test for function strange_sort_list
def test_strange_sort_list():import pytest
from strange_sort_list import strange_sort_list

@pytest.mark.parametrize("inp, expected", [
    ([], []),                    # empty
    ([7], [7]),                  # single
    ([1, 2, 3, 4], [1, 4, 2, 3]),
    ([5, 0, 3, 1], [0, 5, 1, 3]),
    ([3, 1, 2], [1, 3, 2]),      # odd length
    ([3, 3, 1], [1, 3, 3]),      # duplicates
    ([-2, 0, -5, 9], [-5, 9, -2, 0]),
])
def test_strange_sort_list(inp, expected):
    assert module_0.strange_sort_list(inp) == expected

def test_mutates_input():
    data = [4, 1, 3]
    module_0.strange_sort_list(data)
    assert data == []            # function empties the input list

# Generated at 2026-10-24 21:08:44.415597
# Unit test for function strange_sort_list
def test_strange_sort_list():assert module_0.strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]

# Generated at 2026-10-24 21:08:45.748353
# Unit test for function strange_sort_list
def test_strange_sort_list():import pytest
from strange_sort_list import strange_sort_list

@pytest.mark.parametrize("inp, expected", [
    ([], []),                    # empty
    ([7], [7]),                  # single
    ([1, 2, 3, 4], [1, 4, 2, 3]),
    ([5, 0, 3, 1], [0, 5, 1, 3]),
    ([3, 1, 2], [1, 3, 2]),      # odd length
    ([3, 3, 1], [1, 3, 3]),      # duplicates
    ([-2, 0, -5, 9], [-5, 9, -2, 0]),
])
def test_strange_sort_list(inp, expected):
    assert module_0.strange_sort_list(inp) == expected

def test_mutates_input():
    data = [4, 1, 3]
    module_0.strange_sort_list(data)
    assert data == []            # function empties the input list

# Generated at 2026-10-24 21:08:47.065229
# Unit test for function strange_sort_list
def test_strange_sort_list():assert module_0.strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]