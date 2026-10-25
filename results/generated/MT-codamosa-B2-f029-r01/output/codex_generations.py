

# Generated at 2026-10-24 11:00:11.369201
# Unit test for function filter_by_prefix

# Generated at 2026-10-24 11:00:13.790002
# Unit test for function filter_by_prefix

# Generated at 2026-10-24 11:00:16.209154
# Unit test for function filter_by_prefix

# Generated at 2026-10-24 11:00:18.628080
# Unit test for function filter_by_prefix

# Generated at 2026-10-24 11:00:26.347777
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    assert module_0.filter_by_prefix([], 'a') == []
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'b') == ['bcd']
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'c') == ['cde']
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'd') == []
    assert module_0.filter_by_prefix(['abc', 'abcd', 'ab'], 'ab') == ['abc', 'abcd', 'ab']
    assert module_0.filter_by_prefix(['', 'a', 'ab'], '') == ['', 'a', 'ab']
    assert module_0.filter_by_prefix(['hello'], 'hello') == ['hello']
    assert module_0.filter_by_prefix(['hello'], 'hello world') == []

# Generated at 2026-10-24 11:00:28.078041
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    assert module_0.filter_by_prefix(["apple", "apricot", "banana"], "ap") == ["apple", "apricot"]
    assert module_0.filter_by_prefix(["hello", "world"], "z") == []
    assert module_0.filter_by_prefix([], "a") == []
    assert module_0.filter_by_prefix(["abc", "def"], "") == ["abc", "def"]
    assert module_0.filter_by_prefix(["test", "testing", "tester"], "test") == ["test", "testing", "tester"]
    assert module_0.filter_by_prefix(["Apple", "apple"], "ap") == ["apple"]

# Generated at 2026-10-24 11:00:29.510298
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    assert module_0.filter_by_prefix(["apple", "apricot", "banana"], "ap") == ["apple", "apricot"]
    assert module_0.filter_by_prefix(["hello", "world"], "z") == []
    assert module_0.filter_by_prefix([], "a") == []
    assert module_0.filter_by_prefix(["abc", "def"], "") == ["abc", "def"]
    assert module_0.filter_by_prefix(["test", "testing", "tester"], "test") == ["test", "testing", "tester"]
    assert module_0.filter_by_prefix(["Apple", "apple"], "ap") == ["apple"]

# Generated at 2026-10-24 11:00:30.878776
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    assert module_0.filter_by_prefix(["apple", "apricot", "banana"], "ap") == ["apple", "apricot"]
    assert module_0.filter_by_prefix(["hello", "world"], "z") == []
    assert module_0.filter_by_prefix([], "a") == []
    assert module_0.filter_by_prefix(["abc", "def"], "") == ["abc", "def"]
    assert module_0.filter_by_prefix(["test", "testing", "tester"], "test") == ["test", "testing", "tester"]
    assert module_0.filter_by_prefix(["Apple", "apple"], "ap") == ["apple"]