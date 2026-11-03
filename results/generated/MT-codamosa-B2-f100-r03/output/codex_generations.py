

# Generated at 2026-11-03 03:47:55.868978
# Unit test for function make_a_pile
def test_make_a_pile():
    # Basic cases
    assert module_0.make_a_pile(1) == [1]
    assert module_0.make_a_pile(2) == [2, 4]
    assert module_0.make_a_pile(3) == [3, 5, 7]
    assert module_0.make_a_pile(4) == [4, 6, 8, 10]

    # Edge case: n = 0 returns an empty list
    assert module_0.make_a_pile(0) == []

    # Larger values
    assert module_0.make_a_pile(5) == [5, 7, 9, 11, 13]
    assert module_0.make_a_pile(10) == [10, 12, 14, 16, 18, 20, 22, 24, 26, 28]

    # Property-based checks
    for n in range(1, 20):
        pile = module_0.make_a_pile(n)
        assert len(pile) == n                                   # length equals n
        assert pile[0] == n                                     # starts at n
        assert all(pile[i + 1] - pile[i] == 2 for i in range(n - 1))  # step of 2
        assert all(level % 2 == n % 2 for level in pile)        # parity matches n

    print("All tests passed!")


if __name__ == "__main__":
    test_make_a_pile()

# Generated at 2026-11-03 03:49:59.672195
# Unit test for function make_a_pile
def test_make_a_pile():
    # Basic test cases
    assert module_0.make_a_pile(3) == [3, 5, 7]
    assert module_0.make_a_pile(1) == [1]
    assert module_0.make_a_pile(2) == [2, 4]

    # Edge case: empty pile
    assert module_0.make_a_pile(0) == []

    # Verify length matches n
    assert len(module_0.make_a_pile(5)) == 5

    # Verify arithmetic progression with step 2 starting at n
    result = module_0.make_a_pile(4)
    assert result == [4, 6, 8, 10]

    # Verify each element increments by 2
    for i in range(1, len(result)):
        assert result[i] - result[i-1] == 2

    # Verify first element equals n
    assert result[0] == 4

    # Larger input
    assert module_0.make_a_pile(10)[-1] == 28  # last element = n + 2*(n-1) = 10 + 18

    print("All tests passed!")


if __name__ == "__main__":
    test_make_a_pile()

# Generated at 2026-11-03 03:51:51.801425
# Unit test for function make_a_pile
def test_make_a_pile():
    # Basic case: n = 3 -> [3, 5, 7]
    assert module_0.make_a_pile(3) == [3, 5, 7]

    # Smallest non-trivial case: n = 1 -> [1]
    assert module_0.make_a_pile(1) == [1]

    # Edge case: n = 0 -> empty list
    assert module_0.make_a_pile(0) == []

    # Even n: n = 4 -> [4, 6, 8, 10]
    assert module_0.make_a_pile(4) == [4, 6, 8, 10]

    # Larger case: n = 5 -> [5, 7, 9, 11, 13]
    assert module_0.make_a_pile(5) == [5, 7, 9, 11, 13]

    # Property check: length of result equals n
    for n in range(0, 10):
        result = module_0.make_a_pile(n)
        assert len(result) == n

    # Property check: first element is n, last element is n + 2*(n-1)
    for n in range(1, 10):
        result = module_0.make_a_pile(n)
        assert result[0] == n
        assert result[-1] == n + 2 * (n - 1)

    # Property check: consecutive elements differ by 2
    for n in range(2, 10):
        result = module_0.make_a_pile(n)
        for i in range(1, n):
            assert result[i] - result[i - 1] == 2

    print("All tests passed!")


if __name__ == "__main__":
    test_make_a_pile()

# Generated at 2026-11-03 03:54:27.248809
# Unit test for function make_a_pile
def test_make_a_pile():
    # Test with n = 1
    assert module_0.make_a_pile(1) == [1]
    
    # Test with n = 3
    assert module_0.make_a_pile(3) == [3, 5, 7]
    
    # Test with n = 5
    assert module_0.make_a_pile(5) == [5, 7, 9, 11, 13]
    
    # Test with n = 0 (edge case)
    assert module_0.make_a_pile(0) == []
    
    # Test with even n
    assert module_0.make_a_pile(4) == [4, 6, 8, 10]
    
    # Verify result length equals n
    result = module_0.make_a_pile(6)
    assert len(result) == 6
    
    # Verify each element follows the pattern n + 2*i
    n = 7
    result = module_0.make_a_pile(n)
    for i in range(n):
        assert result[i] == n + 2 * i
    
    print("All tests passed!")


if __name__ == "__main__":
    test_make_a_pile()

# Generated at 2026-11-03 03:55:57.459939
# Unit test for function make_a_pile
def test_make_a_pile():
    # Test with n = 1
    assert module_0.make_a_pile(1) == [1]
    
    # Test with n = 2
    assert module_0.make_a_pile(2) == [2, 4]
    
    # Test with n = 3
    assert module_0.make_a_pile(3) == [3, 5, 7]
    
    # Test with n = 5
    assert module_0.make_a_pile(5) == [5, 7, 9, 11, 13]
    
    # Test with n = 6
    assert module_0.make_a_pile(6) == [6, 8, 10, 12, 14, 16]
    
    # Test with n = 0 (empty pile)
    assert module_0.make_a_pile(0) == []
    
    # Test that the length of the result equals n
    assert len(module_0.make_a_pile(10)) == 10
    
    # Test that the first level equals n
    assert module_0.make_a_pile(7)[0] == 7
    
    # Test that levels increase by 2 each step
    pile = module_0.make_a_pile(4)
    for i in range(1, len(pile)):
        assert pile[i] - pile[i - 1] == 2
    
    # Test that all levels are even when n is even
    assert all(level % 2 == 0 for level in module_0.make_a_pile(8))
    
    # Test that all levels are odd when n is odd
    assert all(level % 2 == 1 for level in module_0.make_a_pile(9))
    
    # Test with a larger value
    assert module_0.make_a_pile(20)[19] == 20 + 2 * 19  # last element
    
    print("All tests passed!")


test_make_a_pile()