

# Generated at 2026-11-02 23:28:36.562023
# Unit test for function max_element
def test_max_element():
    # nonce:02916f3a
    # Basic positive numbers
    assert module_0.max_element([1, 2, 3]) == 3
    assert module_0.max_element([5, 3, -5, 2, -3, 3, 9, 0, 124]) == 124

    # Already sorted / reverse sorted
    assert module_0.max_element([1, 2, 3, 4, 5]) == 5
    assert module_0.max_element([5, 4, 3, 2, 1]) == 5

    # All negative numbers
    assert module_0.max_element([-1, -2, -3]) == -1
    assert module_0.max_element([-10, -5, -20]) == -5

    # Single element
    assert module_0.max_element([42]) == 42

    # Duplicates
    assert module_0.max_element([7, 7, 7]) == 7
    assert module_0.max_element([3, 3, 5, 5, 1]) == 5

    # Mixed positives, negatives, and zero
    assert module_0.max_element([0, -1, 1]) == 1
    assert module_0.max_element([-100, 0, 100, -50]) == 100

    # Floats
    assert module_0.max_element([1.5, 2.7, 0.3]) == 2.7
    assert module_0.max_element([-1.5, -2.7, -0.3]) == -0.3

    # Max at various positions
    assert module_0.max_element([9, 1, 2, 3]) == 9      # max first
    assert module_0.max_element([1, 2, 3, 9]) == 9      # max last
    assert module_0.max_element([1, 9, 2, 3]) == 9      # max middle

# Generated at 2026-11-02 23:29:43.096093
# Unit test for function max_element
def test_max_element():
    # Basic case with positive integers
    assert module_0.max_element([1, 2, 3]) == 3
    
    # Max at the beginning
    assert module_0.max_element([10, 2, 3]) == 10
    
    # Max at the end
    assert module_0.max_element([1, 2, 10]) == 10
    
    # All negative numbers
    assert module_0.max_element([-1, -2, -3]) == -1
    
    # Mixed positive and negative
    assert module_0.max_element([-5, 3, -2, 8]) == 8
    
    # Single element list
    assert module_0.max_element([42]) == 42
    
    # List with duplicates
    assert module_0.max_element([5, 5, 5]) == 5
    
    # Duplicates with a larger element
    assert module_0.max_element([1, 7, 7, 2]) == 7
    
    # Floats
    assert module_0.max_element([1.5, 2.7, 0.3]) == 2.7
    
    # Already sorted ascending
    assert module_0.max_element([1, 2, 3, 4, 5]) == 5
    
    # Sorted descending
    assert module_0.max_element([5, 4, 3, 2, 1]) == 5
    
    # Zero included
    assert module_0.max_element([0, -1, -2]) == 0
    
    # Mixed ints and floats
    assert module_0.max_element([1, 2.5, 2]) == 2.5

# Generated at 2026-11-02 23:30:41.298579
# Unit test for function max_element
def test_max_element():
    # Basic positive numbers
    assert module_0.max_element([1, 2, 3]) == 3
    assert module_0.max_element([3, 2, 1]) == 3
    assert module_0.max_element([2, 3, 1]) == 3

    # Max at different positions
    assert module_0.max_element([5, 1, 2, 3]) == 5
    assert module_0.max_element([1, 2, 3, 5]) == 5
    assert module_0.max_element([1, 5, 2, 3]) == 5

    # Negative numbers
    assert module_0.max_element([-1, -2, -3]) == -1
    assert module_0.max_element([-3, -2, -1]) == -1
    assert module_0.max_element([-5, -1, -3]) == -1

    # Mixed positive and negative
    assert module_0.max_element([-10, 4, 6, 1000, 10, 20]) == 1000
    assert module_0.max_element([5, -3, 2, -8, 0]) == 5

    # Single element
    assert module_0.max_element([42]) == 42
    assert module_0.max_element([-42]) == -42

    # Duplicates
    assert module_0.max_element([7, 7, 7, 7]) == 7
    assert module_0.max_element([1, 3, 3, 2]) == 3

    # Floats
    assert module_0.max_element([1.5, 2.7, 0.3]) == 2.7
    assert module_0.max_element([-1.5, -2.7, -0.3]) == -0.3

    # Two elements
    assert module_0.max_element([1, 2]) == 2
    assert module_0.max_element([2, 1]) == 2

    print("All test_max_element tests passed!")


if __name__ == "__main__":
    test_max_element()

# Generated at 2026-11-02 23:31:42.489466
# Unit test for function max_element
def test_max_element():
    # Basic cases
    assert module_0.max_element([1, 2, 3]) == 3
    assert module_0.max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123

    # Max at beginning, middle, end
    assert module_0.max_element([10, 2, 3, 4]) == 10
    assert module_0.max_element([1, 50, 3, 4]) == 50
    assert module_0.max_element([1, 2, 3, 100]) == 100

    # Negative numbers
    assert module_0.max_element([-5, -3, -1, -10]) == -1
    assert module_0.max_element([-10]) == -10

    # Single element
    assert module_0.max_element([7]) == 7

    # Duplicates
    assert module_0.max_element([3, 3, 3]) == 3
    assert module_0.max_element([2, 2, 9, 2]) == 9

    # Mixed positive/negative
    assert module_0.max_element([-1, 0, 1]) == 1
    assert module_0.max_element([0, -1, -2]) == 0

    # Floats
    assert module_0.max_element([1.5, 2.7, 0.3]) == 2.7
    assert module_0.max_element([-1.5, -2.7, -0.3]) == -0.3

    # Ordered lists
    assert module_0.max_element([1, 2, 3, 4]) == 4
    assert module_0.max_element([9, 8, 7, 6]) == 9

# Generated at 2026-11-02 23:32:41.707703
# Unit test for function max_element
def test_max_element():
    # Basic case: positive numbers
    assert module_0.max_element([1, 2, 3]) == 3
    assert module_0.max_element([5, 3, -5, 2, -3, 3, 9, 0, 124]) == 124

    # Negative numbers only
    assert module_0.max_element([-1, -2, -3]) == -1
    assert module_0.max_element([-5, -3, -8]) == -3

    # Single element
    assert module_0.max_element([42]) == 42
    assert module_0.max_element([0]) == 0

    # Max at the beginning
    assert module_0.max_element([100, 2, 3, 4]) == 100

    # Max at the end
    assert module_0.max_element([1, 2, 3, 100]) == 100

    # Duplicates of the max value
    assert module_0.max_element([7, 7, 7]) == 7
    assert module_0.max_element([3, 9, 9, 2]) == 9

    # Mixed positive and negative with zero
    assert module_0.max_element([0, -1, -2]) == 0

    # Floats
    assert module_0.max_element([1.5, 2.7, 0.3]) == 2.7

    # Compare against built-in max on random-ish data
    data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert module_0.max_element(data) == max(data)

    print("All tests passed!")