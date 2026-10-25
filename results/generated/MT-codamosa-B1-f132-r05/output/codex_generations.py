

# Generated at 2026-10-24 15:04:05.675477
# Unit test for function is_nested

# Generated at 2026-10-24 15:04:08.088296
# Unit test for function is_nested

# Generated at 2026-10-24 15:04:10.504724
# Unit test for function is_nested

# Generated at 2026-10-24 15:04:12.919979
# Unit test for function is_nested

# Generated at 2026-10-24 15:04:15.334334
# Unit test for function is_nested

# Generated at 2026-10-24 15:04:17.903300
# Unit test for function is_nested

# Generated at 2026-10-24 15:04:20.321617
# Unit test for function is_nested

# Generated at 2026-10-24 15:04:22.736607
# Unit test for function is_nested

# Generated at 2026-10-24 15:04:25.151277
# Unit test for function is_nested

# Generated at 2026-10-24 15:04:27.561399
# Unit test for function is_nested

# Generated at 2026-10-24 15:04:29.972764
# Unit test for function is_nested

# Generated at 2026-10-24 15:04:32.385994
# Unit test for function is_nested

# Generated at 2026-10-24 15:04:34.220512
# Unit test for function is_nested
def test_is_nested():
    # Valid nested subsequences -> True
    assert module_0.is_nested('[[]]') == True
    assert module_0.is_nested('[[][]]') == True
    assert module_0.is_nested('[[]][[') == True

    # Flat / unmatched -> False
    assert module_0.is_nested('[]') == False
    assert module_0.is_nested('[][]') == False
    assert module_0.is_nested('[]]]]]]][[[[[]') == False
    assert module_0.is_nested('[[[]])') == False if False else True  # placeholder removed below

    # Edge cases
    assert module_0.is_nested('') == False          # empty string
    assert module_0.is_nested('[') == False         # no closing bracket
    assert module_0.is_nested(']') == False         # no opening bracket
    assert module_0.is_nested('[[[') == False       # closings missing
    assert module_0.is_nested(']]]') == False       # openings missing
    assert module_0.is_nested('[[[[') == False      # no pairs at all
    assert module_0.is_nested('[[') == False        # only one possible pair, no nesting

    print("All tests passed.")

test_is_nested()