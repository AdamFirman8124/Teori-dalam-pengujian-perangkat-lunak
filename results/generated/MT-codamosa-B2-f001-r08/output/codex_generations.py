

# Generated at 2026-10-24 15:53:25.950002
# Unit test for function separate_paren_groups
def test_separate_paren_groups():
    # single balanced group
    assert module_0.separate_paren_groups('()') == ['()']
    assert module_0.separate_paren_groups('(())') == ['(())']
    assert module_0.separate_paren_groups('(()())') == ['(()())']

    # multiple groups, no spaces
    assert module_0.separate_paren_groups('()()') == ['()', '()']
    assert module_0.separate_paren_groups('(())(())') == ['(())', '(())']
    assert module_0.separate_paren_groups('()(())(()())') == ['()', '(())', '(()())']

    # canonical example with spaces - spaces are ignored
    assert module_0.separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())']

    # empty / whitespace only
    assert module_0.separate_paren_groups('') == []
    assert module_0.separate_paren_groups('   ') == []

    # spaces between groups are ignored
    assert module_0.separate_paren_groups('  ()  (())  ') == ['()', '(())']

# Generated at 2026-10-24 15:53:42.431677
# Unit test for function separate_paren_groups
def test_separate_paren_groups():
    # single balanced group
    assert module_0.separate_paren_groups('()') == ['()']
    assert module_0.separate_paren_groups('(())') == ['(())']
    assert module_0.separate_paren_groups('(()())') == ['(()())']

    # multiple groups, no spaces
    assert module_0.separate_paren_groups('()()') == ['()', '()']
    assert module_0.separate_paren_groups('(())(())') == ['(())', '(())']
    assert module_0.separate_paren_groups('()(())(()())') == ['()', '(())', '(()())']

    # canonical example with spaces - spaces are ignored
    assert module_0.separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())']

    # empty / whitespace only
    assert module_0.separate_paren_groups('') == []
    assert module_0.separate_paren_groups('   ') == []

    # spaces between groups are ignored
    assert module_0.separate_paren_groups('  ()  (())  ') == ['()', '(())']

# Generated at 2026-10-24 15:53:43.865046
# Unit test for function separate_paren_groups
def test_separate_paren_groups():
    # single balanced group
    assert module_0.separate_paren_groups('()') == ['()']
    assert module_0.separate_paren_groups('(())') == ['(())']
    assert module_0.separate_paren_groups('(()())') == ['(()())']

    # multiple groups, no spaces
    assert module_0.separate_paren_groups('()()') == ['()', '()']
    assert module_0.separate_paren_groups('(())(())') == ['(())', '(())']
    assert module_0.separate_paren_groups('()(())(()())') == ['()', '(())', '(()())']

    # canonical example with spaces - spaces are ignored
    assert module_0.separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())']

    # empty / whitespace only
    assert module_0.separate_paren_groups('') == []
    assert module_0.separate_paren_groups('   ') == []

    # spaces between groups are ignored
    assert module_0.separate_paren_groups('  ()  (())  ') == ['()', '(())']

# Generated at 2026-10-24 15:53:45.299939
# Unit test for function separate_paren_groups
def test_separate_paren_groups():
    # single balanced group
    assert module_0.separate_paren_groups('()') == ['()']
    assert module_0.separate_paren_groups('(())') == ['(())']
    assert module_0.separate_paren_groups('(()())') == ['(()())']

    # multiple groups, no spaces
    assert module_0.separate_paren_groups('()()') == ['()', '()']
    assert module_0.separate_paren_groups('(())(())') == ['(())', '(())']
    assert module_0.separate_paren_groups('()(())(()())') == ['()', '(())', '(()())']

    # canonical example with spaces - spaces are ignored
    assert module_0.separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())']

    # empty / whitespace only
    assert module_0.separate_paren_groups('') == []
    assert module_0.separate_paren_groups('   ') == []

    # spaces between groups are ignored
    assert module_0.separate_paren_groups('  ()  (())  ') == ['()', '(())']

# Generated at 2026-10-24 15:54:01.786890
# Unit test for function separate_paren_groups
def test_separate_paren_groups():
    # single balanced group
    assert module_0.separate_paren_groups('()') == ['()']
    assert module_0.separate_paren_groups('(())') == ['(())']
    assert module_0.separate_paren_groups('(()())') == ['(()())']

    # multiple groups, no spaces
    assert module_0.separate_paren_groups('()()') == ['()', '()']
    assert module_0.separate_paren_groups('(())(())') == ['(())', '(())']
    assert module_0.separate_paren_groups('()(())(()())') == ['()', '(())', '(()())']

    # canonical example with spaces - spaces are ignored
    assert module_0.separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())']

    # empty / whitespace only
    assert module_0.separate_paren_groups('') == []
    assert module_0.separate_paren_groups('   ') == []

    # spaces between groups are ignored
    assert module_0.separate_paren_groups('  ()  (())  ') == ['()', '(())']