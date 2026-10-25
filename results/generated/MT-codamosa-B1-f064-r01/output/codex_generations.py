

# Generated at 2026-10-24 13:34:36.178143
# Unit test for function vowels_count
def test_vowels_count():
    # basic vowels, both cases
    assert module_0.vowels_count("hello") == 2
    assert module_0.vowels_count("HELLO") == 2
    assert module_0.vowels_count("aeiou") == 5
    assert module_0.vowels_count("AEIOU") == 5

    # no vowels, no trailing y
    assert module_0.vowels_count("rhythm") == 0
    assert module_0.vowels_count("cwm") == 0

    # trailing y adds one (lowercase and uppercase)
    assert module_0.vowels_count("sky") == 1
    assert module_0.vowels_count("SKY") == 1
    assert module_0.vowels_count("happy") == 2      # 'a' + trailing 'y'
    assert module_0.vowels_count("toy") == 2        # 'o' + trailing 'y'
    assert module_0.vowels_count("yellow") == 2     # 'e','o' â ends in 'w', no bonus

    # y not at the end is not a vowel
    assert module_0.vowels_count("yes") == 1
    assert module_0.vowels_count("cycle") == 2      # 'e' only; 'y' is mid-string

    # single-char strings
    assert module_0.vowels_count("y") == 1
    assert module_0.vowels_count("b") == 0

    # empty string
    assert module_0.vowels_count("") == 0

# Generated at 2026-10-24 13:35:06.896937
# Unit test for function vowels_count
def test_vowels_count():
    assert module_0.vowels_count("abc") == 1
    assert module_0.vowels_count("aeiou") == 5
    assert module_0.vowels_count("AEIOU") == 5
    assert module_0.vowels_count("bcdfg") == 0
    assert module_0.vowels_count("hello") == 2
    assert module_0.vowels_count("yeah") == 2
    assert module_0.vowels_count("bicycle") == 2  # middle 'y' is not counted
    assert module_0.vowels_count("happy") == 2    # 'a' + final 'y'
    assert module_0.vowels_count("sky") == 1      # only final 'y'
    assert module_0.vowels_count("syzygy") == 1   # only final 'y'
    assert module_0.vowels_count("boy") == 2
    assert module_0.vowels_count("yay") == 2
    assert module_0.vowels_count("ya") == 1       # 'y' not at end
    assert module_0.vowels_count("ay") == 2       # 'a' + final 'y'
    assert module_0.vowels_count("y") == 1
    assert module_0.vowels_count("Y") == 1

# Generated at 2026-10-24 13:35:23.485687
# Unit test for function vowels_count
def test_vowels_count():
    assert module_0.vowels_count("abc") == 1
    assert module_0.vowels_count("aeiou") == 5
    assert module_0.vowels_count("AEIOU") == 5
    assert module_0.vowels_count("bcdfg") == 0
    assert module_0.vowels_count("hello") == 2
    assert module_0.vowels_count("yeah") == 2
    assert module_0.vowels_count("bicycle") == 2  # middle 'y' is not counted
    assert module_0.vowels_count("happy") == 2    # 'a' + final 'y'
    assert module_0.vowels_count("sky") == 1      # only final 'y'
    assert module_0.vowels_count("syzygy") == 1   # only final 'y'
    assert module_0.vowels_count("boy") == 2
    assert module_0.vowels_count("yay") == 2
    assert module_0.vowels_count("ya") == 1       # 'y' not at end
    assert module_0.vowels_count("ay") == 2       # 'a' + final 'y'
    assert module_0.vowels_count("y") == 1
    assert module_0.vowels_count("Y") == 1

# Generated at 2026-10-24 13:35:24.924615
# Unit test for function vowels_count
def test_vowels_count():
    # basic vowels, both cases
    assert module_0.vowels_count("hello") == 2
    assert module_0.vowels_count("HELLO") == 2
    assert module_0.vowels_count("aeiou") == 5
    assert module_0.vowels_count("AEIOU") == 5

    # no vowels, no trailing y
    assert module_0.vowels_count("rhythm") == 0
    assert module_0.vowels_count("cwm") == 0

    # trailing y adds one (lowercase and uppercase)
    assert module_0.vowels_count("sky") == 1
    assert module_0.vowels_count("SKY") == 1
    assert module_0.vowels_count("happy") == 2      # 'a' + trailing 'y'
    assert module_0.vowels_count("toy") == 2        # 'o' + trailing 'y'
    assert module_0.vowels_count("yellow") == 2     # 'e','o' â ends in 'w', no bonus

    # y not at the end is not a vowel
    assert module_0.vowels_count("yes") == 1
    assert module_0.vowels_count("cycle") == 2      # 'e' only; 'y' is mid-string

    # single-char strings
    assert module_0.vowels_count("y") == 1
    assert module_0.vowels_count("b") == 0

    # empty string
    assert module_0.vowels_count("") == 0

# Generated at 2026-10-24 13:35:26.310924
# Unit test for function vowels_count
def test_vowels_count():
    assert module_0.vowels_count("abc") == 1
    assert module_0.vowels_count("aeiou") == 5
    assert module_0.vowels_count("AEIOU") == 5
    assert module_0.vowels_count("bcdfg") == 0
    assert module_0.vowels_count("hello") == 2
    assert module_0.vowels_count("yeah") == 2
    assert module_0.vowels_count("bicycle") == 2  # middle 'y' is not counted
    assert module_0.vowels_count("happy") == 2    # 'a' + final 'y'
    assert module_0.vowels_count("sky") == 1      # only final 'y'
    assert module_0.vowels_count("syzygy") == 1   # only final 'y'
    assert module_0.vowels_count("boy") == 2
    assert module_0.vowels_count("yay") == 2
    assert module_0.vowels_count("ya") == 1       # 'y' not at end
    assert module_0.vowels_count("ay") == 2       # 'a' + final 'y'
    assert module_0.vowels_count("y") == 1
    assert module_0.vowels_count("Y") == 1