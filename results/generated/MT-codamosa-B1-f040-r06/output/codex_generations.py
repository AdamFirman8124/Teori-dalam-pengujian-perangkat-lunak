

# Generated at 2026-10-24 10:55:27.480014
# Unit test for function triples_sum_to_zero

# Generated at 2026-10-24 10:55:30.070302
# Unit test for function triples_sum_to_zero

# Generated at 2026-10-24 10:55:32.491420
# Unit test for function triples_sum_to_zero

# Generated at 2026-10-24 10:55:35.058863
# Unit test for function triples_sum_to_zero

# Generated at 2026-10-24 10:55:37.480880
# Unit test for function triples_sum_to_zero

# Generated at 2026-10-24 10:55:39.902088
# Unit test for function triples_sum_to_zero

# Generated at 2026-10-24 10:55:42.319107
# Unit test for function triples_sum_to_zero

# Generated at 2026-10-24 10:55:44.888078
# Unit test for function triples_sum_to_zero

# Generated at 2026-10-24 10:55:47.305029
# Unit test for function triples_sum_to_zero

# Generated at 2026-10-24 10:55:49.722609
# Unit test for function triples_sum_to_zero

# Generated at 2026-10-24 10:55:52.143839
# Unit test for function triples_sum_to_zero

# Generated at 2026-10-24 10:55:54.561340
# Unit test for function triples_sum_to_zero

# Generated at 2026-10-24 10:55:56.978900
# Unit test for function triples_sum_to_zero

# Generated at 2026-10-24 10:55:59.399271
# Unit test for function triples_sum_to_zero

# Generated at 2026-10-24 10:56:01.817595
# Unit test for function triples_sum_to_zero

# Generated at 2026-10-24 10:56:04.234904
# Unit test for function triples_sum_to_zero

# Generated at 2026-10-24 10:56:06.654199
# Unit test for function triples_sum_to_zero

# Generated at 2026-10-24 10:56:09.074434
# Unit test for function triples_sum_to_zero

# Generated at 2026-10-24 10:56:11.493633
# Unit test for function triples_sum_to_zero

# Generated at 2026-10-24 10:56:13.913838
# Unit test for function triples_sum_to_zero

# Generated at 2026-10-24 10:56:26.926896
# Unit test for function triples_sum_to_zero
def test_triples_sum_to_zero():assert module_0.triples_sum_to_zero([1, 2, -3]) is True

# Generated at 2026-10-24 10:56:38.178176
# Unit test for function triples_sum_to_zero
def test_triples_sum_to_zero():
    # basic cases: triple exists
    assert module_0.triples_sum_to_zero([-1, 0, 1]) is True
    assert module_0.triples_sum_to_zero([1, 2, -3]) is True
    assert module_0.triples_sum_to_zero([-5, 1, 4]) is True

    # basic cases: no triple sums to zero
    assert module_0.triples_sum_to_zero([1, 2, 3]) is False
    assert module_0.triples_sum_to_zero([0, 1, 2]) is False
    assert module_0.triples_sum_to_zero([1, 1, 1]) is False

    # zeros
    assert module_0.triples_sum_to_zero([0, 0, 0]) is True
    assert module_0.triples_sum_to_zero([0, 0, 1]) is False
    assert module_0.triples_sum_to_zero([0, 0, 0, 1]) is True

    # duplicates, distinct indices required
    assert module_0.triples_sum_to_zero([2, -1, -1]) is True
    assert module_0.triples_sum_to_zero([1, 1, -2]) is True
    assert module_0.triples_sum_to_zero([-1, -1, 2]) is True

    # edge cases: fewer than 3 elements
    assert module_0.triples_sum_to_zero([]) is False
    assert module_0.triples_sum_to_zero([0]) is False
    assert module_0.triples_sum_to_zero([1, -1]) is False
    assert module_0.triples_sum_to_zero([0, 0]) is False

    # order should not matter
    assert module_0.triples_sum_to_zero([-3, 1, 2]) is True
    assert module_0.triples_sum_to_zero([1, 2, 3, -6]) is True

    # larger list, no triple
    assert module_0.triples_sum_to_zero([1, 2, 4, 8, 16]) is False

# Generated at 2026-10-24 10:56:53.854945
# Unit test for function triples_sum_to_zero
def test_triples_sum_to_zero():bash

# Generated at 2026-10-24 10:57:09.932832
# Unit test for function triples_sum_to_zero
def test_triples_sum_to_zero():
    assert module_0.triples_sum_to_zero([1, 3, 5, 0]) == True
    assert module_0.triples_sum_to_zero([1, 3, 5, -1]) == True
    assert module_0.triples_sum_to_zero([1, 3, -2, 1]) == True
    assert module_0.triples_sum_to_zero([1, 2, 3, 7]) == False
    assert module_0.triples_sum_to_zero([2, 4, -5, 3, 9, 7]) == False
    assert module_0.triples_sum_to_zero([1]) == False
    assert module_0.triples_sum_to_zero([0, 0, 0]) == True
    assert module_0.triples_sum_to_zero([]) == False

# Generated at 2026-10-24 10:57:11.271905
# Unit test for function triples_sum_to_zero
def test_triples_sum_to_zero():bash

# Generated at 2026-10-24 10:57:12.586632
# Unit test for function triples_sum_to_zero
def test_triples_sum_to_zero():
    assert module_0.triples_sum_to_zero([1, 3, 5, 0]) == True
    assert module_0.triples_sum_to_zero([1, 3, 5, -1]) == True
    assert module_0.triples_sum_to_zero([1, 3, -2, 1]) == True
    assert module_0.triples_sum_to_zero([1, 2, 3, 7]) == False
    assert module_0.triples_sum_to_zero([2, 4, -5, 3, 9, 7]) == False
    assert module_0.triples_sum_to_zero([1]) == False
    assert module_0.triples_sum_to_zero([0, 0, 0]) == True
    assert module_0.triples_sum_to_zero([]) == False

# Generated at 2026-10-24 10:57:13.916121
# Unit test for function triples_sum_to_zero
def test_triples_sum_to_zero():bash

# Generated at 2026-10-24 10:57:15.371541
# Unit test for function triples_sum_to_zero
def test_triples_sum_to_zero():
    assert module_0.triples_sum_to_zero([1, 3, 5, 0]) == True
    assert module_0.triples_sum_to_zero([1, 3, 5, -1]) == True
    assert module_0.triples_sum_to_zero([1, 3, -2, 1]) == True
    assert module_0.triples_sum_to_zero([1, 2, 3, 7]) == False
    assert module_0.triples_sum_to_zero([2, 4, -5, 3, 9, 7]) == False
    assert module_0.triples_sum_to_zero([1]) == False
    assert module_0.triples_sum_to_zero([0, 0, 0]) == True
    assert module_0.triples_sum_to_zero([]) == False

# Generated at 2026-10-24 10:57:16.807226
# Unit test for function triples_sum_to_zero
def test_triples_sum_to_zero():bash

# Generated at 2026-10-24 10:57:18.200352
# Unit test for function triples_sum_to_zero
def test_triples_sum_to_zero():
    assert module_0.triples_sum_to_zero([1, 3, 5, 0]) == True
    assert module_0.triples_sum_to_zero([1, 3, 5, -1]) == True
    assert module_0.triples_sum_to_zero([1, 3, -2, 1]) == True
    assert module_0.triples_sum_to_zero([1, 2, 3, 7]) == False
    assert module_0.triples_sum_to_zero([2, 4, -5, 3, 9, 7]) == False
    assert module_0.triples_sum_to_zero([1]) == False
    assert module_0.triples_sum_to_zero([0, 0, 0]) == True
    assert module_0.triples_sum_to_zero([]) == False

# Generated at 2026-10-24 10:57:19.527351
# Unit test for function triples_sum_to_zero
def test_triples_sum_to_zero():bash

# Generated at 2026-10-24 10:57:20.844523
# Unit test for function triples_sum_to_zero
def test_triples_sum_to_zero():
    assert module_0.triples_sum_to_zero([1, 3, 5, 0]) == True
    assert module_0.triples_sum_to_zero([1, 3, 5, -1]) == True
    assert module_0.triples_sum_to_zero([1, 3, -2, 1]) == True
    assert module_0.triples_sum_to_zero([1, 2, 3, 7]) == False
    assert module_0.triples_sum_to_zero([2, 4, -5, 3, 9, 7]) == False
    assert module_0.triples_sum_to_zero([1]) == False
    assert module_0.triples_sum_to_zero([0, 0, 0]) == True
    assert module_0.triples_sum_to_zero([]) == False

# Generated at 2026-10-24 10:57:22.149347
# Unit test for function triples_sum_to_zero
def test_triples_sum_to_zero():bash

# Generated at 2026-10-24 10:57:23.755695
# Unit test for function triples_sum_to_zero
def test_triples_sum_to_zero():
    assert module_0.triples_sum_to_zero([1, 3, 5, 0]) == True
    assert module_0.triples_sum_to_zero([1, 3, 5, -1]) == True
    assert module_0.triples_sum_to_zero([1, 3, -2, 1]) == True
    assert module_0.triples_sum_to_zero([1, 2, 3, 7]) == False
    assert module_0.triples_sum_to_zero([2, 4, -5, 3, 9, 7]) == False
    assert module_0.triples_sum_to_zero([1]) == False
    assert module_0.triples_sum_to_zero([0, 0, 0]) == True
    assert module_0.triples_sum_to_zero([]) == False

# Generated at 2026-10-24 10:57:25.066422
# Unit test for function triples_sum_to_zero
def test_triples_sum_to_zero():bash

# Generated at 2026-10-24 10:57:26.827270
# Unit test for function triples_sum_to_zero
def test_triples_sum_to_zero():
    assert module_0.triples_sum_to_zero([1, 3, 5, 0]) == True
    assert module_0.triples_sum_to_zero([1, 3, 5, -1]) == True
    assert module_0.triples_sum_to_zero([1, 3, -2, 1]) == True
    assert module_0.triples_sum_to_zero([1, 2, 3, 7]) == False
    assert module_0.triples_sum_to_zero([2, 4, -5, 3, 9, 7]) == False
    assert module_0.triples_sum_to_zero([1]) == False
    assert module_0.triples_sum_to_zero([0, 0, 0]) == True
    assert module_0.triples_sum_to_zero([]) == False