

# Generated at 2026-10-24 12:52:24.427885
# Unit test for function parse_nested_parens
def test_parse_nested_parens():
    assert module_0.parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 1, 3]
    assert module_0.parse_nested_parens('() (()) ((()))') == [1, 2, 3]
    assert module_0.parse_nested_parens('()') == [1]
    assert module_0.parse_nested_parens('(())') == [2]
    assert module_0.parse_nested_parens('((()))') == [3]
    assert module_0.parse_nested_parens('(()(()))') == [3]
    assert module_0.parse_nested_parens('()()') == [1]
    assert module_0.parse_nested_parens('') == []
    assert module_0.parse_nested_parens(' ') == []
    assert module_0.parse_nested_parens('  ()  (())  ') == [1, 2]

# Generated at 2026-10-24 12:52:27.025137
# Unit test for function parse_nested_parens

# Generated at 2026-10-24 12:52:29.439289
# Unit test for function parse_nested_parens

# Generated at 2026-10-24 12:52:31.853185
# Unit test for function parse_nested_parens

# Generated at 2026-10-24 12:52:46.045858
# Unit test for function parse_nested_parens
def test_parse_nested_parens():
    assert module_0.parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 1, 3]
    assert module_0.parse_nested_parens('() (()) ((()))') == [1, 2, 3]
    assert module_0.parse_nested_parens('()') == [1]
    assert module_0.parse_nested_parens('(())') == [2]
    assert module_0.parse_nested_parens('(((())))') == [4]
    assert module_0.parse_nested_parens('() () ()') == [1, 1, 1]
    assert module_0.parse_nested_parens('') == []
    assert module_0.parse_nested_parens('  ()   (())  ') == [1, 2]

# Generated at 2026-10-24 12:52:47.467703
# Unit test for function parse_nested_parens
def test_parse_nested_parens():
    assert module_0.parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 1, 3]
    assert module_0.parse_nested_parens('() (()) ((()))') == [1, 2, 3]
    assert module_0.parse_nested_parens('()') == [1]
    assert module_0.parse_nested_parens('(())') == [2]
    assert module_0.parse_nested_parens('((()))') == [3]
    assert module_0.parse_nested_parens('(()(()))') == [3]
    assert module_0.parse_nested_parens('()()') == [1]
    assert module_0.parse_nested_parens('') == []
    assert module_0.parse_nested_parens(' ') == []
    assert module_0.parse_nested_parens('  ()  (())  ') == [1, 2]

# Generated at 2026-10-24 12:52:48.900268
# Unit test for function parse_nested_parens
def test_parse_nested_parens():
    assert module_0.parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 1, 3]
    assert module_0.parse_nested_parens('() (()) ((()))') == [1, 2, 3]
    assert module_0.parse_nested_parens('()') == [1]
    assert module_0.parse_nested_parens('(())') == [2]
    assert module_0.parse_nested_parens('((()))') == [3]
    assert module_0.parse_nested_parens('(()(()))') == [3]
    assert module_0.parse_nested_parens('()()') == [1]
    assert module_0.parse_nested_parens('') == []
    assert module_0.parse_nested_parens(' ') == []
    assert module_0.parse_nested_parens('  ()  (())  ') == [1, 2]