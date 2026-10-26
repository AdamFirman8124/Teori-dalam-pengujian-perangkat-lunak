

# Generated at 2026-10-25 08:33:28.434424
# Unit test for function Strongest_Extension
def test_Strongest_Extension():
    # Example from spec: strongest is 'SErviNGSliCes' with strength -1
    assert module_0.Strongest_Extension("Slices", ['SErviNGSliCes', 'Cheese', 'StuFfed']) == "Slices.SErviNGSliCes"

    # Tie -> first wins: 'AA'=2, 'Be'=0, 'CC'=2
    assert module_0.Strongest_Extension("my_class", ['AA', 'Be', 'CC']) == "my_class.AA"

    # Single extension
    assert module_0.Strongest_Extension("A", ["b"]) == "A.b"

    # All upper vs all lower
    assert module_0.Strongest_Extension("Test", ["abc", "DEF"]) == "Test.DEF"

    # Non-alpha chars ignored: 'A1B2c'=1, 'a-b_c'=-3
    assert module_0.Strongest_Extension("MyClass", ["A1B2c", "a-b_c"]) == "MyClass.A1B2c"

    # Strongest later in list
    assert module_0.Strongest_Extension("C", ["aa", "BB", "cC"]) == "C.BB"

# Generated at 2026-10-25 08:33:30.854561
# Unit test for function Strongest_Extension

# Generated at 2026-10-25 08:33:33.270474
# Unit test for function Strongest_Extension

# Generated at 2026-10-25 08:33:35.687392
# Unit test for function Strongest_Extension

# Generated at 2026-10-25 08:33:38.102786
# Unit test for function Strongest_Extension

# Generated at 2026-10-25 08:33:40.519153
# Unit test for function Strongest_Extension

# Generated at 2026-10-25 08:33:42.937551
# Unit test for function Strongest_Extension

# Generated at 2026-10-25 08:33:50.025013
# Unit test for function Strongest_Extension
def test_Strongest_Extension():
    # Typical case: 'S' has strength 0, 'SE' has strength 1 -> SE wins
    assert module_0.Strongest_Extension('S', ['SErviNgS', 'LiMe', 'FlaShYy', 'Apple']) == 'S.SErviNgS'
    assert module_0.Strongest_Extension('my_class', ['AA', 'Be', 'do']) == 'my_class.AA'
    assert module_0.Strongest_Extension('my_class', ['Be', 'AA']) == 'my_class.AA'

    # Ties: first extension in the list wins (strict > comparison)
    assert module_0.Strongest_Extension('C', ['AB', 'XY']) == 'C.AB'
    assert module_0.Strongest_Extension('C', ['AA', 'Aa', 'bb', 'Bb']) == 'C.AA'

    # Strength can be negative; the least negative wins
    assert module_0.Strongest_Extension('X', ['aabb', 'abc', 'Ab']) == 'X.Ab'
    assert module_0.Strongest_Extension('X', ['aaa', 'bbbb', 'Cc']) == 'X.Cc'

    # All-lowercase / all-uppercase / mixed with non-alpha characters
    assert module_0.Strongest_Extension('T', ['lower', 'UPPER']) == 'T.UPPER'
    assert module_0.Strongest_Extension('T', ['1a2B3c', 'DD!!']) == 'T.DD!!'
    assert module_0.Strongest_Extension('T', ['!@#$', 'a!B']) == 'T.a!B'

    # Single extension list
    assert module_0.Strongest_Extension('Solo', ['onlyOne']) == 'Solo.onlyOne'

    # Class name with dots/digits passes through unchanged
    assert module_0.Strongest_Extension('Cls_2.0', ['aB']) == 'Cls_2.0.aB'

    # Empty extension string: strength 0, beats negatives
    assert module_0.Strongest_Extension('E', ['', 'aa']) == 'E.'

    print("All tests passed!")


if __name__ == "__main__":
    test_Strongest_Extension()

# Generated at 2026-10-25 08:33:57.213624
# Unit test for function Strongest_Extension
def test_Strongest_Extension():
    # Basic case: CAPS count minus lower count decides the winner
    assert module_0.Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'

    # Ties go to the FIRST strongest extension (strict > comparison)
    assert module_0.Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'
    assert module_0.Strongest_Extension('my_class', ['Be', 'AA', 'CC']) == 'my_class.AA'

    # Single extension
    assert module_0.Strongest_Extension('X', ['AbC']) == 'X.AbC'

    # Digits and symbols are ignored (isalpha filter)
    assert module_0.Strongest_Extension('C', ['A1b!', 'aB2']) == 'C.A1b!'

    # Negative strength still works
    assert module_0.Strongest_Extension('N', ['aaaa', 'bb']) == 'N.bb'

    # All-lowercase class name / odd names pass through unchanged
    assert module_0.Strongest_Extension('lower', ['UP']) == 'lower.UP'

    print("All tests passed!")