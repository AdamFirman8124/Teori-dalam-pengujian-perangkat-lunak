

# Generated at 2026-11-03 03:49:36.223185
# Unit test for function rounded_avg
def test_rounded_avg():
# nonce:01db82fe
    # Invalid range: m < n returns -1
    assert module_0.rounded_avg(7, 5) == -1
    assert module_0.rounded_avg(10, 0) == -1
    assert module_0.rounded_avg(5, 4) == -1
    assert isinstance(module_0.rounded_avg(7, 5), int)

    # Single-element ranges
    assert module_0.rounded_avg(5, 5) == "0b101"
    assert module_0.rounded_avg(0, 0) == "0b0"
    assert module_0.rounded_avg(-3, -3) == "-0b11"

    # Standard ranges
    assert module_0.rounded_avg(1, 5) == "0b11"        # avg = 3
    assert module_0.rounded_avg(10, 20) == "0b1111"    # avg = 15
    assert module_0.rounded_avg(7, 13) == "0b1010"     # avg = 10
    assert module_0.rounded_avg(20, 33) == "0b11010"   # avg = 26.5 -> 26 (round half to even)

    # Rounding behavior (Python banker's rounding)
    assert module_0.rounded_avg(1, 2) == "0b10"        # 1.5 -> 2
    assert module_0.rounded_avg(2, 3) == "0b10"        # 2.5 -> 2
    assert module_0.rounded_avg(3, 4) == "0b100"       # 3.5 -> 4
    assert module_0.rounded_avg(0, 1) == "0b0"         # 0.5 -> 0

    # Ranges including negative numbers
    assert module_0.rounded_avg(-2, 2) == "0b0"        # avg = 0
    assert module_0.rounded_avg(-5, -1) == "-0b11"     # avg = -3

# Generated at 2026-11-03 03:51:24.767082
# Unit test for function rounded_avg
def test_rounded_avg():
    # Test case where m < n should return -1
    assert module_0.rounded_avg(7, 5) == -1
    assert module_0.rounded_avg(10, 1) == -1
    assert module_0.rounded_avg(0, -5) == -1

    # Test normal cases
    assert module_0.rounded_avg(1, 5) == "0b11"        # avg = 15/5 = 3
    assert module_0.rounded_avg(10, 20) == "0b1111"    # avg = 165/11 = 15
    assert module_0.rounded_avg(20, 33) == "0b11010"   # avg = 371/14 = 26.5 -> 26 (banker's rounding)

    # Test single-element range
    assert module_0.rounded_avg(1, 1) == "0b1"
    assert module_0.rounded_avg(0, 0) == "0b0"
    assert module_0.rounded_avg(5, 5) == "0b101"

    # Test rounding behavior (Python banker's rounding to even)
    assert module_0.rounded_avg(1, 2) == "0b10"        # avg = 1.5 -> 2
    assert module_0.rounded_avg(2, 3) == "0b10"        # avg = 2.5 -> 2
    assert module_0.rounded_avg(0, 1) == "0b0"         # avg = 0.5 -> 0
    assert module_0.rounded_avg(0, 2) == "0b1"         # avg = 1.0 -> 1

    # Test range including zero
    assert module_0.rounded_avg(-2, 2) == "0b0"        # avg = 0

    # Test all-negative range
    assert module_0.rounded_avg(-5, -1) == "-0b11"     # avg = -15/5 = -3

    print("All test cases passed!")


test_rounded_avg()

# Generated at 2026-11-03 03:55:20.033311
# Unit test for function rounded_avg
def test_rounded_avg():
    # m < n should return -1
    assert module_0.rounded_avg(7, 5) == -1
    assert module_0.rounded_avg(10, 1) == -1

    # n == m: average is n itself
    assert module_0.rounded_avg(6, 6) == bin(6)          # '0b110'
    assert module_0.rounded_avg(0, 0) == '0b0'

    # Simple ranges
    assert module_0.rounded_avg(1, 5) == '0b11'          # avg = 3
    assert module_0.rounded_avg(10, 20) == '0b1111'      # avg = 15

    # Range with .5 average (banker's rounding: 26.5 -> 26)
    assert module_0.rounded_avg(20, 33) == '0b11010'

    # Negative numbers
    assert module_0.rounded_avg(-5, 5) == '0b0'          # avg = 0
    assert module_0.rounded_avg(-10, -5) == '-0b1000'    # avg = -7.5 -> -8 -> bin(-8)

    # Larger range
    assert module_0.rounded_avg(1, 100) == '0b110010'    # avg = 50.5 -> 50

# Generated at 2026-11-03 03:56:40.367157
# Unit test for function rounded_avg
def test_rounded_avg():
    assert module_0.rounded_avg(1, 5) == "0b11"          # avg 3 -> 0b11
    assert module_0.rounded_avg(7, 5) == -1              # m < n -> -1
    assert module_0.rounded_avg(10, 20) == "0b1111"      # avg 15 -> 0b1111
    assert module_0.rounded_avg(20, 33) == "0b11010"     # avg 26.5 -> rounds to 26 -> 0b11010
    assert module_0.rounded_avg(5, 5) == "0b101"         # single element -> 5
    assert module_0.rounded_avg(0, 0) == "0b0"           # single element -> 0
    assert module_0.rounded_avg(3, 4) == "0b100"         # avg 3.5 -> rounds to 4 -> 0b100
    assert module_0.rounded_avg(2, 3) == "0b10"          # avg 2.5 -> rounds to 2 -> 0b10
    assert module_0.rounded_avg(-5, -1) == "-0b11"       # avg -3 -> -0b11
    assert module_0.rounded_avg(0, 1) == "0b0"           # avg 0.5 -> rounds to 0