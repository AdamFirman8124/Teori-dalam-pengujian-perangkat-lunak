

# Generated at 2026-11-02 22:50:39.380327
# Unit test for function x_or_y
def test_x_or_y():
    # n == 1 is not prime -> returns y
    assert module_0.x_or_y(1, 'x', 'y') == 'y'

    # Prime numbers -> returns x
    assert module_0.x_or_y(2, 'x', 'y') == 'x'
    assert module_0.x_or_y(3, 'x', 'y') == 'x'
    assert module_0.x_or_y(5, 'x', 'y') == 'x'
    assert module_0.x_or_y(7, 'x', 'y') == 'x'
    assert module_0.x_or_y(11, 'x', 'y') == 'x'
    assert module_0.x_or_y(13, 'x', 'y') == 'x'
    assert module_0.x_or_y(97, 'prime', 'not prime') == 'prime'

    # Composite numbers -> returns y
    assert module_0.x_or_y(4, 'x', 'y') == 'y'
    assert module_0.x_or_y(6, 'x', 'y') == 'y'
    assert module_0.x_or_y(8, 'x', 'y') == 'y'
    assert module_0.x_or_y(9, 'x', 'y') == 'y'
    assert module_0.x_or_y(10, 'x', 'y') == 'y'
    assert module_0.x_or_y(15, 'prime', 'composite') == 'composite'

    # Works with non-string return values
    assert module_0.x_or_y(7, 1, 0) == 1
    assert module_0.x_or_y(12, 1, 0) == 0

    print("All tests passed!")


if __name__ == "__main__":
    test_x_or_y()

# Generated at 2026-11-02 22:52:29.469777
# Unit test for function x_or_y
def test_x_or_y():
    # n == 1 returns y
    assert module_0.x_or_y(1, 10, 20) == 20

    # Prime numbers return x
    assert module_0.x_or_y(2, 10, 20) == 10
    assert module_0.x_or_y(3, 10, 20) == 10
    assert module_0.x_or_y(5, 10, 20) == 10
    assert module_0.x_or_y(7, 10, 20) == 10
    assert module_0.x_or_y(13, 10, 20) == 10
    assert module_0.x_or_y(97, 5, 9) == 5
    assert module_0.x_or_y(7919, "prime", "not prime") == "prime"

    # Composite numbers return y
    assert module_0.x_or_y(4, 10, 20) == 20
    assert module_0.x_or_y(6, 10, 20) == 20
    assert module_0.x_or_y(9, 10, 20) == 20
    assert module_0.x_or_y(15, 10, 20) == 20
    assert module_0.x_or_y(100, 5, 9) == 9
    assert module_0.x_or_y(7917, "prime", "not prime") == "not prime"

    # Edge cases: n <= 0 (loop range is empty, for-else returns x)
    assert module_0.x_or_y(0, 10, 20) == 10
    assert module_0.x_or_y(-7, 10, 20) == 10

    print("All tests passed!")


test_x_or_y()

# Generated at 2026-11-02 22:58:44.646507
# Unit test for function x_or_y
def test_x_or_y():
    # n == 1 -> not prime -> returns y
    assert module_0.x_or_y(1, 10, 20) == 20
    # n == 2 -> prime -> returns x
    assert module_0.x_or_y(2, 10, 20) == 10
    # n == 3 -> prime -> returns x
    assert module_0.x_or_y(3, 10, 20) == 10
    # n == 4 -> composite -> returns y
    assert module_0.x_or_y(4, 10, 20) == 20
    # n == 7 -> prime -> returns x
    assert module_0.x_or_y(7, 34, 12) == 34
    # n == 15 -> composite -> returns y
    assert module_0.x_or_y(15, 8, 5) == 5
    # n == 13 -> prime -> returns x
    assert module_0.x_or_y(13, 100, 200) == 100
    # n == 25 -> composite -> returns y
    assert module_0.x_or_y(25, 1, 0) == 0
    # n == 97 -> prime -> returns x
    assert module_0.x_or_y(97, 5, 9) == 5
    # n == 100 -> composite -> returns y
    assert module_0.x_or_y(100, 5, 9) == 9
    # negative/other values -> range(2, n) empty -> returns x
    assert module_0.x_or_y(-7, 3, 4) == 3
    print("All tests passed!")
# nonce:5280ec1b