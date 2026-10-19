

# Generated at 2022-06-13 19:52:31.385792
# Unit test for function take
def test_take():
    assert list(take(0, range(10))) == []
    assert list(take(5, range(10))) == [0, 1, 2, 3, 4]
    assert list(take(10, range(10))) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert list(take(100, range(10))) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# Generated at 2022-06-13 19:52:36.343077
# Unit test for function take
def test_take():
    assert list(take(5, range(100))) == [0, 1, 2, 3, 4]
    assert list(take(10, [1, 2, 3])) == [1, 2, 3]
    assert list(take(-1, range(10))) == []
    assert list(take(-1, [1, 2, 3])) == []
    assert list(take(0, range(10))) == []
test_take()



# Generated at 2022-06-13 19:52:41.314835
# Unit test for function drop
def test_drop():
    assert list(drop(2, [1, 2, 3])) == [3]


# Generated at 2022-06-13 19:52:53.316126
# Unit test for function chunk
def test_chunk():
    import itertools
    a = itertools.cycle(range(10))
    b = itertools.cycle(range(10))

    def test(n: int, a: Iterable[int], b: Iterable[int]) -> bool:
        return all(x == y for x, y in zip(chunk(n, a), b))

    # Test with a constant number of elements in one chunk
    assert test(1, range(10), range(10))
    assert test(2, range(10), range(0, 10, 2))
    assert test(2, range(9), range(0, 9, 2))
    assert test(3, range(10), range(0, 10, 3))
    assert test(3, range(9), range(0, 9, 3))

# Generated at 2022-06-13 19:53:01.758651
# Unit test for function split_by
def test_split_by():
    assert list(split_by(range(10), criterion=lambda x: x % 3 == 0)) == [[1, 2], [4, 5], [7, 8]]

    assert list(split_by(" Split by: ", empty_segments=True, separator='.')) == [[], ['S', 'p', 'l', 'i', 't'], ['b', 'y', ':'], []]
test_split_by()



# Generated at 2022-06-13 19:53:06.394323
# Unit test for function take
def test_take():
    assert list(take(5, range(10))) == list(range(5))
    assert list(take(5, range(3))) == list(range(3))
    assert list(take(-5, range(10))) == []
    raise Exception('test failed')



# Generated at 2022-06-13 19:53:10.176608
# Unit test for function take
def test_take():
    # Test normal case
    assert list(take(2, "abcd")) == ["a", "b"]
    # Test empty case
    assert list(take(0, "abcd")) == []
    # Test limit case
    assert list(take(100, "abcd")) == ["a", "b", "c", "d"]


# Generated at 2022-06-13 19:53:18.337497
# Unit test for method __next__ of class Range
def test_Range___next__():
    # Case 1: Normal case
    try:
        r = Range(3)
        assert next(r) == 0
        assert next(r) == 1
        assert next(r) == 2
        assert next(r) == 3
        try:
            next(r)
            assert False, 'should not reach here'
        except StopIteration:
            pass
        try:
            next(r)
            assert False, 'should not reach here'
        except StopIteration:
            pass
    except Exception as e:
        assert False, 'Exception raised: {}'.format(e)
    else:
        assert True


# Generated at 2022-06-13 19:53:29.172291
# Unit test for function split_by
def test_split_by():
    assert list(split_by(range(10), criterion=lambda x: x % 3 == 0)) == [[1, 2], [4, 5], [7, 8]]
    assert list(split_by(range(10), separator=3)) == [[0, 1, 2], [4, 5, 6, 7, 8, 9]]
    assert list(split_by(" Split by: ", empty_segments=True, separator=' ')) == [[], ['S', 'p', 'l', 'i', 't'],
                                                                                  ['b', 'y', ':'], []]



# Generated at 2022-06-13 19:53:31.645218
# Unit test for function chunk
def test_chunk():
    assert list(chunk(3, range(10))) == [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]


# Generated at 2022-06-13 19:53:51.960509
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    import itertools
    import random
    def test_slice(seq: Iterable) -> None:
        seq = LazyList(seq)
        assert_equal(len(seq), len(list(seq)))
        assert_equal(seq[:None], list(seq))
        assert_equal(seq[:], list(seq))
        assert_equal(seq[:len(seq)], list(seq))
        assert_equal(seq[:-1], list(seq)[:-1])
        assert_equal(seq[:-2], list(seq)[:-2])
        assert_equal(seq[::2], list(seq)[::2])
        assert_equal(seq[::-1], list(seq)[::-1])
        l = len(seq)
        n = len(seq) // 2
        seq[n:]  # for type

# Generated at 2022-06-13 19:53:55.098907
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]



# Generated at 2022-06-13 19:53:58.805034
# Unit test for method __iter__ of class LazyList
def test_LazyList___iter__():
    import pytest
    assert list(LazyList([])) == []
    assert list(LazyList([1,2,3])) == [1,2,3]

# Generated at 2022-06-13 19:54:04.962450
# Unit test for method __len__ of class LazyList
def test_LazyList___len__():
    iterable = range(10)
    lst = LazyList(iterable)
    assert len(lst) == 10
    assert len(lst) == 10
    lst = LazyList(iter(iterable))
    try:
        len(lst)
        raise AssertionError()
    except TypeError:
        pass



# Generated at 2022-06-13 19:54:10.174545
# Unit test for method __iter__ of class LazyList
def test_LazyList___iter__():
    lst = LazyList(range(1000000))
    assert list(take(5, lst)) == [0, 1, 2, 3, 4]
    assert list(lst) == list(range(1000000))

    lst = LazyList([1, 2, 3, 4])
    assert list(lst) == [1, 2, 3, 4]
    assert list(lst) == [1, 2, 3, 4]

# Generated at 2022-06-13 19:54:12.719441
# Unit test for function drop_until
def test_drop_until():
    assert take(5, drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]

# Generated at 2022-06-13 19:54:21.852491
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    l1 = list(range(10))
    l2 = Range(10)
    assert l1 == l2
    l1 = list(range(10))[::-1]
    l2 = Range(10)[::-1]
    assert l1 == l2
    l1 = list(range(10))[::2]
    l2 = Range(10)[::2]
    assert l1 == l2
    l1 = list(range(1, 11))
    l2 = Range(1, 11)
    assert l1 == l2
    l1 = list(range(1, 11))[::-1]
    l2 = Range(1, 11)[::-1]
    assert l1 == l2
    l1 = list(range(1, 11))[::2]

# Generated at 2022-06-13 19:54:28.998023
# Unit test for method __iter__ of class LazyList
def test_LazyList___iter__():
    assert list(LazyList(range(10))) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert list(LazyList(range(10))[3:]) == [3, 4, 5, 6, 7, 8, 9]
    assert list(LazyList(range(10))[6:]) == [6, 7, 8, 9]
    assert list(LazyList(range(10))[:6]) == [0, 1, 2, 3, 4, 5]
    assert list(LazyList(range(10))[:8:2]) == [0, 2, 4, 6]
    assert list(LazyList(range(10))[6:8:2]) == [6]

# Generated at 2022-06-13 19:54:34.893977
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    # Test __getitem__ for integer index
    s = MapList(lambda x: x + 1, [2, 3, 4, 5])
    assert s[-1] == 6 and s[1] == 4 and s[-1] == 6
    try:
        s[10]
        assert False
    except IndexError:
        pass
    # Test __getitem__ for slice index
    s = MapList(lambda x: x * x, [1, 2, 3, 4, 5, 6])
    assert s[0:2] == [1, 4] and s[:2] == [1, 4] and s[4:] == [25, 36] and s[1:-1] == [4, 9, 16, 25]


# Generated at 2022-06-13 19:54:36.636739
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    # test MapList.__getitem__()
    # assert allclose(expected, MapList.__getitem__(item))
    raise NotImplementedError


# Generated at 2022-06-13 19:56:58.744077
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    from bisect import bisect_left
    lst = MapList(lambda i: i, range(10))
    assert bisect_left(lst, 1) == 1
    assert bisect_left(lst, 3) == 3
    assert bisect_left(lst, 5) == 5



# Generated at 2022-06-13 19:57:07.346125
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    lst = LazyList(range(10))
    assert lst[0] == 0
    assert lst[1] == 1
    assert lst[-1] == 9
    # make sure invalid slice parameters don't raise exceptions
    lst[0:None:None]
    assert lst[5:] == list(range(5, 10))
    assert lst[1:5:2] == [1, 3]
    lst[0:-1]
    assert lst[1:5:2] == [1, 3]


# Generated at 2022-06-13 19:57:14.618126
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(2)
    assert [r[0], r[0], r[1]] == [0, 0, 1]
    assert r[0:2] == [0, 1]
    assert [r[0:2], r[:-1], r[-1:]] == [[0, 1], [0], [1]]
    r = Range(0, 9, 3)
    assert r[2] == 6
    assert r[1:] == [3, 6]


# Generated at 2022-06-13 19:57:20.502096
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    # Test getitem with index
    r = Range(0, 5)
    assert r[0] == 0
    assert r[2] == 2
    assert r[4] == 4
    assert r[-1] == 4
    # Test getitem with index out of range
    with raises(IndexError):
        r[5]
    with raises(IndexError):
        r[-6]
    # Test getitem with slice
    assert r[:5] == [0, 1, 2, 3, 4]
    assert r[2:5] == [2, 3, 4]
    assert r[:4:2] == [0, 2]
    assert r[::-1] == [4, 3, 2, 1, 0]
    assert r[:0:-1] == [4, 3, 2, 1]

# Generated at 2022-06-13 19:57:26.743623
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(10)
    assert r[0] == 0
    assert r[1] == 1
    assert r[-1] == 9
    assert r[:5] == [0, 1, 2, 3, 4]
    assert r[1:5:2] == [1, 3]
    assert r[5:] == [5, 6, 7, 8, 9]



# Generated at 2022-06-13 19:57:28.777013
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]



# Generated at 2022-06-13 19:57:37.364101
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():

    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    r = Range(1, 11)

    assert r[0] == 1
    assert r[5] == 6
    assert r[-1] == 10
    assert r[-5] == 6
    assert r[:5] == l[:5]
    assert r[:5:2] == l[:5:2]
    assert r[::2] == l[::2]

    try:
        r[11]
        assert False
    except IndexError:
        pass

    try:
        r[-11]
        assert False
    except IndexError:
        pass



# Generated at 2022-06-13 19:57:52.040310
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    a = LazyList(range(10))
    assert a[0] == 0
    assert a[1] == 1
    assert len(a) == 10
    assert a[2] == 2
    assert a[3] == 3
    assert a[9] == 9
    assert a[-1] == 9
    assert a[-5] == 5
    assert len(a) == 10
    assert a[:] == list(range(10))
    assert a[1:6] == [1, 2, 3, 4, 5]
    assert a[10:] == []
    assert a[-5:-1] == [5, 6, 7, 8]
    assert a[-5:1] == [5, 6, 7, 8, 9]

# Generated at 2022-06-13 19:57:57.999672
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    lst = MapList(lambda x: tuple(range(x)), [1, 2, 3])
    assert lst[0] == ((),)
    assert lst[2] == ((), (1,))
    assert lst[1:3] == [((),), ((), (1,))]

# Generated at 2022-06-13 19:58:03.499788
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    lst = LazyList(range(1000000))
    assert lst[0] == 0
    assert lst[5] == 5
    assert lst[5:10] == [5, 6, 7, 8, 9]



# Generated at 2022-06-13 19:58:13.506948
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(1, 2, 3)
    assert r[0] == 1
    assert r[-1] == 1
    assert r[1] == 4
    assert r[-2] == 4



# Generated at 2022-06-13 19:58:15.153883
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == list(range(6, 10))


# Generated at 2022-06-13 19:58:19.680348
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(1, 10 + 1)
    assert r[2:4] == [3, 4]
    assert r[2] == 3
    assert r[-1] == 10

# Generated at 2022-06-13 19:58:26.876350
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    assert Range(10)[5] == 5
    assert Range(1, 10)[5] == 6
    assert Range(1, 10, 2)[5] == 11
    assert Range(-10)[5] == -5
    assert Range(-10)[-5] == -5
    assert Range(1, 10)[::-2] == [9, 7, 5, 3, 1]
    assert Range(1, 10)[-2:2:-2] == [9, 7]
    assert Range(1, 10)[1:1:-2] == []


# Generated at 2022-06-13 19:58:36.940361
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    import itertools
    from utils.misc import randints
    from random import randint
    def test_generator():
        MAXN = 10 ** 3
        MAXLEN = 10 ** 2
        while True:
            n = randint(1, MAXN)
            yield ([randint(1, 10 ** 6) for _ in range(n)], randint(1, MAXLEN), randint(0, MAXLEN - 1))

    for lst, length, start in itertools.islice(test_generator(), 1000):
        expected = [x * x for x in lst[start : start + length]]
        result = MapList(lambda x: x * x, lst)[start : start + length]
        assert expected == result



# Generated at 2022-06-13 19:58:43.501072
# Unit test for function drop_until
def test_drop_until():
    class IncIterator:
        def __init__(self, start):
            self._value = start
        def __next__(self):
            result = self._value
            self._value += 1
            return result
        def __iter__(self):
            return self
    assert list(drop_until(lambda x: x == 3, IncIterator(0))) == [3, 4, 5, 6, 7, 8, 9, 10]



# Generated at 2022-06-13 19:58:58.053054
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    lst = [5, 4, 3, 2, 1]
    for i in lst:
        for j in lst:
            for k in lst:
                for start in lst:
                    for step in lst:
                        for stop in lst:
                            args = [start, stop]
                            if step != 1:
                                args.append(step)
                            r = Range(*args)
                            if i == 3:
                                assert r[j:k] == list(range(r._get_idx(j), r._get_idx(k)))
                            else:
                                assert r[j:k:i] == list(range(r._get_idx(j), r._get_idx(k), r._get_idx(i)))



# Generated at 2022-06-13 19:59:14.264000
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    from datetime import date
    from common.collections import MapList
    from common import UnitTestCase

    class TestMapList___getitem__(UnitTestCase):
        def test(self):
            holidays = [date(2000, 1, 1), date(2000, 1, 2), date(2000, 1, 3)]
            # Test the case where the function is `lambda x: x`.
            self.assertEqual(
                [x for x in MapList(lambda x: x, holidays)],
                holidays
            )
            # Test the case with other functions.
            self.assertEqual(
                [x.day for x in MapList(lambda x: x, holidays)],
                [x.day for x in holidays]
            )

# Generated at 2022-06-13 19:59:17.289682
# Unit test for function scanl
def test_scanl():
    assert list(scanl(operator.add, range(10)))
    assert list(scanl(operator.add, range(10), 1))


# Generated at 2022-06-13 19:59:28.884217
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    import pytest
    from itertools import tee

    lst = [2, 3, 5, 7, 11, 13]
    positive_squares = MapList(lambda x: x * x, lst)

    # test single-element indexing
    assert positive_squares[2] == 25

    # test slices
    assert positive_squares[0:3] == [4, 9, 25]
    assert positive_squares[5:5] == []

    # test slices for negative indexes
    assert positive_squares[-4:4] == positive_squares[2:4]

    # test slices for negative step size
    with pytest.raises(ValueError):
        positive_squares[::-1]

# Generated at 2022-06-13 19:59:42.761274
# Unit test for function drop_until
def test_drop_until():
    itr = range(10)
    assert list(drop_until(lambda x: x > 5, itr)) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x % 2 == 0, itr)) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert list(drop_until(lambda x: x == 5, itr)) == [5, 6, 7, 8, 9]
    assert list(drop_until(lambda x: x < 5, itr)) == []
    assert list(drop_until(lambda x: False, itr)) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Generated at 2022-06-13 19:59:54.252108
# Unit test for function scanl
def test_scanl():
    assert tuple(scanl(operator.add, [1, 2, 3, 4])) == (1, 3, 6, 10)
    assert tuple(scanl(lambda s, x: x + s, ['a', 'b', 'c', 'd'])) == ('a', 'ba', 'cba', 'dcba')
    assert tuple(scanl(operator.add, [1, 2, 3, 4], 0)) == (0, 1, 3, 6, 10)
    assert tuple(scanl(operator.add, [1, 2, 3, 4], 10)) == (10, 11, 13, 16, 20)
    with pytest.raises(ValueError):
        tuple(scanl(operator.add, [1, 2, 3, 4], 0, 1))



# Generated at 2022-06-13 20:00:04.214265
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, [1, 2, 3, 4, 5])) == []
    assert list(drop_until(lambda x: x > 5, [1, 2, 3, 4, 5, 6])) == [6]
    assert list(drop_until(lambda x: x > 5, [1, 2, 3, 4, 5, 6, 7])) == [6, 7]
    assert list(drop_until(lambda x: x > 5, [6, 7, 8, 9])) == [6, 7, 8, 9]



# Generated at 2022-06-13 20:00:08.493893
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r=Range(1, 10 + 1)
    print(r[0],r[2],r[4])
    print(r[1:5])

    r=Range(1, 10 + 1)
    print(r[:])

    r=Range(1, 10 + 1)
    print(r[::3])

if __name__ == '__main__':
    test_Range___getitem__()

# Generated at 2022-06-13 20:00:17.668300
# Unit test for function drop_until
def test_drop_until():
    assert tuple(drop_until(lambda x: x > 3, [])) == ()
    assert tuple(drop_until(lambda x: x > 3, [1, 2, 3, 4, 5])) == (4, 5)
    assert tuple(drop_until(lambda x: x == 1, [1])) == ()
    assert tuple(drop_until(lambda x: x == 1, [3, 1])) == ()
    assert tuple(drop_until(lambda x: x == 1, [3, 10, 1, 5])) == (1, 5)



# Generated at 2022-06-13 20:00:23.672824
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    for r in (Range(1, 11, 2), Range(1, 11), Range(11)):
        assert list(r[:]) == list(range(1, 11, 2 if r.step == 2 else 1))
        assert list(r[:2]) == list(range(1, 3, 2 if r.step == 2 else 1))
        assert list(r[:5:2]) == list(range(1, 5, 2 if r.step == 2 else 1))
        assert list(r[:-5]) == list(range(1, 6, 2 if r.step == 2 else 1))
        assert list(r[:-2]) == list(range(1, 9, 2 if r.step == 2 else 1))

# Generated at 2022-06-13 20:00:31.445836
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    # Base cases
    assert Range(1, 5)[0] == 1
    assert Range(1, 5)[2] == 3
    assert Range(1, 5)[1:3] == [2, 3]
    assert Range(1, 5)[2:2] == []
    # 5 -> 2, -1 -> 3
    assert Range(1, 5)[-3] == 2
    assert Range(1, 5)[-1] == 3
    # 5 -> []
    assert Range(1, 5)[4:4] == []
    # 4 -> [1, 3], -2 -> [2, 4]
    assert Range(1, 5)[0:4:2] == [1, 3]
    assert Range(1, 5)[1:4:2] == [2, 4]
    assert Range(1, 5)[1:5:2]

# Generated at 2022-06-13 20:00:37.181477
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(10)
    assert r[0] == 0
    assert r[1] == 1
    assert r[-1] == 9
    assert r[-2] == 8
    assert r[-10] == 0
    assert r[:2] == [0, 1]
    assert r[:4] == [0, 1, 2, 3]
    assert r[4:8] == [4, 5, 6, 7]
    assert r[4:] == [4, 5, 6, 7, 8, 9]
    assert r[::2] == [0, 2, 4, 6, 8]
    assert r[1:9:3] == [1, 4, 7]
    assert r[-2:2:-1] == [8, 7, 6, 5, 4]

# Generated at 2022-06-13 20:00:40.666776
# Unit test for function drop_until
def test_drop_until():
    iterable = range(10)
    actual = list(drop_until(lambda x: x > 5, iterable))
    expected = [6, 7, 8, 9]
    assert actual == expected



# Generated at 2022-06-13 20:00:48.782338
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(1, 10+1)
    assert r[0] == 1
    assert r[3] == 4
    assert r[-1] == 10
    assert r[1:6:2] == [2, 4, 6]
    assert r[1:5:2] == [2, 4]
    assert r[1:-1] == [2, 3, 4, 5, 6, 7, 8, 9]
    assert r[-3:-1] == [8, 9]
    assert r[-3:1] == []
    assert r[-3:1:-1] == [8, 7, 6, 5, 4]
    assert r[-3:1:1] == []
    assert r[-3:0:-1] == [8, 7, 6, 5, 4]

# Generated at 2022-06-13 20:01:17.998459
# Unit test for function drop_until
def test_drop_until():
    # Test general usage
    assert list(drop_until(lambda x: x >= 3, range(10))) == [3, 4, 5, 6, 7, 8, 9]
    # Test python equivalent
    assert list(drop_until(lambda x: x >= 3, range(10))) == list(itertools.dropwhile(lambda x: x < 3, range(10)))



# Generated at 2022-06-13 20:01:21.154329
# Unit test for method __getitem__ of class Range
def test_Range___getitem__(): 
    r = Range(10)     
    r = Range(1, 10 + 1)  
    r = Range(1, 11, 2)   

    print(r[0], r[2], r[4])

# Generated at 2022-06-13 20:01:29.053543
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(1, 10, 3)
    assert r[0] == 1
    assert r[1] == 4
    assert r[2] == 7
    assert r[-1] == 7
    assert r[-2] == 4
    assert r[-3] == 1
    assert list(r[1:3]) == [4, 7]
    assert list(r[-3:-1]) == [4, 7]
    r = Range(1, 3, 3)
    assert r[0] == 1
    assert r[-1] == 1
    assert len(r) == 1
    r = Range(0, 3, 3)
    assert r[0] == 0
    assert r[-1] == 0
    assert len(r) == 1
    r = Range(10)

# Generated at 2022-06-13 20:01:32.021133
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(10)
    assert r[0] == 0
    assert r[-1] == 9
    assert r[1:4:2] == [1, 3]



# Generated at 2022-06-13 20:01:37.792780
# Unit test for function drop_until
def test_drop_until():
    to_drop = [0, 1, 2, 3]
    assert list(drop_until(lambda x: x > 2, to_drop)) == [3]
    x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert list(drop_until(lambda y: y > 7, x)) == [8, 9]



# Generated at 2022-06-13 20:01:46.628238
# Unit test for function drop_until
def test_drop_until():
    test_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    test_list2 = [1, 3, 5, 7, 9]
    test_list3 = [0, 2, 4, 6, 8]
    assert list(drop_until(lambda x: x > 5, test_list1)) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x % 2 == 0, test_list2)) == []
    assert list(drop_until(lambda x: x % 2 == 0, test_list3)) == [0, 2, 4, 6, 8]



# Generated at 2022-06-13 20:01:51.241423
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6,7,8,9]
    assert list(drop_until(lambda x: x > 5, range(-3,3))) == []
    assert list(drop_until(lambda x: x > -1, range(-3,3))) == [-3,-2,-1,0,1,2]


# Generated at 2022-06-13 20:01:56.622188
# Unit test for function drop_until
def test_drop_until():
    lst = [2, 3, 1, 4, 5, 0, 8, 6]
    print(list(drop_until(lambda x: x > 5, lst)))
    # print(list(filter(lambda x: x > 3, lst)))
test_drop_until()


# Generated at 2022-06-13 20:02:02.426309
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x > 7, range(10))) == [8, 9]
    assert list(drop_until(lambda x: x > 9, range(10))) == []

