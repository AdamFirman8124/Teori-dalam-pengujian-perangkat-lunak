

# Generated at 2026-10-24 13:29:16.604078
# Unit test for function fix_spaces

# Generated at 2026-10-24 13:29:19.017285
# Unit test for function fix_spaces

# Generated at 2026-10-24 13:29:21.560528
# Unit test for function fix_spaces

# Generated at 2026-10-24 13:29:23.984941
# Unit test for function fix_spaces

# Generated at 2026-10-24 13:29:26.399449
# Unit test for function fix_spaces

# Generated at 2026-10-24 13:29:28.819164
# Unit test for function fix_spaces

# Generated at 2026-10-24 13:29:31.229836
# Unit test for function fix_spaces

# Generated at 2026-10-24 13:29:33.642239
# Unit test for function fix_spaces

# Generated at 2026-10-24 13:29:36.054559
# Unit test for function fix_spaces

# Generated at 2026-10-24 13:30:14.599302
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

# Generated at 2026-10-24 13:30:17.108610
# Unit test for function fix_spaces

# Generated at 2026-10-24 13:30:19.522725
# Unit test for function fix_spaces

# Generated at 2026-10-24 13:30:21.937187
# Unit test for function fix_spaces