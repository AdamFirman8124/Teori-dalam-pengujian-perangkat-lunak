

# Generated at 2026-10-24 07:33:49.129099
# Unit test for function rounded_avg
def test_rounded_avg():
    # Normal ranges
    assert module_0.rounded_avg(1, 5) == "0b11"        # avg of 1..5 = 3
    assert module_0.rounded_avg(7, 13) == "0b1010"     # avg = 10
    assert module_0.rounded_avg(20, 33) == "0b1110"    # avg of 20..33 = 26.5 -> 26
    assert module_0.rounded_avg(-5, 5) == "0b0"        # avg = 0

    # Single-element range
    assert module_0.rounded_avg(4, 4) == "0b100"       # avg = 4

    # Invalid range
    assert module_0.rounded_avg(12, 3) == -1           # m < n

    print("All tests passed!")

# Generated at 2026-10-24 07:33:51.632576
# Unit test for function rounded_avg

# Generated at 2026-10-24 07:33:54.049042
# Unit test for function rounded_avg

# Generated at 2026-10-24 07:33:56.467068
# Unit test for function rounded_avg

# Generated at 2026-10-24 07:33:58.880028
# Unit test for function rounded_avg

# Generated at 2026-10-24 07:34:01.298251
# Unit test for function rounded_avg

# Generated at 2026-10-24 07:34:03.708931
# Unit test for function rounded_avg

# Generated at 2026-10-24 07:34:06.122184
# Unit test for function rounded_avg

# Generated at 2026-10-24 07:34:17.776529
# Unit test for function rounded_avg
def test_rounded_avg():
    assert module_0.rounded_avg(1, 5) == '0b11'
    assert module_0.rounded_avg(2, 4) == '0b11'
    assert module_0.rounded_avg(1, 2) == '0b10'
    assert module_0.rounded_avg(0, 0) == '0b0'
    assert module_0.rounded_avg(5, 1) == -1

# Generated at 2026-10-24 07:34:34.263275
# Unit test for function rounded_avg
def test_rounded_avg():
    # Normal ranges
    assert module_0.rounded_avg(1, 5) == "0b11"        # avg of 1..5 = 3
    assert module_0.rounded_avg(7, 13) == "0b1010"     # avg = 10
    assert module_0.rounded_avg(20, 33) == "0b1110"    # avg of 20..33 = 26.5 -> 26
    assert module_0.rounded_avg(-5, 5) == "0b0"        # avg = 0

    # Single-element range
    assert module_0.rounded_avg(4, 4) == "0b100"       # avg = 4

    # Invalid range
    assert module_0.rounded_avg(12, 3) == -1           # m < n

    print("All tests passed!")