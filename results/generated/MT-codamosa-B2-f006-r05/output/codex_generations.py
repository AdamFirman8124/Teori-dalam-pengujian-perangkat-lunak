

# Generated at 2026-11-02 17:52:30.817072
# Unit test for function parse_nested_parens
def test_parse_nested_parens():
    # Basic example from docstring-style usage
    assert module_0.parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 1, 3]

    # Single group with one level of nesting
    assert module_0.parse_nested_parens('()') == [1]

    # Single group with nested parens
    assert module_0.parse_nested_parens('(())') == [2]

    # Deep nesting
    assert module_0.parse_nested_parens('(((())))') == [4]

    # Multiple groups with increasing depth
    assert module_0.parse_nested_parens('() (()) ((())) (((())))') == [1, 2, 3, 4]

    # Empty string input
    assert module_0.parse_nested_parens('') == []

    # Multiple spaces between groups (empty tokens filtered out)
    assert module_0.parse_nested_parens('()  (())') == [1, 2]

    # Leading/trailing spaces
    assert module_0.parse_nested_parens('  () (())  ') == [1, 2]

    # Adjacent groups at same depth
    assert module_0.parse_nested_parens('()()') == [1, 1]

    # Complex nested structures
    assert module_0.parse_nested_parens('(()()) ((())) (()(()))') == [2, 3, 3]

# Generated at 2026-11-02 17:53:21.150062
# Unit test for function parse_nested_parens
def test_parse_nested_parens():
    # Classic example: multiple groups with varying depths
    assert module_0.parse_nested_parens('(()()) ((())) () ((())())') == [2, 3, 1, 3]

    # Single simple group
    assert module_0.parse_nested_parens('()') == [1]

    # Single nested groups of increasing depth
    assert module_0.parse_nested_parens('(())') == [2]
    assert module_0.parse_nested_parens('((()))') == [3]
    assert module_0.parse_nested_parens('(((())))') == [4]

    # Multiple groups with the same depth
    assert module_0.parse_nested_parens('() () ()') == [1, 1, 1]

    # Groups in increasing order of depth
    assert module_0.parse_nested_parens('() (()) ((())) (((())))') == [1, 2, 3, 4]

    # Groups in decreasing order of depth
    assert module_0.parse_nested_parens('((())) () (())') == [3, 1, 2]

    # Empty string yields empty list
    assert module_0.parse_nested_parens('') == []

    # String of only spaces yields empty list (empty tokens filtered out)
    assert module_0.parse_nested_parens('   ') == []

    # Groups interleaved with multiple spaces
    assert module_0.parse_nested_parens('(()())  ((()))') == [2, 3]

    # Complex mixed groups
    assert module_0.parse_nested_parens('(()()) ((())) ((())()) (()(()))') == [2, 3, 3, 3]

    # Deeply nested single group
    assert module_0.parse_nested_parens('(((()))) ((()))') == [4, 3]

    print("All tests passed!")


if __name__ == "__main__":
    test_parse_nested_parens()

# Generated at 2026-11-02 17:55:03.375429
# Unit test for function parse_nested_parens
def test_parse_nested_parens():
    # Basic example with multiple groups
    assert module_0.parse_nested_parens('(()()) ((())) () ((())())') == [2, 3, 0, 3]

    # Single group
    assert module_0.parse_nested_parens('((()))') == [3]

    # Single pair of parentheses
    assert module_0.parse_nested_parens('()') == [1]

    # Empty string returns empty list
    assert module_0.parse_nested_parens('') == []

    # Multiple consecutive spaces between groups are ignored
    assert module_0.parse_nested_parens('() ()  ()') == [1, 1, 1]

    # Leading/trailing whitespace is ignored
    assert module_0.parse_nested_parens(' (()()) ') == [2]

    # Deeply nested single group
    assert module_0.parse_nested_parens('(((())))') == [4]

    # Increasing depths across groups
    assert module_0.parse_nested_parens('() (()) ((()))') == [1, 2, 3]

    # Decreasing depths across groups
    assert module_0.parse_nested_parens('((())) (()) ()') == [3, 2, 1]

    # Groups where depth goes down then back up; max depth tracked correctly
    assert module_0.parse_nested_parens('(()()) (())') == [2, 2]

    # Max depth is not total count of parens, only nesting level
    assert module_0.parse_nested_parens('()()()') == [1]

    print("All tests passed!")


test_parse_nested_parens()

# Generated at 2026-11-02 17:56:40.209479
# Unit test for function parse_nested_parens
def test_parse_nested_parens():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestParseNestedParens)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    return result.wasSuccessful()


if __name__ == '__main__':
    test_parse_nested_parens()

# Generated at 2026-11-02 17:58:00.836115
# Unit test for function parse_nested_parens
def test_parse_nested_parens():
    # Single group with varying depths
    assert module_0.parse_nested_parens('()') == [1]
    assert module_0.parse_nested_parens('(())') == [2]
    assert module_0.parse_nested_parens('((()))') == [3]

    # Classic example: multiple groups separated by spaces
    assert module_0.parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 1, 3]

    # Empty string yields empty list
    assert module_0.parse_nested_parens('') == []

    # Extra spaces between groups are ignored
    assert module_0.parse_nested_parens('  (())   ()  ') == [2, 1]

    # Group with sequential (non-nested) parens has depth 1
    assert module_0.parse_nested_parens('()()()') == [1]

    # Mixed sequential and nested parens in one group
    assert module_0.parse_nested_parens('()(())') == [2]

    # Deeply nested group
    assert module_0.parse_nested_parens('(((())))') == [4]

    # Multiple groups with identical depth
    assert module_0.parse_nested_parens('(()) ((()) ())') == [2, 2]

    # Single group with closing before opening (depth goes negative, max stays 0)
    assert module_0.parse_nested_parens(')(') == [0]

    # Complex combination
    assert module_0.parse_nested_parens('(()()) ((())) (()(()))') == [2, 3, 3]

    print("All tests passed!")


if __name__ == "__main__":
    test_parse_nested_parens()