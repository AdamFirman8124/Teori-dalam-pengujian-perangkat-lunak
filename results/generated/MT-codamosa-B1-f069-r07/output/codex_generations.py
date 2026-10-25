

# Generated at 2026-10-24 13:33:06.474748
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

# Generated at 2026-10-24 13:33:22.960058
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

# Generated at 2026-10-24 13:33:24.279089
# Unit test for function search
def test_search():
    # Provided examples
    assert module_0.search([4, 1, 2, 2, 3, 1]) == 2
    assert module_0.search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
    assert module_0.search([5, 5, 4, 4, 4]) == -1

    # Single element
    assert module_0.search([1]) == 1
    assert module_0.search([2]) == -1

    # Value exactly equals its frequency
    assert module_0.search([3, 3, 3]) == 3

    # Frequency exceeds value â still qualifies
    assert module_0.search([2, 2, 2]) == 2

    # Larger value qualifies even when smaller ones do too (greatest wins)
    assert module_0.search([1, 1, 2, 2, 3, 3, 3]) == 3

    # Only 1 qualifies
    assert module_0.search([1, 5, 5, 5, 5]) == 1

    # No qualifying value
    assert module_0.search([2, 2, 4, 4, 4]) == -1

    # Unsorted input
    assert module_0.search([3, 1, 3, 2, 3, 2]) == 3

    print("All tests passed!")


test_search()

# Generated at 2026-10-24 13:33:26.700141
# Unit test for function search

# Generated at 2026-10-24 13:33:29.117489
# Unit test for function search

# Generated at 2026-10-24 13:33:31.537162
# Unit test for function search

# Generated at 2026-10-24 13:33:33.956696
# Unit test for function search

# Generated at 2026-10-24 13:33:36.519718
# Unit test for function search

# Generated at 2026-10-24 13:33:39.031397
# Unit test for function search