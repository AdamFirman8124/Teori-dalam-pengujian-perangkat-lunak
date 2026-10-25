

# Generated at 2026-10-24 21:43:29.890506
# Unit test for function histogram

# Generated at 2026-10-24 21:43:32.312019
# Unit test for function histogram

# Generated at 2026-10-24 21:43:34.730477
# Unit test for function histogram

# Generated at 2026-10-24 21:43:37.146981
# Unit test for function histogram

# Generated at 2026-10-24 21:43:39.564889
# Unit test for function histogram

# Generated at 2026-10-24 21:43:41.980536
# Unit test for function histogram

# Generated at 2026-10-24 21:43:44.398968
# Unit test for function histogram

# Generated at 2026-10-24 21:43:46.817401
# Unit test for function histogram

# Generated at 2026-10-24 21:43:49.233506
# Unit test for function histogram

# Generated at 2026-10-24 21:43:51.649871
# Unit test for function histogram

# Generated at 2026-10-24 21:43:54.067908
# Unit test for function histogram

# Generated at 2026-10-24 21:43:56.485798
# Unit test for function histogram

# Generated at 2026-10-24 21:44:03.749181
# Unit test for function histogram
def test_histogram():
    assert module_0.histogram("apple banana apple orange") == {"apple": 2}
    assert module_0.histogram("cat dog cat dog bird") == {"cat": 2, "dog": 2}
    assert module_0.histogram("hello") == {"hello": 1}
    assert module_0.histogram("") == {}
    assert module_0.histogram("  red   blue red  ") == {"red": 2}