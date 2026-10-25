

# Generated at 2026-10-24 07:58:07.496412
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    # Basic match
    assert module_0.filter_by_prefix(["apple", "banana", "avocado"], "a") == ["apple", "avocado"]
    
    # No matches
    assert module_0.filter_by_prefix(["apple", "banana"], "z") == []
    
    # Empty prefix matches everything
    assert module_0.filter_by_prefix(["apple", "banana"], "") == ["apple", "banana"]
    
    # Empty list
    assert module_0.filter_by_prefix([], "a") == []
    
    # Full-string prefix
    assert module_0.filter_by_prefix(["apple", "applesauce", "app"], "app") == ["apple", "applesauce", "app"]
    
    # Case sensitivity: 'A' != 'a'
    assert module_0.filter_by_prefix(["Apple", "apple"], "a") == ["apple"]
    
    # Exact match only
    assert module_0.filter_by_prefix(["abc"], "abc") == ["abc"]
    
    print("All tests passed!")

test_filter_by_prefix()

# Generated at 2026-10-24 07:58:08.864606
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    # Basic match
    assert module_0.filter_by_prefix(["apple", "banana", "avocado"], "a") == ["apple", "avocado"]
    
    # No matches
    assert module_0.filter_by_prefix(["apple", "banana"], "z") == []
    
    # Empty prefix matches everything
    assert module_0.filter_by_prefix(["apple", "banana"], "") == ["apple", "banana"]
    
    # Empty list
    assert module_0.filter_by_prefix([], "a") == []
    
    # Full-string prefix
    assert module_0.filter_by_prefix(["apple", "applesauce", "app"], "app") == ["apple", "applesauce", "app"]
    
    # Case sensitivity: 'A' != 'a'
    assert module_0.filter_by_prefix(["Apple", "apple"], "a") == ["apple"]
    
    # Exact match only
    assert module_0.filter_by_prefix(["abc"], "abc") == ["abc"]
    
    print("All tests passed!")

test_filter_by_prefix()

# Generated at 2026-10-24 07:58:10.180179
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    # Basic match
    assert module_0.filter_by_prefix(["apple", "banana", "avocado"], "a") == ["apple", "avocado"]
    
    # No matches
    assert module_0.filter_by_prefix(["apple", "banana"], "z") == []
    
    # Empty prefix matches everything
    assert module_0.filter_by_prefix(["apple", "banana"], "") == ["apple", "banana"]
    
    # Empty list
    assert module_0.filter_by_prefix([], "a") == []
    
    # Full-string prefix
    assert module_0.filter_by_prefix(["apple", "applesauce", "app"], "app") == ["apple", "applesauce", "app"]
    
    # Case sensitivity: 'A' != 'a'
    assert module_0.filter_by_prefix(["Apple", "apple"], "a") == ["apple"]
    
    # Exact match only
    assert module_0.filter_by_prefix(["abc"], "abc") == ["abc"]
    
    print("All tests passed!")

test_filter_by_prefix()

# Generated at 2026-10-24 07:58:11.529443
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    # Basic match
    assert module_0.filter_by_prefix(["apple", "banana", "avocado"], "a") == ["apple", "avocado"]
    
    # No matches
    assert module_0.filter_by_prefix(["apple", "banana"], "z") == []
    
    # Empty prefix matches everything
    assert module_0.filter_by_prefix(["apple", "banana"], "") == ["apple", "banana"]
    
    # Empty list
    assert module_0.filter_by_prefix([], "a") == []
    
    # Full-string prefix
    assert module_0.filter_by_prefix(["apple", "applesauce", "app"], "app") == ["apple", "applesauce", "app"]
    
    # Case sensitivity: 'A' != 'a'
    assert module_0.filter_by_prefix(["Apple", "apple"], "a") == ["apple"]
    
    # Exact match only
    assert module_0.filter_by_prefix(["abc"], "abc") == ["abc"]
    
    print("All tests passed!")

test_filter_by_prefix()

# Generated at 2026-10-24 07:58:12.859003
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    # Basic match
    assert module_0.filter_by_prefix(["apple", "banana", "avocado"], "a") == ["apple", "avocado"]
    
    # No matches
    assert module_0.filter_by_prefix(["apple", "banana"], "z") == []
    
    # Empty prefix matches everything
    assert module_0.filter_by_prefix(["apple", "banana"], "") == ["apple", "banana"]
    
    # Empty list
    assert module_0.filter_by_prefix([], "a") == []
    
    # Full-string prefix
    assert module_0.filter_by_prefix(["apple", "applesauce", "app"], "app") == ["apple", "applesauce", "app"]
    
    # Case sensitivity: 'A' != 'a'
    assert module_0.filter_by_prefix(["Apple", "apple"], "a") == ["apple"]
    
    # Exact match only
    assert module_0.filter_by_prefix(["abc"], "abc") == ["abc"]
    
    print("All tests passed!")

test_filter_by_prefix()