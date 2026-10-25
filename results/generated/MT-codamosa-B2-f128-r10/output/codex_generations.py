

# Generated at 2026-10-24 04:12:34.329972
# Unit test for function prod_signs
def test_prod_signs():
    assert module_0.prod_signs([1, 2, 3, 4]) == 10
    assert module_0.prod_signs([-1, -2, -3, -4]) == 10
    assert module_0.prod_signs([-1, -2, -3, 4]) == -10
    assert module_0.prod_signs([-1, 2, 3, 4]) == -10
    assert module_0.prod_signs([0, 1, 2, 3]) == 0
    assert module_0.prod_signs([0]) == 0
    assert module_0.prod_signs([]) is None

# Generated at 2026-10-24 04:12:42.727562
# Unit test for function prod_signs
def test_prod_signs():
    assert module_0.prod_signs([]) is None
    assert module_0.prod_signs([1, 2, 3, 4]) == 10
    assert module_0.prod_signs([-1, 2, 3, 4]) == -10
    assert module_0.prod_signs([-1, -2, 3, 4]) == 10
    assert module_0.prod_signs([-1, -2, -3, 4]) == -10
    assert module_0.prod_signs([0, 1, -2, 3]) == 0
    assert module_0.prod_signs([0]) == 0

# Generated at 2026-10-24 04:12:45.244756
# Unit test for function prod_signs

# Generated at 2026-10-24 04:12:50.103804
# Unit test for function prod_signs
def test_prod_signs():assert module_0.prod_signs([1, 2, 3, -4]) == -10

# Generated at 2026-10-24 04:12:55.377371
# Unit test for function prod_signs
def test_prod_signs():
    assert module_0.prod_signs([1, 2, 3, 4]) == 10
    assert module_0.prod_signs([-1, 2, 3, 4]) == -10
    assert module_0.prod_signs([-1, -2, 3, 4]) == 10
    assert module_0.prod_signs([-1, -2, -3, 4]) == -10
    assert module_0.prod_signs([1, 2, 0, -4]) == 0
    assert module_0.prod_signs([0]) == 0
    assert module_0.prod_signs([]) is None

# Generated at 2026-10-24 04:13:00.952212
# Unit test for function prod_signs
def test_prod_signs():
    assert module_0.prod_signs([]) is None
    assert module_0.prod_signs([1, 2, 3, 4]) == 10
    assert module_0.prod_signs([1, -2, 3, 4]) == -10
    assert module_0.prod_signs([-1, -2, 3, 4]) == 10
    assert module_0.prod_signs([-1, -2, -3, 4]) == -10
    assert module_0.prod_signs([1, -2, 0, 4]) == 0
    assert module_0.prod_signs([-5]) == -5
    assert module_0.prod_signs([5]) == 5