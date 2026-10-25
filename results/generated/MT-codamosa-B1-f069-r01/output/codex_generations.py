

# Generated at 2026-10-24 14:53:45.000388
# Unit test for function search

# Generated at 2026-10-24 14:53:47.412413
# Unit test for function search

# Generated at 2026-10-24 14:53:49.827677
# Unit test for function search

# Generated at 2026-10-24 14:53:52.239294
# Unit test for function search

# Generated at 2026-10-24 14:53:54.652388
# Unit test for function search

# Generated at 2026-10-24 14:53:57.069247
# Unit test for function search

# Generated at 2026-10-24 14:53:59.485202
# Unit test for function search

# Generated at 2026-10-24 14:54:01.897123
# Unit test for function search

# Generated at 2026-10-24 14:54:04.309466
# Unit test for function search

# Generated at 2026-10-24 14:54:06.721700
# Unit test for function search

# Generated at 2026-10-24 14:54:09.135458
# Unit test for function search

# Generated at 2026-10-24 14:54:11.549956
# Unit test for function search

# Generated at 2026-10-24 14:54:20.345061
# Unit test for function search
def test_search():
    # Example cases from the docstring
    assert module_0.search([4, 1, 2, 2, 3, 1]) == 2
    assert module_0.search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
    assert module_0.search([5, 5, 4, 4, 4]) == -1

    # Single element list
    assert module_0.search([1]) == 1
    assert module_0.search([2]) == -1

    # Value exactly equal to its frequency
    assert module_0.search([3, 3, 3]) == 3
    assert module_0.search([1, 1]) == 1

    # Frequency greater than value
    assert module_0.search([2, 2, 2, 2, 2]) == 2

    # Multiple qualifying values -> greatest one returned
    assert module_0.search([1, 1, 2, 2, 2, 3, 3, 3]) == 3
    assert module_0.search([1, 1, 1, 2, 2]) == 2

    # No qualifying value
    assert module_0.search([5, 4, 4]) == -1
    assert module_0.search([10, 10, 10]) == -1

    # Large values with sufficient frequency
    assert module_0.search([6] * 6) == 6
    assert module_0.search([6] * 7) == 6

    # Mixed: qualifying and non-qualifying large values
    assert module_0.search([7, 3, 3, 3, 2, 2]) == 3

    print("All tests passed!")

test_search()