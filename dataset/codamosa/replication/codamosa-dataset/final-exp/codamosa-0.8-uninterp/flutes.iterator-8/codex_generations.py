

# Generated at 2022-06-13 19:52:36.824689
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == list(range(6, 10))
    assert list(drop_until(lambda x: x > 5, range(4))) == []



# Generated at 2022-06-13 19:52:40.279229
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]



# Generated at 2022-06-13 19:52:50.393820
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(1, 10 + 1)  # (start, end)
    assert (r[1], r[2], r[3]) == (2, 3, 4)

    r = Range(1, 10 + 1, 2)  # (start, end, step)
    assert (r[1], r[2], r[3]) == (3, 5, 7)

    r = Range(10)         # (end)
    assert (r[1], r[2], r[3]) == (1, 2, 3)

    r = Range(0, 9, -1)
    assert (r[1], r[2], r[3]) == (8, 7, 6)


# Generated at 2022-06-13 19:52:53.037274
# Unit test for function take
def test_take():
    for i in range(20):
        for j in range(20):
            assert list(take(i, range(j))) == list(range(min(i, j)))



# Generated at 2022-06-13 19:53:02.413844
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    import bisect
    a = [1, 2, 3, 4, 5]
    pos = bisect.bisect_left(MapList(lambda x: x * x, a), 10, 0, len(a))
    print(pos)

    b = [2, 3, 4, 5, 6]
    pos = bisect.bisect_left(MapList(lambda i: a[i] * b[i], Range(len(a))), 10, 0, len(a))
    print(pos)



# Generated at 2022-06-13 19:53:09.612619
# Unit test for function chunk
def test_chunk():
    assert list(chunk(3, range(10))) == [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]
    assert list(chunk(3, range(7))) == [[0, 1, 2], [3, 4, 5], [6]]
    assert list(chunk(3, range(2))) == [[0, 1]]
    assert list(chunk(3, range(0))) == []
    assert list(chunk(3, range(-1))) == []
    assert list(chunk(3, range(-3))) == []



# Generated at 2022-06-13 19:53:19.484901
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    import random
    import string
    randstr = lambda: ''.join(random.choice(string.ascii_letters) for _ in range(20))
    r = Range(10, 1, -1)
    assert [r[i] for i in range(10)] == list(r)
    assert [r[i] for i in range(-10, 0)] == list(r)
    assert [r[i] for i in range(0, -10, -1)] == list(r)[::-1]
    # empty range
    r = Range(1, 10, -1)
    assert [r[i] for i in range(0)] == list(r)
    assert [r[i] for i in range(0)] == list(r)
    assert [r[i] for i in range(0, 0)] == list

# Generated at 2022-06-13 19:53:31.903619
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    from utils.testing import assert_list_equal
    lst = MapList(lambda x: x * x, [1, 2, 3, 4, 5])
    assert lst[0] == 1
    assert_list_equal(lst[0:2], [1, 4])
    assert_list_equal(lst[:2], [1, 4])
    assert_list_equal(lst[1:], [4, 9, 16, 25])
    assert_list_equal(lst[:], [1, 4, 9, 16, 25])
    assert_list_equal(lst[0:2:2], [1])
    assert_list_equal(lst[::2], [1, 9, 25])
    assert lst[0] == lst[-5]

# Generated at 2022-06-13 19:53:46.051073
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(10)
    assert [r[0], r[1], r[-1]] == [0, 1, 9]
    assert list(r[::-1]) == list(reversed(list(r)))
    r = Range(10, 21)
    assert [r[0], r[1], r[-1]] == [10, 11, 20]
    assert list(r[::-1]) == list(reversed(list(r)))
    r = Range(10, 21, 2)
    assert [r[0], r[1], r[-1]] == [10, 12, 20]
    assert list(r[::-1]) == list(reversed(list(r)))
    with pytest.raises(TypeError) as excinfo:
        len(r)
    r[0]


# Generated at 2022-06-13 19:53:49.005334
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]



# Generated at 2022-06-13 19:54:13.189170
# Unit test for function take
def test_take():
    list_1 = list(take(5, range(1000000)))
    assert list_1 == [0, 1, 2, 3, 4]
    assert len(list_1) == 5



# Generated at 2022-06-13 19:54:22.212750
# Unit test for function split_by
def test_split_by():
    assert list(split_by(" Split by: ", empty_segments=True, separator=' ')) == [[], ['S', 'p', 'l', 'i', 't'],
                                                                                 ['b', 'y', ':'], []]
    assert list(split_by(" Split by: ", empty_segments=False, separator=' ')) == [['S', 'p', 'l', 'i', 't'],
                                                                                 ['b', 'y', ':']]
    assert list(split_by(" Split by: ", empty_segments=True, criterion=lambda x: x == ' ')) == [[],
                                                                                               ['S', 'p', 'l', 'i', 't'],
                                                                                               ['b', 'y', ':'], []]

# Generated at 2022-06-13 19:54:33.946706
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    assert list(Range(1, 9, 2)) == [1, 3, 5, 7]
    assert Range(1, 9, 2)[0] == 1
    assert Range(1, 9, 2)[1] == 3
    assert Range(1, 9, 2)[2] == 5
    assert Range(1, 9, 2)[3] == 7
    assert Range(1, 9, 2)[-1] == 7
    assert Range(1, 9, 2)[-2] == 5
    assert Range(1, 9, 2)[-3] == 3
    assert Range(1, 9, 2)[-4] == 1
    assert Range(1, 9, 2)[:2] == [1, 3]
    assert Range(1, 9, 2)[2:] == [5, 7]

# Generated at 2022-06-13 19:54:39.325585
# Unit test for function drop_until
def test_drop_until():
    list(drop_until(lambda x: x > 5, range(10))) == range(6,10)
    list(drop_until(lambda x: x < 0, range(10))) == range(10)
    list(drop_until(lambda x: x > 20, range(10))) == []
    list(drop_until(lambda x: x > 5, [])) == []
    list(drop_until(lambda x: x > -1, [])) == []



# Generated at 2022-06-13 19:54:53.348209
# Unit test for function drop_until
def test_drop_until():
    from itertools import count
    from collections import deque
    from random import randint
    for counter in count():
        # Randomly generate test data
        n = randint(0, 50)
        l = deque(range(n))
        for _ in range(n):
            l.appendleft(randint(-50, 50))
        for _ in range(n):
            l.append(randint(-50, 50))
        l = list(l)
        # Randomly choose a pivot value
        pivot = l[randint(0, 2 * n)]
        print("[Test %d] l = %r, pivot = %r" % (counter, l, pivot))
        # Compute expected results
        expected = drop_until(lambda x: x >= pivot, range(n, 2 * n))
        got = drop_until

# Generated at 2022-06-13 19:55:02.765198
# Unit test for function take
def test_take():
    assert list(take(5, range(10))) == [0, 1, 2, 3, 4]
    assert list(take(0, range(10))) == []
    assert list(take(5, [1, 2, 3])) == [1, 2, 3]
    assert list(take(5, [])) == []
    with pytest.raises(ValueError) as excinfo:
        list(take(-1, range(10)))
    assert 'should be non-negative' in str(excinfo.value)
    assert len(list(take(5, range(5)))) == 5
    assert len(list(take(4, range(5)))) == 4

# Generated at 2022-06-13 19:55:06.617076
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    try:
        r = Range(3, 10, 2)
        print(len(r))
        print(r[0], r[2], r[4], r[-1])
        print(r[0:3], r[::2], r[:])
    except:
        print("error")


# Generated at 2022-06-13 19:55:16.405404
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    assert [0, 2] == Range(2)[0:2]
    assert [0, 2] == Range(2)[:2]
    assert [0, 2] == Range(2)[:-1]
    assert [2, 4, 6] == Range(2, 8, 2)[1:]
    assert [2, 4, 6] == Range(2, 8, 2)[1:100]
    assert [2, 4] == Range(2, 8, 2)[1:3]
    assert [0, 4 ,2] == Range(2, 6, 2)[::-1]
    assert [0, 2, 4 ,6 ,8] == Range(10)[::2]
    assert [0, 2, 4 ,6 ,8] == Range(10)[::-2]

# Generated at 2022-06-13 19:55:22.207197
# Unit test for function drop
def test_drop():
    def take(n: int, iterable: Iterable[T]) -> Iterator[T]:
        if n < 0:
            raise ValueError("`n` should be non-negative")
        try:
            it = iter(iterable)
            for _ in range(n):
                yield next(it)
        except StopIteration:
            pass
    it = drop(5,range(5))
    assert (list(it) == [])



# Generated at 2022-06-13 19:55:27.422875
# Unit test for function drop
def test_drop():
    assert list(take(3, drop(3, range(10)))) == [3,4,5]
    assert list(take(3, drop(4, range(10)))) == [4,5,6]
    assert list(drop(2, range(10))) == list(range(2,10))



# Generated at 2022-06-13 19:55:33.927294
# Unit test for method __len__ of class LazyList
def test_LazyList___len__():
  assert LazyList((1, 2, 3, 4))[:2].__len__() == 2



# Generated at 2022-06-13 19:55:42.214937
# Unit test for function drop_until
def test_drop_until():
    # Verify that if the iterable is empty drop_until should return an empty iterator
    assert len(list(drop_until(lambda x: x > 0, []) )) == 0
    # Verify that if the iterable has 0 or 1 element and the predicate is always false, 
    # drop_until should return an empty iterator
    assert len(list(drop_until(lambda x: x > 0, [0] ))) == 0
    assert len(list(drop_until(lambda x: x > 0, [0, 1] ))) == 0
    # Verify that if the iterable has 0 or 1 element and the predicate is always true, 
    # drop_until should return the whole iterator
    assert len(list(drop_until(lambda x: x < 0, [1] ))) == 1

# Generated at 2022-06-13 19:55:54.487599
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    assert Range(10)[0] == 0
    assert Range(10)[-2] == 8
    assert Range(10)[-1] == 9
    assert Range(10)[5] == 5
    assert Range(10)[10] == IndexError
    assert Range(10)[0:9] == [0, 1, 2, 3, 4, 5, 6, 7, 8]
    assert Range(10)[::2] == [0, 2, 4, 6, 8]
    assert Range(10)[::-1] == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert Range(10)[::-2] == [9, 7, 5, 3, 1]
    assert Range(10)[8:2:-2] == [8, 6, 4, 2]

# Generated at 2022-06-13 19:55:57.718894
# Unit test for method __len__ of class LazyList
def test_LazyList___len__():
    testcases = [
        (list(range(5)), 5),
    ]
    for iterable, length in testcases:
        assert len(LazyList(iterable)) == length

# Generated at 2022-06-13 19:56:13.837519
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x % 2 == 0, range(10))) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert list(drop_until(lambda x: False, range(10))) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert list(drop_until(lambda x: True, range(10))) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert list(drop_until(lambda x: True, [0])) == [0]
    assert list(drop_until(lambda x: True, [])) == []
test_drop_until

# Generated at 2022-06-13 19:56:23.776421
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    import random
    import operator
    import itertools

    def _test_lazy_list(it: Iterable[T], size: Optional[int], key=lambda _: _):
        if size is not None:
            it = itertools.islice(it, 0, size)
        lst = LazyList(it)
        lst_copy = []
        for _ in it:
            lst_copy.append(key(_))
        assert lst_copy == list(map(key, lst))
        if size is not None:
            assert len(lst) == size
        assert list(map(key, lst)) == lst_copy
        assert lst[:5] == list(map(key, lst))[:5]

# Generated at 2022-06-13 19:56:27.117561
# Unit test for method __iter__ of class LazyList
def test_LazyList___iter__():
    ll = LazyList([1, 2, 3])
    assert list(ll) == [1, 2, 3]
    assert list(ll) == [1, 2, 3]

# Generated at 2022-06-13 19:56:32.421353
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(4)
    assert r[-4:] == r[0:4] == [0, 1, 2, 3]
    assert r[-4:4] == r[0:4] == [0, 1, 2, 3]
    assert r[1:4:2] == [1, 3]
    assert r[-1:1:-1] == [3, 2]


# Generated at 2022-06-13 19:56:38.488912
# Unit test for method __len__ of class LazyList
def test_LazyList___len__():
    # The iterable appears infinite
    lst = LazyList(itertools.count())
    with pytest.raises(TypeError, match="__len__ is not available before the iterable is depleted"):
        len(lst)

    # Deplete the iterable
    lst = LazyList(range(1000))
    len(lst)



# Generated at 2022-06-13 19:56:46.144990
# Unit test for method __iter__ of class LazyList
def test_LazyList___iter__():
    lst = LazyList([1, 2, 3])
    for i, x in enumerate(lst):
        assert x == i + 1
    assert lst.exhausted
    assert list(lst) == list(lst)
    assert lst.__iter__() is lst
    assert lst.__getitem__(1) == 2
    assert lst.__getitem__(slice(1, 3)) == [2, 3]
    assert lst.__len__() == 3


# Generated at 2022-06-13 19:57:02.516717
# Unit test for function drop_until
def test_drop_until():
    from itertools import count
    assert list(drop_until(lambda x: x > 5, count())) == [6]
    assert list(drop_until(lambda x: x > 5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x > 5, [6, 7, 8, 9])) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x > 5, [5, 6, 7, 8, 9])) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x > 5, [4, 5, 6, 7, 8, 9])) == [6, 7, 8, 9]

# Generated at 2022-06-13 19:57:06.046193
# Unit test for function drop_until
def test_drop_until():
    res = drop_until(lambda x: x > 10, range(50))
    assert[x for x in res] == list(range(11,50))
    print("Function drop_until: PASSED")
test_drop_until()




# Generated at 2022-06-13 19:57:13.172063
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x < 0, range(10))) == list(range(10))
    assert list(drop_until(lambda x: x < 0, [])) == []
    assert list(drop_until(lambda x: x > 0, [-1, -2, -3])) == []



# Generated at 2022-06-13 19:57:16.215224
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]



# Generated at 2022-06-13 19:57:25.679875
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    range_ = Range(1, 10 + 1)
    assert list(range_[:]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert list(range_[::-1]) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert list(range_[2::-1]) == [3, 2, 1]
    assert isinstance(range_[5], int)
    assert isinstance(range_[::2], list)
    with pytest.raises(TypeError):
        len(range_)


# Generated at 2022-06-13 19:57:31.856208
# Unit test for function drop_until
def test_drop_until():
    def assert_drop_until(expected: Iterable[T], pred_fn: Callable[[T], bool], iterable: Iterable[T]):
        actual: List[T] = list(drop_until(pred_fn, iterable))
        assert actual == expected, f"Actual: {actual}, Expected: {expected}"

    assert_drop_until([6, 7, 8, 9], lambda x: x > 5, range(10))
    assert_drop_until([], lambda x: x > 5, range(5))



# Generated at 2022-06-13 19:57:34.342347
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
test_drop_until()


# Generated at 2022-06-13 19:57:48.534809
# Unit test for function drop_until
def test_drop_until():
    from .testing import assert_same_iterable
    from .testing import assert_strict_iterable_equal
    assert_same_iterable(
        drop_until(lambda x: x > 5, range(10)),
        (6, 7, 8, 9),
    )
    assert_strict_iterable_equal(
        drop_until(lambda x: x > 5, [1,2,3]),
        [],
    )
    assert_same_iterable(
        drop_until(lambda x: x < 0, range(5)),
        [],
    )
    assert_same_iterable(
        drop_until(lambda x: x < 0, range(6)),
        [5],
    )

# Generated at 2022-06-13 19:57:58.114398
# Unit test for function scanl
def test_scanl():
    assert list(scanl(operator.add, [1, 2, 3, 4], 0)) == [0, 1, 3, 6, 10]
    assert list(scanl(lambda s, x: x + s, ['a', 'b', 'c', 'd'])) == ['a', 'ba', 'cba', 'dcba']
    assert list(scanl(operator.mul, [1, 2, 3, 4], 2)) == [2, 2, 4, 12, 48]



# Generated at 2022-06-13 19:58:06.420108
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x > 5, range(6))) == []
    assert list(drop_until(lambda x: x > 5, range(5, 10))) == [5, 6, 7, 8, 9]



# Generated at 2022-06-13 19:58:21.432382
# Unit test for function drop_until
def test_drop_until():
    test_cases = (
        ([0, 1, 2, 3, 4, 5, 6], lambda x: x > 0, [1, 2, 3, 4, 5, 6]),
        ([0, 1, 2, 3, 4, 5, 6], lambda x: x > 5, [6]),
        ([0, 1, 2, 3, 4, 5, 6], lambda x: x > 10, []),
        ([0, 1, 2, 3, 4, 5, 6], lambda x: True, [0, 1, 2, 3, 4, 5, 6]),
        ([0, 1, 2, 3, 4, 5, 6], lambda x: False, []),
        ([], lambda x: True, []),
    )

# Generated at 2022-06-13 19:58:24.313115
# Unit test for function drop_until
def test_drop_until():
    for i in range(100):
        assert list(drop_until(lambda x: x > 2, range(i))) == list(range(3, i))

# Generated at 2022-06-13 19:58:38.913035
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(1, 10 + 1)
    assert(r[0] == 1)
    assert(r[2] == 3)
    assert(r[4] == 5)
    assert(r[-1] == 10)
    assert(r[-4] == 7)
    assert(r[-6] == 5)

    assert(r[0:1] == [1])
    assert(r[1:4] == [2, 3, 4])
    assert(r[-3:-1] == [8, 9])
    assert(r[10:13] == [])
    assert(r[-10:-7] == [])
    assert(r[0:10:2] == [1, 3, 5, 7, 9])

# Generated at 2022-06-13 19:58:48.399775
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    """
    Test case for method __getitem__ of class Range.
    """
    obj = Range(0, 100, 2)
    assert obj.__getitem__(0) == 0
    assert obj.__getitem__(5) == 10
    assert obj.__getitem__(20) == 40
    assert obj.__getitem__(-1) == 98
    assert obj.__getitem__(-2) == 96
    assert obj.__getitem__(slice(0, 5)) == [0, 2, 4, 6, 8]
    assert obj.__getitem__(slice(1, 7)) == [2, 4, 6, 8, 10, 12]

# Generated at 2022-06-13 19:58:50.636657
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]



# Generated at 2022-06-13 19:58:53.971067
# Unit test for function drop_until
def test_drop_until():
    test_tuple = "Hello", ",", " ", "World", "!"
    result = tuple(drop_until(lambda x: x == "World", test_tuple))
    assert result == ("World", "!")


# Generated at 2022-06-13 19:58:59.939130
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(10)
    expected = range(10)
    for i in expected:
        assert r[i] == expected[i]
    for i in range(10):
        assert r[i] == expected[i]
    for i in range(-10, 0):
        assert r[i] == expected[i]
    for i in range(-10):
        assert r[i] == expected[i]


# Generated at 2022-06-13 19:59:06.556040
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: False, range(10))) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert list(drop_until(lambda x: True, range(10))) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert list(drop_until(lambda x: True, [])) == []



# Generated at 2022-06-13 19:59:10.355906
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x > 10, range(10))) == []
    assert list(drop_until(lambda x: False, range(10))) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]



# Generated at 2022-06-13 19:59:21.441162
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(1, 10 + 1)
    assert r[0] == 1
    assert r[2] == 3
    assert r[4] == 5
    assert r[-1] == 10
    assert r[-2] == 9
    assert r[-4] == 7

    r = Range(1, 10 + 1, 2)
    assert r[0] == 1
    assert r[1] == 3
    assert r[2] == 5
    assert r[-1] == 9
    assert r[-2] == 7
    assert r[-3] == 5

    r = Range(1, 10 + 1)
    assert r[0:1] == [1]
    assert r[2:3] == [3]
    assert r[1:3] == [2, 3]

# Generated at 2022-06-13 19:59:40.080137
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    from random import randint
    l = [1, 2, 3, 4, 5]
    r = Range(1, len(l) + 1)
    assert list(r) == l
    assert r[0] == l[0]
    assert r[1] == l[1]
    assert r[-1] == l[-1]
    assert r[-2] == l[-2]
    assert r[0:3] == l[0:3]
    assert r[:3] == l[:3]
    assert r[2:] == l[2:]
    assert r[:] == l[:]
    assert r[:-1] == l[:-1]
    k = []
    for i in range(100):
        start = randint(0, len(l))

# Generated at 2022-06-13 19:59:51.309319
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    # Range[int]
    assert Range(3)[1] == 1
    assert Range(3)[-1] == 2
    assert Range(3)[::-1] == [2, 1, 0]
    assert Range(3, 6)[1] == 2
    assert Range(3, 6)[-2] == 4
    assert Range(3, 6)[::-1] == [5, 4, 3]
    assert Range(3, 6, 2)[1] == 4
    assert Range(3, 6, 2)[-1] == 4
    assert Range(3, 6, 2)[::-1] == [4, 2]
    assert Range(3, 5, 3)[::2] == [3]
    assert Range(3, 6, -1)[::-1] == []
    assert Range(3, 6, -1)[::1]

# Generated at 2022-06-13 19:59:54.109382
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6,7,8,9]



# Generated at 2022-06-13 20:00:02.022625
# Unit test for function drop_until
def test_drop_until():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert list(drop_until(lambda x: x % 3 == 0, data)) == [3, 4, 5, 6, 7, 8, 9, 10]
    assert list(drop_until(lambda x: x % 10 == 0, data)) == [10]



# Generated at 2022-06-13 20:00:03.957566
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]



# Generated at 2022-06-13 20:00:07.709393
# Unit test for function drop_until
def test_drop_until():
    cases = [
        (lambda x: x > 5, range(10), [6, 7, 8, 9]),
        (lambda x: x > 5, range(6), []),
    ]
    for f, i, e in cases:
        assert list(drop_until(f, i)) == e

# Generated at 2022-06-13 20:00:20.000420
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x > 5, [])) == []
    assert list(drop_until(lambda x: x > 5, [1, 2, 3])) == []
    assert list(drop_until(lambda x: x > 5, [1, 2, 3, 4, 5, 6])) == [6]
    assert list(drop_until(lambda x: x > 5, [1, 2, 3, 4, 5, 6, 7, 8, 9])) == [6, 7, 8, 9]


# Generated at 2022-06-13 20:00:30.383093
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, [])) == []
    assert list(drop_until(lambda x: x > 5, [1, 2, 3, 4, 5])) == []
    assert list(drop_until(lambda x: x > 5, [1, 2, 3, 4, 5, 6, 7])) == [6, 7]
    assert list(drop_until(lambda x: x > 5, [7, 6, 5, 4, 3, 2, 1])) == [7]



# Generated at 2022-06-13 20:00:36.309770
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():

    for i in range(100):
        start = random.randint(0,100)
        stop = random.randint(0,100)
        if stop < start:
            start, stop = stop, start
        step = random.randint(1,100)

        r = Range(start, stop, step)

        for j in range(100):
            idx = random.randint(-100,100)
            i = idx * step + start
            if i < start or i >= stop:
                try:
                    x = r[idx]
                    assert False, "should raise an exception when the index is out of range"
                except IndexError:
                    pass
            else:
                assert r[idx] == i
                assert isinstance(r[idx], int)

# Generated at 2022-06-13 20:00:42.291387
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    print("Testing method __getitem__ of class Range")
    testRange = Range(0, 100, 2)
    assert testRange[-1] == 98
    assert testRange[2:5] == [4, 6, 8]
    assert testRange[2:5:2] == [4, 8]
    print("Unit test for method __getitem__ of class Range succeeded")


# Generated at 2022-06-13 20:01:01.623500
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    assert (Range(10)          [0], Range(10)         [4], Range(10)         [8]) == (0, 4, 8)
    assert (Range(1, 10 + 1)  [0], Range(1, 10 + 1)  [4], Range(1, 10 + 1)  [8]) == (1, 5, 9)
    assert (Range(1, 11, 2)  [0], Range(1, 11, 2)  [4], Range(1, 11, 2)  [8]) == (1, 9, 17)
    
    # Test `__getitem__` with slice
    assert Range(10)          [:10] == list(map(int, range(0, 10)))

# Generated at 2022-06-13 20:01:04.407279
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]



# Generated at 2022-06-13 20:01:06.244928
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]



# Generated at 2022-06-13 20:01:14.743277
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    print('  testing method __getitem__')
    r = Range(7)
    assert(r == [0, 1, 2, 3, 4, 5, 6])
    assert(r[2: 3] == [2])
    assert(r[-1: -3: -1] == [6, 5])
    assert(r[::-1] == [6, 5, 4, 3, 2, 1, 0])
    with pytest.raises(IndexError):
        r[10]
    with pytest.raises(IndexError):
        r[-10]
    with pytest.raises(TypeError):
        r[0.0]
test_Range___getitem__()



# Generated at 2022-06-13 20:01:19.004490
# Unit test for function drop_until
def test_drop_until():
    test_data = list(range(10))
    # Case 1: no element satisfies the predicate
    res = list(drop_until(lambda x: x > 100, test_data))
    assert res == []
    # Case 2: all elements satisfy the predicate
    res = list(drop_until(lambda x: x > -1, test_data))
    assert res == test_data
    # Case 3: some elements satisfy the predicate
    res = list(drop_until(lambda x: x > 5, test_data))
    assert res == test_data[6:]


# Generated at 2022-06-13 20:01:27.883797
# Unit test for function drop_until
def test_drop_until():
    # empty
    assert list(drop_until(lambda x: x > 0, [])) == []
    assert list(drop_until(lambda x: x == 'a', '')) == []

    # drop nothing
    assert list(drop_until(lambda x: x > 0, [1, 2, 3])) == [1, 2, 3]
    assert list(drop_until(lambda x: x == 'a', 'abc')) == ['a', 'b', 'c']

    # drop all
    assert list(drop_until(lambda x: x > 0, [0, -1, -2, -3])) == []
    assert list(drop_until(lambda x: x == 'a', '123')) == []

    # drop some

# Generated at 2022-06-13 20:01:32.680394
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(10)
    assert r[0] == 0
    assert r[1] == 1
    assert r[3] == 3
    assert r[-1] == 9
    assert r[slice(2, 8, 2)] == [2, 4, 6]


# Generated at 2022-06-13 20:01:44.040552
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    import random
    for _ in range(200):
        num_args = random.randint(0, 3)
        args = []
        for _ in range(num_args):
            args.append(random.randint(-10, 10))
        if num_args == 0:
            args.append(1)
        if num_args == 1:
            args.append(args[0] + 1)
        if num_args == 2:
            args.append(1)

        built_in_range = range(*args)
        length = len(built_in_range)
        my_range = Range(*args)
        assert length == len(my_range)
        assert isinstance(my_range, Range)
        assert isinstance(my_range, Sequence)
        assert my_range == list(built_in_range)


# Generated at 2022-06-13 20:01:46.276197
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda c: c > 5, range(10))) == [6, 7, 8, 9]


# Generated at 2022-06-13 20:01:50.954017
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 3, range(10))) == [4, 5, 6, 7, 8, 9]
    assert list(drop_until(lambda x: x > 10, range(10))) == []
    assert list(drop_until(lambda x: False, range(10))) == list(range(10))


# Split a sequence with a condition.

# Generated at 2022-06-13 20:02:01.007925
# Unit test for function drop_until
def test_drop_until():
    l = list(drop_until(lambda x: x > 5, range(10)))
    print(l)



# Generated at 2022-06-13 20:02:11.217907
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r1 = Range(10)
    assert r1[0] == 0
    assert r1[2] == 2
    assert r1[4] == 4

    r2 = Range(1, 10)
    assert r2[0] == 1
    assert r2[2] == 3
    assert r2[4] == 5

    r3 = Range(1, 10 + 1, 2)
    assert r3[0] == 1
    assert r3[2] == 5
    assert r3[4] == 9

