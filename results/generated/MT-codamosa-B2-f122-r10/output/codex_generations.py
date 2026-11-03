

# Generated at 2026-11-02 15:47:57.786725
# Unit test for function add_elements
def test_add_elements():
    # Typical case: only elements with at most two digits among first k are summed
    assert module_0.add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4) == 24  # 21 + 3

    # k exceeds array length: all elements considered
    assert module_0.add_elements([1, 2, 3], 10) == 6

    # No qualifying elements
    assert module_0.add_elements([100, 200, 300], 3) == 0

    # All elements qualify
    assert module_0.add_elements([1, 22, 33], 3) == 56

    # Negative single-digit numbers count (len(str(-5)) == 2)
    assert module_0.add_elements([-5, -6, 4], 3) == -7

    # Negative two-digit numbers have 3 chars, excluded
    assert module_0.add_elements([-12, 3], 2) == 3

    # k = 0 yields empty slice
    assert module_0.add_elements([1, 2, 3], 0) == 0

    # Empty array
    assert module_0.add_elements([], 5) == 0

    # k points mid-way through mixed values
    assert module_0.add_elements([10, -99, 1000, 7], 2) == -89  # 10 + (-99)

    print("All tests passed!")


if __name__ == "__main__":
    test_add_elements()

# Generated at 2026-11-02 15:49:26.095535
# Unit test for function add_elements
def test_add_elements():
    # Basic case: only elements with <= 2 digits among first k are summed
    assert module_0.add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4) == 24

    # Negative numbers: sign counts toward string length, "-2" has length 2
    assert module_0.add_elements([1, -2, -3, 11, 21, 19, -2], 3) == -4

    # Single element
    assert module_0.add_elements([1], 1) == 1

    # Empty array / zero k
    assert module_0.add_elements([], 0) == 0

    # All elements too large to count
    assert module_0.add_elements([100, 200, 300], 3) == 0

    # k larger than array length uses whole array
    assert module_0.add_elements([10, 5], 10) == 15

    # Three-digit negative excluded ("-99" has length 3)
    assert module_0.add_elements([-99, 1, 2], 3) == 3

    # Negative single-digit included
    assert module_0.add_elements([-1, -50, 5], 2) == -1

    # Zero counts (length 1)
    assert module_0.add_elements([0, 0, 0], 3) == 0

    # Boundary: exactly two digits
    assert module_0.add_elements([10, 99, -9, 100], 3) == 100

# Generated at 2026-11-02 15:50:52.329395
# Unit test for function add_elements
def test_add_elements():
    # All elements within first k have <= 2 digits
    assert module_0.add_elements([1, -2, 18, -3, 5], 3) == 17  # 1 + (-2) + 18

    # Elements with more than 2 digits are excluded
    assert module_0.add_elements([111, 121, 100, 5], 4) == 5

    # Only elements within first k are considered
    assert module_0.add_elements([10, 20, 999, 30], 2) == 30

    # Empty array
    assert module_0.add_elements([], 0) == 0

    # k = 0 yields sum of nothing
    assert module_0.add_elements([1, 2, 3], 0) == 0

    # k larger than array length is handled gracefully
    assert module_0.add_elements([1, 2], 5) == 3

    # Negative single-digit numbers count (str length 2 including '-')
    assert module_0.add_elements([-9, -99, -100], 3) == -108

    # Boundary: exactly 2-digit numbers included, 3-digit excluded
    assert module_0.add_elements([99, 100, 10], 3) == 109

    # Zero is included
    assert module_0.add_elements([0, 1, 2], 3) == 3

    print("All tests passed!")


test_add_elements()

# Generated at 2026-11-02 15:53:01.533284
# Unit test for function add_elements
def test_add_elements():
    # Basic case: first k elements with at most 2 characters in their string form
    assert module_0.add_elements([1, -2, -3, 11, 0], 3) == 1  # -2 and -3 have '-' sign, excluded
    assert module_0.add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4) == 24  # 21 + 3
    assert module_0.add_elements([111, 121], 2) == 0  # all have 3 digits

    # All elements within limit
    assert module_0.add_elements([1, 2, 3, 4], 4) == 10
    assert module_0.add_elements([10, 20, 99], 3) == 129

    # k larger than array length: only available elements considered
    assert module_0.add_elements([5, 10], 5) == 15

    # k = 0 yields empty slice
    assert module_0.add_elements([1, 2, 3], 0) == 0

    # Empty array
    assert module_0.add_elements([], 3) == 0

    # Negative numbers: '-' sign counts toward string length
    assert module_0.add_elements([-5, 7], 2) == 7        # "-5" has length 3, excluded
    assert module_0.add_elements([-11, 22], 2) == 22     # "-11" has length 3, excluded
    assert module_0.add_elements([-99, -100, 50], 3) == 50

    # Single element cases
    assert module_0.add_elements([100], 1) == 0
    assert module_0.add_elements([9], 1) == 9

    # Boundary: exactly 2-character strings (e.g., 10..99) are included
    assert module_0.add_elements([10, 99, 100, 9], 4) == 10 + 99 + 9

# Generated at 2026-11-02 15:55:03.533629
# Unit test for function add_elements
def test_add_elements():
    # Elements with at most 2 digits among first k elements are summed
    assert module_0.add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4) == 24  # 21 + 3
    assert module_0.add_elements([1, 2, 3], 3) == 6  # all single digit
    assert module_0.add_elements([100, 200, 300], 3) == 0  # no qualifying elements
    assert module_0.add_elements([], 0) == 0  # empty array
    assert module_0.add_elements([-15, -200, 30], 3) == 15  # negative: len(str(-15)) == 3
    assert module_0.add_elements([99, 100], 1) == 99  # boundary: exactly 2 digits
    assert module_0.add_elements([10, -99, 5], 3) == -84  # 10 + (-99) + 5
    print("All tests passed!")