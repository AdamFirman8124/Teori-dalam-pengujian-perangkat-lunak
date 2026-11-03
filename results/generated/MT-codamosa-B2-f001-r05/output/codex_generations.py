

# Generated at 2026-11-02 14:12:52.536263
# Unit test for function separate_paren_groups
def test_separate_paren_groups():
    # Test basic case with multiple groups separated by spaces
    assert module_0.separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())']

    # Test single simple group
    assert module_0.separate_paren_groups('()') == ['()']

    # Test fully nested single group
    assert module_0.separate_paren_groups('((()))') == ['((()))']

    # Test empty string returns empty list
    assert module_0.separate_paren_groups('') == []

    # Test group surrounded by spaces
    assert module_0.separate_paren_groups(' ( ) ') == ['()']

    # Test multiple adjacent groups with nesting
    assert module_0.separate_paren_groups('((())) (()()) ()') == ['((()))', '(()())', '()']

    # Test adjacent groups without separators
    assert module_0.separate_paren_groups('()()()') == ['()', '()', '()']

    # Test group with no spaces at all
    assert module_0.separate_paren_groups('()((()))') == ['()', '((()))']

    # Test deep nesting within one group
    assert module_0.separate_paren_groups('(()(()))') == ['(()(()))']

    # Test string containing only spaces
    assert module_0.separate_paren_groups('   ') == []

    print("All tests passed!")


if __name__ == "__main__":
    test_separate_paren_groups()

# Generated at 2026-11-02 14:14:35.691097
# Unit test for function separate_paren_groups
def test_separate_paren_groups():
    # Single simple group
    assert module_0.separate_paren_groups("()") == ["()"]

    # Single nested group
    assert module_0.separate_paren_groups("(())") == ["(())"]

    # Deeply nested group
    assert module_0.separate_paren_groups("((()))") == ["((()))"]

    # Multiple sequential groups
    assert module_0.separate_paren_groups("()()") == ["()", "()"]
    assert module_0.separate_paren_groups("()(())") == ["()", "(())"]

    # Spaces between/inside groups are ignored
    assert module_0.separate_paren_groups("( ) (( )) (( )( ))") == ["()", "(())", "(()())"]

    # Complex mixed example
    assert module_0.separate_paren_groups("(()()) ((())) () ((())()())") == [
        "(()())", "((()))", "()", "((())()())"
    ]

    # Empty string yields no groups
    assert module_0.separate_paren_groups("") == []

    # Only spaces yields no groups
    assert module_0.separate_paren_groups("   ") == []

    # Groups are returned in order of completion
    result = module_0.separate_paren_groups("((())) (()()) ()")
    assert result == ["((()))", "(()())", "()"]

    # Each returned group is balanced
    for group in module_0.separate_paren_groups("(()()) ((())) () ((())()())"):
        depth = 0
        for ch in group:
            if ch == '(':
                depth += 1
            elif ch == ')':
                depth -= 1
            assert depth >= 0
        assert depth == 0

    print("All tests passed!")


if __name__ == "__main__":
    test_separate_paren_groups()

# Generated at 2026-11-02 14:16:24.152991
# Unit test for function separate_paren_groups
def test_separate_paren_groups():
    assert module_0.separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())']
    assert module_0.separate_paren_groups('() (()) ((())) (((())))') == ['()', '(())', '((()))', '(((())))']
    assert module_0.separate_paren_groups('(()(())((())))') == ['(()(())((())))']
    assert module_0.separate_paren_groups('()') == ['()']
    assert module_0.separate_paren_groups('(())') == ['(())']
    assert module_0.separate_paren_groups('(()())') == ['(()())']
    assert module_0.separate_paren_groups('') == []
    assert module_0.separate_paren_groups('()(())') == ['()', '(())']
    assert module_0.separate_paren_groups('(( ))') == ['(())']
    assert module_0.separate_paren_groups('((()))(())') == ['((()))', '(())']

# Generated at 2026-11-02 14:17:17.774962
# Unit test for function separate_paren_groups
def test_separate_paren_groups():
    # Classic case with spaces separating groups
    assert module_0.separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())']

    # Single simple group
    assert module_0.separate_paren_groups('()') == ['()']

    # Simple nested group stays together
    assert module_0.separate_paren_groups('(())') == ['(())']

    # Deeply nested group
    assert module_0.separate_paren_groups('((()))') == ['((()))']

    # Multiple sequential groups
    assert module_0.separate_paren_groups('()()()') == ['()', '()', '()']

    # Nested with siblings inside
    assert module_0.separate_paren_groups('(()())') == ['(()())']

    # Empty input yields empty list
    assert module_0.separate_paren_groups('') == []

    # Spaces only yield empty list
    assert module_0.separate_paren_groups('   ') == []

    # Spaces between nested groups are ignored
    assert module_0.separate_paren_groups(' ( ) ( ( ) ) ( ) ') == ['()', '(())', '()']

    # Complex combination of nested and flat groups
    assert module_0.separate_paren_groups('(( )) (()) ( )( )') == ['(())', '(())', '()', '()']

    # Result is always a list of strings
    result = module_0.separate_paren_groups('() (())')
    assert isinstance(result, list)
    assert all(isinstance(g, str) for g in result)

# Generated at 2026-11-02 14:18:38.736861
# Unit test for function separate_paren_groups
def test_separate_paren_groups():
    # Multiple balanced groups separated by spaces
    assert module_0.separate_paren_groups('(()()) ((())) () ((())()())') == [
        '(()())', '((()))', '()', '((())()())'
    ]
    # Progressively nested groups
    assert module_0.separate_paren_groups('() (()) ((())) (((())))') == [
        '()', '(())', '((()))', '(((())))'
    ]
    # Single group
    assert module_0.separate_paren_groups('()') == ['()']
    assert module_0.separate_paren_groups('(()())') == ['(()())']
    # Empty input yields no groups
    assert module_0.separate_paren_groups('') == []
    # Spaces between parentheses are ignored
    assert module_0.separate_paren_groups('( )') == ['()']
    assert module_0.separate_paren_groups('( ) (( ))') == ['()', '(())']
    # Groups without spaces between them are still split correctly
    assert module_0.separate_paren_groups('()(())') == ['()', '(())']
    assert module_0.separate_paren_groups('(()()())') == ['(()()())']