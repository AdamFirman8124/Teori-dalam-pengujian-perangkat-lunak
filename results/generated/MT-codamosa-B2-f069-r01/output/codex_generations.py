

# Generated at 2026-10-25 12:12:58.889845
# Unit test for function search
def test_search():
    # Examples from docstring
    assert module_0.search([4, 1, 2, 2, 3, 1]) == 2
    assert module_0.search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
    assert module_0.search([5, 5, 4, 4, 4]) == -1

    # frequency == value qualifies
    assert module_0.search([1]) == 1
    assert module_0.search([2, 2]) == 2
    assert module_0.search([3, 3, 3]) == 3
    assert module_0.search([4, 4, 4, 4]) == 4
    assert module_0.search([5, 5, 5, 5, 5]) == 5

    # frequency < value -> -1
    assert module_0.search([2]) == -1
    assert module_0.search([3, 3]) == -1
    assert module_0.search([10]) == -1

    # return greatest, not smallest / first
    assert module_0.search([1, 2, 2]) == 2
    assert module_0.search([1, 1]) == 1
    assert module_0.search([1, 1, 1]) == 1

# Generated at 2026-10-25 12:13:02.166486
# Unit test for function search
def test_search():
    # Examples from docstring
    assert module_0.search([4, 1, 2, 2, 3, 1]) == 2
    assert module_0.search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
    assert module_0.search([5, 5, 4, 4, 4]) == -1

    # frequency == value qualifies
    assert module_0.search([1]) == 1
    assert module_0.search([2, 2]) == 2
    assert module_0.search([3, 3, 3]) == 3
    assert module_0.search([4, 4, 4, 4]) == 4
    assert module_0.search([5, 5, 5, 5, 5]) == 5

    # frequency < value -> -1
    assert module_0.search([2]) == -1
    assert module_0.search([3, 3]) == -1
    assert module_0.search([10]) == -1

    # return greatest, not smallest / first
    assert module_0.search([1, 2, 2]) == 2
    assert module_0.search([1, 1]) == 1
    assert module_0.search([1, 1, 1]) == 1

# Generated at 2026-10-25 12:13:05.136648
# Unit test for function search
def test_search():
    # Examples from docstring
    assert module_0.search([4, 1, 2, 2, 3, 1]) == 2
    assert module_0.search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
    assert module_0.search([5, 5, 4, 4, 4]) == -1

    # frequency == value qualifies
    assert module_0.search([1]) == 1
    assert module_0.search([2, 2]) == 2
    assert module_0.search([3, 3, 3]) == 3
    assert module_0.search([4, 4, 4, 4]) == 4
    assert module_0.search([5, 5, 5, 5, 5]) == 5

    # frequency < value -> -1
    assert module_0.search([2]) == -1
    assert module_0.search([3, 3]) == -1
    assert module_0.search([10]) == -1

    # return greatest, not smallest / first
    assert module_0.search([1, 2, 2]) == 2
    assert module_0.search([1, 1]) == 1
    assert module_0.search([1, 1, 1]) == 1

# Generated at 2026-10-25 12:13:17.935918
# Unit test for function search
def test_search():
    # Examples from docstring
    assert module_0.search([4, 1, 2, 2, 3, 1]) == 2
    assert module_0.search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
    assert module_0.search([5, 5, 4, 4, 4]) == -1

    # frequency == value qualifies
    assert module_0.search([1]) == 1
    assert module_0.search([2, 2]) == 2
    assert module_0.search([3, 3, 3]) == 3
    assert module_0.search([4, 4, 4, 4]) == 4
    assert module_0.search([5, 5, 5, 5, 5]) == 5

    # frequency < value -> -1
    assert module_0.search([2]) == -1
    assert module_0.search([3, 3]) == -1
    assert module_0.search([10]) == -1

    # return greatest, not smallest / first
    assert module_0.search([1, 2, 2]) == 2
    assert module_0.search([1, 1]) == 1
    assert module_0.search([1, 1, 1]) == 1

# Generated at 2026-10-25 12:13:23.912993
# Unit test for function search
def test_search():
    # Examples from docstring
    assert module_0.search([4, 1, 2, 2, 3, 1]) == 2
    assert module_0.search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
    assert module_0.search([5, 5, 4, 4, 4]) == -1

    # frequency == value qualifies
    assert module_0.search([1]) == 1
    assert module_0.search([2, 2]) == 2
    assert module_0.search([3, 3, 3]) == 3
    assert module_0.search([4, 4, 4, 4]) == 4
    assert module_0.search([5, 5, 5, 5, 5]) == 5

    # frequency < value -> -1
    assert module_0.search([2]) == -1
    assert module_0.search([3, 3]) == -1
    assert module_0.search([10]) == -1

    # return greatest, not smallest / first
    assert module_0.search([1, 2, 2]) == 2
    assert module_0.search([1, 1]) == 1
    assert module_0.search([1, 1, 1]) == 1