

# Generated at 2026-10-25 12:13:58.182022
# Unit test for function below_zero
def test_below_zero():
    # never goes below zero
    assert module_0.below_zero([]) == False
    assert module_0.below_zero([1, 2, 3]) == False
    assert module_0.below_zero([0, 0, 0]) == False
    assert module_0.below_zero([1, -1]) == False
    assert module_0.below_zero([10, -5, -5]) == False

    # goes below zero
    assert module_0.below_zero([-1]) == True
    assert module_0.below_zero([1, -2]) == True
    assert module_0.below_zero([5, -10, 5]) == True
    assert module_0.below_zero([10, -5, -6]) == True

# Generated at 2026-10-25 12:14:42.519900
# Unit test for function below_zero
def test_below_zero():
    # never goes below zero
    assert module_0.below_zero([]) == False
    assert module_0.below_zero([1, 2, 3]) == False
    assert module_0.below_zero([0, 0, 0]) == False
    assert module_0.below_zero([1, -1]) == False
    assert module_0.below_zero([10, -5, -5]) == False

    # goes below zero
    assert module_0.below_zero([-1]) == True
    assert module_0.below_zero([1, -2]) == True
    assert module_0.below_zero([5, -10, 5]) == True
    assert module_0.below_zero([10, -5, -6]) == True

# Generated at 2026-10-25 12:14:44.054601
# Unit test for function below_zero
def test_below_zero():
    # never goes below zero
    assert module_0.below_zero([]) == False
    assert module_0.below_zero([1, 2, 3]) == False
    assert module_0.below_zero([0, 0, 0]) == False
    assert module_0.below_zero([1, -1]) == False
    assert module_0.below_zero([10, -5, -5]) == False

    # goes below zero
    assert module_0.below_zero([-1]) == True
    assert module_0.below_zero([1, -2]) == True
    assert module_0.below_zero([5, -10, 5]) == True
    assert module_0.below_zero([10, -5, -6]) == True

# Generated at 2026-10-25 12:15:26.960344
# Unit test for function below_zero
def test_below_zero():
    assert module_0.below_zero([]) is False
    assert module_0.below_zero([1, 2, 3]) is False
    assert module_0.below_zero([-1]) is True
    assert module_0.below_zero([1, -2]) is True
    assert module_0.below_zero([1, -1]) is False
    assert module_0.below_zero([5, -3, -2]) is False
    assert module_0.below_zero([5, -6, 10]) is True

# Generated at 2026-10-25 12:16:14.661425
# Unit test for function below_zero

# Generated at 2026-10-25 12:16:32.908686
# Unit test for function below_zero
def test_below_zero():assert module_0.below_zero([1, 2, 3]) == False