

# Generated at 2026-10-25 05:25:41.618446
# Unit test for function prod_signs
def test_prod_signs():
    assert module_0.prod_signs([1, 2, 3, 4]) == 10
    assert module_0.prod_signs([1, 2, -3, 4]) == -10
    assert module_0.prod_signs([-1, -2, -3, -4]) == 10
    assert module_0.prod_signs([-1, -2, -3]) == -6
    assert module_0.prod_signs([1, 2, 0, -4]) == 0
    assert module_0.prod_signs([5]) == 5
    assert module_0.prod_signs([-5]) == -5
    assert module_0.prod_signs([]) is None

# Generated at 2026-10-25 05:25:47.047537
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

# Generated at 2026-10-25 05:25:51.424694
# Unit test for function prod_signs
def test_prod_signs():
    assert module_0.prod_signs([1, 2, 3, 4]) == 10
    assert module_0.prod_signs([-1, 2, 3, 4]) == -10
    assert module_0.prod_signs([-1, -2, 3, 4]) == 10
    assert module_0.prod_signs([1, 2, 0, -4]) == 0
    assert module_0.prod_signs([-5]) == -5
    assert module_0.prod_signs([]) is None

# Generated at 2026-10-25 05:25:57.105640
# Unit test for function prod_signs
def test_prod_signs():
    assert module_0.prod_signs([]) is None
    assert module_0.prod_signs([1, 2, 3, 4]) == 10
    assert module_0.prod_signs([-1, 2, 3, 4]) == -10
    assert module_0.prod_signs([-1, -2, 3, 4]) == 10
    assert module_0.prod_signs([-1, -2, -3]) == -6
    assert module_0.prod_signs([1, 0, -3]) == 0
    assert module_0.prod_signs([5]) == 5
    assert module_0.prod_signs([-5]) == -5

# Generated at 2026-10-25 05:26:01.686947
# Unit test for function prod_signs
def test_prod_signs():
    assert module_0.prod_signs([1, 2, 3, 4]) == 10
    assert module_0.prod_signs([-1, 2, 3, 4]) == -10
    assert module_0.prod_signs([-1, -2, 3, 4]) == 10
    assert module_0.prod_signs([1, 2, 0, -4]) == 0
    assert module_0.prod_signs([-1]) == -1
    assert module_0.prod_signs([0]) == 0
    assert module_0.prod_signs([]) is None