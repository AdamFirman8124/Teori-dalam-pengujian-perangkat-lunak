

# Generated at 2026-11-03 04:41:03.798858
# Unit test for function search
def test_search():
    # Provided examples
    assert module_0.search([4, 1, 2, 2, 3, 1]) == 2
    assert module_0.search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
    assert module_0.search([5, 5, 4, 4, 4]) == -1

    # No qualifying value
    assert module_0.search([2]) == -1
    assert module_0.search([10, 9, 8]) == -1

    # Single element that qualifies
    assert module_0.search([1]) == 1

    # Value 1 always qualifies if present
    assert module_0.search([1, 5, 5, 5, 5, 5]) == 1
    assert module_0.search([1, 1]) == 1

    # Greatest qualifying value should be returned
    assert module_0.search([3, 3, 3, 2, 2]) == 3
    assert module_0.search([2, 2, 2, 1, 1]) == 2
    assert module_0.search([5, 5, 5, 5, 5, 1, 2, 2, 3, 3, 3]) == 5

    # Exactly meets frequency requirement (frequency == value)
    assert module_0.search([4, 4, 4, 4]) == 4

    # Frequency just below value does not qualify
    assert module_0.search([3, 3]) == -1

    # Mixed case where larger value disqualifies but smaller qualifies
    assert module_0.search([6, 6, 6, 6, 6, 6, 2, 2, 2]) == 2

    # Larger input
    assert module_0.search([1] * 10 + [7] * 7 + [3] * 2) == 7

# Generated at 2026-11-03 04:42:55.778510
# Unit test for function search
def test_search():
    # Provided examples
    assert module_0.search([4, 1, 2, 2, 3, 1]) == 2
    assert module_0.search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
    assert module_0.search([5, 5, 4, 4, 4]) == -1

    # Single element lists
    assert module_0.search([1]) == 1
    assert module_0.search([2]) == -1
    assert module_0.search([10]) == -1

    # All same values, frequency exactly equals value
    assert module_0.search([3, 3, 3]) == 3
    assert module_0.search([5, 5, 5, 5, 5]) == 5
    assert module_0.search([6, 6, 6, 6, 6, 6]) == 6
    assert module_0.search([7, 7, 7, 7, 7, 7, 7]) == 7

    # Frequency exceeds value
    assert module_0.search([2, 2, 2]) == 2
    assert module_0.search([1, 1]) == 1
    assert module_0.search([1, 1, 2, 2, 2]) == 2

    # No qualifying value
    assert module_0.search([1, 2, 3]) == 1  # 1 appears once, qualifies
    assert module_0.search([2, 3, 4]) == -1
    assert module_0.search([4, 4, 4, 4, 3, 3, 3]) == 4

    # Greatest qualifying value wins over smaller ones
    assert module_0.search([1, 1, 1, 2, 2, 2, 3, 3]) == 2
    assert module_0.search([1, 2, 2, 3, 3, 3, 5, 5, 5, 5, 5]) == 5

    # Value with high frequency but small magnitude still loses to larger qualifying value
    assert module_0.search([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 1]) == 10

    # Frequency less than value for all candidates
    assert module_0.search([8, 8, 8, 1, 1, 1, 1]) == 1

    print("All tests passed!")


if __name__ == "__main__":
    test_search()

# Generated at 2026-11-03 04:47:23.712753
# Unit test for function search
def test_search():
    # Provided examples
    assert module_0.search([4, 1, 2, 2, 3, 1]) == 2
    assert module_0.search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
    assert module_0.search([5, 5, 4, 4, 4]) == -1

    # Single element cases
    assert module_0.search([1]) == 1
    assert module_0.search([2]) == -1
    assert module_0.search([5]) == -1

    # Exact frequency matches
    assert module_0.search([2, 2]) == 2
    assert module_0.search([3, 3, 3]) == 3
    assert module_0.search([1, 1, 1]) == 1

    # Frequency greater than value
    assert module_0.search([1, 2, 2, 2]) == 2
    assert module_0.search([1, 1, 2, 3, 3, 3, 3]) == 3

    # Multiple candidates: greatest should be returned
    assert module_0.search([1, 1, 1, 2, 2]) == 2
    assert module_0.search([1, 2, 2, 3, 3, 3, 3]) == 3

    # No valid value
    assert module_0.search([4, 4, 4]) == -1
    assert module_0.search([3, 3, 4, 4, 5]) == -1

    # Larger list
    assert module_0.search([1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == 4

    # Value appears fewer times than itself
    assert module_0.search([1, 1, 5, 5, 5, 5]) == 1

    # Mixed with larger invalid values
    assert module_0.search([2, 2, 2, 6, 6]) == 2