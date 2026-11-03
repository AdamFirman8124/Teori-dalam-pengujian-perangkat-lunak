

# Generated at 2026-11-02 22:56:00.405706
# Unit test for function simplify
def test_simplify():
    # Product results in a whole number
    assert module_0.simplify("1/5", "5/1") == True
    assert module_0.simplify("1/2", "2/1") == True
    assert module_0.simplify("2/4", "2/1") == True
    assert module_0.simplify("3/3", "3/1") == True
    assert module_0.simplify("1/3", "9/1") == True
    assert module_0.simplify("5/2", "4/5") == True
    assert module_0.simplify("10/4", "2/5") == True

    # Product does not result in a whole number
    assert module_0.simplify("1/6", "2/1") == False
    assert module_0.simplify("7/10", "10/2") == False
    assert module_0.simplify("1/4", "3/4") == False
    assert module_0.simplify("2/3", "5/7") == False
    assert module_0.simplify("1/7", "3/2") == False

    # Whole numbers as inputs
    assert module_0.simplify("4/1", "2/1") == True
    assert module_0.simplify("6/2", "1/3") == True

    # Larger numbers
    assert module_0.simplify("100/3", "3/100") == True
    assert module_0.simplify("999/1000", "1000/999") == True
    assert module_0.simplify("123/456", "789/101") == False

    # Zero numerator
    assert module_0.simplify("0/5", "5/1") == True

    print("All tests passed!")

test_simplify()

# Generated at 2026-11-02 22:59:25.299697
# Unit test for function simplify
def test_simplify():
    # Result is a whole number -> True
    assert module_0.simplify("1/2", "4/2") == True      # 1*4 / (2*2) = 4/4 = 1
    assert module_0.simplify("1/4", "4/1") == True      # 4/4 = 1
    assert module_0.simplify("2/3", "3/2") == True      # 6/6 = 1
    assert module_0.simplify("3/1", "1/3") == True      # 3/3 = 1
    assert module_0.simplify("0/2", "5/3") == True      # 0/6 = 0 (whole number)

    # Result is not a whole number -> False
    assert module_0.simplify("1/2", "2/4") == False     # 2/8 = 0.25
    assert module_0.simplify("1/3", "2/1") == False     # 2/3 is not whole
    assert module_0.simplify("3/4", "2/3") == False     # 6/12 = 0.5
    assert module_0.simplify("5/7", "1/3") == False     # 5/21 is not whole
    assert module_0.simplify("7/10", "10/3") == False   # 70/30 = 2.333...

    # Large numbers
    assert module_0.simplify("100/3", "3/100") == True  # 300/300 = 1
    assert module_0.simplify("123/456", "456/122") == False  # not whole