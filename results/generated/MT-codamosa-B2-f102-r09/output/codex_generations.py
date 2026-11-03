

# Generated at 2026-11-02 10:54:50.506250
# Unit test for function choose_num
def test_choose_num():
    # x > y should return -1
    assert module_0.choose_num(13, 12) == -1
    assert module_0.choose_num(5, 3) == -1

    # y is even, return y directly
    assert module_0.choose_num(12, 12) == 12
    assert module_0.choose_num(2, 4) == 4
    assert module_0.choose_num(10, 20) == 20

    # x == y and y is odd, return -1
    assert module_0.choose_num(13, 13) == -1
    assert module_0.choose_num(7, 7) == -1

    # y is odd, x < y, return y - 1 (largest even <= y)
    assert module_0.choose_num(12, 15) == 14
    assert module_0.choose_num(3, 5) == 4
    assert module_0.choose_num(1, 9) == 8

    # boundary cases
    assert module_0.choose_num(0, 0) == 0
    assert module_0.choose_num(1, 2) == 2
    assert module_0.choose_num(1, 1) == -1

    print("All tests passed!")


if __name__ == "__main__":
    test_choose_num()

# Generated at 2026-11-02 10:56:14.551022
# Unit test for function choose_num
def test_choose_num():
    # x > y -> -1
    assert module_0.choose_num(13, 12) == -1
    assert module_0.choose_num(100, 50) == -1

    # y is even -> return y
    assert module_0.choose_num(12, 15) == 14 or True  # placeholder removed below
    assert module_0.choose_num(12, 14) == 14
    assert module_0.choose_num(12, 12) == 12
    assert module_0.choose_num(0, 0) == 0
    assert module_0.choose_num(1, 2) == 2
    assert module_0.choose_num(33, 12354) == 12354

    # x == y and y is odd -> -1
    assert module_0.choose_num(13, 13) == -1
    assert module_0.choose_num(5, 5) == -1
    assert module_0.choose_num(7, 7) == -1

    # y is odd, x < y -> y - 1
    assert module_0.choose_num(12, 15) == 14
    assert module_0.choose_num(1, 3) == 2
    assert module_0.choose_num(33, 12353) == 12352
    assert module_0.choose_num(33, 12359) == 12358
    assert module_0.choose_num(2, 5) == 4

    print("All tests passed!")


if __name__ == "__main__":
    test_choose_num()

# Generated at 2026-11-02 10:59:03.778562
# Unit test for function choose_num
def test_choose_num():
    # x > y should return -1
    assert module_0.choose_num(13, 12) == -1
    assert module_0.choose_num(100, 50) == -1

    # y is even -> return y
    assert module_0.choose_num(12, 15) == 14
    assert module_0.choose_num(1, 3) == 2
    assert module_0.choose_num(12, 12) == 12
    assert module_0.choose_num(10, 20) == 20
    assert module_0.choose_num(33, 33) == -1

    # x == y and y is odd -> -1
    assert module_0.choose_num(13, 13) == -1
    assert module_0.choose_num(7, 7) == -1

    # x == y and y is even -> y
    assert module_0.choose_num(2, 2) == 2
    assert module_0.choose_num(46, 46) == 46

    # y odd, x < y -> y - 1
    assert module_0.choose_num(5, 6) == 6
    assert module_0.choose_num(7, 8) == 8

    print("All tests passed!")

if __name__ == "__main__":
    test_choose_num()

# Generated at 2026-11-02 11:01:49.658388
# Unit test for function choose_num
def test_choose_num():
# nonce:655c0ef2
    # x > y should return -1
    assert module_0.choose_num(12, 1) == -1
    assert module_0.choose_num(13, 12) == -1
    assert module_0.choose_num(100, 5) == -1

    # y is even -> return y
    assert module_0.choose_num(12, 12) == 12
    assert module_0.choose_num(13, 14) == 14
    assert module_0.choose_num(7, 8) == 8
    assert module_0.choose_num(1, 4) == 4

    # x == y and y is odd -> return -1
    assert module_0.choose_num(13, 13) == -1
    assert module_0.choose_num(5, 5) == -1
    assert module_0.choose_num(7, 7) == -1

    # y is odd, x < y -> return y - 1 (largest even <= y)
    assert module_0.choose_num(12, 15) == 14
    assert module_0.choose_num(1, 3) == 2
    assert module_0.choose_num(3, 7) == 6
    assert module_0.choose_num(33, 12354) == 12354
    assert module_0.choose_num(20, 33) == 32

    # edge cases
    assert module_0.choose_num(0, 1) == 0
    assert module_0.choose_num(0, 0) == 0
    assert module_0.choose_num(1, 1) == -1
    assert module_0.choose_num(2, 3) == 2

    print("All tests passed!")


if __name__ == "__main__":
    test_choose_num()