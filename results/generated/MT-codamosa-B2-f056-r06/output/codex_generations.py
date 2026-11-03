

# Generated at 2026-11-03 02:43:06.272550
# Unit test for function correct_bracketing
def test_correct_bracketing():
    # Empty string is considered correctly bracketed
    assert module_0.correct_bracketing("") is True

    # Simple matched pair
    assert module_0.correct_bracketing("<>") is True

    # Simple unmatched: closing before opening
    assert module_0.correct_bracketing("><") is False

    # Nested brackets
    assert module_0.correct_bracketing("<<>>") is True

    # Deeply nested brackets
    assert module_0.correct_bracketing("<<<><>>>") is True

    # Sequential pairs
    assert module_0.correct_bracketing("<><>") is True

    # Unbalanced: only opening
    assert module_0.correct_bracketing("<") is False

    # Unbalanced: only closing
    assert module_0.correct_bracketing(">") is False

    # Unbalanced: extra opening
    assert module_0.correct_bracketing("<<>") is False

    # Unbalanced: extra closing
    assert module_0.correct_bracketing("<>>") is False

    # Closing appears before opening at start
    assert module_0.correct_bracketing("><<>") is False

    # Correct prefix but closes too early overall
    assert module_0.correct_bracketing("><<>") is False

    # Long balanced sequence
    assert module_0.correct_bracketing("<" * 50 + ">" * 50) is True

    # Long unbalanced sequence
    assert module_0.correct_bracketing("<" * 51 + ">" * 50) is False

    # Mixed nested and sequential
    assert module_0.correct_bracketing("<<>><<>>") is True

    # Mixed with imbalance
    assert module_0.correct_bracketing("<<>><<") is False

# Generated at 2026-11-03 02:45:48.176948
# Unit test for function correct_bracketing
def test_correct_bracketing():
    # Valid cases
    assert module_0.correct_bracketing("") == True          # empty string is balanced
    assert module_0.correct_bracketing("<>") == True        # simple pair
    assert module_0.correct_bracketing("<<>>") == True      # nested brackets
    assert module_0.correct_bracketing("<><>") == True      # sequential pairs
    assert module_0.correct_bracketing("<<<>>>") == True    # triple nesting
    assert module_0.correct_bracketing("<<><>>") == True    # mixed nesting

    # Invalid cases
    assert module_0.correct_bracketing(">") == False        # closing before opening
    assert module_0.correct_bracketing("<") == False        # unclosed opening bracket
    assert module_0.correct_bracketing("><") == False       # closing first
    assert module_0.correct_bracketing("<<") == False       # two unclosed brackets
    assert module_0.correct_bracketing(">>") == False       # two closings, no opening
    assert module_0.correct_bracketing("<<>") == False      # missing one closing
    assert module_0.correct_bracketing("<>>") == False      # extra closing
    assert module_0.correct_bracketing("<><>>") == False    # unbalanced at end
    assert module_0.correct_bracketing("<><") == False      # unclosed at end
    assert module_0.correct_bracketing("<<><") == False     # nested but unclosed
    assert module_0.correct_bracketing("<><><") == False    # sequence ending unclosed

    # Edge case: goes negative mid-string even if it would balance later
    assert module_0.correct_bracketing(">><<") == False

# Generated at 2026-11-03 02:49:16.244825
# Unit test for function correct_bracketing
def test_correct_bracketing():
    # Balanced single pair
    assert module_0.correct_bracketing("<>") is True
    # Unclosed opening bracket
    assert module_0.correct_bracketing("<") is False
    # Closing bracket with no opener
    assert module_0.correct_bracketing(">") is False
    # Closing before opening
    assert module_0.correct_bracketing("><") is False
    # Nested brackets
    assert module_0.correct_bracketing("<<>>") is True
    assert module_0.correct_bracketing("<<><>>") is True
    assert module_0.correct_bracketing("<<<>>>") is True
    assert module_0.correct_bracketing("<<<<>>>>") is True
    # Sequential pairs
    assert module_0.correct_bracketing("<><>") is True
    # Mixed nested and sequential
    assert module_0.correct_bracketing("<><<>><>") is True
    # Unbalanced: extra openers
    assert module_0.correct_bracketing("<<") is False
    assert module_0.correct_bracketing("<><") is False
    # Unbalanced: extra closers
    assert module_0.correct_bracketing(">>") is False
    assert module_0.correct_bracketing("<>>") is False
    # Depth goes negative mid-string (early exit path)
    assert module_0.correct_bracketing("><>") is False
    assert module_0.correct_bracketing("><<>") is False
    # Empty string is trivially balanced
    assert module_0.correct_bracketing("") is True
    # Ends with nonzero depth
    assert module_0.correct_bracketing("<><<<>>>><") is False
# nonce:1a76a78c

# Generated at 2026-11-03 02:50:42.071783
# Unit test for function correct_bracketing
def test_correct_bracketing():
    assert module_0.correct_bracketing("") == True
    assert module_0.correct_bracketing("<") == False
    assert module_0.correct_bracketing(">") == False
    assert module_0.correct_bracketing("<>") == True
    assert module_0.correct_bracketing("><") == False
    assert module_0.correct_bracketing("<<>>") == True
    assert module_0.correct_bracketing("<<>") == False
    assert module_0.correct_bracketing("<><>") == True
    assert module_0.correct_bracketing("<><>>") == False
    assert module_0.correct_bracketing("<<><>>") == True
    assert module_0.correct_bracketing(">>><<<") == False
    assert module_0.correct_bracketing("<<<<<>>>>>") == True
    assert module_0.correct_bracketing("<<>><<>>") == True
# nonce:b8dcad58