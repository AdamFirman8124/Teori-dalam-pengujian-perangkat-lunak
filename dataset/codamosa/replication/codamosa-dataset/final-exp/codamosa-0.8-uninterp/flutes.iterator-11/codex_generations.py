

# Generated at 2022-06-13 19:52:40.279229
# Unit test for function take
def test_take():
    assert list(take(3, range(50))) == list(range(3))
    assert list(take(0, range(50))) == []
    assert list(take(-1, range(50))) == []
    assert list(take(50, range(50))) == list(range(50))


# Generated at 2022-06-13 19:52:48.424282
# Unit test for function drop
def test_drop():
    import random
    xs = [random.uniform(0, 1) for _ in range(1000)]
    assert list(drop(1, (x for x in xs))) == xs[1::]
    assert list(drop(0, (x for x in xs))) == xs
    assert list(drop(2, (x for x in xs))) == xs[2::]
    assert list(drop(101, (x for x in xs))) == xs[101::]



# Generated at 2022-06-13 19:52:57.234236
# Unit test for function chunk
def test_chunk():
    assert list(chunk(3, range(10))) == [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]
    assert list(chunk(3, range(7))) == [[0, 1, 2], [3, 4, 5], [6]]
    assert list(chunk(2, range(7))) == [[0, 1], [2, 3], [4, 5], [6]]
    assert list(chunk(1, range(10))) == [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]]
    assert list(chunk(0, range(10))) == []
    assert list(chunk(3, [])) == []
    assert list(chunk(0, [])) == []

# Generated at 2022-06-13 19:53:05.742828
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    a = Range(3)
    if not a[0] == 0:
        print("Fail: Range___getitem___1")
    if not a[1] == 1:
        print("Fail: Range___getitem___2")
    if not a[2] == 2:
        print("Fail: Range___getitem___3")
    if not a[-1] == 2:
        print("Fail: Range___getitem___4")
    if not a[-2] == 1:
        print("Fail: Range___getitem___5")
    if not a[-3] == 0:
        print("Fail: Range___getitem___6")
    if not list(a[0:2]) == [0, 1]:
        print("Fail: Range___getitem___7")

# Generated at 2022-06-13 19:53:14.443213
# Unit test for function take
def test_take():
    list1 = [1, 2, 3, 4, 5]
    list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list3 = []
    test_take_list1 = list(take(5, list1))
    test_take_list2 = list(take(5, list2))
    test_take_list3 = list(take(5, list3))
    assert list1 == test_take_list1
    assert list1 == test_take_list2
    assert [] == test_take_list3
    print("test_take passed")

test_take()



# Generated at 2022-06-13 19:53:28.109323
# Unit test for function chunk
def test_chunk():
    assert list(chunk(3, [])) == []
    assert list(chunk(3, iter([1,2,3,4,5,6]))) == [[1,2,3], [4,5,6]]
    assert list(chunk(2, iter([1,2,3,4,5,6]))) == [[1,2], [3,4], [5,6]]
    assert list(chunk(4, iter([1,2,3,4,5,6]))) == [[1,2,3,4], [5,6]]
    assert list(chunk(0, iter([1,2,3,4,5,6]))) == ValueError
    assert list(chunk(-1, iter([1,2,3,4,5,6]))) == ValueError




# Generated at 2022-06-13 19:53:32.459375
# Unit test for function chunk
def test_chunk():
    assert list(chunk(3, range(10))) == [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]
    assert list(chunk(-1, range(10))) == []
    assert list(chunk(3, [])) == []



# Generated at 2022-06-13 19:53:40.649413
# Unit test for function split_by
def test_split_by():
    assert list(split_by("CamelCase".lower(), criterion=str.isupper)) == [
        [], list("camel"), list("case")]

    assert list(split_by(" Split by: ", empty_segments=True, separator='.')) == [
        [], ['S', 'p', 'l', 'i', 't'], ['b', 'y', ':'], []]



# Generated at 2022-06-13 19:53:48.964900
# Unit test for function split_by
def test_split_by():
    lis = [1, 2, 4, 5, 12, 13, 14, 15, 23, 22, 21, 21, 23, 24, 25, 26, 68, 67, 66, 65, 64, 63, 62, 61,
           62, 63, 64, 65, 68, 67, 66, 65, 64, 63, 62, 61, 62, 63, 64, 65]
    # criterion : lambda x: 2<=x<=68
    # separator : 5, 15, 25


# Generated at 2022-06-13 19:53:55.220793
# Unit test for function chunk
def test_chunk():
    list(chunk(3, range(10)))
    list(chunk(2, range(10)))
    list(chunk(3, range(3)))
    list(chunk(1, range(10)))
    list(chunk(10, range(10)))
    list(chunk(0, range(10)))



# Generated at 2022-06-13 19:54:06.321225
# Unit test for method __len__ of class LazyList
def test_LazyList___len__():
    lazy_list = LazyList(range(10000))
    try:
        len(lazy_list)
        assert False, "Expect Exception: __len__ is not available before the iterable is depleted"
    except TypeError:
        pass
    assert len(list(lazy_list)) == 10000



# Generated at 2022-06-13 19:54:08.305044
# Unit test for function drop_until
def test_drop_until():
    result = list(drop_until(lambda x: x > 5, range(10)))
    assert result == [6, 7, 8, 9]



# Generated at 2022-06-13 19:54:14.010834
# Unit test for method __iter__ of class LazyList
def test_LazyList___iter__():
    lst = [1, 2, 3]
    ll = LazyList(lst)
    ll_iter = ll.__iter__()
    assert next(ll_iter) == 1
    assert next(ll_iter) == 2
    assert next(ll_iter) == 3



# Generated at 2022-06-13 19:54:24.453897
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    for x in range(10000):
        assert x == LazyList(range(x))[-1]
        assert x == LazyList(range(x))[x >> 1]
        assert x == LazyList(range(x))[x >> 1]
        assert x == LazyList(range(x))[x - 1]
        assert list(range(100)) == LazyList(range(x))[:100]
        assert list(range(1000)) == LazyList(range(x))[::10]
        assert list(range(1000)) == LazyList(range(x))[::10]
        assert list(range(1000)) == LazyList(range(x))[::10]
    x = 100000

# Generated at 2022-06-13 19:54:34.191580
# Unit test for method __iter__ of class LazyList
def test_LazyList___iter__():
    for data in (
        [],
        [1],
        [1, 2, 3, 4],
        [1, 2, 3, 4, 2, 1, 2],
    ):
        lst = LazyList(data[:-1])
        assert list(lst) == data
        lst._fetch_until(None)
        assert list(lst) == data
        assert list(lst) == data
        # Ensure that __iter__ can be called after the iterable is fully depleted
        assert list(lst) == data



# Generated at 2022-06-13 19:54:40.624640
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x == 5, range(10))) == [5, 6, 7, 8, 9]
    assert list(drop_until(lambda x: x > 10, range(10))) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert list(drop_until(lambda x: x < 5, range(10))) == []



# Generated at 2022-06-13 19:54:43.967460
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    # Given
    r = Range(3)
    # When
    res = r[1]
    # Then
    assert res == 1

# Generated at 2022-06-13 19:54:50.268735
# Unit test for method __len__ of class LazyList
def test_LazyList___len__():
    from hypothesis import given
    from . import strategies
    @given(strategies.lists(strategies.integers()))
    def test(x: List[int]) -> None:
        result = LazyList(x).__len__()
        result0 = x.__len__()
        assert result == result0
    test()



# Generated at 2022-06-13 19:55:01.658488
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    # boundary case
    r = Range(1, 3)
    assert r[0] == 1
    assert r[1] == 2
    assert r[1:2] == [2]
    try:
        _ = r[2]
        raise AssertionError()
    except IndexError:
        pass

    # normal case
    r = Range(2, 10, 2)
    assert r[0] == 2
    assert r[1] == 4
    assert r[1:2] == [4]
    try:
        _ = r[4]
        raise AssertionError()
    except IndexError:
        pass

    # negative index
    assert r[-1] == 8
    assert r[-3:-1] == [4, 6]



# Generated at 2022-06-13 19:55:06.365648
# Unit test for method __iter__ of class LazyList
def test_LazyList___iter__():
    lst = LazyList(range(10))
    assert [0, 1, 2, 3] == list(take(4, lst))
    assert [4, 5, 6, 7, 8] == list(take(5, lst))
    assert [9] == list(take(1, lst))
    assert [] == list(take(1, lst))

# Generated at 2022-06-13 19:55:14.996768
# Unit test for function drop
def test_drop():
    it = drop(1, ['a','b'])
    assert iter(it)
    assert it.__next__() == 'b'
    try:
        it.__next__()
    except:
        return True
    return False


# Generated at 2022-06-13 19:55:22.354709
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    from itertools import chain

    for lst in (list(range(10)), list(range(10))[::-1], list(range(0, 10, 2)), list(range(1, 10, 3)), []):
        for idx in chain(range(len(lst)), range(-len(lst), 0)):
            assert lst[idx] == MapList(lambda x: x, lst)[idx]
        assert lst[2:5] == MapList(lambda x: x, lst)[2:5]
        assert lst[0:len(lst)] == MapList(lambda x: x, lst)[:]
        assert lst[len(lst):0:-1] == MapList(lambda x: x, lst)[::-1]

# Generated at 2022-06-13 19:55:28.336099
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    assert Range(10)[0] == 0
    assert Range(10)[1] == 1
    assert Range(10)[-1] == 9
    assert Range(10)[-2] == 8
    assert Range(10)[0:2] == [0, 1]
    assert Range(10)[1:7:2] == [1, 3, 5]

# Generated at 2022-06-13 19:55:36.491367
# Unit test for method __len__ of class LazyList
def test_LazyList___len__():
    # can only invoke __len__ when the iterable is depleted
    lst = LazyList(range(10))
    assert len(lst) == 10
    # would raise exception (that's fine)
    try:
        LazyList(range(10)).__len__()
        lst = LazyList(range(10))
        lst._exhausted = False
        lst.__len__()
    except TypeError as e:
        assert str(e) == "__len__ is not available before the iterable is depleted"



# Generated at 2022-06-13 19:55:43.340154
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(10)
    assert r.__getitem__(0) == 0
    assert r.__getitem__(1) == 1
    r = Range(1, 10+1)
    assert r.__getitem__(0) == 1
    assert r.__getitem__(1) == 2
    assert r.__getitem__(9) == 10
    r = Range(1, 11, 2)
    assert r.__getitem__(0) == 1
    assert r.__getitem__(1) == 3
    assert r.__getitem__(2) == 5
    assert r.__getitem__(3) == 7
    assert r.__getitem__(4) == 9


# Generated at 2022-06-13 19:55:44.253941
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]



# Generated at 2022-06-13 19:55:48.310906
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    def func(x): return 2*x
    lst = [1, 2, 3, 4, 5]
    m = MapList(func, lst)
    assert m.func == func
    assert m.list == lst
    assert m[0] == 2
    assert m[1] == 4
    assert m[2] == 6
    assert m[3] == 8
    assert m[4] == 10
    assert m[-1] == 10
    assert m[-2] == 8
    assert type(m[0:3]) == list
    assert len(m[0:3]) == 3
    assert m[0:3][0] == 2
    assert m[0:3][1] == 4
    assert m[0:3][2] == 6
    assert m[1:-1][0] == 4


# Generated at 2022-06-13 19:55:57.915972
# Unit test for function drop
def test_drop():
    it = iter(range(10))
    assert list(it) == list(drop(100, it))
    it = iter(range(10))
    assert list(it) == list(drop(-1, it))
    it = iter(range(10))
    assert list(it) == list(drop(0, it))
    it = iter(range(10))
    assert list(drop(1, it)) == list(range(1, 10))
    it = iter(range(10))
    assert list(drop(9, it)) == list(range(9, 10))
    it = iter(range(10))
    assert list(drop(10, it)) == list(range(10, 10))
    it = iter(range(10))
    assert list(drop(11, it)) == list(range(10, 10))




# Generated at 2022-06-13 19:56:03.086036
# Unit test for function drop
def test_drop():
    it = drop(5, range(10))
    assert next(it) == 5
    assert next(it) == 6
    assert next(it) == 7
    assert next(it) == 8
    assert next(it) == 9



# Generated at 2022-06-13 19:56:13.510649
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():

    r = Range(1, 10, 2)
    r_ = [1, 3, 5, 7, 9]
    assert (r[0]== r_[0])
    assert (r[4]== r_[4])
    r = Range(1, 9)
    r_ = [1, 2, 3, 4, 5, 6, 7, 8]
    assert (r[0]== r_[0])
    assert (r[3]== r_[3])
    r = Range(1, 20, 4)
    r_ = [1, 5, 9, 13, 17]
    assert (r[0]== r_[0])
    assert (r[4]== r_[4])
test_Range___getitem__()

# Generated at 2022-06-13 19:56:28.400258
# Unit test for function drop_until
def test_drop_until():
    assert [6, 7, 8, 9] == list(drop_until(lambda x: x > 5, range(10)))



# Generated at 2022-06-13 19:56:32.954981
# Unit test for function drop_until
def test_drop_until():
    for i in range(1000):
        xs = random.choices(range(1000), k=1000)
        p = random.choice(xs)
        pred_fn = lambda x: x > p
        cut = next((i for i, x in enumerate(xs) if x > p), len(xs))
        assert list(drop_until(pred_fn, xs)) == xs[cut:]



# Generated at 2022-06-13 19:56:34.829254
# Unit test for function drop_until
def test_drop_until():
    data = range(10)
    assert list(drop_until(lambda x: x > 5, data)) == [6, 7, 8, 9]



# Generated at 2022-06-13 19:56:42.397950
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    lst = LazyList(range(5))
    assert lst[:] == [0, 1, 2, 3, 4]
    assert lst[1:] == [1, 2, 3, 4]
    assert lst[0:3] == [0, 1, 2]
    assert lst[::-1] == [4, 3, 2, 1, 0]


Range = TypeVar('Range', int, 'Range[Any]')



# Generated at 2022-06-13 19:56:47.811847
# Unit test for function drop_until
def test_drop_until():
    # Drop 0 elements
    assert list(drop_until(lambda x: x > 0, range(10))) == list(range(10))
    # Drop 1 element
    assert list(drop_until(lambda x: x > 0, range(-10, 10))) == list(range(1, 10))
    # Drop all elements
    assert list(drop_until(lambda x: x > 10, range(-10, 10))) == []



# Generated at 2022-06-13 19:57:02.207099
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    state = random.getstate()
    random.seed(0)
    lst = [randint(0, 100) for _ in range(100)]
    random.setstate(state)
    assert list(MapList(lambda x: x + 1, lst)) == [x + 1 for x in lst]
    state = random.getstate()
    random.seed(0)
    assert [MapList(lambda x: x + 1, lst)[i]
            for i in range(100)] == [x + 1 for x in lst]
    random.setstate(state)
    state = random.getstate()
    random.seed(0)
    assert MapList(lambda x: x + 1, lst)[:] == [x + 1 for x in lst]
    random.setstate(state)


# Generated at 2022-06-13 19:57:11.172245
# Unit test for function drop_until
def test_drop_until():
    cases = [([1,2,3], lambda x: x == 3, [3]),
             ([1,1,1], lambda x: x == 3, []),
             ([1], lambda x: x == 3, []),
             ([], lambda x: x == 3, []),
             ([3], lambda x: x == 3, [3]),
             ([1,2,3,4,5], lambda x: x > 3, [4,5])]
    for case in cases:
        assert list(drop_until(case[1], case[0])) == case[2]



# Generated at 2022-06-13 19:57:16.687971
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(1, 5)
    assert r[2] == 3
    assert r[2:4] == [3, 4]
    assert r[-1] == 4
    assert r[:] == [1, 2, 3, 4]
    assert r[:2] == [1, 2]
    assert r[2:] == [3, 4]
    assert r[:-1] == [1, 2, 3]
    assert r[::2] == [1, 3]

# Generated at 2022-06-13 19:57:25.373127
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    lst = LazyList(range(100))
    assert isinstance(lst[0], int)
    assert isinstance(lst[50:60], list)
    assert len(lst[50:60]) == 10
    assert lst[4] == 4
    assert lst[0] == 0
    assert lst[-1] == 99
    assert lst[-2] == 98
    assert list(lst[30:60]) == list(range(30, 60))
    assert list(lst[45:45]) == []



# Generated at 2022-06-13 19:57:33.859419
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    test_range = Range(10)
    assert test_range[0] == 0
    assert test_range[1] == 1
    assert test_range[2] == 2
    assert test_range[3] == 3
    assert test_range[4] == 4
    assert test_range[5] == 5
    assert test_range[6] == 6
    assert test_range[7] == 7
    assert test_range[8] == 8
    assert test_range[9] == 9
    assert test_range[-1] == 9
    assert test_range[-2] == 8
    assert test_range[-3] == 7
    assert test_range[-4] == 6
    assert test_range[-5] == 5
    assert test_range[-6] == 4

# Generated at 2022-06-13 19:57:51.968145
# Unit test for function scanl
def test_scanl():
    assert list(scanl(lambda s, x: ''.join([x, s]), ['a', 'b', 'c', 'd'])) == ['a', 'ab', 'abc', 'abcd']
    assert list(scanl(lambda s, x: ''.join([x, s]), ['a', 'b', 'c', 'd'], 'e')) == ['e', 'ea', 'eab', 'eabc']
    assert list(scanl(lambda s, x: s + x, [1, 2, 3, 4], 0)) == [0, 1, 3, 6, 10]
    assert list(scanl(lambda s, x: s + x, [1, 2, 3, 4])) == [1, 3, 6, 10]
    assert list(scanl(lambda s, x: s + x, [])) == []


# Generated at 2022-06-13 19:58:03.585252
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    range_ = Range(10)
    assert range_[0] == 0
    assert range_[1] == 1
    assert range_[-1] == 9
    assert range_[-3] == 7

    range_ = Range(1, 10 + 1)
    assert range_[0] == 1
    assert range_[1] == 2
    assert range_[-1] == 10
    assert range_[-3] == 8

    range_ = Range(1, 11, 2)
    assert range_[0] == 1
    assert range_[1] == 3
    assert range_[-1] == 9
    assert range_[-3] == 5

    range_ = Range(1, 11, 3)
    assert range_[0] == 1
    assert range_[1] == 4

# Generated at 2022-06-13 19:58:07.106395
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x > 5, range(3))) == []



# Generated at 2022-06-13 19:58:18.643063
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    msg = ":method:`__getitem__` of :class:`Range` is broken"
    assert Range(10)[0] == 0, msg
    assert Range(10)[1] == 1, msg
    assert Range(1, 10 + 1)[2] == 2, msg
    assert Range(1, 10 + 1)[3] == 3, msg
    assert Range(1, 11, 2)[0] == 1, msg
    assert Range(1, 11, 2)[1] == 3, msg
    assert Range(1, 11, 2)[2] == 5, msg
    assert Range(1, 11, 2)[3] == 7, msg
    assert Range(1, 11, 2)[4] == 9, msg
    assert Range(10)[-1] == 9, msg

# Generated at 2022-06-13 19:58:35.598385
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(10)
    assert r[0] == r[-10] == 0
    assert r[5] == r[-5] == 5
    assert r[9] == r[-1] == 9
    assert r[10] == r[-0] == 10
    assert r[11] == r[-11] == 10

    r = Range(1, 10 + 1)
    assert r[0] == r[-9] == 1
    assert r[5] == r[-4] == 6
    assert r[9] == r[-1] == 10
    assert r[10] == r[-0] == 11

    r = Range(1, 11, 2)
    assert r[0] == r[-5] == 1
    assert r[5] == r[-1] == 11

# Generated at 2022-06-13 19:58:38.191295
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    range1 = Range(10)
    print(range1[0], range1[2], range1[4])
test_Range___getitem__()


# Generated at 2022-06-13 19:58:40.778247
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]



# Generated at 2022-06-13 19:58:45.134576
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]

test_drop_until()



# Generated at 2022-06-13 19:58:50.373751
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    lst = MapList(lambda x: x * x, [1, 2, 3])
    assert lst[0] == 1
    assert lst[1] == 4
    assert lst[2] == 9
    assert lst[-1] == 9
    assert lst[1:2] == [4]
    assert lst[0:3:2] == [1, 9]
    with pytest.raises(IndexError):
        lst[-4]
    with pytest.raises(IndexError):
        lst[3]


# Generated at 2022-06-13 19:58:52.409228
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]



# Generated at 2022-06-13 19:59:04.320554
# Unit test for function scanl
def test_scanl():
    assert list(scanl(operator.add, [1, 2, 3, 4])) == [1, 3, 6, 10]
    assert list(scanl(operator.add, [1, 2, 3, 4], 0)) == [0, 1, 3, 6, 10]
    assert list(scanl(lambda s, x: x + s, ['a', 'b', 'c', 'd'])) == ['a', 'ba', 'cba', 'dcba']



# Generated at 2022-06-13 19:59:10.954841
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    lst = [1, 2, 3, 4, 5]
    m = MapList(lambda x: x * x, lst)
    assert m[1] == m.func(lst[1])
    assert m[::2] == [m.func(x) for x in lst[::2]]

# Generated at 2022-06-13 19:59:18.508868
# Unit test for function drop_until
def test_drop_until():
    it = range(10)
    assert list(drop_until(lambda x: x > 5, it)) == list(it)[5:]
    it = range(10)
    assert list(drop_until(lambda x: x > 10, it)) == []
    it = range(10)
    assert list(drop_until(lambda x: x < 0, it)) == list(it)
    it = []
    assert list(drop_until(lambda x: x > 1, it)) == []


# Generated at 2022-06-13 19:59:21.785342
# Unit test for function drop_until
def test_drop_until():
    a = list(drop_until(lambda x: x > 5, range(10)))
    assert a == [6,7,8,9]


# Generated at 2022-06-13 19:59:31.542811
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(3)
    assert r[0] == 0
    assert r[1] == 1
    assert r[2] == 2
    r = Range(1, 4)
    assert r[0] == 1
    assert r[1] == 2
    assert r[2] == 3
    r = Range(1, 5, 2)
    assert r[0] == 1
    assert r[1] == 3
    assert r[2] == 5


# Generated at 2022-06-13 19:59:35.065188
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    assert Range(10)[0] == 0
    assert Range(-3, 3)[0] == 0
    assert Range(3, -3, -1)[0] == 3


# Generated at 2022-06-13 19:59:41.492454
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(5)
    assert r[0] == 0
    assert r[1] == 1
    assert r[-1] == 4
    assert r[-2] == 3
    assert r[-5] == 0
    assert r[2:4] == [2, 3]
    assert r[1:5:2] == [1, 3]
    assert r[-3:] == [2, 3, 4]
    assert r[-3::-1] == [2, 1, 0]


# Generated at 2022-06-13 19:59:53.325578
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    assert Range(10)[0] == 0
    assert Range(10)[1] == 1
    assert Range(10)[-1] == 9
    assert Range(10)[10] == raise_(IndexError, 'range object index out of range')
    assert Range(1, 10 + 1)[0] == 1
    assert Range(1, 10 + 1)[1] == 2
    assert Range(1, 10 + 1)[-1] == 10
    assert Range(1, 10 + 1)[10] == raise_(IndexError, 'range object index out of range')
    assert Range(1, 11, 2)[0] == 1
    assert Range(1, 11, 2)[1] == 3
    assert Range(1, 11, 2)[-1] == 9

# Generated at 2022-06-13 20:00:00.108115
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r0 = Range(1,10)
    assert r0[0] == 1
    assert r0[9] == 10
    assert r0[-1] == 10
    assert r0[1:3] == [2,3]
    assert r0[3:] == [4,5,6,7,8,9,10]
    r1 = Range(1,10,2)
    assert r1[0] == 1
    assert r1[-1] == 9
    assert r1[1:3] == [3,5]
    assert r1[3:] == [7,9]
    return


# Generated at 2022-06-13 20:00:09.061121
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 3, range(10))) == [4, 5, 6, 7, 8, 9]
    assert list(drop_until(lambda x: x % 3 == 0, range(10))) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert list(drop_until(lambda x: x % 5 == 0, range(10))) == [5, 6, 7, 8, 9]
    assert list(drop_until(lambda x: x > 10, range(10))) == []
    assert list(drop_until(lambda x: x > 5, range(1, 4))) == []
    
test_drop_until()


# Generated at 2022-06-13 20:00:18.393771
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    obj = Range(1, 10)
    print(obj[0], obj[0:10:1], obj[0:5:1], obj[-1])


# Generated at 2022-06-13 20:00:24.116025
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x % 5 == 0, range(10))) == [5, 6, 7, 8, 9]
    assert list(drop_until(lambda x: x % 2 == 0, range(10))) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert list(drop_until(lambda x: x >= 10, range(10))) == []



# Generated at 2022-06-13 20:00:28.865849
# Unit test for function drop_until
def test_drop_until():
    # no predicate match
    assert list(drop_until(lambda x: x == 3, range(10))) == []
    # all elements match
    assert list(drop_until(lambda x: x > 0, range(10))) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # some elements match
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]



# Generated at 2022-06-13 20:00:33.491348
# Unit test for function drop_until
def test_drop_until():
    for x in range(4):
        for xs in ([3,4,5], [0,1,2,3,4,5], [3,3,3,3,3], [1,2,3,4,5,6,7]):
            assert list(drop_until(lambda y: y >= x, xs)) == [y for y in xs if y >= x]



# Generated at 2022-06-13 20:00:44.670565
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():  
    r = Range(1, 10+1)  # (start, end)
    assert r[0] == 1
    assert r[2] == 3
    assert r[4] == 5
    assert r[6] == 7
    assert r[8] == 9
    assert r[10] == 11
    assert r[12] == 13
    assert r[14] == 15
    assert r[16] == 17
    assert r[18] == 19
    assert r[-1] == 10
    assert r[-2] == 8
    assert r[-4] == 6
    assert r[-6] == 4
    assert r[-8] == 2
    assert r[-10] == 0
    assert r[-12] == -2
 
    r = Range(0, 10+1, 2)  # (

# Generated at 2022-06-13 20:00:48.516956
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    """Tests:
    - method __getitem__ of class Range
    """
    r = Range(1, 11, 2)

    print(r[0], r[2], r[4])
    print(r[slice(0, 5, 2)])



# Generated at 2022-06-13 20:00:55.115666
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    assert Range(1,10,2)[-1] == 9
    assert Range(1,10,2)[1] == 3
    assert Range(1,10,2)[0] == 1
    assert Range(1,10,2)[1:3] == [3,5]
    try:
        Range(1,10,2)[2:1]
    except ValueError:
        pass
    else:
        assert False



# Generated at 2022-06-13 20:01:03.758991
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    assert MapList(id, []) == [], "Empty list"
    assert MapList(id, [1, 2, 3]) == [1, 2, 3], "Non-empty list"
    assert MapList(id, [1, 2, 3])[0] == 1, "First item of non-empty list"
    assert MapList(id, [1, 2, 3])[-1] == 3, "Last item of non-empty list"
    assert MapList(id, [1, 2, 3, 4, 5])[2:4] == [3, 4], "Slice of non-empty list"
    assert MapList(id, [1, 2, 3, 4, 5])[3:] == [4, 5], "Right slice of non-empty list"

# Generated at 2022-06-13 20:01:07.629375
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    from random import randint
    
    for i in range(10):
        len_ = randint(0, 10)
        a = [randint(-10, 10) for i in range(len_)]
        func = lambda i: a[i] ** 2
        b = MapList(func, a)
        for j in range(len_):
            assert b[j] == func(j), "Wrong answer for test case: {}, {}".format(a, func)
        

# Generated at 2022-06-13 20:01:13.807729
# Unit test for function drop_until
def test_drop_until():
    xs = [1, 2, 3, 4, 5]
    assert drop_until(lambda x: x > 2, xs) == [3, 4, 5]
    assert drop_until(lambda x: x > 5, xs) == xs
    assert list(drop_until(lambda x: x > 2, iter(xs))) == [3, 4, 5]
    assert list(drop_until(lambda x: x > 2, (x for x in xs))) == [3, 4, 5]



# Generated at 2022-06-13 20:01:36.859884
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    # String test
    assert MapList(lambda x: x * 2, "abc")[0] == 'aa'
    assert MapList(lambda x: x * 2, "abc")[1] == 'bb'
    assert MapList(lambda x: x * 2, "abc")[2] == 'cc'
    assert MapList(lambda x: x * 2, "abc")[slice(0, 2)] == ['aa', 'bb']
    assert MapList(lambda x: x * 2, "abc")[slice(0, 3, 2)] == ['aa', 'cc']
    assert MapList(lambda x: x * 2, "abc")[:] == ['aa', 'bb', 'cc']

    # List test
    assert MapList(lambda x: x * 2, [1, 2, 3])[0] == 2

# Generated at 2022-06-13 20:01:40.628391
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(10)
    r = Range(1, 10 + 1)
    r = Range(1, 11, 2)
    print(r[0], r[2], r[4])

test_Range___getitem__()

# Generated at 2022-06-13 20:01:50.796528
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    class Foo:
        def __init__(self, x: int) -> None:
            self.x = x

        def __str__(self):
            return f"Foo({self.x})"

        def __repr__(self):
            return str(self)

    a = [Foo(i) for i in range(5)]
    aa = MapList(lambda x: x.x, a)
    assert aa[0] == 0
    assert aa[1] == 1
    assert aa[2] == 2
    assert aa[3] == 3
    assert aa[4] == 4
    assert aa[-1] == 4
    assert aa[-2] == 3
    assert aa[-3] == 2
    assert aa[-4] == 1
    assert aa

# Generated at 2022-06-13 20:02:04.114148
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(2, 10)
    assertEqual(r[0], 2)
    assertEqual(r[1], 3)
    assertEqual(r[-1], 9)
    assertEqual(r[-2], 8)

    assertEqual(r[0:1], [2])
    assertEqual(r[1:3], [3, 4])
    assertEqual(r[3:], [5, 6, 7, 8, 9])
    assertEqual(r[:5], [2, 3, 4, 5, 6])
    assertEqual(r[2:2], [])
    assertEqual(r[-4:-1], [6, 7, 8])
    assertEqual(r[-3:3], [7, 8])

# Generated at 2022-06-13 20:02:12.609763
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x > 5, [])) == []
    assert list(drop_until(lambda x: x > 5, [3, 4, 5, 6, 7])) == [6, 7]
    assert list(drop_until(lambda x: x > 5, [6, 7])) == [6, 7]

