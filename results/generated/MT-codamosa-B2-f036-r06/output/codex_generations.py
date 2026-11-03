

# Generated at 2026-11-02 23:17:06.725010
# Unit test for function fizz_buzz
def test_fizz_buzz():
    # Numbers < 50 divisible by 11 or 13: 0, 11, 13, 22, 26, 33, 39, 44 -> no '7' digits
    assert module_0.fizz_buzz(50) == 0

    # Adds 55, 65, 66, 77 below 78 -> '77' contributes two 7s
    assert module_0.fizz_buzz(78) == 2

    # Adds 78 below 79 -> one more '7'
    assert module_0.fizz_buzz(79) == 3

    # Edge case: empty range
    assert module_0.fizz_buzz(0) == 0
    assert module_0.fizz_buzz(11) == 0

    # Only multiples of 11 or 13 are considered
    assert module_0.fizz_buzz(100) == 3  # 77 and 78 contribute the 7s

    # Below 11, only 0 qualifies (0 % 11 == 0), no 7s
    assert module_0.fizz_buzz(1) == 0

# nonce:2cff3d7f

# Generated at 2026-11-02 23:19:44.383349
# Unit test for function fizz_buzz
def test_fizz_buzz():
    # No multiples of 11 or 13 below 50 contain the digit 7
    assert module_0.fizz_buzz(50) == 0
    
    # 77 is the first number with 7s (two of them)
    assert module_0.fizz_buzz(78) == 2
    
    # 78 is divisible by 13 and contains one more 7
    assert module_0.fizz_buzz(79) == 3
    
    # Edge case: n = 0 or n = 1 gives empty range
    assert module_0.fizz_buzz(0) == 0
    assert module_0.fizz_buzz(1) == 0
    
    # 0 is divisible by both 11 and 13, but contributes no 7s
    assert module_0.fizz_buzz(11) == 0
    assert module_0.fizz_buzz(12) == 0
    
    # Only 77 (< 100) contains 7s among multiples of 11 or 13
    assert module_0.fizz_buzz(100) == 2
    
    # Multiples of 11 or 13 below 200 containing 7s: 77, 117, 143, 154, 165, 176, 187 -> digits: 7+1+7+1+7+7 = 5... verify
    # 77 -> two 7s; 117 -> one 7; 143, 154, 165 -> none; 176 -> one 7; 187 -> one 7
    # 77 (2) + 117 (1) + 176 (1) + 187 (1) = 5
    assert module_0.fizz_buzz(200) == 5

# Generated at 2026-11-02 23:22:30.077918
# Unit test for function fizz_buzz
def test_fizz_buzz():
    # Canonical examples
    assert module_0.fizz_buzz(50) == 0
    assert module_0.fizz_buzz(78) == 2
    assert module_0.fizz_buzz(79) == 3
    assert module_0.fizz_buzz(100) == 3
    assert module_0.fizz_buzz(200) == 6

    # Larger inputs
    assert module_0.fizz_buzz(4000) == 192
    assert module_0.fizz_buzz(10000) == 639
    assert module_0.fizz_buzz(100000) == 8026

    # Edge cases: empty/negative range
    assert module_0.fizz_buzz(0) == 0
    assert module_0.fizz_buzz(1) == 0
    assert module_0.fizz_buzz(-5) == 0

    # Boundary behavior around multiples of 11 and 13
    assert module_0.fizz_buzz(11) == 0    # only 0 qualifies (< 11)
    assert module_0.fizz_buzz(13) == 0    # 13 itself is excluded
    assert module_0.fizz_buzz(14) == 0    # 13 included but has no '7' digit
    assert module_0.fizz_buzz(77) == 0    # 77 is excluded when n == 77
    assert module_0.fizz_buzz(78) == 2    # 77 -> "77" contributes two 7s
    assert module_0.fizz_buzz(79) == 3    # 78 adds one more 7
# nonce:d9de1e50

# Generated at 2026-11-02 23:24:37.913285
# Unit test for function fizz_buzz
def test_fizz_buzz():
    # Edge cases: empty/very small ranges
    assert module_0.fizz_buzz(0) == 0
    assert module_0.fizz_buzz(1) == 0
    assert module_0.fizz_buzz(-5) == 0

    # Small ranges with no 7s in collected digits
    assert module_0.fizz_buzz(12) == 0   # ns = [0, 11] -> "011"
    assert module_0.fizz_buzz(14) == 0   # ns = [0, 11, 13] -> "01113"
    assert module_0.fizz_buzz(50) == 0   # ns = [0,11,13,22,26,33,39,44] -> no '7'

    # Known values containing 7s
    assert module_0.fizz_buzz(78) == 2   # ...66, 77 -> two 7s from "77"
    assert module_0.fizz_buzz(79) == 3   # adds 78 -> one more '7'
    assert module_0.fizz_buzz(100) == 2  # includes 77 but not 78
    assert module_0.fizz_buzz(117) == 3  # includes 77 and 78

    # Result must be a non-negative int
    result = module_0.fizz_buzz(1000)
    assert isinstance(result, int)
    assert result >= 0

    # Consistency: increasing n can never decrease the count
    assert module_0.fizz_buzz(200) >= module_0.fizz_buzz(100)
    assert module_0.fizz_buzz(300) >= module_0.fizz_buzz(200)

    print("All tests passed!")


if __name__ == "__main__":
    test_fizz_buzz()

# Generated at 2026-11-02 23:26:09.105656
# Unit test for function fizz_buzz
def test_fizz_buzz():
    # No multiples of 11 or 13 below these bounds
    assert module_0.fizz_buzz(0) == 0
    assert module_0.fizz_buzz(11) == 0  # only 0 -> "0", no '7'

    # Known reference cases
    assert module_0.fizz_buzz(50) == 0  # "011132226333944" -> no '7'
    assert module_0.fizz_buzz(78) == 2  # includes 77 -> two '7's
    assert module_0.fizz_buzz(79) == 3  # includes 77 and 78 -> three '7's
    assert module_0.fizz_buzz(100) == 3  # 77 (two) + 78 (one) -> three '7's