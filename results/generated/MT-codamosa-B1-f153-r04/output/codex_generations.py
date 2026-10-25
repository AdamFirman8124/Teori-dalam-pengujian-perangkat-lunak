

# Generated at 2026-10-24 19:58:25.961813
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

# Generated at 2026-10-24 19:58:27.323486
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

# Generated at 2026-10-24 19:58:28.730083
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

# Generated at 2026-10-24 19:58:30.090665
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

# Generated at 2026-10-24 19:58:31.477499
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