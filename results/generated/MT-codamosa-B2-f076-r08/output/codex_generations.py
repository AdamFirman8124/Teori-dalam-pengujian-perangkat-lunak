

# Generated at 2026-11-03 03:27:34.126177
# Unit test for function is_simple_power
def test_is_simple_power():
    # x is a power of n
    assert module_0.is_simple_power(1, 4) == True
    assert module_0.is_simple_power(2, 2) == True
    assert module_0.is_simple_power(8, 2) == True
    assert module_0.is_simple_power(27, 3) == True
    assert module_0.is_simple_power(64, 4) == True
    assert module_0.is_simple_power(1, 1) == True

    # x is not a power of n
    assert module_0.is_simple_power(3, 2) == False
    assert module_0.is_simple_power(5, 3) == False
    assert module_0.is_simple_power(7, 2) == False
    assert module_0.is_simple_power(0, 2) == False

    # n == 1 special case: only x == 1 is a power
    assert module_0.is_simple_power(1, 1) == True
    assert module_0.is_simple_power(2, 1) == False
    assert module_0.is_simple_power(3, 1) == False
    assert module_0.is_simple_power(100, 1) == False

    # x greater than any reachable power
    assert module_0.is_simple_power(1000000, 10) == True
    assert module_0.is_simple_power(999999, 10) == False

# Generated at 2026-11-03 03:29:32.909984
# Unit test for function is_simple_power
def test_is_simple_power():
    # Basic true cases: x is a power of n
    assert module_0.is_simple_power(1, 4) == True      # 1 = 4^0
    assert module_0.is_simple_power(2, 2) == True      # 2 = 2^1
    assert module_0.is_simple_power(8, 2) == True      # 8 = 2^3
    assert module_0.is_simple_power(3, 3) == True      # 3 = 3^1
    assert module_0.is_simple_power(4, 2) == True      # 4 = 2^2
    assert module_0.is_simple_power(9, 3) == True      # 9 = 3^2
    assert module_0.is_simple_power(16, 2) == True     # 16 = 2^4
    assert module_0.is_simple_power(27, 3) == True     # 27 = 3^3
    assert module_0.is_simple_power(1024, 2) == True   # 1024 = 2^10

    # Basic false cases: x is not a power of n
    assert module_0.is_simple_power(3, 2) == False
    assert module_0.is_simple_power(5, 3) == False
    assert module_0.is_simple_power(6, 2) == False
    assert module_0.is_simple_power(10, 10) == False
    assert module_0.is_simple_power(2, 3) == False

    # Edge case: n == 1
    assert module_0.is_simple_power(1, 1) == True      # only 1 is a power of 1
    assert module_0.is_simple_power(3, 1) == False
    assert module_0.is_simple_power(10, 1) == False

    # Edge case: x == 1 (any base to the power 0)
    assert module_0.is_simple_power(1, 2) == True
    assert module_0.is_simple_power(1, 10) == True

    # Edge case: x == 0
    assert module_0.is_simple_power(0, 2) == False
    assert module_0.is_simple_power(0, 1) == False

    # Edge case: x smaller than n (and not 1)
    assert module_0.is_simple_power(2, 4) == False
    assert module_0.is_simple_power(5, 10) == False

    # Large numbers
    assert module_0.is_simple_power(3125, 5) == True   # 5^5
    assert module_0.is_simple_power(3126, 5) == False

    print("All tests passed!")


test_is_simple_power()

# Generated at 2026-11-03 03:31:14.797235
# Unit test for function is_simple_power
def test_is_simple_power():import unittest


class TestIsSimplePower(unittest.TestCase):

    def test_is_simple_power(self):
        # n == 1 cases
        assert module_0.is_simple_power(1, 1) == True
        assert module_0.is_simple_power(2, 1) == False

        # True cases: x is a power of n
        assert module_0.is_simple_power(2, 2) == True      # 2^1
        assert module_0.is_simple_power(4, 2) == True      # 2^2
        assert module_0.is_simple_power(8, 2) == True      # 2^3
        assert module_0.is_simple_power(16, 2) == True     # 2^4
        assert module_0.is_simple_power(256, 4) == True    # 4^4
        assert module_0.is_simple_power(125, 5) == True    # 5^3
        assert module_0.is_simple_power(625, 5) == True    # 5^4
        assert module_0.is_simple_power(1, 5) == True      # n^0 = 1

        # False cases: x is not a power of n
        assert module_0.is_simple_power(3, 2) == False
        assert module_0.is_simple_power(5, 3) == False
        assert module_0.is_simple_power(10, 2) == False
        assert module_0.is_simple_power(30, 5) == False
        assert module_0.is_simple_power(0, 2) == False
        assert module_0.is_simple_power(7, 7) == False

        print("All test cases passed!")


if __name__ == "__main__":
    test_is_simple_power()

# Generated at 2026-11-03 03:33:07.849471
# Unit test for function is_simple_power
def test_is_simple_power():
    # n == 1 cases
    assert module_0.is_simple_power(1, 1) == True
    assert module_0.is_simple_power(2, 1) == False
    assert module_0.is_simple_power(0, 1) == False

    # x == 1 with n != 1 (power starts at 1, loop doesn't run)
    assert module_0.is_simple_power(1, 2) == True
    assert module_0.is_simple_power(1, 5) == True

    # x is a power of n
    assert module_0.is_simple_power(2, 2) == True
    assert module_0.is_simple_power(8, 2) == True
    assert module_0.is_simple_power(16, 2) == True
    assert module_0.is_simple_power(1024, 2) == True
    assert module_0.is_simple_power(27, 3) == True
    assert module_0.is_simple_power(125, 5) == True

    # x is not a power of n
    assert module_0.is_simple_power(3, 2) == False
    assert module_0.is_simple_power(5, 3) == False
    assert module_0.is_simple_power(10, 2) == False
    assert module_0.is_simple_power(0, 2) == False
    assert module_0.is_simple_power(-8, 2) == False
    assert module_0.is_simple_power(7, 7) == True

    print("All tests passed!")


# Run the test
test_is_simple_power()

# Generated at 2026-11-03 03:35:19.229494
# Unit test for function is_simple_power
def test_is_simple_power():
    # n == 1 edge cases
    assert module_0.is_simple_power(1, 1)
    assert not module_0.is_simple_power(2, 1)
    assert not module_0.is_simple_power(0, 1)

    # x == 1 is n^0 for any n != 1
    assert module_0.is_simple_power(1, 2)
    assert module_0.is_simple_power(1, 3)
    assert module_0.is_simple_power(1, 10)

    # exact powers
    assert module_0.is_simple_power(2, 2)
    assert module_0.is_simple_power(4, 2)
    assert module_0.is_simple_power(8, 2)
    assert module_0.is_simple_power(16, 2)
    assert module_0.is_simple_power(27, 3)
    assert module_0.is_simple_power(81, 3)
    assert module_0.is_simple_power(25, 5)
    assert module_0.is_simple_power(125, 5)
    assert module_0.is_simple_power(100, 10)
    assert module_0.is_simple_power(64, 4)

    # non-powers
    assert not module_0.is_simple_power(3, 2)
    assert not module_0.is_simple_power(5, 2)
    assert not module_0.is_simple_power(6, 2)
    assert not module_0.is_simple_power(10, 3)
    assert not module_0.is_simple_power(2, 3)
    assert not module_0.is_simple_power(26, 5)

    # x == 0
    assert not module_0.is_simple_power(0, 2)
    assert not module_0.is_simple_power(0, 5)

    # x == n
    assert module_0.is_simple_power(7, 7)
    assert module_0.is_simple_power(13, 13)

    # negative base
    assert module_0.is_simple_power(4, -2)
    assert module_0.is_simple_power(16, -2)
    assert not module_0.is_simple_power(8, -2)