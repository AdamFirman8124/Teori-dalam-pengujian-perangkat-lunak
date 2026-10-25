

# Generated at 2026-10-24 13:57:36.183038
# Unit test for function int_to_mini_roman

# Generated at 2026-10-24 13:57:38.600185
# Unit test for function int_to_mini_roman

# Generated at 2026-10-24 13:57:46.373779
# Unit test for function int_to_mini_roman
def test_int_to_mini_roman():assert module_0.int_to_mini_roman(1) == "i"

# Generated at 2026-10-24 13:57:47.702307
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

# Generated at 2026-10-24 13:57:49.046196
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

# Generated at 2026-10-24 13:57:50.399795
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

# Generated at 2026-10-24 13:57:51.718019
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

# Generated at 2026-10-24 13:58:42.938847
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

# Generated at 2026-10-24 13:58:44.293408
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

# Generated at 2026-10-24 13:58:45.667813
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

# Generated at 2026-10-24 13:58:47.050176
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

# Generated at 2026-10-24 13:58:48.392943
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

# Generated at 2026-10-24 13:58:49.809354
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

# Generated at 2026-10-24 13:58:51.208842
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

# Generated at 2026-10-24 13:58:52.534539
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

# Generated at 2026-10-24 13:58:53.960990
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

# Generated at 2026-10-24 13:58:55.326242
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

# Generated at 2026-10-24 13:58:57.845218
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

# Generated at 2026-10-24 13:58:59.366713
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

# Generated at 2026-10-24 13:59:01.897927
# Unit test for function int_to_mini_roman

# Generated at 2026-10-24 13:59:04.452932
# Unit test for function int_to_mini_roman

# Generated at 2026-10-24 13:59:06.985891
# Unit test for function int_to_mini_roman

# Generated at 2026-10-24 13:59:09.511055
# Unit test for function int_to_mini_roman

# Generated at 2026-10-24 13:59:12.067127
# Unit test for function int_to_mini_roman

# Generated at 2026-10-24 13:59:14.888401
# Unit test for function int_to_mini_roman

# Generated at 2026-10-24 13:59:17.528882
# Unit test for function int_to_mini_roman

# Generated at 2026-10-24 13:59:20.070599
# Unit test for function int_to_mini_roman

# Generated at 2026-10-24 13:59:22.578505
# Unit test for function int_to_mini_roman

# Generated at 2026-10-24 13:59:25.110100
# Unit test for function int_to_mini_roman

# Generated at 2026-10-24 13:59:27.612787
# Unit test for function int_to_mini_roman

# Generated at 2026-10-24 13:59:30.116749
# Unit test for function int_to_mini_roman

# Generated at 2026-10-24 13:59:32.621775
# Unit test for function int_to_mini_roman

# Generated at 2026-10-24 13:59:35.119418
# Unit test for function int_to_mini_roman

# Generated at 2026-10-24 13:59:37.668854
# Unit test for function int_to_mini_roman

# Generated at 2026-10-24 13:59:40.197829
# Unit test for function int_to_mini_roman

# Generated at 2026-10-24 13:59:42.712904
# Unit test for function int_to_mini_roman

# Generated at 2026-10-24 13:59:45.226009
# Unit test for function int_to_mini_roman

# Generated at 2026-10-24 13:59:47.761040
# Unit test for function int_to_mini_roman

# Generated at 2026-10-24 13:59:50.277407
# Unit test for function int_to_mini_roman

# Generated at 2026-10-24 13:59:52.795420
# Unit test for function int_to_mini_roman

# Generated at 2026-10-24 13:59:55.287803
# Unit test for function int_to_mini_roman

# Generated at 2026-10-24 13:59:57.802656
# Unit test for function int_to_mini_roman

# Generated at 2026-10-24 14:00:00.295795
# Unit test for function int_to_mini_roman

# Generated at 2026-10-24 14:03:55.430129
# Unit test for function int_to_mini_roman

# Generated at 2026-10-24 14:03:58.984400
# Unit test for function int_to_mini_roman

# Generated at 2026-10-24 14:04:01.934108
# Unit test for function int_to_mini_roman

# Generated at 2026-10-24 14:04:05.375899
# Unit test for function int_to_mini_roman

# Generated at 2026-10-24 14:04:09.481991
# Unit test for function int_to_mini_roman

# Generated at 2026-10-24 14:04:14.625284
# Unit test for function int_to_mini_roman

# Generated at 2026-10-24 14:04:17.880785
# Unit test for function int_to_mini_roman

# Generated at 2026-10-24 14:04:21.065481
# Unit test for function int_to_mini_roman

# Generated at 2026-10-24 14:04:24.345168
# Unit test for function int_to_mini_roman

# Generated at 2026-10-24 14:04:27.052556
# Unit test for function int_to_mini_roman

# Generated at 2026-10-24 14:04:30.764512
# Unit test for function int_to_mini_roman

# Generated at 2026-10-24 14:04:33.405066
# Unit test for function int_to_mini_roman

# Generated at 2026-10-24 14:04:37.495071
# Unit test for function int_to_mini_roman

# Generated at 2026-10-24 14:04:40.561823
# Unit test for function int_to_mini_roman

# Generated at 2026-10-24 14:04:44.194582
# Unit test for function int_to_mini_roman

# Generated at 2026-10-24 14:04:48.149938
# Unit test for function int_to_mini_roman

# Generated at 2026-10-24 14:04:52.517630
# Unit test for function int_to_mini_roman

# Generated at 2026-10-24 14:04:54.766237
# Unit test for function int_to_mini_roman

# Generated at 2026-10-24 14:04:57.345670
# Unit test for function int_to_mini_roman

# Generated at 2026-10-24 14:05:02.416147
# Unit test for function int_to_mini_roman

# Generated at 2026-10-24 14:05:05.065364
# Unit test for function int_to_mini_roman

# Generated at 2026-10-24 14:05:08.541962
# Unit test for function int_to_mini_roman

# Generated at 2026-10-24 14:05:11.185086
# Unit test for function int_to_mini_roman

# Generated at 2026-10-24 14:05:14.212168
# Unit test for function int_to_mini_roman

# Generated at 2026-10-24 14:05:17.813435
# Unit test for function int_to_mini_roman

# Generated at 2026-10-24 14:05:21.098372
# Unit test for function int_to_mini_roman

# Generated at 2026-10-24 14:05:25.993445
# Unit test for function int_to_mini_roman

# Generated at 2026-10-24 14:05:29.540681
# Unit test for function int_to_mini_roman

# Generated at 2026-10-24 14:05:32.759034
# Unit test for function int_to_mini_roman

# Generated at 2026-10-24 14:05:39.283159
# Unit test for function int_to_mini_roman