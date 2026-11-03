

# Generated at 2026-11-02 21:41:05.018174
# Unit test for function rounded_avg
def test_rounded_avg():
    # Basic cases: average of range returned as binary string
    assert module_0.rounded_avg(1, 5) == "0b11"          # avg = 3
    assert module_0.rounded_avg(7, 13) == "0b1010"       # avg = 10
    assert module_0.rounded_avg(1, 1) == "0b1"           # single element -> itself
    assert module_0.rounded_avg(10, 20) == "0b1111"      # avg = 15

    # Rounding behavior
    assert module_0.rounded_avg(20, 33) == "0b11010"     # avg = 26.5 -> rounds to 26
    assert module_0.rounded_avg(4, 52) == "0b11100"      # avg = 28

    # Larger ranges
    assert module_0.rounded_avg(964, 977) == "0b1111001010"
    assert module_0.rounded_avg(996, 998) == "0b1111110010"
    assert module_0.rounded_avg(185, 546) == "0b101101101"
    assert module_0.rounded_avg(55, 955) == "0b101111111"

    # Invalid ranges: m < n returns -1
    assert module_0.rounded_avg(7, 5) == -1
    assert module_0.rounded_avg(10, 2) == -1
    assert module_0.rounded_avg(660, 419) == -1

    # Return type checks
    result = module_0.rounded_avg(1, 5)
    assert isinstance(result, str) and result.startswith("0b")
    assert module_0.rounded_avg(5, 3) == -1

    print("All tests passed!")


if __name__ == "__main__":
    test_rounded_avg()

# Generated at 2026-11-02 21:42:08.942089
# Unit test for function rounded_avg
def test_rounded_avg():
    # Test when m < n, should return -1
    assert module_0.rounded_avg(7, 5) == -1
    assert module_0.rounded_avg(10, 0) == -1
    assert module_0.rounded_avg(100, 99) == -1

    # Test single element range
    assert module_0.rounded_avg(5, 5) == "0b101"
    assert module_0.rounded_avg(0, 0) == "0b0"
    assert module_0.rounded_avg(7, 7) == "0b111"

    # Test normal ranges
    assert module_0.rounded_avg(1, 5) == "0b11"       # avg 3
    assert module_0.rounded_avg(10, 20) == "0b1111"   # avg 15
    assert module_0.rounded_avg(20, 33) == "0b11010"  # avg 26.5 rounds to 26 (banker's rounding)
    assert module_0.rounded_avg(2, 3) == "0b10"       # avg 2.5 rounds to 2 (banker's rounding)

    # Test range starting from 0
    assert module_0.rounded_avg(0, 4) == "0b10"       # avg 2

    # Test larger range
    assert module_0.rounded_avg(1, 100) == "0b110010" # avg 50.5 rounds to 50

# Run the test
test_rounded_avg()
print("All tests passed!")

# Generated at 2026-11-02 21:43:27.830676
# Unit test for function rounded_avg
def test_rounded_avg():
    # Basic case: average of 1..5 is 3 -> binary "0b11"
    assert module_0.rounded_avg(1, 5) == "0b11"

    # m < n should return -1
    assert module_0.rounded_avg(7, 5) == -1
    assert module_0.rounded_avg(10, 1) == -1

    # Average of 10..20 is 15 -> "0b1111"
    assert module_0.rounded_avg(10, 20) == "0b1111"

    # Average of 20..33 is 26.5 -> Python banker's rounding gives 26 -> "0b11010"
    assert module_0.rounded_avg(20, 33) == "0b11010"

    # Single-element range: average is the element itself
    assert module_0.rounded_avg(5, 5) == "0b101"
    assert module_0.rounded_avg(0, 0) == "0b0"

    # Zero included range: average of 0..1 is 0.5 -> rounds to 0 -> "0b0"
    assert module_0.rounded_avg(0, 1) == "0b0"

    # Negative numbers: average of -3..1 is -1 -> bin(-1) = "-0b1"
    assert module_0.rounded_avg(-3, 1) == "-0b1"

    # Negative range where m < n
    assert module_0.rounded_avg(-1, -5) == -1

    print("All tests passed!")

test_rounded_avg()

# Generated at 2026-11-02 21:45:37.185670
# Unit test for function rounded_avg
def test_rounded_avg():
    # Test when m < n, should return -1
    assert module_0.rounded_avg(7, 5) == -1
    assert module_0.rounded_avg(10, 1) == -1

    # Test basic averaging
    assert module_0.rounded_avg(1, 5) == "0b11"        # avg of 1..5 = 3
    assert module_0.rounded_avg(5, 5) == "0b101"       # single element, avg = 5
    assert module_0.rounded_avg(10, 20) == "0b1111"    # avg of 10..20 = 15

    # Test rounding behavior (banker's rounding)
    assert module_0.rounded_avg(20, 33) == "0b11010"   # avg = 26.5 -> 26
    assert module_0.rounded_avg(1, 2) == "0b10"        # avg = 1.5 -> 2
    assert module_0.rounded_avg(0, 1) == "0b0"         # avg = 0.5 -> 0

    # Test return type is a string for valid ranges
    assert isinstance(module_0.rounded_avg(1, 5), str)

    # Test zero included in range
    assert module_0.rounded_avg(-3, 3) == "0b0"        # avg of -3..3 = 0

    print("All tests passed!")


test_rounded_avg()

# Generated at 2026-11-02 21:47:22.653090
# Unit test for function rounded_avg
def test_rounded_avg():
    # m < n should return -1
    assert module_0.rounded_avg(7, 5) == -1
    assert module_0.rounded_avg(10, 1) == -1
    assert module_0.rounded_avg(5, 4) == -1

    # Single element range
    assert module_0.rounded_avg(5, 5) == "0b101"
    assert module_0.rounded_avg(0, 0) == "0b0"
    assert module_0.rounded_avg(1, 1) == "0b1"

    # Basic averages
    assert module_0.rounded_avg(1, 5) == "0b11"        # avg of 1..5 = 3
    assert module_0.rounded_avg(10, 20) == "0b1111"    # avg of 10..20 = 15

    # Rounding behavior (banker's rounding: 26.5 -> 26)
    assert module_0.rounded_avg(20, 33) == "0b11010"   # avg = 26.5 -> 26
    assert module_0.rounded_avg(1, 2) == "0b1"         # avg = 1.5 -> 2? No: round(1.5)=2
    # Note: round(1.5) == 2 in Python (banker's rounding rounds to even)
    # so recompute: bin(2) == "0b10"
    assert module_0.rounded_avg(1, 2) == "0b10"

    # Negative numbers
    assert module_0.rounded_avg(-5, -1) == "0b-11"     # avg = -3

    print("All tests passed!")


if __name__ == "__main__":
    test_rounded_avg()