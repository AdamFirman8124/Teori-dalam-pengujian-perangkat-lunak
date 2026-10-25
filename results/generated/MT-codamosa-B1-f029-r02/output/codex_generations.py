

# Generated at 2026-10-24 13:06:40.089249
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    strings = ["apple", "application", "banana", "apricot", "grape"]

    result = module_0.filter_by_prefix(strings, "app")

    assert result == ["apple", "application"]

# Generated at 2026-10-24 13:06:41.623258
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    assert module_0.filter_by_prefix(["apple", "apricot", "banana"], "ap") == ["apple", "apricot"]
    assert module_0.filter_by_prefix(["hello", "world"], "z") == []
    assert module_0.filter_by_prefix([], "a") == []
    assert module_0.filter_by_prefix(["abc", "def"], "") == ["abc", "def"]
    assert module_0.filter_by_prefix(["test", "testing", "tester"], "test") == ["test", "testing", "tester"]
    assert module_0.filter_by_prefix(["Apple", "apple"], "ap") == ["apple"]

# Generated at 2026-10-24 13:06:43.057063
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    assert module_0.filter_by_prefix(["apple", "apricot", "banana"], "ap") == ["apple", "apricot"]
    assert module_0.filter_by_prefix(["hello", "world"], "z") == []
    assert module_0.filter_by_prefix([], "a") == []
    assert module_0.filter_by_prefix(["abc", "def"], "") == ["abc", "def"]
    assert module_0.filter_by_prefix(["test", "testing", "tester"], "test") == ["test", "testing", "tester"]
    assert module_0.filter_by_prefix(["Apple", "apple"], "ap") == ["apple"]

# Generated at 2026-10-24 13:06:44.611494
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    assert module_0.filter_by_prefix(["apple", "apricot", "banana"], "ap") == ["apple", "apricot"]
    assert module_0.filter_by_prefix(["hello", "world"], "z") == []
    assert module_0.filter_by_prefix([], "a") == []
    assert module_0.filter_by_prefix(["abc", "def"], "") == ["abc", "def"]
    assert module_0.filter_by_prefix(["test", "testing", "tester"], "test") == ["test", "testing", "tester"]
    assert module_0.filter_by_prefix(["Apple", "apple"], "ap") == ["apple"]

# Generated at 2026-10-24 13:06:57.698247
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    strings = ["apple", "application", "banana", "apricot", "berry"]

    assert module_0.filter_by_prefix(strings, "app") == ["apple", "application"]
    assert module_0.filter_by_prefix(strings, "ban") == ["banana"]
    assert module_0.filter_by_prefix(strings, "z") == []
    assert module_0.filter_by_prefix([], "app") == []
    assert module_0.filter_by_prefix(strings, "") == strings