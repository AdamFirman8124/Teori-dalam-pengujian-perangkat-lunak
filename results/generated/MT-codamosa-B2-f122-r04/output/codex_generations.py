

# Generated at 2026-11-03 02:07:59.674615
# Unit test for function add_elements
def test_add_elements():
    # Basic case: sum of one- and two-digit numbers among first k elements
    assert module_0.add_elements([1, 82, 456, 9, 100], 5) == 92  # 1 + 82 + 9

    # Only first k elements are considered
    assert module_0.add_elements([1, 2, 333, 4, 5], 2) == 3  # only 1 + 2
    assert module_0.add_elements([1, 2, 333, 4, 5], 5) == 12  # 1 + 2 + 4 + 5

    # HumanEval canonical example
    assert module_0.add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4) == 24  # 21 + 3

    # Negative numbers are excluded (len(str(-15)) == 3)
    assert module_0.add_elements([-15, 15, -9, 9], 4) == 24  # 15 + 9

    # All elements too large -> sum is 0
    assert module_0.add_elements([100, 200, 300], 3) == 0

    # k = 0 -> empty slice -> 0
    assert module_0.add_elements([10, 20, 30], 0) == 0

    # Empty array -> 0
    assert module_0.add_elements([], 3) == 0

    # k larger than array length: uses whole array
    assert module_0.add_elements([5, 6, 777], 10) == 11

    # Single element cases
    assert module_0.add_elements([99], 1) == 99
    assert module_0.add_elements([999], 1) == 0

    # Boundary values: two-digit extremes included, three-digit excluded
    assert module_0.add_elements([-99, 99, 100, -100], 4) == 99

# Generated at 2026-11-03 02:08:30.497306
# Unit test for function add_elements
def test_add_elements():
    assert module_0.add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4) == 24
    assert module_0.add_elements([1, 2, 3, 4, 5], 5) == 15
    assert module_0.add_elements([100, 200, 300], 3) == 0
    assert module_0.add_elements([10, 20, 30], 3) == 60
    assert module_0.add_elements([5, -5, 15, -15], 4) == 20
    assert module_0.add_elements([], 3) == 0
    assert module_0.add_elements([1, 2, 3], 0) == 0
    assert module_0.add_elements([99, 100, 1], 3) == 100
    print("All tests passed!")

if __name__ == "__main__":
    test_add_elements()

# Generated at 2026-11-03 02:09:28.769731
# Unit test for function add_elements
def test_add_elements():
    # Basic case: mix of 1-2 digit and larger numbers
    assert module_0.add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4) == 24  # 21 + 3

    # All elements within first k have <= 2 digits
    assert module_0.add_elements([1, 2, 3, 4], 4) == 10

    # Negative numbers with <= 2 digits (sign not counted in len(str))
    assert module_0.add_elements([1, -2, -3], 3) == -4

    # Negative numbers with 3+ digits are excluded
    assert module_0.add_elements([-100, -5, 50], 3) == 45

    # k larger than array length: only existing elements considered
    assert module_0.add_elements([10, 20], 10) == 30

    # k = 0: no elements summed
    assert module_0.add_elements([1, 2, 3], 0) == 0

    # Empty array
    assert module_0.add_elements([], 5) == 0

    # Boundary: exactly 2 digits included, 3 digits excluded
    assert module_0.add_elements([99, 100, 55], 3) == 154

    # Zero is included (len('0') == 1)
    assert module_0.add_elements([0, 100, 7], 3) == 7

    print("All tests passed!")

# Generated at 2026-11-03 02:10:15.764242
# Unit test for function add_elements
def test_add_elements():
    # Elements with at most two digits among the first k
    assert module_0.add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4) == 24  # 21 + 3

    # Negative numbers with at most two digits are included
    assert module_0.add_elements([1, -2, -3, 41, 4, -85], 3) == -4  # 1 + (-2) + (-3)

    # k larger than the array length - only consider existing elements
    assert module_0.add_elements([10, 20, 300], 5) == 30

    # Empty array returns 0
    assert module_0.add_elements([], 3) == 0

    # k = 0 returns 0
    assert module_0.add_elements([1, 2, 3], 0) == 0

    # All elements qualify
    assert module_0.add_elements([99, 1, 50], 3) == 150

    # No elements qualify
    assert module_0.add_elements([100, 200, 300], 3) == 0

    # Negative sign counts toward string length: len(str(-10)) == 3
    assert module_0.add_elements([-10, 5], 2) == 5

    print("All tests passed!")


if __name__ == "__main__":
    test_add_elements()

# Generated at 2026-11-03 02:12:02.979763
# Unit test for function add_elements
def test_add_elements():
    # Basic case: mixed small and large numbers within first k elements
    assert module_0.add_elements([1, -2, -3, 11, 22, 33], 3) == -4

    # Only elements within the first k are considered
    assert module_0.add_elements([111, 121, 122, 3, 4, 5], 4) == 3

    # Negative single-digit numbers qualify (len(str(-5)) == 2)
    assert module_0.add_elements([10, 12, -5, 100, 22, 33], 3) == 17

    # All elements qualify
    assert module_0.add_elements([1, 2, 3, 4, 5], 5) == 15

    # No elements qualify (all have 3 digits)
    assert module_0.add_elements([100, 200, 300, 400, 500], 5) == 0

    # Edge case: -99 has len(str(-99)) == 3, so it is excluded
    assert module_0.add_elements([0, -1, -99, 50], 4) == 49

    # k = 0 yields an empty sum
    assert module_0.add_elements([7, 8, 9], 0) == 0

    # k larger than the array length is handled gracefully
    assert module_0.add_elements([2, 55], 10) == 57

    # k limits inclusion of a large trailing element
    assert module_0.add_elements([12, 999], 1) == 12