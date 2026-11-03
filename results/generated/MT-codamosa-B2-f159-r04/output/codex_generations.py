

# Generated at 2026-11-02 15:31:32.491040
# Unit test for function eat
def test_eat():
    # Case where need <= remaining: eats all needed carrots
    assert module_0.eat(5, 6, 10) == [11, 4]
    # Case where need <= remaining: eats all needed carrots
    assert module_0.eat(4, 8, 9) == [12, 1]
    # Case where need == remaining: eats exactly all remaining
    assert module_0.eat(1, 10, 10) == [11, 0]
    # Case where need > remaining: eats only remaining carrots
    assert module_0.eat(2, 11, 5) == [7, 0]
    # Case where remaining is 0: eats nothing more
    assert module_0.eat(10, 5, 0) == [10, 0]
    # Case where need is 0: eats nothing
    assert module_0.eat(100, 0, 50) == [100, 50]
    # Zero eaten previously, plenty remaining
    assert module_0.eat(0, 3, 7) == [3, 4]
    print("All tests passed!")


if __name__ == "__main__":
    test_eat()

# Generated at 2026-11-02 15:32:33.188139
# Unit test for function eat
def test_eat():
# nonce:3cbce157
    # Case 1: need less than remaining (plenty of food)
    assert module_0.eat(5, 3, 10) == [8, 7]
    # Case 2: need greater than remaining (not enough food)
    assert module_0.eat(5, 10, 3) == [8, 0]
    # Case 3: need exactly equals remaining
    assert module_0.eat(5, 7, 7) == [12, 0]
    # Case 4: no need to eat
    assert module_0.eat(5, 0, 10) == [5, 10]
    # Case 5: no remaining food
    assert module_0.eat(5, 10, 0) == [5, 0]
    # Case 6: zero everything
    assert module_0.eat(0, 0, 0) == [0, 0]
    # Case 7: need less than remaining, larger numbers
    assert module_0.eat(100, 50, 200) == [150, 150]
    # Case 8: need greater than remaining, larger numbers
    assert module_0.eat(100, 250, 200) == [300, 0]
    print("All tests passed!")

if __name__ == "__main__":
    test_eat()

# Generated at 2026-11-02 15:34:03.435420
# Unit test for function eat
def test_eat():
    # Case where need <= remaining
    assert module_0.eat(5, 6, 10) == [11, 4]
    assert module_0.eat(2, 3, 10) == [5, 7]
    
    # Case where need > remaining
    assert module_0.eat(4, 8, 9) == [13, 0]
    assert module_0.eat(2, 11, 5) == [7, 0]
    
    # Edge case: need equals remaining
    assert module_0.eat(1, 10, 10) == [11, 0]
    assert module_0.eat(0, 5, 5) == [5, 0]
    
    # Edge case: need is zero
    assert module_0.eat(3, 0, 5) == [3, 5]
    
    # Edge case: remaining is zero
    assert module_0.eat(7, 3, 0) == [7, 0]
    
    # Edge case: all zeros
    assert module_0.eat(0, 0, 0) == [0, 0]

test_eat()

# Generated at 2026-11-02 15:35:08.820479
# Unit test for function eat
def test_eat():
    # Test case where need is less than remaining
    assert module_0.eat(5, 3, 10) == [8, 7]
    
    # Test case where need is less than remaining
    assert module_0.eat(10, 5, 15) == [15, 10]
    
    # Test case where need is equal to remaining
    assert module_0.eat(5, 10, 10) == [15, 0]
    
    # Test case where need is greater than remaining
    assert module_0.eat(5, 15, 10) == [15, 0]
    
    # Test case where remaining is 0
    assert module_0.eat(5, 3, 0) == [5, 0]
    
    # Test case where need is 0
    assert module_0.eat(5, 0, 10) == [5, 10]
    
    # Test case where both need and remaining are 0
    assert module_0.eat(5, 0, 0) == [5, 0]
    
    # Test case with larger numbers
    assert module_0.eat(100, 50, 200) == [150, 150]
    
    # Test case where need exactly consumes remaining
    assert module_0.eat(0, 7, 7) == [7, 0]
    
    print("All tests passed!")

# Run the tests
test_eat()

# Generated at 2026-11-02 15:36:02.158233
# Unit test for function eat
def test_eat():
    # Case: need is less than remaining
    assert module_0.eat(5, 3, 10) == [8, 7]
    # Case: need is exactly equal to remaining
    assert module_0.eat(5, 10, 10) == [15, 0]
    # Case: need is greater than remaining
    assert module_0.eat(5, 15, 10) == [15, 0]
    # Case: remaining is zero
    assert module_0.eat(5, 3, 0) == [5, 0]
    # Case: need is zero
    assert module_0.eat(5, 0, 10) == [5, 10]
    # Case: all zeros
    assert module_0.eat(0, 0, 0) == [0, 0]
    # Case: large numbers
    assert module_0.eat(1000, 500, 2000) == [1500, 1500]
    assert module_0.eat(1000, 3000, 2000) == [3000, 0]
    print("All tests passed!")

if __name__ == "__main__":
    test_eat()