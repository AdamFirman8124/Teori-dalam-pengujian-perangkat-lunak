

# Generated at 2026-10-24 10:58:37.801535
# Unit test for function filter_by_prefix

# Generated at 2026-10-24 10:58:40.218340
# Unit test for function filter_by_prefix

# Generated at 2026-10-24 10:58:42.637352
# Unit test for function filter_by_prefix

# Generated at 2026-10-24 10:58:45.055052
# Unit test for function filter_by_prefix

# Generated at 2026-10-24 10:58:47.470324
# Unit test for function filter_by_prefix

# Generated at 2026-10-24 10:58:49.889406
# Unit test for function filter_by_prefix

# Generated at 2026-10-24 10:58:52.308112
# Unit test for function filter_by_prefix

# Generated at 2026-10-24 10:58:54.726571
# Unit test for function filter_by_prefix

# Generated at 2026-10-24 10:58:57.145899
# Unit test for function filter_by_prefix

# Generated at 2026-10-24 10:58:59.580807
# Unit test for function filter_by_prefix

# Generated at 2026-10-24 10:59:07.179790
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    assert module_0.filter_by_prefix(['abc', 'abd', 'bcd', 'abcd', 'xyz'], 'ab') == ['abc', 'abd', 'abcd']
    assert module_0.filter_by_prefix(['abc', 'abd', 'bcd'], 'b') == ['bcd']
    assert module_0.filter_by_prefix(['abc', 'abd'], 'z') == []
    assert module_0.filter_by_prefix([], 'a') == []
    assert module_0.filter_by_prefix(['hello'], 'hello') == ['hello']
    assert module_0.filter_by_prefix(['hello'], 'hello!') == []
    assert module_0.filter_by_prefix(['a', 'ab', 'abc'], '') == ['a', 'ab', 'abc']

# Generated at 2026-10-24 10:59:15.529996
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    assert module_0.filter_by_prefix(["apple", "apricot", "banana"], "ap") == ["apple", "apricot"]
    assert module_0.filter_by_prefix(["hello", "world"], "z") == []
    assert module_0.filter_by_prefix([], "a") == []
    assert module_0.filter_by_prefix(["abc", "def"], "") == ["abc", "def"]
    assert module_0.filter_by_prefix(["test", "testing", "tester"], "test") == ["test", "testing", "tester"]
    assert module_0.filter_by_prefix(["Apple", "apple"], "ap") == ["apple"]