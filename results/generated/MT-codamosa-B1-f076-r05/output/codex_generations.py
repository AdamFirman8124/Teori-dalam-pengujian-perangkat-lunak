

# Generated at 2026-10-25 10:46:26.671266
# Unit test for function is_simple_power
def test_is_simple_power():
    # n == 1 branch
    assert module_0.is_simple_power(1, 1) == True      # x is 1, n is 1
    assert module_0.is_simple_power(2, 1) == False     # x != 1, n is 1
    
    # exact powers
    assert module_0.is_simple_power(8, 2) == True      # 2^3 = 8
    assert module_0.is_simple_power(9, 3) == True      # 3^2 = 9
    assert module_0.is_simple_power(27, 3) == True     # 3^3 = 27
    assert module_0.is_simple_power(16, 4) == True     # 4^2 = 16
    assert module_0.is_simple_power(1, 5) == True      # n^0 = 1
    
    # non-powers
    assert module_0.is_simple_power(3, 2) == False     # 3 is not a power of 2
    assert module_0.is_simple_power(5, 3) == False     # 5 is not a power of 3
    assert module_0.is_simple_power(10, 2) == False    # 10 is not a power of 2
    
    # x == n (first power)
    assert module_0.is_simple_power(2, 2) == True
    assert module_0.is_simple_power(7, 7) == True
    
    # loop-exit edge: power overshoots x
    assert module_0.is_simple_power(6, 2) == False     # 4 < 6, 8 > 6
    
    print("All tests passed!")

test_is_simple_power()

# Generated at 2026-10-25 10:46:28.190992
# Unit test for function is_simple_power
def test_is_simple_power():
    # n == 1 branch
    assert module_0.is_simple_power(1, 1) == True      # x is 1, n is 1
    assert module_0.is_simple_power(2, 1) == False     # x != 1, n is 1
    
    # exact powers
    assert module_0.is_simple_power(8, 2) == True      # 2^3 = 8
    assert module_0.is_simple_power(9, 3) == True      # 3^2 = 9
    assert module_0.is_simple_power(27, 3) == True     # 3^3 = 27
    assert module_0.is_simple_power(16, 4) == True     # 4^2 = 16
    assert module_0.is_simple_power(1, 5) == True      # n^0 = 1
    
    # non-powers
    assert module_0.is_simple_power(3, 2) == False     # 3 is not a power of 2
    assert module_0.is_simple_power(5, 3) == False     # 5 is not a power of 3
    assert module_0.is_simple_power(10, 2) == False    # 10 is not a power of 2
    
    # x == n (first power)
    assert module_0.is_simple_power(2, 2) == True
    assert module_0.is_simple_power(7, 7) == True
    
    # loop-exit edge: power overshoots x
    assert module_0.is_simple_power(6, 2) == False     # 4 < 6, 8 > 6
    
    print("All tests passed!")

test_is_simple_power()

# Generated at 2026-10-25 10:46:29.632245
# Unit test for function is_simple_power
def test_is_simple_power():
    # n == 1 branch
    assert module_0.is_simple_power(1, 1) == True      # x is 1, n is 1
    assert module_0.is_simple_power(2, 1) == False     # x != 1, n is 1
    
    # exact powers
    assert module_0.is_simple_power(8, 2) == True      # 2^3 = 8
    assert module_0.is_simple_power(9, 3) == True      # 3^2 = 9
    assert module_0.is_simple_power(27, 3) == True     # 3^3 = 27
    assert module_0.is_simple_power(16, 4) == True     # 4^2 = 16
    assert module_0.is_simple_power(1, 5) == True      # n^0 = 1
    
    # non-powers
    assert module_0.is_simple_power(3, 2) == False     # 3 is not a power of 2
    assert module_0.is_simple_power(5, 3) == False     # 5 is not a power of 3
    assert module_0.is_simple_power(10, 2) == False    # 10 is not a power of 2
    
    # x == n (first power)
    assert module_0.is_simple_power(2, 2) == True
    assert module_0.is_simple_power(7, 7) == True
    
    # loop-exit edge: power overshoots x
    assert module_0.is_simple_power(6, 2) == False     # 4 < 6, 8 > 6
    
    print("All tests passed!")

test_is_simple_power()

# Generated at 2026-10-25 10:46:31.168663
# Unit test for function is_simple_power
def test_is_simple_power():
    # n == 1 branch
    assert module_0.is_simple_power(1, 1) == True      # x is 1, n is 1
    assert module_0.is_simple_power(2, 1) == False     # x != 1, n is 1
    
    # exact powers
    assert module_0.is_simple_power(8, 2) == True      # 2^3 = 8
    assert module_0.is_simple_power(9, 3) == True      # 3^2 = 9
    assert module_0.is_simple_power(27, 3) == True     # 3^3 = 27
    assert module_0.is_simple_power(16, 4) == True     # 4^2 = 16
    assert module_0.is_simple_power(1, 5) == True      # n^0 = 1
    
    # non-powers
    assert module_0.is_simple_power(3, 2) == False     # 3 is not a power of 2
    assert module_0.is_simple_power(5, 3) == False     # 5 is not a power of 3
    assert module_0.is_simple_power(10, 2) == False    # 10 is not a power of 2
    
    # x == n (first power)
    assert module_0.is_simple_power(2, 2) == True
    assert module_0.is_simple_power(7, 7) == True
    
    # loop-exit edge: power overshoots x
    assert module_0.is_simple_power(6, 2) == False     # 4 < 6, 8 > 6
    
    print("All tests passed!")

test_is_simple_power()

# Generated at 2026-10-25 10:46:39.257964
# Unit test for function is_simple_power
def test_is_simple_power():
    # n == 1 branch
    assert module_0.is_simple_power(1, 1) == True      # x is 1, n is 1
    assert module_0.is_simple_power(2, 1) == False     # x != 1, n is 1
    
    # exact powers
    assert module_0.is_simple_power(8, 2) == True      # 2^3 = 8
    assert module_0.is_simple_power(9, 3) == True      # 3^2 = 9
    assert module_0.is_simple_power(27, 3) == True     # 3^3 = 27
    assert module_0.is_simple_power(16, 4) == True     # 4^2 = 16
    assert module_0.is_simple_power(1, 5) == True      # n^0 = 1
    
    # non-powers
    assert module_0.is_simple_power(3, 2) == False     # 3 is not a power of 2
    assert module_0.is_simple_power(5, 3) == False     # 5 is not a power of 3
    assert module_0.is_simple_power(10, 2) == False    # 10 is not a power of 2
    
    # x == n (first power)
    assert module_0.is_simple_power(2, 2) == True
    assert module_0.is_simple_power(7, 7) == True
    
    # loop-exit edge: power overshoots x
    assert module_0.is_simple_power(6, 2) == False     # 4 < 6, 8 > 6
    
    print("All tests passed!")

test_is_simple_power()