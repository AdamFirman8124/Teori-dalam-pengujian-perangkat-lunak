

# Generated at 2026-11-02 13:00:55.321688
# Unit test for function eat
def test_eat():
# nonce:01bd2cb9
    # Case where need is less than remaining
    assert module_0.eat(5, 3, 10) == [8, 7]
    
    # Case where need is greater than remaining
    assert module_0.eat(5, 12, 10) == [15, 0]
    
    # Case where need equals remaining
    assert module_0.eat(4, 5, 5) == [9, 0]
    
    # Case with zero need
    assert module_0.eat(10, 0, 5) == [10, 5]
    
    # Case with zero remaining
    assert module_0.eat(10, 5, 0) == [10, 0]
    
    # Case with all zeros
    assert module_0.eat(0, 0, 0) == [0, 0]
    
    # Case with large numbers
    assert module_0.eat(1000, 500, 2000) == [1500, 1500]
    assert module_0.eat(1000, 3000, 2000) == [3000, 0]
    
    print("All tests passed!")

test_eat()

# Generated at 2026-11-02 13:02:36.862127
# Unit test for function eat
def test_eat():
    # Enough remaining carrots: eats exactly what it needs
    assert module_0.eat(5, 6, 10) == [11, 4]
    assert module_0.eat(4, 8, 9) == [12, 1]
    assert module_0.eat(1, 10, 10) == [11, 0]

    # Not enough remaining carrots: eats all remaining
    assert module_0.eat(2, 11, 5) == [7, 0]
    assert module_0.eat(10, 20, 3) == [13, 0]

    # Edge cases
    assert module_0.eat(0, 5, 5) == [5, 0]          # need equals remaining
    assert module_0.eat(3, 0, 5) == [3, 5]          # no need to eat
    assert module_0.eat(7, 5, 0) == [7, 0]          # no carrots left
    assert module_0.eat(0, 0, 0) == [0, 0]          # all zeros
    assert module_0.eat(100, 50, 60) == [150, 10]   # larger numbers

# Generated at 2026-11-02 13:05:48.098836
# Unit test for function eat
def test_eat():
    # Test when need is less than remaining
    assert module_0.eat(5, 3, 10) == [8, 7], "Expected [8, 7]"
    # Test when need equals remaining
    assert module_0.eat(5, 10, 10) == [15, 0], "Expected [15, 0]"
    # Test when need is greater than remaining
    assert module_0.eat(5, 15, 10) == [15, 0], "Expected [15, 0]"
    # Test with zero need
    assert module_0.eat(5, 0, 10) == [5, 10], "Expected [5, 10]"
    # Test with zero remaining
    assert module_0.eat(5, 3, 0) == [5, 0], "Expected [5, 0]"
    # Test with all zeros
    assert module_0.eat(0, 0, 0) == [0, 0], "Expected [0, 0]"
    # Test typical cases
    assert module_0.eat(2, 5, 12) == [7, 7], "Expected [7, 7]"
    assert module_0.eat(4, 8, 9) == [12, 1], "Expected [12, 1]"
    assert module_0.eat(1, 10, 5) == [6, 0], "Expected [6, 0]"
    assert module_0.eat(10, 5, 5) == [15, 0], "Expected [15, 0]"
    # Test large numbers
    assert module_0.eat(1000, 500, 2000) == [1500, 1500], "Expected [1500, 1500]"
    assert module_0.eat(1000, 2000, 1500) == [2500, 0], "Expected [2500, 0]"
    print("All tests passed!")

test_eat()

# Generated at 2026-11-02 13:07:59.791605
# Unit test for function eat
def test_eat():
    # Case where need <= remaining
    assert module_0.eat(5, 6, 10) == [11, 4]
    assert module_0.eat(2, 3, 7) == [5, 4]
    # Case where need == remaining
    assert module_0.eat(2, 3, 3) == [5, 0]
    assert module_0.eat(4, 4, 4) == [8, 0]
    # Case where need > remaining
    assert module_0.eat(1, 10, 5) == [6, 0]
    assert module_0.eat(3, 8, 2) == [5, 0]
    # Edge cases with zeros
    assert module_0.eat(0, 0, 0) == [0, 0]
    assert module_0.eat(0, 0, 10) == [0, 10]
    assert module_0.eat(10, 5, 0) == [10, 0]
    print("All tests passed!")

test_eat()

# Generated at 2026-11-02 13:09:43.528738
# Unit test for function eat
def test_eat():
    # need <= remaining: eat exactly `need`, subtract from remaining
    assert module_0.eat(5, 6, 10) == [11, 4]
    assert module_0.eat(4, 8, 9) == [12, 1]
    assert module_0.eat(1, 10, 10) == [11, 0]
    
    # need > remaining: eat all remaining, leave 0
    assert module_0.eat(2, 11, 5) == [7, 0]
    assert module_0.eat(10, 3, 2) == [12, 0]
    
    # edge cases
    assert module_0.eat(0, 0, 0) == [0, 0]
    assert module_0.eat(7, 7, 7) == [14, 0]
    assert module_0.eat(0, 5, 100) == [5, 95]