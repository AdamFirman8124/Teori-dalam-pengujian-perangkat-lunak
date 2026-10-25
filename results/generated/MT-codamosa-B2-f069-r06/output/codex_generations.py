

# Generated at 2026-10-24 19:41:56.249270
# Unit test for function search
def test_search():
    # Provided examples
    assert module_0.search([4, 1, 2, 2, 3, 1]) == 2
    assert module_0.search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
    assert module_0.search([5, 5, 4, 4, 4]) == -1

    # Single element
    assert module_0.search([1]) == 1
    assert module_0.search([2]) == -1

    # Value appears exactly as many times as itself (boundary: frq[i] == i)
    assert module_0.search([3, 3, 3]) == 3

    # Ties: pick the greatest qualifying value
    assert module_0.search([2, 2, 3, 3, 3]) == 3

    # Largest qualifying value is not the max of the list
    assert module_0.search([2, 2, 2, 10]) == 2

    # No qualifying value
    assert module_0.search([5, 4, 4]) == -1

    print("All tests passed!")

# Generated at 2026-10-24 19:41:58.775245
# Unit test for function search

# Generated at 2026-10-24 19:42:01.291592
# Unit test for function search

# Generated at 2026-10-24 19:42:03.711794
# Unit test for function search

# Generated at 2026-10-24 19:42:06.127494
# Unit test for function search

# Generated at 2026-10-24 19:42:08.543505
# Unit test for function search

# Generated at 2026-10-24 19:42:10.960937
# Unit test for function search

# Generated at 2026-10-24 19:42:13.379265
# Unit test for function search

# Generated at 2026-10-24 19:42:15.795165
# Unit test for function search

# Generated at 2026-10-24 19:42:18.211699
# Unit test for function search

# Generated at 2026-10-24 19:42:20.631835
# Unit test for function search

# Generated at 2026-10-24 19:42:23.048286
# Unit test for function search

# Generated at 2026-10-24 19:42:25.462922
# Unit test for function search