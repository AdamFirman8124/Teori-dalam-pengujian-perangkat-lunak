

# Generated at 2026-10-24 22:33:58.365580
# Unit test for function parse_nested_parens

# Generated at 2026-10-24 22:34:00.888697
# Unit test for function parse_nested_parens

# Generated at 2026-10-24 22:34:03.308168
# Unit test for function parse_nested_parens

# Generated at 2026-10-24 22:34:10.810673
# Unit test for function parse_nested_parens
def test_parse_nested_parens():assert module_0.parse_nested_parens("(()()) ((())) () ((())()())") == [2, 3, 1, 3]

# Generated at 2026-10-24 22:34:15.524631
# Unit test for function parse_nested_parens
def test_parse_nested_parens():
    assert module_0.parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 0, 3]
    assert module_0.parse_nested_parens('()') == [0]
    assert module_0.parse_nested_parens('(())') == [1]
    assert module_0.parse_nested_parens('((()))') == [2]
    assert module_0.parse_nested_parens('(()())') == [2]
    assert module_0.parse_nested_parens('') == []
    assert module_0.parse_nested_parens('   ') == []
    assert module_0.parse_nested_parens('(()) () ((()))') == [1, 0, 2]
    print("All tests passed!")


test_parse_nested_parens()

# Generated at 2026-10-24 22:34:16.952913
# Unit test for function parse_nested_parens
def test_parse_nested_parens():
    assert module_0.parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 0, 3]
    assert module_0.parse_nested_parens('()') == [0]
    assert module_0.parse_nested_parens('(())') == [1]
    assert module_0.parse_nested_parens('((()))') == [2]
    assert module_0.parse_nested_parens('(()())') == [2]
    assert module_0.parse_nested_parens('') == []
    assert module_0.parse_nested_parens('   ') == []
    assert module_0.parse_nested_parens('(()) () ((()))') == [1, 0, 2]
    print("All tests passed!")


test_parse_nested_parens()

# Generated at 2026-10-24 22:34:18.275326
# Unit test for function parse_nested_parens
def test_parse_nested_parens():
    assert module_0.parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 0, 3]
    assert module_0.parse_nested_parens('()') == [0]
    assert module_0.parse_nested_parens('(())') == [1]
    assert module_0.parse_nested_parens('((()))') == [2]
    assert module_0.parse_nested_parens('(()())') == [2]
    assert module_0.parse_nested_parens('') == []
    assert module_0.parse_nested_parens('   ') == []
    assert module_0.parse_nested_parens('(()) () ((()))') == [1, 0, 2]
    print("All tests passed!")


test_parse_nested_parens()