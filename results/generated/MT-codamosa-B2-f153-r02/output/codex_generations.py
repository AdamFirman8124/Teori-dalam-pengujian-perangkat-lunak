

# Generated at 2026-11-02 07:47:20.866187
# Unit test for function Strongest_Extension
def test_Strongest_Extension():
# nonce:e1b0c8a3
    # Basic cases from the specification
    assert module_0.Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'
    assert module_0.Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'
    assert module_0.Strongest_Extension('fonny', ['ShortEND', 'bArthur']) == 'fonny.ShortEND'
    assert module_0.Strongest_Extension('Watashi', ['tEN', 'niNE', 'eIGHt8OKe']) == 'Watashi.eIGHt8OKe'

    # Single extension list
    assert module_0.Strongest_Extension('Solo', ['one']) == 'Solo.one'
    assert module_0.Strongest_Extension('X', ['abc']) == 'X.abc'

    # Tie between extensions: first one with max strength wins
    assert module_0.Strongest_Extension('Tie', ['AB', 'CD']) == 'Tie.AB'
    assert module_0.Strongest_Extension('Tie2', ['aB', 'Cd', 'EF']) == 'Tie2.EF'

    # All extensions have negative strength; least negative wins
    assert module_0.Strongest_Extension('Neg', ['abcdef', 'de']) == 'Neg.de'
    assert module_0.Strongest_Extension('Neg2', ['abc', 'abcd']) == 'Neg2.abc'

    # Non-alphabetic characters are ignored in strength computation
    assert module_0.Strongest_Extension('Num', ['a1B2', 'C']) == 'Num.C'
    assert module_0.Strongest_Extension('Sym', ['A!b?', 'c#']) == 'Sym.A!b?'

    # A later extension strictly exceeding earlier strength replaces it
    assert module_0.Strongest_Extension('Later', ['abc', 'ABC']) == 'Later.ABC'
    assert module_0.Strongest_Extension('Later2', ['aB', 'ABcD']) == 'Later2.ABcD'

    # Empty-string extension has strength 0
    assert module_0.Strongest_Extension('Empty', ['']) == 'Empty.'

    # Class name with special characters is passed through unchanged
    assert module_0.Strongest_Extension('My-Class_1', ['AB']) == 'My-Class_1.AB'

# Generated at 2026-11-02 07:48:02.952967
# Unit test for function Strongest_Extension
def test_Strongest_Extension():
    # Basic example: 'AA' has strength 2, 'Be' has 0, 'CC' has 2; first max wins ties
    assert module_0.Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'

    # 'SErviNGSliCes' has strength 3, 'Cheese' has 2, 'StuFfed' has 2
    assert module_0.Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'

    # Later extension with strictly greater strength wins
    assert module_0.Strongest_Extension('X', ['a', 'B']) == 'X.B'
    assert module_0.Strongest_Extension('X', ['bA', 'AA']) == 'X.AA'

    # Single extension
    assert module_0.Strongest_Extension('Solo', ['OnE']) == 'Solo.OnE'

    # Ties keep the first extension
    assert module_0.Strongest_Extension('Tie', ['AB', 'CD']) == 'Tie.AB'

    # Non-alpha characters don't count; '123' (0) beats 'abc' (-3)
    assert module_0.Strongest_Extension('Neg', ['123', 'abc']) == 'Neg.123'

    # Empty extensions list should raise IndexError
    try:
        module_0.Strongest_Extension('Empty', [])
        assert False, "Expected IndexError for empty extensions list"
    except IndexError:
        pass

    print("All tests passed!")


if __name__ == "__main__":
    test_Strongest_Extension()

# Generated at 2026-11-02 07:48:39.835868
# Unit test for function Strongest_Extension
def test_Strongest_Extension():
    # Basic example: tie between 'AA' and 'CC', first one wins
    assert module_0.Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'

    # Classic example
    assert module_0.Strongest_Extension('Slices', ['SErviCSsITics', 'Yeeaw', 'Slices']) == 'Slices.SErviCSsITics'

    # Single extension
    assert module_0.Strongest_Extension('Solo', ['abc']) == 'Solo.abc'

    # Ties: strictly-greater comparison keeps the earliest max
    assert module_0.Strongest_Extension('Tie', ['AB', 'CD', 'EF']) == 'Tie.AB'
    assert module_0.Strongest_Extension('Tie', ['aB', 'Cd', 'EF']) == 'Tie.EF'

    # All negative strengths -> strongest is the least negative
    assert module_0.Strongest_Extension('Neg', ['abcd', 'abc']) == 'Neg.abc'

    # Non-alphabetic characters are ignored in strength calculation
    assert module_0.Strongest_Extension('Num', ['A1b2', 'ab']) == 'Num.A1b2'

    # Empty extension has strength 0 and beats negative strengths
    assert module_0.Strongest_Extension('Empty', ['xyz', '']) == 'Empty.'

    # Later extension with strictly higher strength replaces the current one
    assert module_0.Strongest_Extension('Mix', ['aBcDeF', 'XYZ']) == 'Mix.XYZ'

    # Class name with special characters is preserved as-is
    assert module_0.Strongest_Extension('my_class.1', ['A']) == 'my_class.1.A'

    print("All tests passed!")


test_Strongest_Extension()

# Generated at 2026-11-02 07:49:01.322243
# Unit test for function Strongest_Extension
def test_Strongest_Extension():
    # Basic case: extension with more uppercase letters wins
    assert module_0.Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'

    # Tie in strength: first extension in the list wins
    assert module_0.Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'

    # Single extension
    assert module_0.Strongest_Extension('Person', ['Ewf']) == 'Person.Ewf'

    # Extensions with same counts of upper/lower: first one is kept
    assert module_0.Strongest_Extension('abc', ['aB', 'Ba', 'cD']) == 'abc.aB'

    # All lowercase extensions (all tied at negative strength)
    assert module_0.Strongest_Extension('Klass', ['abc', 'def']) == 'Klass.abc'

    # Extension with non-alpha characters ignored in strength calc
    assert module_0.Strongest_Extension('Test', ['a1B!', 'zz']) == 'Test.a1B!'

    # Strength can be negative; strongest is the least negative
    assert module_0.Strongest_Extension('Neg', ['aBcDeF', 'abcdef']) == 'Neg.aBcDeF'

    # Class name with underscores/digits
    assert module_0.Strongest_Extension('my_class_2', ['QQ', 'bb']) == 'my_class_2.QQ'

    print("All tests passed!")


if __name__ == "__main__":
    test_Strongest_Extension()

# Generated at 2026-11-02 07:49:24.060185
# Unit test for function Strongest_Extension
def test_Strongest_Extension():
    # Basic example: first extension has the strongest value (least negative)
    assert module_0.Strongest_Extension('my_class', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'my_class.SErviNGSliCes'

    # Tie in strength: first one in the list wins (strict > comparison)
    assert module_0.Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'

    # Only one extension available
    assert module_0.Strongest_Extension('Slices', ['SErviNGSliCes']) == 'Slices.SErviNGSliCes'

    # Later extension strictly stronger than earlier ones
    assert module_0.Strongest_Extension('Xyz', ['abc', 'ABC', 'aBc']) == 'Xyz.ABC'

    # Non-alphabetic characters are ignored in strength computation
    assert module_0.Strongest_Extension('fin', ['a1b2C3', 'ZZzz']) == 'fin.ZZzz'

    # All-lowercase extensions: the one with fewest lowercase letters wins
    assert module_0.Strongest_Extension('pkg', ['aaaa', 'aa', 'aaa']) == 'pkg.aa'

    # Class name with underscore gets concatenated correctly
    assert module_0.Strongest_Extension('my_class_01', ['ext']) == 'my_class_01.ext'

    # Equal strength (both zero) keeps the first
    assert module_0.Strongest_Extension('mod', ['Aa', 'Bb']) == 'mod.Aa'

    print("All tests passed!")


test_Strongest_Extension()