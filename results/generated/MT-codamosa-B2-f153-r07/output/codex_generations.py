

# Generated at 2026-11-02 12:22:13.903704
# Unit test for function Strongest_Extension
def test_Strongest_Extension():
    # Basic case: extension with highest (uppercase - lowercase) count wins
    assert module_0.Strongest_Extension('Slices', ['SErviCSAPY', 'Chin', 'STOP']) == 'Slices.SErviCSAPY'

    # Ties are broken by the first occurrence in the list
    assert module_0.Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'
    assert module_0.Strongest_Extension('my_class', ['BB', 'AA', 'CC']) == 'my_class.BB'

    # Single extension in list
    assert module_0.Strongest_Extension('X', ['abc']) == 'X.abc'

    # Non-alphabetic characters are ignored in counting
    assert module_0.Strongest_Extension('A', ['1a2B3c', 'Xy']) == 'A.Xy'

    # All values negative: the least negative wins
    assert module_0.Strongest_Extension('C', ['abcdef', 'ab']) == 'C.ab'

    # Extension with no letters has value 0 and beats negative values
    assert module_0.Strongest_Extension('D', ['123', 'a']) == 'D.123'

    # Empty class name still joins with a dot
    assert module_0.Strongest_Extension('', ['A']) == '.A'

    # A later, strictly stronger extension replaces the earlier one
    assert module_0.Strongest_Extension('Test', ['aa', 'BB', 'cc']) == 'Test.BB'

    # Mixed case with underscores/digits
    assert module_0.Strongest_Extension('MyApp', ['uSer_1', 'ADMIN_x', 'zz']) == 'MyApp.ADMIN_x'

    # Class name with dots/numbers passes through unchanged
    assert module_0.Strongest_Extension('v1.2_Class', ['Ab', 'Cd']) == 'v1.2_Class.Ab'

    print("All tests passed!")


test_Strongest_Extension()

# Generated at 2026-11-02 12:23:13.078763
# Unit test for function Strongest_Extension
def test_Strongest_Extension():
# nonce:41cffc5a
    # Strongest extension wins even if all strengths are negative
    assert module_0.Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'
    # Tie between 'AA' and 'CC' (both strength 2): first occurrence wins
    assert module_0.Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'
    # Strongest extension in the middle of the list
    assert module_0.Strongest_Extension('Foo', ['bar', 'BAZ', 'qux']) == 'Foo.BAZ'
    # Single extension in the list
    assert module_0.Strongest_Extension('Test', ['only']) == 'Test.only'
    # Equal strengths ('aA' and 'Aa' both 0): first one is returned
    assert module_0.Strongest_Extension('C', ['aA', 'Aa']) == 'C.aA'
    # Non-alphabetic characters (digits) are ignored in strength calculation
    assert module_0.Strongest_Extension('Num', ['a1B2', 'cd']) == 'Num.a1B2'
    # All lowercase: least negative strength wins
    assert module_0.Strongest_Extension('Low', ['abc', 'a']) == 'Low.a'
    # Later extension strictly stronger replaces the current best
    assert module_0.Strongest_Extension('X', ['aBc', 'BcD']) == 'X.BcD'
    # Class name with underscores and dots preserved in result
    assert module_0.Strongest_Extension('my_class.v2', ['Ab', 'AB']) == 'my_class.v2.AB'
    # Extension with no letters at all has strength 0
    assert module_0.Strongest_Extension('Blank', ['123', 'ab']) == 'Blank.123'

# Generated at 2026-11-02 12:24:03.564744
# Unit test for function Strongest_Extension
def test_Strongest_Extension():
    # Basic case: 'AA' has strength 2, highest among the options
    assert module_0.Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'

    # Tie between 'SErviCSsHmi' (strength 1) and 'SOUrCE' (strength 1);
    # first in list wins, but 'SOUrCE' has strength 2-1... let's verify:
    # 'SErviCSsHmi': upper S,C,S,S,H = 5, lower e,r,v,i,i,m,i = 7 -> -2
    # 'SOUrCE': upper S,O,U,C,E = 5, lower r = 1 -> 4
    assert module_0.Strongest_Extension('Slices', ['SErviCSsHmi', 'SOUrCE', 'TablE', 'lasT', 'Get']) == 'Slices.SOUrCE'

    # Single extension
    assert module_0.Strongest_Extension('class1', ['abc']) == 'class1.abc'

    # Tie broken by first occurrence: 'AB' and 'CD' both have strength 2
    assert module_0.Strongest_Extension('Tie', ['AB', 'CD']) == 'Tie.AB'

    # Extension with non-alpha characters ignored in strength calculation
    assert module_0.Strongest_Extension('Num', ['A1b!', 'AB']) == 'Num.AB'

    # All lowercase extensions: first one (strength 0 vs -1) wins
    assert module_0.Strongest_Extension('Low', ['ab', 'abc']) == 'Low.ab'

    # Class name with special characters is preserved
    assert module_0.Strongest_Extension('My_Class-2', ['X']) == 'My_Class-2.X'

    # Negative strengths: least negative wins
    # 'aBc' -> 1-2 = -1, 'abCd' -> 1-3 = -2
    assert module_0.Strongest_Extension('Neg', ['abCd', 'aBc']) == 'Neg.aBc'

# Generated at 2026-11-02 12:25:27.669854
# Unit test for function Strongest_Extension
def test_Strongest_Extension():
    # Basic case: extension with more uppercase letters wins
    assert module_0.Strongest_Extension("Slices", ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'

    # Tie in strength: first extension in the list wins
    assert module_0.Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'

    # Uppercase-heavy extension beats lowercase-heavy ones
    assert module_0.Strongest_Extension('my_class', ['aa', 'Be', 'CC']) == 'my_class.CC'

    # Single extension in list
    assert module_0.Strongest_Extension('X', ['abc']) == 'X.abc'

    # All uppercase extension
    assert module_0.Strongest_Extension('X', ['ABC']) == 'X.ABC'

    # Special characters are ignored in strength calculation
    assert module_0.Strongest_Extension('X', ['A!b', 'cD']) == 'X.A!b'

    # Digits are ignored in strength calculation
    assert module_0.Strongest_Extension('X', ['A1', 'b2C']) == 'X.A1'

    # All negative strengths: least negative wins
    assert module_0.Strongest_Extension('X', ['abc', 'ab']) == 'X.ab'

    # Empty string has strength 0 and can win over negative strengths
    assert module_0.Strongest_Extension('X', ['a', '']) == 'X.'

    # Empty string first with strength 0 beats negative-strength extensions
    assert module_0.Strongest_Extension('X', ['', 'ab']) == 'X.'

    # Class name with special characters is preserved in output
    assert module_0.Strongest_Extension('My_Class-1', ['UP']) == 'My_Class-1.UP'

    print("All tests passed!")


test_Strongest_Extension()

# Generated at 2026-11-02 12:26:51.398315
# Unit test for function Strongest_Extension
def test_Strongest_Extension():import unittest


class TestStrongestExtension(unittest.TestCase):

    def test_basic_case(self):
        self.assertEqual(
            module_0.Strongest_Extension("Slices", ['SErviNGSliCes', 'Cheese', 'StuFfed']),
            'Slices.SErviNGSliCes'
        )

    def test_tie_returns_first(self):
        # Extensions with equal strength: first one wins
        self.assertEqual(
            module_0.Strongest_Extension("my_class", ['AA', 'bb', 'CC']),
            'my_class.AA'
        )

    def test_later_extension_stronger(self):
        self.assertEqual(
            module_0.Strongest_Extension("my_class", ['aa', 'BB', 'cc']),
            'my_class.BB'
        )

    def test_single_extension(self):
        self.assertEqual(
            module_0.Strongest_Extension("single", ['OnlyOne']),
            'single.OnlyOne'
        )

    def test_extension_with_digits_and_special_chars(self):
        # Non-alpha characters should not count toward strength
        self.assertEqual(
            module_0.Strongest_Extension("cls", ['a1!B', 'ABc']),
            'cls.a1!B'  # both have strength 0, first wins
        )

    def test_all_lowercase(self):
        self.assertEqual(
            module_0.Strongest_Extension("cls", ['abc', 'def', 'xyz']),
            'cls.abc'
        )

    def test_all_uppercase(self):
        self.assertEqual(
            module_0.Strongest_Extension("cls", ['ABC', 'DEF', 'XYZ']),
            'cls.ABC'
        )

    def test_negative_strength(self):
        # Extension with more lowercase than uppercase has negative strength
        self.assertEqual(
            module_0.Strongest_Extension("cls", ['aaaa', 'b']),
            'cls.b'  # strength -1 beats strength -4
        )

    def test_class_name_with_underscores(self):
        self.assertEqual(
            module_0.Strongest_Extension("My_Class_Name", ['ext']),
            'My_Class_Name.ext'
        )

    def test_empty_string_extension(self):
        self.assertEqual(
            module_0.Strongest_Extension("cls", ['', 'A']),
            'cls.A'  # strength 0 vs 1
        )

    def test_empty_string_wins_if_first_ties(self):
        self.assertEqual(
            module_0.Strongest_Extension("cls", ['', 'b']),
            'cls.'  # strength 0 vs -1, empty string wins
        )

    def test_strictly_greater_required(self):
        # Equal strength should NOT replace the current strongest
        self.assertEqual(
            module_0.Strongest_Extension("cls", ['Ab', 'CD', 'EF']),
            'cls.Ab'
        )


if __name__ == "__main__":
    unittest.main()