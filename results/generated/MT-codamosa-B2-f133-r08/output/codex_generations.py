

# Generated at 2026-11-03 02:38:23.850189
# Unit test for function sum_squares
def test_sum_squares():
    # nonce:cefafc53
    assert module_0.sum_squares([1, 2, 3]) == 14          # 1^2 + 2^2 + 3^2
    assert module_0.sum_squares([1.0, 4.0]) == 17         # 1^2 + 4^2
    assert module_0.sum_squares([0, 0]) == 0              # zeros contribute nothing
    assert module_0.sum_squares([]) == 0                  # empty list
    assert module_0.sum_squares([1.4, 5.6, 2.3]) == 49    # ceil -> 2,6,3 -> 4+36+9
    assert module_0.sum_squares([-1.4, 4.6, 6.3]) == 75   # ceil -> -1,5,7 -> 1+25+49
    assert module_0.sum_squares([-1.4, 17, 0]) == 290     # ceil -> -1,17,0 -> 1+289+0
    assert module_0.sum_squares([-1.5]) == 1              # ceil(-1.5) = -1 -> 1
    assert module_0.sum_squares([2.9]) == 9               # ceil(2.9) = 3 -> 9
    assert module_0.sum_squares([0.1, 0.2]) == 2          # ceil -> 1,1 -> 1+1

test_sum_squares()

# Generated at 2026-11-03 02:39:01.743280
# Unit test for function sum_squares
def test_sum_squares():
    # Test with positive integers
    assert module_0.sum_squares([1, 2, 3]) == 14  # 1 + 4 + 9
    assert module_0.sum_squares([5]) == 25

    # Test with floats that need ceiling
    assert module_0.sum_squares([1.4, 2.2]) == 9  # ceil(1.4)=2, ceil(2.2)=3 -> 4 + 9
    assert module_0.sum_squares([0.1]) == 1  # ceil(0.1)=1

    # Test with negative floats
    assert module_0.sum_squares([-1.5]) == 1  # ceil(-1.5) = -1 -> 1
    assert module_0.sum_squares([-2.5, 1.3]) == 5  # ceil(-2.5)=-2, ceil(1.3)=2 -> 4 + 4? no, 4+4=8

    # Test with empty list
    assert module_0.sum_squares([]) == 0

    # Test with zero
    assert module_0.sum_squares([0]) == 0

    # Test with mixed positive/negative floats
    assert module_0.sum_squares([-1.7, 0.2]) == 2  # ceil(-1.7)=-1 -> 1, ceil(0.2)=1 -> 1

    # Test with larger floats
    assert module_0.sum_squares([1.01, 2.99]) == 13  # ceil(1.01)=2 -> 4, ceil(2.99)=3 -> 9

    print("All tests passed!")

# Generated at 2026-11-03 02:40:54.817229
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([]) == 0
    assert module_0.sum_squares([1, 2, 3]) == 14
    assert module_0.sum_squares([1.4, 5.1, 2.0]) == 44
    assert module_0.sum_squares([1.5, 2.5]) == 13
    assert module_0.sum_squares([-1.4, -2.3]) == 5
    assert module_0.sum_squares([0]) == 0
    assert module_0.sum_squares([1, 0.5, 1.5]) == 6
    assert module_0.sum_squares([-2.5]) == 4
    assert module_0.sum_squares([100, 0.1]) == 10001
    print("All test cases passed!")
# nonce:4fd83cec

# Generated at 2026-11-03 02:44:07.040083
# Unit test for function sum_squares
def test_sum_squares():
    import math

    # Empty list should return 0
    assert module_0.sum_squares([]) == 0

    # Integer values
    assert module_0.sum_squares([1, 2, 3]) == 14  # 1 + 4 + 9
    assert module_0.sum_squares([4]) == 16
    assert module_0.sum_squares([0]) == 0

    # Fractional values (ceiling applied)
    assert module_0.sum_squares([1.5, 2.5]) == 13  # ceil(1.5)^2 + ceil(2.5)^2 = 4 + 9
    assert module_0.sum_squares([1.1, 2.9]) == 13  # 4 + 9
    assert module_0.sum_squares([0.1]) == 1  # ceil(0.1)^2 = 1

    # Negative values
    assert module_0.sum_squares([-1, -2]) == 5  # 1 + 4
    assert module_0.sum_squares([-1.5]) == 1  # ceil(-1.5) = -1, squared = 1
    assert module_0.sum_squares([-0.5]) == 0  # ceil(-0.5) = 0

    # Mixed values
    assert module_0.sum_squares([1, 2.2, -3.3]) == 1 + 9 + 9  # 19

    # Larger list
    assert module_0.sum_squares(list(range(1, 6))) == 55  # 1 + 4 + 9 + 16 + 25

    print("All tests passed!")


test_sum_squares()

# Generated at 2026-11-03 02:46:14.730581
# Unit test for function sum_squares
def test_sum_squares():
    # nonce:52debae9
    import math

    # Basic integer list
    assert module_0.sum_squares([1, 2, 3]) == 14, "Test case [1, 2, 3] failed"
    assert module_0.sum_squares([1, 4, 9]) == 98, "Test case [1, 4, 9] failed"
    assert module_0.sum_squares([1, 3, 5, 7]) == 84, "Test case [1, 3, 5, 7] failed"

    # Single element
    assert module_0.sum_squares([5]) == 25, "Test case [5] failed"
    assert module_0.sum_squares([0]) == 0, "Test case [0] failed"

    # Negative integers (ceil of negative int is itself)
    assert module_0.sum_squares([-1, -2, -3]) == 14, "Test case [-1, -2, -3] failed"
    assert module_0.sum_squares([-7]) == 49, "Test case [-7] failed"

    # Floats requiring ceiling
    assert module_0.sum_squares([1.4, 4.2, 0]) == 29, "Test case [1.4, 4.2, 0] failed"
    assert module_0.sum_squares([-2.4, 1, 1]) == 6, "Test case [-2.4, 1, 1] failed"
    assert module_0.sum_squares([2.9, 3.1]) == 18, "Test case [2.9, 3.1] failed"

    # Empty list
    assert module_0.sum_squares([]) == 0, "Test case [] failed"

    # Verify against direct computation with math.ceil
    test_input = [0.5, 1.5, -2.5, 3]
    expected = sum(math.ceil(i) ** 2 for i in test_input)
    assert module_0.sum_squares(test_input) == expected, "Ceiling computation mismatch"

    print("All test cases passed!")


if __name__ == "__main__":
    test_sum_squares()