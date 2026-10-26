

# Generated at 2026-10-25 10:07:06.230796
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

# Generated at 2026-10-25 10:07:08.379381
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

# Generated at 2026-10-25 10:07:10.119211
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

# Generated at 2026-10-25 10:07:28.697532
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

# Generated at 2026-10-25 10:07:30.090166
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

# Generated at 2026-10-25 10:07:34.797590
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

# Generated at 2026-10-25 10:07:36.628916
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

# Generated at 2026-10-25 10:07:38.074324
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

# Generated at 2026-10-25 10:07:39.613172
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

# Generated at 2026-10-25 10:07:41.147856
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

# Generated at 2026-10-25 10:07:42.588389
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

# Generated at 2026-10-25 10:07:44.014412
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

# Generated at 2026-10-25 10:07:45.407341
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

# Generated at 2026-10-25 10:07:46.835233
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

# Generated at 2026-10-25 10:08:31.023263
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

# Generated at 2026-10-25 10:08:49.038244
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

# Generated at 2026-10-25 10:08:50.470460
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

# Generated at 2026-10-25 10:08:51.983712
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

# Generated at 2026-10-25 10:08:53.375097
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

# Generated at 2026-10-25 10:08:54.876040
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

# Generated at 2026-10-25 10:09:11.412763
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

# Generated at 2026-10-25 10:09:19.389101
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

# Generated at 2026-10-25 10:09:21.804545
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:09:24.585131
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:09:27.007437
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:09:29.709896
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:09:32.123497
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:09:34.537148
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:09:36.247171
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

# Generated at 2026-10-25 10:09:39.316673
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

# Generated at 2026-10-25 10:09:40.852649
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

# Generated at 2026-10-25 10:09:42.388724
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

# Generated at 2026-10-25 10:09:43.925518
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

# Generated at 2026-10-25 10:09:45.460243
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

# Generated at 2026-10-25 10:09:46.893178
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

# Generated at 2026-10-25 10:09:48.326882
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

# Generated at 2026-10-25 10:09:49.730675
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

# Generated at 2026-10-25 10:09:51.194370
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

# Generated at 2026-10-25 10:09:52.734282
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

# Generated at 2026-10-25 10:09:54.165380
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

# Generated at 2026-10-25 10:09:55.600827
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

# Generated at 2026-10-25 10:10:00.315410
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

# Generated at 2026-10-25 10:10:28.675085
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

# Generated at 2026-10-25 10:10:31.089370
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:10:33.504818
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:10:36.233995
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:10:38.658983
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:10:52.122834
# Unit test for function will_it_fly
def test_will_it_fly():assert module_0.will_it_fly([1, 2, 1], 5) is True

# Generated at 2026-10-25 10:11:10.852213
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

# Generated at 2026-10-25 10:11:15.459789
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

# Generated at 2026-10-25 10:11:16.892998
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

# Generated at 2026-10-25 10:11:36.946957
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

# Generated at 2026-10-25 10:11:39.364043
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:11:41.959044
# Unit test for function will_it_fly
def test_will_it_fly():assert module_0.will_it_fly([1, 2, 1], 5) is True

# Generated at 2026-10-25 10:11:58.479146
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

# Generated at 2026-10-25 10:11:59.912090
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

# Generated at 2026-10-25 10:12:01.346513
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

# Generated at 2026-10-25 10:12:21.739677
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

# Generated at 2026-10-25 10:12:24.281313
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:12:26.697319
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:12:29.261398
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:12:31.676677
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:12:34.091951
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:12:36.756146
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:12:39.171750
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:12:41.585743
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:12:44.001188
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:12:46.415004
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:12:48.828626
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:12:51.251516
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:12:53.748111
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:12:56.163640
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:12:58.577799
# Unit test for function will_it_fly