

# Generated at 2026-10-24 19:36:53.804742
# Unit test for function Strongest_Extension

# Generated at 2026-10-24 19:36:56.318976
# Unit test for function Strongest_Extension

# Generated at 2026-10-24 19:36:58.734370
# Unit test for function Strongest_Extension

# Generated at 2026-10-24 19:37:01.260980
# Unit test for function Strongest_Extension

# Generated at 2026-10-24 19:37:03.677317
# Unit test for function Strongest_Extension

# Generated at 2026-10-24 19:37:10.210232
# Unit test for function Strongest_Extension
def test_Strongest_Extension():
    # Basic case: 'SE' has strength 1, 'Analyst' has 0, 'AA' has 2 -> 'AA' wins
    assert module_0.Strongest_Extension('Slices', ['SErviNGSliCes', 'Roller', 'Provi', 'der']) == 'Slices.Provi'
    assert module_0.Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'
    # Tie: first extension with max strength wins ('AA' and 'BB' both strength 2)
    assert module_0.Strongest_Extension('C', ['AA', 'BB']) == 'C.AA'
    # Strengths: 'S' = 1, 'ER' = 1, 'ing' = -3, 'R' = 1 -> 'S' first wins tie
    assert module_0.Strongest_Extension('typ', ['SER', 'ger']) == 'typ.SER'
    # Digits and non-letters don't count
    assert module_0.Strongest_Extension('X', ['a1B2', 'c']) == 'X.a1B2'
    # Single extension
    assert module_0.Strongest_Extension('Solo', ['OnlyOne']) == 'Solo.OnlyOne'
    # Negative strength still selected when it's the max
    assert module_0.Strongest_Extension('Neg', ['abc', 'ab']) == 'Neg.ab'

# Generated at 2026-10-24 19:37:11.569728
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

# Generated at 2026-10-24 19:37:12.943477
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

# Generated at 2026-10-24 19:37:14.441926
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