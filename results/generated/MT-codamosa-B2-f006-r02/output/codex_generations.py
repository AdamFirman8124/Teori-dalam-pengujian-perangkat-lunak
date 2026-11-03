

# Generated at 2026-11-03 02:13:25.690709
# Unit test for function parse_nested_parens
def test_parse_nested_parens():
    # Basic example with multiple groups
    assert module_0.parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 1, 3]

    # Single simple group
    assert module_0.parse_nested_parens('()') == [1]

    # Single deeply nested group
    assert module_0.parse_nested_parens('(((())))') == [4]

    # Multiple identical groups
    assert module_0.parse_nested_parens('() () ()') == [1, 1, 1]

    # Groups with varying depths
    assert module_0.parse_nested_parens('(()) () ((()))') == [2, 1, 3]

    # Empty string returns empty list
    assert module_0.parse_nested_parens('') == []

    # String with only spaces returns empty list
    assert module_0.parse_nested_parens('   ') == []

    # Extra spaces between groups are handled
    assert module_0.parse_nested_parens('(())  ((()))') == [2, 3]

    # Complex nesting patterns
    assert module_0.parse_nested_parens('((())) (()) ()') == [3, 2, 1]

    assert module_0.parse_nested_parens('(()(())((())))') == [5]

    # Leading/trailing whitespace
    assert module_0.parse_nested_parens('  (())  ') == [2]

    print("All tests passed!")


if __name__ == "__main__":
    test_parse_nested_parens()

# Generated at 2026-11-03 02:14:57.066891
# Unit test for function parse_nested_parens
def test_parse_nested_parens():
    # Canonical example: multiple groups separated by spaces
    assert module_0.parse_nested_parens('(()()) ((())) () ((())())') == [2, 3, 0, 3]

    # Single group
    assert module_0.parse_nested_parens('(())') == [2]
    assert module_0.parse_nested_parens('()') == [0]
    assert module_0.parse_nested_parens('((()))') == [3]

    # Deeply nested single group
    assert module_0.parse_nested_parens('(((())))') == [4]
    assert module_0.parse_nested_parens('((((((()))))))') == [7]

    # Empty parentheses groups
    assert module_0.parse_nested_parens('() () ()') == [0, 0, 0]

    # Mixed depths
    assert module_0.parse_nested_parens('(()(())) () ((()))') == [3, 0, 3]

    # Single character groups
    assert module_0.parse_nested_parens('() ()') == [0, 0]

    # Empty string returns empty list
    assert module_0.parse_nested_parens('') == []

    # Extra spaces are ignored (empty tokens filtered out)
    assert module_0.parse_nested_parens('  (()())   ((()))  ') == [2, 3]

    # Whitespace-only string
    assert module_0.parse_nested_parens('   ') == []

    # Multiple spaces between groups
    assert module_0.parse_nested_parens('()   (())    ((()))') == [0, 2, 3]

    # Alternating depths
    assert module_0.parse_nested_parens('() (()) (()()) ((()))') == [0, 2, 2, 3]

    # Group with immediate nesting then closing
    assert module_0.parse_nested_parens('(()())') == [2]

    # Group where depth increases gradually
    assert module_0.parse_nested_parens('(()(()))') == [3]

    # Long sequence of same group
    assert module_0.parse_nested_parens('(()) (()) (())') == [2, 2, 2]

    print("All tests passed!")


test_parse_nested_parens()

# Generated at 2026-11-03 02:16:26.151303
# Unit test for function parse_nested_parens
def test_parse_nested_parens():
    # Example from the problem statement
    assert module_0.parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 1, 3]

    # Single groups of increasing depth
    assert module_0.parse_nested_parens('()') == [1]
    assert module_0.parse_nested_parens('(())') == [2]
    assert module_0.parse_nested_parens('((()))') == [3]
    assert module_0.parse_nested_parens('(((())))') == [4]

    # Multiple identical groups
    assert module_0.parse_nested_parens('() () ()') == [1, 1, 1]
    assert module_0.parse_nested_parens('(()) (())') == [2, 2]

    # Mixed depths across groups
    assert module_0.parse_nested_parens('(()(())) (()())') == [3, 2]
    assert module_0.parse_nested_parens('((())) () (())') == [3, 1, 2]

    # Empty and whitespace-only inputs
    assert module_0.parse_nested_parens('') == []
    assert module_0.parse_nested_parens('   ') == []

    # Single group without spaces (treated as one group)
    assert module_0.parse_nested_parens('(()())') == [2]

    print('All tests passed!')


test_parse_nested_parens()

# Generated at 2026-11-03 02:17:51.963136
# Unit test for function parse_nested_parens
def test_parse_nested_parens():
    # Basic single group
    assert module_0.parse_nested_parens("(()())") == [2]
    assert module_0.parse_nested_parens("((()))") == [3]
    assert module_0.parse_nested_parens("()") == [1]

    # Multiple groups separated by spaces
    assert module_0.parse_nested_parens("() (()) ((()))") == [1, 2, 3]
    assert module_0.parse_nested_parens("(()()) ((())) () ((())()())") == [2, 3, 1, 3]

    # Deeply nested
    assert module_0.parse_nested_parens("(((())))") == 4 if False else module_0.parse_nested_parens("(((())))") == [4]

    # Empty string yields empty list
    assert module_0.parse_nested_parens("") == []

    # Extra spaces are filtered out
    assert module_0.parse_nested_parens("  ()   (())  ") == [1, 2]

    # Single group with mixed content
    assert module_0.parse_nested_parens("(()(()))") == [3]

    print("All tests passed!")


test_parse_nested_parens()

# Generated at 2026-11-03 02:19:30.477741
# Unit test for function parse_nested_parens
def test_parse_nested_parens():
    # Canonical example: max nesting depth per group
    assert module_0.parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 1, 3]

    # Single group cases
    assert module_0.parse_nested_parens('()') == [1]
    assert module_0.parse_nested_parens('(())') == [2]
    assert module_0.parse_nested_parens('((()))') == [3]

    # Deeply nested single group
    assert module_0.parse_nested_parens('((((()))))') == [5]

    # Multiple groups with varying depths
    assert module_0.parse_nested_parens('() (()) ((())) (((())))') == [1, 2, 3, 4]

    # Extra whitespace between groups is ignored
    assert module_0.parse_nested_parens('  () ()  ()  ') == [1, 1, 1]

    # Empty string yields empty list
    assert module_0.parse_nested_parens('') == []

    # Groups with interleaved sibling parens
    assert module_0.parse_nested_parens('(()()) ((()))') == [2, 3]
    assert module_0.parse_nested_parens('(()(())) (()())') == [3, 2]

    print("All tests passed!")


test_parse_nested_parens()