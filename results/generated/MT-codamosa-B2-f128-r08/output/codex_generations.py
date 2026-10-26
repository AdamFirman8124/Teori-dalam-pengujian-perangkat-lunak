

# Generated at 2026-10-25 08:53:04.930789
# Unit test for function prod_signs

# Generated at 2026-10-25 08:53:07.349112
# Unit test for function prod_signs

# Generated at 2026-10-25 08:53:09.768878
# Unit test for function prod_signs

# Generated at 2026-10-25 08:53:12.184204
# Unit test for function prod_signs

# Generated at 2026-10-25 08:53:14.601139
# Unit test for function prod_signs

# Generated at 2026-10-25 08:53:17.019332
# Unit test for function prod_signs

# Generated at 2026-10-25 08:53:19.454778
# Unit test for function prod_signs

# Generated at 2026-10-25 08:53:21.869146
# Unit test for function prod_signs

# Generated at 2026-10-25 08:53:24.285728
# Unit test for function prod_signs

# Generated at 2026-10-25 08:53:26.709411
# Unit test for function prod_signs

# Generated at 2026-10-25 08:53:29.125066
# Unit test for function prod_signs

# Generated at 2026-10-25 08:53:31.544782
# Unit test for function prod_signs

# Generated at 2026-10-25 08:53:33.961024
# Unit test for function prod_signs

# Generated at 2026-10-25 08:53:45.259880
# Unit test for function prod_signs
def test_prod_signs():
    assert module_0.prod_signs([1, 2, 2, -4]) == -9
    assert module_0.prod_signs([0, 1]) == 0
    assert module_0.prod_signs([]) is None
    assert module_0.prod_signs([-1, -2, -3]) == -6
    assert module_0.prod_signs([2, 3, 4]) == 9
    assert module_0.prod_signs([-5]) == -5
    assert module_0.prod_signs([0, -1, -2, -3]) == 0