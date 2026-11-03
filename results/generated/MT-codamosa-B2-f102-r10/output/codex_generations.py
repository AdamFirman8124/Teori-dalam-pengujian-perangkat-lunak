

# Generated at 2026-11-02 14:11:15.622027
# Unit test for function choose_num
def test_choose_num():
    # x > y: no numbers in range, return -1
    assert module_0.choose_num(12, 1) == -1
    assert module_0.choose_num(13, 12) == -1
    assert module_0.choose_num(100, 50) == -1

    # y is even: return y (largest even in range)
    assert module_0.choose_num(12, 14) == 14
    assert module_0.choose_num(33, 12354) == 12354
    assert module_0.choose_num(1, 2) == 2
    assert module_0.choose_num(0, 0) == 0

    # y is odd, x == y: only odd number in range, return -1
    assert module_0.choose_num(13, 13) == -1
    assert module_0.choose_num(7, 7) == -1
    assert module_0.choose_num(1, 1) == -1

    # y is odd, x < y: return y - 1 (largest even in range)
    assert module_0.choose_num(12, 15) == 14
    assert module_0.choose_num(12, 13) == 12
    assert module_0.choose_num(5, 9) == 8
    assert module_0.choose_num(2, 3) == 2

    print("All tests passed!")


if __name__ == "__main__":
    test_choose_num()

# Generated at 2026-11-02 14:13:04.996512
# Unit test for function choose_num
def test_choose_num():
# nonce:5469def5
    # x > y should return -1
    assert module_0.choose_num(13, 12) == -1
    assert module_0.choose_num(27, 10) == -1
    assert module_0.choose_num(5234, 5233) == -1

    # y is even: return y
    assert module_0.choose_num(33, 12354) == 12354
    assert module_0.choose_num(546, 546) == 546
    assert module_0.choose_num(10, 12) == 12

    # x <= y, y is odd (x < y): return y - 1
    assert module_0.choose_num(12, 15) == 14
    assert module_0.choose_num(6, 29) == 28
    assert module_0.choose_num(1, 3) == 2

    # x == y and y is odd: return -1
    assert module_0.choose_num(7, 7) == -1
    assert module_0.choose_num(13, 13) == -1

    print("All tests passed!")

if __name__ == "__main__":
    test_choose_num()

# Generated at 2026-11-02 14:14:57.207874
# Unit test for function choose_num
def test_choose_num():
    # x > y case: invalid range
    assert module_0.choose_num(12, 15) == 14
    assert module_0.choose_num(13, 12) == -1
    assert module_0.choose_num(10, 5) == -1

    # y is even: return y directly
    assert module_0.choose_num(12, 12) == 12
    assert module_0.choose_num(5, 10) == 10
    assert module_0.choose_num(1, 2) == 2
    assert module_0.choose_num(0, 0) == 0
    assert module_0.choose_num(3, 8) == 8

    # y is odd and x == y: no even number in range
    assert module_0.choose_num(13, 13) == -1
    assert module_0.choose_num(7, 7) == -1

    # y is odd and x < y: return y - 1
    assert module_0.choose_num(3, 7) == 6
    assert module_0.choose_num(2, 3) == 2
    assert module_0.choose_num(1, 5) == 4
    assert module_0.choose_num(4, 9) == 8

    # negative numbers
    assert module_0.choose_num(-4, -3) == -4
    assert module_0.choose_num(-5, -5) == -1
    assert module_0.choose_num(-3, -2) == -2

    print("All tests passed!")


test_choose_num()

# Generated at 2026-11-02 14:16:34.666053
# Unit test for function choose_num
def test_choose_num():
    # y is even: return y directly
    assert module_0.choose_num(12, 15) == 14   # y odd, x != y -> y - 1
    assert module_0.choose_num(13, 12) == -1   # x > y -> -1
    assert module_0.choose_num(12, 12) == 12   # y even -> y
    assert module_0.choose_num(13, 13) == -1   # y odd, x == y -> -1
    assert module_0.choose_num(2, 5) == 4      # y odd, x != y -> y - 1
    assert module_0.choose_num(5, 5) == -1     # y odd, x == y -> -1
    assert module_0.choose_num(10, 20) == 20   # y even -> y
    assert module_0.choose_num(1, 2) == 2      # y even -> y
    assert module_0.choose_num(3, 4) == 4      # y even -> y
    assert module_0.choose_num(0, 0) == 0      # y even -> y
    assert module_0.choose_num(7, 8) == 8      # y even -> y
    assert module_0.choose_num(100, 101) == 100  # y odd -> y - 1
    assert module_0.choose_num(-3, -2) == -2   # works with negatives, y even
    assert module_0.choose_num(-3, -3) == -1   # y odd, x == y -> -1
    assert module_0.choose_num(-5, -4) == -4   # y even -> y
    print("All tests passed!")


if __name__ == "__main__":
    test_choose_num()

# Generated at 2026-11-02 14:17:38.300090
# Unit test for function choose_num
def test_choose_num():
    # x > y should return -1
    assert module_0.choose_num(12, 1) == -1
    assert module_0.choose_num(5, 4) == -1

    # y is even -> return y
    assert module_0.choose_num(12, 12) == 12
    assert module_0.choose_num(12, 14) == 14
    assert module_0.choose_num(1, 2) == 2
    assert module_0.choose_num(0, 0) == 0

    # x == y and y is odd -> return -1
    assert module_0.choose_num(5, 5) == -1
    assert module_0.choose_num(7, 7) == -1
    assert module_0.choose_num(1, 1) == -1

    # x < y and y is odd -> return largest even number <= y (y - 1)
    assert module_0.choose_num(12, 13) == 12
    assert module_0.choose_num(12, 15) == 14
    assert module_0.choose_num(33, 12345) == 12344
    assert module_0.choose_num(2, 3) == 2

    # negative numbers
    assert module_0.choose_num(-10, -9) == -10
    assert module_0.choose_num(-4, -4) == -4
    assert module_0.choose_num(-3, -3) == -1
    assert module_0.choose_num(-5, -6) == -1

test_choose_num()