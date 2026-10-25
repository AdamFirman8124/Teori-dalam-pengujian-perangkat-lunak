

# Generated at 2026-10-25 01:08:03.944426
# Unit test for function search

# Generated at 2026-10-25 01:08:06.355871
# Unit test for function search

# Generated at 2026-10-25 01:08:08.773148
# Unit test for function search

# Generated at 2026-10-25 01:08:11.188968
# Unit test for function search

# Generated at 2026-10-25 01:08:13.603896
# Unit test for function search

# Generated at 2026-10-25 01:08:16.024231
# Unit test for function search

# Generated at 2026-10-25 01:08:18.450758
# Unit test for function search

# Generated at 2026-10-25 01:08:20.865323
# Unit test for function search

# Generated at 2026-10-25 01:08:23.279740
# Unit test for function search

# Generated at 2026-10-25 01:08:30.367649
# Unit test for function search
def test_search():
    assert module_0.search([4, 1, 2, 2, 3, 1]) == 2
    assert module_0.search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
    assert module_0.search([5, 5, 4, 4, 4]) == -1

    # Edge and additional cases
    assert module_0.search([1]) == 1
    assert module_0.search([2]) == -1
    assert module_0.search([2, 2]) == 2
    assert module_0.search([1, 1, 2]) == 1
    assert module_0.search([1, 1, 2, 2]) == 2
    assert module_0.search([3, 3, 3, 2, 2, 1]) == 3

# Generated at 2026-10-25 01:08:38.264063
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

    # No integer has sufficient frequency
    assert module_0.search([3, 3, 4, 4, 4]) == -1