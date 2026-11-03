

# Generated at 2026-11-02 22:33:09.326684
# Unit test for function parse_nested_parens
def test_parse_nested_parens():
    # Single group, simple nesting
    assert module_0.parse_nested_parens('()') == [1]
    assert module_0.parse_nested_parens('(())') == [2]
    assert module_0.parse_nested_parens('(()())') == [2]
    assert module_0.parse_nested_parens('((()))') == [3]
    assert module_0.parse_nested_parens('(((())))') == [4]

    # Max depth tracked within a single group (not per pair)
    assert module_0.parse_nested_parens('()(())') == [2]
    assert module_0.parse_nested_parens('(()()())') == [2]

    # Multiple groups separated by single spaces
    assert module_0.parse_nested_parens('() () ()') == [1, 1, 1]
    assert module_0.parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 1, 3]
    assert module_0.parse_nested_parens('() (()) ((())) (((())))') == [1, 2, 3, 4]

    # Multiple spaces between/around groups are ignored (empty strings filtered)
    assert module_0.parse_nested_parens('(())  ()') == [2, 1]
    assert module_0.parse_nested_parens('  (()) ()  ') == [2, 1]
    assert module_0.parse_nested_parens('   ') == []

    # Empty input yields empty list
    assert module_0.parse_nested_parens('') == []

    print("All tests passed!")


if __name__ == "__main__":
    test_parse_nested_parens()

# Generated at 2026-11-02 22:34:32.684639
# Unit test for function parse_nested_parens
def test_parse_nested_parens():
    # Basic example from the problem statement
    assert module_0.parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 0, 3]

    # Empty string yields empty list
    assert module_0.parse_nested_parens('') == []

    # Single simple group
    assert module_0.parse_nested_parens('()') == [1]

    # Single deeply nested group
    assert module_0.parse_nested_parens('((()))') == [3]
    assert module_0.parse_nested_parens('(((())))') == [4]

    # Increasing depths across groups
    assert module_0.parse_nested_parens('() (()) ((())) (((())))') == [1, 2, 3, 4]

    # Multiple spaces between groups (empty tokens are filtered out)
    assert module_0.parse_nested_parens('(())  (()())') == [2, 2]

    # Leading and trailing spaces
    assert module_0.parse_nested_parens('  () ()  ') == [1, 1]

    # Adjacent groups without spaces count as one token
    assert module_0.parse_nested_parens('()()()') == [1]

    # Complex mixed nesting
    assert module_0.parse_nested_parens('(()()) ((())) ((())()())') == [2, 3, 3]

    print("All tests passed!")


test_parse_nested_parens()

# Generated at 2026-11-02 22:35:26.979155
# Unit test for function parse_nested_parens
def test_parse_nested_parens():import unittest


class TestParseNestedParens(unittest.TestCase):

    def test_multiple_groups(self):
        self.assertEqual(module_0.parse_nested_parens('(()()) ((())) () ((())()())'), [2, 3, 1, 3])

    def test_single_group(self):
        self.assertEqual(module_0.parse_nested_parens('((()))'), [3])

    def test_simple_group(self):
        self.assertEqual(module_0.parse_nested_parens('()'), [1])

    def test_nested_groups(self):
        self.assertEqual(module_0.parse_nested_parens('(()())'), [2])

    def test_empty_string(self):
        self.assertEqual(module_0.parse_nested_parens(''), [])

    def test_multiple_spaces(self):
        self.assertEqual(module_0.parse_nested_parens('()  ((()))   ()'), [1, 3, 1])

    def test_leading_trailing_spaces(self):
        self.assertEqual(module_0.parse_nested_parens('  () ()  '), [1, 1])

    def test_deep_nesting(self):
        self.assertEqual(module_0.parse_nested_parens('((((()))))'), [5])

    def test_sequential_groups(self):
        self.assertEqual(module_0.parse_nested_parens('()()()'), [1])

    def test_mixed_depths(self):
        self.assertEqual(module_0.parse_nested_parens('(()) () ((())())'), [2, 1, 3])


if __name__ == '__main__':
    unittest.main()

# Generated at 2026-11-02 22:36:49.717593
# Unit test for function parse_nested_parens
def test_parse_nested_parens():
    # Example from docstring
    assert module_0.parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 1, 3]

    # Single group cases
    assert module_0.parse_nested_parens('()') == [1]
    assert module_0.parse_nested_parens('(())') == [2]
    assert module_0.parse_nested_parens('((()))') == [3]
    assert module_0.parse_nested_parens('((((()))))') == [5]

    # Multiple groups
    assert module_0.parse_nested_parens('() () ()') == [1, 1, 1]
    assert module_0.parse_nested_parens('(()()) () (())') == [2, 1, 2]
    assert module_0.parse_nested_parens('((())) ((())())') == [3, 3]

    # Empty and whitespace-only input
    assert module_0.parse_nested_parens('') == []
    assert module_0.parse_nested_parens('   ') == []

    # Extra spaces around groups are ignored
    assert module_0.parse_nested_parens('  ()  (()) ') == [1, 2]


if __name__ == '__main__':
    test_parse_nested_parens()
    print('All tests passed!')

# Generated at 2026-11-02 22:38:59.356936
# Unit test for function parse_nested_parens
def test_parse_nested_parens():
    # Basic multi-group example
    assert module_0.parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 0, 3]

    # Single groups of increasing depth
    assert module_0.parse_nested_parens('()') == [1]
    assert module_0.parse_nested_parens('(())') == [2]
    assert module_0.parse_nested_parens('((()))') == [3]
    assert module_0.parse_nested_parens('(((())))') == [4]

    # Empty string yields empty list
    assert module_0.parse_nested_parens('') == []

    # Groups separated by single spaces
    assert module_0.parse_nested_parens('() (()) ((()))') == [1, 2, 3]

    # Multiple spaces between groups are ignored
    assert module_0.parse_nested_parens('()  (())   ((()))') == [1, 2, 3]

    # Leading and trailing whitespace is ignored
    assert module_0.parse_nested_parens('  () (())  ') == [1, 2]

    # Mixed depths across groups
    assert module_0.parse_nested_parens('(()()) ((())()) (()())') == [2, 3, 2]

    # Same depth repeated across groups
    assert module_0.parse_nested_parens('() () ()') == [1, 1, 1]

    # Complex nesting patterns
    assert module_0.parse_nested_parens('(()(())) ((()())())') == [3, 3]
    assert module_0.parse_nested_parens('() ((())) (())') == [1, 3, 2]

    # Unbalanced: only opening parens still counts depth
    assert module_0.parse_nested_parens('(((') == [3]

    # Unbalanced: only closing parens keeps max depth at 0
    assert module_0.parse_nested_parens(')))') == [0]

    # Interleaved unbalanced group
    assert module_0.parse_nested_parens('(() (())') == [2]


if __name__ == '__main__':
    test_parse_nested_parens()
    print("All tests passed!")