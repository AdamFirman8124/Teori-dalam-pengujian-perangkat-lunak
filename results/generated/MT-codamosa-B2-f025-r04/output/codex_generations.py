

# Generated at 2026-11-02 16:47:31.954500
# Unit test for function factorize
def test_factorize():
    # Basic factorizations
    assert module_0.factorize(8) == [2, 2, 2]
    assert module_0.factorize(25) == [2, 2] or module_0.factorize(25) == [5, 5]
    assert module_0.factorize(70) == [2, 5, 7]
    assert module_0.factorize(100) == [2, 2, 5, 5]
    assert module_0.factorize(2 * 3 * 5 * 7 * 11) == [2, 3, 5, 7, 11]

    # Prime numbers
    assert module_0.factorize(2) == [2]
    assert module_0.factorize(3) == [3]
    assert module_0.factorize(13) == [13]
    assert module_0.factorize(97) == [97]

    # Edge cases
    assert module_0.factorize(1) == []
    assert module_0.factorize(4) == [2, 2]

    # Property check: product of factors equals original number
    for n in [12, 360, 9973, 1024, 6469693230]:
        result = module_0.factorize(n)
        product = 1
        for f in result:
            product *= f
        assert product == n, f"Product of factors of {n} is wrong"

    # Factors must be non-decreasing (trial division order)
    result = module_0.factorize(2 ** 10 * 3 ** 5)
    assert result == sorted(result)

    print("All tests passed!")


test_factorize()

# Generated at 2026-11-02 16:52:36.308416
# Unit test for function factorize
def test_factorize():import math

    # Simple cases