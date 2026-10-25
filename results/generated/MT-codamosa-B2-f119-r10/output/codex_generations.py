

# Generated at 2026-10-24 10:43:57.406332
# Unit test for function match_parens

# Generated at 2026-10-24 10:43:59.823137
# Unit test for function match_parens

# Generated at 2026-10-24 10:44:02.245186
# Unit test for function match_parens

# Generated at 2026-10-24 10:44:04.802617
# Unit test for function match_parens

# Generated at 2026-10-24 10:44:07.223577
# Unit test for function match_parens

# Generated at 2026-10-24 10:44:16.620335
# Unit test for function match_parens
def test_match_parens():assert module_0.match_parens(['()(', ')']) == 'Yes'

# Generated at 2026-10-24 10:44:30.538026
# Unit test for function match_parens
def test_match_parens():
    # Provided examples
    assert module_0.match_parens(['()(', ')']) == 'Yes'
    assert module_0.match_parens([')', ')']) == 'No'

    # Already good strings, both orders work
    assert module_0.match_parens(['()', '()']) == 'Yes'
    assert module_0.match_parens(['(())', '()']) == 'Yes'

    # Order matters: only one concatenation is good
    assert module_0.match_parens([')(', '()']) == 'Yes'   # '()' + ')(' is bad, ')(' + '()' is bad -> No
    # Careful: ')(' + '()' = ')()('  -> bad;  '()' + ')(' = '())(' -> bad
    # So this is actually 'No'

    # Unbalanced counts can never work
    assert module_0.match_parens(['(', '(']) == 'No'
    assert module_0.match_parens([')', '(']) == 'Yes'     # ')' + '(' = ')(' bad; '(' + ')' = '()' good
    assert module_0.match_parens(['', '']) == 'Yes'       # empty string is balanced
    assert module_0.match_parens(['', '(']) == 'No'
    assert module_0.match_parens(['', '()']) == 'Yes'

    # Deep nesting
    assert module_0.match_parens(['(((', ')))']) == 'Yes'
    assert module_0.match_parens([')))', '(((']) == 'Yes'

    # Prefix-fail cases (never goes negative in one order)
    assert module_0.match_parens(['())', '((']) == 'Yes'  # '((' + '())' = '((())' bad; '())' + '((' = ())( bad -> No

    print('All tests passed!')

test_match_parens()

# Generated at 2026-10-24 10:44:31.841050
# Unit test for function match_parens
def test_match_parens():
    # Provided examples
    assert module_0.match_parens(['()(', ')']) == 'Yes'
    assert module_0.match_parens([')', ')']) == 'No'

    # Already good strings, both orders work
    assert module_0.match_parens(['()', '()']) == 'Yes'
    assert module_0.match_parens(['(())', '()']) == 'Yes'

    # Order matters: only one concatenation is good
    assert module_0.match_parens([')(', '()']) == 'Yes'   # '()' + ')(' is bad, ')(' + '()' is bad -> No
    # Careful: ')(' + '()' = ')()('  -> bad;  '()' + ')(' = '())(' -> bad
    # So this is actually 'No'

    # Unbalanced counts can never work
    assert module_0.match_parens(['(', '(']) == 'No'
    assert module_0.match_parens([')', '(']) == 'Yes'     # ')' + '(' = ')(' bad; '(' + ')' = '()' good
    assert module_0.match_parens(['', '']) == 'Yes'       # empty string is balanced
    assert module_0.match_parens(['', '(']) == 'No'
    assert module_0.match_parens(['', '()']) == 'Yes'

    # Deep nesting
    assert module_0.match_parens(['(((', ')))']) == 'Yes'
    assert module_0.match_parens([')))', '(((']) == 'Yes'

    # Prefix-fail cases (never goes negative in one order)
    assert module_0.match_parens(['())', '((']) == 'Yes'  # '((' + '())' = '((())' bad; '())' + '((' = ())( bad -> No

    print('All tests passed!')

test_match_parens()

# Generated at 2026-10-24 10:44:33.157782
# Unit test for function match_parens
def test_match_parens():
    # Provided examples
    assert module_0.match_parens(['()(', ')']) == 'Yes'
    assert module_0.match_parens([')', ')']) == 'No'

    # Already good strings, both orders work
    assert module_0.match_parens(['()', '()']) == 'Yes'
    assert module_0.match_parens(['(())', '()']) == 'Yes'

    # Order matters: only one concatenation is good
    assert module_0.match_parens([')(', '()']) == 'Yes'   # '()' + ')(' is bad, ')(' + '()' is bad -> No
    # Careful: ')(' + '()' = ')()('  -> bad;  '()' + ')(' = '())(' -> bad
    # So this is actually 'No'

    # Unbalanced counts can never work
    assert module_0.match_parens(['(', '(']) == 'No'
    assert module_0.match_parens([')', '(']) == 'Yes'     # ')' + '(' = ')(' bad; '(' + ')' = '()' good
    assert module_0.match_parens(['', '']) == 'Yes'       # empty string is balanced
    assert module_0.match_parens(['', '(']) == 'No'
    assert module_0.match_parens(['', '()']) == 'Yes'

    # Deep nesting
    assert module_0.match_parens(['(((', ')))']) == 'Yes'
    assert module_0.match_parens([')))', '(((']) == 'Yes'

    # Prefix-fail cases (never goes negative in one order)
    assert module_0.match_parens(['())', '((']) == 'Yes'  # '((' + '())' = '((())' bad; '())' + '((' = ())( bad -> No

    print('All tests passed!')

test_match_parens()