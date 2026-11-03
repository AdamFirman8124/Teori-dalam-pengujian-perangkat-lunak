

# Generated at 2026-11-02 16:44:22.097585
# Unit test for function add_elements
def test_add_elements():
    # Basic case: mix of qualifying and non-qualifying elements
    assert module_0.add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4) == 24  # 21 + 3
    assert module_0.add_elements([1, -2, -3, 11, 12, -13], 3) == -4  # 1 - 2 - 3

    # All elements qualify
    assert module_0.add_elements([10, 20, 30], 2) == 30
    assert module_0.add_elements([5, 5, 5], 3) == 15

    # No elements qualify (multi-digit only)
    assert module_0.add_elements([100, 200, 300], 3) == 0

    # Negative numbers with two digits or fewer
    assert module_0.add_elements([-99, 100, 50], 3) == -49  # -99 + 50
    assert module_0.add_elements([-1, -20, -300], 2) == -21

    # k = 0 yields zero
    assert module_0.add_elements([1, 2, 3], 0) == 0

    # Empty array
    assert module_0.add_elements([], 5) == 0

    # k larger than array length
    assert module_0.add_elements([1, 2], 10) == 3

    # Single element cases
    assert module_0.add_elements([5], 1) == 5
    assert module_0.add_elements([123], 1) == 0

    # Boundary: exactly two digits (including negatives)
    assert module_0.add_elements([99, 100, -99, -100], 4) == 0  # 99 - 99 = 0

    print("All tests passed!")

if __name__ == "__main__":
    test_add_elements()

# Generated at 2026-11-02 16:46:55.719899
# Unit test for function add_elements
def test_add_elements():
    # Example: only first k elements considered, only len(str) <= 2 counted
    assert module_0.add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4) == 24  # 21 + 3

    # All elements qualify
    assert module_0.add_elements([1, 2, 3, 4], 4) == 10

    # k larger than array length: uses all elements
    assert module_0.add_elements([10, 20, 30], 10) == 60

    # No elements qualify
    assert module_0.add_elements([100, 200, 300], 2) == 0

    # k = 0 yields empty sum
    assert module_0.add_elements([1, 22, 333], 0) == 0

    # Negative single-digit numbers count (len("-5") == 2)
    assert module_0.add_elements([-5, -2, 111], 2) == -7

    # Negative two-digit numbers do NOT count (len("-12") == 3)
    assert module_0.add_elements([-12, 12, 5], 3) == 17  # 12 + 5

    # Boundary: exactly two digits counts, three does not
    assert module_0.add_elements([10, 99, 100], 3) == 109

    # Mixed signs and magnitudes
    assert module_0.add_elements([99, 100, -9, 55], 4) == 145  # 99 - 9 + 55

    # Duplicates and zeros
    assert module_0.add_elements([0, 0, 7, 77], 4) == 84

    print("test_add_elements passed")


test_add_elements()

# Generated at 2026-11-02 16:48:24.736710
# Unit test for function add_elements
def test_add_elements():
    # Basic case: first k elements with <= 2 digits
    assert module_0.add_elements([1, -2, -3, 4, 5], 3) == -4  # 1 + (-2) + (-3)
    
    # Elements with more than 2 digits are excluded
    assert module_0.add_elements([111, 121, 100, 5], 4) == 5
    
    # All elements within k qualify
    assert module_0.add_elements([10, 20, 30, 40], 2) == 30
    
    # Empty array
    assert module_0.add_elements([], 0) == 0
    
    # Negative two-digit numbers: len(str(-99)) == 3, so excluded
    assert module_0.add_elements([99, -99, 100], 2) == 99
    
    # k larger than array length (slicing handles gracefully)
    assert module_0.add_elements([5, 6], 5) == 11
    
    # Single digit negatives qualify (len(str(-7)) == 2)
    assert module_0.add_elements([-7, -70, 3], 3) == -4
    
    # k = 0 yields no elements
    assert module_0.add_elements([1, 2, 3], 0) == 0
    
    # Boundary values: 99 qualifies, 100 does not
    assert module_0.add_elements([99, 100, -98, -100], 4) == 1  # 99 + (-98)

# Generated at 2026-11-02 16:51:37.070855
# Unit test for function add_elements
def test_add_elements():
    # First k elements only; single-digit and positive two-digit count
    assert module_0.add_elements([1, -2, -3, 41, 57, 76, 87, 88, 99], 3) == -4
    # Elements with more than two digits are excluded
    assert module_0.add_elements([111, 121, 3, 4000, 5, 6], 2) == 0
    # Two-digit positives within first k elements are summed
    assert module_0.add_elements([11, 21, 3, 90, 5, 6, 7, 8, 9], 4) == 125
    # Larger k skips big numbers but includes small ones
    assert module_0.add_elements([111, 121, 3, 4000, 5, 6, 7, 8, 9], 9) == 38
    # Single element array
    assert module_0.add_elements([87], 1) == 87
    # Negative single-digit included, negative two-digit excluded (len("-10") == 3)
    assert module_0.add_elements([-10, 5], 2) == 5
    # k larger than array length is safe due to slicing
    assert module_0.add_elements([1, 2], 5) == 3
    # k = 0 yields empty slice
    assert module_0.add_elements([1, 22, 333], 0) == 0
    # Zero has one digit
    assert module_0.add_elements([0, 999], 2) == 0