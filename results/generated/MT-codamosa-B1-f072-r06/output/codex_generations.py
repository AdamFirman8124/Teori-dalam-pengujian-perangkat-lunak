

# Generated at 2026-10-25 12:27:30.467210
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

# Generated at 2026-10-25 12:27:31.943548
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

# Generated at 2026-10-25 12:27:33.445758
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

# Generated at 2026-10-25 12:27:57.661129
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

# Generated at 2026-10-25 12:28:18.962904
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

# Generated at 2026-10-25 12:29:06.663236
# Unit test for function will_it_fly

# Generated at 2026-10-25 12:29:18.659051
# Unit test for function will_it_fly
def test_will_it_fly():assert module_0.will_it_fly([1, 2, 1], 4) == True

# Generated at 2026-10-25 12:29:22.459262
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

# Generated at 2026-10-25 12:29:23.983520
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

# Generated at 2026-10-25 12:29:28.694940
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

# Generated at 2026-10-25 12:29:30.496509
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

# Generated at 2026-10-25 12:29:57.433955
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

# Generated at 2026-10-25 12:30:24.766534
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

# Generated at 2026-10-25 12:31:27.293585
# Unit test for function will_it_fly
def test_will_it_fly():
    assert module_0.will_it_fly([1, 2, 1], 4) == True
    assert module_0.will_it_fly([1, 2, 1], 3) == False
    assert module_0.will_it_fly([1, 2, 3], 6) == False
    assert module_0.will_it_fly([3, 2, 3], 10) == True
    assert module_0.will_it_fly([3, 2, 3], 5) == False
    assert module_0.will_it_fly([1, 2, 2, 1], 10) == True
    assert module_0.will_it_fly([1, 2], 3) == False
    assert module_0.will_it_fly([], 0) == True
    assert module_0.will_it_fly([5], 5) == True
    assert module_0.will_it_fly([5], 4) == False

# Generated at 2026-10-25 12:31:52.261136
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

# Generated at 2026-10-25 12:31:53.798026
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