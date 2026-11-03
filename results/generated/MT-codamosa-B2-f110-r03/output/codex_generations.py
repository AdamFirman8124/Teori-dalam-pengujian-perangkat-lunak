

# Generated at 2026-11-02 23:42:29.544892
# Unit test for function exchange
def test_exchange():
    # lst1 already all even -> YES regardless of lst2
    assert module_0.exchange([2, 4, 6], [1, 3, 5]) == "YES"
    assert module_0.exchange([2, 4, 6], []) == "YES"

    # lst1 all odd, lst2 has enough evens -> YES
    assert module_0.exchange([1, 3, 5], [2, 4, 6]) == "YES"
    assert module_0.exchange([1, 3, 5], [2]) == "YES"

    # lst1 has more odds than lst2 has evens -> NO
    assert module_0.exchange([1, 3, 5], []) == "NO"
    assert module_0.exchange([1, 3, 5, 7], [2]) == "NO"

    # mixed lists
    assert module_0.exchange([1, 2, 3, 4], [1, 2, 3, 4]) == "YES"  # 2 odds, 2 evens
    assert module_0.exchange([1, 2, 3], [5, 7]) == "NO"            # 2 odds, 0 evens
    assert module_0.exchange([1, 2], [4, 6, 8]) == "YES"           # 1 odd, 3 evens

    # empty lists
    assert module_0.exchange([], []) == "YES"
    assert module_0.exchange([], [1, 3]) == "YES"

    # single elements
    assert module_0.exchange([1], [2]) == "YES"
    assert module_0.exchange([1], [3]) == "NO"
    assert module_0.exchange([0], [1]) == "YES"

    # negative numbers: -3 % 2 == 1 in Python, -2 % 2 == 0
    assert module_0.exchange([-3, -5], [-2, -4]) == "YES"
    assert module_0.exchange([-2, -4], [-3, -5]) == "YES"

    # zero counts as even
    assert module_0.exchange([1], [0]) == "YES"

    # larger inputs
    assert module_0.exchange([1] * 10, [2] * 10) == "YES"
    assert module_0.exchange([1] * 10, [2] * 9) == "NO"

    # duplicates
    assert module_0.exchange([1, 1, 1], [2, 2, 2, 2]) == "YES"
    assert module_0.exchange([1, 1, 1, 1], [2, 2, 2]) == "NO"

    print("All test_exchange tests passed!")


if __name__ == "__main__":
    unittest.main(exit=False)
    test_exchange()

# Generated at 2026-11-02 23:44:09.226415
# Unit test for function exchange
def test_exchange():
    # odd count in lst1 equals even count in lst2 -> YES
    assert module_0.exchange([1, 2, 3, 4], [1, 2, 3, 4]) == "YES"
    # more odds in lst1 than evens in lst2 -> NO
    assert module_0.exchange([1, 3, 5], [2]) == "NO"
    # no odd numbers in lst1 -> YES
    assert module_0.exchange([2, 4, 6], [1, 3]) == "YES"
    # no even numbers in lst2 but lst1 has odds -> NO
    assert module_0.exchange([1], [1, 3]) == "NO"
    # equal counts of odds and evens -> YES
    assert module_0.exchange([1, 3], [2, 4]) == "YES"
    # both lists empty -> YES
    assert module_0.exchange([], []) == "YES"
    # lst1 empty, lst2 has evens -> YES
    assert module_0.exchange([], [2, 4]) == "YES"
    # lst1 has odds, lst2 empty -> NO
    assert module_0.exchange([1], []) == "NO"
    # negative numbers: -1 is odd, -2 is even -> YES
    assert module_0.exchange([-1], [-2]) == "YES"
    # single element lists -> YES
    assert module_0.exchange([1], [2]) == "YES"

# Generated at 2026-11-02 23:45:26.846556
# Unit test for function exchange
def test_exchange():
    assert module_0.exchange([1, 2, 3, 4], [1, 2, 3, 4]) == "YES"
    assert module_0.exchange([1, 2, 3, 4], [1, 5, 3, 4]) == "NO"
    assert module_0.exchange([1, 3, 5], [2, 4, 6]) == "YES"
    assert module_0.exchange([5], [2]) == "YES"
    assert module_0.exchange([1], [3]) == "NO"
    assert module_0.exchange([], []) == "YES"
    assert module_0.exchange([2, 4, 6], [1, 3, 5]) == "YES"
    assert module_0.exchange([1, 2, 3], [1, 2, 3]) == "NO"
    assert module_0.exchange([7, 8, 9], [2, 4, 10]) == "YES"
    assert module_0.exchange([1, 1, 1, 1], [2, 2]) == "NO"
    assert module_0.exchange([0, 1, 2], [2]) == "YES"
    print("All test_exchange tests passed!")

test_exchange()

# Generated at 2026-11-02 23:46:28.378995
# Unit test for function exchange
def test_exchange():
    # YES cases: lst2 has enough even numbers to swap out odd numbers in lst1
    assert module_0.exchange([1, 2, 3, 4], [1, 2, 3, 4]) == "YES"
    assert module_0.exchange([1, 3, 5], [2, 4, 6]) == "YES"
    assert module_0.exchange([1, 2, 3], [2, 4]) == "YES"
    assert module_0.exchange([1], [2]) == "YES"
    assert module_0.exchange([5, 7, 9], [8, 10, 12, 14]) == "YES"

    # NO cases: not enough even numbers in lst2
    assert module_0.exchange([1, 3, 5], [1, 3, 5]) == "NO"
    assert module_0.exchange([1, 3], [2]) == "NO"
    assert module_0.exchange([1, 2, 3, 4, 5], [2]) == "NO"
    assert module_0.exchange([1], [1]) == "NO"
    assert module_0.exchange([7, 11], []) == "NO"

    # Edge cases: empty lists
    assert module_0.exchange([], []) == "YES"
    assert module_0.exchange([], [1, 3]) == "YES"
    assert module_0.exchange([2, 4], []) == "YES"

    # All even in lst1 (no odd numbers to swap)
    assert module_0.exchange([2, 4, 6], [1, 3]) == "YES"

    # Negative numbers
    assert module_0.exchange([-1, -3], [-2, -4]) == "YES"
    assert module_0.exchange([-1, -3], [-1, -3]) == "NO"

    # Zero is even
    assert module_0.exchange([1], [0]) == "YES"

    print("All tests passed!")


if __name__ == "__main__":
    test_exchange()

# Generated at 2026-11-02 23:47:52.153681
# Unit test for function exchange
def test_exchange():
    # lst1 already contains all even numbers -> "YES"
    assert module_0.exchange([2, 4, 6], [1, 3, 5]) == "YES"

    # lst1 has odds, lst2 has enough evens to swap -> "YES"
    assert module_0.exchange([1, 2, 3, 4], [2, 4, 6, 8]) == "YES"

    # lst2 lacks enough even numbers -> "NO"
    assert module_0.exchange([1, 3, 5], [2]) == "NO"

    # exactly enough even numbers in lst2 -> "YES"
    assert module_0.exchange([1, 3], [2, 4]) == "YES"

    # no odd numbers in lst1 -> "YES" regardless of lst2
    assert module_0.exchange([2, 4], [1, 3]) == "YES"

    # empty lst1 -> "YES"
    assert module_0.exchange([], [1, 2]) == "YES"

    # lst1 has odds but lst2 is empty -> "NO"
    assert module_0.exchange([1], []) == "NO"

    # both lists empty -> "YES"
    assert module_0.exchange([], []) == "YES"

    # negative odd/even numbers
    assert module_0.exchange([-1, -3], [-2, -4]) == "YES"
    assert module_0.exchange([-1, -3], [2]) == "NO"

    # zero counts as even in lst2
    assert module_0.exchange([1], [0]) == "YES"

    # equal counts of odds in lst1 and evens in lst2 -> "YES"
    assert module_0.exchange([1, 3, 5], [2, 4, 6]) == "YES"

    # more odds in lst1 than evens in lst2 -> "NO"
    assert module_0.exchange([1, 3, 5], [2, 4]) == "NO"

    # mixed values with duplicates
    assert module_0.exchange([1, 1, 1], [2, 2, 2, 2]) == "YES"
    assert module_0.exchange([1, 1, 1], [2, 2]) == "NO"