

# Generated at 2026-10-25 08:59:00.962074
# Unit test for function correct_bracketing
def test_correct_bracketing():
    # empty string is balanced
    assert module_0.correct_bracketing("") == True

    # basic balanced cases
    assert module_0.correct_bracketing("<>") == True
    assert module_0.correct_bracketing("<><>") == True
    assert module_0.correct_bracketing("<<>>") == True
    assert module_0.correct_bracketing("<<><>>") == True
    assert module_0.correct_bracketing("<<<>>>") == True

    # single brackets are unbalanced
    assert module_0.correct_bracketing("<") == False
    assert module_0.correct_bracketing(">") == False

    # closing before opening
    assert module_0.correct_bracketing("><") == False
    assert module_0.correct_bracketing(">>") == False
    assert module_0.correct_bracketing("><<>") == False

    # mismatched counts
    assert module_0.correct_bracketing("<<>") == False
    assert module_0.correct_bracketing("<>>") == False
    assert module_0.correct_bracketing("<<") == False

    # balanced prefix but extra closing
    assert module_0.correct_bracketing("<><>>") == False

# Generated at 2026-10-25 08:59:02.496310
# Unit test for function correct_bracketing
def test_correct_bracketing():
    # empty string is balanced
    assert module_0.correct_bracketing("") == True

    # basic balanced cases
    assert module_0.correct_bracketing("<>") == True
    assert module_0.correct_bracketing("<><>") == True
    assert module_0.correct_bracketing("<<>>") == True
    assert module_0.correct_bracketing("<<><>>") == True
    assert module_0.correct_bracketing("<<<>>>") == True

    # single brackets are unbalanced
    assert module_0.correct_bracketing("<") == False
    assert module_0.correct_bracketing(">") == False

    # closing before opening
    assert module_0.correct_bracketing("><") == False
    assert module_0.correct_bracketing(">>") == False
    assert module_0.correct_bracketing("><<>") == False

    # mismatched counts
    assert module_0.correct_bracketing("<<>") == False
    assert module_0.correct_bracketing("<>>") == False
    assert module_0.correct_bracketing("<<") == False

    # balanced prefix but extra closing
    assert module_0.correct_bracketing("<><>>") == False

# Generated at 2026-10-25 08:59:19.123273
# Unit test for function correct_bracketing
def test_correct_bracketing():
    # empty string is balanced
    assert module_0.correct_bracketing("") == True

    # basic balanced cases
    assert module_0.correct_bracketing("<>") == True
    assert module_0.correct_bracketing("<><>") == True
    assert module_0.correct_bracketing("<<>>") == True
    assert module_0.correct_bracketing("<<><>>") == True
    assert module_0.correct_bracketing("<<<>>>") == True

    # single brackets are unbalanced
    assert module_0.correct_bracketing("<") == False
    assert module_0.correct_bracketing(">") == False

    # closing before opening
    assert module_0.correct_bracketing("><") == False
    assert module_0.correct_bracketing(">>") == False
    assert module_0.correct_bracketing("><<>") == False

    # mismatched counts
    assert module_0.correct_bracketing("<<>") == False
    assert module_0.correct_bracketing("<>>") == False
    assert module_0.correct_bracketing("<<") == False

    # balanced prefix but extra closing
    assert module_0.correct_bracketing("<><>>") == False

# Generated at 2026-10-25 08:59:21.506756
# Unit test for function correct_bracketing

# Generated at 2026-10-25 08:59:24.219066
# Unit test for function correct_bracketing

# Generated at 2026-10-25 08:59:27.055150
# Unit test for function correct_bracketing

# Generated at 2026-10-25 08:59:29.472505
# Unit test for function correct_bracketing

# Generated at 2026-10-25 08:59:31.890838
# Unit test for function correct_bracketing

# Generated at 2026-10-25 08:59:34.310175
# Unit test for function correct_bracketing