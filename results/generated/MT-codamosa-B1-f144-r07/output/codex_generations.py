

# Generated at 2026-10-24 12:09:58.479230
# Unit test for function simplify

# Generated at 2026-10-24 12:10:00.898073
# Unit test for function simplify

# Generated at 2026-10-24 12:10:26.416933
# Unit test for function simplify
def test_simplify():
    # Whole-result cases
    assert module_0.simplify("1/2", "2/1") is True
    assert module_0.simplify("1/2", "4/1") is True
    assert module_0.simplify("3/4", "4/3") is True
    assert module_0.simplify("0/5", "7/3") is True
    assert module_0.simplify("-1/2", "4/1") is True
    assert module_0.simplify("-1/2", "-4/1") is True

    # Non-whole-result cases
    assert module_0.simplify("1/3", "2/1") is False
    assert module_0.simplify("1/2", "3/1") is False
    assert module_0.simplify("-1/3", "2/1") is False
    assert module_0.simplify("5/4", "3/1") is False

# Generated at 2026-10-24 12:10:55.584707
# Unit test for function simplify
def test_simplify():
    # Whole-number results -> True
    assert module_0.simplify("1/5", "5/1") == True      # 1*5 / (5*1) = 5/5 = 1
    assert module_0.simplify("1/6", "2/1") == False     # 2/6 = 1/3, not whole
    assert module_0.simplify("7/4", "4/3") == False     # 28/12 = 7/3, not whole
    assert module_0.simplify("2/3", "3/2") == True      # 6/6 = 1
    assert module_0.simplify("3/1", "4/1") == True      # 12/1 = 12
    assert module_0.simplify("-1/2", "2/1") == True     # -2/2 = -1 (negatives work)
    assert module_0.simplify("0/5", "3/7") == True      # 0 is a whole number

    # Zero denominator raises ZeroDivisionError
    try:
        module_0.simplify("1/0", "2/3")
        assert False, "Expected ZeroDivisionError"
    except ZeroDivisionError:
        pass

    # Malformed input raises ValueError
    try:
        module_0.simplify("abc/2", "1/3")
        assert False, "Expected ValueError"
    except ValueError:
        pass

    print("All tests passed.")


test_simplify()

# Generated at 2026-10-24 12:10:58.178257
# Unit test for function simplify

# Generated at 2026-10-24 12:11:00.592106
# Unit test for function simplify

# Generated at 2026-10-24 12:11:03.042117
# Unit test for function simplify

# Generated at 2026-10-24 12:11:05.450775
# Unit test for function simplify

# Generated at 2026-10-24 12:11:07.881836
# Unit test for function simplify

# Generated at 2026-10-24 12:11:10.298584
# Unit test for function simplify

# Generated at 2026-10-24 12:11:12.715259
# Unit test for function simplify

# Generated at 2026-10-24 12:11:15.146023
# Unit test for function simplify

# Generated at 2026-10-24 12:11:17.564196
# Unit test for function simplify