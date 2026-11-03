

# Generated at 2026-11-01 21:41:13.254959
# Unit test for function search
def test_search():
    # Docstring examples
    assert module_0.search([4, 1, 2, 2, 3, 1]) == 2
    assert module_0.search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
    assert module_0.search([5, 5, 4, 4, 4]) == -1

    # Single element lists
    assert module_0.search([1]) == 1
    assert module_0.search([2]) == -1

    # Value exactly meeting its frequency threshold
    assert module_0.search([3, 3, 3]) == 3
    assert module_0.search([6, 6, 6, 6, 6, 6]) == 6
    assert module_0.search([5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 5

    # Multiple qualifying values — must return the greatest
    assert module_0.search([2, 2, 3, 3, 3]) == 3
    assert module_0.search([1, 1, 1, 2, 2, 2]) == 2
    assert module_0.search([1, 1, 2, 2, 3, 3, 3, 4, 4]) == 3

    # Only 1 qualifies (frequency of 1 is always >= 1)
    assert module_0.search([1, 2, 3]) == 1
    assert module_0.search([2, 3, 4, 5]) == -1

    # Frequency exceeds value
    assert module_0.search([1, 1, 1, 1]) == 1

    # No qualifying value
    assert module_0.search([10, 10, 10]) == -1
    assert module_0.search([2, 2, 3, 3]) == -1

    print("All tests passed!")


if __name__ == "__main__":
    test_search()

# Generated at 2026-11-01 21:42:02.304690
# Unit test for function search
def test_search():
    # Provided examples
    assert module_0.search([4, 1, 2, 2, 3, 1]) == 2
    assert module_0.search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
    assert module_0.search([5, 5, 4, 4, 4]) == -1

    # Single element list - frequency 1 >= 1
    assert module_0.search([1]) == 1
    # Single element list - frequency 1 < 2
    assert module_0.search([2]) == -1

    # All same elements meeting condition
    assert module_0.search([3, 3, 3]) == 3
    assert module_0.search([2, 2]) == 2

    # Frequency exactly equal to value
    assert module_0.search([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == 4

    # Greatest qualifying value wins over smaller ones
    assert module_0.search([1, 1, 1, 2, 2, 2, 3, 3, 3]) == 3

    # Value with high frequency but condition fails for larger values
    assert module_0.search([10, 10, 10, 10, 10]) == -1
    assert module_0.search([6, 6, 6, 6, 6, 6]) == 6

    # Mixed case where only small value qualifies
    assert module_0.search([7, 1, 7, 1, 7, 1]) == 1

    # Duplicates of qualifying value scattered
    assert module_0.search([2, 1, 2, 1, 2]) == 2

    # Only 1s always qualify (frequency >= 1)
    assert module_0.search([9, 8, 1]) == 1

    print("All tests passed!")


if __name__ == "__main__":
    test_search()

# Generated at 2026-11-01 21:42:27.842779
# Unit test for function search
def test_search():
    # Provided examples
    assert module_0.search([4, 1, 2, 2, 3, 1]) == 2
    assert module_0.search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
    assert module_0.search([5, 5, 4, 4, 4]) == -1

    # Single-element lists
    assert module_0.search([1]) == 1           # frequency of 1 is 1 >= 1
    assert module_0.search([2]) == -1          # frequency of 2 is 1 < 2
    assert module_0.search([5]) == -1

    # All identical elements
    assert module_0.search([3, 3, 3]) == 3     # frequency 3 >= 3
    assert module_0.search([3, 3]) == -1       # frequency 2 < 3

    # Frequency exactly equal to value
    assert module_0.search([2, 2]) == 2
    assert module_0.search([1, 1, 1, 1]) == 1

    # Greatest qualifying value should win when several qualify
    assert module_0.search([1, 2, 2, 3, 3, 3]) == 3
    assert module_0.search([3, 3, 3, 2, 2, 1]) == 3   # order independence

    # Large value appearing enough times
    assert module_0.search([10] * 10 + [5] * 5) == 10

    # Only a small value qualifies
    assert module_0.search([6, 6, 6, 6, 6, 1]) == 1   # 6 appears 5 times (< 6), 1 appears once

    # No qualifying value at all
    assert module_0.search([7, 7, 7, 8, 8, 9]) == -1

# Generated at 2026-11-01 21:43:12.144457
# Unit test for function search
def test_search():
    # Docstring examples
    assert module_0.search([4, 1, 2, 2, 3, 1]) == 2
    assert module_0.search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
    assert module_0.search([5, 5, 4, 4, 4]) == -1

    # Single-element lists
    assert module_0.search([1]) == 1
    assert module_0.search([2]) == -1
    assert module_0.search([100]) == -1

    # All identical elements
    assert module_0.search([3, 3, 3]) == 3
    assert module_0.search([2, 2]) == 2
    assert module_0.search([4, 4, 4, 4]) == 4
    assert module_0.search([5, 5, 5]) == -1
    assert module_0.search([6, 6, 6, 6, 6, 6]) == 6
    assert module_0.search([6, 6, 6, 6, 6]) == -1

    # Frequency exactly equals value
    assert module_0.search([1, 2, 2]) == 2

    # Greatest qualifying value wins
    assert module_0.search([1, 1, 2, 2, 3, 3, 3]) == 3
    assert module_0.search([2, 2, 3, 3, 3, 4, 4, 4, 4]) == 4
    assert module_0.search([1, 1, 1, 2]) == 1
    assert module_0.search([1, 3, 3, 3, 2, 2]) == 3

    # Unordered input
    assert module_0.search([3, 1, 2, 3, 1, 3, 2]) == 3
    assert module_0.search([2, 2, 1, 3]) == 2

    # Larger values
    assert module_0.search([10] * 10) == 10
    assert module_0.search([10] * 9) == -1
    assert module_0.search([5, 5, 5, 5, 5, 3, 3, 3, 2, 2, 4]) == 5

    # Only small values qualify
    assert module_0.search([7, 7, 7, 8, 8]) == -1
    assert module_0.search([1, 9, 9, 9]) == 1

# Generated at 2026-11-01 21:43:26.787964
# Unit test for function search
def test_search():
    # Test cases from docstring
    assert module_0.search([4, 1, 2, 2, 3, 1]) == 2
    assert module_0.search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
    assert module_0.search([5, 5, 4, 4, 4]) == -1

    # Single element lists
    assert module_0.search([1]) == 1
    assert module_0.search([2]) == -1

    # All elements the same
    assert module_0.search([5, 5, 5, 5, 5]) == 5
    assert module_0.search([3, 3, 3]) == 3
    assert module_0.search([10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 10

    # Multiple qualifying values, return the greatest
    assert module_0.search([2, 2, 3, 3, 3]) == 3
    assert module_0.search([1, 1, 1, 2, 2]) == 2
    assert module_0.search([1, 2, 2, 3, 3, 3, 4, 4]) == 3

    # Only 1 qualifies (frequency of 1 is always >= 1)
    assert module_0.search([1, 5, 5]) == 1
    assert module_0.search([1, 7, 7, 7, 7, 7, 7, 7]) == 1

    # No value qualifies
    assert module_0.search([6, 6, 6, 6, 6]) == -1
    assert module_0.search([3, 3]) == -1

    # Unsorted input
    assert module_0.search([3, 1, 2, 3, 3, 2, 1, 1]) == 3

    # Larger frequency than value
    assert module_0.search([4, 4, 4, 4, 4, 4, 1, 2]) == 4

    print("All test cases passed!")


if __name__ == "__main__":
    test_search()