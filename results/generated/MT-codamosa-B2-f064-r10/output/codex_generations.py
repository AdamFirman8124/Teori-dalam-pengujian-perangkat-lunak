

# Generated at 2026-10-25 02:58:47.941150
# Unit test for function vowels_count

# Generated at 2026-10-25 02:58:50.357855
# Unit test for function vowels_count

# Generated at 2026-10-25 02:58:52.773785
# Unit test for function vowels_count

# Generated at 2026-10-25 02:58:55.189065
# Unit test for function vowels_count

# Generated at 2026-10-25 02:58:59.263044
# Unit test for function vowels_count
def test_vowels_count():assert module_0.vowels_count("hello") == 2

# Generated at 2026-10-25 02:59:00.697565
# Unit test for function vowels_count
def test_vowels_count():
    # basic counting
    assert module_0.vowels_count("hello") == 2
    assert module_0.vowels_count("abcde") == 2
    assert module_0.vowels_count("bcdfg") == 0
    assert module_0.vowels_count("aeiouAEIOU") == 10
    assert module_0.vowels_count("ACEDY") == 3
    # y/Y at end counts as vowel
    assert module_0.vowels_count("y") == 1
    assert module_0.vowels_count("Y") == 1
    assert module_0.vowels_count("sky") == 1
    assert module_0.vowels_count("happy") == 2
    assert module_0.vowels_count("boy") == 2
    # y not at end does not count
    assert module_0.vowels_count("yellow") == 2
    assert module_0.vowels_count("Year") == 2

# Generated at 2026-10-25 02:59:02.133484
# Unit test for function vowels_count
def test_vowels_count():
    # basic counting
    assert module_0.vowels_count("hello") == 2
    assert module_0.vowels_count("abcde") == 2
    assert module_0.vowels_count("bcdfg") == 0
    assert module_0.vowels_count("aeiouAEIOU") == 10
    assert module_0.vowels_count("ACEDY") == 3
    # y/Y at end counts as vowel
    assert module_0.vowels_count("y") == 1
    assert module_0.vowels_count("Y") == 1
    assert module_0.vowels_count("sky") == 1
    assert module_0.vowels_count("happy") == 2
    assert module_0.vowels_count("boy") == 2
    # y not at end does not count
    assert module_0.vowels_count("yellow") == 2
    assert module_0.vowels_count("Year") == 2

# Generated at 2026-10-25 02:59:03.564171
# Unit test for function vowels_count
def test_vowels_count():
    # basic counting
    assert module_0.vowels_count("hello") == 2
    assert module_0.vowels_count("abcde") == 2
    assert module_0.vowels_count("bcdfg") == 0
    assert module_0.vowels_count("aeiouAEIOU") == 10
    assert module_0.vowels_count("ACEDY") == 3
    # y/Y at end counts as vowel
    assert module_0.vowels_count("y") == 1
    assert module_0.vowels_count("Y") == 1
    assert module_0.vowels_count("sky") == 1
    assert module_0.vowels_count("happy") == 2
    assert module_0.vowels_count("boy") == 2
    # y not at end does not count
    assert module_0.vowels_count("yellow") == 2
    assert module_0.vowels_count("Year") == 2