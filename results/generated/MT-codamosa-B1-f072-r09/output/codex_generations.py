

# Generated at 2026-10-25 10:10:00.821951
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

# Generated at 2026-10-25 10:10:05.533363
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

# Generated at 2026-10-25 10:10:08.501084
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

# Generated at 2026-10-25 10:10:24.926100
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

# Generated at 2026-10-25 10:10:27.460326
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:10:29.873258
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:10:32.288139
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:10:35.025490
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:10:37.445143
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:10:40.074233
# Unit test for function will_it_fly
def test_will_it_fly():assert module_0.will_it_fly([1, 2, 1], 5) is True

# Generated at 2026-10-25 10:10:41.474721
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

# Generated at 2026-10-25 10:10:58.306913
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

# Generated at 2026-10-25 10:10:59.716536
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

# Generated at 2026-10-25 10:11:01.115760
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

# Generated at 2026-10-25 10:11:09.114144
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

# Generated at 2026-10-25 10:11:25.598573
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

# Generated at 2026-10-25 10:11:42.197998
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

# Generated at 2026-10-25 10:11:59.298886
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

# Generated at 2026-10-25 10:12:00.875845
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

# Generated at 2026-10-25 10:12:02.268399
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

# Generated at 2026-10-25 10:12:03.702099
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

# Generated at 2026-10-25 10:12:05.134540
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

# Generated at 2026-10-25 10:12:09.882679
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

# Generated at 2026-10-25 10:12:11.380974
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

# Generated at 2026-10-25 10:12:12.814989
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

# Generated at 2026-10-25 10:12:15.350223
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:12:17.874671
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:12:20.289434
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:12:23.079612
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:12:25.494467
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:12:28.022370
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:12:30.438324
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:12:32.853352
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:12:35.268291
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:12:38.098685
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:12:40.513343
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:12:42.929104
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:12:45.342325
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:12:47.756190
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:12:50.174780
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:12:52.600345
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:12:55.012337
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:12:57.426081
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:12:59.844022
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:13:02.256098
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:13:04.670628
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:13:07.086003
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:13:09.499878
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:13:11.914504
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:13:14.330709
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:13:16.745554
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:13:19.166325
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:13:21.580724
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:13:23.994791
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:13:26.409442
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:13:28.824398
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:13:31.240216
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:13:33.655405
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:13:36.068653
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:13:38.485220
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:13:40.896390
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:13:43.311796
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:13:45.726799
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:13:48.140855
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:13:50.554516
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:13:52.969308
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:13:55.384414
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:13:57.798642
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:14:00.213524
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:14:02.626889
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:14:05.042432
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:14:07.456474
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:14:09.871273
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:14:12.285807
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:14:14.704375
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:14:17.113763
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:14:19.529093
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:14:22.011611
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:14:24.425770
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:14:26.840223
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:14:29.254128
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:14:31.669194
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:14:34.083936
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:14:36.498308
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:14:38.913116
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:14:41.328087
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:14:43.743188
# Unit test for function will_it_fly

# Generated at 2026-10-25 10:14:56.757805
# Unit test for function will_it_fly
def test_will_it_fly():assert module_0.will_it_fly([1, 2, 1], 4) is True

# Generated at 2026-10-25 10:15:13.246497
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

# Generated at 2026-10-25 10:15:31.268130
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

# Generated at 2026-10-25 10:15:59.426966
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