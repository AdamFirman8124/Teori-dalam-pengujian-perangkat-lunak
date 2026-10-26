

# Generated at 2026-10-25 14:18:40.589651
# Unit test for function count_up_to
def test_count_up_to():
    # basic case: primes strictly below n
    assert module_0.count_up_to(10) == [2, 3, 5, 7]

    # n itself is excluded (range(2, n))
    assert module_0.count_up_to(11) == [2, 3, 5, 7]
    assert module_0.count_up_to(12) == [2, 3, 5, 7, 11]

    # smallest non-empty result
    assert module_0.count_up_to(3) == [2]

    # empty results: nothing below 2, and nothing for tiny/negative n
    assert module_0.count_up_to(2) == []
    assert module_0.count_up_to(1) == []
    assert module_0.count_up_to(0) == []
    assert module_0.count_up_to(-5) == []

    # every returned value is prime and < n; nothing is missed
    n = 50
    result = module_0.count_up_to(n)
    assert all(i < n for i in result)
    assert all(i % d for i in result for d in range(2, i))  # no divisor found
    assert result == sorted(set(result))                    # no dups, ascending
    assert result[-1] == 47

    # 2 is the only even prime -> catches an i % 2 shortcut bug
    assert module_0.count_up_to(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    print("all assertions passed")


if __name__ == "__main__":
    test_count_up_to()

# Generated at 2026-10-25 14:18:46.834160
# Unit test for function count_up_to
def test_count_up_to():
    assert module_0.count_up_to(10) == [2, 3, 5, 7]
    assert module_0.count_up_to(3) == [2]
    assert module_0.count_up_to(2) == []
    assert module_0.count_up_to(1) == []
    assert module_0.count_up_to(20) == [2, 3, 5, 7, 11, 13, 17]

# Generated at 2026-10-25 14:18:57.382242
# Unit test for function count_up_to
def test_count_up_to():
    assert module_0.count_up_to(10) == [2, 3, 5, 7]
    assert module_0.count_up_to(3) == [2]
    assert module_0.count_up_to(2) == []
    assert module_0.count_up_to(0) == []

# Generated at 2026-10-25 14:19:03.116753
# Unit test for function count_up_to
def test_count_up_to():
    assert module_0.count_up_to(1) == []
    assert module_0.count_up_to(2) == []
    assert module_0.count_up_to(3) == [2]
    assert module_0.count_up_to(10) == [2, 3, 5, 7]
    assert module_0.count_up_to(20) == [2, 3, 5, 7, 11, 13, 17, 19]

# Generated at 2026-10-25 14:19:08.444398
# Unit test for function count_up_to
def test_count_up_to():
    assert module_0.count_up_to(10) == [2, 3, 5, 7]
    assert module_0.count_up_to(3) == [2]
    assert module_0.count_up_to(2) == []
    assert module_0.count_up_to(1) == []