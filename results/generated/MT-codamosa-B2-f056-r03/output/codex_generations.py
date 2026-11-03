

# Generated at 2026-11-01 20:47:31.871297
# Unit test for function correct_bracketing
def test_correct_bracketing():import unittest


def module_0.correct_bracketing(brackets: str):
    
    depth = 0
    for b in brackets:
        if b == "<":
            depth += 1
        else:
            depth -= 1
        if depth < 0:
            return False
    return depth == 0



# Unit test for function correct_bracketing
class TestCorrectBracketing(unittest.TestCase):

    def test_empty_string(self):
        self.assertTrue(module_0.correct_bracketing(""))

    def test_single_open(self):
        self.assertFalse(module_0.correct_bracketing("<"))

    def test_single_close(self):
        self.assertFalse(module_0.correct_bracketing(">"))

    def test_simple_pair(self):
        self.assertTrue(module_0.correct_bracketing("<>"))

    def test_reversed_pair(self):
        self.assertFalse(module_0.correct_bracketing("><"))

    def test_nested_pairs(self):
        self.assertTrue(module_0.correct_bracketing("<<>>"))

    def test_sequential_pairs(self):
        self.assertTrue(module_0.correct_bracketing("<><>"))

    def test_deeply_nested(self):
        self.assertTrue(module_0.correct_bracketing("<<<>>>"))

    def test_missing_closing(self):
        self.assertFalse(module_0.correct_bracketing("<<>"))

    def test_extra_closing(self):
        self.assertFalse(module_0.correct_bracketing("<>>"))

    def test_mixed_valid(self):
        self.assertTrue(module_0.correct_bracketing("<><<>>"))

    def test_mixed_invalid(self):
        self.assertFalse(module_0.correct_bracketing("<><>>"))

    def test_close_before_open(self):
        self.assertFalse(module_0.correct_bracketing("><<>"))


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-01 20:48:08.078689
# Unit test for function correct_bracketing
def test_correct_bracketing():
    # Empty string is considered correctly bracketed
    assert module_0.correct_bracketing("") is True

    # Simple valid pair
    assert module_0.correct_bracketing("<>") is True

    # Nested brackets
    assert module_0.correct_bracketing("<<>>") is True

    # Sequential brackets
    assert module_0.correct_bracketing("<><>") is True

    # Deeply nested brackets
    assert module_0.correct_bracketing("<<<>>>") is True

    # Mixed nesting and sequencing
    assert module_0.correct_bracketing("<<><>>") is True

    # Starts with closing bracket
    assert module_0.correct_bracketing(">") is False

    # Closing before opening
    assert module_0.correct_bracketing("><") is False

    # Unclosed opening bracket
    assert module_0.correct_bracketing("<") is False

    # Unclosed nested opening brackets
    assert module_0.correct_bracketing("<<") is False

    # Extra closing bracket at end
    assert module_0.correct_bracketing("<>>") is False

    # Valid prefix but unbalanced overall
    assert module_0.correct_bracketing("<<>>><") is False

# Generated at 2026-11-01 20:48:35.111915
# Unit test for function correct_bracketing
def test_correct_bracketing():
    assert module_0.correct_bracketing("") == True          # empty string is balanced
    assert module_0.correct_bracketing("<") == False        # unclosed bracket
    assert module_0.correct_bracketing(">") == False        # closing without opening
    assert module_0.correct_bracketing("<>") == True        # simple pair
    assert module_0.correct_bracketing("><") == False       # wrong order
    assert module_0.correct_bracketing("<<>>") == True      # nested
    assert module_0.correct_bracketing("<><>") == True      # sequential pairs
    assert module_0.correct_bracketing("<<><>>") == True    # mixed nesting
    assert module_0.correct_bracketing("><<>") == False     # goes negative early
    assert module_0.correct_bracketing(">>") == False       # depth goes negative
    assert module_0.correct_bracketing("<<<>>>") == True    # deep nesting
    assert module_0.correct_bracketing("<><>>") == False    # extra closing at end
    assert module_0.correct_bracketing("<<><") == False     # unclosed at end
    assert module_0.correct_bracketing("<><<>>") == True    # nested inside sequence

# nonce:d8cc665d

# Generated at 2026-11-01 20:49:19.379934
# Unit test for function correct_bracketing
def test_correct_bracketing():
    # Empty string is trivially balanced
    assert module_0.correct_bracketing("") is True

    # Simple balanced pair
    assert module_0.correct_bracketing("<>") is True

    # Single open bracket — never closed
    assert module_0.correct_bracketing("<") is False

    # Single close bracket with no opener
    assert module_0.correct_bracketing(">") is False

    # Closing before opening (wrong order) triggers negative depth
    assert module_0.correct_bracketing("><") is False

    # Nested brackets
    assert module_0.correct_bracketing("<<>>") is True

    # Deep nesting
    assert module_0.correct_bracketing("<<<>>>") is True

    # Sequential balanced pairs
    assert module_0.correct_bracketing("<><>") is True

    # Nested plus sequential
    assert module_0.correct_bracketing("<<>><<>") is True

    # Extra closers at end leaves depth negative path / nonzero depth
    assert module_0.correct_bracketing("<>>") is False

    # Extra opener at end leaves depth positive
    assert module_0.correct_bracketing("<<>") is False

    # Mismatched pattern where depth recovers but ends nonzero
    assert module_0.correct_bracketing("<><") is False

    # Longer mixed example
    assert module_0.correct_bracketing("<<><>>") is True

    # Negative depth occurs midway even though total counts match
    assert module_0.correct_bracketing("><<") is False

    print("All tests passed!")


if __name__ == "__main__":
    test_correct_bracketing()

# Generated at 2026-11-01 20:49:54.368861
# Unit test for function correct_bracketing
def test_correct_bracketing():
    # Valid bracketing cases
    assert module_0.correct_bracketing("") is True          # empty string is balanced
    assert module_0.correct_bracketing("<>") is True        # simple pair
    assert module_0.correct_bracketing("<<>>") is True      # nested pair
    assert module_0.correct_bracketing("<><>") is True      # sequential pairs
    assert module_0.correct_bracketing("<<><>>") is True    # mixed nesting
    assert module_0.correct_bracketing("<<<>>>") is True    # deep nesting

    # Invalid bracketing cases
    assert module_0.correct_bracketing("<") is False        # unclosed bracket
    assert module_0.correct_bracketing(">") is False        # close before open
    assert module_0.correct_bracketing("><") is False       # closes first
    assert module_0.correct_bracketing("<><") is False      # trailing unclosed
    assert module_0.correct_bracketing("<<>") is False      # unbalanced depth
    assert module_0.correct_bracketing("<><>>") is False    # extra closing
    assert module_0.correct_bracketing(">>>") is False      # all closing
    assert module_0.correct_bracketing("<<>>><") is False   # valid then unclosed