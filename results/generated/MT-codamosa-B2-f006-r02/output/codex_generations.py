

# Generated at 2026-10-24 07:43:06.683075
# Unit test for function parse_nested_parens
def test_parse_nested_parens():
    assert module_0.parse_nested_parens("()") == [1]
    assert module_0.parse_nested_parens("(()) ((())) ()") == [2, 3, 1]
    assert module_0.parse_nested_parens("(()()) ((())) () ((())()())") == [2, 3, 1, 3]
    assert module_0.parse_nested_parens("(()(())((())))") == [3]
    assert module_0.parse_nested_parens("   ()   (())   ") == [1, 2]
    assert module_0.parse_nested_parens("") == []

# Generated at 2026-10-24 07:43:13.569185
# Unit test for function parse_nested_parens
def test_parse_nested_parens():
    assert module_0.parse_nested_parens("") == []
    assert module_0.parse_nested_parens("()") == [1]
    assert module_0.parse_nested_parens("(())") == [2]
    assert module_0.parse_nested_parens("((()))") == [3]
    assert module_0.parse_nested_parens("(()()) ((())) () ((())()())") == [2, 3, 1, 3]
    assert module_0.parse_nested_parens("()   (())    ((()))") == [1, 2, 3]

# Generated at 2026-10-24 07:43:21.731207
# Unit test for function parse_nested_parens
def test_parse_nested_parens():
    assert module_0.parse_nested_parens("(()()) ((())) () ((())()())") == [2, 3, 1, 3]
    assert module_0.parse_nested_parens("() (()) ((())) (((())))") == [1, 2, 3, 4]
    assert module_0.parse_nested_parens("()") == [1]
    assert module_0.parse_nested_parens("(())  ()") == [2, 1]
    assert module_0.parse_nested_parens("") == []

# Generated at 2026-10-24 07:43:24.288458
# Unit test for function parse_nested_parens

# Generated at 2026-10-24 07:43:26.893963
# Unit test for function parse_nested_parens

# Generated at 2026-10-24 07:43:29.421036
# Unit test for function parse_nested_parens

# Generated at 2026-10-24 07:43:31.923818
# Unit test for function parse_nested_parens

# Generated at 2026-10-24 07:43:34.423983
# Unit test for function parse_nested_parens

# Generated at 2026-10-24 07:43:36.842203
# Unit test for function parse_nested_parens