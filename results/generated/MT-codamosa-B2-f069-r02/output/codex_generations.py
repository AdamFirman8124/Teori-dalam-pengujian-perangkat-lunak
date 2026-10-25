

# Generated at 2026-10-24 12:58:28.800425
# Unit test for function search
def test_search():
    # Examples from docstring
    assert module_0.search([4, 1, 2, 2, 3, 1]) == 2
    assert module_0.search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
    assert module_0.search([5, 5, 4, 4, 4]) == -1

    # Single element
    assert module_0.search([1]) == 1
    assert module_0.search([2]) == -1

    # Exact frequency match
    assert module_0.search([2, 2]) == 2
    assert module_0.search([3, 3, 3]) == 3
    assert module_0.search([4, 4, 4, 4]) == 4
    assert module_0.search([5, 5, 5, 5, 5]) == 5

    # Frequency below value
    assert module_0.search([3, 3]) == -1
    assert module_0.search([4, 4, 4]) == -1

    # Multiple values qualify -> return greatest
    assert module_0.search([1, 2, 2]) == 2
    assert module_0.search([1, 1, 2, 2, 2]) == 2
    assert module_0.search([1, 2, 2, 3, 3, 3]) == 3

    # Only 1 qualifies
    assert module_0.search([1, 1, 1]) == 1
    assert module_0.search([1, 2, 3]) == 1

    # No value qualifies
    assert module_0.search([5]) == -1
    assert module_0.search([2, 3, 3]) == -1

# Generated at 2026-10-24 12:58:30.196668
# Unit test for function search
def test_search():
    # Examples from docstring
    assert module_0.search([4, 1, 2, 2, 3, 1]) == 2
    assert module_0.search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
    assert module_0.search([5, 5, 4, 4, 4]) == -1

    # Single element
    assert module_0.search([1]) == 1
    assert module_0.search([2]) == -1

    # Exact frequency match
    assert module_0.search([2, 2]) == 2
    assert module_0.search([3, 3, 3]) == 3
    assert module_0.search([4, 4, 4, 4]) == 4
    assert module_0.search([5, 5, 5, 5, 5]) == 5

    # Frequency below value
    assert module_0.search([3, 3]) == -1
    assert module_0.search([4, 4, 4]) == -1

    # Multiple values qualify -> return greatest
    assert module_0.search([1, 2, 2]) == 2
    assert module_0.search([1, 1, 2, 2, 2]) == 2
    assert module_0.search([1, 2, 2, 3, 3, 3]) == 3

    # Only 1 qualifies
    assert module_0.search([1, 1, 1]) == 1
    assert module_0.search([1, 2, 3]) == 1

    # No value qualifies
    assert module_0.search([5]) == -1
    assert module_0.search([2, 3, 3]) == -1

# Generated at 2026-10-24 12:58:31.568914
# Unit test for function search
def test_search():
    # Examples from docstring
    assert module_0.search([4, 1, 2, 2, 3, 1]) == 2
    assert module_0.search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
    assert module_0.search([5, 5, 4, 4, 4]) == -1

    # Single element
    assert module_0.search([1]) == 1
    assert module_0.search([2]) == -1

    # Exact frequency match
    assert module_0.search([2, 2]) == 2
    assert module_0.search([3, 3, 3]) == 3
    assert module_0.search([4, 4, 4, 4]) == 4
    assert module_0.search([5, 5, 5, 5, 5]) == 5

    # Frequency below value
    assert module_0.search([3, 3]) == -1
    assert module_0.search([4, 4, 4]) == -1

    # Multiple values qualify -> return greatest
    assert module_0.search([1, 2, 2]) == 2
    assert module_0.search([1, 1, 2, 2, 2]) == 2
    assert module_0.search([1, 2, 2, 3, 3, 3]) == 3

    # Only 1 qualifies
    assert module_0.search([1, 1, 1]) == 1
    assert module_0.search([1, 2, 3]) == 1

    # No value qualifies
    assert module_0.search([5]) == -1
    assert module_0.search([2, 3, 3]) == -1

# Generated at 2026-10-24 12:58:32.959139
# Unit test for function search
def test_search():
    # Examples from docstring
    assert module_0.search([4, 1, 2, 2, 3, 1]) == 2
    assert module_0.search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
    assert module_0.search([5, 5, 4, 4, 4]) == -1

    # Single element
    assert module_0.search([1]) == 1
    assert module_0.search([2]) == -1

    # Exact frequency match
    assert module_0.search([2, 2]) == 2
    assert module_0.search([3, 3, 3]) == 3
    assert module_0.search([4, 4, 4, 4]) == 4
    assert module_0.search([5, 5, 5, 5, 5]) == 5

    # Frequency below value
    assert module_0.search([3, 3]) == -1
    assert module_0.search([4, 4, 4]) == -1

    # Multiple values qualify -> return greatest
    assert module_0.search([1, 2, 2]) == 2
    assert module_0.search([1, 1, 2, 2, 2]) == 2
    assert module_0.search([1, 2, 2, 3, 3, 3]) == 3

    # Only 1 qualifies
    assert module_0.search([1, 1, 1]) == 1
    assert module_0.search([1, 2, 3]) == 1

    # No value qualifies
    assert module_0.search([5]) == -1
    assert module_0.search([2, 3, 3]) == -1

# Generated at 2026-10-24 12:58:34.492678
# Unit test for function search
def test_search():
    # Examples from docstring
    assert module_0.search([4, 1, 2, 2, 3, 1]) == 2
    assert module_0.search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
    assert module_0.search([5, 5, 4, 4, 4]) == -1

    # Single element
    assert module_0.search([1]) == 1
    assert module_0.search([2]) == -1

    # Exact frequency match
    assert module_0.search([2, 2]) == 2
    assert module_0.search([3, 3, 3]) == 3
    assert module_0.search([4, 4, 4, 4]) == 4
    assert module_0.search([5, 5, 5, 5, 5]) == 5

    # Frequency below value
    assert module_0.search([3, 3]) == -1
    assert module_0.search([4, 4, 4]) == -1

    # Multiple values qualify -> return greatest
    assert module_0.search([1, 2, 2]) == 2
    assert module_0.search([1, 1, 2, 2, 2]) == 2
    assert module_0.search([1, 2, 2, 3, 3, 3]) == 3

    # Only 1 qualifies
    assert module_0.search([1, 1, 1]) == 1
    assert module_0.search([1, 2, 3]) == 1

    # No value qualifies
    assert module_0.search([5]) == -1
    assert module_0.search([2, 3, 3]) == -1