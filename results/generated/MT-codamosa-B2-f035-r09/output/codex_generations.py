

# Generated at 2026-11-02 15:51:34.512159
# Unit test for function max_element
def test_max_element():
    assert module_0.max_element([1, 2, 3]) == 3
    assert module_0.max_element([5, 3, -5, 2, -3, 3, 9, 0, 124, 1, -10]) == 124
    assert module_0.max_element([-1, -2, -3]) == -1
    assert module_0.max_element([42]) == 42
    assert module_0.max_element([0, 0, 0]) == 0
    assert module_0.max_element([3.5, 2.1, 9.8]) == 9.8
    assert module_0.max_element([7, 7, 7]) == 7
    assert module_0.max_element([-5, -1, -10, 0]) == 0
    assert module_0.max_element([100, 99, 98]) == 100
    assert module_0.max_element([1, 100, 1]) == 100
    # Test with max at various positions
    assert module_0.max_element([10, 2, 3]) == 10       # max first
    assert module_0.max_element([1, 10, 3]) == 10       # max middle
    assert module_0.max_element([1, 2, 10]) == 10       # max last
    # Test with mixed positive/negative floats
    assert module_0.max_element([-1.5, -0.5, -2.5]) == -0.5


if __name__ == "__main__":
    test_max_element()
    print("All tests passed!")

# Generated at 2026-11-02 15:53:23.166681
# Unit test for function max_element
def test_max_element():
    # Basic positive numbers
    assert module_0.max_element([1, 2, 3]) == 3
    assert module_0.max_element([5, 3, -5, 2, -3, 3, 9, 0, 124]) == 124

    # Max at the beginning
    assert module_0.max_element([10, 2, 3, 4]) == 10

    # Max in the middle
    assert module_0.max_element([1, 50, 3, 4]) == 50

    # All elements equal
    assert module_0.max_element([7, 7, 7, 7]) == 7

    # Negative numbers only
    assert module_0.max_element([-10, -5, -20, -1]) == -1
    assert module_0.max_element([-3]) == -3

    # Single element list
    assert module_0.max_element([42]) == 42

    # Mixed positive and negative
    assert module_0.max_element([-100, 0, 100]) == 100

    # Floats
    assert module_0.max_element([1.5, 2.7, 0.3]) == 2.7
    assert module_0.max_element([-1.5, -2.7, -0.3]) == -0.3

    # Duplicates of max value
    assert module_0.max_element([3, 9, 9, 2]) == 9

    # Descending order
    assert module_0.max_element([9, 7, 5, 3, 1]) == 9

    # Ascending order
    assert module_0.max_element([1, 3, 5, 7, 9]) == 9

    # Strings (lexicographic comparison)
    assert module_0.max_element(["apple", "banana", "cherry"]) == "cherry"

    # Booleans mixed with integers
    assert module_0.max_element([False, True, 0, 1]) == True

    # Large numbers
    assert module_0.max_element([10**18, 10**18 - 1]) == 10**18

# Generated at 2026-11-02 15:55:33.846906
# Unit test for function max_element
def test_max_element():
    # Basic cases
    assert module_0.max_element([1, 2, 3]) == 3
    assert module_0.max_element([5, 3, -5, 2, -3, 3, 9, 0, 124]) == 124
    assert module_0.max_element([-1, -2, -3]) == -1

    # Single element and duplicates
    assert module_0.max_element([7]) == 7
    assert module_0.max_element([4, 4, 4]) == 4

    # Max at the beginning
    assert module_0.max_element([100, 1, 2]) == 100

    # Floats and mixed types
    assert module_0.max_element([1.5, 2.5, 0.5]) == 2.5
    assert module_0.max_element([1, 2.5, 2]) == 2.5

# Generated at 2026-11-02 15:57:23.857134
# Unit test for function max_element
def test_max_element():
    assert module_0.max_element([1, 2, 3]) == 3
    assert module_0.max_element([5, 3, -5, 2, -3, 3, 9, 0, 124]) == 124
    assert module_0.max_element([-1, -2, -3]) == -1
    assert module_0.max_element([42]) == 42
    assert module_0.max_element([0, 0, 0]) == 0
    assert module_0.max_element([7, 7, 3, 7]) == 7
    assert module_0.max_element([1.5, 2.5, 0.5]) == 2.5
    assert module_0.max_element([-10, -20, -5, -30]) == -5
    assert module_0.max_element(list(range(100))) == 99
    assert module_0.max_element([100, 1, 2, 3, 4]) == 100


def test_max_element_single_element():
    assert module_0.max_element([5]) == 5


def test_max_element_negative_numbers():
    assert module_0.max_element([-1, -5, -3]) == -1


def test_max_element_mixed():
    assert module_0.max_element([-5, 0, 5]) == 5


def test_max_element_duplicates():
    assert module_0.max_element([3, 3, 3, 3]) == 3


def test_max_element_floats():
    assert module_0.max_element([1.1, 2.2, 3.3]) == 3.3

# Generated at 2026-11-02 15:58:46.703359
# Unit test for function max_element
def test_max_element():
    # Basic positive integers
    assert module_0.max_element([1, 2, 3]) == 3
    assert module_0.max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123

    # Max element at the beginning
    assert module_0.max_element([100, 2, 3, 4]) == 100

    # Max element at the end
    assert module_0.max_element([1, 2, 3, 100]) == 100

    # All negative numbers
    assert module_0.max_element([-5, -2, -10, -1]) == -1

    # Single element list
    assert module_0.max_element([42]) == 42

    # All elements equal
    assert module_0.max_element([7, 7, 7, 7]) == 7

    # Duplicates of the max
    assert module_0.max_element([1, 9, 3, 9, 2]) == 9

    # Floats
    assert module_0.max_element([1.5, 2.7, 0.3]) == 2.7

    # Mixed ints and floats
    assert module_0.max_element([1, 2.5, 2]) == 2.5

    # Zero present
    assert module_0.max_element([-3, 0, -1]) == 0

    # Large numbers
    assert module_0.max_element([10**6, 10**9, 10**3]) == 10**9

    print("All tests passed!")


test_max_element()