

# Generated at 2026-10-24 23:00:24.396764
# Unit test for function search
def test_search():
    # Examples from docstring
    assert module_0.search([4, 1, 2, 2, 3, 1]) == 2
    assert module_0.search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
    assert module_0.search([5, 5, 4, 4, 4]) == -1

    # Single element
    assert module_0.search([1]) == 1
    assert module_0.search([2]) == -1
    assert module_0.search([5]) == -1

    # Exact frequency match
    assert module_0.search([2, 2]) == 2
    assert module_0.search([3, 3, 3]) == 3
    assert module_0.search([4, 4, 4, 4]) == 4
    assert module_0.search([5, 5, 5, 5, 5]) == 5

    # Frequency less than value
    assert module_0.search([3, 3]) == -1
    assert module_0.search([4, 4, 4]) == -1

    # Frequency greater than value
    assert module_0.search([1, 1]) == 1
    assert module_0.search([5, 5, 5, 5, 5, 5]) == 5
    assert module_0.search([10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 10

    # Greatest qualifying value wins
    assert module_0.search([1, 1, 1, 2, 2, 2, 2]) == 2
    assert module_0.search([2, 2, 3, 3, 3]) == 3
    assert module_0.search([6, 6, 6, 6, 6, 6, 1, 1, 1, 1, 1, 1]) == 6

    # Only 1 qualifies
    assert module_0.search([1, 2, 3, 4, 5]) == 1

# Generated at 2026-10-24 23:00:25.782132
# Unit test for function search
def test_search():
    # Examples from docstring
    assert module_0.search([4, 1, 2, 2, 3, 1]) == 2
    assert module_0.search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
    assert module_0.search([5, 5, 4, 4, 4]) == -1

    # Single element
    assert module_0.search([1]) == 1
    assert module_0.search([2]) == -1
    assert module_0.search([5]) == -1

    # Exact frequency match
    assert module_0.search([2, 2]) == 2
    assert module_0.search([3, 3, 3]) == 3
    assert module_0.search([4, 4, 4, 4]) == 4
    assert module_0.search([5, 5, 5, 5, 5]) == 5

    # Frequency less than value
    assert module_0.search([3, 3]) == -1
    assert module_0.search([4, 4, 4]) == -1

    # Frequency greater than value
    assert module_0.search([1, 1]) == 1
    assert module_0.search([5, 5, 5, 5, 5, 5]) == 5
    assert module_0.search([10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 10

    # Greatest qualifying value wins
    assert module_0.search([1, 1, 1, 2, 2, 2, 2]) == 2
    assert module_0.search([2, 2, 3, 3, 3]) == 3
    assert module_0.search([6, 6, 6, 6, 6, 6, 1, 1, 1, 1, 1, 1]) == 6

    # Only 1 qualifies
    assert module_0.search([1, 2, 3, 4, 5]) == 1

# Generated at 2026-10-24 23:00:27.263579
# Unit test for function search
def test_search():
    # Examples from docstring
    assert module_0.search([4, 1, 2, 2, 3, 1]) == 2
    assert module_0.search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
    assert module_0.search([5, 5, 4, 4, 4]) == -1

    # Single element
    assert module_0.search([1]) == 1
    assert module_0.search([2]) == -1
    assert module_0.search([5]) == -1

    # Exact frequency match
    assert module_0.search([2, 2]) == 2
    assert module_0.search([3, 3, 3]) == 3
    assert module_0.search([4, 4, 4, 4]) == 4
    assert module_0.search([5, 5, 5, 5, 5]) == 5

    # Frequency less than value
    assert module_0.search([3, 3]) == -1
    assert module_0.search([4, 4, 4]) == -1

    # Frequency greater than value
    assert module_0.search([1, 1]) == 1
    assert module_0.search([5, 5, 5, 5, 5, 5]) == 5
    assert module_0.search([10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 10

    # Greatest qualifying value wins
    assert module_0.search([1, 1, 1, 2, 2, 2, 2]) == 2
    assert module_0.search([2, 2, 3, 3, 3]) == 3
    assert module_0.search([6, 6, 6, 6, 6, 6, 1, 1, 1, 1, 1, 1]) == 6

    # Only 1 qualifies
    assert module_0.search([1, 2, 3, 4, 5]) == 1

# Generated at 2026-10-24 23:00:28.696882
# Unit test for function search
def test_search():
    # Examples from docstring
    assert module_0.search([4, 1, 2, 2, 3, 1]) == 2
    assert module_0.search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
    assert module_0.search([5, 5, 4, 4, 4]) == -1

    # Single element
    assert module_0.search([1]) == 1
    assert module_0.search([2]) == -1
    assert module_0.search([5]) == -1

    # Exact frequency match
    assert module_0.search([2, 2]) == 2
    assert module_0.search([3, 3, 3]) == 3
    assert module_0.search([4, 4, 4, 4]) == 4
    assert module_0.search([5, 5, 5, 5, 5]) == 5

    # Frequency less than value
    assert module_0.search([3, 3]) == -1
    assert module_0.search([4, 4, 4]) == -1

    # Frequency greater than value
    assert module_0.search([1, 1]) == 1
    assert module_0.search([5, 5, 5, 5, 5, 5]) == 5
    assert module_0.search([10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 10

    # Greatest qualifying value wins
    assert module_0.search([1, 1, 1, 2, 2, 2, 2]) == 2
    assert module_0.search([2, 2, 3, 3, 3]) == 3
    assert module_0.search([6, 6, 6, 6, 6, 6, 1, 1, 1, 1, 1, 1]) == 6

    # Only 1 qualifies
    assert module_0.search([1, 2, 3, 4, 5]) == 1

# Generated at 2026-10-24 23:00:30.130233
# Unit test for function search
def test_search():
    # Examples from docstring
    assert module_0.search([4, 1, 2, 2, 3, 1]) == 2
    assert module_0.search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
    assert module_0.search([5, 5, 4, 4, 4]) == -1

    # Single element
    assert module_0.search([1]) == 1
    assert module_0.search([2]) == -1
    assert module_0.search([5]) == -1

    # Exact frequency match
    assert module_0.search([2, 2]) == 2
    assert module_0.search([3, 3, 3]) == 3
    assert module_0.search([4, 4, 4, 4]) == 4
    assert module_0.search([5, 5, 5, 5, 5]) == 5

    # Frequency less than value
    assert module_0.search([3, 3]) == -1
    assert module_0.search([4, 4, 4]) == -1

    # Frequency greater than value
    assert module_0.search([1, 1]) == 1
    assert module_0.search([5, 5, 5, 5, 5, 5]) == 5
    assert module_0.search([10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 10

    # Greatest qualifying value wins
    assert module_0.search([1, 1, 1, 2, 2, 2, 2]) == 2
    assert module_0.search([2, 2, 3, 3, 3]) == 3
    assert module_0.search([6, 6, 6, 6, 6, 6, 1, 1, 1, 1, 1, 1]) == 6

    # Only 1 qualifies
    assert module_0.search([1, 2, 3, 4, 5]) == 1