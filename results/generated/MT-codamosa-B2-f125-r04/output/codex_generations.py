

# Generated at 2026-10-25 10:30:47.700201
# Unit test for function split_words
def test_split_words():
    # Case 1: spaces â split on whitespace
    assert module_0.split_words("Hello world!") == ["Hello", "world!"]
    assert module_0.split_words("one two three") == ["one", "two", "three"]

    # Case 2: commas â commas treated as separators
    assert module_0.split_words("Hello,world!") == ["Hello", "world!"]
    assert module_0.split_words("a,b,c") == ["a", "b", "c"]

    # Case 3: no space or comma â count lowercase chars with even ord
    # even-ord letters: b(98), d(100), f(102), h(104)...
    assert module_0.split_words("abcdef") == 3        # b, d, f
    assert module_0.split_words("aaabb") == 4         # b appears 3 times... see note below
    assert module_0.split_words("") == 0
    assert module_0.split_words("ABC") == 0           # uppercase ignored
    assert module_0.split_words("1234") == 2          # '2'(50), '4'(52) are even-ord chars

# Generated at 2026-10-25 10:30:50.208023
# Unit test for function split_words

# Generated at 2026-10-25 10:30:52.623072
# Unit test for function split_words

# Generated at 2026-10-25 10:30:55.036931
# Unit test for function split_words

# Generated at 2026-10-25 10:30:57.454087
# Unit test for function split_words

# Generated at 2026-10-25 10:30:59.868676
# Unit test for function split_words

# Generated at 2026-10-25 10:31:02.286902
# Unit test for function split_words

# Generated at 2026-10-25 10:31:04.700668
# Unit test for function split_words

# Generated at 2026-10-25 10:31:07.116017
# Unit test for function split_words

# Generated at 2026-10-25 10:31:09.533694
# Unit test for function split_words

# Generated at 2026-10-25 10:31:12.002960
# Unit test for function split_words

# Generated at 2026-10-25 10:31:14.409760
# Unit test for function split_words

# Generated at 2026-10-25 10:31:16.821447
# Unit test for function split_words