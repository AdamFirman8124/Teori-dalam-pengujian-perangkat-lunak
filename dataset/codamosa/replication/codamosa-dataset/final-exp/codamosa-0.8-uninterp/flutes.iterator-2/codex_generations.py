

# Generated at 2022-06-13 19:52:40.116977
# Unit test for function drop
def test_drop():
    assert list(drop(0, range(10))) == list(range(10))

    assert list(drop(3, range(10))) == list(range(3, 10))

    assert list(drop(10, range(10))) == []

    assert list(drop(10, range(5))) == []

    assert list(drop(10, [])) == []



# Generated at 2022-06-13 19:52:42.662594
# Unit test for function split_by
def test_split_by():
    assert list(split_by([1, 2, 3, 4, 5], criterion=lambda x: x % 3 == 0)) == [[1, 2], [4, 5]]



# Generated at 2022-06-13 19:52:48.910531
# Unit test for method __next__ of class Range
def test_Range___next__():
    __expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    __instance = Range(0, 10)
    __actual = []
    for i in range(len(__expected)):
        __actual.append(__instance.__next__())
    assert all_equal(__expected, __actual)



# Generated at 2022-06-13 19:52:51.833010
# Unit test for function drop
def test_drop():
    it = iter(range(10))
    assert next(it) == 0
    assert next(it) == 1
    for x in drop(5, it):
        print(x)



# Generated at 2022-06-13 19:52:59.433144
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    from sys import version_info
    if version_info[0] == 2:
        print("__getitem__ not tested in Python 2")
        return
    L = [1, 2, 3, 4]
    R = Range(1, 5)
    assert L[0] == R[0]
    assert L[1] == R[1]
    assert L[2] == R[2]
    assert L[3] == R[3]
    assert L[:] == R[:]
    assert L[::-1] == R[::-1]
    assert L[::2] == R[::2]
    assert L[1::2] == R[1::2]
    assert L[:10:2] == R[:10:2]
    assert L[::-10] == R[::-10]
   

# Generated at 2022-06-13 19:53:04.127986
# Unit test for function drop
def test_drop():
    with pytest.raises(ValueError) as excinfo:
        list(drop(-1, range(10)))
    assert "`n` should be non-negative" in str(excinfo.value)
    assert list(drop(1, range(3))) == [1, 2]
    assert list(drop(4, range(4))) == []



# Generated at 2022-06-13 19:53:06.275302
# Unit test for function take
def test_take():
    t = take(3,range(5))
    assert t == [0,1,2]
test_take()



# Generated at 2022-06-13 19:53:11.014982
# Unit test for function take
def test_take():
    assert list(take(5, range(10))) == [0, 1, 2, 3, 4]
    assert list(take(5, range(0))) == []
    assert list(take(0, range(10))) == []
    assert list(take(0, range(0))) == []



# Generated at 2022-06-13 19:53:18.365905
# Unit test for function split_by
def test_split_by():
    list(split_by([1, 2, 3, 5, 6, 7, 8, 9], criterion=lambda x: x % 3 == 0)) == [[1, 2], [5, 6], [8, 9]]
    list(split_by([1, 2, 3, 4], criterion=lambda x: x % 3 == 0)) == [[1, 2], [4]]
    list(split_by([1, 2, 3, 4], criterion=lambda x: x % 3 == 0, empty_segments=True)) == [[1, 2], [], [4]]
test_split_by()



# Generated at 2022-06-13 19:53:24.284862
# Unit test for function drop_until
def test_drop_until():
    iterable = iter(range(10))
    pred_fn = lambda x: x > 5
    dropped_iterable = drop_until(pred_fn, iterable)
    assert list(dropped_iterable) == [6,7,8,9]


# Generated at 2022-06-13 19:53:43.773157
# Unit test for function split_by
def test_split_by():
    s = "Split by :"
    for x in split_by(s, separator=':'):
        print(x)

    for x in split_by(s, separator=':', empty_segments=True):
        print(x)

    for x in split_by(s, empty_segments=True, criterion=lambda x: x.isspace()):
        print(x)

    n = 1
    for x in split_by(n, criterion=lambda x: x > 1, empty_segments=True):
        print(x)


# Generated at 2022-06-13 19:53:52.147254
# Unit test for function chunk
def test_chunk():
    data = [
        ([], 0, []),
        ([], 1, []),
        (range(10), 0, []),
        (range(10), 1, [[i] for i in range(10)]),
        (range(10), 2, [[i, i + 1] for i in range(0, 9, 2)]),
        (range(10), 3, [[i, i + 1, i + 2] for i in range(0, 9, 3)]),
    ]
    for iterable, n, expected_output in data:
        actual_output = list(chunk(n, iterable))
        assert actual_output == expected_output, "{} {} {}".format(iterable, n, expected_output)



# Generated at 2022-06-13 19:54:03.137052
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x < 0, range(10))) == []
    assert list(drop_until(lambda x: x > 5, [10, 2])) == [10, 2]
    assert list(drop_until(lambda x: x > 5, [10])) == [10]
    assert list(drop_until(lambda x: x > 5, [])) == []
    assert list(drop_until(lambda x: x > 5, [4, 5, 6, 7, 8])) == [6, 7, 8]



# Generated at 2022-06-13 19:54:13.091101
# Unit test for function drop_until

# Generated at 2022-06-13 19:54:22.179395
# Unit test for function chunk
def test_chunk():
    assert list(chunk(0, range(10))) == []
    assert list(chunk(1, range(10))) == [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]]
    assert list(chunk(2, range(10))) == [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]]
    assert list(chunk(3, range(10))) == [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]
    assert list(chunk(4, range(10))) == [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9]]

# Generated at 2022-06-13 19:54:27.553438
# Unit test for method __iter__ of class LazyList
def test_LazyList___iter__():
    it = iter(range(100))
    lst = LazyList(it)
    it2 = iter(lst)
    next(it2)
    next(it2)
    next(it2)
    assert list(it2) == list(range(3, 100))
    assert list(lst) == list(range(100))
    it3 = iter(lst)
    assert list(it3) == list(range(100))
    it4 = iter(it3)



# Generated at 2022-06-13 19:54:35.992308
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    import bisect
    a = [1, 2, 3, 4, 5]
    pos = bisect.bisect_left(MapList(lambda x : x * x, a), 10)
    assert_equal(pos, 3)
    b = [2, 3, 4, 5, 6]
    pos = bisect.bisect_left(MapList(lambda i : a[i] * b[i],
                                    Range(len(a))), 10)
    assert_equal(pos, 2)



# Generated at 2022-06-13 19:54:38.581149
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x > 5, range(6))) == []


# Generated at 2022-06-13 19:54:51.813072
# Unit test for function chunk
def test_chunk():
    assert list(chunk(3, range(10))) == [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]
    assert list(chunk(3, range(9))) == [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    assert list(chunk(3, range(8))) == [[0, 1, 2], [3, 4, 5], [6, 7]]
    assert list(chunk(3, range(7))) == [[0, 1, 2], [3, 4, 5], [6]]
    assert list(chunk(3, range(6))) == [[0, 1, 2], [3, 4, 5]]
    assert list(chunk(3, range(5))) == [[0, 1, 2], [3, 4]]

# Generated at 2022-06-13 19:55:03.247506
# Unit test for function split_by
def test_split_by():
    test_set = [
        (range(10), lambda x: x % 3 == 0, [[1, 2], [4, 5], [7, 8]]),
        (" Split by: ", '.', [[], ['S', 'p', 'l', 'i', 't'], ['b', 'y', ':'], []]),
        (" Split by: ", '.', [['S', 'p', 'l', 'i', 't'], ['b', 'y', ':'], []], False),
        (" Split by: ", '.', [], False, False),
        (" Split by: ", '.', [[]], True, False),
    ]
    for arg in test_set:
        try:
            assert list(split_by(*arg)) == arg[-1]
        except ValueError:
            pass

# Generated at 2022-06-13 19:55:24.481985
# Unit test for function drop_until
def test_drop_until():
    it = range(10)
    assert(list(drop_until(lambda x: x > 5, it)) == [6, 7, 8, 9])



# Generated at 2022-06-13 19:55:32.883893
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    import unittest

    class Test(unittest.TestCase):
        def test_case(self):
            m = MapList(lambda x: x * x * x, [1, 2, 3, 4, 5])
            self.assertEqual(m[4], 625)
            self.assertEqual(m[2:4], [27, 64])

    t = Test()
    t.test_case()

# Generated at 2022-06-13 19:55:40.603193
# Unit test for function split_by
def test_split_by():
    assert list(split_by(range(10), criterion=lambda x: x % 3 == 0)) == [[1, 2], [4, 5], [7, 8]]
    assert list(split_by((1,2,3,10,11,12,13), criterion=lambda x: x % 10 == 0)) == [[1, 2, 3], [], [11, 12, 13]]
    assert list(split_by(" Split by: ", True, separator='.')) == [[], ['S', 'p', 'l', 'i', 't'], ['b', 'y', ':'], []]



# Generated at 2022-06-13 19:55:44.542400
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(-2, 3)
    assert r[2] == r[-2] == 0
    assert r[-1] == 1
    assert r[0] == -2


# Generated at 2022-06-13 19:55:48.325901
# Unit test for function drop_until
def test_drop_until():
    def pred_fn(x: int) -> bool:
        return x > 5

    list(drop_until(pred_fn, range(10))) == [6, 7, 8, 9]



# Generated at 2022-06-13 19:55:50.889295
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x > 5, range(2))) == []
    assert list(drop_until(lambda x: x > 5, range(6))) == [6]
    assert list(drop_until(lambda x: x > 5, [])) == []



# Generated at 2022-06-13 19:55:59.372853
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    import random
    n = random.randint(1, 20)
    r = Range(n)
    assert r[-1] == r[n - 1]
    assert r[: -1] == r[:-1]
    assert r[:] == r[:]
    assert r[1: -1] == r[1: -1]
    assert r[1:] == r[1:]
    assert r[:-1] == r[:-1]
    assert r[: -1] == r[:-1]
    assert [i for i in r[1: -1]] == [i for i in r[1: -1]]
    assert [i for i in r[1:]] == [i for i in r[1:]]
    assert [i for i in r[:-1]] == [i for i in r[:-1]]

# Generated at 2022-06-13 19:56:15.457216
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    l = LazyList(range(10))
    assert l[0] == 0
    assert l[1] == 1
    assert l[-1] == 9
    assert l[2:6] == [2, 3, 4, 5]
    assert l[2:6:2] == [2, 4]
    assert l[3:] == [3, 4, 5, 6, 7, 8, 9]
    assert l[:3] == [0, 1, 2]
    assert l[::2] == [0, 2, 4, 6, 8]
    assert l[5:5] == []
    assert l[5:4] == []
    assert l[5:3:-1] == [5, 4]
    assert l[5:1:-2] == [5, 3]

# Generated at 2022-06-13 19:56:25.119301
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(1, 10 + 1)  # (start, end)
    assert(r[0] == 1)
    assert(r[2] == 3)
    assert(r[4] == 5)
    r = Range(1, 10 + 1, 2)   # (start, end, step)
    assert(r[0] == 1)
    assert(r[1] == 3)
    assert(r[2] == 5)
    #assert(r[4] == 9)
    arr = r[:]
    assert(len(arr) == 5)
    assert(arr[0] == 1)
    assert(arr[2] == 5)
    assert(arr[len(arr) - 1] == 9)
    arr = r[1:3]
    assert(len(arr) == 2)

# Generated at 2022-06-13 19:56:28.536432
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == list(range(6, 10))


# Generated at 2022-06-13 19:56:47.774655
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    assert_equal(Range(1, 10 + 1, 2)[0], 1)
    assert_equal(Range(1, 10 + 1, 2)[1], 3)
    assert_equal(Range(1, 10 + 1, 2)[2], 5)
    assert_equal(Range(1, 10 + 1, 2)[5], 11)

    assert_equal(Range(1, 10 + 1, 2)[-1], 11)
    assert_equal(Range(1, 10 + 1, 2)[-2], 9)
    assert_equal(Range(1, 10 + 1, 2)[-3], 7)
    assert_equal(Range(1, 10 + 1, 2)[-6], 1)

    assert_equal(Range(1, 10 + 1, 2)[1:5], [3, 5, 7, 9])

# Generated at 2022-06-13 19:56:50.314677
# Unit test for function drop_until
def test_drop_until():
    list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]



# Generated at 2022-06-13 19:57:04.708647
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    ll = LazyList([1, 2, 3, 4])
    assert ll[1] == 2
    
    assert ll[::2] == [1, 3]
    assert ll[::-1] == [4, 3, 2, 1]
    
    assert list(ll) == [1, 2, 3, 4]
    
    # exception is raised only after the iterable gets depleted
    ll = LazyList([1, 2, 3, 4])
    ll[1:3]
    with pytest.raises(TypeError):
        len(ll)
    
    # fetching past the length of the iterable raises IndexError
    ll = LazyList([1, 2, 3, 4])
    with pytest.raises(IndexError):
        ll[4]



# Generated at 2022-06-13 19:57:15.546343
# Unit test for function split_by
def test_split_by():
    assert list(split_by(range(10), criterion=lambda x: x % 3 == 0)) == [[1, 2], [4, 5], [7, 8]]
    assert list(split_by(range(11), criterion=lambda x: x % 3 == 0)) == [[1, 2], [4, 5], [7, 8], [10]]
    assert list(split_by(range(9), criterion=lambda x: x % 3 == 0)) == [[1, 2], [4, 5], [7, 8]]
    assert list(split_by(range(10), criterion=lambda x: x % 3 == 0, empty_segments=True)) == [[1, 2], [4, 5], [7, 8], []]

# Generated at 2022-06-13 19:57:21.298929
# Unit test for function scanl
def test_scanl():
    assert list(scanl(operator.add, [1, 2, 3, 4], 0)) == [0, 1, 3, 6, 10]
    assert list(scanl(lambda acc, x: x + acc, ['a', 'b', 'c', 'd'])) == ['a', 'ba', 'cba', 'dcba']

# Generated at 2022-06-13 19:57:31.261772
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(100)
    a = r[0:3]
    assert type(a) == list
    assert a == [0,1,2]
    a = r[-3:]
    assert type(a) == list
    assert a == [97,98,99]
    a = r[0]
    assert type(a) == int
    assert a == 0
    a = r[7]
    assert type(a) == int
    assert a == 7
    a = r[-7]
    assert type(a) == int
    assert a == 93
    try:
        r[100]
        assert False
    except IndexError:
        assert True
    try:
        r[-100]
        assert False
    except IndexError:
        assert True

# Generated at 2022-06-13 19:57:40.325789
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(10)
    assert r[0] == 0
    assert r[9] == 9
    assert r[-1] == 9
    assert list(r[::2]) == list(range(0, 10, 2))
    r = Range(1, 10 + 1)
    assert r[0] == 1
    assert r[9] == 10
    assert r[-1] == 10
    assert list(r[::2]) == list(range(1, 10 + 1, 2))
    r = Range(1, 11, 2)
    assert r[0] == 1
    assert r[4] == 9
    assert r[-1] == 9
    assert list(r[::2]) == list(range(1, 11, 4))


# Generated at 2022-06-13 19:57:53.114797
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    print("Testing Range.__getitem__()")
    r = Range(10)
    assert r[0] == 0
    assert r[-1] == 9
    assert r[5] == 5
    assert r[0:3] == [0, 1, 2]
    assert r[0:3:2] == [0, 2]
    assert r[1:10:3] == [1, 4, 7]
    assert r[3:-1] == [3, 4, 5, 6, 7, 8]
    assert r[-1:0] == []
    assert r[-1:0:-1] == [9, 8, 7, 6, 5, 4, 3, 2, 1]
    try:
        _ = r[-11]
        assert False
    except IndexError:
        pass

# Generated at 2022-06-13 19:57:57.143821
# Unit test for function split_by
def test_split_by():
    assert list(split_by(range(1, 10), separator=4)) == [[1, 2, 3], [5, 6, 7, 8, 9]]



# Generated at 2022-06-13 19:58:07.888120
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    _log.debug('')
    a = LazyList(range(100))
    assert a[5] == 5
    assert a[5:10] == [5, 6, 7, 8, 9]
    assert len(a) == 100
    a = LazyList(range(60))
    assert len(a) == 60
    with pytest.raises(TypeError):
        len(a[::-1])
    assert a[-10:] == list(range(50, 60))



# Generated at 2022-06-13 19:58:21.431582
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    for i in range(1,4):
        r = Range(i, 10, 2)
        rli = [r[j] for j in range(len(r))]
        assert rli == [i,i+2, i+4, i+6, i+8]
    r = Range(10)
    rli = [r[j] for j in range(len(r))]
    assert rli == [0,1,2,3,4,5,6,7,8,9]



# Generated at 2022-06-13 19:58:28.855625
# Unit test for function split_by
def test_split_by():
    a = "Split by: "
    b = ["", ["S", "p", "l", "i", "t"], ["b", "y", ":"], ""]
    c = list(split_by(a, separator='.'))
    assert c == b
    c = list(split_by(a, separator='.', empty_segments=False))
    assert c == ["", ["S", "p", "l", "i", "t"], ["b", "y", ":"], ""]
    c = list(split_by(a, separator='.', empty_segments=True))
    assert c == b



# Generated at 2022-06-13 19:58:36.017848
# Unit test for function drop_until
def test_drop_until():
    iter1 = iter(range(10))
    iter2 = iter(range(10))
    assert tuple(drop_until(lambda x: x > 5, iter1)) == (6, 7, 8, 9)
    assert tuple(iter2) == (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)



# Generated at 2022-06-13 19:58:40.536518
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x > 5, range(10))) == list(itertools.dropwhile(lambda x: x <= 5, range(10)))



# Generated at 2022-06-13 19:58:57.049863
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    test_range1 = Range(10)
    test_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    try:
        assert test_range1[0] == test_list[0]
        assert test_range1[1] == test_list[1]
        assert test_range1[2] == test_list[2]
    except:
        print("wrong at test_range1 with single parameters")    
    
    test_range2 = Range(1,10+1)

# Generated at 2022-06-13 19:59:01.461010
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    test_range_object = Range(1, 10)
    # Test slice object
    assert test_range_object[0:2] == [1, 2]
    # Test negative index
    assert test_range_object[-1] == 9

# Generated at 2022-06-13 19:59:10.046975
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(-1,1)
    assert r[0] == -1
    assert r[1] == 1
    assert r[-1] == 1
    assert r[-2] == -1
    assert r[-3] == -1
    assert r[:2] == [-1, 0, 1]
    assert r[:-1] == [-1, 0]
    assert r[:-1:2] == [-1]
    assert r[::2] == [-1, 1]
    assert r[::-2] == [1, -1]
    assert r[-3:-3:-1] == [0]
    assert r[-4:-4:-1] == [0]
    assert r[-4:-4:-2] == []
    assert r[-4:-4:4] == []

# Generated at 2022-06-13 19:59:13.771320
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    a = Range(1,10,1)
    try:
        b = a[2]
        b = a[2:4]
        assert b == [1,2,3]
    except StopIteration:
        pass



# Generated at 2022-06-13 19:59:23.016427
# Unit test for function drop_until
def test_drop_until():
    cases = [
        ((lambda x: x > 5, range(10)), [6, 7, 8, 9]),
        ((lambda x: x == 4, [1, 2, 3, 4, 5, 6, 7, 8]), [4, 5, 6, 7, 8]),
        ((lambda x: x <= 3, [1, 2, 3, 4, 5, 6, 7, 8]), [4, 5, 6, 7, 8]),
        ((lambda x: x >= 8, [1, 2, 3, 4, 5, 6, 7, 8]), [8]),
    ]
    for args, expect in cases:
        assert list(drop_until(*args)) == expect



# Generated at 2022-06-13 19:59:31.460462
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(1, 10 + 1)
    assert r[0] == 1
    assert r[2] == 3
    assert r[4] == 5
    assert r[0:3] == [1, 2, 3]
    assert r[4: -1] == [5, 6, 7, 8, 9]
    assert r[1::2] == [2, 4, 6, 8, 10]



# Generated at 2022-06-13 19:59:46.065463
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x > 10, range(10))) == []
    assert list(drop_until(lambda x: x > -10, range(10))) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]




# Generated at 2022-06-13 19:59:56.984238
# Unit test for function drop_until
def test_drop_until():
    # Test empty iterable
    assert list(drop_until(lambda x: x > 0, [])) == []

    # Test iterable 'abcd'
    assert list(drop_until(lambda x: x > 'a', 'abcd')) == ['b', 'c', 'd']

    # Test list [1, 2, 3, 4, 5]
    assert list(drop_until(lambda x: x > 2, [1, 2, 3, 4, 5])) == [3, 4, 5]

    # Test list [1, 3, 4, 5]
    assert list(drop_until(lambda x: x > 2, [1, 3, 4, 5])) == [3, 4, 5]

    # Test list [5, 1, 2, 3, 4]

# Generated at 2022-06-13 20:00:00.182112
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    a = Range(1,10,1)
    print(a[2])


# Generated at 2022-06-13 20:00:05.499965
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(1,10,1)
    print(r[0], r[2], r[4])
    print(r[-1], r[-3], r[-5])
    print(r[0:10], r[0:10:2])
    print(r[::2], r[::-2])
    # Will rise an exception
    # print(r[0:10:0])


# Generated at 2022-06-13 20:00:11.590996
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    assert Range(10) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert Range(1, 10 + 1) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert Range(1, 11, 2) == [1, 3, 5, 7, 9]
    assert Range(1, 11, 3)[:2] == [1, 4]
    assert Range(1, 11, 3)[2:3] == [7]
    assert Range(1, 11, 3)[1:3] == [4, 7]
    assert Range(1, 11, 3)[-1] == 9
    assert Range(1, 11, 3)[2:-1] == [7]

# Generated at 2022-06-13 20:00:20.705051
# Unit test for function drop_until
def test_drop_until():
    # test case 1
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
    # test case 2
    assert list(drop_until(lambda x: x > 0, range(10))) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # test case 3
    assert list(drop_until(lambda x: x > 0, range(-10, 0))) == []
    # test case 4
    assert list(drop_until(lambda x: x >= 0, range(-10, 0))) == [-1]


# Generated at 2022-06-13 20:00:29.293069
# Unit test for function drop_until
def test_drop_until():
    from collections import deque
    from .show import show
    lst = deque([1,2,3,4,5,6,3,4,5,6,3,4,5,6,3,4,5,6])
    import sys
    show(drop_until(lambda x: x % 2 == 0, range(0,100)))


# Generated at 2022-06-13 20:00:34.948008
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(1, 10)
    assert r[0] == 1
    assert r[5] == 6
    assert isinstance(r[-1], int)
    assert r[-2] == 9
    assert r[2:4] == [3,4]
    assert r[0:20:2] == [1,3,5,7,9]
    assert r[-1:-3:-1] == [9,8]
    with raises(TypeError):
        r[1.1]
    with raises(IndexError):
        r[20]



# Generated at 2022-06-13 20:00:43.109403
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    rng = Range(10)
    assert rng[0] == 0
    assert rng[3] == 3
    assert rng[-1] == 9

    rng = Range(1, 10 + 1)
    assert rng[0] == 1
    assert rng[3] == 4
    assert rng[-1] == 10

    rng = Range(1, 11, 2)
    assert rng[0] == 1
    assert rng[2] == 5
    assert rng[-1] == 9



# Generated at 2022-06-13 20:00:46.878589
# Unit test for function drop_until
def test_drop_until():
    import random
    n = 100
    a = [0] * n
    a[random.randrange(n)] = random.randrange(n)

    def pred_fn(x: int) -> bool:
        return x == 0

    assert list(drop_until(pred_fn, a)) == a[a.index(0):]



# Generated at 2022-06-13 20:01:02.808316
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x == 0, range(10))) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert list(drop_until(lambda x: True, range(10))) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert list(drop_until(lambda x: False, range(10))) == []
    assert list(drop_until(lambda x: True, [])) == []
    assert list(drop_until(lambda x: False, [])) == []


# Generated at 2022-06-13 20:01:05.460778
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r1 = Range(10)
    assert [r1[0], r1[2], r1[4]] == [0, 2, 4]


# Generated at 2022-06-13 20:01:07.538877
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    assert Range(5)[2] == 2
    assert Range(3, 10)[3] == 6
    assert Range(1, 11, 2)[3] == 7



# Generated at 2022-06-13 20:01:12.519954
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    assert Range(1, 3)[1] == 2
    assert Range(1, 3)[0] == 1
    assert Range(1, 3)[-1] == 2
    assert Range(1, 3)[-2] == 1
    assert Range(1, 3)[0:-1] == [1, 2]
    assert Range(1, 3)[1:-1] == [2]



# Generated at 2022-06-13 20:01:23.549370
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    assert [x for x in np.arange(10)] == Range(10)[:]
    assert [x for x in np.arange(10)] == Range(0, 10)[:]
    assert [x for x in np.arange(10)] == Range(0, 10, 1)[:]
    assert [x for x in np.arange(1, 10)] == Range(1, 10 + 1)[:]
    assert [x for x in np.arange(1, 10)] == Range(1, 10 + 1, 1)[:]
    assert [x for x in np.arange(1, 10, 2)] == Range(1, 10 + 1, 2)[:]
    assert [0, 2, 4, 6, 8] == Range(10)[0::2]

# Generated at 2022-06-13 20:01:36.283320
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(10)
    assert r[0] == 0 and r[9] == 9 and r[-1] == 9
    assert list(r[::-1]) == list(reversed(list(r)))
    assert list(r[::2]) == list(enumerate(r))[::2]
    assert r[:10:2] == list(enumerate(r))[:10:2]
    assert r[-1:0:-2] == list(enumerate(r))[-1:0:-2]
    assert r[-1::-2] == list(enumerate(r))[-1::-2]
    assert r[-2::-2] == list(enumerate(r))[-2::-2]

# Generated at 2022-06-13 20:01:47.126066
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    a1 = Range(3,3,3)
    a2 = Range(0,0)
    a3 = Range(0,0)
    a4 = Range(1,1,1)
    a5 = Range(1,1,1)
    a6 = Range(0,0,0)
    a7 = Range(0,1,1)
    a8 = Range(0,1,1)
    a9 = Range(0,2,1)
    a10 = Range(0,3,1)
    a11 = Range(0,3,2)
    a12 = Range(0,2,2)

    assert a1[0] is None
    assert a2[0] is None
    assert a3[0] is None
    assert a4[0] is None
    assert a5[0]

# Generated at 2022-06-13 20:01:50.950193
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x > 5, range(6))) == []
    assert list(drop_until(lambda x: x > 5, [])) == []



# Generated at 2022-06-13 20:01:59.867290
# Unit test for function drop_until
def test_drop_until():
    lst = [1,2,3,4,5,0,1,2,3,4,5]
    it = drop_until(lambda x: x > 3, lst)
    assert next(it) == 4
    assert next(it) == 5
    assert next(it) == 0
    assert next(it) == 1
    assert next(it) == 2
    assert next(it) == 3
    assert next(it) == 4
    assert next(it) == 5



# Generated at 2022-06-13 20:02:05.993959
# Unit test for function drop_until
def test_drop_until():
    it = drop_until(lambda x: x>5, range(10))
    assert next(it) == 6
    assert next(it) == 7
    assert next(it) == 8
    assert next(it) == 9
    with pytest.raises(StopIteration):
        next(it)

