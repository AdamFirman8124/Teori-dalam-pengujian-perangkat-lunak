

# Generated at 2026-11-01 21:23:56.660813
# Unit test for function Strongest_Extension
def test_Strongest_Extension():
    # Basic case: first extension is strongest
    assert module_0.Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'
    # Tie case: first of equal-strength extensions wins
    assert module_0.Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'
    # All strengths negative, pick least negative
    assert module_0.Strongest_Extension('Slices', ['cheese', 'Stuff']) == 'Slices.Stuff'
    # Single extension
    assert module_0.Strongest_Extension('X', ['abc']) == 'X.abc'
    # Single uppercase letter beats lowercase
    assert module_0.Strongest_Extension('C', ['a', 'A']) == 'C.A'
    # Later extension stronger than first
    assert module_0.Strongest_Extension('Cls', ['weak', 'STRONG']) == 'Cls.STRONG'
    # Digits/symbols are ignored in strength calculation
    assert module_0.Strongest_Extension('Cls', ['a1B', 'aB']) == 'Cls.aB'
    # Empty class name still concatenates
    assert module_0.Strongest_Extension('', ['ext']) == '.ext'
    print("All tests passed!")

test_Strongest_Extension()

# Generated at 2026-11-01 21:24:13.652565
# Unit test for function Strongest_Extension
def test_Strongest_Extension():
    # Classic example: picks extension with max (uppercase - lowercase) count
    assert module_0.Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'

    # Tie between 'AA' and 'CC' (both strength 2) -> first occurrence wins
    assert module_0.Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'

    # Single extension
    assert module_0.Strongest_Extension('Foo', ['bar']) == 'Foo.bar'

    # All strengths negative: picks the least negative
    assert module_0.Strongest_Extension('Klass', ['aBc', 'abc', 'abcd']) == 'Klass.aBc'

    # Non-alphabetic characters are ignored in strength calculation
    assert module_0.Strongest_Extension('Num', ['!1a2B', 'zz']) == 'Num.!1a2B'

    # A later, strictly stronger extension replaces the current best
    assert module_0.Strongest_Extension('Mod', ['xY', 'XY', 'z']) == 'Mod.XY'

    # Empty extension string has strength 0, beats a negative one
    assert module_0.Strongest_Extension('T', ['', 'a']) == 'T.'

    # Identical extensions: first one is kept
    assert module_0.Strongest_Extension('Dup', ['AB', 'AB']) == 'Dup.AB'

    # Class name passes through unchanged
    assert module_0.Strongest_Extension('My_Lib-1', ['xyz']) == 'My_Lib-1.xyz'

# Generated at 2026-11-01 21:24:35.154707
# Unit test for function Strongest_Extension
def test_Strongest_Extension():
    # Basic case: 'AA' has strength 2 (2 upper - 0 lower), the highest
    assert module_0.Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'

    # Tie between 'AA' and 'CC' (both strength 2): first occurrence wins
    assert module_0.Strongest_Extension('my_class', ['Be', 'AA', 'CC']) == 'my_class.AA'

    # Mixed-case example: 'SErviCSsitiCS' has strength -1, tied with others, first wins
    assert module_0.Strongest_Extension('Slices', ['SErviCSsitiCS', 'Chip', 'StAte', 'pPpPpPp']) == 'Slices.SErviCSsitiCS'

    # Digits and non-alpha characters are ignored in strength calculation
    assert module_0.Strongest_Extension('Num', ['a1B2', 'c3D4']) == 'Num.a1B2'

    # Later extension with higher strength replaces the initial one
    assert module_0.Strongest_Extension('Neg', ['abc', 'Ab']) == 'Neg.Ab'

    # Single extension in list
    assert module_0.Strongest_Extension('Solo', ['x']) == 'Solo.x'

    # All-lowercase extensions: all strength -3, first wins
    assert module_0.Strongest_Extension('Low', ['abc', 'def']) == 'Low.abc'

    # Special characters ignored: 'XY' (strength 2) beats 'A!b@c#' (strength 0)
    assert module_0.Strongest_Extension('Mix', ['A!b@c#', 'XY']) == 'Mix.XY'

    # All-uppercase extensions: all strength equal, first wins
    assert module_0.Strongest_Extension('Upper', ['ABC', 'DEF']) == 'Upper.ABC'

    # Empty class name still concatenates correctly
    assert module_0.Strongest_Extension('', ['AB']) == '.AB'

    print("All tests passed!")

# Generated at 2026-11-01 21:25:04.837066
# Unit test for function Strongest_Extension
def test_Strongest_Extension():assert module_0.Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'

# Generated at 2026-11-01 21:25:23.904095
# Unit test for function Strongest_Extension
def test_Strongest_Extension():# nonce:aad042f4
    # Basic case: extension with highest (uppercase - lowercase) count wins
    assert module_0.Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'
    # Ties resolved by first occurrence (strictly greater comparison)
    assert module_0.Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'
    # Equal strength keeps the first extension
    assert module_0.Strongest_Extension('X', ['ab', 'cd']) == 'X.ab'
    # Single extension list
    assert module_0.Strongest_Extension('Test', ['only']) == 'Test.only'
    # All lowercase: fewer lowercase letters is stronger
    assert module_0.Strongest_Extension('A', ['abc', 'abcd']) == 'A.abc'
    # Non-alphabetic characters are ignored
    assert module_0.Strongest_Extension('N', ['1a2B', 'BB']) == 'N.BB'
    # Empty extension string
    assert module_0.Strongest_Extension('C', ['']) == 'C.'
    # Later extension strictly stronger replaces earlier one
    assert module_0.Strongest_Extension('Z', ['aa', 'BB', 'cc']) == 'Z.BB'
    # Class name with dots/underscores is preserved as-is
    assert module_0.Strongest_Extension('my.Class_1', ['x']) == 'my.Class_1.x'