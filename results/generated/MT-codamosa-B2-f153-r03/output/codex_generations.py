

# Generated at 2026-11-03 06:00:49.311269
# Unit test for function Strongest_Extension
def test_Strongest_Extension():
    # Basic case: extension with more uppercase letters relative to lowercase wins
    assert module_0.Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'

    # Tie case: first extension with the max strength wins
    assert module_0.Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'

    # Single extension
    assert module_0.Strongest_Extension('single', ['OnlyOne']) == 'single.OnlyOne'

    # Non-alphabetic characters should not affect strength
    assert module_0.Strongest_Extension('num', ['A1b2C3', 'xyz']) == 'num.A1b2C3'

    # All lowercase: less-negative (fewer lowercase) wins
    assert module_0.Strongest_Extension('lower', ['abc', 'ab']) == 'lower.ab'

    # Extension with no letters (strength 0) beats all-lowercase (negative strength)
    assert module_0.Strongest_Extension('zero', ['abc', '123', 'aB']) == 'zero.123'

    # Strongest appears later in the list
    assert module_0.Strongest_Extension('later', ['weak', 'weaker', 'STRONG']) == 'later.STRONG'

    # Empty-ish extension (empty string has strength 0)
    assert module_0.Strongest_Extension('empty', ['abc', '']) == 'empty.'

    # Class name with dots/underscores is used as-is
    assert module_0.Strongest_Extension('My_Class_1', ['A']) == 'My_Class_1.A'

    # Equal strength across all: first is returned
    assert module_0.Strongest_Extension('ties', ['XY', 'ZW', 'PQ']) == 'ties.XY'

    print("All tests passed!")


if __name__ == "__main__":
    test_Strongest_Extension()

# Generated at 2026-11-03 06:02:00.107639
# Unit test for function Strongest_Extension
def test_Strongest_Extension():
    # Basic case: extension with highest (upper - lower) count wins
    assert module_0.Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'

    # Tie case: first extension with the max value wins
    assert module_0.Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'

    # All extensions identical
    assert module_0.Strongest_Extension('fake_class_name', ['AA', 'AA', 'AA']) == 'fake_class_name.AA'

    # Single extension, negative strength still selected
    assert module_0.Strongest_Extension('X', ['abc']) == 'X.abc'

    # Later extension with strictly greater strength replaces earlier one
    assert module_0.Strongest_Extension('Cls', ['Ab', 'ABc', 'ABC']) == 'Cls.ABC'

    # Digits/special characters are ignored in counting
    assert module_0.Strongest_Extension('Cls', ['a1B2c', 'AB']) == 'Cls.AB'

    # All-lowercase extension only choice
    assert module_0.Strongest_Extension('Cls', ['xyz']) == 'Cls.xyz'

    # All-uppercase beats all-lowercase
    assert module_0.Strongest_Extension('Cls', ['abc', 'ABC']) == 'Cls.ABC'

    # Empty-ish strength: extension with no letters
    assert module_0.Strongest_Extension('Cls', ['123', 'aB']) == 'Cls.aB'

    print("All tests passed!")


if __name__ == "__main__":
    test_Strongest_Extension()

# Generated at 2026-11-03 06:03:07.076177
# Unit test for function Strongest_Extension
def test_Strongest_Extension():
    # Basic case: uppercase count minus lowercase count determines strength
    assert module_0.Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'

    # First extension wins on ties (strict > comparison keeps earlier one)
    assert module_0.Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'

    # Single extension
    assert module_0.Strongest_Extension('Class', ['onlyOne']) == 'Class.onlyOne'

    # All lowercase gives negative strength but is still chosen if only option
    assert module_0.Strongest_Extension('Klass', ['abc']) == 'Klass.abc'

    # Extension with no letters has strength 0, still selected among negatives
    assert module_0.Strongest_Extension('C', ['abc', '123', 'Ab']) == 'C.Ab'

    # Digits and symbols are ignored in strength calculation
    assert module_0.Strongest_Extension('X', ['a1!', 'B2?']) == 'X.B2?'

    # All uppercase beats mixed case
    assert module_0.Strongest_Extension('Prog', ['lower', 'UPPER', 'MiXeD']) == 'Prog.UPPER'

    # Equal strength: earlier extension preferred
    assert module_0.Strongest_Extension('Tie', ['Aa', 'aA', 'Bb']) == 'Tie.Aa'

    # Stronger extension appears later in the list
    assert module_0.Strongest_Extension('Late', ['weak', 'STRONG']) == 'Late.STRONG'

    # Empty-string extension has strength 0
    assert module_0.Strongest_Extension('E', ['abc', '']) == 'E.'

    print("All tests passed!")


if __name__ == "__main__":
    test_Strongest_Extension()

# Generated at 2026-11-03 06:04:31.351049
# Unit test for function Strongest_Extension
def test_Strongest_Extension():
    # Basic case: strongest extension by uppercase-lowercase difference
    assert module_0.Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'
    assert module_0.Strongest_Extension('my_class', ['Be', 'AA', 'CC']) == 'my_class.AA'

    # Mixed case example from problem statement
    assert module_0.Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'

    # Tie goes to the first occurrence (strictly greater comparison)
    assert module_0.Strongest_Extension('fin', ['AA', 'Ab']) == 'fin.AA'
    assert module_0.Strongest_Extension('fin', ['AA', 'Aa', 'AA']) == 'fin.AA'

    # Single extension
    assert module_0.Strongest_Extension('Spam', ['Aa']) == 'Spam.Aa'
    assert module_0.Strongest_Extension('Spam', ['eggs']) == 'Spam.eggs'

    # Extension with no alphabetic characters has strength 0
    assert module_0.Strongest_Extension('cls', ['123', 'A']) == 'cls.A'
    assert module_0.Strongest_Extension('cls', ['!@#', 'abc']) == 'cls.!@#'

    # Negative strength still selected if it's the only/first max
    assert module_0.Strongest_Extension('neg', ['aaa', 'b']) == 'neg.b'
    assert module_0.Strongest_Extension('neg', ['aaa']) == 'neg.aaa'

    # Digits and special characters are ignored in strength calculation
    assert module_0.Strongest_Extension('mix', ['A1b2C3', 'xY']) == 'mix.A1b2C3'

    # Class name concatenation with dot
    assert module_0.Strongest_Extension('MyClass', ['ext']) == 'MyClass.ext'

    print("All tests passed!")


test_Strongest_Extension()

# Generated at 2026-11-03 06:06:00.137813
# Unit test for function Strongest_Extension
def test_Strongest_Extension():
    # Basic case: strongest extension wins
    assert module_0.Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'
    # Tie broken by first occurrence in list
    assert module_0.Strongest_Extension('my_class', ['AA', 'bb', 'CC']) == 'my_class.AA'
    # All negative strengths, still picks the max
    assert module_0.Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'
    # All zero strength, first extension wins
    assert module_0.Strongest_Extension('my_class', ['bb', 'Aa', 'Cc']) == 'my_class.bb'
    # Single extension
    assert module_0.Strongest_Extension('X', ['aB']) == 'X.aB'
    # All uppercase beats mixed
    assert module_0.Strongest_Extension('cls', ['abc', 'ABC', 'aBc']) == 'cls.ABC'
    # Non-alphabetic characters ignored in strength calculation
    assert module_0.Strongest_Extension('cls', ['A1!', 'b2']) == 'cls.A1!'
    # Digits/symbols only extension has zero strength
    assert module_0.Strongest_Extension('mod', ['123', 'Ab']) == 'mod.Ab'
    # Class name with underscores/dots preserved in output
    assert module_0.Strongest_Extension('my_Class.v2', ['x']) == 'my_Class.v2.x'
    # Mixed case with more uppercase wins
    assert module_0.Strongest_Extension('pkg', ['aBcD', 'AbCd']) == 'pkg.aBcD'