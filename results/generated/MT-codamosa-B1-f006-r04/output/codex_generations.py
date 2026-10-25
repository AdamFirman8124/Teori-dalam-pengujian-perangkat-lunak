

# Generated at 2026-10-24 19:46:10.919184
# Unit test for function parse_nested_parens
def test_parse_nested_parens():
    assert module_0.parse_nested_parens("(()()) ((())) () ((())()())") == [2, 3, 1, 3]
    assert module_0.parse_nested_parens("() (()) ((())) (((())))") == [1, 2, 3, 4]
    assert module_0.parse_nested_parens("(()(())((())))") == [4]
    assert module_0.parse_nested_parens("") == []
    assert module_0.parse_nested_parens("   ()   (())   ") == [1, 2]

# Generated at 2026-10-24 19:46:17.983879
# Unit test for function parse_nested_parens
def test_parse_nested_parens():
    assert module_0.parse_nested_parens("()") == [1]
    assert module_0.parse_nested_parens("(()) ((())) () ((())()())") == [2, 3, 1, 3]
    assert module_0.parse_nested_parens("() (()) ((())) (((())))") == [1, 2, 3, 4]
    assert module_0.parse_nested_parens("  ()   (())  ") == [1, 2]
    assert module_0.parse_nested_parens("") == []

# Generated at 2026-10-24 19:46:20.528541
# Unit test for function parse_nested_parens

# Generated at 2026-10-24 19:46:22.945408
# Unit test for function parse_nested_parens

# Generated at 2026-10-24 19:46:25.368560
# Unit test for function parse_nested_parens

# Generated at 2026-10-24 19:46:27.796556
# Unit test for function parse_nested_parens

# Generated at 2026-10-24 19:46:30.211862
# Unit test for function parse_nested_parens

# Generated at 2026-10-24 19:46:32.728495
# Unit test for function parse_nested_parens

# Generated at 2026-10-24 19:46:35.143263
# Unit test for function parse_nested_parens

# Generated at 2026-10-24 19:46:37.561928
# Unit test for function parse_nested_parens

# Generated at 2026-10-24 19:46:40.146413
# Unit test for function parse_nested_parens