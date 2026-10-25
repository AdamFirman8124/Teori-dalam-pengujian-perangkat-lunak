

# Generated at 2026-10-24 07:59:25.686603
# Unit test for function search
def test_search():
    # Examples from the docstring
    assert module_0.search([4, 1, 2, 2, 3, 1]) == 2
    assert module_0.search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
    assert module_0.search([5, 5, 4, 4, 4]) == -1

    # Edge cases
    assert module_0.search([1]) == 1
    assert module_0.search([2]) == -1
    assert module_0.search([1, 1, 1]) == 1

    # Return the greatest qualifying integer
    assert module_0.search([1, 2, 2, 3, 3, 3]) == 3

    # Frequency may be greater than the integer
    assert module_0.search([2, 2, 2, 2]) == 2

    # No qualifying integer
    assert module_0.search([3, 3, 4, 4, 4]) == -1

# Generated at 2026-10-24 07:59:30.735749
# Unit test for function search
def test_search():
    assert module_0.search([4, 1, 2, 2, 3, 1]) == 2
    assert module_0.search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
    assert module_0.search([5, 5, 4, 4, 4]) == -1

    # Edge cases
    assert module_0.search([1]) == 1
    assert module_0.search([2]) == -1
    assert module_0.search([2, 2]) == 2
    assert module_0.search([1, 1, 2, 2, 3, 3, 3]) == 3
    assert module_0.search([10, 10, 10]) == -1

# Generated at 2026-10-24 07:59:36.812645
# Unit test for function search
def test_search():
    # Provided examples
    assert module_0.search([4, 1, 2, 2, 3, 1]) == 2
    assert module_0.search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
    assert module_0.search([5, 5, 4, 4, 4]) == -1

    # Edge cases
    assert module_0.search([1]) == 1
    assert module_0.search([2]) == -1
    assert module_0.search([2, 2]) == 2

    # Return the greatest qualifying integer
    assert module_0.search([1, 2, 2, 3, 3, 3]) == 3

    # Frequency may be greater than the integer
    assert module_0.search([2, 2, 2, 2]) == 2

# Generated at 2026-10-24 07:59:43.023507
# Unit test for function search
def test_search():
    assert module_0.search([4, 1, 2, 2, 3, 1]) == 2
    assert module_0.search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
    assert module_0.search([5, 5, 4, 4, 4]) == -1

    # Edge cases
    assert module_0.search([1]) == 1
    assert module_0.search([2]) == -1
    assert module_0.search([2, 2]) == 2
    assert module_0.search([1, 1, 2, 2]) == 2
    assert module_0.search([3, 3, 3, 2, 2, 1]) == 3
    assert module_0.search([10, 10, 10]) == -1

# Generated at 2026-10-24 07:59:49.371981
# Unit test for function search
def test_search():
    # Examples from the docstring
    assert module_0.search([4, 1, 2, 2, 3, 1]) == 2
    assert module_0.search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
    assert module_0.search([5, 5, 4, 4, 4]) == -1

    # Edge cases
    assert module_0.search([1]) == 1
    assert module_0.search([2]) == -1
    assert module_0.search([2, 2]) == 2
    assert module_0.search([1, 1, 1]) == 1

    # Return the greatest qualifying integer
    assert module_0.search([1, 2, 2, 3, 3, 3]) == 3

    # No integer occurs often enough
    assert module_0.search([2, 3, 4, 5]) == -1