

# Generated at 2026-10-24 06:22:41.251860
# Unit test for function histogram
def test_histogram():
    # One most-frequent word
    assert module_0.histogram("apple banana apple orange apple") == {
        "apple": 3
    }

    # Multiple words tied for most frequent
    assert module_0.histogram("cat dog cat dog bird") == {
        "cat": 2,
        "dog": 2
    }

    # All words occur once
    assert module_0.histogram("one two three") == {
        "one": 1,
        "two": 1,
        "three": 1
    }

    # Empty input
    assert module_0.histogram("") == {}

    # Extra spaces should not create an empty-string entry
    assert module_0.histogram("cat  dog") == {
        "cat": 1,
        "dog": 1
    }

# Generated at 2026-10-24 06:22:50.261382
# Unit test for function histogram
def test_histogram():
    assert module_0.histogram("apple banana apple") == {"apple": 2}
    assert module_0.histogram("apple banana apple banana orange") == {
        "apple": 2,
        "banana": 2,
    }
    assert module_0.histogram("apple banana orange") == {
        "apple": 1,
        "banana": 1,
        "orange": 1,
    }
    assert module_0.histogram("") == {}
    assert module_0.histogram("   ") == {}
    assert module_0.histogram("apple  banana") == {
        "apple": 1,
        "banana": 1,
    }

# Generated at 2026-10-24 06:22:52.764450
# Unit test for function histogram

# Generated at 2026-10-24 06:22:55.273295
# Unit test for function histogram

# Generated at 2026-10-24 06:22:57.689959
# Unit test for function histogram

# Generated at 2026-10-24 06:23:00.215706
# Unit test for function histogram

# Generated at 2026-10-24 06:23:02.631059
# Unit test for function histogram

# Generated at 2026-10-24 06:23:05.045537
# Unit test for function histogram

# Generated at 2026-10-24 06:23:07.461101
# Unit test for function histogram

# Generated at 2026-10-24 06:23:09.875634
# Unit test for function histogram

# Generated at 2026-10-24 06:23:12.290998
# Unit test for function histogram