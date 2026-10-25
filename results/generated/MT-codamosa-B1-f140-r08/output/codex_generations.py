

# Generated at 2026-10-24 14:17:16.395523
# Unit test for function fix_spaces
def test_fix_spaces():
    # no spaces
    assert module_0.fix_spaces("") == ""
    assert module_0.fix_spaces("abc") == "abc"

    # 1-2 spaces -> underscores
    assert module_0.fix_spaces("a b") == "a_b"
    assert module_0.fix_spaces("a  b") == "a__b"

    # 3+ spaces -> single hyphen (run collapses, not repeated)
    assert module_0.fix_spaces("a   b") == "a-b"
    assert module_0.fix_spaces("a     b") == "a-b"

    # leading / trailing runs
    assert module_0.fix_spaces("  a") == "__a"
    assert module_0.fix_spaces("a  ") == "a__"
    assert module_0.fix_spaces("a   ") == "a-"
    assert module_0.fix_spaces("   ") == "-"

    # mixed
    assert module_0.fix_spaces("a  b   c") == "a__b-c"
    assert module_0.fix_spaces("  hello  world  ") == "__hello__world__"


if __name__ == "__main__":
    test_fix_spaces()
    print("all fix_spaces tests passed")

# Generated at 2026-10-24 14:17:18.811697
# Unit test for function fix_spaces

# Generated at 2026-10-24 14:17:21.226573
# Unit test for function fix_spaces

# Generated at 2026-10-24 14:17:23.638092
# Unit test for function fix_spaces

# Generated at 2026-10-24 14:17:26.054650
# Unit test for function fix_spaces

# Generated at 2026-10-24 14:17:28.473077
# Unit test for function fix_spaces

# Generated at 2026-10-24 14:17:30.891175
# Unit test for function fix_spaces

# Generated at 2026-10-24 14:17:33.304787
# Unit test for function fix_spaces

# Generated at 2026-10-24 14:17:35.719153
# Unit test for function fix_spaces

# Generated at 2026-10-24 14:17:38.133907
# Unit test for function fix_spaces

# Generated at 2026-10-24 14:17:40.548335
# Unit test for function fix_spaces

# Generated at 2026-10-24 14:17:42.960409
# Unit test for function fix_spaces

# Generated at 2026-10-24 14:17:45.378300
# Unit test for function fix_spaces