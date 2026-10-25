

# Generated at 2026-10-24 14:20:13.253013
# Unit test for function Strongest_Extension
def test_Strongest_Extension():
    # basic: highest (uppercase - lowercase) wins
    assert module_0.Strongest_Extension("S", ["AA", "Be", "CC"]) == "S.AA"

    # tie -> first one kept (strict >)
    assert module_0.Strongest_Extension("S", ["Ab", "bA"]) == "S.Ab"

    # all lowercase -> first element
    assert module_0.Strongest_Extension("S", ["ab", "cd"]) == "S.ab"

    # single element
    assert module_0.Strongest_Extension("S", ["X"]) == "S.X"

    # non-alpha chars ignored
    assert module_0.Strongest_Extension("S", ["A_1", "b"]) == "S.A_1"

    # negative scores, best is still picked
    assert module_0.Strongest_Extension("S", ["abc", "AB"]) == "S.AB"

    # class name is concatenated verbatim
    assert module_0.Strongest_Extension("MyClass", ["xY", "ZZ"]) == "MyClass.ZZ"

# Generated at 2026-10-24 14:20:14.607199
# Unit test for function Strongest_Extension
def test_Strongest_Extension():
    # basic: highest (uppercase - lowercase) wins
    assert module_0.Strongest_Extension("S", ["AA", "Be", "CC"]) == "S.AA"

    # tie -> first one kept (strict >)
    assert module_0.Strongest_Extension("S", ["Ab", "bA"]) == "S.Ab"

    # all lowercase -> first element
    assert module_0.Strongest_Extension("S", ["ab", "cd"]) == "S.ab"

    # single element
    assert module_0.Strongest_Extension("S", ["X"]) == "S.X"

    # non-alpha chars ignored
    assert module_0.Strongest_Extension("S", ["A_1", "b"]) == "S.A_1"

    # negative scores, best is still picked
    assert module_0.Strongest_Extension("S", ["abc", "AB"]) == "S.AB"

    # class name is concatenated verbatim
    assert module_0.Strongest_Extension("MyClass", ["xY", "ZZ"]) == "MyClass.ZZ"

# Generated at 2026-10-24 14:20:16.005458
# Unit test for function Strongest_Extension
def test_Strongest_Extension():
    # basic: highest (uppercase - lowercase) wins
    assert module_0.Strongest_Extension("S", ["AA", "Be", "CC"]) == "S.AA"

    # tie -> first one kept (strict >)
    assert module_0.Strongest_Extension("S", ["Ab", "bA"]) == "S.Ab"

    # all lowercase -> first element
    assert module_0.Strongest_Extension("S", ["ab", "cd"]) == "S.ab"

    # single element
    assert module_0.Strongest_Extension("S", ["X"]) == "S.X"

    # non-alpha chars ignored
    assert module_0.Strongest_Extension("S", ["A_1", "b"]) == "S.A_1"

    # negative scores, best is still picked
    assert module_0.Strongest_Extension("S", ["abc", "AB"]) == "S.AB"

    # class name is concatenated verbatim
    assert module_0.Strongest_Extension("MyClass", ["xY", "ZZ"]) == "MyClass.ZZ"

# Generated at 2026-10-24 14:20:17.440389
# Unit test for function Strongest_Extension
def test_Strongest_Extension():
    # basic: highest (uppercase - lowercase) wins
    assert module_0.Strongest_Extension("S", ["AA", "Be", "CC"]) == "S.AA"

    # tie -> first one kept (strict >)
    assert module_0.Strongest_Extension("S", ["Ab", "bA"]) == "S.Ab"

    # all lowercase -> first element
    assert module_0.Strongest_Extension("S", ["ab", "cd"]) == "S.ab"

    # single element
    assert module_0.Strongest_Extension("S", ["X"]) == "S.X"

    # non-alpha chars ignored
    assert module_0.Strongest_Extension("S", ["A_1", "b"]) == "S.A_1"

    # negative scores, best is still picked
    assert module_0.Strongest_Extension("S", ["abc", "AB"]) == "S.AB"

    # class name is concatenated verbatim
    assert module_0.Strongest_Extension("MyClass", ["xY", "ZZ"]) == "MyClass.ZZ"

# Generated at 2026-10-24 14:20:19.963500
# Unit test for function Strongest_Extension

# Generated at 2026-10-24 14:20:22.381640
# Unit test for function Strongest_Extension

# Generated at 2026-10-24 14:20:24.881895
# Unit test for function Strongest_Extension