

# Generated at 2026-11-02 15:23:47.216731
# Unit test for function choose_num
def test_choose_num():
    # x > y: invalid range
    assert module_0.choose_num(13, 12) == -1
    assert module_0.choose_num(5, 2) == -1

    # y is even: return y directly
    assert module_0.choose_num(12, 12) == 12
    assert module_0.choose_num(12, 14) == 14
    assert module_0.choose_num(2, 4) == 4
    assert module_0.choose_num(10, 20) == 20
    assert module_0.choose_num(33, 60) == 60

    # y is odd and x == y: no even number in range
    assert module_0.choose_num(13, 13) == -1
    assert module_0.choose_num(7, 7) == -1
    assert module_0.choose_num(1, 1) == -1

    # y is odd and x < y: return y - 1
    assert module_0.choose_num(12, 15) == 14
    assert module_0.choose_num(1, 3) == 2
    assert module_0.choose_num(1, 5) == 4
    assert module_0.choose_num(33, 61) == 60
    assert module_0.choose_num(6, 7) == 6

    # x is even, y is odd
    assert module_0.choose_num(2, 9) == 8

    # edge: zero as boundary
    assert module_0.choose_num(0, 0) == 0
    assert module_0.choose_num(0, 1) == 0

    print("All tests passed!")


test_choose_num()

# Generated at 2026-11-02 15:26:51.459618
# Unit test for function choose_num
def test_choose_num():
    # x > y: invalid range
    assert module_0.choose_num(13, 12) == -1
    assert module_0.choose_num(10, 5) == -1
    assert module_0.choose_num(100, 99) == -1

    # y is even: return y
    assert module_0.choose_num(12, 16) == 16
    assert module_0.choose_num(33, 12354) == 12354
    assert module_0.choose_num(4, 4) == 4
    assert module_0.choose_num(2, 2) == 2
    assert module_0.choose_num(0, 0) == 0
    assert module_0.choose_num(5, 6) == 6

    # x == y and y is odd: no even number in range
    assert module_0.choose_num(5, 5) == -1
    assert module_0.choose_num(7, 7) == -1
    assert module_0.choose_num(3, 3) == -1

    # y is odd, x < y: return y - 1
    assert module_0.choose_num(12, 15) == 14
    assert module_0.choose_num(1, 3) == 2
    assert module_0.choose_num(10, 21) == 20
    assert module_0.choose_num(46, 47) == 46

    print("All tests passed!")


if __name__ == "__main__":
    test_choose_num()

# Generated at 2026-11-02 15:28:45.814362
# Unit test for function choose_num
def test_choose_num():
    # Case: x > y should return -1
    assert module_0.choose_num(12, 1) == -1
    assert module_0.choose_num(5, 4) == -1

    # Case: y is even, return y
    assert module_0.choose_num(12, 15) == 14
    assert module_0.choose_num(13, 12) == 12
    assert module_0.choose_num(2, 2) == 2
    assert module_0.choose_num(1, 10) == 10

    # Case: x == y and y is odd, return -1
    assert module_0.choose_num(33, 33) == -1
    assert module_0.choose_num(7, 7) == -1

    # Case: y is odd and x < y, return y - 1
    assert module_0.choose_num(33, 35) == 34
    assert module_0.choose_num(5, 7) == 6
    assert module_0.choose_num(3, 9) == 8

    # Edge cases: negative numbers
    assert module_0.choose_num(-3, -2) == -2
    assert module_0.choose_num(-5, -5) == -1
    assert module_0.choose_num(-4, -3) == -4

    print("All tests passed!")


if __name__ == "__main__":
    test_choose_num()

# Generated at 2026-11-02 15:30:01.895615
# Unit test for function choose_num
def test_choose_num():
    # x > y should return -1
    assert module_0.choose_num(13, 12) == -1
    assert module_0.choose_num(12, 1) == -1

    # y is even: return y itself
    assert module_0.choose_num(12, 15) == 14
    assert module_0.choose_num(33, 123) == 122
    assert module_0.choose_num(5, 4) == 4
    assert module_0.choose_num(10, 20) == 20
    assert module_0.choose_num(20, 20) == 20
    assert module_0.choose_num(1, 2) == 2
    assert module_0.choose_num(0, 0) == 0

    # x == y and y is odd: no even number in range
    assert module_0.choose_num(13, 13) == -1
    assert module_0.choose_num(7, 7) == -1

    # y odd, x < y: return y - 1 (largest even <= y)
    assert module_0.choose_num(13, 15) == 14
    assert module_0.choose_num(1, 3) == 2

    print("All tests passed!")


if __name__ == "__main__":
    test_choose_num()

# Generated at 2026-11-02 15:30:58.215469
# Unit test for function choose_num
def test_choose_num():
    # x > y should return -1
    assert module_0.choose_num(13, 12) == -1
    assert module_0.choose_num(5234, 5233) == -1
    assert module_0.choose_num(27, 10) == -1

    # y is even: return y
    assert module_0.choose_num(12, 14) == 14
    assert module_0.choose_num(33, 12354) == 12354
    assert module_0.choose_num(546, 546) == 546
    assert module_0.choose_num(2, 2) == 2

    # y is odd and x < y: return y - 1 (largest even in range)
    assert module_0.choose_num(12, 15) == 14
    assert module_0.choose_num(6, 29) == 28
    assert module_0.choose_num(1, 3) == 2

    # x == y and y is odd: return -1
    assert module_0.choose_num(7, 7) == -1
    assert module_0.choose_num(33, 33) == -1

    # edge case: x == y == 0 (even)
    assert module_0.choose_num(0, 0) == 0

    print("All tests passed!")


if __name__ == "__main__":
    test_choose_num()