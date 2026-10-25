

# Generated at 2026-10-24 11:14:39.542809
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

# Generated at 2026-10-24 11:14:49.572788
# Unit test for function separate_paren_groups
def test_separate_paren_groups():
    assert module_0.separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())']
    assert module_0.separate_paren_groups('()') == ['()']
    assert module_0.separate_paren_groups('(())') == ['(())']
    assert module_0.separate_paren_groups('()()') == ['()', '()']
    assert module_0.separate_paren_groups('') == []
    assert module_0.separate_paren_groups('   ') == []
    assert module_0.separate_paren_groups('(( ))') == ['(())']
    assert module_0.separate_paren_groups('(()())') == ['(()())']

# Generated at 2026-10-24 11:14:50.891275
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

# Generated at 2026-10-24 11:14:52.209362
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

# Generated at 2026-10-24 11:14:53.535598
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