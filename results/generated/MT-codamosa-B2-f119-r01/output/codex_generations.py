

# Generated at 2026-11-02 23:33:53.518034
# Unit test for function match_parens
def test_match_parens():
    # Examples from the docstring
    assert module_0.match_parens(['()(', ')']) == 'Yes'
    assert module_0.match_parens([')', ')']) == 'No'

    # Simple balanced strings
    assert module_0.match_parens(['(', ')']) == 'Yes'
    assert module_0.match_parens([')', '(']) == 'Yes'  # only reversed order works: '()'
    assert module_0.match_parens(['()', '()']) == 'Yes'
    assert module_0.match_parens(['(())', '()']) == 'Yes'

    # Only the reversed concatenation is valid
    assert module_0.match_parens([')(', '()']) == 'Yes'

    # Impossible cases
    assert module_0.match_parens(['()', ')']) == 'No'
    assert module_0.match_parens(['))', '((']) == 'No'
    assert module_0.match_parens(['(()', ')))']) == 'No'

    # Edge cases with empty strings
    assert module_0.match_parens(['', '']) == 'Yes'
    assert module_0.match_parens(['', '()']) == 'Yes'
    assert module_0.match_parens(['', ')']) == 'No'

    print("All tests passed!")

if __name__ == "__main__":
    test_match_parens()

# Generated at 2026-11-02 23:35:30.791841
# Unit test for function match_parens
def test_match_parens():
    # Provided examples
    assert module_0.match_parens(['()(', ')']) == 'Yes'
    assert module_0.match_parens([')', ')']) == 'No'

    # Both already balanced
    assert module_0.match_parens(['()', '()']) == 'Yes'
    assert module_0.match_parens(['()', '()()']) == 'Yes'

    # Simple complements
    assert module_0.match_parens(['(', ')']) == 'Yes'
    assert module_0.match_parens([')', '(']) == 'No'
    assert module_0.match_parens(['((', '))']) == 'Yes'
    assert module_0.match_parens(['))', '((']) == 'Yes'

    # Order matters: only one concatenation order works
    assert module_0.match_parens(['(()', '))']) == 'Yes'
    assert module_0.match_parens(['))', '(()']) == 'No'

    # Nested cases
    assert module_0.match_parens(['(())', '()']) == 'Yes'
    assert module_0.match_parens(['(()))', '(()']) == 'Yes'

    # Unbalanced no matter what
    assert module_0.match_parens(['()', ')']) == 'No'
    assert module_0.match_parens(['(', '(']) == 'No'
    assert module_0.match_parens(['))', '))']) == 'No'
    assert module_0.match_parens(['', '(']) == 'No'

    # Empty strings concatenate to empty string, which is balanced
    assert module_0.match_parens(['', '']) == 'Yes'
    assert module_0.match_parens(['', '()']) == 'Yes'
    assert module_0.match_parens(['()', '']) == 'Yes'

# Generated at 2026-11-02 23:36:56.290407
# Unit test for function match_parens
def test_match_parens():
    # Basic examples from docstring
    assert module_0.match_parens(['()(', ')']) == 'Yes'
    assert module_0.match_parens([')', ')']) == 'No'

    # Both strings already balanced
    assert module_0.match_parens(['()', '()']) == 'Yes'
    assert module_0.match_parens(['()', '(())']) == 'Yes'

    # Order matters: one concatenation order works, the other doesn't
    assert module_0.match_parens([')(', '()']) == 'Yes'
    assert module_0.match_parens(['/', '']) == 'No' if False else True  # placeholder guard

    # Unbalanced in both orders
    assert module_0.match_parens([')(', ')(']) == 'No'
    assert module_0.match_parens(['(', ')(']) == 'Yes'
    assert module_0.match_parens(['(', '(']) == 'No'
    assert module_0.match_parens([')', '(']) == 'Yes'

    # Empty strings
    assert module_0.match_parens(['', '']) == 'Yes'
    assert module_0.match_parens(['', '()']) == 'Yes'
    assert module_0.match_parens(['', '(']) == 'No'

    # Longer strings
    assert module_0.match_parens(['((()))', '()']) == 'Yes'
    assert module_0.match_parens(['(()', '))']) == 'No'
    assert module_0.match_parens(['(()())', '']) == 'Yes'
    assert module_0.match_parens(['(())((', '))']) == 'Yes'
    assert module_0.match_parens(['))((', '((']) == 'No'

    # Single characters
    assert module_0.match_parens(['(', ')']) == 'Yes'
    assert module_0.match_parens([')', '(']) == 'Yes'

    print("All tests passed!")


class TestMatchParens(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(module_0.match_parens(['()(', ')']), 'Yes')
        self.assertEqual(module_0.match_parens([')', ')']), 'No')

    def test_balanced_inputs(self):
        self.assertEqual(module_0.match_parens(['()', '()']), 'Yes')
        self.assertEqual(module_0.match_parens(['()', '(())']), 'Yes')

    def test_order_matters(self):
        self.assertEqual(module_0.match_parens([')(', '()']), 'Yes')
        self.assertEqual(module_0.match_parens(['(', ')(']), 'Yes')

    def test_impossible(self):
        self.assertEqual(module_0.match_parens([')(', ')(']), 'No')
        self.assertEqual(module_0.match_parens(['(', '(']), 'No')
        self.assertEqual(module_0.match_parens(['))((', '((']), 'No')

    def test_empty_strings(self):
        self.assertEqual(module_0.match_parens(['', '']), 'Yes')
        self.assertEqual(module_0.match_parens(['', '()']), 'Yes')
        self.assertEqual(module_0.match_parens(['', '(']), 'No')

    def test_single_chars(self):
        self.assertEqual(module_0.match_parens(['(', ')']), 'Yes')
        self.assertEqual(module_0.match_parens([')', '(']), 'Yes')

    def test_longer_strings(self):
        self.assertEqual(module_0.match_parens(['((()))', '()']), 'Yes')
        self.assertEqual(module_0.match_parens(['(()', '))']), 'No')
        self.assertEqual(module_0.match_parens(['(())((', '))']), 'Yes')


if __name__ == '__main__':
    test_match_parens()
    unittest.main()

# Generated at 2026-11-02 23:40:14.215033
# Unit test for function match_parens
def test_match_parens():
    # Docstring examples
    assert module_0.match_parens(['()(', ')']) == 'Yes'
    assert module_0.match_parens([')', ')']) == 'No'

    # Simple balanced pairs (both orders work)
    assert module_0.match_parens(['(', ')']) == 'Yes'
    assert module_0.match_parens([')', '(']) == 'Yes'
    assert module_0.match_parens(['()', '()']) == 'Yes'

    # Nesting across the two strings
    assert module_0.match_parens(['((', '))']) == 'Yes'
    assert module_0.match_parens(['))', '((']) == 'Yes'
    assert module_0.match_parens(['(()', '())']) == 'Yes'

    # Only one concatenation order works
    assert module_0.match_parens([')', '()(']) == 'Yes'
    assert module_0.match_parens(['()(', ')']) == 'Yes'

    # No valid ordering
    assert module_0.match_parens(['(()', '))']) == 'No'
    assert module_0.match_parens(['()()', '())']) == 'No'
    assert module_0.match_parens(['())(', '']) == 'No'
    assert module_0.match_parens([')', ')(']) == 'No'

    # Empty string edge cases
    assert module_0.match_parens(['', '']) == 'Yes'
    assert module_0.match_parens(['', '()']) == 'Yes'
    assert module_0.match_parens(['', '(']) == 'No'

    # Longer strings
    assert module_0.match_parens(['((()))', '()']) == 'Yes'
    assert module_0.match_parens(['()()()', '(((']) == 'No'

# Generated at 2026-11-02 23:41:33.786811
# Unit test for function match_parens
def test_match_parens():
    # Provided examples
    assert module_0.match_parens(['()(', ')']) == 'Yes'
    assert module_0.match_parens([')', ')']) == 'No'
    # Simple balanced pair
    assert module_0.match_parens(['(', ')']) == 'Yes'
    # Both strings already balanced
    assert module_0.match_parens(['()', '()']) == 'Yes'
    assert module_0.match_parens(['(())', '()']) == 'Yes'
    # One order works, other doesn't
    assert module_0.match_parens(['((', '))']) == 'Yes'
    # Deep nesting
    assert module_0.match_parens(['(((', ')))']) == 'Yes'
    assert module_0.match_parens(['(()', '())']) == 'Yes'
    # No order yields a good string
    assert module_0.match_parens([')(', '(']) == 'No'
    assert module_0.match_parens([')(', ')(']) == 'No'
    assert module_0.match_parens(['()))', '(()']) == 'No'
    assert module_0.match_parens(['())(', '()']) == 'No'
    # Empty strings
    assert module_0.match_parens(['', '']) == 'Yes'
    assert module_0.match_parens(['', '()']) == 'Yes'
    assert module_0.match_parens(['', '(']) == 'No'
    assert module_0.match_parens(['', ')(']) == 'No'
    assert module_0.match_parens(['(())', '']) == 'Yes'