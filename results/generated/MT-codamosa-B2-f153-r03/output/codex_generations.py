

# Generated at 2026-10-24 06:14:28.317264
# Unit test for function Strongest_Extension
def test_Strongest_Extension():
    # Extension with the highest strength is selected
    assert module_0.Strongest_Extension("MyClass", ["AA", "Bc", "DDD"]) == "MyClass.DDD"

    # Strength = uppercase letters - lowercase letters
    assert module_0.Strongest_Extension("Test", ["abc", "aBC", "ABcd"]) == "Test.aBC"

    # In a tie, the first extension is selected
    assert module_0.Strongest_Extension("File", ["AB", "CD", "ef"]) == "File.AB"

    # Non-alphabetic characters do not affect strength
    assert module_0.Strongest_Extension("Document", ["A-1", "BB!", "C_d"]) == "Document.BB!"

    # A single extension is returned
    assert module_0.Strongest_Extension("Only", ["ext"]) == "Only.ext"

# Generated at 2026-10-24 06:14:39.714933
# Unit test for function Strongest_Extension
def test_Strongest_Extension():
    # Selects the extension with the highest strength
    assert module_0.Strongest_Extension(
        "Slices",
        ["SErviNGSliCes", "Cheese", "StuFfed"]
    ) == "Slices.SErviNGSliCes"

    # All-uppercase extension is strongest
    assert module_0.Strongest_Extension(
        "Class",
        ["lowercase", "MiXeD", "UPPER"]
    ) == "Class.UPPER"

    # In a tie, the first extension is selected
    assert module_0.Strongest_Extension(
        "Test",
        ["ABcd", "XYzz"]
    ) == "Test.ABcd"

    # Non-alphabetic characters do not affect strength
    assert module_0.Strongest_Extension(
        "File",
        ["A1!", "bb"]
    ) == "File.A1!"

# Generated at 2026-10-24 06:14:42.228871
# Unit test for function Strongest_Extension

# Generated at 2026-10-24 06:14:44.732737
# Unit test for function Strongest_Extension

# Generated at 2026-10-24 06:14:47.175112
# Unit test for function Strongest_Extension

# Generated at 2026-10-24 06:14:49.568975
# Unit test for function Strongest_Extension

# Generated at 2026-10-24 06:14:51.981959
# Unit test for function Strongest_Extension

# Generated at 2026-10-24 06:14:54.397641
# Unit test for function Strongest_Extension

# Generated at 2026-10-24 06:15:05.977581
# Unit test for function Strongest_Extension
def test_Strongest_Extension():
    # Selects the extension with the highest uppercase-minus-lowercase score
    assert module_0.Strongest_Extension(
        "Slices", ["SErviCe", "CheEse", "STOre"]
    ) == "Slices.STOre"

    # A fully uppercase extension is stronger
    assert module_0.Strongest_Extension(
        "MyClass", ["Aa", "B", "c"]
    ) == "MyClass.B"

    # In a tie, the first extension is selected
    assert module_0.Strongest_Extension(
        "Demo", ["ABcd", "XYzz"]
    ) == "Demo.ABcd"

    # Works when all scores are negative
    assert module_0.Strongest_Extension(
        "Lower", ["abc", "de", "fghi"]
    ) == "Lower.de"

    # Non-alphabetic characters do not affect the score
    assert module_0.Strongest_Extension(
        "Symbols", ["A1!", "BB??c"]
    ) == "Symbols.A1!"