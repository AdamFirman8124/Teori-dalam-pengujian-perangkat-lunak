

# Generated at 2026-10-25 00:47:22.795253
# Unit test for function parse_nested_parens

# Generated at 2026-10-25 00:47:25.209685
# Unit test for function parse_nested_parens

# Generated at 2026-10-25 00:47:27.635859
# Unit test for function parse_nested_parens

# Generated at 2026-10-25 00:47:30.049663
# Unit test for function parse_nested_parens

# Generated at 2026-10-25 00:47:32.468509
# Unit test for function parse_nested_parens

# Generated at 2026-10-25 00:47:36.166838
# Unit test for function parse_nested_parens
def test_parse_nested_parens():assert module_0.parse_nested_parens("(()()) ((())) () ((())()())") == [2, 3, 1, 3]

# Generated at 2026-10-25 00:47:37.531147
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

# Generated at 2026-10-25 00:47:38.852175
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

# Generated at 2026-10-25 00:47:40.264357
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