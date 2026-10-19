

# Generated at 2022-06-13 19:52:36.581197
# Unit test for function drop
def test_drop():
    assert sum(take(10000, drop(5, range(1000000)))) == 49995000



# Generated at 2022-06-13 19:52:39.932333
# Unit test for method __len__ of class LazyList
def test_LazyList___len__():
    from nose.tools import assert_raises
    foo = LazyList([0, 1, 2, 3, 4])
    assert_raises(TypeError, len, foo)
    list(foo)
    assert len(foo) == 5
    assert len(LazyList(range(4))) == 4
    assert len(LazyList(range(1000000))) == 1000000



# Generated at 2022-06-13 19:52:42.517947
# Unit test for function drop_until
def test_drop_until():
    a = list(drop_until(lambda x: x > 5, range(10)))
    assert a == [6, 7, 8, 9]


# Generated at 2022-06-13 19:52:53.894215
# Unit test for function split_by
def test_split_by():
    assert list(split_by("", empty_segments=True)) == [[]]
    assert list(split_by(" ", empty_segments=True)) == [[' ']]
    assert list(split_by("", empty_segments=False)) == []
    assert list(split_by(" ", empty_segments=False)) == []
    assert list(split_by("a", empty_segments=True)) == [['a']]
    assert list(split_by("a", empty_segments=False)) == [['a']]
    assert list(split_by("a a", empty_segments=True)) == [['a'], ['a']]
    assert list(split_by("a a", empty_segments=False)) == [['a', 'a']]

# Generated at 2022-06-13 19:53:03.877279
# Unit test for function drop_until
def test_drop_until():
    def test(iterable, pred_fn):
        print('drop_until({}, {})'.format(iterable, pred_fn))
        filtered_iter = drop_until(pred_fn, iterable)
        print(type(filtered_iter))
        for item in filtered_iter:
            print(item)
        print()

    test(range(10), lambda x: x > 5)
    print('-' * 100)
    test(range(10), lambda x: x > 0)
    print('-' * 100)
    test(range(10), lambda x: x > 10)

test_drop_until()


# Generated at 2022-06-13 19:53:11.871323
# Unit test for function chunk
def test_chunk():
    assert list(chunk(3, range(10))) == [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]
    assert list(chunk(3, range(9))) == [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    assert list(chunk(3, range(8))) == [[0, 1, 2], [3, 4, 5], [6, 7]]
    assert list(chunk(3, range(7))) == [[0, 1, 2], [3, 4, 5], [6]]
    assert list(chunk(3, range(6))) == [[0, 1, 2], [3, 4, 5]]
    assert list(chunk(3, range(5))) == [[0, 1, 2], [3, 4]]

# Generated at 2022-06-13 19:53:21.063795
# Unit test for function split_by
def test_split_by():
    assert list(split_by(range(10), criterion=lambda x: x % 3 == 0)) \
        == [[1, 2], [4, 5], [7, 8]]
    assert list(split_by(" Split by: ", empty_segments=True, separator='.')) \
        == [[], ['S', 'p', 'l', 'i', 't'], ['b', 'y', ':'], []]
    # Test invalid usage
    try:
        split_by([], criterion=None, separator=None)
        assert False
    except ValueError:
        pass
    try:
        split_by([], criterion=lambda x: x, separator='.')
        assert False
    except ValueError:
        pass

# Generated at 2022-06-13 19:53:27.793712
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    assert isinstance(MapList(lambda x: x, [])[0], int) == True
    assert MapList(lambda x: x, [])[0 : 0] == []
    assert isinstance(MapList(lambda x: x, [])[None], int) == True
    assert MapList(lambda x: x, [])[None : 0] == []


# Generated at 2022-06-13 19:53:33.118267
# Unit test for function split_by
def test_split_by():
    assert list(split_by(range(10), criterion=lambda x: x % 3 == 0)) == [[1, 2], [4, 5], [7, 8]]
    assert list(split_by(" Split by: ", empty_segments=True, separator='.')) == [[], ['S', 'p', 'l', 'i', 't'], ['b', 'y', ':'], []]


# Generated at 2022-06-13 19:53:40.252264
# Unit test for function drop
def test_drop():
    c = drop(1,range(10))
    print(type(c))
    print(type(range(10)))
    print(type(c))
    a = next(c)
    print(a)
    print(type(c))
    a = next(c)
    print(a)
    print(type(c))


# Generated at 2022-06-13 19:54:01.279307
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    if config.debug:
        m = MapList(lambda x: 2 * x, [1, 2, 3])
        assert m[0] == 2
        assert m[1] == 4
        assert m[2] == 6
        assert m[-1] == 6

        assert m[0:2] == [2, 4]
        assert m[1:3] == [4, 6]
        assert m[-3:-1] == [4, 6]



# Generated at 2022-06-13 19:54:07.723246
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(5)
    assert r[0] == 0
    assert r[1] == 1
    assert r[2] == 2
    assert r[3] == 3
    assert r[4] == 4
    try:
        r[5]
    except IndexError:
        pass
    else:
        raise AssertionError
    try:
        r[-1]
    except IndexError:
        pass
    else:
        raise AssertionError
    r = Range(1, 5)
    assert r[0] == 1
    assert r[1] == 2
    assert r[2] == 3
    assert r[3] == 4
    try:
        r[4]
    except IndexError:
        pass
    else:
        raise AssertionError

# Generated at 2022-06-13 19:54:11.853857
# Unit test for function drop_until
def test_drop_until():
    assert(list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9])
test_drop_until()



# Generated at 2022-06-13 19:54:15.313436
# Unit test for function drop
def test_drop():
    assert list(drop(3, range(10))) == list(range(3, 10))
    assert list(drop(0, range(10))) == list(range(10))
    assert list(drop(10, range(10))) == []



# Generated at 2022-06-13 19:54:25.060914
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x > 0, range(5))) == [1, 2, 3, 4]
    assert list(drop_until(lambda x: x > 5, [0, 1, 2, 3, 4, 5, 5, 5, 6])) == [6, 5, 5, 6]
    assert list(drop_until(lambda x: x == 7, [0, 1, 2, 3, 4, 5, 6])) == []
    assert list(drop_until(lambda x: True, [0, 1, 2, 3, 4, 5, 6])) == [0, 1, 2, 3, 4, 5, 6]

# Generated at 2022-06-13 19:54:29.656029
# Unit test for function drop_until
def test_drop_until():
    for t in range(4):
        for i in range(8):
            assert list(drop_until(lambda x: x > t, range(8))) == list(range(i, 8))[i:]

test_drop_until()



# Generated at 2022-06-13 19:54:32.163039
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x>5, range(10))) == [6,7,8,9]
    assert list(drop_until(lambda x: x > 5, range(5))) == []
    assert list(drop_until(lambda x: x > 5, range(6))) == [6]


# Generated at 2022-06-13 19:54:41.075586
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x > 10, range(10))) == []
    assert list(drop_until(lambda x: x > 0, range(10))) == [0,1,2,3,4,5,6,7,8,9]
    assert list(drop_until(lambda x: False, range(10))) == [0,1,2,3,4,5,6,7,8,9]
    assert list(drop_until(lambda x: True, range(10))) == [0,1,2,3,4,5,6,7,8,9]
    assert list(drop_until(lambda x: x > 10, [])) == []

# Generated at 2022-06-13 19:54:51.571523
# Unit test for function scanl
def test_scanl():
    test_data = [(0, []), ([], [0]), ([0], [0]), ([0, 1, 3, 6, 10], [1, 2, 3, 4]),
                 ([0, 1, 3, 6, 10], ["a", "b", "c", "d"])]
    for expected, input in test_data:
        try:
            result = list(scanl(operator.add, input, 0))
            assert result == expected
        except:
            print("\n" + "*" * 80)
            print(f"Unexpected error for scanl(operator.add, {input}, 0):\n")
            raise

test_scanl()



# Generated at 2022-06-13 19:54:57.320220
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x % 4 == 0, range(13))) == [4, 5, 6, 7, 8, 9, 10, 11, 12]
    assert list(drop_until(lambda x: x > 0, range(3))) == [1, 2]
    assert list(drop_until(lambda x: x > 3, range(3))) == []



# Generated at 2022-06-13 19:55:09.464095
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    from .test_lib import test_equal

    test_equal([], list(LazyList(range(0)).__getitem__(0)))
    test_equal([], list(LazyList(range(0)).__getitem__(slice(0, 0))))

    test_equal([], list(LazyList(range(1)).__getitem__(0)))
    test_equal([], list(LazyList(range(1)).__getitem__(slice(0, 0))))

    test_equal([1], list(LazyList(range(1)).__getitem__(slice(0, 1))))
    test_equal([0], list(LazyList(range(1)).__getitem__(slice(0, 1, None))))


# Generated at 2022-06-13 19:55:14.093882
# Unit test for function drop_until
def test_drop_until():
    lst = list(range(20))
    # lst = list(drop_until(lambda x: x > 5, lst))
    # assert drop_until()
    assert list(drop_until(lambda x: x > 5, lst)) == list(range(6,20))



# Generated at 2022-06-13 19:55:21.839951
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    def test(lst: LazyList[int], idx):
        try:
            assert lst[idx] == lst.list[idx]
        except IndexError:
            assert idx < 0 or idx >= len(lst.list)

    from random import randint

    lst = LazyList(range(1000))
    test(lst, -1)
    for i in range(1000):
        test(lst, randint(-2, 999))
    test(lst, 1001)

    lst = LazyList(range(1000))
    for i in range(1000):
        test(lst, slice(0, i))
        test(lst, slice(i, 1000))
        test(lst, slice(i, i + 1))



# Generated at 2022-06-13 19:55:28.546981
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    import bisect
    a = [1, 2, 3, 4, 5]
    pos = bisect.bisect_left(MapList(lambda x: x * x, a), 10)
    b = [2, 3, 4, 5, 6]
    pos = bisect.bisect_left(MapList(lambda i: a[i] * b[i], Range(len(a))), 10)

# Generated at 2022-06-13 19:55:37.122497
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    print (Range(2, 3, 1))
    print (Range(0, 10, 2))
    print (Range(-3, -3))
    print (Range(-3, 3))
    print (Range(3, -3))
    print (Range(2, 3, 4))
    print (Range(3, -3, -4))
    print (Range(3, -3, 4))
    print (Range(-3, 3, -4))
    print (Range(-3, 3, 4))
    print (Range(-3, 3, 0))


# Generated at 2022-06-13 19:55:43.590953
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x>5, range(10))) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x>5, iter([0, 1, 2]))) == []
    assert list(drop_until(lambda x: x < 0, iter([1, -1]))) == [-1]

# Generated at 2022-06-13 19:55:48.597696
# Unit test for function drop_until
def test_drop_until():
    l = range(10)
    l1 = drop_until(lambda x: x > 5, l)
    assert list(l1) == [6, 7, 8, 9]
    l1 = drop_until(lambda x: x > 10, l)
    assert list(l1) == []


# Generated at 2022-06-13 19:55:52.720576
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    # Test with isinstance(item, slice):
    # Test item is a slice
    assert list(Range(10)[0:2]) == [0, 1]
    # Test item is not a slice
    assert Range(10)[2] == 2

# Generated at 2022-06-13 19:56:02.619606
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 1, count(0))) == list(range(2, sys.maxsize))
    assert list(drop_until(lambda x: x > 1, count(0, 2))) == list(range(2, sys.maxsize, 2))
    assert list(drop_until(lambda x: False, count(0))) == list(range(sys.maxsize))
    assert list(drop_until(lambda x: False, count(0, 2))) == list(range(0, sys.maxsize, 2))
    assert list(drop_until(lambda x: True, count(0))) == list(range(sys.maxsize))
    assert list(drop_until(lambda x: True, count(0, 2))) == list(range(0, sys.maxsize, 2))



# Generated at 2022-06-13 19:56:06.123309
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    with pytest.raises(TypeError):
        MapList(lambda x: x, [1, 2, 3])[1.0]

# Generated at 2022-06-13 19:56:19.406400
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    lazy_list = LazyList(range(5))
    assert lazy_list[0] == 0
    assert lazy_list[1] == 1
    assert lazy_list[:5] == [0, 1, 2, 3, 4]
    assert lazy_list[0] == 0
    assert lazy_list[:2] == [0, 1]
    assert lazy_list[:] == [0, 1, 2, 3, 4]
    assert lazy_list[2] == 2
    with pytest.raises(TypeError):
        assert len(lazy_list)
    assert len(lazy_list[:]) == 5
    with pytest.raises(StopIteration):
        lazy_list[5]
    with pytest.raises(TypeError):
        len(lazy_list)

# Generated at 2022-06-13 19:56:23.133040
# Unit test for function drop_until
def test_drop_until():
    for i in range(10):
        assert list(drop_until(lambda x: x > 5, range(10))) == list(range(6, 10))
        assert list(drop_until(lambda x: x > 5, reversed(range(10)))) == list(reversed(range(5, 10)))



# Generated at 2022-06-13 19:56:26.031013
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    a = MapList(lambda x: x * x, [1, 2, 3, 4, 5])
    assert a[0] == 1
    assert a[-1] == 25
    assert a[2:4] == [9, 16]


# Generated at 2022-06-13 19:56:35.390818
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    data_set = ['a', 'b', 'c', 'd', 'e']
    data_iter = iter(data_set)
  
    ll = LazyList(data_iter)
    assert len(ll) == 5
    assert ll[0] == 'a'
    assert ll[1] == 'b'
    assert ll[3] == 'd'
    assert ll[2] == 'c'
    assert ll[4] == 'e'
    assert ll[-1] == 'e'
    assert ll[-3] == 'c'
    assert ll[-5] == 'a'
    assert ll[-10] == 'a'
    assert ll[2:5] == ['c', 'd', 'e']
    assert ll[2:10] == ['c', 'd', 'e']

# Generated at 2022-06-13 19:56:42.819246
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    for i in [1, 0, 2, -1, None]:
        l = LazyList(range(10))
        for j in [0, 1, i, None]:
            if j == i or j is None:
                assert l[i] == list(l)[i]
            if j == i or (j is not None and i != j):
                l[j]
                assert l[i] == list(l)[i]


# Generated at 2022-06-13 19:56:50.521237
# Unit test for function scanl
def test_scanl():
    """
    test function scanl
    """
    import operator
    import functools
    test_list = [1, 2, 3, 4]
    assert list(scanl(operator.add, test_list, 0)) == [0, 1, 3, 6, 10]
    assert list(scanl(lambda s, x: x + s, ['a', 'b', 'c', 'd'])) == ['a', 'ba', 'cba', 'dcba']
    assert list(scanl(lambda s, x: x + s, ['a', 'b', 'c', 'd'], '*')) == ['*', '*a', '*ab', '*abc']
    return



# Generated at 2022-06-13 19:57:03.011108
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    lst = MapList(lambda x: x * x, range(10))
    for idx in range(10):
        assert lst[idx] == idx * idx
    assert lst[0:2] == [0, 1]
    assert lst[:2] == [0, 1]
    assert lst[2:] == [4, 9, 16, 25, 36, 49, 64, 81]
    assert lst[:] == [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    assert lst[-1] == 81
    assert lst[::2] == [0, 4, 16, 36, 64]
    assert lst[1::2] == [1, 9, 25, 49, 81]



# Generated at 2022-06-13 19:57:14.296941
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x > 5, range(5))) == []
    assert list(drop_until(lambda x: x > 5, [7, 8, 9])) == [7, 8, 9]
    assert list(drop_until(lambda x: x > 5, [])) == []
    for n in range(10):
        r = list(range(n, 10))
        assert list(drop_until(lambda _: True, r)) == r
        assert list(drop_until(lambda x: x == n, r)) == r[n:]
        assert list(drop_until(lambda x: x > n, r)) == r[n + 1:]

# Generated at 2022-06-13 19:57:27.030940
# Unit test for function drop_until
def test_drop_until():
    # All positive numbers
    assert list(drop_until(lambda x: x < 0, range(10))) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # All negative numbers
    assert list(drop_until(lambda x: x >= 0, range(-5, 5))) == [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]
    # Empty iterable
    assert list(drop_until(lambda x: x >= 0, [])) == []
    # One element satisfies predicate
    assert list(drop_until(lambda x: x % 2 == 0, [1, 3, 4, 5, 6])) == [4, 5, 6]
    # No element satisfies predicate
    assert list(drop_until(lambda x: x > 5, range(5)))

# Generated at 2022-06-13 19:57:32.255957
# Unit test for function drop_until
def test_drop_until():
    # should drop nothing
    assert list(drop_until(lambda x: x > 5, range(10))) == list(range(10))
    # should drop 1 element
    assert list(drop_until(lambda x: x > 5, range(10, 1, -1))) == list(range(9, 1, -1))
    # should drop all elements
    assert list(drop_until(lambda x: x > 5, range(5, -1, -1))) == []



# Generated at 2022-06-13 19:57:49.191138
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    l = LazyList(range(100))
    assert l[0] == 0
    assert l[-1] == 99
    assert l[:10] == list(range(10))
    assert l[5:10] == list(range(5, 10))
    assert l[5:] == list(range(5, 100))
    assert l[:] == list(range(100))



# Generated at 2022-06-13 19:57:56.516038
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    for x in range(0,1000):
        l = [1,2,3,4,5]
        m = MapList(lambda x: x*x, l)
        if m[x] != l[x]*l[x]:
            raise RuntimeError("MapList___getitem__: the method __getitem__ of class MapList is wrong")


# Generated at 2022-06-13 19:58:05.928774
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    assert list(LazyList([1, 2, 3])[:]) == [1, 2, 3]
    assert list(LazyList([1, 2, 3])[1:]) == [2, 3]
    assert LazyList([1, 2, 3])[1] == 2
    raises(TypeError, lambda: len(LazyList([])))
    assert len(LazyList([1, 2, 3])) == 3


# Generated at 2022-06-13 19:58:13.349828
# Unit test for function drop
def test_drop():
    assert list(drop(0, range(10))) == list(range(10))
    assert list(drop(1, range(10))) == list(range(1, 10))
    assert list(drop(10, range(10))) == []
    assert list(drop(5, [1, 2, 3])) == [3]



# Generated at 2022-06-13 19:58:15.965194
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]


# Generated at 2022-06-13 19:58:22.252587
# Unit test for function drop_until
def test_drop_until():
    # iterable that is empty
    assert list(drop_until(lambda x: x > 10, range(10))) == []
    # iterable that contains elements that satisfy the predicate
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
    # iterable that contains no elements that satisfy the predicate
    assert list(drop_until(lambda x: x > 10, range(1))) == []



# Generated at 2022-06-13 19:58:24.483258
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]


# Generated at 2022-06-13 19:58:35.675019
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    print(Range(10)[5])
    print(Range(10)[5:8])
    print(Range(10)[5:8:2])
    print(Range(10)[::2])
    print(Range(10)[::-1])
    print(Range(10)[-1])
    print(Range(10)[-1:0:-1])
    print(Range(10)[-1:0:-2])
    print(Range(10)[-1:0:2])


# Generated at 2022-06-13 19:58:43.261190
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    import random
    import bisect
    a = [random.randint(0, 100) for _ in range(10)]
    b = sorted(a)
    m = MapList(lambda x: x * x, a)
    for x in a:
        assert m[x] == x * x, f"{m[x]} != {x * x}"
    assert m[::2] == [x * x for x in a[::2]]
    for x in a:
        assert bisect.bisect_left(m, x * x) == bisect.bisect_left(b, x * x)
    assert bisect.bisect_left(m, -1) == 0
    assert bisect.bisect_left(m, 10001) == len(m)

# Generated at 2022-06-13 19:58:57.976942
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    # Test for __getitem__ with three range inputs
    r = Range(1, 10+1)
    for i in range(10):
        assert(r[i] == i+1)
    
    r = Range(1, 10+1, 2)
    for i in range(10):
        assert(r[i] == 2*i+1)
        
    r = Range(7, 10+1, 3)
    for i in range(10):
        assert(r[i] == 3*i+7)
    # End of test

    # Test for __getitem__ with one range input
    r = Range(5)
    for i in range(5):
        assert(r[i] == i)
    # End of test

    # Test for __getitem__ with two range inputs

# Generated at 2022-06-13 19:59:12.790165
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(1, 10, 2)
    assert r[0] == 1
    assert r[1] == 3
    assert r[2] == 5
    assert r[3] == 7
    assert r[-1] == 9
    assert r[-2] == 7
    assert r[:3] == [1, 3, 5]
    assert r[2:] == [5, 7, 9]
    assert r[2:4] == [5, 7]
    assert r[-5:-2] == [1, 3, 5]
    assert r[-4:4] == [1, 3, 5]
    assert r[-4:-2] == [1, 3]
    assert r[1:1] == []


# Generated at 2022-06-13 19:59:23.652820
# Unit test for function split_by
def test_split_by():
    # criterion
    assert list(split_by(range(10), criterion=lambda x: x % 3 == 0)) == [[1, 2], [4, 5], [7, 8]]
    assert list(split_by(range(10), criterion=lambda x: x <= 2)) == [[3, 4, 5, 6, 7, 8, 9]]
    assert list(split_by(range(10), criterion=lambda x: x % 2 == 0)) == [[1, 3, 5, 7, 9]]
    assert list(split_by(range(10), criterion=lambda x: x % 5 == 0)) == [[1, 2, 3, 4], [6, 7, 8, 9]]
    assert list(split_by([], criterion=lambda x: True)) == []
    # separator

# Generated at 2022-06-13 19:59:28.373821
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    from itertools import count
    lst = LazyList(count())
    for i in range(1000):
        assert lst[i] == i
    for i in range(1000):
        assert lst[i] == i



# Generated at 2022-06-13 19:59:34.600741
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    xs = range(10)
    ys = LazyList(xs)
    assert ys[1] == 1
    assert ys[:7] == list(xs[:7])
    assert ys[:20] == ys[::2] == list(xs)[::2]
    assert ys[-1] == ys[:20][-1] == list(xs)[-1]
    assert ys[-2] == ys[-1] - 1 == ys[20:][0] == list(xs)[-2]
    assert ys[-3] == ys[-2] - 1 == list(xs)[-3]
    assert ys[4:4] == []

# Generated at 2022-06-13 19:59:42.347216
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x == 0, [])) == []
    assert list(drop_until(lambda x: True, iter([1, 2, 3]))) == [1, 2, 3]
    assert list(drop_until(lambda x: x == 5, iter([1, 2, 5, 6]))) == [5, 6]
    assert list(drop_until(lambda x: x == 5, iter([5, 6]))) == [5, 6]
    assert list(drop_until(lambda x: x == 5, iter([5]))) == [5]
    assert list(drop_until(lambda x: x == 5, iter([]))) == []



# Generated at 2022-06-13 19:59:51.352802
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    n1, n2 = random.randint(1, 10), random.randint(1, 10)
    r = Range(n1, n2, 1)
    for i in range(n1, n2):
        assert r[i - n1] == i
    for i in range(n1):
        try:
            r[i - n1]
            assert False
        except IndexError:
            pass
    for i in range(n2, n2 + 10):
        try:
            r[i - n1]
            assert False
        except IndexError:
            pass


# Generated at 2022-06-13 20:00:00.443962
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    class TestIterable:
        def __init__(self):
            self.counter = 0
        def __iter__(self):
            return self
        def __next__(self):
            self.counter += 1
            return self.counter - 1
    import pytest
    it = TestIterable()
    ugly = LazyList(it)
    assert it.counter == 0
    assert ugly[0] == 0
    assert it.counter == 1
    assert ugly[0] == 0
    assert it.counter == 1
    assert ugly[1] == 1
    assert it.counter == 2
    assert ugly[2] == 2
    assert it.counter == 3
    assert ugly[5] == 5
    assert it.counter == 6
    with pytest.raises(IndexError):
        ugly[6]
    assert it.counter

# Generated at 2022-06-13 20:00:02.667900
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]



# Generated at 2022-06-13 20:00:13.996517
# Unit test for method __getitem__ of class Range

# Generated at 2022-06-13 20:00:23.626538
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    from itertools import count
    from operator import add, mul

    # Test LazyList
    llist = LazyList(count(0))
    # test lazy list indexing
    assert llist[0] == 0
    assert llist[1] == 1
    assert llist[2] == 2
    assert llist[3] == 3
    assert llist[-1] == 3
    assert llist[:3] == [0, 1, 2]
    assert llist[3:] == [3]
    assert len(llist) == 4
    assert all(x == i for i, x in enumerate(llist))  # test that the iterator works correctly
    llist = LazyList(mul(x, x) for x in count(1))
    assert llist[0] == 1

# Generated at 2022-06-13 20:00:34.049245
# Unit test for function drop_until
def test_drop_until():
    seq = range(10)
    result = list(drop_until(lambda x: x > 5, seq))
    assert result == [6, 7, 8, 9]

    result = list(drop_until(lambda x: x > 15, seq))
    assert result == []

    result = list(drop_until(lambda x: x < 0, seq))
    assert result == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]



# Generated at 2022-06-13 20:00:44.626363
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    list1 = [1, 2, 3]
    def func(v):
        return v * v

    mapobj = MapList(func, list1)
    for index, item in enumerate(mapobj):
        assert item == mapobj[index]
    for index in range(-len(list1), len(list1)):
        assert mapobj[index] == mapobj[slice(index, index + 1)][0]
    for index in range(-len(list1), len(list1)):
        sliceobj = slice(index, index + 1)
        assert mapobj[-index - 1] == mapobj[sliceobj][0]


if __name__ == '__main__':
    test_MapList___getitem__()



# Generated at 2022-06-13 20:00:49.138996
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x > 5, range(6))) == []
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]



# Generated at 2022-06-13 20:00:52.925743
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    for i in range(1, 5):
        llist = LazyList(range(i))
        assert llist[0] == 0
        assert llist[i - 1] == i - 1


# Generated at 2022-06-13 20:00:58.393307
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    lst = LazyList(range(10))
    assert lst[0] == 0
    assert lst[9] == 9
    assert lst[10] == 10
    assert lst[-1] == 9
    assert lst[:4] == [0, 1, 2, 3]
    assert lst[2:7] == [2, 3, 4, 5, 6]

# Generated at 2022-06-13 20:01:08.232170
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    import types
    def fibgen(x: int, fib_prev: int, fib_cur: int) -> Iterator[int]:
        for _ in range(x):
            yield fib_cur
            fib_prev, fib_cur = fib_cur, fib_prev + fib_cur

    assert isinstance(LazyList(fibgen(10, 0, 1))[:], list)
    assert isinstance(LazyList(fibgen(10, 0, 1))[:10], list)
    assert isinstance(LazyList(fibgen(10, 0, 1))[:-1], list)
    assert isinstance(LazyList(fibgen(10, 0, 1))[0:10], list)
    assert isinstance(LazyList(fibgen(10, 0, 1))[0:-1], list)


# Generated at 2022-06-13 20:01:13.302104
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    import bisect

    # Find index of the first element in `a` whose square is >= 10.
    a = [1, 2, 3, 4, 5]
    pos = bisect.bisect_left(MapList(lambda x: x * x, a), 10)
    assert pos == 3

    # Find the first index `i` such that `a[i] * b[i]` is >= 10.
    b = [2, 3, 4, 5, 6]
    pos = bisect.bisect_left(MapList(lambda i: a[i] * b[i], Range(len(a))), 10)
    assert pos == 2



# Generated at 2022-06-13 20:01:18.143134
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    a = [1, 2, 3, 4, 5]
    b = [2, 3, 4, 5, 6]
    l = MapList(lambda i: a[i] * b[i], Range(len(a)))
    if l[2] == 18:
        return True
    return False

# Generated at 2022-06-13 20:01:21.656224
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    assert Range(10)[5] == 5
    assert Range(1, 10 + 1)[5 - 1] == 5
    assert Range(1, 11, 2)[5 - 1] == 9
test_Range___getitem__()



# Generated at 2022-06-13 20:01:22.837725
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(1,10)
    assert r[2] == 3
    assert r[-1] == 9
    

    

# Generated at 2022-06-13 20:01:46.050125
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    from .maptools import MapList
    from .rangetools import Range
    lst = [1, 2, 3, 4]
    assert(MapList(lambda x: x + 1, lst)[0] == 2)
    assert(MapList(lambda x: x + 1, lst)[1] == 3)
    assert(MapList(lambda x: x + 1, lst)[2] == 4)
    assert(MapList(lambda x: x + 1, lst)[3] == 5)
    assert(MapList(lambda x: x + 1, lst)[-1] == 5)
    assert(MapList(lambda x: x + 1, lst)[-2] == 4)
    assert(MapList(lambda x: x + 1, lst)[-3] == 3)

# Generated at 2022-06-13 20:01:54.297155
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    lst = MapList(lambda x: x * x, [1, 2, 3, 4, 5])
    item_0 = lst.__getitem__(0)
    item_1 = lst.__getitem__(1)
    item_2 = lst.__getitem__(2)
    item_3 = lst.__getitem__(3)
    item_4 = lst.__getitem__(4)
    item_neg_4 = lst.__getitem__(-4)
    item_neg_5 = lst.__getitem__(-5)
    item_slice_0_5 = lst.__getitem__(slice(0, 5, None))
    item_slice_0_neg_4 = lst.__getitem__(slice(0, -4, None))
    item

# Generated at 2022-06-13 20:01:59.781381
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    print("\nTEST TestMapList___getitem__")
    a = [1, 2, 3, 4, 5]
    b = [2, 3, 4, 5, 6]
    pos = bisect.bisect_left(MapList(lambda x: x * x, a), 10)
    print("pos expected: 3, result:", pos)
    pos = bisect.bisect_left(MapList(lambda i: a[i] * b[i], Range(len(a))), 10)
    print("pos expected: 2, result:", pos)
    # Test with slice
    print("Test with slice")
    m1 = MapList(lambda i: i % 2 == 0, list(range(10)))
    assert m1[0:1] == [False]

# Generated at 2022-06-13 20:02:02.930186
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    lst = LazyList(range(10))
    assert lst[0] == 0
    assert lst[5] == 5
