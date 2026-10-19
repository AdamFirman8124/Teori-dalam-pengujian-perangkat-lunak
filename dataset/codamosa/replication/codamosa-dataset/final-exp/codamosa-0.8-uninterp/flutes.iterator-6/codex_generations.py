

# Generated at 2022-06-13 19:52:44.362241
# Unit test for function drop
def test_drop():
    assert list(drop(3, ['a', 'b', 'c', 'd', 'e'])) == ['d', 'e']
    assert list(drop(0, ['a', 'b', 'c', 'd', 'e'])) == ['a', 'b', 'c', 'd', 'e']
    assert list(drop(5, ['a', 'b', 'c', 'd', 'e'])) == []
    assert list(drop(6, ['a', 'b', 'c', 'd', 'e'])) == []
    assert list(drop(3, [3, 7, 8, 4, 5, 6])) == [4, 5, 6]
    # negative n
    assert list(drop(-1, ['a', 'b', 'c', 'd', 'e'])) == []
    # exception is raised
    got_

# Generated at 2022-06-13 19:52:49.347938
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    assert Range(start=1, stop=3, step=1)[1] == 2
    assert Range(start=1, stop=4, step=2)[0:2] == [1, 3]
    assert Range(start=1, stop=4, step=1)[-1] == 3


# Generated at 2022-06-13 19:52:55.179402
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    lst = LazyList(range(10))
    assert lst[0] == 0
    assert lst[9] == 9
    assert lst[10] == 1
    assert lst[12] == 3
    assert lst[:3] == [0, 1, 2]
    assert lst[3:6] == [3, 4, 5]
    assert lst[6:] == [6, 7, 8, 9, 1, 2]

# Generated at 2022-06-13 19:52:59.643260
# Unit test for function take
def test_take():
    assert list(take(3, range(10))) == list(range(3))
    assert list(take(3, range(0))) == []
    try:
        list(take(-1, range(10)))
    except ValueError:
        pass



# Generated at 2022-06-13 19:53:10.663543
# Unit test for function chunk
def test_chunk():
    assert list(chunk(0, range(5))) == []
    assert list(chunk(1, range(5))) == [[0], [1], [2], [3], [4]]
    assert list(chunk(2, range(5))) == [[0, 1], [2, 3], [4]]
    assert list(chunk(3, range(5))) == [[0, 1, 2], [3, 4]]
    assert list(chunk(4, range(5))) == [[0, 1, 2, 3], [4]]
    assert list(chunk(5, range(5))) == [[0, 1, 2, 3, 4]]
    assert list(chunk(6, range(5))) == [[0, 1, 2, 3, 4]]
    assert list(chunk(0, [])) == []

# Generated at 2022-06-13 19:53:17.243112
# Unit test for function drop
def test_drop():
    assert list(drop(0, range(10))) == list(range(10))
    assert list(drop(1, range(10))) == list(range(1, 10))
    assert list(drop(10, range(10))) == []
    assert list(drop(100, range(10))) == []
    assert list(drop(0, [])) == []
    assert list(drop(1, [])) == []
    assert list(drop(100, [])) == []



# Generated at 2022-06-13 19:53:23.522642
# Unit test for function chunk
def test_chunk():
    assert list(chunk(3, range(10))) == [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]
    with pytest.raises(ValueError):
        list(chunk(0, range(10)))


# Generated at 2022-06-13 19:53:27.773146
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x == 1, [])) == []
    assert list(drop_until(lambda x: False, [1, 2, 3])) == [1, 2, 3]
    assert list(drop_until(lambda x: x == 1, [0, 1, 2, 3])) == [1, 2, 3]
    assert list(drop_until(lambda x: x == 2, [0, 1, 2, 3])) == [2, 3]



# Generated at 2022-06-13 19:53:30.147531
# Unit test for function drop
def test_drop():
    assert list(drop(5, range(10))) == list(range(5, 10))



# Generated at 2022-06-13 19:53:33.590038
# Unit test for function drop_until
def test_drop_until():
    it = iter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    assert list(drop_until(lambda x: x > 5, it)) == [6, 7, 8, 9, 10]
    assert list(drop_until(lambda x: x > 10, it)) == []
test_drop_until()



# Generated at 2022-06-13 19:53:46.970471
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    from random import sample
    from bisect import bisect_left
    from operator import itemgetter
    from typing import Tuple

    gt2 = lambda x: x + 2
    gt3 = lambda x: x + 3
    f = lambda x: x + 4
    g = lambda x: x + 5
    h = lambda x: x + 6
    lst1 = list(range(-10, 10))
    v = [(3,4)]

    # Test single: a[0] = f(lst1[0])
    ml = MapList(f, lst1)
    assert ml[0] == f(lst1[0])
    assert ml[1] == f(lst1[1])
    # Test single: a[0] = f(g(lst1[0]))
    ml = MapList

# Generated at 2022-06-13 19:53:53.881719
# Unit test for function split_by
def test_split_by():
    assert list(split_by(range(10), criterion=lambda x: x % 3 == 0)) \
        == [[1, 2], [4, 5], [7, 8]]
    assert list(split_by([1, 2, 3, 4], criterion=lambda x: x % 3 == 0)) \
        == [[1, 2], [4]]
    assert list(split_by([1, 2, 3, 4], criterion=lambda x: x % 3 == 0, empty_segments=True)) \
        == [[1, 2], [], [4]]
    assert list(split_by(" Split by: ", empty_segments=True, separator='.')) \
        == [[], ['S', 'p', 'l', 'i', 't'], ['b', 'y', ':'], []]

# Generated at 2022-06-13 19:54:07.468398
# Unit test for function split_by
def test_split_by():
    assert [[1, 2], [4, 5], [7, 8]] == list(split_by(range(10), criterion=lambda x: x % 3 == 0))
    assert [[], ['S', 'p', 'l', 'i', 't'], ['b', 'y', ':'], []] == list(split_by(" Split by: ", empty_segments=True, separator='.'))
    try:
        list(split_by(" Split by: ", empty_segments=False, separator='.'))
    except ValueError as e:
        assert str(e) == "Exactly one of `criterion` and `separator` should be specified"

# Generated at 2022-06-13 19:54:16.752358
# Unit test for method __iter__ of class LazyList
def test_LazyList___iter__():
    lst = LazyList(range(5))
    for x, y in zip(lst, range(5)):
        assert x == y
    for x, y in zip(lst, range(5,10)):
        assert x == y
    # make sure __iter__ is not called again after the iterable is depleted
    lst = LazyList(iter(range(5)))
    for x, y in zip(lst, range(5)):
        assert x == y
    for x, y in zip(lst, range(5)):
        assert x == y



# Generated at 2022-06-13 19:54:17.969649
# Unit test for method __iter__ of class LazyList
def test_LazyList___iter__():
    for _ in LazyList(range(10000)):
        pass

# Generated at 2022-06-13 19:54:20.438265
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    try:
        map_list = MapList(None, None)
    except AttributeError:
        pass


# Generated at 2022-06-13 19:54:21.037693
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    pass

# Generated at 2022-06-13 19:54:23.902836
# Unit test for method __iter__ of class LazyList
def test_LazyList___iter__():
    # Arrange
    lst = LazyList([1, 2, 3])
    # Act
    result = list(lst)
    # Assert
    assert result == [1, 2, 3]


# Generated at 2022-06-13 19:54:31.777320
# Unit test for function split_by
def test_split_by():
    assert list(split_by(" Split by: ", empty_segments=True, separator='.')) == [[], ['S', 'p', 'l', 'i', 't'],
                                                                                  ['b', 'y', ':'], []]
    assert list(split_by(range(10), criterion=lambda x: x % 3 == 0)) == [[1, 2], [4, 5], [7, 8]]

test_split_by()



# Generated at 2022-06-13 19:54:36.761450
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    assert LazyList(range(10000))[-1] == 9999
    assert LazyList(range(10000))[-3:-1] == [9997, 9998]
    assert LazyList(range(10000))[::2][:3] == [0, 2, 4]


# Generated at 2022-06-13 19:54:54.321295
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]



# Generated at 2022-06-13 19:55:02.207359
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 1, range(10, 20))) == [12, 13, 14, 15, 16, 17, 18, 19]
    assert list(drop_until(lambda x: x > 1, range(10, 10))) == []
    assert list(drop_until(lambda x: x > 0, range(10, 10))) == []
    assert list(drop_until(lambda x: x > -1, range(10, 10))) == []
    assert list(drop_until(lambda x: x > -2, range(10, 10))) == []



# Generated at 2022-06-13 19:55:08.383707
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, [1,2,3,4,5])) == []
    assert list(drop_until(lambda x: x > 5, [1,2,3,4,5, 6])) == [6]
    assert list(drop_until(lambda x: x > 5, [1,2,3,4,5,6,7])) == [6,7]
    assert list(drop_until(lambda x: x > 5, [6,7])) == [6,7]


# Generated at 2022-06-13 19:55:13.253660
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    a = [1, 2, 3, 4, 5]
    lst = MapList(lambda x: x * x, a)
    assert lst[0] == 1
    assert lst[1] == 4
    assert lst[2] == 9
    assert lst[0:4] == [1, 4, 9, 16]


# Generated at 2022-06-13 19:55:17.335015
# Unit test for function scanl
def test_scanl():
    assert list(scanl(operator.add, [1, 2, 3, 4], 0)) == [0, 1, 3, 6, 10]
    assert list(scanl(lambda s, x: x + s, ['a', 'b', 'c', 'd'])) == ['a', 'ba', 'cba', 'dcba']



# Generated at 2022-06-13 19:55:19.438541
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, [1,2,3,4,5,6,7])) == [6,7]



# Generated at 2022-06-13 19:55:25.478883
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    assert Range(10)[4] == 4
    assert Range(1, 10 + 1)[4] == 5
    assert Range(1, 11, 2)[2] == 5
    assert Range(1, 11, 2)[-1] == 9
    assert Range(1, 11, 2)[:-1] == [1, 3, 5, 7]
    assert Range(1, 11, 2)[-2:] == [7, 9]


# Generated at 2022-06-13 19:55:28.497987
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x>5, range(10))) == [6,7,8,9]



# Generated at 2022-06-13 19:55:33.780893
# Unit test for function drop_until
def test_drop_until():
    # Unit test for function drop_until
    @given(st.lists(elements=st.integers()))
    def test_integers(ls):
        assert list(drop_until(lambda x: x > 5, ls)) == [x for x in ls if x > 5]
    test_integers()



# Generated at 2022-06-13 19:55:41.165610
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    lst = list(range(10000))
    lazy_lst = LazyList(lst)
    for i in range(1000):
        assert lazy_lst[i] == lst[i]
    assert lazy_lst[999] == lst[999]
    assert lazy_lst[-1] == lst[-1]
    assert lazy_lst[-100] == lst[-100]
    assert lazy_lst[-100:] == lst[-100:]
    assert len(lazy_lst) == len(lst)
    for i in range(1000, 2000):
        assert lazy_lst[i] == lst[i]



# Generated at 2022-06-13 19:55:49.335038
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    rng = Range(1, 10+1)
    for i in range(-15, 20):
        print(i, rng[i])
    print(rng[0:5])
    print(rng[-5:])
    print(rng[:])

# Generated at 2022-06-13 19:55:54.402870
# Unit test for function drop_until
def test_drop_until():
    assert take(3, drop_until(lambda x: x > 5, range(10))) == [6, 7, 8]
    assert take(3, drop_until(lambda x: x > 1000, range(10))) == []
    assert take(3, drop_until(lambda x: False, range(10))) == [0, 1, 2]



# Generated at 2022-06-13 19:55:59.457779
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    obj = Range(1, 11, 2)
    assert obj[0] == 1
    assert obj[2] == 5
    assert obj[4] == 9
    assert obj[:2] == [1, 3]
    assert obj[2:4] == [5, 7]
    assert obj[:3:2] == [1, 5]

# Generated at 2022-06-13 19:56:02.108295
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]

# Generated at 2022-06-13 19:56:12.161629
# Unit test for function drop_until
def test_drop_until():
    it = range(10)
    assert list(drop_until(lambda x: x > 5, it)) == [6, 7, 8, 9]
    it = range(10)
    assert list(drop_until(lambda x: x < 5, it)) == [0, 1, 2, 3, 4]
    assert list(drop_until(lambda x: x > 20, it)) == []
    assert list(drop_until(lambda x: x == 0, it)) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert list(drop_until(lambda x: x > 2, drop(2, it))) == [3, 4, 5, 6, 7, 8, 9]


# Generated at 2022-06-13 19:56:16.209591
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    l = LazyList((x for x in range(10)))
    assert all(x == y for x, y in zip(l, range(10)))
    assert l[:5] == list(range(5))
    assert l[-1] == 9
    assert list(l) == range(10)



# Generated at 2022-06-13 19:56:23.263909
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(10)
    assert r[0] == 0
    assert r[1] == 1
    assert r[5] == 5
    assert r[-1] == 9
    assert r[-2] == 8
    assert r[:5] == [0, 1, 2, 3, 4]
    assert r[-5:] == [5, 6, 7, 8, 9]
    assert r[::-1] == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]



# Generated at 2022-06-13 19:56:33.595729
# Unit test for function drop_until
def test_drop_until():
    it = iter(range(10))
    assert list(drop_until(lambda x: x > 5, it)) == [6, 7, 8, 9]
    assert list(it) == []
    assert list(drop_until(lambda x: x == 7, range(10))) == [7, 8, 9]
    assert list(drop_until(lambda x: True, range(10))) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert list(drop_until(None, range(10))) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # Same as last assertion
    assert list(drop_until(lambda x: x, range(10))) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# Generated at 2022-06-13 19:56:36.509773
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    test = Range(1,1,1)
    assert test[1] == 1
    assert test[0] == 1
    assert test[-1] == 1

# Generated at 2022-06-13 19:56:45.968995
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    from math import sqrt

    lst = [9, 4, 25, 49]
    m = MapList(sqrt, lst)
    for i in range(len(lst)):
        assert m[i] == sqrt(lst[i])
    assert m[0:2] == list(map(sqrt, lst[0:2]))
    assert m[1::2] == list(map(sqrt, lst[1::2]))
    assert list(m.__iter__()) == list(map(sqrt, lst))


# Examples of function drop_while

# Generated at 2022-06-13 19:57:05.112302
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    # Test with __getitem__(idx: int)->R
    a = [1, 2, 3, 4, 5]
    b = MapList(lambda x: x * x, a)
    assert b[0] == 1
    assert b[1] == 4
    assert b[2] == 9
    assert len(b) == 5
    # Test with __getitem__(idx: slice)->List[R]
    assert b[0:2] == [1, 4]
    assert b[2:] == [9, 16, 25]
    assert b[:] == [1, 4, 9, 16, 25]
    assert b[-3:] == [9, 16, 25]


# Generated at 2022-06-13 19:57:15.862676
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    item = Range(5)
    if (0 != item[0]):
        raise RuntimeError("should be 0")
    if (1 != item[1]):
        raise RuntimeError("should be 1")
    if (2 != item[2]):
        raise RuntimeError("should be 2")

    if (1 != item[-4]):
        raise RuntimeError("should be 1")
    if (2 != item[-3]):
        raise RuntimeError("should be 2")
    if (3 != item[-2]):
        raise RuntimeError("should be 3")
    if (4 != item[-1]):
        raise RuntimeError("should be 4")

    if ([0, 1, 2] != item[0:3]):
        raise RuntimeError("should be [0, 1, 2]")

# Generated at 2022-06-13 19:57:20.564482
# Unit test for function drop_until
def test_drop_until():
    print(list(drop_until(lambda x: x > 5, [7, 1, 4, 6, 2, 5, 5])))
    print(list(drop_until(lambda x: x > 5, [7, 1, 4, 6, 2, 5, 5])))
#test_drop_until()


# Generated at 2022-06-13 19:57:31.378407
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    assert Range(10)[0] == 0
    assert Range(10)[10] == 9
    assert Range(10)[-1] == 9
    assert Range(10)[-10] == 0
    try:
        Range(10)[-11]
        assert False
    except IndexError:
        pass
    try:
        Range(10)[11]
        assert False
    except IndexError:
        pass

    assert Range(10)[:] == list(range(10))
    assert Range(10)[::-1] == list(reversed(range(10)))
    assert Range(10)[::-2] == list(reversed(range(0, 10, 2)))
    assert Range(10)[2:] == list(range(2, 10))
    assert Range(10)[:-2] == list(range(0, 8))

# Generated at 2022-06-13 19:57:37.582086
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    def test_Range___getitem___by_item():
        r = Range(1, 6)
        assert r[0] == r.l
        assert r[5] == r.r - 1
    """
    def test_Range___getitem___by_slice():
        r = Range(1, 6)
        assert r[:] == list(r)
        assert r[:-2] == list(r)[:-2]
    """
    test_Range___getitem___by_item()
    # test_Range___getitem___by_slice()

# Generated at 2022-06-13 19:57:45.954395
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    assert Range(10)[5] == 5
    assert Range(10)[-3] == 7
    assert Range(10)[slice(0, 5)] == [0, 1, 2, 3, 4]
    assert Range(10)[slice(5, 10)] == [5, 6, 7, 8, 9]
# End of unit test for method __getitem__ of class Range



# Generated at 2022-06-13 19:57:46.727529
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    pass

# Generated at 2022-06-13 19:57:51.103441
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    import doctest
    from .list import LazyList

    # Unit test for method __getitem__ of class LazyList
    doctest.run_docstring_examples(LazyList.__getitem__, globals(), verbose=True)



# Generated at 2022-06-13 19:57:58.708428
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x < 5, range(10))) == []
    assert list(drop_until(lambda x: x > 5, [])) == []
    assert list(drop_until(lambda x: x < 5, [])) == []
test_drop_until()



# Generated at 2022-06-13 19:58:04.231235
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    mapper = MapList(lambda item : item * 2, list(range(4)))
    assert mapper[0] == 0
    assert mapper[-1] == 6
    assert mapper[slice(1, 2)] == [2]


# Generated at 2022-06-13 19:58:24.566922
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    def test_getitem_basic():
        ll = LazyList(range(10))
        ll[5]
        ll[5]
        ll[7]

        assert ll[5] == 5
        assert ll[7] == 7
        assert ll[6] == 6
        assert ll[4] == 4

        assert ll[4:8] == list(range(4, 8))

        del ll
        assert gc.collect() == 0  # __del__ is not directly called, but indirectly called when the reference is cleared

    def test_getitem_invalid():
        ll = LazyList(range(5))
        with pytest.raises(IndexError):
            ll[5]

        ll = LazyList(range(5))
        with pytest.raises(IndexError):
            ll[5:10]



# Generated at 2022-06-13 19:58:35.713697
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    lst = LazyList(range(20))
    assert isinstance(lst, LazyList)
    assert len(lst) == 20
    assert list(lst) == list(range(20))
    assert lst[:10] == list(range(10))
    assert lst[:2] == [0, 1]
    assert lst[10:] == list(range(10, 20))
    assert lst[19] == 19
    assert lst[19:19] == []



# Generated at 2022-06-13 19:58:38.623202
# Unit test for function drop_until
def test_drop_until():
    prefix = range(10)
    def pred_fn(x):
        return x > 5
    assert list(drop_until(pred_fn, prefix)) == [6, 7, 8, 9]


# Generated at 2022-06-13 19:58:48.177504
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    # Test for overloaded method __getitem__ of class Range
    # Item getter
    r = Range(10)
    assert (r[0] == 0)
    assert (r[9] == 9)
    r = Range(1, 10 + 1)
    assert (r[0] == 1)
    assert (r[9] == 10)
    r = Range(1, 11, 2)
    assert (r[0] == 1)
    assert (r[4] == 9)
    # Slice getter
    assert (list(r[:]) == [1, 3, 5, 7, 9])
    assert (list(r[:-1]) == [1, 3, 5, 7])
    assert (list(Range(10)[2:5]) == list(range(2, 5)))

# Generated at 2022-06-13 19:58:53.067884
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    lst = LazyList(range(1000000))
    for _ in range(10000):
        assert lst[12345] == 12345
        assert lst[slice(0, 100)] == list(range(100))
    assert lst._fetch_until(999999) is None
    assert lst == list(range(1000000))
test_LazyList___getitem__()



# Generated at 2022-06-13 19:59:04.021625
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    assert Range(5)[0] == 0
    assert Range(5)[-1] == 4
    assert Range(5)[-5] == 0
    assert Range(5, 10)[-1] == 9
    assert Range(5, 10)[0] == 5
    assert Range(5, 10)[-5] == 5
    assert Range(5, 8)[-1] == 7
    assert Range(8, 5, -1)[-1] == 6
    assert Range(8, 5, -1)[0] == 8
    assert Range(8, 5, -1)[-4] == 8
    assert Range(8, 5, -1)[-5] == 8
    assert Range(5, 8, 2)[-1] == 7
    assert Range(5, 8, 2)[0] == 5

# Generated at 2022-06-13 19:59:11.781895
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    inst = Range(10)
    assert inst[0] == 0
    assert inst[2] == 2
    assert inst[4] == 4
    assert inst[-1] == 9
    assert inst[-4] == 6
    assert inst[0:4] == [0, 1, 2, 3]
    assert inst[0:-1] == [0, 1, 2, 3, 4, 5, 6, 7, 8]
    assert inst[1:4:2] == [1, 3]
    assert inst[-4:-1:2] == [6, 8]
    inst = Range(1, 10)
    assert inst[0] == 1
    assert inst[2] == 3
    assert inst[4] == 5
    assert inst[-1] == 9
    assert inst[-4] == 6

# Generated at 2022-06-13 19:59:22.872503
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    from copy import copy
    a = [1, 2, 3, 4, 5]
    x = MapList(lambda x: x * x, a)
    assert x[0] == 1
    assert x[1] == 4
    assert x[2] == 9
    assert x[3] == 16
    assert x[4] == 25
    assert x[-1] == 25
    assert x[:3] == [1, 4, 9]
    assert x[2:] == [9, 16, 25]
    assert x[1:3] == [4, 9]
    assert x[::2] == [1, 9, 25]
    assert x[::-1] == [25, 16, 9, 4, 1]
    assert copy(x) == a

# Generated at 2022-06-13 19:59:30.076166
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    ll = LazyList('abcdefgh')
    assert ll[5] == 'f'
    assert ll[-5] == 'c'
    assert ll[:5] == ['a', 'b', 'c', 'd', 'e']
    assert ll[::2] == ['a', 'c', 'e', 'g']
    assert ll[::-1] == ['h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']



# Generated at 2022-06-13 19:59:38.133621
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    import bisect
    from typing import Optional, Callable
    from functools import reduce
    from operator import mul
    from pytest import raises

    a = [1, 2, 3, 4, 5]
    pos = bisect.bisect_left(MapList(lambda x: x * x, a), 10)
    assert pos == 3

    b = [2, 3, 4, 5, 6]
    pos = bisect.bisect_left(MapList(lambda i: a[i] * b[i], Range(len(a))), 10)
    assert pos == 2



# Generated at 2022-06-13 19:59:59.336482
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    for i in range(10000):
        l = [i for i in Random.randint(1,100).sample(100)]
        for i in range(100):
            l1 = Range(0,l[i],1)
            l2 = range(0,l[i],1)
            assert(l1[l[i]-1] == l2[l[i]-1])
            assert(l1[i] == l2[i])
            assert(l1[l[i]-2] == l2[l[i]-2])
            assert(l1[l[i]-3] == l2[l[i]-3])
            assert(l1[l[i]-5] == l2[l[i]-5])
            assert(l1[l[i]-7] == l2[l[i]-7])

# Generated at 2022-06-13 20:00:03.111370
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(0,10)
    assert r[1] == 1
    assert r[0] == 0
    assert r[2:5] == [2, 3, 4]



# Generated at 2022-06-13 20:00:14.547354
# Unit test for function split_by
def test_split_by():
    assert list(split_by(['', '1', '', '2', '', '3', '', '', '4', ''])) == [['1'], ['2'], ['3'], [], ['4']]
    assert list(split_by(['', '1', '', '2', '', '3', '', '', '4', ''], empty_segments=True)) == \
        [[], ['1'], [], ['2'], [], ['3'], [], [], ['4'], []]
    assert list(split_by(range(7), criterion=lambda x: x % 3 == 0)) == [[1, 2], [4, 5]]

# Generated at 2022-06-13 20:00:24.191486
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    from utils.test_utils import test_this
    test_this(MapList(lambda x: x * x, [1, 2, 3, 4, 5])[0], 1)
    test_this(MapList(lambda x: x * x, [1, 2, 3, 4, 5])[0], 1)
    test_this(MapList(lambda x: x * x, [1, 2, 3, 4, 5])[3], 16)
    test_this(MapList(lambda x: x * x, [1, 2, 3, 4, 5])[-1], 25)
    test_this(MapList(lambda x: x * x, [1, 2, 3, 4, 5])[1:2], [4])

# Generated at 2022-06-13 20:00:31.583625
# Unit test for function drop_until
def test_drop_until():
    print("test case 1")
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
    print("test case 2")
    assert list(drop_until(lambda x: x > 5, [])) == []
    print("test case 3")
    assert list(drop_until(lambda x: x > 5, [2, 3, 4, 5, 6, 7])) == [6, 7]
    print("test case 4")
    assert list(drop_until(lambda x: x > 5, [6, 7])) == [6, 7]
    print("test case 5")
    assert list(drop_until(lambda x: x > 5, [7, 6])) == [7, 6]


# Generated at 2022-06-13 20:00:34.669707
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    m = MapList(lambda x: x * 2, [1, 2, 3])
    assertEq([2, 4, 6], m[:])  # noqa
    assertEq(2, m[0])
    assertEq([4, 6], m[1:])  # noqa

test_MapList___getitem__()


# Generated at 2022-06-13 20:00:45.728776
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    from hypothesis import given
    from .strategies import lists
    from .strategies import integers_from
    from .strategies import integers
    from typing import List
    from typing import Tuple
    from typing import Callable
    from typing import TypeVar
    from typing import Optional
    import hypothesis.strategies
    import operators

    Elem = TypeVar("Elem")
    Func = Callable[[Elem], Elem]
    Lst = List[Elem]
    Hyp = hypothesis.strategies.SearchStrategy[Lst]

    @given(hypothesis.strategies.integers())
    def test_map_list(seed: int) -> None:
        hypothesis.settings.register_profile("slow", deadline=None)
        hypothesis.settings.load_profile("slow")
        from hypothesis import settings
       

# Generated at 2022-06-13 20:00:47.345640
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    print(Range(10)[0])
    print(Range(1, 11, 2)[0:3:2])


# Generated at 2022-06-13 20:00:58.213833
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    assert list(Range(10)[:]) == list(range(10))
    assert list(Range(1, 10 + 1)[:]) == list(range(1, 10 + 1))
    assert list(Range(1, 10 + 1, 2)[:]) == list(range(1, 10 + 1, 2))
    assert list(Range(1, 10 + 1)[2:4]) == list(range(1, 10 + 1))[2:4]
    assert list(Range(1, 10 + 1, 2)[2:4]) == list(range(1, 10 + 1, 2))[2:4]
    assert Range(1, 10 + 1)[2:4] == range(1, 10 + 1)[2:4]

# Generated at 2022-06-13 20:01:08.054605
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x > 5, range(1, 11))) == [6, 7, 8, 9, 10]
    assert list(drop_until(lambda x: x > 0, range(10))) == []
    assert list(drop_until(lambda x: x > 10, range(10))) == []
    assert list(drop_until(lambda x: x > -10, range(10))) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    try:
        list(drop_until(lambda x: x > 5, range(0, 10, -1)))
        assert False, 'Expect ValueError'
    except ValueError:
        pass



# Generated at 2022-06-13 20:01:26.208415
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    assert Range(5)[1] == 1
    assert Range(3)[-1] == 2
    assert Range(3)[2] == 2
    assert Range(3)[-2] == 1
    assert Range(3)[-3] == 0
    assert Range(3)[3] == IndexError
    assert Range(3)[-4] == IndexError
    assert Range(2)[:1][0] == Range(2)[:1]
    assert Range(5)[1:4] == [1, 2, 3]
    assert Range(5)[1:] == [1, 2, 3, 4]
    assert Range(5)[:4] == [0, 1, 2, 3]
    assert Range(5)[:] == [0, 1, 2, 3, 4]
    assert Range(5)[::2] == [0, 2, 4]


# Generated at 2022-06-13 20:01:32.180895
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    assert (Range(1,10,2)[0] == 1)
    assert (Range(1,10,2)[-1] == 9)
    assert (Range(1,10,2)[1] == 3)
    assert (Range(1,10,2)[2] == 5)
    assert (Range(1,10,2)[-2] == 7)

# Generated at 2022-06-13 20:01:35.972229
# Unit test for function drop_until
def test_drop_until():
    def fn1(x: int) -> bool:
        return x > 5
    assert list(drop_until(fn1, range(10))) == [6, 7, 8, 9]


# Generated at 2022-06-13 20:01:46.721849
# Unit test for function drop_until
def test_drop_until():
    # Test a list
    lst = list(drop_until(lambda x: x > 0, range(-5, 5)))
    assert lst == [1, 2, 3, 4]
    # Test an iterator
    lst = list(drop_until(lambda x: x > 0, range(-5, 5)))
    assert lst == [1, 2, 3, 4]
    # Test an empty list
    lst = list(drop_until(lambda x: x > 0, range(-5, -1)))
    assert lst == []
    # Test an empty iterator
    def never_positive() -> Iterator[int]:
        x = -5
        while x < 0:
            yield x
            x += 1
    lst = list(drop_until(lambda x: x > 0, never_positive()))

# Generated at 2022-06-13 20:01:48.808971
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]

# Generated at 2022-06-13 20:01:52.808199
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
test_drop_until()



# Generated at 2022-06-13 20:02:05.564778
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    for i in range(-5, 5):
        for j in range(-5, 5):
            for k in range(-5, 5):
                if not (k == 0):
                    assert list(Range(i,j,k))[:] == Range(i,j,k)[:]  # tests: (start, end, step)
                if not (j == i):
                    assert list(Range(j))[:i] == Range(j)[:i]  # tests: (end)
                    assert list(Range(i,j))[i:j] == Range(i,j)[i:j]  # tests: (start, end)
                    assert list(Range(i,j,k))[:i:j] == Range(i,j,k)[:i:j]  # tests: (start, end, step)