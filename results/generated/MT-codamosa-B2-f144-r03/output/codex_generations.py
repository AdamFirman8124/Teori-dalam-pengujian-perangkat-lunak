

# Generated at 2026-11-02 13:41:56.821783
# Unit test for function simplify
def test_simplify():
    # Product simplifies to a whole number
    assert module_0.simplify("1/2", "2/1") == True
    assert module_0.simplify("1/3", "3/1") == True
    assert module_0.simplify("2/4", "2/2") == True

    # Product does not simplify to a whole number
    assert module_0.simplify("1/2", "1/2") == False
    assert module_0.simplify("7/26", "11/26") == False
    assert module_0.simplify("3/4", "5/6") == False

    # Zero numerator always simplifies to whole number
    assert module_0.simplify("0/5", "3/7") == True

    # Larger numbers
    assert module_0.simplify("100/3", "3/100") == True
    assert module_0.simplify("100/3", "3/101") == False

    # Negative values
    assert module_0.simplify("-1/2", "4/1") == True
    assert module_0.simplify("-1/2", "3/1") == False

    print("All test_simplify tests passed!")

test_simplify()

# Generated at 2026-11-02 13:42:31.990275
# Unit test for function simplify
def test_simplify():
    # Whole number products -> True
    assert module_0.simplify("1/5", "5/1") == True       # 1/5 * 5/1 = 1
    assert module_0.simplify("3/4", "4/3") == True       # 3/4 * 4/3 = 1
    assert module_0.simplify("2/3", "3/2") == True       # 2/3 * 3/2 = 1
    assert module_0.simplify("4/2", "2/1") == True       # 4/2 * 2/1 = 4
    assert module_0.simplify("5/1", "1/5") == True       # 5/1 * 1/5 = 1
    assert module_0.simplify("6/3", "1/2") == True       # 6/3 * 1/2 = 1
    assert module_0.simplify("10/4", "2/5") == True      # 10/4 * 2/5 = 1

    # Non-whole products -> False
    assert module_0.simplify("1/6", "2/1") == False      # 1/6 * 2/1 = 1/3
    assert module_0.simplify("7/10", "10/2") == False    # 7/10 * 10/2 = 7/2
    assert module_0.simplify("1/2", "1/2") == False      # 1/2 * 1/2 = 1/4
    assert module_0.simplify("3/7", "2/5") == False      # 3/7 * 2/5 = 6/35
    assert module_0.simplify("1/3", "5/2") == False      # 1/3 * 5/2 = 5/6

    # Zero numerator yields whole number 0
    assert module_0.simplify("0/1", "3/7") == True

    # Negative numerators
    assert module_0.simplify("-1/2", "2/1") == True      # -1/2 * 2/1 = -1
    assert module_0.simplify("-1/3", "2/1") == False     # -1/3 * 2/1 = -2/3

# Generated at 2026-11-02 13:43:06.353416
# Unit test for function simplify
def test_simplify():
# nonce:3320b8ba
    # Product is a whole number
    assert module_0.simplify("1/2", "2/2") == True
    assert module_0.simplify("2/3", "3/2") == True
    assert module_0.simplify("1/2", "4/1") == True
    assert module_0.simplify("3/4", "4/3") == True

    # Product is not a whole number
    assert module_0.simplify("1/2", "3/4") == False
    assert module_0.simplify("1/2", "1/2") == False
    assert module_0.simplify("2/3", "4/5") == False
    assert module_0.simplify("5/7", "3/2") == False

    # Zero numerator yields whole number 0
    assert module_0.simplify("0/5", "3/4") == True

    # Negative fractions
    assert module_0.simplify("-1/2", "2/1") == True
    assert module_0.simplify("-1/2", "-2/1") == True
    assert module_0.simplify("-1/2", "3/4") == False

    # Larger values
    assert module_0.simplify("100/3", "3/100") == True
    assert module_0.simplify("100/7", "2/3") == False

# Generated at 2026-11-02 13:43:28.650192
# Unit test for function simplify
def test_simplify():
    # Result is a whole number
    assert module_0.simplify("1/2", "2/1") == True      # 1/2 * 2/1 = 1
    assert module_0.simplify("3/2", "2/3") == True      # 3/2 * 2/3 = 1
    assert module_0.simplify("4/2", "2/1") == True      # 4/2 * 2/1 = 4
    assert module_0.simplify("1/1", "5/1") == True      # 1/1 * 5/1 = 5
    assert module_0.simplify("10/2", "3/5") == True     # 10/2 * 3/5 = 3

    # Result is not a whole number
    assert module_0.simplify("1/2", "1/3") == False     # 1/2 * 1/3 = 1/6
    assert module_0.simplify("1/4", "1/2") == False     # 1/4 * 1/2 = 1/8
    assert module_0.simplify("2/3", "3/4") == False     # 2/3 * 3/4 = 1/2
    assert module_0.simplify("5/7", "1/2") == False     # 5/7 * 1/2 = 5/14

    # Zero numerator
    assert module_0.simplify("0/5", "3/4") == True      # 0 * 3/4 = 0

    # Negative fractions
    assert module_0.simplify("-1/2", "2/1") == True     # -1/2 * 2/1 = -1
    assert module_0.simplify("-1/2", "-2/1") == True    # -1/2 * -2/1 = 1
    assert module_0.simplify("-1/2", "1/3") == False    # -1/2 * 1/3 = -1/6

    # Whole number inputs
    assert module_0.simplify("3/1", "4/1") == True      # 3 * 4 = 12
    assert module_0.simplify("7/1", "1/7") == True      # 7 * 1/7 = 1

    # Larger numbers
    assert module_0.simplify("100/3", "3/100") == True  # = 1
    assert module_0.simplify("100/7", "7/100") == True  # = 1
    assert module_0.simplify("100/3", "2/100") == False # = 2/3

    print("All tests passed!")


if __name__ == "__main__":
    test_simplify()

# Generated at 2026-11-02 13:44:16.643616
# Unit test for function simplify
def test_simplify():
    # Product is a whole number
    assert module_0.simplify("1/5", "5/1") == True
    assert module_0.simplify("2/3", "3/2") == True
    assert module_0.simplify("4/2", "1/2") == True
    assert module_0.simplify("1/1", "1/1") == True
    assert module_0.simplify("10/2", "2/1") == True

    # Product is not a whole number
    assert module_0.simplify("1/6", "2/1") == False
    assert module_0.simplify("7/10", "10/2") == False
    assert module_0.simplify("1/2", "1/2") == False
    assert module_0.simplify("3/4", "2/3") == False

    # Zero numerator -> product is 0, a whole number
    assert module_0.simplify("0/5", "3/2") == True

    # Negative fractions
    assert module_0.simplify("-1/5", "5/1") == True
    assert module_0.simplify("-1/2", "1/2") == False

    # Larger numbers
    assert module_0.simplify("100/3", "3/1") == True
    assert module_0.simplify("999/2", "2/997") == False

    print("All tests passed!")


if __name__ == "__main__":
    test_simplify()