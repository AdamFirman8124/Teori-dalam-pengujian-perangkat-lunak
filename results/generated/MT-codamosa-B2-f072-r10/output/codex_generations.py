

# Generated at 2026-10-24 14:24:05.762692
# Unit test for function will_it_fly
def test_will_it_fly():
    # True: palindrome and sum(q) <= w
    assert module_0.will_it_fly([3, 2, 3], 9) == True
    assert module_0.will_it_fly([3, 2, 3], 8) == True  # boundary: sum == w
    assert module_0.will_it_fly([1, 2, 1], 4) == True
    assert module_0.will_it_fly([2, 2], 4) == True
    assert module_0.will_it_fly([1, 2, 2, 1], 6) == True
    assert module_0.will_it_fly([1], 1) == True
    assert module_0.will_it_fly([], 0) == True

    # False: palindrome but sum(q) > w
    assert module_0.will_it_fly([3, 2, 3], 1) == False
    assert module_0.will_it_fly([1, 2, 1], 3) == False

    # False: sum(q) <= w but not palindrome
    assert module_0.will_it_fly([1, 2], 5) == False
    assert module_0.will_it_fly([1, 2, 3], 6) == False

    # False: not palindrome and too heavy
    assert module_0.will_it_fly([1, 2, 3], 5) == False

# Generated at 2026-10-24 14:24:08.178513
# Unit test for function will_it_fly

# Generated at 2026-10-24 14:24:10.594362
# Unit test for function will_it_fly

# Generated at 2026-10-24 14:24:13.013739
# Unit test for function will_it_fly

# Generated at 2026-10-24 14:24:15.427713
# Unit test for function will_it_fly

# Generated at 2026-10-24 14:24:17.845023
# Unit test for function will_it_fly

# Generated at 2026-10-24 14:24:20.258909
# Unit test for function will_it_fly

# Generated at 2026-10-24 14:24:22.674352
# Unit test for function will_it_fly

# Generated at 2026-10-24 14:24:25.276548
# Unit test for function will_it_fly

# Generated at 2026-10-24 14:24:27.694682
# Unit test for function will_it_fly

# Generated at 2026-10-24 14:24:30.111459
# Unit test for function will_it_fly

# Generated at 2026-10-24 14:24:32.528916
# Unit test for function will_it_fly

# Generated at 2026-10-24 14:24:34.953715
# Unit test for function will_it_fly