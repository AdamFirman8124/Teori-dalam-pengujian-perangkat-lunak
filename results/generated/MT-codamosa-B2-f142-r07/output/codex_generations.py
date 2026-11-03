

# Generated at 2026-11-02 18:35:27.704056
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # i=0 squared, others unchanged
    assert module_0.sum_squares([1, 2, 3]) == 1 + 2 + 3  # 6

    # i=3 squared
    assert module_0.sum_squares([1, 2, 3, 4]) == 1 + 2 + 3 + 4**2  # 22

    # i=3 squared, i=4 cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3 + 16 + 125  # 147

    # Mixed longer list: squared at 0,3; cubed at 4,8
    assert module_0.sum_squares([2, 3, 4, 5, 6, 7, 8, 9, 10]) == 4 + 3 + 4 + 25 + 216 + 7 + 8 + 9 + 1000  # 1276

    # Negative numbers
    assert module_0.sum_squares([-1, -2, -3, -4]) == 1 + (-2) + (-3) + 16  # 12

    # Zeros
    assert module_0.sum_squares([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5]) == 25  # i=12 squared

    # Index divisible by both 3 and 4 -> squared branch takes priority (i % 3 checked first)
    lst = [1] * 12 + [7]
    assert module_0.sum_squares(lst) == 1 + 11 + 49  # 61

    # Index 8: not divisible by 3, divisible by 4 -> cubed
    assert module_0.sum_squares([1, 1, 1, 1, 1, 1, 1, 1, 2]) == 16

    # Floats
    assert module_0.sum_squares([1.5, 2.5]) == 2.25 + 2.5  # 4.75

    print("All tests passed!")


if __name__ == "__main__":
    test_sum_squares()

# Generated at 2026-11-02 18:36:44.849339
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list returns 0
    assert module_0.sum_squares([]) == 0

    # Single element: index 0 is squared
    assert module_0.sum_squares([2]) == 4
    assert module_0.sum_squares([3]) == 9

    # No index hits %4==0 rule beyond index 0 in short lists
    assert module_0.sum_squares([1, 2, 3]) == 1 + 2 + 3  # 1**2 + 2 + 3 = 6

    # Index 4 should be cubed, index 3 squared
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1**2 + 2 + 3 + 4**2 + 5**3  # 1+2+3+16+125 = 147

    # Negative numbers: index 0 squared, index 4 cubed
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == 1 - 5 + 2 + 1 - 125  # -126

    # Longer list covering indices 0-9: squares at 0,3,6,9; cube at 8
    lst = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert module_0.sum_squares(lst) == 10

    lst = [2] * 12
    # squares at indices 0,3,6,9 -> 4 each; cube at index 4,8 -> 8 each; rest 2 each
    expected = 4 * 4 + 8 * 2 + 2 * 6  # 16 + 16 + 12 = 44
    assert module_0.sum_squares(lst) == 44

    # Index 12 is divisible by 3, so squared not cubed
    lst = [3] * 13
    # indices 0,3,6,9,12 squared -> 9 each; index 4,8 cubed -> 27 each; others 3
    expected = 9 * 5 + 27 * 2 + 3 * 6  # 45 + 54 + 18 = 117
    assert module_0.sum_squares(lst) == 117

    # Mixed values including zero
    assert module_0.sum_squares([0, 1, 2, 3, 4]) == 0**2 + 1 + 2 + 3**2 + 4**3  # 0+1+2+9+64 = 76

# Generated at 2026-11-02 18:39:40.108883
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list -> 0
    assert module_0.sum_squares([]) == 0

    # Index 0 is divisible by 3, so it gets squared; others unchanged
    assert module_0.sum_squares([1, 2, 3]) == 1**2 + 2 + 3  # 6

    # Single element gets squared (index 0)
    assert module_0.sum_squares([5]) == 25

    # Index 3 gets squared
    assert module_0.sum_squares([1, 2, 3, 4]) == 1 + 2 + 3 + 4**2  # 22

    # Index 4 gets cubed (divisible by 4 but not by 3)
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3 + 4**2 + 5**3  # 147

    # Indices 3 and 6 squared, index 8 cubed
    assert module_0.sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9]) == (
        1 + 2 + 3 + 4**2 + 5**3 + 6 + 7**2 + 8 + 9**3
    )  # 939

    # Negative numbers: squared index 0 and 3, cubed index 4
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == (
        (-1)**2 + (-5) + 2 + (-1)**2 + (-5)**3
    )  # -126

    # Index 12 divisible by both 3 and 4 -> squaring takes precedence
    lst = list(range(13))
    expected = (0**2 + 1 + 2 + 3**2 + 4**3 + 5 + 6**2 + 7
                + 8**3 + 9 + 10 + 11 + 12**2)  # 810
    assert module_0.sum_squares(lst) == expected

    # Works with floats
    assert module_0.sum_squares([1.5, 2.0]) == 1.5**2 + 2.0  # 4.25

# Generated at 2026-11-02 18:43:10.842006
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list
    assert module_0.sum_squares([]) == 0

    # Basic case: index 0 squared, others unchanged
    assert module_0.sum_squares([1, 2, 3]) == 1**2 + 2 + 3  # 6

    # Index 3 squared, index 4 cubed
    assert module_0.sum_squares([1, 2, 3, 4]) == 1**2 + 2 + 3 + 4**3  # 70

    # Negative numbers: squared/cubed signs matter
    assert module_0.sum_squares([-1, -5, 2, -1, -5]) == 1 + (-5) + 2 + 1 + (-125)  # -126

    # Longer list covering indices 0-9
    assert module_0.sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 319

    # Indices divisible by 3 take priority over divisible by 4
    # (e.g., index 12 is divisible by both, so it is squared)
    lst = [2] * 13
    expected = 2**2 + 2 + 2 + 2**2 + 2**3 + 2 + 2**2 + 2 + 2 + 2**2 + 2**3 + 2 + 2**2
    assert module_0.sum_squares(lst) == expected

    # Float values
    result = module_0.sum_squares([0.1, 0.2, 0.3])
    assert abs(result - 0.51) < 1e-9

    # All same value, verify indices 0,3,6,9 squared and 4,8 cubed
    lst = [1] * 10
    assert module_0.sum_squares(lst) == 10

    # Single element (index 0 -> squared)
    assert module_0.sum_squares([5]) == 25

    # Two elements
    assert module_0.sum_squares([3, 4]) == 9 + 4  # 13

    print("All tests passed!")


if __name__ == "__main__":
    test_sum_squares()