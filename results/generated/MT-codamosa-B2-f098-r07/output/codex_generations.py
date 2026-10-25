

# Generated at 2026-10-25 01:18:51.921805
# Unit test for function count_upper

# Generated at 2026-10-25 01:18:54.337640
# Unit test for function count_upper

# Generated at 2026-10-25 01:18:56.865572
# Unit test for function count_upper

# Generated at 2026-10-25 01:18:59.280040
# Unit test for function count_upper

# Generated at 2026-10-25 01:19:01.879392
# Unit test for function count_upper

# Generated at 2026-10-25 01:19:04.296374
# Unit test for function count_upper

# Generated at 2026-10-25 01:19:06.712636
# Unit test for function count_upper

# Generated at 2026-10-25 01:19:09.126908
# Unit test for function count_upper

# Generated at 2026-10-25 01:19:11.542067
# Unit test for function count_upper

# Generated at 2026-10-25 01:19:13.956773
# Unit test for function count_upper

# Generated at 2026-10-25 01:19:16.373297
# Unit test for function count_upper

# Generated at 2026-10-25 01:19:19.645808
# Unit test for function count_upper
def test_count_upper():assert module_0.count_upper("AbEcIdOfU") == 5

# Generated at 2026-10-25 01:19:26.357450
# Unit test for function count_upper
def test_count_upper():
    assert module_0.count_upper("") == 0
    assert module_0.count_upper("AEIOU") == 3          # A, I, U are at even indices
    assert module_0.count_upper("AbEcIdO") == 4        # A, E, I, O are at even indices
    assert module_0.count_upper("xAxExIxOxU") == 0     # Vowels are at odd indices
    assert module_0.count_upper("abcdef") == 0         # Lowercase vowels do not count