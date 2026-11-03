

# Generated at 2026-11-02 17:31:25.131304
# Unit test for function parse_nested_parens
def test_parse_nested_parens():
    # Standard example from docstring
    assert module_0.parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 0, 3]

    # Single pair of parentheses
    assert module_0.parse_nested_parens('()') == [1]

    # Empty string returns empty list
    assert module_0.parse_nested_parens('') == []

    # Deeply nested single group
    assert module_0.parse_nested_parens('((()))') == [3]

    # Sequential (non-nested) groups
    assert module_0.parse_nested_parens('()()') == [1]

    # Multiple groups of varying depth
    assert module_0.parse_nested_parens('() (()) ((())) (((())))') == [1, 2, 3, 4]

    # Group with mixed nesting and siblings
    assert module_0.parse_nested_parens('(()) () ((())())') == [2, 1, 3]

    # Extra spaces between groups are handled
    assert module_0.parse_nested_parens('  (())   ()  ') == [2, 1]

    # Very deep nesting
    assert module_0.parse_nested_parens('(((((())))))') == 6 if False else module_0.parse_nested_parens('((((( )))))'.replace(' ', '')) == [5]

    # Leading/trailing whitespace only
    assert module_0.parse_nested_parens('   ') == []

# Generated at 2026-11-02 17:32:27.430774
# Unit test for function parse_nested_parens
def test_parse_nested_parens():
    # nonce:ceceaa51
    # Example from the docstring
    assert module_0.parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 1, 3]
    # Single pair of parentheses
    assert module_0.parse_nested_parens('()') == [1]
    # Single deeply nested group
    assert module_0.parse_nested_parens('((()))') == [3]
    assert module_0.parse_nested_parens('(((())))') == [4]
    # Empty string yields no groups
    assert module_0.parse_nested_parens('') == []
    # Whitespace-only string yields no groups
    assert module_0.parse_nested_parens('   ') == []
    # Multiple spaces between groups are ignored
    assert module_0.parse_nested_parens('(())  ()  (()())') == [2, 1, 2]
    # Single group with simple nesting
    assert module_0.parse_nested_parens('(())') == [2]
    # Mixed depths across groups
    assert module_0.parse_nested_parens('(()(())) ()') == [3, 1]
    # Group with adjacent sibling nests
    assert module_0.parse_nested_parens('((())()())') == [3]
    print('test_parse_nested_parens passed')


if __name__ == '__main__':
    test_parse_nested_parens()

# Generated at 2026-11-02 17:34:06.654585
# Unit test for function parse_nested_parens
def test_parse_nested_parens():
    # Basic example with multiple groups
    assert module_0.parse_nested_parens('(()()) ((())) () ((())())') == [2, 3, 1, 3]

    # Single group
    assert module_0.parse_nested_parens('((()))') == [3]

    # Simple non-nested group
    assert module_0.parse_nested_parens('()') == [1]

    # Deeply nested single group
    assert module_0.parse_nested_parens('(((())))') == [4]

    # Multiple groups with varying depths
    assert module_0.parse_nested_parens('() (()) ((())) (((())))') == [1, 2, 3, 4]

    # Empty string returns empty list
    assert module_0.parse_nested_parens('') == []

    # String with only spaces returns empty list
    assert module_0.parse_nested_parens('   ') == []

    # Multiple consecutive spaces between groups are handled
    assert module_0.parse_nested_parens('(())  (()())') == [2, 2]

    # Leading and trailing spaces are ignored
    assert module_0.parse_nested_parens('  (())  ') == [2]

    # Alternating shallow and deep groups
    assert module_0.parse_nested_parens('(()(())) () ((())(()))') == [3, 1, 3]

    # Single pair repeated
    assert module_0.parse_nested_parens('() () ()') == [1, 1, 1]

    # One character group ('(' unclosed still counts depth)
    assert module_0.parse_nested_parens('(') == [1]

    print("All tests passed!")


if __name__ == "__main__":
    test_parse_nested_parens()

# Generated at 2026-11-02 17:35:42.090338
# Unit test for function parse_nested_parens
def test_parse_nested_parens():
    # Classic example with multiple groups
    assert module_0.parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 1, 3]
    # Single group with one level of nesting
    assert module_0.parse_nested_parens('()') == [1]
    # Deeply nested single group
    assert module_0.parse_nested_parens('(((())))') == [4]
    # Multiple groups with the same depth
    assert module_0.parse_nested_parens('(()) (())') == [2, 2]
    # Empty string yields an empty list
    assert module_0.parse_nested_parens('') == []
    # Extra spaces between groups are ignored
    assert module_0.parse_nested_parens('  () ((()))  ') == [1, 3]
    # Maximum depth determined by the deepest group
    assert module_0.parse_nested_parens('()((()))') == [3]
    # Mixed depths in order
    assert module_0.parse_nested_parens('(()()) ((())) ()') == [2, 3, 1]


if __name__ == '__main__':
    test_parse_nested_parens()
    print("All tests passed.")

# Generated at 2026-11-02 17:37:28.578258
# Unit test for function parse_nested_parens
def test_parse_nested_parens():
    # Canonical example from the docstring
    assert module_0.parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 1, 3]

    # Single simple group
    assert module_0.parse_nested_parens('()') == [1]

    # Single nested group
    assert module_0.parse_nested_parens('(())') == [2]
    assert module_0.parse_nested_parens('((()))') == [3]

    # Deeply nested group
    assert module_0.parse_nested_parens('(()(()))') == [3]

    # Multiple groups in one call
    assert module_0.parse_nested_parens('() (()) ((()))') == [1, 2, 3]
    assert module_0.parse_nested_parens('((())) (()())') == [3, 2]

    # Empty input yields empty result
    assert module_0.parse_nested_parens('') == []

    # Multiple spaces between groups are handled (empty strings filtered out)
    assert module_0.parse_nested_parens('()  (())') == [1, 2]

    # Groups with interleaved nesting
    assert module_0.parse_nested_parens('(()()) ((())) () ((())()()) (()())') == [2, 3, 1, 3, 2]

    # Single group without spaces
    assert module_0.parse_nested_parens('((()()))') == [3]

    print("All tests passed!")


if __name__ == "__main__":
    test_parse_nested_parens()