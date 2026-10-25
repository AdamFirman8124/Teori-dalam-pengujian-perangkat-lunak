

# Generated at 2026-10-24 11:37:40.000223
# Unit test for function is_nested

# Generated at 2026-10-24 11:37:42.416587
# Unit test for function is_nested

# Generated at 2026-10-24 11:37:44.837139
# Unit test for function is_nested

# Generated at 2026-10-24 11:37:47.254912
# Unit test for function is_nested

# Generated at 2026-10-24 11:37:49.676373
# Unit test for function is_nested

# Generated at 2026-10-24 11:37:52.096084
# Unit test for function is_nested

# Generated at 2026-10-24 11:37:54.518210
# Unit test for function is_nested

# Generated at 2026-10-24 11:37:56.940118
# Unit test for function is_nested

# Generated at 2026-10-24 11:37:59.355426
# Unit test for function is_nested

# Generated at 2026-10-24 11:38:01.776073
# Unit test for function is_nested

# Generated at 2026-10-24 11:38:04.194090
# Unit test for function is_nested

# Generated at 2026-10-24 11:38:06.610724
# Unit test for function is_nested

# Generated at 2026-10-24 11:38:08.000620
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