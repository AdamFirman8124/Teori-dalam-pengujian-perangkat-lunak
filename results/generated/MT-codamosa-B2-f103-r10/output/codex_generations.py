

# Generated at 2026-11-02 17:41:42.700583
# Unit test for function rounded_avg
def test_rounded_avg():
    # Valid range cases
    assert module_0.rounded_avg(1, 5) == "0b11"          # avg=3 -> 0b11
    assert module_0.rounded_avg(10, 20) == "0b1111"      # avg=15 -> 0b1111
    assert module_0.rounded_avg(20, 33) == "0b11010"     # avg=26.5 rounds to 26 -> 0b11010
    assert module_0.rounded_avg(5, 5) == "0b101"         # single element, avg=5
    assert module_0.rounded_avg(0, 0) == "0b0"           # single element, avg=0
    assert module_0.rounded_avg(1, 3) == "0b10"          # avg=2 -> 0b10
    assert module_0.rounded_avg(10, 10) == "0b1010"      # single element, avg=10
    # Invalid range: m < n returns -1
    assert module_0.rounded_avg(7, 5) == -1
    assert module_0.rounded_avg(3, 2) == -1
    assert module_0.rounded_avg(100, 0) == -1
    print("All tests passed!")

if __name__ == "__main__":
    test_rounded_avg()

# Generated at 2026-11-02 17:43:35.244345
# Unit test for function rounded_avg
def test_rounded_avg():
    assert module_0.rounded_avg(1, 5) == "0b11"
    assert module_0.rounded_avg(7, 13) == "0b1010"
    assert module_0.rounded_avg(10, 20) == "0b1111"
    assert module_0.rounded_avg(20, 33) == "0b11010"
    assert module_0.rounded_avg(7, 5) == -1
    assert module_0.rounded_avg(5, 5) == "0b101"
    assert module_0.rounded_avg(0, 0) == "0b0"
    assert module_0.rounded_avg(100, 1) == -1
    print("All test cases passed!")

test_rounded_avg()

# Generated at 2026-11-02 17:48:08.886510
# Unit test for function rounded_avg
def test_rounded_avg():
    assert module_0.rounded_avg(1, 5) == "0b11"
    assert module_0.rounded_avg(7, 13) == "0b1010"
    assert module_0.rounded_avg(17, 5) == -1
    assert module_0.rounded_avg(7, 5) == -1
    assert module_0.rounded_avg(10, 20) == "0b1111"
    assert module_0.rounded_avg(20, 33) == "0b11010"
    assert module_0.rounded_avg(0, 33) == "0b10000"
    assert module_0.rounded_avg(3, 39) == "0b10101"
    assert module_0.rounded_avg(30, 39) == "0b100010"
    assert module_0.rounded_avg(10, 49) == "0b11110"
    assert module_0.rounded_avg(5, 5) == "0b101"
    assert module_0.rounded_avg(0, 0) == "0b0"

# Generated at 2026-11-02 17:49:32.884572
# Unit test for function rounded_avg
def test_rounded_avg():
    # Test when m < n, should return -1
    assert module_0.rounded_avg(7, 5) == -1
    assert module_0.rounded_avg(10, 1) == -1
    assert module_0.rounded_avg(100, 50) == -1

    # Test normal cases
    assert module_0.rounded_avg(1, 5) == "0b11"       # avg = 3
    assert module_0.rounded_avg(7, 13) == "0b1010"    # avg = 10
    assert module_0.rounded_avg(10, 20) == "0b1111"   # avg = 15
    assert module_0.rounded_avg(20, 33) == "0b11010"  # avg = 26.5 -> rounds to 26

    # Test single-element ranges
    assert module_0.rounded_avg(0, 0) == "0b0"        # avg = 0
    assert module_0.rounded_avg(1, 1) == "0b1"        # avg = 1
    assert module_0.rounded_avg(5, 5) == "0b101"      # avg = 5

    # Test rounding up case
    assert module_0.rounded_avg(1, 2) == "0b10"       # avg = 1.5 -> rounds to 2

    print("All tests passed!")


# Run the test
test_rounded_avg()