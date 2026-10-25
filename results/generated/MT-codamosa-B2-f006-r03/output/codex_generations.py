

# Generated at 2026-10-24 11:01:12.416557
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

# Generated at 2026-10-24 11:01:14.836191
# Unit test for function parse_nested_parens

# Generated at 2026-10-24 11:01:17.253679
# Unit test for function parse_nested_parens

# Generated at 2026-10-24 11:01:19.670636
# Unit test for function parse_nested_parens

# Generated at 2026-10-24 11:01:47.661314
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

# Generated at 2026-10-24 11:01:50.081028
# Unit test for function parse_nested_parens

# Generated at 2026-10-24 11:01:52.498975
# Unit test for function parse_nested_parens

# Generated at 2026-10-24 11:01:54.915589
# Unit test for function parse_nested_parens

# Generated at 2026-10-24 11:01:57.336091
# Unit test for function parse_nested_parens

# Generated at 2026-10-24 11:01:59.754477
# Unit test for function parse_nested_parens

# Generated at 2026-10-24 11:02:02.174582
# Unit test for function parse_nested_parens