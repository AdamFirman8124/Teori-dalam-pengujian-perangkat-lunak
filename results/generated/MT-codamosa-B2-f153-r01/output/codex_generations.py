

# Generated at 2026-10-24 05:58:05.249897
# Unit test for function Strongest_Extension
def test_Strongest_Extension():
    # Extension with the highest strength wins
    assert module_0.Strongest_Extension("MyClass", ["AA", "Be", "CCc"]) == "MyClass.AA"

    # Strength = uppercase letters - lowercase letters
    assert module_0.Strongest_Extension("Sample", ["abc", "aBC", "XYZ"]) == "Sample.XYZ"

    # In a tie, the first extension is selected
    assert module_0.Strongest_Extension("Test", ["AB", "CD", "EF"]) == "Test.AB"

    # All extensions can have negative strength
    assert module_0.Strongest_Extension("Lower", ["abcd", "Abc", "ABc"]) == "Lower.ABc"

    # Non-alphabetic characters do not affect strength
    assert module_0.Strongest_Extension("File", ["A1!", "BB2", "C_"]) == "File.BB2"

    # A single extension
    assert module_0.Strongest_Extension("Only", ["Py"]) == "Only.Py"

# Generated at 2026-10-24 05:58:16.924125
# Unit test for function Strongest_Extension
def test_Strongest_Extension():
    # Extension with the greatest uppercase-minus-lowercase score
    assert module_0.Strongest_Extension(
        "Slices", ["SErvice", "SSE", "sse"]
    ) == "Slices.SSE"

    # A single uppercase letter is stronger than mixed-case extensions
    assert module_0.Strongest_Extension(
        "MyClass", ["Aa", "B", "Cc"]
    ) == "MyClass.B"

    # On a tie, the first strongest extension is selected
    assert module_0.Strongest_Extension(
        "Document", ["AA", "BB", "cc"]
    ) == "Document.AA"

    # Non-alphabetic characters do not affect strength
    assert module_0.Strongest_Extension(
        "File", ["A1!", "BB2", "ccc"]
    ) == "File.BB2"

    # Works with a single extension
    assert module_0.Strongest_Extension(
        "Example", ["Test"]
    ) == "Example.Test"

# Generated at 2026-10-24 05:58:19.428814
# Unit test for function Strongest_Extension

# Generated at 2026-10-24 05:58:27.980826
# Unit test for function Strongest_Extension
def test_Strongest_Extension():assert module_0.Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'

# Generated at 2026-10-24 05:58:37.709891
# Unit test for function Strongest_Extension
def test_Strongest_Extension():
    # Extension with the greatest uppercase-minus-lowercase score
    assert module_0.Strongest_Extension(
        "Slices", ["SErvice", "LIFE"]
    ) == "Slices.LIFE"

    # Lowercase letters reduce the strength
    assert module_0.Strongest_Extension(
        "MyClass", ["aBc", "ABc", "ABC"]
    ) == "MyClass.ABC"

    # On a tie, the first extension is selected
    assert module_0.Strongest_Extension(
        "MyClass", ["AB", "CD"]
    ) == "MyClass.AB"

    # A single extension
    assert module_0.Strongest_Extension(
        "Test", ["Extension"]
    ) == "Test.Extension"

    # Non-alphabetic characters do not affect strength
    assert module_0.Strongest_Extension(
        "File", ["A1b", "AB-1"]
    ) == "File.AB-1"

# Generated at 2026-10-24 05:58:49.114858
# Unit test for function Strongest_Extension
def test_Strongest_Extension():
    # Extension with the greatest uppercase/lowercase difference
    assert module_0.Strongest_Extension(
        "MyClass", ["aB", "ABC", "ab"]
    ) == "MyClass.ABC"

    # If strengths are equal, the first extension is selected
    assert module_0.Strongest_Extension(
        "Test", ["ABcd", "XYzz"]
    ) == "Test.ABcd"

    # Non-alphabetic characters are ignored
    assert module_0.Strongest_Extension(
        "File", ["a!1", "B-2"]
    ) == "File.B-2"

    # Negative strengths are compared normally
    assert module_0.Strongest_Extension(
        "Module", ["abc", "de"]
    ) == "Module.de"

    # A single extension
    assert module_0.Strongest_Extension(
        "Base", ["Only"]
    ) == "Base.Only"