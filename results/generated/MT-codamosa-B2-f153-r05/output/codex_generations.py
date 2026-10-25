

# Generated at 2026-10-25 03:45:29.371530
# Unit test for function Strongest_Extension
def test_Strongest_Extension():
    # Highest strength wins
    assert module_0.Strongest_Extension(
        "MyClass", ["weak", "STRONG", "Medium"]
    ) == "MyClass.STRONG"

    # Strength = uppercase count - lowercase count
    assert module_0.Strongest_Extension(
        "Class", ["AbC", "ABCd", "abc"]
    ) == "Class.ABCd"

    # In a tie, the first extension is selected
    assert module_0.Strongest_Extension(
        "Test", ["AA", "BB", "CC"]
    ) == "Test.AA"

    # Non-alphabetic characters do not affect strength
    assert module_0.Strongest_Extension(
        "File", ["A1!", "AB12", "abc"]
    ) == "File.AB12"

    # An empty extension is supported when the list is non-empty
    assert module_0.Strongest_Extension(
        "Base", ["", "a"]
    ) == "Base."

# Generated at 2026-10-25 03:45:39.199500
# Unit test for function Strongest_Extension
def test_Strongest_Extension():
    # Extension with the highest strength is selected
    assert module_0.Strongest_Extension("Class", ["abc", "ABc", "ABC"]) == "Class.ABC"

    # Ties are resolved by selecting the first extension
    assert module_0.Strongest_Extension("Class", ["AA", "Bb", "CC"]) == "Class.AA"

    # Strength can be negative
    assert module_0.Strongest_Extension("Class", ["abc", "de", "fghi"]) == "Class.de"

    # Non-alphabetic characters do not affect strength
    assert module_0.Strongest_Extension("Class", ["A1_b", "AB-1"]) == "Class.AB-1"

    # A single extension is returned
    assert module_0.Strongest_Extension("Class", ["Ext"]) == "Class.Ext"

# Generated at 2026-10-25 03:45:41.741896
# Unit test for function Strongest_Extension

# Generated at 2026-10-25 03:45:44.266740
# Unit test for function Strongest_Extension

# Generated at 2026-10-25 03:45:48.824713
# Unit test for function Strongest_Extension
def test_Strongest_Extension():assert module_0.Strongest_Extension("Class", ["AAaa", "Bcd", "XYZ"]) == "Class.XYZ"

# Generated at 2026-10-25 03:45:56.791829
# Unit test for function Strongest_Extension
def test_Strongest_Extension():
    # Highest strength: AA (+2)
    assert module_0.Strongest_Extension("Slices", ["SErviCe", "COFFEE", "AA"]) == "Slices.AA"

    # Negative strengths are compared correctly
    assert module_0.Strongest_Extension("Class", ["abc", "aBc", "ABC"]) == "Class.ABC"

    # The first extension wins when strengths are tied
    assert module_0.Strongest_Extension("Class", ["ABcd", "XYzz", "ABCd"]) == "Class.ABCd"

    # Non-alphabetic characters do not affect strength
    assert module_0.Strongest_Extension("File", ["A1!", "BB22", "C_d"]) == "File.BB22"

    # A single extension
    assert module_0.Strongest_Extension("Only", ["TeST"]) == "Only.TeST"

# Generated at 2026-10-25 03:46:03.356189
# Unit test for function Strongest_Extension
def test_Strongest_Extension():
    # Highest uppercase-minus-lowercase score
    assert module_0.Strongest_Extension("MyClass", ["abc", "aBC", "XYZ"]) == "MyClass.XYZ"

    # Ties select the first extension
    assert module_0.Strongest_Extension("MyClass", ["ABC", "XYZ"]) == "MyClass.ABC"

    # Non-alphabetic characters do not affect the score
    assert module_0.Strongest_Extension("File", ["A1!", "ab", "BC"]) == "File.BC"

    # Single extension
    assert module_0.Strongest_Extension("Test", ["Py"]) == "Test.Py"