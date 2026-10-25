

# Generated at 2026-10-24 12:20:27.195434
# Unit test for function parse_nested_parens
def test_parse_nested_parens():
    assert module_0.parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 0, 3]
    assert module_0.parse_nested_parens('()') == [0]
    assert module_0.parse_nested_parens('(())') == [1]
    assert module_0.parse_nested_parens('((()))') == [2]
    assert module_0.parse_nested_parens('') == []
    assert module_0.parse_nested_parens('   ') == []  # only spaces
    assert module_0.parse_nested_parens('(()()) ((()))') == [2, 3]
    print("All tests passed!")


if __name__ == "__main__":
    test_parse_nested_parens()

# Generated at 2026-10-24 12:20:29.617574
# Unit test for function parse_nested_parens

# Generated at 2026-10-24 12:20:32.208263
# Unit test for function parse_nested_parens

# Generated at 2026-10-24 12:20:34.718758
# Unit test for function parse_nested_parens

# Generated at 2026-10-24 12:20:37.138757
# Unit test for function parse_nested_parens

# Generated at 2026-10-24 12:20:43.157695
# Unit test for function parse_nested_parens
def test_parse_nested_parens():
    # Single group
    assert module_0.parse_nested_parens("()") == [1]
    assert module_0.parse_nested_parens("(())") == [2]
    assert module_0.parse_nested_parens("((()))") == [3]

    # Multiple groups separated by spaces
    assert module_0.parse_nested_parens("() (()) ((()))") == [1, 2, 3]
    assert module_0.parse_nested_parens("(()()) ((())) () ((()()))") == [2, 3, 1, 3]

    # Classic example
    assert module_0.parse_nested_parens("(()()) ((())) () ((())()())") == [2, 3, 1, 3]

    # Empty string yields empty list
    assert module_0.parse_nested_parens("") == []

    # Multiple spaces between groups are ignored
    assert module_0.parse_nested_parens("()  (())   ((()))") == [1, 2, 3]

    # Deeply nested single group
    assert module_0.parse_nested_parens("((((()))))") == [5]

    # Alternating shallow and deep groups
    assert module_0.parse_nested_parens("(()) () ((())) () (())") == [2, 1, 3, 1, 2]

# Generated at 2026-10-24 12:20:44.512081
# Unit test for function parse_nested_parens
def test_parse_nested_parens():
    assert module_0.parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 0, 3]
    assert module_0.parse_nested_parens('()') == [0]
    assert module_0.parse_nested_parens('(())') == [1]
    assert module_0.parse_nested_parens('((()))') == [2]
    assert module_0.parse_nested_parens('') == []
    assert module_0.parse_nested_parens('   ') == []  # only spaces
    assert module_0.parse_nested_parens('(()()) ((()))') == [2, 3]
    print("All tests passed!")


if __name__ == "__main__":
    test_parse_nested_parens()

# Generated at 2026-10-24 12:20:45.853153
# Unit test for function parse_nested_parens
def test_parse_nested_parens():
    assert module_0.parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 0, 3]
    assert module_0.parse_nested_parens('()') == [0]
    assert module_0.parse_nested_parens('(())') == [1]
    assert module_0.parse_nested_parens('((()))') == [2]
    assert module_0.parse_nested_parens('') == []
    assert module_0.parse_nested_parens('   ') == []  # only spaces
    assert module_0.parse_nested_parens('(()()) ((()))') == [2, 3]
    print("All tests passed!")


if __name__ == "__main__":
    test_parse_nested_parens()