

# Generated at 2026-10-24 05:04:30.785391
# Unit test for function prod_signs
def test_prod_signs():
    assert module_0.prod_signs([]) is None
    assert module_0.prod_signs([1, 2, 3]) == 6
    assert module_0.prod_signs([-1, 2, 3]) == -6
    assert module_0.prod_signs([-1, -2, 3]) == 6
    assert module_0.prod_signs([0, 1, -2]) == 0
    assert module_0.prod_signs([-5]) == -5
    assert module_0.prod_signs([0]) == 0

# Generated at 2026-10-24 05:04:36.521093
# Unit test for function prod_signs
def test_prod_signs():
    assert module_0.prod_signs([]) is None
    assert module_0.prod_signs([1, 2, 3, 4]) == 10
    assert module_0.prod_signs([-1, 2, 3, 4]) == -10
    assert module_0.prod_signs([-1, -2, 3, 4]) == 10
    assert module_0.prod_signs([-1, -2, -3, 4]) == -10
    assert module_0.prod_signs([0, -1, 2, 3]) == 0
    assert module_0.prod_signs([-5]) == -5
    assert module_0.prod_signs([5]) == 5

# Generated at 2026-10-24 05:04:42.079870
# Unit test for function prod_signs
def test_prod_signs():
    assert module_0.prod_signs([]) is None
    assert module_0.prod_signs([1, 2, 3, 4]) == 10
    assert module_0.prod_signs([-1, 2, 3, 4]) == -10
    assert module_0.prod_signs([-1, -2, 3, 4]) == 10
    assert module_0.prod_signs([-1, -2, -3, 4]) == -10
    assert module_0.prod_signs([0, 1, -2, 3]) == 0
    assert module_0.prod_signs([5]) == 5
    assert module_0.prod_signs([-5]) == -5

# Generated at 2026-10-24 05:04:47.888714
# Unit test for function prod_signs
def test_prod_signs():
    assert module_0.prod_signs([]) is None
    assert module_0.prod_signs([1, 2, 3, 4]) == 10
    assert module_0.prod_signs([-1, 2, 3, 4]) == -10
    assert module_0.prod_signs([-1, -2, 3, 4]) == 10
    assert module_0.prod_signs([-1, -2, -3]) == -6
    assert module_0.prod_signs([1, -2, 0, 4]) == 0
    assert module_0.prod_signs([0]) == 0

# Generated at 2026-10-24 05:04:55.109140
# Unit test for function prod_signs
def test_prod_signs():
    assert module_0.prod_signs([]) is None
    assert module_0.prod_signs([1, 2, 3, 4]) == 10
    assert module_0.prod_signs([-1, 2, 3, 4]) == -10
    assert module_0.prod_signs([-1, -2, 3, 4]) == 10
    assert module_0.prod_signs([-1, -2, -3]) == -6
    assert module_0.prod_signs([0, 1, -2, 3]) == 0
    assert module_0.prod_signs([5]) == 5
    assert module_0.prod_signs([-5]) == -5