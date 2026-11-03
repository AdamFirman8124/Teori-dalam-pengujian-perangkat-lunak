

# Generated at 2026-11-02 06:49:02.756818
# Unit test for function search
def test_search():
    # Examples from the docstring
    assert module_0.search([4, 1, 2, 2, 3, 1]) == 2
    assert module_0.search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
    assert module_0.search([5, 5, 4, 4, 4]) == -1

    # Single-element lists
    assert module_0.search([1]) == 1
    assert module_0.search([2]) == -1

    # All identical elements
    assert module_0.search([1, 1, 1]) == 1
    assert module_0.search([2, 2, 2]) == 2
    assert module_0.search([3, 3, 3, 3]) == 3

    # No qualifying value
    assert module_0.search([2, 3, 3]) == -1
    assert module_0.search([10]) == -1

    # Multiple qualifying values -> greatest one is returned
    assert module_0.search([1, 1, 2, 2]) == 2
    assert module_0.search([2, 2, 3, 3, 3]) == 3

    # Frequency exactly equals the value
    assert module_0.search([10] * 10) == 10

    # Frequency just below the value
    assert module_0.search([7] * 6) == -1

    # Unsorted input
    assert module_0.search([3, 1, 2, 3, 2, 3, 1]) == 3
# nonce:a22fe01e

# Generated at 2026-11-02 06:49:24.359665
# Unit test for function search
def test_search():
    # Provided examples
    assert module_0.search([4, 1, 2, 2, 3, 1]) == 2
    assert module_0.search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
    assert module_0.search([5, 5, 4, 4, 4]) == -1

    # Single element cases
    assert module_0.search([1]) == 1          # freq 1 >= 1
    assert module_0.search([5]) == -1         # freq 1 < 5

    # No qualifying value
    assert module_0.search([3, 3, 3]) == -1   # freq 3 < 3... wait, freq == 3 >= 3
    assert module_0.search([2, 2, 3]) == 2    # freq(2)=2 >= 2, freq(3)=1 < 3

    # All elements the same
    assert module_0.search([1, 1, 1]) == 1
    assert module_0.search([2, 2, 2]) == 2
    assert module_0.search([3, 3, 3, 3]) == 3  # freq 4 >= 3

    # Greatest qualifying value must be returned
    assert module_0.search([1, 1, 2, 2, 3]) == 2   # 1 and 2 qualify, 3 does not
    assert module_0.search([1, 2, 2, 3, 3, 3, 3]) == 3
    assert module_0.search([1, 1, 1, 1, 1]) == 1

    # Frequency strictly greater than value
    assert module_0.search([2, 2, 2, 5]) == 2      # freq(2)=3 >= 2, freq(5)=1 < 5
    assert module_0.search([1, 1, 4, 4, 4, 4, 4]) == 4

    # Large values not qualifying
    assert module_0.search([10, 1, 1, 1]) == 1

# Generated at 2026-11-02 06:49:49.056653
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

    # All identical elements
    assert module_0.search([2, 2]) == 2
    assert module_0.search([3, 3, 3]) == 3
    assert module_0.search([5, 5, 5, 5, 5]) == 5
    assert module_0.search([5, 5]) == -1

    # Only ones (frequency always >= 1)
    assert module_0.search([1, 1, 1, 1]) == 1

    # Multiple qualifying values -> return the greatest
    assert module_0.search([1, 2, 2, 3, 3, 3, 4, 4]) == 3

    # Frequency exactly equal to value qualifies
    assert module_0.search([6, 6, 6, 6, 6, 6]) == 6

    # Larger non-qualifying value along with smaller qualifying one
    assert module_0.search([1, 1, 1, 10, 10]) == 1
    assert module_0.search([1, 1, 1, 1, 1, 10, 10, 10, 10]) == 1

    # Mixed values where a larger value qualifies
    assert module_0.search([2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]) == 4

    # Unsorted input
    assert module_0.search([2, 1, 2, 1, 2, 3]) == 2

    # No qualifying value at all
    assert module_0.search([7, 7, 7, 3, 3, 1]) == 3

# Generated at 2026-11-02 06:50:19.578287
# Unit test for function search
def test_search():
    # Provided examples
    assert module_0.search([4, 1, 2, 2, 3, 1]) == 2
    assert module_0.search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
    assert module_0.search([5, 5, 4, 4, 4]) == -1

    # Single element list
    assert module_0.search([1]) == 1
    assert module_0.search([2]) == -1

    # Element frequency exactly equals the value
    assert module_0.search([3, 3, 3]) == 3

    # Frequency greater than value
    assert module_0.search([2, 2, 2, 2]) == 2

    # Largest qualifying value should be returned
    assert module_0.search([1, 1, 1, 2, 2, 3, 3, 3, 3]) == 3

    # No qualifying value
    assert module_0.search([10, 20, 30]) == -1

    # Repeated non-qualifying values
    assert module_0.search([7, 7, 7]) == -1

    # Mixed values with qualifying smaller ones only
    assert module_0.search([5, 1, 1]) == 1

    # Larger input
    assert module_0.search(list(range(1, 101)) * 1) == 1
    assert module_0.search([100] * 100 + [50] * 50) == 100

    print("All tests passed!")


if __name__ == "__main__":
    test_search()

# Generated at 2026-11-02 06:51:13.826737
# Unit test for function search
def test_search():
    # Provided examples
    assert module_0.search([4, 1, 2, 2, 3, 1]) == 2
    assert module_0.search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
    assert module_0.search([5, 5, 4, 4, 4]) == -1

    # Single element lists
    assert module_0.search([1]) == 1
    assert module_0.search([2]) == -1

    # No qualifying value
    assert module_0.search([10, 10, 10]) == -1
    assert module_0.search([7, 8, 9]) == -1

    # All same values that qualify
    assert module_0.search([3, 3, 3]) == 3
    assert module_0.search([5, 5, 5, 5, 5]) == 5

    # Greatest qualifying value should be returned, not smallest
    assert module_0.search([1, 1, 2, 2, 2]) == 2
    assert module_0.search([1, 2, 2, 3, 3, 3, 5, 5, 5, 5, 5]) == 5

    # Multiple qualifying values, check greatest is picked
    assert module_0.search([2, 2, 3, 3, 3, 4, 4, 4, 4]) == 4

    # Frequency exactly equal to value
    assert module_0.search([6, 6, 6, 6, 6, 6]) == 6

    # Larger list with mixed values
    assert module_0.search([1, 1, 1, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == 5

    # Value appears more times than its magnitude
    assert module_0.search([2, 2, 2, 2, 2]) == 2

    # Qualifying value lower than non-qualifying larger value
    assert module_0.search([3, 3, 3, 10, 10]) == 3