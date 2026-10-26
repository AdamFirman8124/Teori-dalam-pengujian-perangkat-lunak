

# Generated at 2026-10-25 12:38:45.316921
# Unit test for function separate_paren_groups

# Generated at 2026-10-25 12:38:47.942735
# Unit test for function separate_paren_groups

# Generated at 2026-10-25 12:38:50.358075
# Unit test for function separate_paren_groups

# Generated at 2026-10-25 12:38:52.772799
# Unit test for function separate_paren_groups

# Generated at 2026-10-25 12:38:55.360312
# Unit test for function separate_paren_groups

# Generated at 2026-10-25 12:38:57.774392
# Unit test for function separate_paren_groups

# Generated at 2026-10-25 12:39:00.188100
# Unit test for function separate_paren_groups

# Generated at 2026-10-25 12:39:02.601076
# Unit test for function separate_paren_groups

# Generated at 2026-10-25 12:39:05.031107
# Unit test for function separate_paren_groups

# Generated at 2026-10-25 12:39:07.440217
# Unit test for function separate_paren_groups

# Generated at 2026-10-25 12:39:09.855148
# Unit test for function separate_paren_groups

# Generated at 2026-10-25 12:39:12.268554
# Unit test for function separate_paren_groups

# Generated at 2026-10-25 12:39:30.319388
# Unit test for function separate_paren_groups
def test_separate_paren_groups():
    # Mixed groups separated by spaces (spaces are ignored by the function)
    assert module_0.separate_paren_groups('(()()) ((())) () ((())()())') == ['(()())', '((()))', '()', '((())()())']

    # Increasing nesting levels, space-separated
    assert module_0.separate_paren_groups('() (()) ((())) (((())))') == ['()', '(())', '((()))', '(((())))']

    # Single deeply nested group
    assert module_0.separate_paren_groups('(((())))') == ['(((())))']

    # Adjacent groups with no separators
    assert module_0.separate_paren_groups('()()()') == ['()', '()', '()']

    # Groups with inline nesting mixed with simple groups
    assert module_0.separate_paren_groups('(()) () (())') == ['(())', '()', '(())']

    # Empty input yields no groups
    assert module_0.separate_paren_groups('') == []

    # Whitespace-only input yields no groups
    assert module_0.separate_paren_groups('   ') == []