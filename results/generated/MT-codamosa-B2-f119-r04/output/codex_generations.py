

# Generated at 2026-11-01 20:52:53.942981
# Unit test for function match_parens
def test_match_parens():
    # nonce:a2e890b5
    # Docstring examples
    assert module_0.match_parens(['()(', ')']) == 'Yes'
    assert module_0.match_parens([')', ')']) == 'No'

    # Both concatenation orders are balanced
    assert module_0.match_parens(['()', '()']) == 'Yes'
    assert module_0.match_parens(['((()))', '((()))']) == 'Yes'
    assert module_0.match_parens(['', '']) == 'Yes'

    # Only one of the two orders is balanced
    assert module_0.match_parens(['(', ')']) == 'Yes'
    assert module_0.match_parens(['((', '))']) == 'Yes'
    assert module_0.match_parens(['(()', ')']) == 'Yes'
    assert module_0.match_parens(['())', '((']) == 'Yes'      # '((' + '())' = '(())'
    assert module_0.match_parens([')', '(']) == 'Yes'         # '(' + ')' = '()'
    assert module_0.match_parens(['', '()']) == 'Yes'

    # Neither order is balanced
    assert module_0.match_parens(['(', '(']) == 'No'
    assert module_0.match_parens(['()', ')']) == 'No'
    assert module_0.match_parens([')(', ')(']) == 'No'
    assert module_0.match_parens(['())', '())']) == 'No'
    assert module_0.match_parens(['', '(']) == 'No'
    assert module_0.match_parens(['', ')']) == 'No'
    assert module_0.match_parens([')(', '()']) == 'No'        # equal counts, but no order works

# Generated at 2026-11-01 20:53:14.910330
# Unit test for function match_parens
def test_match_parens():
    # Examples from docstring
    assert module_0.match_parens(['()(', ')']) == 'Yes'
    assert module_0.match_parens([')', ')']) == 'No'

    # Both strings already balanced, either order works
    assert module_0.match_parens(['()', '()']) == 'Yes'
    assert module_0.match_parens(['()', '(())']) == 'Yes'

    # Only one concatenation order is valid
    assert module_0.match_parens(['((', '))']) == 'Yes'
    assert module_0.match_parens(['))', '((']) == 'Yes'  # reversed order still valid
    assert module_0.match_parens([')(', '()']) == 'Yes'
    assert module_0.match_parens(['()', ')(']) == 'Yes'

    # Impossible cases
    assert module_0.match_parens(['(', ')']) == 'Yes'   # '(' + ')' is balanced
    assert module_0.match_parens([')', '(']) == 'Yes'   # ')' + '(' is not... but '(' + ')' is
    assert module_0.match_parens([')', '))']) == 'No'
    assert module_0.match_parens(['))(', '))']) == 'No'
    assert module_0.match_parens(['()(', '))']) == 'No'

    # Empty strings edge cases
    assert module_0.match_parens(['', '']) == 'Yes'     # empty string is balanced
    assert module_0.match_parens(['', '()']) == 'Yes'
    assert module_0.match_parens(['', '(']) == 'No'

    # Longer strings
    assert module_0.match_parens(['((()))', '()']) == 'Yes'
    assert module_0.match_parens(['()()()', '']) == 'Yes'
    assert module_0.match_parens(['(()', '())']) == 'Yes'

# Generated at 2026-11-01 20:54:01.139755
# Unit test for function match_parens
def test_match_parens():
    # Provided examples
    assert module_0.match_parens(['()(', ')']) == 'Yes'
    assert module_0.match_parens([')', ')']) == 'No'

    # Simple balanced combinations
    assert module_0.match_parens(['(', ')']) == 'Yes'
    assert module_0.match_parens(['()', '()']) == 'Yes'
    assert module_0.match_parens(['((', '))']) == 'Yes'
    assert module_0.match_parens(['(((', ')))']) == 'Yes'
    assert module_0.match_parens(['(())', '()']) == 'Yes'

    # Order matters: only one concatenation direction produces a good string
    assert module_0.match_parens([')', '(']) == 'Yes'      # only lst[1]+lst[0] = '()' is good
    assert module_0.match_parens(['())', '(()']) == 'Yes'  # only '(()' + '())' = '(()())' is good

    # No ordering yields a balanced string
    assert module_0.match_parens([')(', ')(']) == 'No'
    assert module_0.match_parens(['(()', '))']) == 'No'    # equal counts but neither order works
    assert module_0.match_parens(['()', ')']) == 'No'
    assert module_0.match_parens([')(', '(']) == 'No'

# Generated at 2026-11-01 20:54:31.706174
# Unit test for function match_parens
def test_match_parens():
    # Examples from the docstring
    assert module_0.match_parens(['()(', ')']) == 'Yes'
    assert module_0.match_parens([')', ')']) == 'No'

    # Simple balanced pairs
    assert module_0.match_parens(['()', '()']) == 'Yes'
    assert module_0.match_parens(['(', ')']) == 'Yes'
    assert module_0.match_parens(['(()', ')']) == 'Yes'

    # Order swapping makes it work
    assert module_0.match_parens([')', '(']) == 'Yes'      # '()' via second ordering
    assert module_0.match_parens(['((', '))']) == 'Yes'    # '(())' via first ordering
    assert module_0.match_parens(['))', '((']) == 'Yes'    # '(())' via second ordering

    # Impossible cases
    assert module_0.match_parens(['(', '(']) == 'No'       # too many opens overall
    assert module_0.match_parens([')(', ')(']) == 'No'     # balanced counts but no valid order
    assert module_0.match_parens([')(', '()']) == 'No'
    assert module_0.match_parens(['())(', '(()']) == 'No'  # unbalanced total counts

    # Empty-string edge cases
    assert module_0.match_parens(['', '']) == 'Yes'
    assert module_0.match_parens(['', '()']) == 'Yes'
    assert module_0.match_parens(['', '(']) == 'No'
    assert module_0.match_parens(['', ')']) == 'No'

    # Longer nested strings
    assert module_0.match_parens(['((()))', '()']) == 'Yes'
    assert module_0.match_parens(['(()())', '']) == 'Yes'
    assert module_0.match_parens(['((()', ')))']) == 'Yes'  # '((())))' -> '((( )))' balanced


test_match_parens()
print("All tests passed!")

# Generated at 2026-11-01 20:55:10.630570
# Unit test for function match_parens
def test_match_parens():
# nonce:dd178e9a
    # Examples from docstring
    assert module_0.match_parens(['()(', ')']) == 'Yes'
    assert module_0.match_parens([')', ')']) == 'No'

    # Simple balanced pairs
    assert module_0.match_parens(['(', ')']) == 'Yes'
    assert module_0.match_parens([')', '(']) == 'Yes'
    assert module_0.match_parens(['()', '()']) == 'Yes'
    assert module_0.match_parens(['((', '))']) == 'Yes'
    assert module_0.match_parens(['(((', ')))']) == 'Yes'

    # Impossible cases
    assert module_0.match_parens(['(', '(']) == 'No'
    assert module_0.match_parens([')(', '(']) == 'No'
    assert module_0.match_parens([')(', ')(']) == 'No'
    assert module_0.match_parens(['(()', '))']) == 'No'
    assert module_0.match_parens(['))((', '))((']) == 'No'

    # Empty strings (empty result is balanced)
    assert module_0.match_parens(['', '']) == 'Yes'
    assert module_0.match_parens(['', '(']) == 'No'
    assert module_0.match_parens(['', ')']) == 'No'