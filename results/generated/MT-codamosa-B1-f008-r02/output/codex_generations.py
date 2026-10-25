

# Generated at 2026-10-24 21:55:38.804202
# Unit test for function sum_product

# Generated at 2026-10-24 21:55:41.223173
# Unit test for function sum_product

# Generated at 2026-10-24 21:55:43.791231
# Unit test for function sum_product

# Generated at 2026-10-24 21:55:46.209307
# Unit test for function sum_product

# Generated at 2026-10-24 21:55:48.628971
# Unit test for function sum_product

# Generated at 2026-10-24 21:55:51.046397
# Unit test for function sum_product

# Generated at 2026-10-24 21:55:53.465949
# Unit test for function sum_product

# Generated at 2026-10-24 21:55:55.884583
# Unit test for function sum_product

# Generated at 2026-10-24 21:55:58.304895
# Unit test for function sum_product

# Generated at 2026-10-24 21:56:00.722896
# Unit test for function sum_product

# Generated at 2026-10-24 21:56:03.136283
# Unit test for function sum_product

# Generated at 2026-10-24 21:56:07.278239
# Unit test for function sum_product
def test_sum_product():
    assert module_0.sum_product([]) == (0, 1)
    assert module_0.sum_product([1, 2, 3]) == (6, 6)
    assert module_0.sum_product([1, 2, 3, 4]) == (10, 24)
    assert module_0.sum_product([5]) == (5, 5)
    assert module_0.sum_product([-1, 2, -3]) == (-2, 6)
    assert module_0.sum_product([0, 1, 2, 3]) == (6, 0)

# Generated at 2026-10-24 21:56:13.424758
# Unit test for function sum_product
def test_sum_product():
    assert module_0.sum_product([1, 2, 3, 4]) == (10, 24)
    assert module_0.sum_product([-1, 2, -3]) == (-2, 6)
    assert module_0.sum_product([0, 2, 3]) == (5, 0)
    assert module_0.sum_product([5]) == (5, 5)
    assert module_0.sum_product([]) == (0, 1)