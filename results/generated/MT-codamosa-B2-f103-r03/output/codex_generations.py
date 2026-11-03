

# Generated at 2026-11-02 23:56:14.337794
# Unit test for function rounded_avg
def test_rounded_avg():
# nonce:4f85ed26
    # Basic case: average of 1..5 is 3 -> 0b11
    assert module_0.rounded_avg(1, 5) == "0b11"
    # m < n returns -1
    assert module_0.rounded_avg(7, 5) == -1
    # Average of 10..20 is 15 -> 0b1111
    assert module_0.rounded_avg(10, 20) == "0b1111"
    # Average of 20..33 is 26.5, rounds to 26 (banker's rounding) -> 0b11010
    assert module_0.rounded_avg(20, 33) == "0b11010"
    # Single-element range
    assert module_0.rounded_avg(5, 5) == "0b101"
    assert module_0.rounded_avg(0, 0) == "0b0"
    # Negative numbers
    assert module_0.rounded_avg(-10, -10) == "-0b1010"
    # Average of -5..5 is 0 -> 0b0
    assert module_0.rounded_avg(-5, 5) == "0b0"
    # Rounding down case: average of 1..2 is 1.5, rounds to 2 (banker's) -> 0b10
    assert module_0.rounded_avg(1, 2) == "0b10"
    # Larger range: average of 0..10 is 5 -> 0b101
    assert module_0.rounded_avg(0, 10) == "0b101"

# Generated at 2026-11-02 23:57:04.403155
# Unit test for function rounded_avg
def test_rounded_avg():
    # Valid range: average of 1..5 is 3 -> binary "0b11"
    assert module_0.rounded_avg(1, 5) == "0b11"
    # m < n returns -1
    assert module_0.rounded_avg(7, 5) == -1
    assert module_0.rounded_avg(10, 5) == -1
    # Average of 10..20 is 15 -> binary "0b1111"
    assert module_0.rounded_avg(10, 20) == "0b1111"
    # Average of 20..33 is 26.5 -> round() gives 26 -> "0b11010"
    assert module_0.rounded_avg(20, 33) == "0b11010"
    # Single-element range
    assert module_0.rounded_avg(5, 5) == "0b101"
    assert module_0.rounded_avg(0, 0) == "0b0"
    # Negative numbers: average of -3..1 is -1 -> "-0b1"
    assert module_0.rounded_avg(-3, 1) == "-0b1"
    # Average of 0..7 is 3.5 -> round() gives 4 -> "0b100"
    assert module_0.rounded_avg(0, 7) == "0b100"
    print("All tests passed!")

test_rounded_avg()
# nonce:49812c89

# Generated at 2026-11-02 23:58:37.576259
# Unit test for function rounded_avg
def test_rounded_avg():
    # nonce:8d002332
    # Normal cases: average is an integer
    assert module_0.rounded_avg(1, 5) == "0b11"          # avg 3
    assert module_0.rounded_avg(10, 20) == "0b1111"      # avg 15
    assert module_0.rounded_avg(0, 0) == "0b0"           # avg 0
    assert module_0.rounded_avg(5, 5) == "0b101"         # avg 5

    # Cases exercising banker's rounding (round half to even)
    assert module_0.rounded_avg(1, 2) == "0b10"          # avg 1.5 -> 2
    assert module_0.rounded_avg(2, 3) == "0b10"          # avg 2.5 -> 2
    assert module_0.rounded_avg(20, 33) == "0b11010"     # avg 26.5 -> 26

    # Negative range
    assert module_0.rounded_avg(-10, -5) == "-0b1000"    # avg -7.5 -> -8

    # Invalid ranges: m < n returns -1
    assert module_0.rounded_avg(7, 5) == -1
    assert module_0.rounded_avg(-5, -10) == -1

    print("All tests passed!")


test_rounded_avg()

# Generated at 2026-11-02 23:59:51.724468
# Unit test for function rounded_avg
def test_rounded_avg():
    # Valid range cases
    assert module_0.rounded_avg(1, 5) == "0b11"        # avg = 3
    assert module_0.rounded_avg(7, 13) == "0b1010"     # avg = 10
    assert module_0.rounded_avg(10, 20) == "0b1111"    # avg = 15
    assert module_0.rounded_avg(20, 33) == "0b11010"   # avg = 26.5 -> 26 (banker's rounding)
    assert module_0.rounded_avg(5, 5) == "0b101"       # single element, avg = 5
    assert module_0.rounded_avg(0, 0) == "0b0"         # single element, avg = 0
    assert module_0.rounded_avg(2, 3) == "0b10"        # avg = 2.5 -> 2 (banker's rounding)
    assert module_0.rounded_avg(1, 2) == "0b10"        # avg = 1.5 -> 2 (rounds to even)
    assert module_0.rounded_avg(-3, 3) == "0b0"        # negative range, avg = 0
    assert module_0.rounded_avg(-10, -5) == "0b1000"   # avg = -7.5 -> -8 -> "0b-1000"? no: bin(-8) = '-0b1000'

    # Invalid range case
    assert module_0.rounded_avg(7, 5) == -1            # m < n
    assert module_0.rounded_avg(5, 4) == -1            # m < n
    assert module_0.rounded_avg(0, -1) == -1           # m < n

    print("All tests passed!")

if __name__ == "__main__":
    test_rounded_avg()

# Generated at 2026-11-03 00:02:21.944114
# Unit test for function rounded_avg
def test_rounded_avg():
    # Normal cases: average rounds down
    assert module_0.rounded_avg(1, 5) == "0b11"          # avg = 3
    assert module_0.rounded_avg(10, 20) == "0b1111"      # avg = 15
    assert module_0.rounded_avg(12, 12) == "0b1100"      # single element
    assert module_0.rounded_avg(5, 5) == "0b101"

    # m < n returns -1
    assert module_0.rounded_avg(7, 5) == -1
    assert module_0.rounded_avg(100, 0) == -1

    # Banker's rounding (round half to even)
    assert module_0.rounded_avg(20, 33) == "0b11010"     # avg = 26.5 -> 26
    assert module_0.rounded_avg(3, 4) == "0b100"         # avg = 3.5 -> 4

    # Zero and negative ranges
    assert module_0.rounded_avg(0, 0) == "0b0"
    assert module_0.rounded_avg(-5, -1) == "-0b11"       # avg = -3
    assert module_0.rounded_avg(-2, 2) == "0b0"          # avg = 0

    print("All test cases passed!")

test_rounded_avg()