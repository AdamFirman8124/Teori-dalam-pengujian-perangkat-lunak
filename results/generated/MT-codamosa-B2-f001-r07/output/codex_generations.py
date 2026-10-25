

# Generated at 2026-10-24 12:58:58.774865
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

# Generated at 2026-10-24 12:59:01.191893
# Unit test for function separate_paren_groups

# Generated at 2026-10-24 12:59:03.609900
# Unit test for function separate_paren_groups

# Generated at 2026-10-24 12:59:15.966784
# Unit test for function separate_paren_groups
def test_separate_paren_groups():assert module_0.separate_paren_groups('') == []

# Generated at 2026-10-24 12:59:17.352108
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

# Generated at 2026-10-24 12:59:18.742536
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

# Generated at 2026-10-24 12:59:20.185232
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