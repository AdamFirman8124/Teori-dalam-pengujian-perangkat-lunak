

# Generated at 2026-10-25 06:32:53.287120
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    assert module_0.filter_by_prefix([], 'a') == []
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'b') == ['bcd']
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'c') == ['cde']
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'd') == []
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], '') == ['abc', 'bcd', 'cde', 'array']
    assert module_0.filter_by_prefix(['abc', 'abcd', 'abcde'], 'abc') == ['abc', 'abcd', 'abcde']
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'ab') == ['abc']
    assert module_0.filter_by_prefix(['ABC', 'abc'], 'a') == ['abc']  # case-sensitive

# Generated at 2026-10-25 06:32:54.654270
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    assert module_0.filter_by_prefix([], 'a') == []
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'b') == ['bcd']
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'c') == ['cde']
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'd') == []
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], '') == ['abc', 'bcd', 'cde', 'array']
    assert module_0.filter_by_prefix(['abc', 'abcd', 'abcde'], 'abc') == ['abc', 'abcd', 'abcde']
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'ab') == ['abc']
    assert module_0.filter_by_prefix(['ABC', 'abc'], 'a') == ['abc']  # case-sensitive

# Generated at 2026-10-25 06:32:56.010012
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    assert module_0.filter_by_prefix([], 'a') == []
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'b') == ['bcd']
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'c') == ['cde']
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'd') == []
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], '') == ['abc', 'bcd', 'cde', 'array']
    assert module_0.filter_by_prefix(['abc', 'abcd', 'abcde'], 'abc') == ['abc', 'abcd', 'abcde']
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'ab') == ['abc']
    assert module_0.filter_by_prefix(['ABC', 'abc'], 'a') == ['abc']  # case-sensitive

# Generated at 2026-10-25 06:32:57.384713
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    assert module_0.filter_by_prefix([], 'a') == []
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'b') == ['bcd']
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'c') == ['cde']
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'd') == []
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], '') == ['abc', 'bcd', 'cde', 'array']
    assert module_0.filter_by_prefix(['abc', 'abcd', 'abcde'], 'abc') == ['abc', 'abcd', 'abcde']
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'ab') == ['abc']
    assert module_0.filter_by_prefix(['ABC', 'abc'], 'a') == ['abc']  # case-sensitive

# Generated at 2026-10-25 06:32:58.732516
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    assert module_0.filter_by_prefix([], 'a') == []
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'b') == ['bcd']
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'c') == ['cde']
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'd') == []
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], '') == ['abc', 'bcd', 'cde', 'array']
    assert module_0.filter_by_prefix(['abc', 'abcd', 'abcde'], 'abc') == ['abc', 'abcd', 'abcde']
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'ab') == ['abc']
    assert module_0.filter_by_prefix(['ABC', 'abc'], 'a') == ['abc']  # case-sensitive