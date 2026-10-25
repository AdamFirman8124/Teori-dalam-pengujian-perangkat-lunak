

# Generated at 2026-10-24 15:26:00.986340
# Unit test for function hex_key

# Generated at 2026-10-24 15:26:03.402031
# Unit test for function hex_key

# Generated at 2026-10-24 15:26:05.813465
# Unit test for function hex_key

# Generated at 2026-10-24 15:26:08.226903
# Unit test for function hex_key

# Generated at 2026-10-24 15:26:10.641908
# Unit test for function hex_key

# Generated at 2026-10-24 15:26:13.057848
# Unit test for function hex_key

# Generated at 2026-10-24 15:26:15.473886
# Unit test for function hex_key

# Generated at 2026-10-24 15:26:17.882931
# Unit test for function hex_key

# Generated at 2026-10-24 15:26:20.295272
# Unit test for function hex_key

# Generated at 2026-10-24 15:26:22.708760
# Unit test for function hex_key

# Generated at 2026-10-24 15:26:36.765377
# Unit test for function hex_key
def test_hex_key():assert module_0.hex_key("AB") == 1

# Generated at 2026-10-24 15:26:49.419779
# Unit test for function hex_key
def test_hex_key():
    cases = [
        ("", 0),                 # empty string
        ("0", 0),                # no primes
        ("1", 0),
        ("2", 1),                # single prime digit
        ("B", 1),                # prime hex letter
        ("A", 0),                # non-prime hex letter
        ("bd", 0),               # lowercase is NOT counted (case-sensitive)
        ("AB", 1),               # A=no, B=yes
        ("1077E", 2),            # 7, 7
        ("ABED1A33", 4),         # B, D, 3, 3
        ("123456789ABCDEF", 6),  # 2, 3, 5, 7, B, D
        ("2B3D5F7", 6),          # 2, B, 3, D, 5, 7 (F excluded)
    ]
    for num, expected in cases:
        result = module_0.hex_key(num)
        assert result == expected, f"module_0.hex_key({num!r}) -> {result}, expected {expected}"