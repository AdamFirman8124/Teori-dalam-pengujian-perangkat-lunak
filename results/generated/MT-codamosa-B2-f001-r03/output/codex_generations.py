

# Generated at 2026-10-24 11:54:01.354255
# Unit test for function separate_paren_groups

# Generated at 2026-10-24 11:54:03.774530
# Unit test for function separate_paren_groups

# Generated at 2026-10-24 11:54:06.191745
# Unit test for function separate_paren_groups

# Generated at 2026-10-24 11:54:08.613172
# Unit test for function separate_paren_groups

# Generated at 2026-10-24 11:54:11.030316
# Unit test for function separate_paren_groups

# Generated at 2026-10-24 11:54:13.452075
# Unit test for function separate_paren_groups

# Generated at 2026-10-24 11:54:15.870351
# Unit test for function separate_paren_groups

# Generated at 2026-10-24 11:54:18.288014
# Unit test for function separate_paren_groups

# Generated at 2026-10-24 11:54:20.709337
# Unit test for function separate_paren_groups

# Generated at 2026-10-24 11:54:22.401770
# Unit test for function separate_paren_groups
def test_separate_paren_groups():
    # Empty / no parentheses
    assert module_0.separate_paren_groups("") == []
    assert module_0.separate_paren_groups("   ") == []

    # Single group
    assert module_0.separate_paren_groups("()") == ["()"]
    assert module_0.separate_paren_groups("(())") == ["(())"]
    assert module_0.separate_paren_groups("(((())))") == ["(((())))"]

    # Multiple groups
    assert module_0.separate_paren_groups("()()") == ["()", "()"]
    assert module_0.separate_paren_groups("() (()) ()") == ["()", "(())", "()"]

    # Spaces ignored, nested groups kept together
    assert module_0.separate_paren_groups("( ) (( )) (( )( ))") == ["()", "(())", "(()())"]
    assert module_0.separate_paren_groups("(()()) ((()))") == ["(()())", "((()))"]

# Generated at 2026-10-24 11:54:23.709246
# Unit test for function separate_paren_groups
def test_separate_paren_groups():
    # Empty / no parentheses
    assert module_0.separate_paren_groups("") == []
    assert module_0.separate_paren_groups("   ") == []

    # Single group
    assert module_0.separate_paren_groups("()") == ["()"]
    assert module_0.separate_paren_groups("(())") == ["(())"]
    assert module_0.separate_paren_groups("(((())))") == ["(((())))"]

    # Multiple groups
    assert module_0.separate_paren_groups("()()") == ["()", "()"]
    assert module_0.separate_paren_groups("() (()) ()") == ["()", "(())", "()"]

    # Spaces ignored, nested groups kept together
    assert module_0.separate_paren_groups("( ) (( )) (( )( ))") == ["()", "(())", "(()())"]
    assert module_0.separate_paren_groups("(()()) ((()))") == ["(()())", "((()))"]