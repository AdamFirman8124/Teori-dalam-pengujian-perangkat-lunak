

# Generated at 2026-10-24 13:47:52.294454
# Unit test for function int_to_mini_roman

# Generated at 2026-10-24 13:47:54.711071
# Unit test for function int_to_mini_roman

# Generated at 2026-10-24 13:47:57.125824
# Unit test for function int_to_mini_roman

# Generated at 2026-10-24 13:47:59.541482
# Unit test for function int_to_mini_roman

# Generated at 2026-10-24 13:48:01.953636
# Unit test for function int_to_mini_roman

# Generated at 2026-10-24 13:48:04.379491
# Unit test for function int_to_mini_roman

# Generated at 2026-10-24 13:48:13.770839
# Unit test for function int_to_mini_roman

# Generated at 2026-10-24 13:48:16.274747
# Unit test for function int_to_mini_roman

# Generated at 2026-10-24 13:48:18.808929
# Unit test for function int_to_mini_roman

# Generated at 2026-10-24 13:48:21.322523
# Unit test for function int_to_mini_roman

# Generated at 2026-10-24 13:48:23.821506
# Unit test for function int_to_mini_roman

# Generated at 2026-10-24 13:48:40.685807
# Unit test for function int_to_mini_roman
def test_int_to_mini_roman():assert module_0.int_to_mini_roman(1) == "i"

# Generated at 2026-10-24 13:48:49.055786
# Unit test for function int_to_mini_roman
def test_int_to_mini_roman():
    # Basic values
    assert module_0.int_to_mini_roman(1) == "i"
    assert module_0.int_to_mini_roman(4) == "iv"
    assert module_0.int_to_mini_roman(5) == "v"
    assert module_0.int_to_mini_roman(9) == "ix"
    assert module_0.int_to_mini_roman(10) == "x"
    assert module_0.int_to_mini_roman(40) == "xl"
    assert module_0.int_to_mini_roman(50) == "l"
    assert module_0.int_to_mini_roman(90) == "xc"
    assert module_0.int_to_mini_roman(100) == "c"
    assert module_0.int_to_mini_roman(400) == "cd"
    assert module_0.int_to_mini_roman(500) == "d"
    assert module_0.int_to_mini_roman(900) == "cm"
    assert module_0.int_to_mini_roman(1000) == "m"

    # Subtractive combinations
    assert module_0.int_to_mini_roman(14) == "xiv"
    assert module_0.int_to_mini_roman(19) == "xix"
    assert module_0.int_to_mini_roman(44) == "xliv"
    assert module_0.int_to_mini_roman(99) == "xcix"
    assert module_0.int_to_mini_roman(444) == "cdxliv"
    assert module_0.int_to_mini_roman(944) == "cmxliv"
    assert module_0.int_to_mini_roman(1994) == "mcmxciv"

    # Repetition and mixed values
    assert module_0.int_to_mini_roman(3) == "iii"
    assert module_0.int_to_mini_roman(38) == "xxxviii"
    assert module_0.int_to_mini_roman(2023) == "mmxxiii"
    assert module_0.int_to_mini_roman(3000) == "mmm"

    # Round-trip check against a decoder
    def mini_roman_to_int(s):
        vals = {"i": 1, "v": 5, "x": 10, "l": 50, "c": 100, "d": 500, "m": 1000}
        total = 0
        for a, b in zip(s, s[1:]):
            total += vals[a] if vals[a] >= vals[b] else -vals[a]
        return total + (vals[s[-1]] if s else 0)

    for n in range(1, 4000):
        assert mini_roman_to_int(module_0.int_to_mini_roman(n)) == n, f"round-trip failed for {n}"

    print("All tests passed!")


# Run the test
test_int_to_mini_roman()