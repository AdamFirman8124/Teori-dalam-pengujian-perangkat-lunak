

# Generated at 2026-11-02 22:31:55.482607
# Unit test for function fix_spaces
def test_fix_spaces():
    # No spaces - text unchanged
    assert module_0.fix_spaces("Example") == "Example"

    # Single space between words -> underscore
    assert module_0.fix_spaces("Example 1") == "Example_1"

    # Leading single space -> underscore
    assert module_0.fix_spaces(" Example 2") == "_Example_2"

    # Three consecutive spaces -> dash
    assert module_0.fix_spaces(" Example   3") == "_Example-3"

    # Two consecutive spaces -> two underscores
    assert module_0.fix_spaces("Hello  World") == "Hello__World"

    # Three spaces between words -> single dash
    assert module_0.fix_spaces("Hello   World") == "Hello-World"

    # Four spaces between words -> single dash
    assert module_0.fix_spaces("a    b") == "a-b"

    # Trailing single space -> underscore
    assert module_0.fix_spaces("abc ") == "abc_"

    # Trailing two spaces -> one underscore
    assert module_0.fix_spaces("abc  ") == "abc_"

    # Trailing three spaces -> dash
    assert module_0.fix_spaces("abc   ") == "abc-"

    # Leading two spaces -> two underscores
    assert module_0.fix_spaces("  ab") == "__ab"

    # Leading three spaces -> dash
    assert module_0.fix_spaces("   ab") == "-ab"

    # Empty string
    assert module_0.fix_spaces("") == ""

    # Only spaces
    assert module_0.fix_spaces(" ") == "_"
    assert module_0.fix_spaces("  ") == "_"
    assert module_0.fix_spaces("   ") == "-"

    # Mixed spacing pattern
    assert module_0.fix_spaces("a b  c   d") == "a_b__c-d"

    # No spaces, single character
    assert module_0.fix_spaces("x") == "x"

# Generated at 2026-11-02 22:33:40.520130
# Unit test for function fix_spaces
def test_fix_spaces():
    # No spaces — text unchanged
    assert module_0.fix_spaces("") == ""
    assert module_0.fix_spaces("example") == "example"
    assert module_0.fix_spaces("plainText") == "plainText"

    # Single space -> single underscore
    assert module_0.fix_spaces("example 1") == "example_1"
    assert module_0.fix_spaces(" example") == "_example"
    assert module_0.fix_spaces("example ") == "example_"

    # Two consecutive spaces -> two underscores
    assert module_0.fix_spaces("example  2") == "example__2"
    assert module_0.fix_spaces("a  b") == "a__b"

    # Three or more consecutive spaces -> single dash
    assert module_0.fix_spaces("example   3") == "example-3"
    assert module_0.fix_spaces("example    4") == "example-4"
    assert module_0.fix_spaces("   example") == "-example"
    assert module_0.fix_spaces("example   ") == "example-"

    # Input consisting only of spaces
    assert module_0.fix_spaces(" ") == "_"
    assert module_0.fix_spaces("  ") == "__"
    assert module_0.fix_spaces("   ") == "-"

    # Multiple groups of spaces
    assert module_0.fix_spaces("a  b   c") == "a__b-c"
    assert module_0.fix_spaces("a b  c   d") == "a_b__c-d"

    # Mixed punctuation and trailing spaces
    assert module_0.fix_spaces("Hello,   World!") == "Hello,-World!"
    assert module_0.fix_spaces("Hello,   World!  ") == "Hello,-World!_"

    print("All fix_spaces tests passed!")
# nonce:329e6b4e

# Generated at 2026-11-02 22:34:40.332835
# Unit test for function fix_spaces
def test_fix_spaces():
    # No spaces
    assert module_0.fix_spaces("example") == "example"
    # Single space replaced with underscore
    assert module_0.fix_spaces("example 1") == "example_1"
    # Leading single space
    assert module_0.fix_spaces(" example 2") == "_example_2"
    assert module_0.fix_spaces(" example 3") == "_example_3"
    # Two consecutive spaces become two underscores
    assert module_0.fix_spaces("a  b") == "a__b"
    # Three or more consecutive spaces become a single dash
    assert module_0.fix_spaces("a   b") == "a-b"
    assert module_0.fix_spaces("a    b") == "a-b"
    assert module_0.fix_spaces("a     b") == "a-b"
    # Multiple separated spaces
    assert module_0.fix_spaces("a b c") == "a_b_c"
    assert module_0.fix_spaces("a   b   c") == "a-b-c"
    assert module_0.fix_spaces("a  b   c") == "a__b-c"
    # Trailing spaces
    assert module_0.fix_spaces("a ") == "a_"
    assert module_0.fix_spaces("a  ") == "a_"
    assert module_0.fix_spaces("a   ") == "a-"
    # Only spaces
    assert module_0.fix_spaces("") == ""
    assert module_0.fix_spaces(" ") == "_"
    assert module_0.fix_spaces("  ") == "_"
    assert module_0.fix_spaces("   ") == "-"
    assert module_0.fix_spaces("    ") == "-"
    # Mixed words
    assert module_0.fix_spaces("hello   world  foo") == "hello-world__foo"
    assert module_0.fix_spaces("trailing   ") == "trailing-"
    assert module_0.fix_spaces("  leading") == "__leading"
    print("All fix_spaces tests passed!")


if __name__ == "__main__":
    test_fix_spaces()

# Generated at 2026-11-02 22:35:40.396938
# Unit test for function fix_spaces
def test_fix_spaces():
    # No spaces
    assert module_0.fix_spaces("example") == "example"
    assert module_0.fix_spaces("") == ""

    # Single and double spaces become underscores
    assert module_0.fix_spaces("example 1") == "example_1"
    assert module_0.fix_spaces("example  1") == "example__1"

    # Three or more spaces become a dash
    assert module_0.fix_spaces("example   1") == "example-1"
    assert module_0.fix_spaces("example    1") == "example-1"

    # Leading spaces
    assert module_0.fix_spaces(" example") == "_example"
    assert module_0.fix_spaces("  example") == "__example"
    assert module_0.fix_spaces("   example") == "-example"

    # Trailing spaces
    assert module_0.fix_spaces("example ") == "example_"
    assert module_0.fix_spaces("example  ") == "example_"
    assert module_0.fix_spaces("example   ") == "example-"

    # Only spaces
    assert module_0.fix_spaces(" ") == "_"
    assert module_0.fix_spaces("  ") == "_"
    assert module_0.fix_spaces("   ") == "-"

    # Mixed patterns
    assert module_0.fix_spaces("a  b   c") == "a__b-c"
    assert module_0.fix_spaces("a - b") == "a_-_b"
    assert module_0.fix_spaces("hello   world  foo") == "hello-world__foo"
    assert module_0.fix_spaces("no_spaces_here") == "no_spaces_here"

# Generated at 2026-11-02 22:37:19.624018
# Unit test for function fix_spaces
def test_fix_spaces():
    # nonce:17b66e12
    # No spaces — text unchanged
    assert module_0.fix_spaces("example") == "example"
    assert module_0.fix_spaces("a") == "a"
    assert module_0.fix_spaces("no_spaces_here") == "no_spaces_here"
    assert module_0.fix_spaces("") == ""

    # Single space -> single underscore
    assert module_0.fix_spaces("example 1") == "example_1"
    assert module_0.fix_spaces(" example") == "_example"
    assert module_0.fix_spaces("example ") == "example_"
    assert module_0.fix_spaces("a b c") == "a_b_c"

    # Two consecutive spaces -> two underscores
    assert module_0.fix_spaces("example  1") == "example__1"
    assert module_0.fix_spaces("  example") == "__example"
    assert module_0.fix_spaces("example  ") == "example_"
    assert module_0.fix_spaces("  a  b  ") == "__a__b_"

    # Three or more consecutive spaces -> single dash
    assert module_0.fix_spaces("example   1") == "example-1"
    assert module_0.fix_spaces("   example") == "-example"
    assert module_0.fix_spaces("example   ") == "example-"
    assert module_0.fix_spaces("a    b") == "a-b"
    assert module_0.fix_spaces("hello   world") == "hello-world"
    assert module_0.fix_spaces("a   b   c") == "a-b-c"

    # Mixed runs of different space lengths
    assert module_0.fix_spaces(" four    spaces  test") == "_four-spaces__test"

    # Input consisting only of spaces
    assert module_0.fix_spaces(" ") == "_"
    assert module_0.fix_spaces("  ") == "_"
    assert module_0.fix_spaces("   ") == "-"
    assert module_0.fix_spaces("      ") == "-"

    # Non-space whitespace characters are left untouched
    assert module_0.fix_spaces("a\tb\nc") == "a\tb\nc"