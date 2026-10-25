

# Generated at 2026-10-25 05:15:31.076326
# Unit test for function Strongest_Extension
def test_Strongest_Extension():
    assert module_0.Strongest_Extension("MyClass", ["AA", "Be", "CC"]) == "MyClass.AA"
    assert module_0.Strongest_Extension("MyClass", ["aA", "B", "c"]) == "MyClass.B"
    assert module_0.Strongest_Extension("Class", ["abc", "ABC", "AbC"]) == "Class.ABC"
    assert module_0.Strongest_Extension("Test", ["AB", "CD", "EF"]) == "Test.AB"  # first wins ties
    assert module_0.Strongest_Extension("File", ["A1!", "bb", "Cc"]) == "File.A1!"  # nonletters ignored

# Generated at 2026-10-25 05:15:40.961392
# Unit test for function Strongest_Extension
def test_Strongest_Extension():
    # Highest strength wins
    assert module_0.Strongest_Extension(
        "MyClass", ["abc", "ABC", "AbC"]
    ) == "MyClass.ABC"

    # If strengths are equal, the first extension wins
    assert module_0.Strongest_Extension(
        "MyClass", ["AA", "be", "CC"]
    ) == "MyClass.AA"

    # Lowercase letters reduce strength
    assert module_0.Strongest_Extension(
        "Vehicle", ["Car", "TRUCK", "plane"]
    ) == "Vehicle.TRUCK"

    # Non-alphabetic characters do not affect strength
    assert module_0.Strongest_Extension(
        "File", ["A1!", "bb22", "CCC?"]
    ) == "File.CCC?"

    # A later extension can replace the initial extension
    assert module_0.Strongest_Extension(
        "Example", ["lower", "MiXeD", "UPPER"]
    ) == "Example.UPPER"

# Generated at 2026-10-25 05:15:48.026308
# Unit test for function Strongest_Extension
def test_Strongest_Extension():
    # Extension with the highest uppercase-minus-lowercase score
    assert module_0.Strongest_Extension("MyClass", ["Aa", "ABC", "ab"]) == "MyClass.ABC"

    # If scores are tied, return the first extension
    assert module_0.Strongest_Extension("MyClass", ["AB", "CD", "EF"]) == "MyClass.AB"

    # All extensions have negative scores
    assert module_0.Strongest_Extension("Test", ["abc", "Abc", "abcd"]) == "Test.Abc"

    # Non-alphabetic characters do not affect the score
    assert module_0.Strongest_Extension("File", ["A1B!", "ABC?", "ab"]) == "File.ABC?"

    # A single extension
    assert module_0.Strongest_Extension("Only", ["Py"]) == "Only.Py"

    # Empty extension string
    assert module_0.Strongest_Extension("Base", ["", "a", "A"]) == "Base.A"

# Generated at 2026-10-25 05:15:56.494462
# Unit test for function Strongest_Extension
def test_Strongest_Extension():
    assert module_0.Strongest_Extension(
        "Slices",
        ["SErviNGS", "Cheese", "StuFfed"]
    ) == "Slices.SErviNGS"

    assert module_0.Strongest_Extension(
        "Vehicle",
        ["Car", "Truck", "BUs"]
    ) == "Vehicle.BUs"

    # The first extension wins when strengths are equal.
    assert module_0.Strongest_Extension(
        "Class",
        ["ABcd", "XYzz"]
    ) == "Class.ABcd"

    # Non-alphabetic characters do not affect strength.
    assert module_0.Strongest_Extension(
        "File",
        ["A-1b", "ABC"]
    ) == "File.ABC"

    # A single extension is returned automatically.
    assert module_0.Strongest_Extension(
        "Animal",
        ["CAT"]
    ) == "Animal.CAT"

# Generated at 2026-10-25 05:16:03.979904
# Unit test for function Strongest_Extension
def test_Strongest_Extension():
    # Extension with the highest uppercase-minus-lowercase score
    assert module_0.Strongest_Extension(
        "Slices", ["DIAMOND", "Ruby", "coal"]
    ) == "Slices.DIAMOND"

    # Lowercase letters produce a negative score
    assert module_0.Strongest_Extension(
        "Power", ["weak", "STRONG", "Medium"]
    ) == "Power.STRONG"

    # On a tie, the first extension is selected
    assert module_0.Strongest_Extension(
        "Example", ["AB", "CD", "EF"]
    ) == "Example.AB"

    # Non-alphabetic characters do not affect the score
    assert module_0.Strongest_Extension(
        "File", ["A1-b", "ZZ!!", "abc"]
    ) == "File.ZZ!!"

    # Single extension
    assert module_0.Strongest_Extension(
        "Only", ["Extension"]
    ) == "Only.Extension"