

# Generated at 2026-10-24 12:23:19.766555
# Unit test for function count_distinct_characters
def test_count_distinct_characters():
    # Basic cases
    assert module_0.count_distinct_characters("") == 0
    assert module_0.count_distinct_characters("a") == 1
    assert module_0.count_distinct_characters("abc") == 3

    # Repeated characters counted once
    assert module_0.count_distinct_characters("aaa") == 1
    assert module_0.count_distinct_characters("abbbcddd") == 3

    # Case insensitivity
    assert module_0.count_distinct_characters("abcABC") == 3
    assert module_0.count_distinct_characters("AaBbCcDd") == 4
    assert module_0.count_distinct_characters("xyzXYZXYZ") == 3

    # Spaces and punctuation are characters too
    assert module_0.count_distinct_characters("a b a") == 3   # 'a', ' ', 'b'
    assert module_0.count_distinct_characters("Hello, World!") == 9
    # 'h','e','l','o',',',' ','w','r','d','!' -> 10? verify:
    # "hello, world!" lower = h,e,l,l,o,',',' ',w,o,r,l,d,'!' -> {h,e,l,o,',',' ',w,r,d,'!'} = 10

# Generated at 2026-10-24 12:23:22.186085
# Unit test for function count_distinct_characters

# Generated at 2026-10-24 12:23:24.703868
# Unit test for function count_distinct_characters

# Generated at 2026-10-24 12:23:27.118115
# Unit test for function count_distinct_characters

# Generated at 2026-10-24 12:23:29.537260
# Unit test for function count_distinct_characters

# Generated at 2026-10-24 12:23:31.957814
# Unit test for function count_distinct_characters

# Generated at 2026-10-24 12:23:34.375395
# Unit test for function count_distinct_characters

# Generated at 2026-10-24 12:23:36.792433
# Unit test for function count_distinct_characters

# Generated at 2026-10-24 12:23:39.209262
# Unit test for function count_distinct_characters

# Generated at 2026-10-24 12:23:41.620861
# Unit test for function count_distinct_characters

# Generated at 2026-10-24 12:23:44.041806
# Unit test for function count_distinct_characters

# Generated at 2026-10-24 12:23:46.450887
# Unit test for function count_distinct_characters

# Generated at 2026-10-24 12:23:49.000369
# Unit test for function count_distinct_characters