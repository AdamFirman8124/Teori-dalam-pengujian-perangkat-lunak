

# Generated at 2026-10-25 02:21:54.617817
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

    # Return the greatest qualifying integer
    assert module_0.search([1, 1, 2, 2, 3, 3, 3]) == 3

    # No integer occurs often enough
    assert module_0.search([2, 3, 4, 5]) == -1

# Generated at 2026-10-25 02:21:57.148085
# Unit test for function search

# Generated at 2026-10-25 02:21:59.560770
# Unit test for function search

# Generated at 2026-10-25 02:22:01.980415
# Unit test for function search

# Generated at 2026-10-25 02:22:10.997243
# Unit test for function search
def test_search():assert module_0.search([4, 1, 2, 2, 3, 1]) == 2

# Generated at 2026-10-25 02:22:17.040177
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

    # Return the greatest qualifying integer
    assert module_0.search([1, 1, 2, 2, 3, 3, 3]) == 3

    # Frequencies may exceed their corresponding values
    assert module_0.search([1, 2, 2, 2, 2]) == 2

    # No integer occurs often enough
    assert module_0.search([3, 4, 5, 6]) == -1

# Generated at 2026-10-25 02:22:23.860524
# Unit test for function search
def test_search():
    # Examples from the docstring
    assert module_0.search([4, 1, 2, 2, 3, 1]) == 2
    assert module_0.search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
    assert module_0.search([5, 5, 4, 4, 4]) == -1

    # Edge and additional cases
    assert module_0.search([1]) == 1
    assert module_0.search([2]) == -1
    assert module_0.search([1, 1, 1]) == 1
    assert module_0.search([2, 2]) == 2
    assert module_0.search([2, 2, 3, 3, 3]) == 3
    assert module_0.search([1, 2, 3]) == 1
    assert module_0.search([4, 4, 4, 4, 3, 3, 3]) == 4