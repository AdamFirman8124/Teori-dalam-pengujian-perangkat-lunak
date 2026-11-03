

# Generated at 2026-11-02 11:37:22.387656
# Unit test for function fix_spaces
def test_fix_spaces():
    # No spaces - text returned unchanged
    assert module_0.fix_spaces("example") == "example"
    assert module_0.fix_spaces("abc") == "abc"

    # Single space -> single underscore
    assert module_0.fix_spaces("example 1") == "example_1"
    assert module_0.fix_spaces("a b c") == "a_b_c"
    assert module_0.fix_spaces("Mudasir Raza") == "Mudasir_Raza"

    # Two consecutive spaces -> two underscores
    assert module_0.fix_spaces("example  1") == "example__1"
    assert module_0.fix_spaces("a  b") == "a__b"

    # Three or more consecutive spaces -> single dash
    assert module_0.fix_spaces("example   1") == "example-1"
    assert module_0.fix_spaces("example    1") == "example-1"
    assert module_0.fix_spaces("hello   world") == "hello-world"
    assert module_0.fix_spaces("hello    world") == "hello-world"
    assert module_0.fix_spaces("Multiple   spaces") == "Multiple-spaces"

    # Leading spaces
    assert module_0.fix_spaces(" example") == "_example"
    assert module_0.fix_spaces("  leading") == "__leading"
    assert module_0.fix_spaces("   leading") == "-leading"

    # Trailing spaces (trailing runs collapse to one "_" or "-")
    assert module_0.fix_spaces("example ") == "example_"
    assert module_0.fix_spaces("example  ") == "example_"
    assert module_0.fix_spaces("example   ") == "example-"
    assert module_0.fix_spaces("abc  x   ") == "abc__x-"

    # Mixed runs within one string
    assert module_0.fix_spaces("a  b   c") == "a__b-c"
    assert module_0.fix_spaces("text with  four spaces") == "text_with__four_spaces"

    # Only spaces / empty string
    assert module_0.fix_spaces("") == ""
    assert module_0.fix_spaces(" ") == "_"
    assert module_0.fix_spaces("  ") == "_"
    assert module_0.fix_spaces("   ") == "-"
    assert module_0.fix_spaces("     ") == "-"

# Generated at 2026-11-02 11:41:10.518274
# Unit test for function fix_spaces
def test_fix_spaces():
    # No spaces — text unchanged
    assert module_0.fix_spaces("example") == "example"
    # Single space replaced by underscore
    assert module_0.fix_spaces("example 1") == "example_1"
    assert module_0.fix_spaces(" example 2") == "_example_2"
    assert module_0.fix_spaces("example 3") == "example_3"
    # Two consecutive spaces -> two underscores
    assert module_0.fix_spaces("hello  world") == "hello__world"
    # Three or more consecutive spaces -> single dash
    assert module_0.fix_spaces("hello   world") == "hello-world"
    assert module_0.fix_spaces("a    b") == "a-b"
    assert module_0.fix_spaces("a     b") == "a-b"
    # Leading spaces
    assert module_0.fix_spaces("  hello") == "__hello"
    assert module_0.fix_spaces("   hello") == "-hello"
    # Trailing spaces (1-2 -> one underscore, 3+ -> dash)
    assert module_0.fix_spaces("hello ") == "hello_"
    assert module_0.fix_spaces("hello  ") == "hello_"
    assert module_0.fix_spaces("hello   ") == "hello-"
    # Mixed groups
    assert module_0.fix_spaces("hello   world  foo") == "hello-world__foo"
    assert module_0.fix_spaces("a  b   c d") == "a__b-c_d"
    assert module_0.fix_spaces("a b c") == "a_b_c"
    # Empty string
    assert module_0.fix_spaces("") == ""
    # Strings consisting only of spaces
    assert module_0.fix_spaces(" ") == "_"
    assert module_0.fix_spaces("  ") == "_"
    assert module_0.fix_spaces("   ") == "-"
    assert module_0.fix_spaces("    ") == "-"
    # Punctuation preserved
    assert module_0.fix_spaces("hello   world!") == "hello-world!"
    print("All test cases passed!")

test_fix_spaces()