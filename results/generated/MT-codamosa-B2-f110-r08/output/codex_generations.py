

# Generated at 2026-11-02 21:22:39.750944
# Unit test for function exchange
def test_exchange():
    # lst1 already contains all even numbers
    assert module_0.exchange([2, 4, 6], [1, 3, 5]) == "YES"
    # lst2 has enough even numbers to swap for odd ones in lst1
    assert module_0.exchange([1, 2, 3, 4], [2, 4, 6]) == "YES"
    # lst2 does not have enough even numbers
    assert module_0.exchange([1, 3, 5], [2, 4]) == "NO"
    # exact count match
    assert module_0.exchange([1, 3], [2, 4]) == "YES"
    # empty lst1 (nothing to fix)
    assert module_0.exchange([], [1, 2, 3]) == "YES"
    # empty lst2 but lst1 has odd numbers
    assert module_0.exchange([1, 2], []) == "NO"
    # both lists empty
    assert module_0.exchange([], []) == "YES"
    # zero counts as even
    assert module_0.exchange([0, 1], [0]) == "YES"
    # negative numbers: -1 % 2 == 1 in Python, so treated as odd
    assert module_0.exchange([-1, -3], [-2, -4]) == "YES"
    assert module_0.exchange([-1, -3], [1, 3]) == "NO"
    # single element lists
    assert module_0.exchange([1], [2]) == "YES"
    assert module_0.exchange([1], [3]) == "NO"
    assert module_0.exchange([2], [1]) == "YES"
    # larger mixed case
    assert module_0.exchange([1, 3, 5, 7, 8], [2, 4, 6, 8, 10]) == "YES"
    assert module_0.exchange([1, 3, 5, 7, 9], [2, 4, 6, 8, 10, 12]) == "YES"

# Generated at 2026-11-02 21:25:05.693290
# Unit test for function exchange
def test_exchange():
    # lst1 all even -> YES
    assert module_0.exchange([2, 4, 6], [1, 3, 5]) == "YES"

    # lst1 has odd elements, lst2 has enough even to cover -> YES
    assert module_0.exchange([1, 2, 3, 4], [1, 2, 3, 4]) == "YES"
    assert module_0.exchange([1, 3], [2, 4]) == "YES"

    # lst2 lacks enough even elements -> NO
    assert module_0.exchange([1, 2, 3, 4], [1, 5, 3, 4]) == "NO"
    assert module_0.exchange([1, 3, 5], [2, 4]) == "NO"
    assert module_0.exchange([1, 3], [2]) == "NO"

    # empty lst1 -> trivially YES
    assert module_0.exchange([], [1, 2]) == "YES"

    # empty lst2 with odd in lst1 -> NO
    assert module_0.exchange([1], []) == "NO"

    # negative numbers: negative odds count as odd
    assert module_0.exchange([-3, 2], [-2, 4]) == "YES"
    assert module_0.exchange([-3, -5], [-2]) == "NO"

    # zero is even
    assert module_0.exchange([1, 3, 5], [0, 2, 4]) == "YES"

    # large numbers
    assert module_0.exchange([1000001], [1000000]) == "YES"

    # mixed: odd count equals even count -> YES
    assert module_0.exchange([1, 3, 5], [0, 2, 4]) == "YES"

# Generated at 2026-11-02 21:27:11.339849
# Unit test for function exchange
def test_exchange():import pytest


def test_exchange_sufficient_evens():
    # lst1 has 2 odd numbers, lst2 has 2 even numbers -> enough to exchange
    assert module_0.exchange([1, 3, 2], [2, 4]) == "YES"


def test_exchange_insufficient_evens():
    # lst1 has 2 odd numbers, lst2 has only 1 even number -> not enough
    assert module_0.exchange([1, 3, 2], [3, 4]) == "NO"


def test_exchange_no_odds_in_lst1():
    # lst1 has no odd numbers, no exchange needed
    assert module_0.exchange([2, 4, 6], [1, 3]) == "YES"


def test_exchange_all_odd_in_lst1():
    # lst1 all odd, lst2 all even -> plenty of evens
    assert module_0.exchange([1, 3, 5], [2, 4, 6]) == "YES"


def test_exchange_all_odd_in_both():
    # lst1 all odd, lst2 has no evens -> cannot exchange
    assert module_0.exchange([1, 3, 5], [1, 3, 5]) == "NO"


def test_exchange_equal_counts():
    # equal number of odds in lst1 and evens in lst2 -> "YES"
    assert module_0.exchange([1, 3], [2, 4]) == "YES"


def test_exchange_empty_lst1():
    # empty lst1 means zero odds -> trivially "YES"
    assert module_0.exchange([], [1, 3, 5]) == "YES"


def test_exchange_empty_lst2():
    # empty lst2 provides no evens; fails if lst1 has any odd
    assert module_0.exchange([1, 2], []) == "NO"
    assert module_0.exchange([2, 4], []) == "YES"


def test_exchange_with_zero():
    # zero is even
    assert module_0.exchange([1], [0]) == "YES"


def test_exchange_negative_numbers():
    # negative odd numbers still count as odd
    assert module_0.exchange([-1, -3, 2], [-2, 4]) == "YES"
    assert module_0.exchange([-1, -3, 2], [-1, 4]) == "NO"


def test_exchange_single_elements():
    assert module_0.exchange([1], [2]) == "YES"
    assert module_0.exchange([1], [1]) == "NO"
    assert module_0.exchange([2], [1]) == "YES"


def test_exchange_more_evens_than_odds():
    # surplus of evens in lst2
    assert module_0.exchange([1, 2, 3], [2, 4, 6, 8, 10]) == "YES"

# Generated at 2026-11-02 21:28:51.923324
# Unit test for function exchange
def test_exchange():
    # lst1 already all even
    assert module_0.exchange([2, 4, 6], [1, 3, 5]) == "YES"
    # enough even numbers in lst2 to swap out odds in lst1
    assert module_0.exchange([1, 2, 3, 4], [2, 4, 6]) == "YES"
    # not enough even numbers in lst2
    assert module_0.exchange([1, 3, 5], [2, 4]) == "NO"
    # lst2 has no even numbers
    assert module_0.exchange([1, 3], [1, 3, 5]) == "NO"
    # lst1 has no odd numbers (empty exchange needed)
    assert module_0.exchange([], [1, 2, 3]) == "YES"
    # both lists empty
    assert module_0.exchange([], []) == "YES"
    # exact match of even count to odd count
    assert module_0.exchange([1, 3, 5], [2, 4, 6]) == "YES"
    # one odd needs one even
    assert module_0.exchange([1], [2]) == "YES"
    # negative numbers: -3 is odd, -2 is even
    assert module_0.exchange([-3, -5], [-2, -4]) == "YES"
    assert module_0.exchange([-3, -5], [-1, -3]) == "NO"
    # zero is even
    assert module_0.exchange([1, 1, 1], [0, 0, 0]) == "YES"
    assert module_0.exchange([1, 1, 1], [0, 1, 3]) == "NO"
    # large numbers
    assert module_0.exchange([1000001], [1000000]) == "YES"
    # duplicates
    assert module_0.exchange([1, 1, 2], [4, 4]) == "YES"
    assert module_0.exchange([1, 1, 2], [4]) == "NO"
    # more evens than odds in lst2
    assert module_0.exchange([1], [2, 4, 6, 8]) == "YES"

    print("All test_exchange tests passed!")


if __name__ == "__main__":
    test_exchange()

# Generated at 2026-11-02 21:30:08.190278
# Unit test for function exchange
def test_exchange():
    # odd count in lst1 <= even count in lst2 -> YES
    assert module_0.exchange([1, 2, 3, 4], [1, 2, 3, 4]) == "YES"
    assert module_0.exchange([1, 2, 3], [1, 2, 3, 4]) == "YES"
    assert module_0.exchange([1, 3, 5], [2, 4, 6]) == "YES"
    assert module_0.exchange([1], [2]) == "YES"

    # odd count in lst1 > even count in lst2 -> NO
    assert module_0.exchange([1, 2, 3, 4], [1, 5]) == "NO"
    assert module_0.exchange([1, 3, 5, 7], [2, 4]) == "NO"
    assert module_0.exchange([1], []) == "NO"

    # empty lists
    assert module_0.exchange([], []) == "YES"
    assert module_0.exchange([], [1, 2]) == "YES"

    # lst1 already all even
    assert module_0.exchange([2, 4, 6], [1, 3]) == "YES"
    assert module_0.exchange([0, 2], [1]) == "YES"

    # negative numbers
    assert module_0.exchange([-1, -3], [-2, -4]) == "YES"
    assert module_0.exchange([-1, -3, -5], [-2]) == "NO"

    print("All test_exchange tests passed!")


test_exchange()