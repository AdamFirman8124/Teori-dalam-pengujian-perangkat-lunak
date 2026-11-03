

# Generated at 2026-11-01 19:36:29.785698
# Unit test for function rounded_avg
def test_rounded_avg():
    # Valid range where average is an integer
    assert module_0.rounded_avg(1, 5) == "0b11"        # avg = 3
    assert module_0.rounded_avg(10, 20) == "0b1111"    # avg = 15
    assert module_0.rounded_avg(0, 0) == "0b0"         # avg = 0
    assert module_0.rounded_avg(5, 5) == "0b101"       # avg = 5

    # Invalid range: m < n returns -1
    assert module_0.rounded_avg(7, 5) == -1
    assert module_0.rounded_avg(10, 1) == -1

    # Range with .5 average (banker's rounding: round(26.5) -> 26)
    assert module_0.rounded_avg(20, 33) == "0b11010"   # avg = 26.5 -> 26

    # Range including negatives
    assert module_0.rounded_avg(-5, 5) == "0b0"        # avg = 0

    # Range rounding up
    assert module_0.rounded_avg(1, 2) == "0b10"        # avg = 1.5 -> 2

    print("All tests passed!")


test_rounded_avg()

# Generated at 2026-11-01 19:37:11.463125
# Unit test for function rounded_avg
def test_rounded_avg():
    # m < n returns -1
    assert module_0.rounded_avg(7, 5) == -1
    assert module_0.rounded_avg(10, 1) == -1
    assert module_0.rounded_avg(5, 4) == -1

    # Single-element ranges
    assert module_0.rounded_avg(1, 1) == "0b1"
    assert module_0.rounded_avg(0, 0) == "0b0"
    assert module_0.rounded_avg(5, 5) == "0b101"

    # Basic averages
    assert module_0.rounded_avg(1, 5) == "0b11"       # avg = 3
    assert module_0.rounded_avg(10, 20) == "0b1111"   # avg = 15
    assert module_0.rounded_avg(0, 10) == "0b101"     # avg = 5

    # Rounding behavior (banker's rounding)
    assert module_0.rounded_avg(1, 2) == "0b10"       # avg = 1.5 -> rounds to 2
    assert module_0.rounded_avg(2, 3) == "0b10"       # avg = 2.5 -> rounds to 2
    assert module_0.rounded_avg(20, 33) == "0b11010"  # avg = 26.5 -> rounds to 26

    # Larger range
    assert module_0.rounded_avg(1, 100) == "0b110010" # avg = 50.5 -> rounds to 50

    print("All tests passed!")


test_rounded_avg()

# Generated at 2026-11-01 19:37:57.026930
# Unit test for function rounded_avg
def test_rounded_avg():
    # Normal cases: average computed and converted to binary string
    assert module_0.rounded_avg(1, 5) == "0b11"          # avg = 3
    assert module_0.rounded_avg(7, 13) == "0b1010"       # avg = 10
    assert module_0.rounded_avg(10, 20) == "0b1111"      # avg = 15
    assert module_0.rounded_avg(20, 33) == "0b11010"     # avg = 26.5 -> 26
    assert module_0.rounded_avg(5, 5) == "0b101"         # single element, avg = 5

    # Invalid range: m < n returns -1
    assert module_0.rounded_avg(7, 5) == -1
    assert module_0.rounded_avg(10, 0) == -1
    assert module_0.rounded_avg(100, 1) == -1

    # Rounding behavior (Python banker's rounding)
    assert module_0.rounded_avg(0, 1) == "0b0"           # avg = 0.5 -> 0
    assert module_0.rounded_avg(1, 2) == "0b10"          # avg = 1.5 -> 2
    assert module_0.rounded_avg(2, 3) == "0b10"          # avg = 2.5 -> 2

    # Zero range starting at 0
    assert module_0.rounded_avg(0, 0) == "0b0"           # avg = 0

    print("All tests passed!")


if __name__ == "__main__":
    test_rounded_avg()

# Generated at 2026-11-01 19:38:44.449623
# Unit test for function rounded_avg
def test_rounded_avg():
    assert module_0.rounded_avg(1, 5) == "0b11"
    assert module_0.rounded_avg(7, 5) == -1
    assert module_0.rounded_avg(10, 20) == "0b1111"
    assert module_0.rounded_avg(20, 33) == "0b11010"
    assert module_0.rounded_avg(4, 5) == "0b100"
    assert module_0.rounded_avg(5, 5) == "0b101"
    assert module_0.rounded_avg(0, 0) == "0b0"
    assert module_0.rounded_avg(3, 2) == -1
    assert module_0.rounded_avg(10, 10) == "0b1010"

# Generated at 2026-11-01 19:39:33.082041
# Unit test for function rounded_avg
def test_rounded_avg():
    # Basic cases: perfect averages
    assert module_0.rounded_avg(1, 5) == "0b11"          # avg = 3 -> 0b11
    assert module_0.rounded_avg(7, 13) == "0b1010"       # avg = 10 -> 0b1010
    assert module_0.rounded_avg(10, 10) == "0b1010"      # single element: avg = 10
    assert module_0.rounded_avg(0, 0) == "0b0"           # single element: avg = 0

    # Case requiring rounding (.5 triggers banker's rounding in Python)
    assert module_0.rounded_avg(20, 33) == "0b11010"     # avg = 26.5 -> round -> 26 -> 0b11010

    # Invalid range: m < n returns -1
    assert module_0.rounded_avg(5, 4) == -1
    assert module_0.rounded_avg(-3, -5) == -1

    # Negative ranges
    assert module_0.rounded_avg(-5, -5) == "-0b101"      # avg = -5
    assert module_0.rounded_avg(-3, 3) == "0b0"          # avg = 0
    assert module_0.rounded_avg(-2, 1) == "0b0"          # avg = (-2 + -1 + 0 + 1)/4 = -0.5 -> 0