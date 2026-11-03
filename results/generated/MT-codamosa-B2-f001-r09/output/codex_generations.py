

# Generated at 2026-11-02 21:14:23.584267
# Unit test for function separate_paren_groups
def test_separate_paren_groups():
    # Test basic case: two separate groups
    assert module_0.separate_paren_groups('()()') == ['()', '()']

    # Test nested group (single group)
    assert module_0.separate_paren_groups('(())') == ['(())']

    # Test deeply nested group
    assert module_0.separate_paren_groups('((()))') == ['((()))']

    # Test mixed nested and simple groups
    assert module_0.separate_paren_groups('()(())') == ['()', '(())']

    # Test complex nesting within a single group
    assert module_0.separate_paren_groups('(()())') == ['(()())']

    # Test standard example with spaces (spaces are ignored)
    assert module_0.separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())']

    # Test empty string returns empty list
    assert module_0.separate_paren_groups('') == []

    # Test string with only spaces returns empty list
    assert module_0.separate_paren_groups('   ') == []

    # Test multiple groups separated by spaces
    assert module_0.separate_paren_groups('( ) ( ) ( )') == ['()', '()', '()']

    # Test groups with nesting and spacing mixed
    assert module_0.separate_paren_groups('(() ) (( ))') == ['(())', '(())']

    # Test result is a list
    assert isinstance(module_0.separate_paren_groups('()'), list)

    print("All tests passed!")


if __name__ == "__main__":
    test_separate_paren_groups()

# Generated at 2026-11-02 21:15:16.595767
# Unit test for function separate_paren_groups
def test_separate_paren_groups():
# nonce:afbe2115
    # Basic case: separate groups with spaces between them
    assert module_0.separate_paren_groups('( ) ( )') == ['()', '()']

    # Nested group within a single outer group
    assert module_0.separate_paren_groups('( ( ) )') == ['(())']

    # Classic example: multiple groups with varying nesting
    assert module_0.separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())']

    # No spaces at all
    assert module_0.separate_paren_groups('()()') == ['()', '()']

    # Single nested group
    assert module_0.separate_paren_groups('(()())') == ['(()())']

    # Deeply nested group
    assert module_0.separate_paren_groups('((()))') == ['((()))']

    # Minimal input: one group
    assert module_0.separate_paren_groups('()') == ['()']

    # Empty input string
    assert module_0.separate_paren_groups('') == []

    # Nested group followed by simple group
    assert module_0.separate_paren_groups('(())()') == ['(())', '()']

    # Leading and trailing whitespace should be ignored
    assert module_0.separate_paren_groups('  ()  ') == ['()']

    # Multiple nested groups separated by spaces
    assert module_0.separate_paren_groups('((())) (()())') == ['((()))', '(()())']

    # Only whitespace characters (no parens)
    assert module_0.separate_paren_groups('   ') == []

    print("All tests passed!")


if __name__ == "__main__":
    test_separate_paren_groups()

# Generated at 2026-11-02 21:16:32.380719
# Unit test for function separate_paren_groups
def test_separate_paren_groups():
    # nonce:0b9c3673
    assert module_0.separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())']
    assert module_0.separate_paren_groups('() (()) ((())) (((())))') == ['()', '(())', '((()))', '(((())))']
    assert module_0.separate_paren_groups('(()())') == ['(()())']
    assert module_0.separate_paren_groups('()(())') == ['()', '(())']
    assert module_0.separate_paren_groups('') == []

# Generated at 2026-11-02 21:17:13.688743
# Unit test for function separate_paren_groups
def test_separate_paren_groups():
    # Standard case: multiple groups separated by spaces
    assert module_0.separate_paren_groups('(()()) ((())) () ((())()())') == ['(()())', '((()))', '()', '((())()())']
    # Nested groups of increasing depth
    assert module_0.separate_paren_groups('() (()) ((())) (((())))') == ['()', '(())', '((()))', '(((())))']
    # Single group
    assert module_0.separate_paren_groups('(())') == ['(())']
    # Adjacent groups without spaces
    assert module_0.separate_paren_groups('()()') == ['()', '()']
    # Empty string
    assert module_0.separate_paren_groups('') == []
    # Only spaces
    assert module_0.separate_paren_groups('   ') == []
    # Spaces inside are ignored
    assert module_0.separate_paren_groups(' ( ) ') == ['()']
    # Unbalanced group never completes, so nothing is returned
    assert module_0.separate_paren_groups('(()') == []
    # Single pair
    assert module_0.separate_paren_groups('()') == ['()']
    # Deeply nested single group
    assert module_0.separate_paren_groups('((()))') == ['((()))']

    print('All tests passed!')


if __name__ == '__main__':
    test_separate_paren_groups()

# Generated at 2026-11-02 21:18:29.004954
# Unit test for function separate_paren_groups
def test_separate_paren_groups():
    # Classic example: spaces ignored, groups split at depth zero
    assert module_0.separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())']

    # Single simple group
    assert module_0.separate_paren_groups('()') == ['()']

    # Deeply nested single group stays as one
    assert module_0.separate_paren_groups('((()))') == ['((()))']

    # Multiple consecutive groups
    assert module_0.separate_paren_groups('()()()') == ['()', '()', '()']

    # Simple nesting
    assert module_0.separate_paren_groups('(())') == ['(())']

    # Empty input yields empty result
    assert module_0.separate_paren_groups('') == []

    # Leading/trailing spaces are ignored
    assert module_0.separate_paren_groups('  ( )  ') == ['()']

    # Mixed nesting and consecutive groups
    assert module_0.separate_paren_groups('((()))(()())') == ['((()))', '(()())']

    # Spaces between all tokens
    assert module_0.separate_paren_groups('( ( ) ) ( )') == ['(())', '()']

    print("All tests passed!")


if __name__ == "__main__":
    test_separate_paren_groups()