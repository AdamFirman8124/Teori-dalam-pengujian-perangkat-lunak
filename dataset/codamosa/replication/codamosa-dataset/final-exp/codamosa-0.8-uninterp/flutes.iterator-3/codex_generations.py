

# Generated at 2022-06-13 19:52:37.629848
# Unit test for function take
def test_take():
    assert list(take(5, range(1000000)))==[0, 1, 2, 3, 4]
test_take()


# Generated at 2022-06-13 19:52:39.648792
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]



# Generated at 2022-06-13 19:52:41.482923
# Unit test for method __iter__ of class LazyList
def test_LazyList___iter__():
    i = LazyList(range(10))
    assert i[0] == 0
    assert i[1] == 1



# Generated at 2022-06-13 19:52:50.988548
# Unit test for function drop_until
def test_drop_until():
    def test_with(expected, pred_fn, iterable):
        assert expected == list(drop_until(pred_fn, iterable))
    yield test_with, [], (lambda x: False), [1]
    yield test_with, [2], (lambda x: x > 1), [1, 2]
    yield test_with, [], (lambda x: x > 10), [1, 2, 3]
    yield test_with, [1, 2, 3], (lambda x: False), [1, 2, 3]
    yield test_with, [], (lambda x: False), []



# Generated at 2022-06-13 19:52:54.312777
# Unit test for method __iter__ of class LazyList
def test_LazyList___iter__():
    assert(list(LazyList([0, 1, 2])) == [0, 1, 2])
    assert(list(LazyList(x + 1 for x in [0, 1, 2])) == [1, 2, 3])

# Generated at 2022-06-13 19:53:01.903696
# Unit test for function take
def test_take():
    for n in range(10):
        for lst in [range(10), range(100), range(100)]:
            assert list(take(n, lst)) == list(lst)[:n]
    assert list(take(42, {})) == []
    assert list(take(0, range(10))) == []
    with pytest.raises(ValueError):
        _ = list(take(-1, range(10)))



# Generated at 2022-06-13 19:53:08.438996
# Unit test for function split_by
def test_split_by():
    a = list(split_by(range(10), criterion=lambda x: x % 3 == 0))
    assert a == [[1, 2], [4, 5], [7, 8]]
    a = list(split_by(" Split by: ", empty_segments=True, separator='.'))
    assert a == [[], ['S', 'p', 'l', 'i', 't'], ['b', 'y', ':'], []]



# Generated at 2022-06-13 19:53:14.664100
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    class_.assert_equal(aio.Range(-3,3,2)[-1],1)
    class_.assert_equal(aio.Range(-3,3,2)[0:2:2],[-3,1])
    class_.assert_equal(aio.Range(-3,3,2)[:], [-3,1])
    class_.assert_equal(aio.Range(-3,3,2)[-2::2],[-1,1])


# Generated at 2022-06-13 19:53:22.546028
# Unit test for function split_by
def test_split_by():
    assert list(split_by(range(10), criterion=lambda x: x % 3 == 0)) == [[1, 2], [4, 5], [7, 8]]
    assert list(split_by(" Split by: ", empty_segments=True, separator='.')) == [[], ['S', 'p', 'l', 'i', 't'],
                                                                                 ['b', 'y', ':'], []]


# Generated at 2022-06-13 19:53:27.346625
# Unit test for function split_by
def test_split_by():
    list(split_by(range(10), criterion=lambda x: x % 3 == 0))
    list(split_by(" Split by: ", empty_segments=True, separator='.'))
    try:
        list(split_by(range(10), criterion=lambda x: x % 3 == 0, separator='.'))
        assert False
    except ValueError:
        pass
    try:
        list(split_by(range(10)))
        assert False
    except ValueError:
        pass



# Generated at 2022-06-13 19:53:45.928269
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    assert([1, 2, 3] == Range(1, 10, 2)[0:3])
    assert([6] == Range(1, 10, 2)[3:4])
    assert([1, 2, 3] == Range(1, 10, 2)[:3])
    assert([6] == Range(1, 10, 2)[3:])
    assert(4 == Range(1, 10, 2)[2])
    assert(1 == Range(1, 10, 2)[0])
    assert(8 == Range(1, 10, 2)[-1])


# Generated at 2022-06-13 19:53:50.267547
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    lst = MapList(lambda x: x * x, [1, 2, 3, 4, 5])
    assert lst[2] == 9, "MapList[index] test failed"
    assert lst[0:3] == [1, 4, 9], "MapList[slice] test failed"

# Generated at 2022-06-13 19:54:04.467517
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    lst = LazyList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    assert 3 == lst[2]
    assert [1, 2, 3] == lst[:3]
    assert [4, 5, 6, 7] == lst[3:7]
    assert [8, 9, 10, 11] == lst[7:]
    assert [1, 2, 3, 4, 5, 6] == lst[:6]
    assert [1, 2, 3, 4] == lst[:4]
    assert [7, 8, 9, 10] == lst[6:]
    assert [7, 8] == lst[6:8]
    assert [1, 2, 3, 4] == lst[:4]

# Generated at 2022-06-13 19:54:12.593601
# Unit test for function drop
def test_drop():
    it=drop(5, range(10))
    assert next(it) == 5
    assert list(it) == [6, 7, 8, 9]
    it=drop(5, range(5))
    assert list(it) == []
    it=drop(15, range(0, 10))
    assert list(it) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    it=drop(0, range(0, 10))
    assert list(it) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    it=drop(-1, range(0, 10))
    assert list(it) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# Generated at 2022-06-13 19:54:21.772555
# Unit test for function drop
def test_drop():
    try:
        drop(1, []); assert False, "'drop(1, []' should raise ValueError"
    except ValueError:
        pass

    try:
        drop(1, range(10)); assert False, "'drop(1, range(10))' should raise ValueError"
    except ValueError:
        pass

    try:
        drop(0, range(10)); assert False, "'drop(0, range(10))' should raise ValueError"
    except ValueError:
        pass

    assert list(drop(1, [])    ) == [], "Drop from empty sequence"
    assert list(drop(1, [1])   ) == [], "Drop from single-element sequence"
    assert list(drop(2, [1])   ) == [], "Drop more than elements in sequence"

# Generated at 2022-06-13 19:54:26.401312
# Unit test for function drop
def test_drop():
    assert list(drop(5, range(10))) == list(range(5, 10))
    assert list(drop(0, range(10))) == list(range(10))
    assert list(drop(1, range(10))) == list(range(1, 10))
    assert list(drop(9, range(10))) == [9]
    assert list(drop(10, range(10))) == []



# Generated at 2022-06-13 19:54:29.585517
# Unit test for function drop
def test_drop():
    for i in range(10):
        assert list(drop(i, range(10))) == list(range(i, 10))



# Generated at 2022-06-13 19:54:35.363282
# Unit test for function scanl
def test_scanl():
    assert list(scanl(operator.add, [1,2,3,4], 0)) == [0, 1, 3, 6, 10]
    assert list(scanl(lambda s, x: x + s, ['a', 'b', 'c', 'd'])) == ['a', 'ba', 'cba', 'dcba']


# Generated at 2022-06-13 19:54:38.349969
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(1, 4)
    assert(r[0] == 1)
    assert(r[1] == 2)
    assert(r[2] == 3)
    assert(r[3] == 4)


# Generated at 2022-06-13 19:54:49.140449
# Unit test for function drop
def test_drop():
    assert list(drop(0, [1,2,3,4])) == [1,2,3,4]
    assert list(drop(1, [1,2,3,4])) == [2,3,4]
    assert list(drop(2, [1,2,3,4])) == [3,4]
    assert list(drop(3, [1,2,3,4])) == [4]
    assert list(drop(4, [1,2,3,4])) == []
    assert list(drop(5, [1,2,3,4])) == []


# Generated at 2022-06-13 19:55:04.863370
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(10)
    assert r[0] == r[-10]
    assert r[1] == r[-9]
    assert r[9] == r[-1]
    r = Range(2, 10)
    assert r[0] == r[-8]
    assert r[1] == r[-7]
    assert r[7] == r[-1]
    r = Range(1, 10, 2)
    assert r[0] == r[-5]
    assert r[1] == r[-4]
    assert r[4] == r[-1]
    assert r[-5] == 1
    assert r[-4] == 3
    assert r[-1] == 9
    assert r[0] == 1
    assert r[1] == 3

# Generated at 2022-06-13 19:55:14.409738
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r=Range(10)
    assert r[0] == 0
    assert r[1] == 1
    assert r[2] == 2
    assert r[3] == 3
    assert r[4] == 4
    assert r[5] == 5
    assert r[6] == 6
    assert r[7] == 7
    assert r[8] == 8
    assert r[9] == 9
    assert r[10] == 10

    assert r[-0] == 0
    assert r[-1] == 1
    assert r[-2] == 2
    assert r[-3] == 3
    assert r[-4] == 4
    assert r[-5] == 5
    assert r[-6] == 6
    assert r[-7] == 7
    assert r[-8] == 8

# Generated at 2022-06-13 19:55:21.811047
# Unit test for function chunk
def test_chunk():
    assert list(chunk(3, range(10))) == [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]
    assert list(chunk(3, range(0))) == []
    assert list(chunk(3, range(2))) == [[0, 1]]
    assert list(chunk(3, range(3))) == [[0, 1, 2]]
    assert list(chunk(3, range(4))) == [[0, 1, 2], [3]]
    assert list(chunk(3, [11, 12, 13, 14, 15])) == [[11, 12, 13], [14, 15]]
    assert list(chunk(3, [11, 12, 13])) == [[11, 12, 13]]



# Generated at 2022-06-13 19:55:29.374286
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    import random

    for _ in range(10):
        seq = [random.randint(0, 100) for _ in range(10)]
        func = lambda x: x * 2
        assert MapList(func, seq)[5] == func(seq[5])
        assert MapList(func, seq)[-1] == func(seq[-1])
        assert MapList(func, seq)[0:4] == [func(x) for x in seq[0:4]]



# Generated at 2022-06-13 19:55:39.947683
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
  test_cases = [
      ([0, 1, 2, 3, 4], int, 1, 1),
      ([0, 1, 2, 3, 4], int, [1, 3, 4], [1, 3, 4]),
      ([0, 1, 2, 3, 4], int, slice(1, 4), [1, 2, 3]),
      ([0, 1, 2, 3, 4], lambda x: x**2, 1, 1),
      ([0, 1, 2, 3, 4], lambda x: x**2, [1, 3, 4], [1, 9, 16]),
      ([0, 1, 2, 3, 4], lambda x: x**2, slice(1, 4), [1, 4, 9]),
  ]

# Generated at 2022-06-13 19:55:52.716592
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    my_test_range = Range(0, 99, 1)
    assert my_test_range[1] == 1
    assert my_test_range[-1] == 98
    assert my_test_range[2:4] == [2, 3]

# Generated at 2022-06-13 19:55:57.070385
# Unit test for function chunk
def test_chunk():
    seq = range(10)  # type: Iterable[int]
    itr = chunk(3, seq)
    assert list(itr) == list(chunk(3, seq))
    assert list(itr) == [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]



# Generated at 2022-06-13 19:56:00.766641
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    v = MapList(lambda x: x * x, [1, 2, 3])
    assert v[0] == 1
    assert v[1] == 4
    assert v[2] == 9
    assert list(v[:]) == [1, 4, 9]



# Generated at 2022-06-13 19:56:06.528457
# Unit test for function chunk
def test_chunk():
    print(list(chunk(3, range(10))))
    print(list(chunk(3, range(1))))
    print(list(chunk(3, [])))
    with pytest.raises(ValueError):
        list(chunk(0, range(10)))
test_chunk()



# Generated at 2022-06-13 19:56:16.980095
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    lst = LazyList(range(100))
    assert lst[:10] == list(range(10))
    assert lst[10:20] == list(range(10, 20))
    assert lst[:10] == list(range(10))
    assert lst[5] == 5
    assert lst[5:5] == []
    assert lst[5:0:-1] == list(range(5 - 1, -1, -1))
    assert lst[1:2][0] == 1
    assert lst[5::10] == [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]



# Generated at 2022-06-13 19:56:28.834977
# Unit test for function drop_until
def test_drop_until():
    assert [6, 7, 8, 9] == list(drop_until(lambda x: x > 5, range(10)))
    assert [0] == list(drop_until(lambda x: x > 5, range(1)))
    assert [] == list(drop_until(lambda x: x > 5, range(0)))
    it = iter(range(10))
    assert [1, 2, 3, 4, 5, 6, 7, 8, 9] == list(drop_until(lambda x: x > 0, it))
    assert [] == list(it)

# Generated at 2022-06-13 19:56:31.788699
# Unit test for function drop_until
def test_drop_until():
    l1 = drop_until(lambda x: x > 5, range(10))
    l2 = [6,7,8,9]
    assert(list(l1) == l2)
test_drop_until()



# Generated at 2022-06-13 19:56:34.404458
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]



# Generated at 2022-06-13 19:56:46.661579
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():

    def _for(obj):
        return [x for x in obj]

    def t(l, r, step, even=False):
        obj = Range(l, r, step)
        assert _for(obj) == _for(range(l, r, step))
        assert len(obj) == (r - l + (1 if even else 0)) // step
        assert obj[-1] == (r - l) - 1
        for idx in range(len(obj)):
            assert obj[idx] == obj[-idx - 1]
        lst = obj[:]
        assert lst == _for(range(l, r, step))
        assert obj[1:3] == _for(range(l + step, l + 3 * step, step))

# Generated at 2022-06-13 19:56:57.822166
# Unit test for function drop_until
def test_drop_until():
    from hypothesis import given
    from hypothesis import strategies as st

    @given(st.lists(st.integers()))
    def test_drop_until_property(a):
        i = iter(a)
        j = iter(drop_until(lambda x: x > 5, a))
        for x in a:
            y = next(i)
            if x > 5:
                z = next(j)
                assert y == z
            else:
                pass
        try:
            next(j)
        except StopIteration:
            pass

    test_drop_until_property()


# Generated at 2022-06-13 19:57:11.126402
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    r"""For each `i` in `[0, len(list))`, ``LazyList(list)[i]`` should be `list[i]`. For each `i` and `j` in `[0, len(list))`,
    ``LazyList(list)[i:j]`` should be `list[i:j]`.
    """
    def check(list: List[T]):
        lst = LazyList(list)
        for i in range(len(list)):
            assert lst[i] == list[i]

# Generated at 2022-06-13 19:57:18.696333
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    ll = LazyList(range(10))
    assert ll._exhausted is False
    assert ll._list == []

    assert list(ll[:]) == []
    assert ll._exhausted is False
    assert ll._list == []

    assert list(ll[:1]) == [0]
    assert ll._exhausted is False
    assert ll._list == [0]

    assert list(ll[:2]) == [0, 1]
    assert ll._exhausted is False
    assert ll._list == [0, 1]

    assert ll[0:0] == []
    assert ll._exhausted is False
    assert ll._list == [0, 1]

    assert list(ll[1:2]) == [1]
    assert ll._exhausted is False

# Generated at 2022-06-13 19:57:23.884011
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    lst = LazyList(range(5))
    assert lst[3] == 3
    assert lst[:3] == [0, 1, 2]
    assert lst[2:][:2] == [2, 3]
    assert len(lst) == 5


# Generated at 2022-06-13 19:57:27.951364
# Unit test for function drop_until
def test_drop_until():
    it = drop_until(lambda x: x > 5, range(10))
    assert next(it) == 6
    assert list(it) == list(range(7, 10))
    assert list(drop_until(lambda x: x > 5, range(5))) == []



# Generated at 2022-06-13 19:57:35.508209
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    lst0 = LazyList([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    assert lst0[0] == 0
    assert lst0[4] == 4
    assert lst0[4:6] == [4, 5]
    assert lst0[4:-1] == [4, 5, 6, 7, 8]
    assert lst0[2:2] == []
    assert lst0[-1] == 9
    assert lst0[-2] == 8
    assert lst0[-3:-1] == [7, 8]
    assert len(lst0) == 10
    assert list(lst0) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Generated at 2022-06-13 19:57:53.143907
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(1, 12, 4)
    assert r[0] == 1
    assert r[1] == 5
    assert r[2] == 9
    assert r[-1] == 9
    assert r[-2] == 5
    assert r[0:1] == [1]
    assert r[0:3] == [1, 5, 9]
    assert r[0:] == [1, 5, 9]
    assert r[:1] == [1]
    assert r[:3] == [1, 5, 9]
    assert r[:] == [1, 5, 9]
    assert r[:-1] == [1, 5]
    assert r[1:-1] == [5]
    assert r[2:-2] == []
    assert r[:] == [1, 5, 9]
   

# Generated at 2022-06-13 19:57:56.193283
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(10)
    range_obj = r.__getitem__(0)


# Generated at 2022-06-13 19:58:07.014525
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(5, 10)
    assert r[0] == r[-5] == 5
    assert r[-1] == 9
    assert r[-4] == 8
    with pytest.raises(IndexError):
        r[-6]
    with pytest.raises(IndexError):
        r[5]
    assert r[::2] == [5, 7, 9]
    assert r[::-1] == [9, 8, 7, 6, 5]



# Generated at 2022-06-13 19:58:17.065834
# Unit test for function drop_until
def test_drop_until():
    A = []
    B = [1, 2, 3]
    R = [1, 2, 3]
    assert list(drop_until(lambda x: x == 0, A)) == []
    assert list(drop_until(lambda x: x == 4, A)) == []
    assert list(drop_until(lambda x: x == 0, B)) == [1, 2, 3]
    assert list(drop_until(lambda x: x == 2, B)) == [2, 3]
    assert list(drop_until(lambda x: x == 4, B)) == [1, 2, 3]
    assert list(drop_until(lambda x: x == 0, R)) == [1, 2, 3]
    assert list(drop_until(lambda x: x == 2, R)) == [2, 3]

# Generated at 2022-06-13 19:58:27.389265
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(0,10,2)
    assert r[0] == 0
    assert r[1] == 2
    assert r[2] == 4
    assert r[3] == 6
    assert r[4] == 8
    assert isinstance(r[5],StopIteration)
    assert r[-1] == 8
    assert r[-2] == 6
    assert r[-3] == 4
    assert r[-4] == 2
    assert r[-5] == 0
    assert isinstance(r[-6],StopIteration)
    assert r[3:5] == [6,8]
    assert r[-5:-1] == [0,2,4,6]
    assert r[:] == [0,2,4,6,8]


# Generated at 2022-06-13 19:58:40.259568
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(10)
    assert r[0] == 0
    assert r[-1] == 9
    assert r[:5] == [0, 1, 2, 3, 4]
    assert r[2:7:2] == [2, 4, 6]
    assert r[-5:] == [5, 6, 7, 8, 9]
    r = Range(1, 10 + 1)
    assert r[0] == 1
    assert r[-1] == 10
    assert r[:5] == [1, 2, 3, 4, 5]
    assert r[2:7:2] == [3, 5, 7]
    assert r[-5:] == [6, 7, 8, 9, 10]
    r = Range(1, 11, 2)
    assert r[0] == 1

# Generated at 2022-06-13 19:58:47.371503
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(100)
    assert r[5] == 5
    assert r[-1] == 99
    assert r[3:10:2] == [3, 5, 7, 9]

# Generated at 2022-06-13 19:58:57.038580
# Unit test for function drop_until
def test_drop_until():
    def test_drop_until_1():
        # type: () -> None
        assert(list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9])

    def test_drop_until_2():
        # type: () -> None
        assert(list(drop_until(lambda x: x == 1, [0])) == [])

    test_drop_until_1()
    test_drop_until_2()



# Generated at 2022-06-13 19:59:07.495621
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r1 = Range(10)
    assert [r1[i] for i in range(0, len(r1))] == range(0, 10)

    r2 = Range(0, 10, 2)
    assert [r2[i] for i in range(0, len(r2))] == range(0, 10, 2)

    r3 = Range(1, 10, 3)
    assert [r3[i] for i in range(0, len(r3))] == range(1, 10, 3)

    r4 = Range(10, 0, -2)
    assert [r4[i] for i in range(0, len(r4))] == range(10, 0, -2)

    r5 = Range(9, 3, -2)

# Generated at 2022-06-13 19:59:19.409075
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    class TestRange(Range):
        def __getitem__(self, idx: object) -> object:
            return self._get_idx(idx)

    for (l, r, step) in [(0, 0, 1), (0, 4, 1), (1, 5, 2), (0, 10, 5)]:
        assert TestRange(l, r, step)[-1] == l
        assert TestRange(l, r, step)[0] == l
        if l % step == 0:
            assert TestRange(l, r, step)[len(TestRange(l, r, step)) - 1] == r - step
            assert TestRange(l, r, step)[len(TestRange(l, r, step))] == l # Exceed range

# Generated at 2022-06-13 19:59:30.159425
# Unit test for function drop_until
def test_drop_until():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert list(drop_until(lambda x: x == 5, lst)) == [5, 6, 7, 8, 9]
    assert list(drop_until(lambda x: x == 10, lst)) == []



# Generated at 2022-06-13 19:59:37.527114
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r0 = Range(10)
    r1 = Range(1, 10 + 1)
    r2 = Range(1, 11, 2)
    print(r0[0], r0[2], r0[4])
    print(r1[0], r1[2], r1[4])
    print(r2[0], r2[2], r2[4])
    print(r0[0:5])
    print(r1[0:5])
    print(r2[0:5])


# Generated at 2022-06-13 19:59:39.635830
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]



# Generated at 2022-06-13 19:59:51.216464
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    from functools import reduce
    from operator import mul
    assert Range(10)[0] == 0
    assert Range(10)[-1] == 9
    assert Range(10)[1:3] == [1, 2]
    assert Range(10)[:3] == [0, 1, 2]
    assert Range(10)[1:] == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert Range(10)[::2] == [0, 2, 4, 6, 8]
    assert Range(10)[-1::-1] == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert Range(10)[::-1] == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert list(Range(10))

# Generated at 2022-06-13 19:59:57.633153
# Unit test for function drop_until
def test_drop_until():
    #0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    assert [6, 7, 8, 9] == list(drop_until(lambda x: x > 5, range(10)))
    assert [4, 5, 6, 7, 8, 9] == list(drop_until(lambda x: x > 3, range(10)))
    assert list(drop_until(lambda x: x > 10, range(10))) == []
test_drop_until()


# Generated at 2022-06-13 20:00:05.628293
# Unit test for function drop_until
def test_drop_until():
    def predicate(x):
        return x > 3
    list_1 = [1, 2, 2, 1, 2, 3, 2, 1, 2, 3]
    assert list(drop_until(predicate,list_1)) == [4, 4, 3, 2, 1, 2, 3]
    list_2 = [4, 2, 4, 2, 1, 2, 3, 1, 4, 2, 3]
    assert list(drop_until(predicate, list_2)) == [4, 2, 4, 2, 1, 2, 3]



# Generated at 2022-06-13 20:00:11.669979
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    try:
        r = Range(10)
        result = r[0]
        assert result == 0
    except AssertionError:
        raise AssertionError()
    try:
        result = r[2]
        assert result == 2
    except AssertionError:
        raise AssertionError()
    try:
        result = r[4]
        assert result == 4
    except AssertionError:
        raise AssertionError()
    try:
        result = r[:]
        assert result == [0,1,2,3,4,5,6,7,8,9]
    except AssertionError:
        raise AssertionError()

# Generated at 2022-06-13 20:00:21.026014
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x != 1, range(1, 10))) == [2, 3, 4, 5, 6, 7, 8, 9]
    assert list(drop_until(lambda x: x != 1, list(range(10))[::-1])) == [0, 8, 7, 6, 5, 4, 3, 2]
    assert list(drop_until(lambda x: x != 'a', ['a', 'b', 'c'])) == ['b', 'c']



# Generated at 2022-06-13 20:00:30.583077
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(1, 10 + 1)
    assert r[0] == 1
    assert r[2] == 3
    assert r[4] == 5
    assert r[-2] == 9
    assert r[slice(2, 5)] == [3, 4, 5]
    assert r[slice(2, -1)] == [3, 4, 5, 6, 7, 8]
    assert r[slice(2, -2, 2)] == [3, 5, 7]


# Generated at 2022-06-13 20:00:36.658876
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r1 = Range(1, 10 + 1)
    assert r1[0] == 1
    assert r1[2] == 3
    assert r1[4] == 5
    assert r1[-1] == 10
    assert r1[-3] == 8
    assert r1[-5] == 6

    r2 = Range(1, 11, 2)
    assert r2[0] == 1
    assert r2[2] == 5
    assert r2[4] == 9
    assert r2[-1] == 9
    assert r2[-3] == 5
    assert r2[-5] == 1

    r3 = Range(10)[-1:0:-1]
    assert r3 == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]



# Generated at 2022-06-13 20:00:49.924074
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(5)
    assert r[0] == 0
    assert r[1] == 1
    assert r[2] == 2
    assert r[3] == 3
    assert r[4] == 4
    assert r[-5] == 0
    assert r[-4] == 1
    assert r[-3] == 2
    assert r[-2] == 3
    assert r[-1] == 4
    assert r[-6] == 0
    assert r[-9] == 0

    r = Range(1, 6)
    assert r[0] == 1
    assert r[1] == 2
    assert r[2] == 3
    assert r[3] == 4
    assert r[4] == 5
    assert r[-5] == 1
    assert r[-4] == 2
   

# Generated at 2022-06-13 20:01:00.350005
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    assert list(Range(0, 10, 2)[2:10:2]) == [6, 10]
    assert list(Range(0, 10, 2)[-10:-2:2]) == [0, 4, 8]
    assert list(Range(0, 10, 2)[-10:-2:2]) == [0, 4, 8]
    assert list(Range(0, -10, -2)[-10:-2:2]) == []
    assert list(Range(0, -10, -2)[-10:-2:2]) == []
    assert list(Range(0, -10, -2)[0:-10:-2]) == [0, -4, -8]
    assert list(Range(0, -10, -2)[0:-10:-2]) == [0, -4, -8]

# Generated at 2022-06-13 20:01:04.446869
# Unit test for function drop_until
def test_drop_until():
    assert [2, 3, 4, 5] == list(drop_until(lambda x: x > 1, range(6)))
    assert [] == list(drop_until(lambda x: x > 5, range(6)))



# Generated at 2022-06-13 20:01:05.196649
# Unit test for function drop_until
def test_drop_until():
    list(drop_until(lambda x: x > 5, range(10)))



# Generated at 2022-06-13 20:01:15.492004
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    import pytest

# Generated at 2022-06-13 20:01:19.913950
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(10)
    print(r[0], r[2], r[4])
    print(r[-1], r[-3], r[-5])
    print(r[:3], r[-3:], r[3:-3])
# End unit test


# Generated at 2022-06-13 20:01:24.514037
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x > 5, range(2))) == []
    assert list(drop_until(lambda x: x > 5, [])) == []
test_drop_until()


# Generated at 2022-06-13 20:01:30.814156
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    testlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert(list(Range(10))== testlist)
    assert(list(Range(5, 10 + 1))==[5, 6, 7, 8, 9, 10])
    assert (list(Range(5, 11, 2))==[5, 7, 9])
    assert(Range(10)[0]==1)
    assert(Range(10)[2]==3)
    assert(Range(10)[4]==5)


with open('./test/input1.txt', 'r') as myfile:
    data=myfile.read()
#print(data)
list1 = data.split()
#print(list1)

list_int = list(map(int, list1))
#print(list

# Generated at 2022-06-13 20:01:41.182189
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    for i in range(10):
        for j in range(10):
            for k in range(2, 10):
                r = Range(i, j, k)
                l = list(r)
                assert l[0] == r[0]
                assert len(l) == len(r)
                assert l[0] == r[0]
                assert l[-1] == r[-1]
                assert l[len(l) // 2] == r[len(r) // 2]
                assert l[:len(l) // 2] == r[:len(r) // 2]
                assert l[len(l) // 2:] == r[len(r) // 2:]



# Generated at 2022-06-13 20:01:49.031493
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6,7,8,9]
    assert list(drop_until(lambda x: True, range(10))) == [0,1,2,3,4,5,6,7,8,9]
    assert list(drop_until(lambda x: False, range(10))) == []
    assert list(drop_until(lambda x: x==5, range(10))) == [5]
    assert list(drop_until(lambda x: x > 10, range(10))) == []
    assert list(drop_until(lambda x: x < 0, range(10))) == []

# Generated at 2022-06-13 20:02:07.467455
# Unit test for function drop_until
def test_drop_until():
    a = list(range(10))
    assert list(drop_until(lambda x: x > 5, a)) == list(map(lambda x: x - 5, drop(5, a)))
    assert list(drop_until(lambda x: x < 0, a)) == a[:]
    assert list(drop_until(lambda x: x > 100, a)) == []

