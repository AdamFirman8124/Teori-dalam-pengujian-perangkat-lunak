

# Generated at 2022-06-13 19:52:31.385864
# Unit test for function take
def test_take():
    assert list(take(0, range(100))) == []
    assert list(take(20, range(100))) == list(range(20))
    assert list(take(20, range(10))) == list(range(10))
    assert list(take(5, ())) == []
    assert list(take(0, ())) == []

# Generated at 2022-06-13 19:52:39.338697
# Unit test for function split_by
def test_split_by():
    assert list(split_by(["a", "b", "c", "d", "e", "f"], criterion=lambda x: x in ["d", "e"])) == \
           [["a", "b", "c"], ["f"]]

    assert list(split_by(["a", "b", "c", "d", "e", "f"], criterion=lambda x: x in ["d", "e"], empty_segments=True)) == \
           [["a", "b", "c"], [], ["f"]]

    assert list(split_by(["a", "b", "c", "d", "e", "f"], separator="d")) == [["a", "b", "c"], ["e", "f"]]


# Generated at 2022-06-13 19:52:45.536437
# Unit test for function split_by
def test_split_by():
    assert list(split_by(range(10), criterion=lambda x: x % 3 == 0)) == [[1, 2], [4, 5], [7, 8]]
    assert list(split_by(" Split by: ", empty_segments=True, separator='.')) == [[], ['S', 'p', 'l', 'i', 't'], ['b', 'y', ':'], []]

# Generated at 2022-06-13 19:52:51.325177
# Unit test for function take
def test_take():
    assert 0 == len(list(take(0, range(10))))
    assert 5 == len(list(take(5, range(5))))
    assert 5 == len(list(take(5, range(10))))
    assert 0 == len(list(take(5, range(0))))
    assert 0 == len(list(take(0, range(0))))



# Generated at 2022-06-13 19:52:59.182189
# Unit test for function split_by
def test_split_by():
    assert len(list(split_by(range(10), criterion=lambda x: x % 3 == 0))) == 3
    assert all(len(segment) in (2, 3) for segment in split_by(range(10), criterion=lambda x: x == 5))
    assert len(list(split_by(range(10), criterion=lambda x: x % 3 == 0, empty_segments=True))) == 3
    assert all(len(segment) in (2, 3) for segment in split_by(range(10), criterion=lambda x: x == 5, empty_segments=True))
    assert len(list(split_by(range(10), criterion=lambda x: x % 3 == 1, empty_segments=True))) == 4

# Generated at 2022-06-13 19:53:07.397839
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(0,10))) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x > 10, range(0,10))) == []
    assert list(drop_until(lambda x: x < 0, range(0,10))) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert list(drop_until(lambda x: x == -1, range(0,10))) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]



# Generated at 2022-06-13 19:53:18.149612
# Unit test for function split_by
def test_split_by():
    assert list(split_by(" Split by: ", empty_segments=True, separator='.')) == [[], ['S', 'p', 'l', 'i', 't'], ['b', 'y', ':'], []]
    assert list(split_by(" Split by: ", empty_segments=False, separator='.')) == [['S', 'p', 'l', 'i', 't'], ['b', 'y', ':']]
    
    assert list(split_by(range(10), criterion=lambda x: x % 3 == 0)) == [[1, 2], [4, 5], [7, 8]]

# Generated at 2022-06-13 19:53:27.468703
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    assert MapList(lambda x: x * x, [1, 2, 3])[0] == 1
    assert MapList(lambda x: x * x, [1, 2, 3])[2] == 9
    assert MapList(lambda x: x * x, [1, 2, 3])[-1] == 9
    assert MapList(lambda x: x * x, [1, 2, 3])[1:3] == [4, 9]


# Generated at 2022-06-13 19:53:35.256736
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    class TestHelper:
        @staticmethod
        def test_case(input_range: Range, input_idx: int, expect_output: int):
            assert input_range[input_idx] == expect_output

    t = TestHelper
    t.test_case(Range(1, 10, 2), 0, 1)
    t.test_case(Range(1, 10, 2), 3, 7)
    t.test_case(Range(1, 10, 2), -1, 9)
    t.test_case(Range(1, 10, 2), -4, 5)

# Generated at 2022-06-13 19:53:39.619044
# Unit test for method __iter__ of class LazyList
def test_LazyList___iter__():
    iterable = range(100000)
    lazy_iterable = LazyList(iterable)
    assert list(iterable[50000:]) == list(lazy_iterable[50000:])



# Generated at 2022-06-13 19:54:05.026697
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x > 0, range(10))) == range(1, 10)
    assert list(drop_until(lambda x: x > 10, range(10))) == []



# Generated at 2022-06-13 19:54:08.268144
# Unit test for method __iter__ of class LazyList
def test_LazyList___iter__():
    lz = LazyList(range(10))
    assert [i for i in lz] == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]



# Generated at 2022-06-13 19:54:15.529087
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    map = MapList(lambda x: x * x, [1, 2, 3, 4, 5])
    assert map[1] == map[1]
    assert map[slice(1, 5, 2)] == [1, 9, 25]
    assert map[Range(1, 5, 2)] == [1, 9, 25]
    assert list(MapList(lambda x: x, Range(5))) == [0, 1, 2, 3, 4]

# Generated at 2022-06-13 19:54:16.897086
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    assert MapList(lambda x: x, [1, 2, 3])[1] == 2

# Generated at 2022-06-13 19:54:26.245487
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x < 5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert list(drop_until(lambda x: x > 100, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])) == []

# Generated at 2022-06-13 19:54:29.918651
# Unit test for function drop
def test_drop():
    assert list(drop(5, range(1000000)))[0] == 5
    assert list(drop(0, range(1000)))[0] == 0



# Generated at 2022-06-13 19:54:40.012818
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(-5,5)
    assert(r._get_idx(0) == -5)
    assert(r._get_idx(-1) == -1)
    assert(r._get_idx(-2) == -3)
    assert(r._get_idx(-3) == -5)
    assert(r._get_idx(0) == -5)
    assert(r._get_idx(1) == -3)
    assert(r._get_idx(2) == -1)
    assert(r._get_idx(3) == 1)
    assert(r._get_idx(4) == 3)
    assert(r._get_idx(5) == 5)
    assert(r._get_idx(6) == 5)


# Generated at 2022-06-13 19:54:44.450172
# Unit test for function drop
def test_drop():
    assert list(drop(5, range(10))) == list(range(5, 10))
    assert list(drop(5, range(5))) == []
    assert list(drop(0, range(10))) == list(range(10))

# Generated at 2022-06-13 19:54:47.412302
# Unit test for method __iter__ of class LazyList
def test_LazyList___iter__():
    from typing import List
    assert list(iter(LazyList(range(5)))) == [0, 1, 2, 3, 4]


# Generated at 2022-06-13 19:54:52.075107
# Unit test for function drop
def test_drop():
    assert list(drop(1, range(2))) == [1]
    assert list(drop(100, [])) == []
    assert list(drop(100, range(2))) == []
    assert list(drop(100, [0])) == []



# Generated at 2022-06-13 19:55:08.726560
# Unit test for function drop_until
def test_drop_until():
    # invoke function drop_until
    result = drop_until(lambda x: x > 5, range(10))
    # assert that the output is as expected
    assert result == [6, 7, 8, 9]
# run unit test 
test_drop_until()


# Generated at 2022-06-13 19:55:18.431416
# Unit test for function split_by
def test_split_by():
    assert list(split_by("Split.by.:", criterion=lambda x: x in ".:")) == [['S', 'p', 'l', 'i', 't'], ['b', 'y']]
    assert list(split_by("Split.by.:", empty_segments=True, criterion=lambda x: x in ".:")) == [['S', 'p', 'l', 'i', 't'], [], ['b', 'y'], []]
    assert list(split_by("Split.by.:", empty_segments=True, separator='.')) == [[], ['S', 'p', 'l', 'i', 't'], ['b', 'y', ':'], []]

# Generated at 2022-06-13 19:55:29.635550
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r1 = Range(1, 2)
    assert r1[0] == 1
    assert_raises(IndexError, lambda: r1[1])
    r2 = Range(1, 11, 2)
    assert r2[0] == 1
    assert r2[2] == 5
    assert r2[-1] == 9
    assert_raises(IndexError, lambda: r2[3])
    assert r2[-1:] == [9]
    assert r2[-2:] == [7, 9]
    assert r2[:2] == [1, 3]
    assert r2[:1:2] == [1]
    assert r2[::2] == [1, 5, 9]
    assert r2[::-1] == [9, 7, 5, 3, 1]
    assert r

# Generated at 2022-06-13 19:55:33.251792
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():

    l = list(range(-100, 100))
    print(l)

    r = Range(-100, 100)
    print(list(r))
    print(r[-1], r[-2], r[2], r[-100], r[99])

    print(r[0:99])
    print(r[-100:99])
    print(r[-100:-99])
    print(r[100:3])
    print(r[100:101])


test_Range___getitem__()


# Generated at 2022-06-13 19:55:37.271304
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
  # test with single index
  range1 = Range(0, 5)
  assert range1[2] == 2
  # test with slice
  range1 = Range(3, 10)
  assert range1[2:6] == [5, 6, 7, 8]
test_Range___getitem__()

# Generated at 2022-06-13 19:55:46.744472
# Unit test for function scanl
def test_scanl():
    assert list(scanl(lambda s, x: x + s, ['a', 'b', 'c', 'd'])) == ['a', 'ba', 'cba', 'dcba']
    assert list(scanl(lambda s, x: x + s, ['a', 'b', 'c', 'd'], 'z')) == ['z', 'za', 'zba', 'zcba', 'zdcba']
    assert list(scanl(lambda s, x: s * x, [2, 3, 5, 7])) == [2, 6, 30, 210]



# Generated at 2022-06-13 19:55:57.319367
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(10)
    for i in range(10):
        assert r[i] == i
        assert r[-i - 1] == -i - 1 + 10
    with pytest.raises(IndexError):
        r[10]
    with pytest.raises(IndexError):
        r[-11]
    
    r = Range(1, 10 + 1)
    for i in range(1, 10 + 1):
        assert r[i - 1] == i
        assert r[-i] == -i + 10
    with pytest.raises(IndexError):
        r[10]
    with pytest.raises(IndexError):
        r[-10 - 1]
    
    r = Range(1, 11, 2)

# Generated at 2022-06-13 19:56:05.337214
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda n: n>=5, range(10))) == [5,6,7,8,9]
    assert list(drop_until(lambda n: n>5, range(10))) == [6,7,8,9]
    assert list(drop_until(lambda n: n>1, range(10))) == [2,3,4,5,6,7,8,9]
    assert list(drop_until(lambda n: n>0, range(10))) == [1,2,3,4,5,6,7,8,9]
    assert list(drop_until(lambda n: n>0, range(1))) == []
    assert list(drop_until(lambda n: n>0, range(0))) == []

# Generated at 2022-06-13 19:56:10.634612
# Unit test for function drop_until
def test_drop_until():
    # (1) drop_until with normal sequence
    assert list(drop_until(lambda x: x > 3, range(10))) == [4, 5, 6, 7, 8, 9]
    # (2) drop_until with empty sequence
    assert list(drop_until(lambda x: True, range(0))) == []



# Generated at 2022-06-13 19:56:14.478741
# Unit test for function drop_until
def test_drop_until():
    assert drop_until(lambda x: x>5,range(10))==(6,7,8,9)
    assert drop_until(lambda x: x>'hello',['hello','world'])==('world',)
# Test cases
for i in test_drop_until():
    print(i)


# Generated at 2022-06-13 19:56:43.220048
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]



# Generated at 2022-06-13 19:56:51.592387
# Unit test for function split_by
def test_split_by():
    assert list(split_by(range(10), criterion=lambda x: x % 3 == 0)) == [[1, 2], [4, 5], [7, 8]]
    assert list(split_by(" Split by: ", empty_segments=True, criterion=lambda x: x == '.')) == [[], ['S', 'p', 'l', 'i', 't'], ['b', 'y', ':'], []]
    assert list(split_by(" Split by: ", empty_segments=True, criterion=lambda x: x == '.')) == [[], ['S', 'p', 'l', 'i', 't'], ['b', 'y', ':'], []]

# Generated at 2022-06-13 19:56:57.821882
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    a = list(range(0, 10))
    b = list(Range(0, 10))
    assert a == b
    assert Range(0, 10)[0] == range(0, 10)[0]
    assert Range(0, 10)[9] == range(0, 10)[9]
    assert Range(0, 10)[-1] == range(0, 10)[-1]
    assert Range(0, 10)[-10] == range(0, 10)[-10]
    assert Range(0, 10)[2:4] == range(0, 10)[2:4]
    assert Range(0, 10)[-3:-1] == range(0, 10)[-3:-1]
    assert Range(0, 10)[-3:3] == range(0, 10)[-3:3]

# Generated at 2022-06-13 19:57:00.528161
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]


# Generated at 2022-06-13 19:57:05.162148
# Unit test for function drop_until
def test_drop_until():
    from random import random

    seq = [random() for _ in range(100)]
    test_seq = drop_until(lambda x: x>0.5, seq)

    for i in test_seq:
        assert i > 0.5




# Generated at 2022-06-13 19:57:07.247205
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]



# Generated at 2022-06-13 19:57:08.344889
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]


# Generated at 2022-06-13 19:57:13.028574
# Unit test for function drop_until
def test_drop_until():
    def is_negative(x):
        return x < 0
    assert list(drop_until(is_negative, [0, -1, 2, -3, 4, 5])) == [-1, 2, -3, 4, 5]



# Generated at 2022-06-13 19:57:14.920617
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    for item in range(-10, 10):
        assert list(Range(1, item + 1))[item] == item + 1



# Generated at 2022-06-13 19:57:27.588516
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    range1 = Range(0, 10, 2)
    print(range1[0]) # should be 0
    print(range1[1]) # should be 2
    print(range1[2]) # should be 4
    print(range1[3]) # should be 6
    print(range1[4]) # should be 8

    range1 = Range(10)
    print(range1[0]) # should be 0
    print(range1[1]) # should be 1
    print(range1[9]) # should be 9
    print(range1[-1]) # should be 9
    print(range1[-2]) # should be 8

    range1 = Range(1, 11, 2)
    print(range1[0]) # should be 1
    print(range1[1]) # should be 3

# Generated at 2022-06-13 19:58:00.735467
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    a = Range(5,5)
    a[1]
    b = Range(5)
    b[2]
    c = Range(3,5)
    c[2]
    d = Range(6,10,3)
    d[0]
    d[1]
    d[2]
    d[0:2]


# Generated at 2022-06-13 19:58:06.765905
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():

    r = Range(3)
    assert r[0] == 0
    assert r[1] == 1
    assert r[2] == 2
    assert r[slice(0, 3)] == [0, 1, 2]
    err = None
    try:
        r[3]
    except IndexError as e:
        err = e
    assert err is not None
    assert err.args[0] == "Range index out of range"
    print("passed")


# Generated at 2022-06-13 19:58:09.276191
# Unit test for function drop_until
def test_drop_until():
    assert_equal(list(drop_until(lambda x: x > 2, range(10))), list(range(3, 10)))



# Generated at 2022-06-13 19:58:15.850893
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x > 5, [])) == []
    assert list(drop_until(lambda x: x > 5, [6])) == [6]
    assert list(drop_until(lambda x: x > 5, [6, 7, 8, 9])) == [6, 7, 8, 9]



# Generated at 2022-06-13 19:58:19.139111
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(10)
    assert(r[0] == 0)
    assert(r[9] == 9)

# Generated at 2022-06-13 19:58:20.000794
# Unit test for method __getitem__ of class Range

# Generated at 2022-06-13 19:58:28.299979
# Unit test for function drop_until
def test_drop_until():
    a = list(range(0, 10))
    assert list(drop_until(lambda x: x > 5, a)) == list(range(6, 10))
    assert list(take(3, drop_until(lambda x: x > 5, a))) == list(range(6, 9))
    assert list(drop_until(lambda x: x > 5, [])) == []



# Generated at 2022-06-13 19:58:40.652223
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(10)
    assert r[0] == 0
    assert r[2] == 2
    assert r[4] == 4
    try:
        r[10]
    except IndexError:
        pass
    else:
        raise AssertionError()
    try:
        r[11]
    except IndexError:
        pass
    else:
        raise AssertionError()

    r = Range(1, 11, 2)
    assert r[0] == 1
    assert r[2] == 5
    assert r[4] == 9
    try:
        r[5]
    except IndexError:
        pass
    else:
        raise AssertionError()

    assert r[0:5] == [1, 3, 5, 7, 9]

# Generated at 2022-06-13 19:58:51.850652
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 2, [1, 2, 3, 4])) == [3, 4]
    assert list(drop_until(lambda x: x > 3, [1, 2, 3, 4])) == [4]
    assert list(drop_until(lambda x: x > 4, [1, 2, 3, 4])) == []
    assert list(drop_until(lambda x: x > 5, [1, 2, 3, 4])) == []



# Generated at 2022-06-13 19:59:02.893592
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    data = [1, 2, 3, 5, 6, 7, 9, 10, 11, 13, 14, 15, 17, 18, 19]
    idx = [3, 2, 4, 9, 11, 13]
    r = Range(1, 20, 2)
    for i, ri in zip(idx, r):
        assert ri == data[i]
    assert list(r[2:4]) == data[2:4]
    assert tuple(r[1:6]) == tuple(data[1:6])
    assert list(r[::3]) == data[::3]
    assert list(r[1:6:2]) == data[1:6:2]
    assert list(r[:6:2]) == data[:6:2]

# Generated at 2022-06-13 19:59:16.199090
# Unit test for function drop_until
def test_drop_until():
    assert (list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9])




# Generated at 2022-06-13 19:59:22.697634
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, [1, 2, 3, 4, 5, 6, 7])) == [6, 7]
    assert list(drop_until(lambda x: False, [1, 2, 3, 4, 5])) == [1, 2, 3, 4, 5]
    assert list(drop_until(lambda x: x > 5, [])) == []
    assert list(drop_until(lambda x: True, [])) == []



# Generated at 2022-06-13 19:59:30.885498
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    global tt_Range
    tt_Range = Range(1, 5 + 1)  # (start, end)
    assert tt_Range[2] == 3
    assert tt_Range[-2] == 4
    assert tt_Range[2:5] == [3, 4, 5]
    assert tt_Range[2:] == [3, 4, 5]
    assert tt_Range[:-2] == [1, 2, 3]
    assert tt_Range[2:5:2] == [3, 5]


# Generated at 2022-06-13 19:59:41.295573
# Unit test for function drop_until
def test_drop_until():
    assert not bool(list(drop_until(lambda x: x > 5, range(0, 2))))
    assert bool(list(drop_until(lambda x: x > 5, range(0, 7))))
    assert bool(list(drop_until(lambda x: x > 5, range(0, 10))))
    assert not bool(list(drop_until(lambda x: x > 5, range(0, 101))))
    assert bool(list(drop_until(lambda x: x > 5, range(0, 1000))))
    assert bool(list(drop_until(lambda x: x > 5, range(0, 10000))))
    assert bool(list(drop_until(lambda x: x > 5, range(0, 100000))))
    assert bool(list(drop_until(lambda x: x > 5, range(0, 1000000))))



# Generated at 2022-06-13 19:59:43.462091
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(3)
    assert(r[0] == 0 and r[1] == 1 and r[2] == 2)



# Generated at 2022-06-13 19:59:50.706646
# Unit test for function drop_until
def test_drop_until():
    assert (list(drop_until(lambda x:x > 5, range(10))) == [6, 7, 8, 9])
    assert (list(drop_until(lambda x:x == 5, range(10))) == [5,6,7,8,9])
    assert (list(drop_until(lambda x:x < 5, range(10))) == [0,1,2,3,4,5,6,7,8,9])
test_drop_until()


# Generated at 2022-06-13 19:59:54.572417
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x > 5, [])) == []



# Generated at 2022-06-13 19:59:57.215110
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(1, 20, 2)
    assert r[3] == 7
    assert r[slice(0, -1, 2)] == [1, 7, 13]



# Generated at 2022-06-13 20:00:06.659517
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    from random import randint
    from copy import deepcopy
    from random import choice
    r = Range(randint(10, 20))
    for _ in range(10):
        idx1 = randint(0, r.__len__() - 1)
        assert (r[idx1] == r.__getitem__(idx1))
    c = randint(1, 5)
    l = list(range(r.__len__()))
    s = choice(l)
    e = choice(l)
    if (s > e):
        s, e = e, s
    assert (r[s:(e + 1)] == r.__getitem__(slice(s, (e + 1))))


# Generated at 2022-06-13 20:00:16.192469
# Unit test for function drop_until
def test_drop_until():
    # Tests that the function does not immediately raise StopIteration
    list(drop_until(lambda x: x > 1, [1]))

    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
    
    assert list(drop_until(lambda x: x > 1, [1, 1, 1, 1, 1, 1, 2, 3, 4])) == [2, 3, 4]
    
    # Tests that the function handles an empty iterable
    assert list(drop_until(lambda x: x > 1, [])) == []



# Generated at 2022-06-13 20:00:31.873312
# Unit test for function drop_until
def test_drop_until():
    # 简单使用
    assert list(drop_until(lambda x: x>5, range(10))) == [6,7,8,9]
    # iterable为空的情况
    assert list(drop_until(lambda x: x>50, [])) == []
    # 保证首个满足predicate的元素被返回
    assert list(drop_until(lambda x: x>5, range(10)))[0] == 6



# Generated at 2022-06-13 20:00:42.936329
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    assert Range(1, 1)[0] == 1
    assert Range(2, 3)[0] == 2
    assert Range(3, 4)[0] == 3
    assert Range(4, 5)[0] == 4
    assert Range(5, 6)[0] == 5
    assert Range(6, 7)[0] == 6
    assert Range(1, 1)[0] == 1
    assert Range(2, 3)[1] == 3
    assert Range(3, 4)[1] == 4
    assert Range(4, 5)[1] == 5
    assert Range(5, 6)[1] == 6
    assert Range(6, 7)[1] == 7
    assert Range(7, 8)[1] == 8
    assert Range(1, 1)[0] == 1
    assert Range(2, 3)[2] == 3

# Generated at 2022-06-13 20:00:48.343764
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(5)
    assert r[0] == 0
    assert r[2] == 2
    assert r[4] == 4
    r = Range(3, 10)
    assert r[0] == 3
    assert r[2] == 5
    assert r[6] == 9
    r = Range(1, 10 + 1, 2)
    assert r[0] == 1
    assert r[2] == 5
    assert r[4] == 9



# Generated at 2022-06-13 20:00:59.272001
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    assert Range(10)[:] == list(range(10))
    assert Range(10)[1:5] == list(range(1, 5))
    assert Range(10)[2:5:2] == list(range(2, 5, 2))

    assert Range(10)[0] == 0
    assert Range(10)[-1] == 9
    assert Range(10)[0:5][-1] == 4

    assert Range(0, 4, 2)[0] == 0
    assert Range(0, 4, 2)[-1] == 2

    segment = Range(0, 100, 5)[10:20:2]
    assert len(segment) == 5
    assert segment[0] == 50
    assert segment[1] == 55
    assert segment[2] == 60
    assert segment[3] == 65
    assert segment[4]

# Generated at 2022-06-13 20:01:02.939811
# Unit test for function drop_until
def test_drop_until():
    fn = lambda x: x > 5
    def _test(pred_fn, data):
        actual = list(drop_until(pred_fn, data))
        print(actual)

    data = range(1, 11)
    _test(fn, data)



# Generated at 2022-06-13 20:01:11.296407
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x == 5, range(10))) == [5, 6, 7, 8, 9]
    assert list(drop_until(lambda x: x == 5, range(10, 0, -1))) == [5, 4, 3, 2, 1]
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x < 5, range(10, 0, -1))) == [10, 9, 8, 7, 6]
    assert list(drop_until(lambda x: False, range(10))) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Generated at 2022-06-13 20:01:13.435408
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(1, 11, 2)
    print(r[-1])
    print(r[0], r[2], r[4])
    return


# Generated at 2022-06-13 20:01:20.440629
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(10)
    assert r[2] == 2
    assert r[-3] == 7
    assert r[:5] == [0, 1, 2, 3, 4]
    assert r[3::2] == [3, 5, 7, 9]
    assert r[1:-1] == [1, 2, 3, 4, 5, 6, 7, 8]
    assert r[1:-1:2] == [1, 3, 5, 7]



# Generated at 2022-06-13 20:01:25.872080
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6,7,8,9]
    assert list(drop_until(lambda x: x > 5, range(0))) == []
    assert list(drop_until(lambda x: x > -1, range(10))) == []
    assert list(drop_until(lambda x: x > 5, [])) == []

# del test_drop_until


# Generated at 2022-06-13 20:01:32.891768
# Unit test for function split_by
def test_split_by():
    assert list(split_by(range(10), criterion=lambda x: x % 3 == 0)) == [[1, 2], [4, 5], [7, 8]]
    assert list(split_by("Split by: ", empty_segments=True, separator='.')) == [[], ['S', 'p', 'l', 'i', 't'],
                                                                                 ['b', 'y', ':'], []]



# Generated at 2022-06-13 20:01:40.478287
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
test_drop_until()



# Generated at 2022-06-13 20:01:49.681121
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    keys = [0, 1, -1, slice(0, 10, 2), slice(None, None, 2), slice(-1, None, 2), slice(-1, 1, 2)]
    expected_values = [[0], [1], [9], [0, 2, 4, 6, 8], [0, 2, 4, 6, 8], [0, 2, 4, 6, 8], [8]]
    range = Range(10)
    for key, expected_value in zip(keys, expected_values):
        assert range[key] == expected_value
    # check that Range works as intended
    for key, expected_value in zip(keys, expected_values):
        assert range[key] == expected_value

# Generated at 2022-06-13 20:01:56.172466
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x > 5, [1, 2, 0, 3, 4, 5, 6, 7, 8, 9])) == [6, 7, 8, 9]



# Generated at 2022-06-13 20:02:01.060803
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(0, 10)
    assert isinstance(r[0], int)
    assert isinstance(r[1], int)
    assert isinstance(r[0:3], list)
    assert isinstance(r[0:-1], list)



# Generated at 2022-06-13 20:02:13.366130
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(0,10,2)
    assert r[1] == 2
    assert all([x==y for x,y in zip(r[:], range(0,10,2))])
    r = Range(3, 7)
    assert all([x==y for x,y in zip(r[2:], range(5,7))])
    assert all([x==y for x,y in zip(r[:2], range(3,5))])
    assert all([x==y for x,y in zip(r[1::-1], range(4,2,-1))])
    assert all([x==y for x,y in zip(r[3:1:-1], range(6,4,-1))])