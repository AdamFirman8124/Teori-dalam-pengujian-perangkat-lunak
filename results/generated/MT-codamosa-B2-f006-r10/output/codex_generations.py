

# Generated at 2026-11-03 01:54:08.797121
# Unit test for function parse_nested_parens
def test_parse_nested_parens():
    # Typical input with multiple groups of varying depth
    assert module_0.parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 1, 3]

    # Single simple groups
    assert module_0.parse_nested_parens('()') == [1]
    assert module_0.parse_nested_parens('(())') == [2]

    # Deeply nested single group
    assert module_0.parse_nested_parens('(((())))') == [4]

    # Multiple groups in increasing depth
    assert module_0.parse_nested_parens('() (()) ((())) (((())))') == [1, 2, 3, 4]

    # Empty string yields an empty list
    assert module_0.parse_nested_parens('') == []

    # Extra spaces: empty tokens between/after groups are ignored
    assert module_0.parse_nested_parens('  ()  (()) ') == [1, 2]

    # Groups with equal maximum depth
    assert module_0.parse_nested_parens('(()) (()())') == [2, 2]

    # Sequential groups where depth goes up and down
    assert module_0.parse_nested_parens('((())) () ((()))') == [3, 1, 3]

    print("test_parse_nested_parens passed")


test_parse_nested_parens()

# Generated at 2026-11-03 01:54:43.816265
# Unit test for function parse_nested_parens
def test_parse_nested_parens():
    # nonce:349f9a67
    # Standard example from the docstring
    assert module_0.parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 1, 3]

    # Single group cases
    assert module_0.parse_nested_parens('()') == [1]
    assert module_0.parse_nested_parens('(())') == [2]
    assert module_0.parse_nested_parens('((()))') == [3]
    assert module_0.parse_nested_parens('((((()))))') == [5]

    # Multiple groups
    assert module_0.parse_nested_parens('() () ()') == [1, 1, 1]
    assert module_0.parse_nested_parens('()()()') == [1, 1, 1]
    assert module_0.parse_nested_parens('((())) (()()) ()') == [3, 2, 1]
    assert module_0.parse_nested_parens('(()()) () ((()))') == [2, 1, 3]

    # Deeply nested single group
    assert module_0.parse_nested_parens('(((())))') == [4]

    # Empty string and whitespace-only input
    assert module_0.parse_nested_parens('') == []
    assert module_0.parse_nested_parens('   ') == []

    # Extra spaces between groups (empty tokens filtered out)
    assert module_0.parse_nested_parens('()  ((()))   ()') == [1, 3, 1]

    print("All tests passed!")


if __name__ == "__main__":
    test_parse_nested_parens()

# Generated at 2026-11-03 01:55:33.022686
# Unit test for function parse_nested_parens
def test_parse_nested_parens():
    # Standard example: multiple groups separated by spaces
    assert module_0.parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 1, 3]

    # Single group
    assert module_0.parse_nested_parens('((()))') == [3]

    # Simple non-nested group
    assert module_0.parse_nested_parens('()') == [1]

    # Deeply nested single group
    assert module_0.parse_nested_parens('((((()))))') == [5]

    # Empty string returns empty list
    assert module_0.parse_nested_parens('') == []

    # Multiple consecutive spaces are handled (empty groups filtered out)
    assert module_0.parse_nested_parens('()  (())   ((()))') == [1, 2, 3]

    # Leading/trailing whitespace
    assert module_0.parse_nested_parens('  (())  ') == [2]

    # Each group evaluated independently
    assert module_0.parse_nested_parens('(()()) ((()))') == [2, 3]

    # Mixed depths across groups
    assert module_0.parse_nested_parens('() (()) ((())) (((())))') == [1, 2, 3, 4]

    # Groups with sequential (non-nested) parens stay at depth 1
    assert module_0.parse_nested_parens('()()()') == [1]

    print("All tests passed!")


if __name__ == "__main__":
    test_parse_nested_parens()

# Generated at 2026-11-03 01:56:53.394535
# Unit test for function parse_nested_parens
def test_parse_nested_parens():
    # Classic example: multiple groups with varying depths
    assert module_0.parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 1, 3]

    # Single simple group
    assert module_0.parse_nested_parens('()') == [1]

    # Single deeply nested group
    assert module_0.parse_nested_parens('((()))') == [3]
    assert module_0.parse_nested_parens('(((())))') == [4]

    # Empty input yields empty list
    assert module_0.parse_nested_parens('') == []

    # Multiple flat groups
    assert module_0.parse_nested_parens('() () ()') == [1, 1, 1]

    # Mixed nesting depths
    assert module_0.parse_nested_parens('(()(())) ()') == [3, 1]

    # Extra whitespace between/around groups is ignored
    assert module_0.parse_nested_parens('  ()  ((()))  ') == [1, 3]

    # Consecutive groups separated by single spaces
    assert module_0.parse_nested_parens('(()) () (())') == [2, 1, 2]

    # Group with alternating nesting
    assert module_0.parse_nested_parens('()(())((()))') == [1, 2, 3]

# Generated at 2026-11-03 01:57:24.388578
# Unit test for function parse_nested_parens
def test_parse_nested_parens():
    # Canonical example
    assert module_0.parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 0, 3]

    # Single group with varying depths
    assert module_0.parse_nested_parens('()') == [1]
    assert module_0.parse_nested_parens('(())') == [2]
    assert module_0.parse_nested_parens('((()))') == [3]
    assert module_0.parse_nested_parens('((((()))))') == [5]
    assert module_0.parse_nested_parens('(()(()))') == [3]

    # Multiple groups
    assert module_0.parse_nested_parens('() ()') == [1, 1]
    assert module_0.parse_nested_parens('()(())') == [1, 2]
    assert module_0.parse_nested_parens('() (()) ((())) (((())))') == [1, 2, 3, 4]
    assert module_0.parse_nested_parens('(()()) (())') == [2, 2]
    assert module_0.parse_nested_parens('(()()) ((())) ()') == [2, 3, 0]

    # Empty string yields empty list
    assert module_0.parse_nested_parens('') == []

    # Extra spaces between/around groups are ignored
    assert module_0.parse_nested_parens('()  (())') == [1, 2]
    assert module_0.parse_nested_parens('  ()  (())  ') == [1, 2]

    # Groups with trailing no-op pairs
    assert module_0.parse_nested_parens('(()())()') == [2]
    assert module_0.parse_nested_parens('(()()) ((()))()') == [2, 3]