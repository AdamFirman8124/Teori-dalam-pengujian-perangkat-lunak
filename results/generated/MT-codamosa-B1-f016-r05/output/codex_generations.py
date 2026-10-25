

# Generated at 2026-10-24 12:08:38.572947
# Unit test for function count_distinct_characters

# Generated at 2026-10-24 12:08:40.949708
# Unit test for function count_distinct_characters

# Generated at 2026-10-24 12:08:43.369011
# Unit test for function count_distinct_characters

# Generated at 2026-10-24 12:08:45.786679
# Unit test for function count_distinct_characters

# Generated at 2026-10-24 12:08:48.211184
# Unit test for function count_distinct_characters

# Generated at 2026-10-24 12:08:50.625794
# Unit test for function count_distinct_characters

# Generated at 2026-10-24 12:08:53.047678
# Unit test for function count_distinct_characters

# Generated at 2026-10-24 12:08:55.466175
# Unit test for function count_distinct_characters

# Generated at 2026-10-24 12:08:57.885169
# Unit test for function count_distinct_characters

# Generated at 2026-10-24 12:09:00.303022
# Unit test for function count_distinct_characters

# Generated at 2026-10-24 12:09:13.285974
# Unit test for function count_distinct_characters
def test_count_distinct_characters():assert module_0.count_distinct_characters("hello") == 4

# Generated at 2026-10-24 12:09:25.344846
# Unit test for function count_distinct_characters
def test_count_distinct_characters():
    assert module_0.count_distinct_characters("") == 0
    assert module_0.count_distinct_characters("a") == 1
    assert module_0.count_distinct_characters("hello") == 4
    assert module_0.count_distinct_characters("Hello") == 4  # case-insensitive
    assert module_0.count_distinct_characters("AaBbCc") == 3
    assert module_0.count_distinct_characters("abcABC") == 3
    assert module_0.count_distinct_characters("123321") == 3
    assert module_0.count_distinct_characters("a A") == 2  # includes space
    assert module_0.count_distinct_characters("!@#!@#") == 3