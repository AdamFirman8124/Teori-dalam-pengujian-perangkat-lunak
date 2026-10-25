

# Generated at 2026-10-24 13:29:30.004187
# Unit test for function filter_by_prefix

# Generated at 2026-10-24 13:29:32.420372
# Unit test for function filter_by_prefix

# Generated at 2026-10-24 13:29:34.837303
# Unit test for function filter_by_prefix

# Generated at 2026-10-24 13:29:58.363068
# Unit test for function filter_by_prefix
def test_filter_by_prefix():assert module_0.filter_by_prefix(["apple", "apricot", "banana"], "ap") == ["apple", "apricot"]

# Generated at 2026-10-24 13:30:09.015177
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    assert module_0.filter_by_prefix(["apple", "banana", "apricot"], "ap") == ["apple", "apricot"]
    assert module_0.filter_by_prefix(["apple", "banana"], "z") == []
    assert module_0.filter_by_prefix([], "ap") == []
    assert module_0.filter_by_prefix(["apple", "banana"], "") == ["apple", "banana"]
    assert module_0.filter_by_prefix(["Apple", "apple"], "ap") == ["apple"]

# Generated at 2026-10-24 13:30:10.392079
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    assert module_0.filter_by_prefix(["apple", "apricot", "banana"], "ap") == ["apple", "apricot"]
    assert module_0.filter_by_prefix(["hello", "world"], "z") == []
    assert module_0.filter_by_prefix([], "a") == []
    assert module_0.filter_by_prefix(["abc", "def"], "") == ["abc", "def"]
    assert module_0.filter_by_prefix(["test", "testing", "tester"], "test") == ["test", "testing", "tester"]
    assert module_0.filter_by_prefix(["Apple", "apple"], "ap") == ["apple"]

# Generated at 2026-10-24 13:30:11.784093
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    assert module_0.filter_by_prefix(["apple", "banana", "apricot"], "ap") == ["apple", "apricot"]
    assert module_0.filter_by_prefix(["apple", "banana"], "z") == []
    assert module_0.filter_by_prefix([], "ap") == []
    assert module_0.filter_by_prefix(["apple", "banana"], "") == ["apple", "banana"]
    assert module_0.filter_by_prefix(["Apple", "apple"], "ap") == ["apple"]