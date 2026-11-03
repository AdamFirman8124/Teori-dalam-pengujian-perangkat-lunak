

# Generated at 2026-11-02 00:50:52.259002
# Unit test for function count_distinct_characters
def test_count_distinct_characters():
    # Empty string has no characters
    assert module_0.count_distinct_characters("") == 0

    # Single character
    assert module_0.count_distinct_characters("a") == 1

    # All unique characters
    assert module_0.count_distinct_characters("abc") == 3

    # Repeated characters
    assert module_0.count_distinct_characters("aabb") == 2
    assert module_0.count_distinct_characters("aaaa") == 1

    # Case insensitivity
    assert module_0.count_distinct_characters("xyzXYZ") == 3
    assert module_0.count_distinct_characters("aA") == 1

    # Mixed case with repetition
    assert module_0.count_distinct_characters("Jerry") == 4
    assert module_0.count_distinct_characters("Hello, World!") == 10

    # Spaces and punctuation count as characters
    assert module_0.count_distinct_characters("a b a") == 3

    print("All tests passed!")


test_count_distinct_characters()

# Generated at 2026-11-02 00:52:03.733090
# Unit test for function count_distinct_characters
def test_count_distinct_characters():
    # Basic cases with mixed case (case-insensitive)
    assert module_0.count_distinct_characters('xyzXYZ') == 3
    assert module_0.count_distinct_characters('Jerry') == 4

    # All same character, different cases
    assert module_0.count_distinct_characters('aAaA') == 1
    assert module_0.count_distinct_characters('A') == 1

    # Empty string
    assert module_0.count_distinct_characters('') == 0

    # Repeated characters
    assert module_0.count_distinct_characters('abcabc') == 3
    assert module_0.count_distinct_characters('aaaa') == 1

    # String with spaces, punctuation, and digits
    assert module_0.count_distinct_characters('Hello, World!') == 10
    assert module_0.count_distinct_characters('112233') == 1

    # All distinct characters
    assert module_0.count_distinct_characters('abcdefg') == 7

    print("All tests passed!")


test_count_distinct_characters()