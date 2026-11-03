

# Generated at 2026-11-01 21:50:23.799985
# Unit test for function fix_spaces
def test_fix_spaces():
# nonce:28b3538f
    # No spaces: text unchanged
    assert module_0.fix_spaces("Example") == "Example"
    assert module_0.fix_spaces("abc123") == "abc123"

    # Single space between words -> underscore
    assert module_0.fix_spaces("Example 1") == "Example_1"

    # Two consecutive spaces -> two underscores
    assert module_0.fix_spaces("Example  1") == "Example__1"

    # Three consecutive spaces -> single dash
    assert module_0.fix_spaces("Example   1") == "Example-1"

    # More than three consecutive spaces -> still single dash
    assert module_0.fix_spaces("Example    1") == "Example-1"

    # Leading single space -> underscore prefix
    assert module_0.fix_spaces(" Example 2") == "_Example_2"

    # Leading two spaces -> two underscores prefix
    assert module_0.fix_spaces("  Example") == "__Example"

    # Leading three spaces -> dash prefix
    assert module_0.fix_spaces("   Example") == "-Example"

    # Trailing single space -> underscore suffix
    assert module_0.fix_spaces("Example ") == "Example_"

    # Trailing two spaces -> single underscore suffix
    assert module_0.fix_spaces("Example  ") == "Example_"

    # Trailing three spaces -> single dash suffix
    assert module_0.fix_spaces("Example   ") == "Example-"

    # Mixed leading, middle (3 spaces), and trailing (2 spaces)
    assert module_0.fix_spaces(" Hello   World  ") == "_Hello-World_"

    # String of only spaces
    assert module_0.fix_spaces(" ") == "_"
    assert module_0.fix_spaces("  ") == "_"
    assert module_0.fix_spaces("   ") == "-"

    # Empty string
    assert module_0.fix_spaces("") == ""

    # Single non-space character
    assert module_0.fix_spaces("a") == "a"

# Generated at 2026-11-01 21:51:13.389497
# Unit test for function fix_spaces

# Generated at 2026-11-01 21:51:29.606256
# Unit test for function fix_spaces
def test_fix_spaces():
    # No spaces -> unchanged
    assert module_0.fix_spaces("Example") == "Example"
    # Single internal space -> single underscore
    assert module_0.fix_spaces("Example 1") == "Example_1"
    # Two consecutive internal spaces -> two underscores
    assert module_0.fix_spaces("Example  1") == "Example__1"
    # Three or more consecutive internal spaces -> dash
    assert module_0.fix_spaces("Example   1") == "Example-1"
    # Leading space handling
    assert module_0.fix_spaces(" Example 2") == "_Example_2"
    assert module_0.fix_spaces(" Example   3") == "_Example-3"
    # Trailing space handling
    assert module_0.fix_spaces("abc ") == "abc_"
    assert module_0.fix_spaces("ab   ") == "ab-"
    # Edge cases: empty and all-space strings
    assert module_0.fix_spaces("") == ""
    assert module_0.fix_spaces(" ") == "_"
    assert module_0.fix_spaces("  ") == "_"
    assert module_0.fix_spaces("   ") == "-"
    # Mixed content
    assert module_0.fix_spaces("a b  c   d") == "a_b__c-d"

# Generated at 2026-11-01 21:51:57.357297
# Unit test for function fix_spaces
def test_fix_spaces():
    # nonce:ad3c30ba
    # No spaces
    assert module_0.fix_spaces("Example") == "Example"
    assert module_0.fix_spaces("") == ""

    # Single space between words -> single underscore
    assert module_0.fix_spaces("Example 1") == "Example_1"
    assert module_0.fix_spaces("a b") == "a_b"

    # Two consecutive spaces -> two underscores
    assert module_0.fix_spaces("Example  1") == "Example__1"
    assert module_0.fix_spaces("a  b") == "a__b"

    # Three or more consecutive spaces -> single dash
    assert module_0.fix_spaces(" Example   3") == "_Example-3"
    assert module_0.fix_spaces("a   b") == "a-b"
    assert module_0.fix_spaces("a    b") == "a-b"

    # Leading spaces
    assert module_0.fix_spaces(" Example 2") == "_Example_2"
    assert module_0.fix_spaces("   Example") == "-Example"

    # Trailing spaces (trailing 1 or 2 spaces -> one underscore; 3+ -> dash)
    assert module_0.fix_spaces("Example ") == "Example_"
    assert module_0.fix_spaces("Example  ") == "Example_"
    assert module_0.fix_spaces("Example   ") == "Example-"

    # Strings of only spaces
    assert module_0.fix_spaces(" ") == "_"
    assert module_0.fix_spaces("  ") == "_"
    assert module_0.fix_spaces("   ") == "-"
    assert module_0.fix_spaces("    ") == "-"

    # Mixed spacing
    assert module_0.fix_spaces("a b  c   d") == "a_b__c-d"
    assert module_0.fix_spaces("  leading and trailing  ") == "__leading_and_trailing_"


if __name__ == "__main__":
    test_fix_spaces()
    print("All tests passed!")

# Generated at 2026-11-01 21:52:14.399336
# Unit test for function fix_spaces
def test_fix_spaces():
    # Empty string and no spaces
    assert module_0.fix_spaces("") == ""
    assert module_0.fix_spaces("example") == "example"

    # Single spaces replaced with underscores
    assert module_0.fix_spaces("example 1") == "example_1"
    assert module_0.fix_spaces("a b c") == "a_b_c"
    assert module_0.fix_spaces(" example 1") == "_example_1"

    # Two consecutive spaces become two underscores
    assert module_0.fix_spaces("example  1") == "example__1"
    assert module_0.fix_spaces("a  b") == "a__b"

    # More than two consecutive spaces become a dash
    assert module_0.fix_spaces("example   1") == "example-1"
    assert module_0.fix_spaces("example    1") == "example-1"
    assert module_0.fix_spaces("a  b   c") == "a__b-c"

    # Trailing spaces
    assert module_0.fix_spaces("example ") == "example_"
    assert module_0.fix_spaces("example  ") == "example_"
    assert module_0.fix_spaces("example   ") == "example-"

    # Strings consisting only of spaces
    assert module_0.fix_spaces(" ") == "_"
    assert module_0.fix_spaces("  ") == "_"
    assert module_0.fix_spaces("   ") == "-"
    assert module_0.fix_spaces("    ") == "-"


test_fix_spaces()
print("All tests passed!")

# Generated at 2026-11-01 21:52:27.131712
# Unit test for function fix_spaces
def test_fix_spaces():
    # No spaces
    assert module_0.fix_spaces("example") == "example"
    # Single space between words -> underscore
    assert module_0.fix_spaces("example 1") == "example_1"
    assert module_0.fix_spaces("hello world") == "hello_world"
    # Two spaces -> two underscores
    assert module_0.fix_spaces("a  b") == "a__b"
    # Three or more spaces -> single dash
    assert module_0.fix_spaces("a   b") == "a-b"
    assert module_0.fix_spaces("a    b") == "a-b"
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
    assert module_0.fix_spaces("     ") == "-"
    # Empty string
    assert module_0.fix_spaces("") == ""
    # Mixed spacing
    assert module_0.fix_spaces("a b  c   d    e") == "a_b__c-d-e"
    assert module_0.fix_spaces("  start middle   end  ") == "__start_middle-end_"
    # Multiple groups of spaces
    assert module_0.fix_spaces("one  two      three four") == "one__two-three_four"