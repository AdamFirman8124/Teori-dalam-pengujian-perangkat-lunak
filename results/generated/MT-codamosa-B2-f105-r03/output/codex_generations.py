

# Generated at 2026-10-25 06:42:19.906094
# Unit test for function by_length
def test_by_length():
    assert module_0.by_length([2, 1, 1, 4, 3]) == ["Four", "Three", "Two", "One", "One"]
    assert module_0.by_length([]) == []
    assert module_0.by_length([1, -1, 55]) == ["One"]
    assert module_0.by_length([3, 3, 3]) == ["Three", "Three", "Three"]
    assert module_0.by_length([9, 8, 7, 6, 5, 4, 3, 2, 1]) == [
        "Nine", "Eight", "Seven", "Six", "Five",
        "Four", "Three", "Two", "One",
    ]
    print("All tests passed")


test_by_length()

# Generated at 2026-10-25 06:42:21.337499
# Unit test for function by_length
def test_by_length():
    assert module_0.by_length([2, 1, 1, 4, 3]) == ["Four", "Three", "Two", "One", "One"]
    assert module_0.by_length([8, 8, 8]) == ["Eight", "Eight", "Eight"]
    assert module_0.by_length([]) == []
    assert module_0.by_length([10, 0, -1, 100]) == []          # out of range -> dropped
    assert module_0.by_length([9, 5, 12, 1]) == ["Nine", "Five", "One"]  # mixed
    assert module_0.by_length([1]) == ["One"]

# Generated at 2026-10-25 06:42:22.906663
# Unit test for function by_length
def test_by_length():
    assert module_0.by_length([2, 1, 1, 4, 3]) == ["Four", "Three", "Two", "One", "One"]
    assert module_0.by_length([8, 8, 8]) == ["Eight", "Eight", "Eight"]
    assert module_0.by_length([]) == []
    assert module_0.by_length([10, 0, -1, 100]) == []          # out of range -> dropped
    assert module_0.by_length([9, 5, 12, 1]) == ["Nine", "Five", "One"]  # mixed
    assert module_0.by_length([1]) == ["One"]

# Generated at 2026-10-25 06:42:24.239874
# Unit test for function by_length
def test_by_length():
    assert module_0.by_length([2, 1, 1, 4, 3]) == ["Four", "Three", "Two", "One", "One"]
    assert module_0.by_length([8, 8, 8]) == ["Eight", "Eight", "Eight"]
    assert module_0.by_length([]) == []
    assert module_0.by_length([10, 0, -1, 100]) == []          # out of range -> dropped
    assert module_0.by_length([9, 5, 12, 1]) == ["Nine", "Five", "One"]  # mixed
    assert module_0.by_length([1]) == ["One"]

# Generated at 2026-10-25 06:42:25.575188
# Unit test for function by_length
def test_by_length():
    assert module_0.by_length([2, 1, 1, 4, 3]) == ["Four", "Three", "Two", "One", "One"]
    assert module_0.by_length([8, 8, 8]) == ["Eight", "Eight", "Eight"]
    assert module_0.by_length([]) == []
    assert module_0.by_length([10, 0, -1, 100]) == []          # out of range -> dropped
    assert module_0.by_length([9, 5, 12, 1]) == ["Nine", "Five", "One"]  # mixed
    assert module_0.by_length([1]) == ["One"]