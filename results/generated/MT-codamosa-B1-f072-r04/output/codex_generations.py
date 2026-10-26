

# Generated at 2026-10-25 10:02:24.229591
# Unit test for function will_it_fly
def test_will_it_fly():
    # True: palindrome and sum(q) <= w
    assert module_0.will_it_fly([1, 2, 1], 5) == True   # sum=4 <= 5, palindrome
    assert module_0.will_it_fly([1, 2, 1], 4) == True   # sum=4 == w, palindrome
    assert module_0.will_it_fly([3, 2, 3], 9) == True   # sum=8 <= 9, palindrome
    assert module_0.will_it_fly([2, 2], 4) == True      # even-length palindrome
    assert module_0.will_it_fly([5], 5) == True        # single element is palindrome
    assert module_0.will_it_fly([], 0) == True         # sum=0 <= 0, vacuously palindrome

    # False: palindrome but too heavy sum(q) > w
    assert module_0.will_it_fly([1, 2, 1], 3) == False  # sum=4 > 3
    assert module_0.will_it_fly([3, 2, 3], 7) == False  # sum=8 > 7
    assert module_0.will_it_fly([5], 4) == False        # sum=5 > 4
    assert module_0.will_it_fly([2, 2], 3) == False     # sum=4 > 3

    # False: light enough but not palindrome
    assert module_0.will_it_fly([1, 2, 3], 10) == False # sum=6 <= 10, not palindrome
    assert module_0.will_it_fly([1, 2], 5) == False     # sum=3 <= 5, not palindrome
    assert module_0.will_it_fly([2, 3], 5) == False     # sum=5 <= 5, not palindrome

    # False: both too heavy and not palindrome
    assert module_0.will_it_fly([1, 2, 3], 5) == False  # sum=6 > 5, not palindrome

# Generated at 2026-10-25 10:02:52.888510
# Unit test for function will_it_fly
def test_will_it_fly():
    # True: palindrome and sum(q) <= w
    assert module_0.will_it_fly([1, 2, 1], 5) == True   # sum=4 <= 5, palindrome
    assert module_0.will_it_fly([1, 2, 1], 4) == True   # sum=4 == w, palindrome
    assert module_0.will_it_fly([3, 2, 3], 9) == True   # sum=8 <= 9, palindrome
    assert module_0.will_it_fly([2, 2], 4) == True      # even-length palindrome
    assert module_0.will_it_fly([5], 5) == True        # single element is palindrome
    assert module_0.will_it_fly([], 0) == True         # sum=0 <= 0, vacuously palindrome

    # False: palindrome but too heavy sum(q) > w
    assert module_0.will_it_fly([1, 2, 1], 3) == False  # sum=4 > 3
    assert module_0.will_it_fly([3, 2, 3], 7) == False  # sum=8 > 7
    assert module_0.will_it_fly([5], 4) == False        # sum=5 > 4
    assert module_0.will_it_fly([2, 2], 3) == False     # sum=4 > 3

    # False: light enough but not palindrome
    assert module_0.will_it_fly([1, 2, 3], 10) == False # sum=6 <= 10, not palindrome
    assert module_0.will_it_fly([1, 2], 5) == False     # sum=3 <= 5, not palindrome
    assert module_0.will_it_fly([2, 3], 5) == False     # sum=5 <= 5, not palindrome

    # False: both too heavy and not palindrome
    assert module_0.will_it_fly([1, 2, 3], 5) == False  # sum=6 > 5, not palindrome

# Generated at 2026-10-25 10:02:54.424123
# Unit test for function will_it_fly
def test_will_it_fly():
    # True: palindrome and sum(q) <= w
    assert module_0.will_it_fly([1, 2, 1], 5) == True   # sum=4 <= 5, palindrome
    assert module_0.will_it_fly([1, 2, 1], 4) == True   # sum=4 == w, palindrome
    assert module_0.will_it_fly([3, 2, 3], 9) == True   # sum=8 <= 9, palindrome
    assert module_0.will_it_fly([2, 2], 4) == True      # even-length palindrome
    assert module_0.will_it_fly([5], 5) == True        # single element is palindrome
    assert module_0.will_it_fly([], 0) == True         # sum=0 <= 0, vacuously palindrome

    # False: palindrome but too heavy sum(q) > w
    assert module_0.will_it_fly([1, 2, 1], 3) == False  # sum=4 > 3
    assert module_0.will_it_fly([3, 2, 3], 7) == False  # sum=8 > 7
    assert module_0.will_it_fly([5], 4) == False        # sum=5 > 4
    assert module_0.will_it_fly([2, 2], 3) == False     # sum=4 > 3

    # False: light enough but not palindrome
    assert module_0.will_it_fly([1, 2, 3], 10) == False # sum=6 <= 10, not palindrome
    assert module_0.will_it_fly([1, 2], 5) == False     # sum=3 <= 5, not palindrome
    assert module_0.will_it_fly([2, 3], 5) == False     # sum=5 <= 5, not palindrome

    # False: both too heavy and not palindrome
    assert module_0.will_it_fly([1, 2, 3], 5) == False  # sum=6 > 5, not palindrome

# Generated at 2026-10-25 10:02:55.961663
# Unit test for function will_it_fly
def test_will_it_fly():
    # True: palindrome and sum(q) <= w
    assert module_0.will_it_fly([1, 2, 1], 5) == True   # sum=4 <= 5, palindrome
    assert module_0.will_it_fly([1, 2, 1], 4) == True   # sum=4 == w, palindrome
    assert module_0.will_it_fly([3, 2, 3], 9) == True   # sum=8 <= 9, palindrome
    assert module_0.will_it_fly([2, 2], 4) == True      # even-length palindrome
    assert module_0.will_it_fly([5], 5) == True        # single element is palindrome
    assert module_0.will_it_fly([], 0) == True         # sum=0 <= 0, vacuously palindrome

    # False: palindrome but too heavy sum(q) > w
    assert module_0.will_it_fly([1, 2, 1], 3) == False  # sum=4 > 3
    assert module_0.will_it_fly([3, 2, 3], 7) == False  # sum=8 > 7
    assert module_0.will_it_fly([5], 4) == False        # sum=5 > 4
    assert module_0.will_it_fly([2, 2], 3) == False     # sum=4 > 3

    # False: light enough but not palindrome
    assert module_0.will_it_fly([1, 2, 3], 10) == False # sum=6 <= 10, not palindrome
    assert module_0.will_it_fly([1, 2], 5) == False     # sum=3 <= 5, not palindrome
    assert module_0.will_it_fly([2, 3], 5) == False     # sum=5 <= 5, not palindrome

    # False: both too heavy and not palindrome
    assert module_0.will_it_fly([1, 2, 3], 5) == False  # sum=6 > 5, not palindrome

# Generated at 2026-10-25 10:02:57.489566
# Unit test for function will_it_fly
def test_will_it_fly():
    # True: palindrome and sum(q) <= w
    assert module_0.will_it_fly([1, 2, 1], 5) == True   # sum=4 <= 5, palindrome
    assert module_0.will_it_fly([1, 2, 1], 4) == True   # sum=4 == w, palindrome
    assert module_0.will_it_fly([3, 2, 3], 9) == True   # sum=8 <= 9, palindrome
    assert module_0.will_it_fly([2, 2], 4) == True      # even-length palindrome
    assert module_0.will_it_fly([5], 5) == True        # single element is palindrome
    assert module_0.will_it_fly([], 0) == True         # sum=0 <= 0, vacuously palindrome

    # False: palindrome but too heavy sum(q) > w
    assert module_0.will_it_fly([1, 2, 1], 3) == False  # sum=4 > 3
    assert module_0.will_it_fly([3, 2, 3], 7) == False  # sum=8 > 7
    assert module_0.will_it_fly([5], 4) == False        # sum=5 > 4
    assert module_0.will_it_fly([2, 2], 3) == False     # sum=4 > 3

    # False: light enough but not palindrome
    assert module_0.will_it_fly([1, 2, 3], 10) == False # sum=6 <= 10, not palindrome
    assert module_0.will_it_fly([1, 2], 5) == False     # sum=3 <= 5, not palindrome
    assert module_0.will_it_fly([2, 3], 5) == False     # sum=5 <= 5, not palindrome

    # False: both too heavy and not palindrome
    assert module_0.will_it_fly([1, 2, 3], 5) == False  # sum=6 > 5, not palindrome

# Generated at 2026-10-25 10:02:59.034698
# Unit test for function will_it_fly
def test_will_it_fly():
    # True: palindrome and sum(q) <= w
    assert module_0.will_it_fly([1, 2, 1], 5) == True   # sum=4 <= 5, palindrome
    assert module_0.will_it_fly([1, 2, 1], 4) == True   # sum=4 == w, palindrome
    assert module_0.will_it_fly([3, 2, 3], 9) == True   # sum=8 <= 9, palindrome
    assert module_0.will_it_fly([2, 2], 4) == True      # even-length palindrome
    assert module_0.will_it_fly([5], 5) == True        # single element is palindrome
    assert module_0.will_it_fly([], 0) == True         # sum=0 <= 0, vacuously palindrome

    # False: palindrome but too heavy sum(q) > w
    assert module_0.will_it_fly([1, 2, 1], 3) == False  # sum=4 > 3
    assert module_0.will_it_fly([3, 2, 3], 7) == False  # sum=8 > 7
    assert module_0.will_it_fly([5], 4) == False        # sum=5 > 4
    assert module_0.will_it_fly([2, 2], 3) == False     # sum=4 > 3

    # False: light enough but not palindrome
    assert module_0.will_it_fly([1, 2, 3], 10) == False # sum=6 <= 10, not palindrome
    assert module_0.will_it_fly([1, 2], 5) == False     # sum=3 <= 5, not palindrome
    assert module_0.will_it_fly([2, 3], 5) == False     # sum=5 <= 5, not palindrome

    # False: both too heavy and not palindrome
    assert module_0.will_it_fly([1, 2, 3], 5) == False  # sum=6 > 5, not palindrome

# Generated at 2026-10-25 10:03:04.461471
# Unit test for function will_it_fly
def test_will_it_fly():
    # True: palindrome and sum(q) <= w
    assert module_0.will_it_fly([1, 2, 1], 5) == True   # sum=4 <= 5, palindrome
    assert module_0.will_it_fly([1, 2, 1], 4) == True   # sum=4 == w, palindrome
    assert module_0.will_it_fly([3, 2, 3], 9) == True   # sum=8 <= 9, palindrome
    assert module_0.will_it_fly([2, 2], 4) == True      # even-length palindrome
    assert module_0.will_it_fly([5], 5) == True        # single element is palindrome
    assert module_0.will_it_fly([], 0) == True         # sum=0 <= 0, vacuously palindrome

    # False: palindrome but too heavy sum(q) > w
    assert module_0.will_it_fly([1, 2, 1], 3) == False  # sum=4 > 3
    assert module_0.will_it_fly([3, 2, 3], 7) == False  # sum=8 > 7
    assert module_0.will_it_fly([5], 4) == False        # sum=5 > 4
    assert module_0.will_it_fly([2, 2], 3) == False     # sum=4 > 3

    # False: light enough but not palindrome
    assert module_0.will_it_fly([1, 2, 3], 10) == False # sum=6 <= 10, not palindrome
    assert module_0.will_it_fly([1, 2], 5) == False     # sum=3 <= 5, not palindrome
    assert module_0.will_it_fly([2, 3], 5) == False     # sum=5 <= 5, not palindrome

    # False: both too heavy and not palindrome
    assert module_0.will_it_fly([1, 2, 3], 5) == False  # sum=6 > 5, not palindrome

# Generated at 2026-10-25 10:03:06.099603
# Unit test for function will_it_fly
def test_will_it_fly():
    # True: palindrome and sum(q) <= w
    assert module_0.will_it_fly([1, 2, 1], 5) == True   # sum=4 <= 5, palindrome
    assert module_0.will_it_fly([1, 2, 1], 4) == True   # sum=4 == w, palindrome
    assert module_0.will_it_fly([3, 2, 3], 9) == True   # sum=8 <= 9, palindrome
    assert module_0.will_it_fly([2, 2], 4) == True      # even-length palindrome
    assert module_0.will_it_fly([5], 5) == True        # single element is palindrome
    assert module_0.will_it_fly([], 0) == True         # sum=0 <= 0, vacuously palindrome

    # False: palindrome but too heavy sum(q) > w
    assert module_0.will_it_fly([1, 2, 1], 3) == False  # sum=4 > 3
    assert module_0.will_it_fly([3, 2, 3], 7) == False  # sum=8 > 7
    assert module_0.will_it_fly([5], 4) == False        # sum=5 > 4
    assert module_0.will_it_fly([2, 2], 3) == False     # sum=4 > 3

    # False: light enough but not palindrome
    assert module_0.will_it_fly([1, 2, 3], 10) == False # sum=6 <= 10, not palindrome
    assert module_0.will_it_fly([1, 2], 5) == False     # sum=3 <= 5, not palindrome
    assert module_0.will_it_fly([2, 3], 5) == False     # sum=5 <= 5, not palindrome

    # False: both too heavy and not palindrome
    assert module_0.will_it_fly([1, 2, 3], 5) == False  # sum=6 > 5, not palindrome

# Generated at 2026-10-25 10:03:09.170748
# Unit test for function will_it_fly
def test_will_it_fly():
    # True: palindrome and sum(q) <= w
    assert module_0.will_it_fly([1, 2, 1], 5) == True   # sum=4 <= 5, palindrome
    assert module_0.will_it_fly([1, 2, 1], 4) == True   # sum=4 == w, palindrome
    assert module_0.will_it_fly([3, 2, 3], 9) == True   # sum=8 <= 9, palindrome
    assert module_0.will_it_fly([2, 2], 4) == True      # even-length palindrome
    assert module_0.will_it_fly([5], 5) == True        # single element is palindrome
    assert module_0.will_it_fly([], 0) == True         # sum=0 <= 0, vacuously palindrome

    # False: palindrome but too heavy sum(q) > w
    assert module_0.will_it_fly([1, 2, 1], 3) == False  # sum=4 > 3
    assert module_0.will_it_fly([3, 2, 3], 7) == False  # sum=8 > 7
    assert module_0.will_it_fly([5], 4) == False        # sum=5 > 4
    assert module_0.will_it_fly([2, 2], 3) == False     # sum=4 > 3

    # False: light enough but not palindrome
    assert module_0.will_it_fly([1, 2, 3], 10) == False # sum=6 <= 10, not palindrome
    assert module_0.will_it_fly([1, 2], 5) == False     # sum=3 <= 5, not palindrome
    assert module_0.will_it_fly([2, 3], 5) == False     # sum=5 <= 5, not palindrome

    # False: both too heavy and not palindrome
    assert module_0.will_it_fly([1, 2, 3], 5) == False  # sum=6 > 5, not palindrome

# Generated at 2026-10-25 10:03:10.592013
# Unit test for function will_it_fly
def test_will_it_fly():
    # True: palindrome and sum(q) <= w
    assert module_0.will_it_fly([1, 2, 1], 5) == True   # sum=4 <= 5, palindrome
    assert module_0.will_it_fly([1, 2, 1], 4) == True   # sum=4 == w, palindrome
    assert module_0.will_it_fly([3, 2, 3], 9) == True   # sum=8 <= 9, palindrome
    assert module_0.will_it_fly([2, 2], 4) == True      # even-length palindrome
    assert module_0.will_it_fly([5], 5) == True        # single element is palindrome
    assert module_0.will_it_fly([], 0) == True         # sum=0 <= 0, vacuously palindrome

    # False: palindrome but too heavy sum(q) > w
    assert module_0.will_it_fly([1, 2, 1], 3) == False  # sum=4 > 3
    assert module_0.will_it_fly([3, 2, 3], 7) == False  # sum=8 > 7
    assert module_0.will_it_fly([5], 4) == False        # sum=5 > 4
    assert module_0.will_it_fly([2, 2], 3) == False     # sum=4 > 3

    # False: light enough but not palindrome
    assert module_0.will_it_fly([1, 2, 3], 10) == False # sum=6 <= 10, not palindrome
    assert module_0.will_it_fly([1, 2], 5) == False     # sum=3 <= 5, not palindrome
    assert module_0.will_it_fly([2, 3], 5) == False     # sum=5 <= 5, not palindrome

    # False: both too heavy and not palindrome
    assert module_0.will_it_fly([1, 2, 3], 5) == False  # sum=6 > 5, not palindrome

# Generated at 2026-10-25 10:03:27.202665
# Unit test for function will_it_fly
def test_will_it_fly():
    # True: palindrome and sum(q) <= w
    assert module_0.will_it_fly([1, 2, 1], 5) == True   # sum=4 <= 5, palindrome
    assert module_0.will_it_fly([1, 2, 1], 4) == True   # sum=4 == w, palindrome
    assert module_0.will_it_fly([3, 2, 3], 9) == True   # sum=8 <= 9, palindrome
    assert module_0.will_it_fly([2, 2], 4) == True      # even-length palindrome
    assert module_0.will_it_fly([5], 5) == True        # single element is palindrome
    assert module_0.will_it_fly([], 0) == True         # sum=0 <= 0, vacuously palindrome

    # False: palindrome but too heavy sum(q) > w
    assert module_0.will_it_fly([1, 2, 1], 3) == False  # sum=4 > 3
    assert module_0.will_it_fly([3, 2, 3], 7) == False  # sum=8 > 7
    assert module_0.will_it_fly([5], 4) == False        # sum=5 > 4
    assert module_0.will_it_fly([2, 2], 3) == False     # sum=4 > 3

    # False: light enough but not palindrome
    assert module_0.will_it_fly([1, 2, 3], 10) == False # sum=6 <= 10, not palindrome
    assert module_0.will_it_fly([1, 2], 5) == False     # sum=3 <= 5, not palindrome
    assert module_0.will_it_fly([2, 3], 5) == False     # sum=5 <= 5, not palindrome

    # False: both too heavy and not palindrome
    assert module_0.will_it_fly([1, 2, 3], 5) == False  # sum=6 > 5, not palindrome

# Generated at 2026-10-25 10:03:43.785498
# Unit test for function will_it_fly
def test_will_it_fly():
    # True: palindrome and sum(q) <= w
    assert module_0.will_it_fly([1, 2, 1], 5) == True   # sum=4 <= 5, palindrome
    assert module_0.will_it_fly([1, 2, 1], 4) == True   # sum=4 == w, palindrome
    assert module_0.will_it_fly([3, 2, 3], 9) == True   # sum=8 <= 9, palindrome
    assert module_0.will_it_fly([2, 2], 4) == True      # even-length palindrome
    assert module_0.will_it_fly([5], 5) == True        # single element is palindrome
    assert module_0.will_it_fly([], 0) == True         # sum=0 <= 0, vacuously palindrome

    # False: palindrome but too heavy sum(q) > w
    assert module_0.will_it_fly([1, 2, 1], 3) == False  # sum=4 > 3
    assert module_0.will_it_fly([3, 2, 3], 7) == False  # sum=8 > 7
    assert module_0.will_it_fly([5], 4) == False        # sum=5 > 4
    assert module_0.will_it_fly([2, 2], 3) == False     # sum=4 > 3

    # False: light enough but not palindrome
    assert module_0.will_it_fly([1, 2, 3], 10) == False # sum=6 <= 10, not palindrome
    assert module_0.will_it_fly([1, 2], 5) == False     # sum=3 <= 5, not palindrome
    assert module_0.will_it_fly([2, 3], 5) == False     # sum=5 <= 5, not palindrome

    # False: both too heavy and not palindrome
    assert module_0.will_it_fly([1, 2, 3], 5) == False  # sum=6 > 5, not palindrome

# Generated at 2026-10-25 10:04:03.688568
# Unit test for function will_it_fly
def test_will_it_fly():
    # True: palindrome and sum(q) <= w
    assert module_0.will_it_fly([1, 2, 1], 5) == True   # sum=4 <= 5, palindrome
    assert module_0.will_it_fly([1, 2, 1], 4) == True   # sum=4 == w, palindrome
    assert module_0.will_it_fly([3, 2, 3], 9) == True   # sum=8 <= 9, palindrome
    assert module_0.will_it_fly([2, 2], 4) == True      # even-length palindrome
    assert module_0.will_it_fly([5], 5) == True        # single element is palindrome
    assert module_0.will_it_fly([], 0) == True         # sum=0 <= 0, vacuously palindrome

    # False: palindrome but too heavy sum(q) > w
    assert module_0.will_it_fly([1, 2, 1], 3) == False  # sum=4 > 3
    assert module_0.will_it_fly([3, 2, 3], 7) == False  # sum=8 > 7
    assert module_0.will_it_fly([5], 4) == False        # sum=5 > 4
    assert module_0.will_it_fly([2, 2], 3) == False     # sum=4 > 3

    # False: light enough but not palindrome
    assert module_0.will_it_fly([1, 2, 3], 10) == False # sum=6 <= 10, not palindrome
    assert module_0.will_it_fly([1, 2], 5) == False     # sum=3 <= 5, not palindrome
    assert module_0.will_it_fly([2, 3], 5) == False     # sum=5 <= 5, not palindrome

    # False: both too heavy and not palindrome
    assert module_0.will_it_fly([1, 2, 3], 5) == False  # sum=6 > 5, not palindrome

# Generated at 2026-10-25 10:04:06.107037
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:04:08.876666
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:04:11.289384
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:04:13.704022
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:04:16.119666
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:04:30.752848
# Unit test for function will_it_fly
def test_will_it_fly():assert module_0.will_it_fly([1, 2, 1], 4) is True

# Generated at 2026-10-25 10:04:47.275968
# Unit test for function will_it_fly
def test_will_it_fly():
    # True: palindrome and sum(q) <= w
    assert module_0.will_it_fly([1, 2, 1], 5) == True   # sum=4 <= 5, palindrome
    assert module_0.will_it_fly([1, 2, 1], 4) == True   # sum=4 == w, palindrome
    assert module_0.will_it_fly([3, 2, 3], 9) == True   # sum=8 <= 9, palindrome
    assert module_0.will_it_fly([2, 2], 4) == True      # even-length palindrome
    assert module_0.will_it_fly([5], 5) == True        # single element is palindrome
    assert module_0.will_it_fly([], 0) == True         # sum=0 <= 0, vacuously palindrome

    # False: palindrome but too heavy sum(q) > w
    assert module_0.will_it_fly([1, 2, 1], 3) == False  # sum=4 > 3
    assert module_0.will_it_fly([3, 2, 3], 7) == False  # sum=8 > 7
    assert module_0.will_it_fly([5], 4) == False        # sum=5 > 4
    assert module_0.will_it_fly([2, 2], 3) == False     # sum=4 > 3

    # False: light enough but not palindrome
    assert module_0.will_it_fly([1, 2, 3], 10) == False # sum=6 <= 10, not palindrome
    assert module_0.will_it_fly([1, 2], 5) == False     # sum=3 <= 5, not palindrome
    assert module_0.will_it_fly([2, 3], 5) == False     # sum=5 <= 5, not palindrome

    # False: both too heavy and not palindrome
    assert module_0.will_it_fly([1, 2, 3], 5) == False  # sum=6 > 5, not palindrome

# Generated at 2026-10-25 10:04:48.688776
# Unit test for function will_it_fly
def test_will_it_fly():
    # True: palindrome and sum(q) <= w
    assert module_0.will_it_fly([1, 2, 1], 5) == True   # sum=4 <= 5, palindrome
    assert module_0.will_it_fly([1, 2, 1], 4) == True   # sum=4 == w, palindrome
    assert module_0.will_it_fly([3, 2, 3], 9) == True   # sum=8 <= 9, palindrome
    assert module_0.will_it_fly([2, 2], 4) == True      # even-length palindrome
    assert module_0.will_it_fly([5], 5) == True        # single element is palindrome
    assert module_0.will_it_fly([], 0) == True         # sum=0 <= 0, vacuously palindrome

    # False: palindrome but too heavy sum(q) > w
    assert module_0.will_it_fly([1, 2, 1], 3) == False  # sum=4 > 3
    assert module_0.will_it_fly([3, 2, 3], 7) == False  # sum=8 > 7
    assert module_0.will_it_fly([5], 4) == False        # sum=5 > 4
    assert module_0.will_it_fly([2, 2], 3) == False     # sum=4 > 3

    # False: light enough but not palindrome
    assert module_0.will_it_fly([1, 2, 3], 10) == False # sum=6 <= 10, not palindrome
    assert module_0.will_it_fly([1, 2], 5) == False     # sum=3 <= 5, not palindrome
    assert module_0.will_it_fly([2, 3], 5) == False     # sum=5 <= 5, not palindrome

    # False: both too heavy and not palindrome
    assert module_0.will_it_fly([1, 2, 3], 5) == False  # sum=6 > 5, not palindrome

# Generated at 2026-10-25 10:04:50.123432
# Unit test for function will_it_fly
def test_will_it_fly():
    # True: palindrome and sum(q) <= w
    assert module_0.will_it_fly([1, 2, 1], 5) == True   # sum=4 <= 5, palindrome
    assert module_0.will_it_fly([1, 2, 1], 4) == True   # sum=4 == w, palindrome
    assert module_0.will_it_fly([3, 2, 3], 9) == True   # sum=8 <= 9, palindrome
    assert module_0.will_it_fly([2, 2], 4) == True      # even-length palindrome
    assert module_0.will_it_fly([5], 5) == True        # single element is palindrome
    assert module_0.will_it_fly([], 0) == True         # sum=0 <= 0, vacuously palindrome

    # False: palindrome but too heavy sum(q) > w
    assert module_0.will_it_fly([1, 2, 1], 3) == False  # sum=4 > 3
    assert module_0.will_it_fly([3, 2, 3], 7) == False  # sum=8 > 7
    assert module_0.will_it_fly([5], 4) == False        # sum=5 > 4
    assert module_0.will_it_fly([2, 2], 3) == False     # sum=4 > 3

    # False: light enough but not palindrome
    assert module_0.will_it_fly([1, 2, 3], 10) == False # sum=6 <= 10, not palindrome
    assert module_0.will_it_fly([1, 2], 5) == False     # sum=3 <= 5, not palindrome
    assert module_0.will_it_fly([2, 3], 5) == False     # sum=5 <= 5, not palindrome

    # False: both too heavy and not palindrome
    assert module_0.will_it_fly([1, 2, 3], 5) == False  # sum=6 > 5, not palindrome

# Generated at 2026-10-25 10:04:51.570093
# Unit test for function will_it_fly
def test_will_it_fly():
    # True: palindrome and sum(q) <= w
    assert module_0.will_it_fly([1, 2, 1], 5) == True   # sum=4 <= 5, palindrome
    assert module_0.will_it_fly([1, 2, 1], 4) == True   # sum=4 == w, palindrome
    assert module_0.will_it_fly([3, 2, 3], 9) == True   # sum=8 <= 9, palindrome
    assert module_0.will_it_fly([2, 2], 4) == True      # even-length palindrome
    assert module_0.will_it_fly([5], 5) == True        # single element is palindrome
    assert module_0.will_it_fly([], 0) == True         # sum=0 <= 0, vacuously palindrome

    # False: palindrome but too heavy sum(q) > w
    assert module_0.will_it_fly([1, 2, 1], 3) == False  # sum=4 > 3
    assert module_0.will_it_fly([3, 2, 3], 7) == False  # sum=8 > 7
    assert module_0.will_it_fly([5], 4) == False        # sum=5 > 4
    assert module_0.will_it_fly([2, 2], 3) == False     # sum=4 > 3

    # False: light enough but not palindrome
    assert module_0.will_it_fly([1, 2, 3], 10) == False # sum=6 <= 10, not palindrome
    assert module_0.will_it_fly([1, 2], 5) == False     # sum=3 <= 5, not palindrome
    assert module_0.will_it_fly([2, 3], 5) == False     # sum=5 <= 5, not palindrome

    # False: both too heavy and not palindrome
    assert module_0.will_it_fly([1, 2, 3], 5) == False  # sum=6 > 5, not palindrome

# Generated at 2026-10-25 10:04:53.005496
# Unit test for function will_it_fly
def test_will_it_fly():
    # True: palindrome and sum(q) <= w
    assert module_0.will_it_fly([1, 2, 1], 5) == True   # sum=4 <= 5, palindrome
    assert module_0.will_it_fly([1, 2, 1], 4) == True   # sum=4 == w, palindrome
    assert module_0.will_it_fly([3, 2, 3], 9) == True   # sum=8 <= 9, palindrome
    assert module_0.will_it_fly([2, 2], 4) == True      # even-length palindrome
    assert module_0.will_it_fly([5], 5) == True        # single element is palindrome
    assert module_0.will_it_fly([], 0) == True         # sum=0 <= 0, vacuously palindrome

    # False: palindrome but too heavy sum(q) > w
    assert module_0.will_it_fly([1, 2, 1], 3) == False  # sum=4 > 3
    assert module_0.will_it_fly([3, 2, 3], 7) == False  # sum=8 > 7
    assert module_0.will_it_fly([5], 4) == False        # sum=5 > 4
    assert module_0.will_it_fly([2, 2], 3) == False     # sum=4 > 3

    # False: light enough but not palindrome
    assert module_0.will_it_fly([1, 2, 3], 10) == False # sum=6 <= 10, not palindrome
    assert module_0.will_it_fly([1, 2], 5) == False     # sum=3 <= 5, not palindrome
    assert module_0.will_it_fly([2, 3], 5) == False     # sum=5 <= 5, not palindrome

    # False: both too heavy and not palindrome
    assert module_0.will_it_fly([1, 2, 3], 5) == False  # sum=6 > 5, not palindrome

# Generated at 2026-10-25 10:04:55.661720
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:04:58.225237
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:05:00.640490
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:05:03.865534
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:05:06.433944
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:05:08.848956
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:05:11.265029
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:05:13.830889
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:05:16.246703
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:05:18.660824
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:05:30.176910
# Unit test for function will_it_fly
def test_will_it_fly():assert module_0.will_it_fly([1, 2, 1], 5) is True

# Generated at 2026-10-25 10:05:36.746138
# Unit test for function will_it_fly
def test_will_it_fly():
    assert module_0.will_it_fly([1, 2], 5) is False       # Not a palindrome
    assert module_0.will_it_fly([3, 2, 3], 7) is False    # Sum exceeds limit
    assert module_0.will_it_fly([3, 2, 3], 8) is True     # Palindrome and sum equals limit
    assert module_0.will_it_fly([1, 2, 1], 5) is True     # Valid palindrome within limit
    assert module_0.will_it_fly([5], 5) is True           # Single-element list
    assert module_0.will_it_fly([], 0) is True             # Empty list