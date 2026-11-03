

# Generated at 2026-11-02 17:22:31.108081
# Unit test for function Strongest_Extension
def test_Strongest_Extension():
    # Basic case: extension with more uppercase letters wins
    assert module_0.Strongest_Extension('Slices', ['SErviCSHUB', 'Ptns', 'ware']) == 'Slices.SErviCSHUB'

    # Tie in strength: first extension in the list wins
    assert module_0.Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'

    # Single extension
    assert module_0.Strongest_Extension('Test', ['onlyOne']) == 'Test.onlyOne'

    # Non-alphabetic characters are ignored in strength calculation
    assert module_0.Strongest_Extension('Nums', ['a1B2', 'xyz']) == 'Nums.a1B2'

    # Both strengths negative: the less negative one wins
    assert module_0.Strongest_Extension('Neg', ['abcdef', 'abc']) == 'Neg.abc'

    # Later strictly stronger extension replaces earlier one
    assert module_0.Strongest_Extension('X', ['aB', 'AB', 'Ab']) == 'X.AB'

    # Class name joined with a dot
    assert module_0.Strongest_Extension('C', ['e']) == 'C.e'

    print("All tests passed!")


test_Strongest_Extension()

# Generated at 2026-11-02 17:23:50.719847
# Unit test for function Strongest_Extension
def test_Strongest_Extension():
    # Basic case: strength = uppercase count - lowercase count
    assert module_0.Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'

    # Example with all-negative strengths; highest (least negative) wins
    assert module_0.Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'

    # Tie in strength: first occurrence wins (strict > comparison)
    assert module_0.Strongest_Extension('Tie', ['AB', 'cd', 'EF']) == 'Tie.AB'

    # Single extension list
    assert module_0.Strongest_Extension('Single', ['only']) == 'Single.only'

    # Non-alphabetic characters are ignored in strength calculation
    assert module_0.Strongest_Extension('Nums', ['a1B2', 'xy']) == 'Nums.a1B2'

    # Mixed case comparison
    assert module_0.Strongest_Extension('C', ['abc', 'aB']) == 'C.aB'

    # Extension with only uppercase letters is strongest
    assert module_0.Strongest_Extension('X', ['aaa', 'ZZZ', 'bBb']) == 'X.ZZZ'

    print("All tests passed!")


test_Strongest_Extension()

# Generated at 2026-11-02 17:26:25.905130
# Unit test for function Strongest_Extension
def test_Strongest_Extension():
    # Basic case: extension with more uppercase letters is strongest
    assert module_0.Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'

    # Classic example: strongest by upper-lower difference
    assert module_0.Strongest_Extension(
        'Slices',
        ['SErviCS_ScHED', 'SErviCS_ScHEDing', 'SErviCS_ScHEDule', 'SErviCS_ScHEDuling']
    ) == 'Slices.SErviCS_ScHED'

    # Tie in strength: first extension wins
    assert module_0.Strongest_Extension('X', ['aB', 'Ab']) == 'X.aB'

    # Single extension with negative strength
    assert module_0.Strongest_Extension('Foo', ['bar']) == 'Foo.bar'

    # Empty string (strength 0) beats negative-strength extension
    assert module_0.Strongest_Extension('Cls', ['', 'a']) == 'Cls.'

    # Non-alphabetic characters contribute 0 to strength
    assert module_0.Strongest_Extension('Cls', ['123', 'Ab']) == 'Cls.123'

    # All uppercase beats all lowercase
    assert module_0.Strongest_Extension('Test', ['UPPER', 'lower']) == 'Test.UPPER'

    # Later extension wins only if strictly stronger
    assert module_0.Strongest_Extension('Mod', ['a', 'B']) == 'Mod.B'

# Generated at 2026-11-02 17:28:06.183388
# Unit test for function Strongest_Extension
def test_Strongest_Extension():
    # Basic case: extension with highest (uppercase - lowercase) count wins
    assert module_0.Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'
    assert module_0.Strongest_Extension('Slices', ['SErviSes', 'NamiSeS', 'manage', 'stack', 'extend']) == 'Slices.NamiSeS'

    # Tie in strength: first extension in the list wins
    assert module_0.Strongest_Extension('my_class', ['Ab', 'Cd', 'Ef']) == 'my_class.Ab'

    # Single extension in the list
    assert module_0.Strongest_Extension('Klass', ['onlyOne']) == 'Klass.onlyOne'

    # Non-alphabetic characters are ignored when counting
    assert module_0.Strongest_Extension('test', ['A1b!', 'BB']) == 'test.BB'
    assert module_0.Strongest_Extension('pkg', ['x_9Y', 'z']) == 'pkg.x_9Y'

    # All-lowercase extensions: least negative strength wins
    assert module_0.Strongest_Extension('mod', ['abc', 'ab', 'abcd']) == 'mod.ab'

    # All strengths negative: the strongest (least negative) is still chosen
    assert module_0.Strongest_Extension('C', ['bAd', 'bbAd']) == 'C.bAd'

    # Extension stronger than the first element replaces it
    assert module_0.Strongest_Extension('cls', ['a', 'XY']) == 'cls.XY'

    # Class name containing dots/special characters is used verbatim
    assert module_0.Strongest_Extension('My.Class_v2', ['X']) == 'My.Class_v2.X'

# Generated at 2026-11-02 17:29:20.698512
# Unit test for function Strongest_Extension
def test_Strongest_Extension():
    # Basic case: extension with more uppercase letters wins
    assert module_0.Strongest_Extension('Sushi', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Sushi.SErviNGSliCes'

    # Strongest extension at the end of the list
    assert module_0.Strongest_Extension('X', ['VarL', 'x', 'XX']) == 'X.XX'

    # All extensions have equal strength -> first one is chosen
    assert module_0.Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'

    # Ties broken by first occurrence
    assert module_0.Strongest_Extension('Tie', ['AB', 'CD']) == 'Tie.AB'

    # Extension with negative strength (more lowercase)
    assert module_0.Strongest_Extension('Neg', ['abcdef', 'aB']) == 'Neg.aB'

    # Single extension list
    assert module_0.Strongest_Extension('Single', ['OnlyOne']) == 'Single.OnlyOne'

    # Empty string extension vs normal one
    assert module_0.Strongest_Extension('Empty', ['', 'A']) == 'Empty.A'

    # Extension with non-alpha characters ignored in counting
    assert module_0.Strongest_Extension('Mixed', ['A1b2C3', 'abc']) == 'Mixed.A1b2C3'

    # Class name with dots/underscores is preserved
    assert module_0.Strongest_Extension('my.Class_name', ['Ext']) == 'my.Class_name.Ext'

    # Strength comparison ignores case of class name
    assert module_0.Strongest_Extension('CLASS', ['a', 'B']) == 'CLASS.B'

    print("All tests passed!")


test_Strongest_Extension()