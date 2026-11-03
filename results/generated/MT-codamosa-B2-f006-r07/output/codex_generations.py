

# Generated at 2026-11-02 13:19:32.867946
# Unit test for function parse_nested_parens
def test_parse_nested_parens():
    # Classic example: multiple groups with varying depths
    assert module_0.parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 1, 3]

    # Simple single pair
    assert module_0.parse_nested_parens('()') == [1]

    # Single nested group
    assert module_0.parse_nested_parens('(())') == [2]

    # Deeply nested single group
    assert module_0.parse_nested_parens('(((())))') == [4]

    # Increasing depths across groups
    assert module_0.parse_nested_parens('() (()) ((())) (((())))') == [1, 2, 3, 4]

    # Decreasing depths across groups
    assert module_0.parse_nested_parens('((())) (()) ()') == [3, 2, 1]

    # Empty string returns empty list
    assert module_0.parse_nested_parens('') == []

    # Multiple consecutive spaces between groups (empty strings filtered out)
    assert module_0.parse_nested_parens('(()())  ((()))') == [2, 3]

    # Leading/trailing spaces are handled
    assert module_0.parse_nested_parens(' (()()) ') == [2]

    print("test_parse_nested_parens passed")


test_parse_nested_parens()

# Generated at 2026-11-02 13:22:19.405627
# Unit test for function parse_nested_parens
def test_parse_nested_parens():
    # Empty string yields an empty list
    assert module_0.parse_nested_parens('') == []

    # Single simple group
    assert module_0.parse_nested_parens('()') == [1]
    assert module_0.parse_nested_parens('(())') == [2]
    assert module_0.parse_nested_parens('((()))') == [3]

    # Group with multiple siblings at same depth
    assert module_0.parse_nested_parens('(()())') == [2]
    assert module_0.parse_nested_parens('((()()))') == [3]

    # Multiple groups separated by spaces
    assert module_0.parse_nested_parens('() () ()') == [1, 1, 1]
    assert module_0.parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 1, 3]
    assert module_0.parse_nested_parens('((())) (()) ()') == [3, 2, 1]

    # Extra spaces between groups are ignored
    assert module_0.parse_nested_parens('  ()  (())  ') == [1, 2]

    print("All tests passed!")


test_parse_nested_parens()

# Generated at 2026-11-02 13:23:17.735924
# Unit test for function parse_nested_parens
def test_parse_nested_parens():
    # Basic example from the classic problem
    assert module_0.parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 0, 3]

    # Single group with nesting depth 2
    assert module_0.parse_nested_parens('(())') == [2]

    # Single group with nesting depth 1
    assert module_0.parse_nested_parens('()') == [1]

    # Deeply nested single group
    assert module_0.parse_nested_parens('(((())))') == [4]

    # Empty string should return empty list
    assert module_0.parse_nested_parens('') == []

    # String with only spaces should return empty list
    assert module_0.parse_nested_parens('   ') == []

    # Multiple simple groups
    assert module_0.parse_nested_parens('() () ()') == [1, 1, 1]

    # Mixed depths
    assert module_0.parse_nested_parens('() (()) ((()))') == [1, 2, 3]

    # Extra spaces between groups are ignored
    assert module_0.parse_nested_parens('()  (())   ((()))') == [1, 2, 3]

    # Leading/trailing spaces
    assert module_0.parse_nested_parens('  (())  ') == [2]

    # Group where max depth occurs after closing some parens
    assert module_0.parse_nested_parens('(())()') == 2 == module_0.parse_nested_parens('(())()')[0]

    # Alternating shallow and deep groups
    assert module_0.parse_nested_parens('(()(())) () ((()))') == [3, 1, 3]

# Generated at 2026-11-02 13:24:59.343909
# Unit test for function parse_nested_parens
def test_parse_nested_parens():
    # Single group with basic nesting
    assert module_0.parse_nested_parens('(()())') == [2]

    # Multiple groups of varying depth (classic example)
    assert module_0.parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 1, 3]

    # Single pair of parentheses
    assert module_0.parse_nested_parens('()') == [1]

    # Deeply nested group
    assert module_0.parse_nested_parens('(((())))') == [4]

    # Empty string yields empty list
    assert module_0.parse_nested_parens('') == []

    # Extra spaces between groups are ignored
    assert module_0.parse_nested_parens('  ()   ((()))  ') == [1, 3]

    # Several identical simple groups
    assert module_0.parse_nested_parens('() () ()') == [1, 1, 1]

    # Mixed depths across groups
    assert module_0.parse_nested_parens('((())) (()()) (()())') == [3, 2, 2]

    # Single group per call
    assert module_0.parse_nested_parens('(()(()))') == [3]

    # Group where depth goes up and down repeatedly
    assert module_0.parse_nested_parens('()((()))()') == [3]

    print("All tests passed!")


if __name__ == "__main__":
    test_parse_nested_parens()