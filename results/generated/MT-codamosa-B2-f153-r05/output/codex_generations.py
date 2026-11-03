

# Generated at 2026-11-02 12:22:30.889605
# Unit test for function Strongest_Extension
def test_Strongest_Extension():
    # Basic case: extension with more uppercase letters wins
    assert module_0.Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'

    # Only one extension available
    assert module_0.Strongest_Extension('Class', ['ExT']) == 'Class.ExT'

    # All lowercase should have negative strength, still returned if only option
    assert module_0.Strongest_Extension('Class', ['abc']) == 'Class.abc'

    # Tie in strength: first one in the list wins (strict > comparison)
    assert module_0.Strongest_Extension('my_class', ['AA', 'BB', 'CC']) == 'my_class.AA'

    # Later extension strictly stronger than earlier ones
    assert module_0.Strongest_Extension('my_class', ['a', 'BB', 'c']) == 'my_class.BB'

    # Special characters are not counted (isalpha check)
    assert module_0.Strongest_Extension('X', ['!@#$', 'A!']) == 'X.A!'

    # Digits ignored, only alpha counted
    assert module_0.Strongest_Extension('Num', ['a1B2', 'xy']) == 'Num.a1B2'

    # Equal strength (all zero) keeps the first
    assert module_0.Strongest_Extension('Zero', ['12', '!!', '34']) == 'Zero.12'

    # Extension with mixed case, uppercase advantage
    assert module_0.Strongest_Extension('Prog', ['pHiLiP', 'JoHn', 'aLiCe']) == 'Prog.pHiLiP'

    # Class name with special characters passes through unchanged
    assert module_0.Strongest_Extension('My-Cl@ss', ['Ext']) == 'My-Cl@ss.Ext'

    # Negative strength comparison: less negative wins
    assert module_0.Strongest_Extension('Neg', ['abcd', 'ab']) == 'Neg.ab'

    print("All tests passed!")


# Run tests
test_Strongest_Extension()

# Generated at 2026-11-02 12:23:40.840538
# Unit test for function Strongest_Extension
def test_Strongest_Extension():
    # Standard example: strength = uppercase count - lowercase count
    assert module_0.Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'

    # Tie in strength: first extension wins
    assert module_0.Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'

    # Single extension
    assert module_0.Strongest_Extension('X', ['abc']) == 'X.abc'

    # All lowercase (negative strength): first wins
    assert module_0.Strongest_Extension('Foo', ['abc', 'def']) == 'Foo.abc'

    # Non-alphabetic characters are ignored
    assert module_0.Strongest_Extension('Bar', ['a1B!', 'xy']) == 'Bar.a1B!'

    # Empty extension string
    assert module_0.Strongest_Extension('Foo', ['']) == 'Foo.'

    # Later extension strictly stronger wins
    assert module_0.Strongest_Extension('Cls', ['aa', 'BB']) == 'Cls.BB'

    # Class name joined with dot
    assert module_0.Strongest_Extension('MyClass', ['x']) == 'MyClass.x'

# Generated at 2026-11-02 12:24:42.371148
# Unit test for function Strongest_Extension
def test_Strongest_Extension():# Basic case: strongest extension has the most uppercase letters
    assert module_0.Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'

    # Classic example: strength computed as uppercase count minus lowercase count
    assert module_0.Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'

    # Mixed case extension wins over all-lowercase ones
    assert module_0.Strongest_Extension('random', ['abc', 'ABC', 'aBc']) == 'random.ABC'

    # Single extension in the list
    assert module_0.Strongest_Extension('single', ['xyz']) == 'single.xyz'

    # Tie in strength: the first extension encountered wins
    assert module_0.Strongest_Extension('tie', ['AB', 'CD', 'ef']) == 'tie.AB'

    # Digits and special characters are ignored (isalpha check)
    assert module_0.Strongest_Extension('digits', ['a1b2', 'X9Y']) == 'digits.X9Y'

    # Extension with no alphabetic characters has strength 0
    assert module_0.Strongest_Extension('empty_str', ['123', 'A!']) == 'empty_str.A!'

    # Class name with dots/underscores is preserved as-is
    assert module_0.Strongest_Extension('My_Class.Name', ['ext']) == 'My_Class.Name.ext'

    # All strengths negative: the least negative (first among ties) wins
    assert module_0.Strongest_Extension('neg', ['abc', 'abC', 'a']) == 'neg.abC'

    print("All tests passed!")

# Generated at 2026-11-02 12:26:03.472078
# Unit test for function Strongest_Extension
def test_Strongest_Extension():
    # Basic case: first extension has the highest strength
    assert module_0.Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'

    # Tie in strength: first extension in the list wins
    assert module_0.Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'

    # Single extension in the list
    assert module_0.Strongest_Extension('Klass', ['abc']) == 'Klass.abc'

    # A later extension is stronger than earlier ones
    assert module_0.Strongest_Extension('X', ['aa', 'BB', 'c']) == 'X.BB'

    # Non-alphabetic characters (digits, punctuation) are ignored in strength
    assert module_0.Strongest_Extension('X', ['a1!B', 'cc']) == 'X.a1!B'

    # All-lowercase extensions: strength ties, first wins
    assert module_0.Strongest_Extension('Foo', ['abc', 'def']) == 'Foo.abc'

    # Strength can be negative; still picks the maximum
    assert module_0.Strongest_Extension('Neg', ['aaaa', 'bbC']) == 'Neg.bbC'

    print("All tests passed!")


test_Strongest_Extension()

# Generated at 2026-11-02 12:27:20.920035
# Unit test for function Strongest_Extension
def test_Strongest_Extension():
    # Basic case: extension with more uppercase relative to lowercase wins
    assert module_0.Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'
    assert module_0.Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'

    # Ties are resolved by first occurrence
    assert module_0.Strongest_Extension('my_class', ['Be', 'AA', 'CC']) == 'my_class.Be'
    assert module_0.Strongest_Extension('X', ['aBc', 'Abc']) == 'X.aBc'

    # Single extension
    assert module_0.Strongest_Extension('X', ['abc']) == 'X.abc'
    assert module_0.Strongest_Extension('X', ['ABC']) == 'X.ABC'

    # All uppercase beats all lowercase
    assert module_0.Strongest_Extension('X', ['abc', 'ABC']) == 'X.ABC'
    assert module_0.Strongest_Extension('X', ['ABC', 'abc']) == 'X.ABC'

    # Mixed case comparisons
    assert module_0.Strongest_Extension('X', ['AAb', 'aBb']) == 'X.AAb'
    assert module_0.Strongest_Extension('X', ['A', 'b', 'C']) == 'X.A'

    # Extensions with digits/symbols (non-alpha chars ignored)
    assert module_0.Strongest_Extension('X', ['A1b', 'aB2']) == 'X.A1b'
    assert module_0.Strongest_Extension('X', ['!@#', 'a']) == 'X.a'

    # Empty extension string has strength 0
    assert module_0.Strongest_Extension('X', ['', 'a']) == 'X.a'
    assert module_0.Strongest_Extension('X', ['a', '']) == 'X.a'

    # Class name formatting
    assert module_0.Strongest_Extension('My_Class', ['Ab']) == 'My_Class.Ab'
    assert module_0.Strongest_Extension('', ['Ab']) == '.Ab'

    # Negative strength comparisons
    assert module_0.Strongest_Extension('X', ['aaaaB', 'aaBB']) == 'X.aaBB'