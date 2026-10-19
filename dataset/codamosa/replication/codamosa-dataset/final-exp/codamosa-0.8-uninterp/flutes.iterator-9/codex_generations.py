

# Generated at 2022-06-13 19:52:44.358077
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 1, [0, 1, 2])) == [2]
    assert list(drop_until(lambda x: x > 1, [0, 1, 0])) == []
    assert list(drop_until(lambda x: x > 1, [])) == []
    assert list(drop_until(lambda x: x > 1, "hello")) == ["l", "l", "o"]
    assert list(drop_until(lambda x: x > 1, "h")) == []
    assert list(drop_until(lambda x: x > 1, "hl")) == []
    assert list(drop_until(lambda x: x > 1, "h1")) == ["1"]



# Generated at 2022-06-13 19:52:48.960147
# Unit test for function drop
def test_drop():
    assert list(drop(0, [1, 2])) == [1, 2]
    assert list(drop(2, [1, 2])) == []
    with pytest.raises(ValueError):
        list(drop(-1, [1, 2]))



# Generated at 2022-06-13 19:52:57.326903
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(1, 5)
    assert isinstance(r, Range)
    assert r[0] == 1
    assert r[1] == 2
    assert r[2] == 3
    assert r[3] == 4
    assert r[-1] == 4
    assert isinstance(r[0:2], list)
    assert r[0:2] == [1, 2]
    assert isinstance(r[0:], list)
    assert r[0:] == [1, 2, 3, 4]
    assert isinstance(r[:2], list)
    assert r[:2] == [1, 2]
    assert isinstance(r[:], list)
    assert r[:] == [1, 2, 3, 4]


# Generated at 2022-06-13 19:53:00.624822
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    for n in range(-10, 10):
        for step in range(1, 10):
            r = Range(20, 299, step)
            assert r[n] == r._get_idx(n)
    for end in range(1, 10):
        r = Range(end)
        for n in [0, 1, -1, 2, -2]:
            assert r[n] == r._get_idx(n)



# Generated at 2022-06-13 19:53:02.391239
# Unit test for method __iter__ of class LazyList
def test_LazyList___iter__():
    l = LazyList(range(10))
    l2 = list(l)


# Generated at 2022-06-13 19:53:07.464866
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    import itertools
    x = LazyList(itertools.count())
    assert x[0] == 0
    assert x[1] == 1
    assert x[-1] == -1
    assert x[:3] == [0, 1, 2]
    assert x[::2] == [0, 2, 4, 6, 8]



# Generated at 2022-06-13 19:53:18.215155
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(10)
    assert r[0] == 0
    assert r[1] == 1
    assert r[9] == 9

    r = Range(1, 10 + 1)
    assert r[0] == 1
    assert r[1] == 2
    assert r[8] == 9
    assert r[9] == 10

    r = Range(1, 11, 2)
    assert r[0] == 1
    assert r[1] == 3
    assert r[3] == 7
    assert r[4] == 9

    r = Range(2, 11, 2)
    assert r[0:2] == [2, 4]
    assert r[0:3] == [2, 4, 6]
    assert r[:4:2] == [2, 6, 10]



# Generated at 2022-06-13 19:53:31.706668
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x >= 0, range(-5, 5))) == list(range(-5, 5))
    assert list(drop_until(lambda x: x == 'a', 'bcdefghij')) == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    assert list(drop_until(lambda x: x * 2 == 6, [1, 2, 3, 4])) == [3, 4]
    assert list(drop_until(lambda x: x == False, [True, True, True, False])) == [False]

# Generated at 2022-06-13 19:53:34.666255
# Unit test for function drop
def test_drop():
    assert list(drop(5, range(10))) == [5, 6, 7, 8, 9]



# Generated at 2022-06-13 19:53:38.003359
# Unit test for function take
def test_take():
    n = 5
    it = range(1000000)
    it = take(n=n, iterable=it)
    assert list(take(n=n, iterable=it)) == list(range(n))


# Generated at 2022-06-13 19:54:06.909745
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 0, range(5))) == list(range(0, 5))
    assert list(drop_until(lambda x: x > 5, range(10))) == list(range(6, 10))
test_drop_until()



# Generated at 2022-06-13 19:54:13.325316
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
  seq = list(range(1000000))
  for idx in range(len(seq) // 2):
    assert seq[idx] == LazyList(seq)[idx]
  acc_idx = 0
  for idx in range(len(seq) // 2, len(seq)):
    while seq[acc_idx] == LazyList(seq)[acc_idx]:
      acc_idx += 1
    assert seq[idx] == LazyList(seq)[idx]
    acc_idx += 1
  assert LazyList(seq) == LazyList(seq)
  for idx in range(len(seq) // 2):
    assert seq[idx] == LazyList(seq[idx])



# Generated at 2022-06-13 19:54:17.176299
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
        test_input= [0, 1, 2, 3, 4, 5]
        test_length = 6
        test_class = Range(6)
        expected_output = test_input
        output = test_class.__getitem__(slice(len(test_input)))
        assert output == expected_output


# Generated at 2022-06-13 19:54:26.406961
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    import random

    for i in range(100):
        l = [random.randint(0, 1000) for _ in range(10)]
        l1 = MapList(lambda x: x * 2, l)
        l2 = MapList(lambda x: x - 1, l)
        l3 = MapList(lambda x: x + 10, l)

        assert l1[3] == l[3] * 2
        assert l1[5:8] == [x * 2 for x in l[5:8]]
        assert list(l2[3:]) == [(x - 1) for x in l[3:]]
        assert list(l3[1:10:2]) == [(x + 10) for x in l[1:10:2]]

# Generated at 2022-06-13 19:54:34.089314
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    c = Range(1, 5 + 1)
    c = Range(1, 11, 2)
    c = Range(1, 5 + 1)
    c = Range(1, 11, 2)
    temp = c[0]
    temp = c[1]
    temp = c[2]
    temp = c[3]
    temp = c[4]
    temp = c[-1]

# Generated at 2022-06-13 19:54:37.369352
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    from itertools import count
    lst = LazyList(count(0))
    assert lst[:3] == [0, 1, 2]
    assert lst[:6] == [0, 1, 2, 3, 4, 5]
    for i in range(10000):
        assert lst[i] == i

# Generated at 2022-06-13 19:54:51.432147
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(-2, 3)
    assert_eq(r[0], -2)
    assert_eq(r[1], -1)
    assert_eq(r[2], 0)
    assert_eq(r[3], 1)
    assert_eq(r[-1], 1)
    assert_eq(r[-2], 0)
    assert_eq(r[-5], -2)
    assert_eq(r[0:3], [-2, -1, 0])
    assert_eq(r[0:3:2], [-2, 0])
    assert_eq(r[0:2:-1], [])
    assert_eq(r[0:2:-2], [])
    assert_eq(r[3:0:-1], [1, 0, -1])

# Generated at 2022-06-13 19:54:59.333671
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    for i in range(5):
        for j in range(5):
            for k in range(5):
                result = Range(i, j, k)[:]
                if k == 0:
                    assert result == [i]
                elif k == 1:
                    assert result == list(range(i, j))
                elif j < i:
                    assert result == []
                else:
                    assert result == [i + k * x for x in range((j - i - 1) // k + 1)]



# Generated at 2022-06-13 19:55:08.645288
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    # test single index
    assert Range(10)[0] == 0
    assert Range(10)[1] == 1
    assert Range(10)[-1] == 9
    assert Range(2, 10)[0] == 2
    # test slices
    assert Range(10)[:] == list(range(10))
    assert Range(10)[:3] == list(range(3))
    assert Range(10)[1:3] == list(range(1, 3))
    assert Range(10)[2:4] == list(range(2, 4))
    assert Range(10)[-1:-1] == list(range(-1, -1))
    assert Range(2)[:3:2] == list(range(0, 3, 2))
    assert Range(2, 10)[:3:2] == list(range(2, 3, 2))

# Generated at 2022-06-13 19:55:18.403095
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    from random import randint
    from io import StringIO
    from unittest import TestCase
    import re

    class _TestLazyList(TestCase):
        def check(self, iterable: Iterable[T], idx: int, expected: Optional[T]):
            obj = LazyList(iterable)
            if expected is None:
                with self.assertRaises(IndexError):
                    obj[idx]
            else:
                self.assertEqual(obj[idx], expected)

        def test__getitem__(self):
            # Not iterable
            self.check([1, 2, 3], randint(4, 10), None)
            # Single element, not iterable
            self.check((4,), randint(4, 10), None)
            # Single element, iterable

# Generated at 2022-06-13 19:55:29.269207
# Unit test for function split_by
def test_split_by():
    assert list(split_by(range(10), criterion=lambda x: x % 3 == 0)) == [[1, 2], [4, 5], [7, 8]]
    assert list(split_by(" Split by: ", empty_segments=True, separator='.')) == [[], ['S', 'p', 'l', 'i', 't'], ['b', 'y', ':'], []]
test_split_by()



# Generated at 2022-06-13 19:55:39.295920
# Unit test for function split_by
def test_split_by():
    assert list(split_by(range(10), criterion=lambda x: x % 3 == 0)) == [[1, 2], [4, 5], [7, 8]]
    assert list(split_by(" Split by: ", empty_segments=True, separator='.')) == [[], ['S', 'p', 'l', 'i', 't'],
                                                                                ['b', 'y', ':'], []]
    with pytest.raises(ValueError):
        list(split_by(range(10), criterion=lambda x: x % 3 == 0, separator=0))
    with pytest.raises(ValueError):
        list(split_by(range(10), criterion=None, separator=0))



# Generated at 2022-06-13 19:55:52.166886
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    #__getitem__ with type(x) == int
    def test_Range_getitem_int(x):
        r = Range(1,4)
        first = r[x]
        second = r[x]
        third = r[x]
        return first == second and second == third
    #__getitem__ with type(x) == list
    def test_Range_getitem_list(x):
        r = Range(1,4)
        first = r[x]
        second = r[x]
        third = r[x]
        return first == second and second == third
    test_Range_getitem_int(1)
    test_Range_getitem_int(1)
    test_Range_getitem_int(1)
    test_Range_getitem_int(2)
    test_

# Generated at 2022-06-13 19:55:57.070394
# Unit test for function split_by
def test_split_by():
    input_string = list("Split By")
    expected_split_string = [["S", "p", "l", "i", "t"], ["B", "y"]]
    split_string = list(split_by(input_string, criterion=lambda x: x == " "))
    assert split_string == expected_split_string

test_split_by()



# Generated at 2022-06-13 19:56:05.200489
# Unit test for function split_by
def test_split_by():
    for l in [
        [],
        [0],
        [1, 2],
        [0, 0],
        [0, 0, 1, 0, 2, 3, 0, 0, 4, 0, 0],
        [0, 0, 1, 0, 2, 3, 0, 0, 0],
        [0, 0, 0],
    ]:
        # test criterion
        assert list(split_by(l, criterion=lambda x: x == 0)) == [x for x in l if x != 0]
        assert list(split_by(l, criterion=lambda x: x == 0, empty_segments=True)) == [
            [] if y == 0 else y for y in l]
        # test separator

# Generated at 2022-06-13 19:56:14.139406
# Unit test for function split_by
def test_split_by():
    assert list(split_by(' Split by: ', empty_segments=True, separator='.')) == [[], ['S', 'p', 'l', 'i', 't'],
                                                                                  ['b', 'y', ':'], []]
    assert list(split_by([0, 2, 4, 2, 0], empty_segments=True, criterion=lambda x: x % 2 == 0)) == [[], [2], [4],
                                                                                                   [2], []]
    assert list(split_by([0, 2, 4, 2, 0], criterion=lambda x: x % 2 == 0)) == [[2], [4], [2]]



# Generated at 2022-06-13 19:56:24.101190
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    l = LazyList(range(10))
    assert list(l) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert len(l) == 10
    assert l[5] == 5
    assert l[-5] == 5
    with pytest.raises(TypeError):
        len(l)  # until this point, the length is not cached
    assert l[:5] == [0, 1, 2, 3, 4]
    assert l[-5:] == [5, 6, 7, 8, 9]
    assert l[::-1] == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert l[3:8:2] == [3, 5, 7]

# Generated at 2022-06-13 19:56:30.262519
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    rng = range(1000)
    for i in rng:
        assert LazyList(rng)[i] == i
    assert LazyList(rng)[0:4] == [0, 1, 2, 3]
    assert LazyList(rng)[0:10:2] == [0, 2, 4, 6, 8]
    assert LazyList(rng)[1000] == 1000



# Generated at 2022-06-13 19:56:37.283502
# Unit test for function split_by
def test_split_by():
    assert list(split_by(range(10), criterion=lambda x: x % 3 == 0)) == [[1, 2], [4, 5], [7, 8]]
    assert list(split_by(" Split by: ", empty_segments=True, separator='.')) == [[], ['S', 'p', 'l', 'i', 't'], ['b', 'y', ':'], []]
    
test_split_by()


# Generated at 2022-06-13 19:56:41.581700
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(5, 10)
    assert r[2] == 7
    assert r[-1] == 9
    assert r[-3:-1] == [7, 8]
    assert r[:2] == [5, 6]

# Generated at 2022-06-13 19:56:52.962795
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x == 3, [1, 2, 3])) == [3]
    assert list(drop_until(lambda x: x == 3, [1, 2])) == []



# Generated at 2022-06-13 19:56:57.942850
# Unit test for function take
def test_take():
    object_list = [1,2,3]
    assert iter(take(2, object_list)) != 1, "failure"
    assert iter(take(2, object_list)) != 2, "failure"
    return("Test complete")
test_take()


# Generated at 2022-06-13 19:57:11.221152
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    print("Unit Test: Range.__getitem__()")
    r1 = Range(10)
    print("r1[0] = " + str(r1[0]))
    assert r1[0] == 0
    print("r1[-1] = " + str(r1[-1]))
    assert r1[-1] == 9
    print("r1[:-1] = " + str(r1[:-1]))
    assert r1[:-1].tolist() == [0, 1, 2, 3, 4, 5, 6, 7, 8]
    print("r1[-4:] = " + str(r1[-4:]))
    assert r1[-4:].tolist() == [6, 7, 8, 9]

# Generated at 2022-06-13 19:57:13.796426
# Unit test for function chunk
def test_chunk():
    m = list(chunk(3, range(10)))
    assert m == [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]


# Generated at 2022-06-13 19:57:20.069601
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    def _eq(r1, r2):
        return all(x == y for x, y in zip(r1, r2))
    _Range = Range(0, 10, 2)
    print(_Range[0])
    print(_Range[1])
    print(_Range[0:2])
    print(_Range[:2])
    print(_Range[::2])
    print(_Range[1::2])
    print(_Range[3:])
    print(_Range[:-1])
    print(_Range[-1])
    assert _eq(_Range[0], 0)
    assert _eq(_Range[1], 2)
    assert _eq(_Range[0:2], [0, 2])
    assert _eq(_Range[:2], [0, 2])

# Generated at 2022-06-13 19:57:25.581589
# Unit test for function drop_until
def test_drop_until():
    iterable = range(1, 11)
    for i in range(11):
        expected = list(iterable[i:])
        actual = list(drop_until(lambda x: x > i, iterable))
        assert expected == actual, f'expected = {expected} != actual = {actual}'



# Generated at 2022-06-13 19:57:29.973966
# Unit test for function scanl
def test_scanl():
    assert list(scanl(operator.add, [1, 2, 3, 4], 0)) == [0, 1, 3, 6, 10]
    assert list(scanl(lambda s, x: x + s, ['a', 'b', 'c', 'd'])) == ['a', 'ba', 'cba', 'dcba']


# Generated at 2022-06-13 19:57:33.431667
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    list = LazyList(range(10))
    assert list[1] == 1
    assert list[-1] == 9
    assert list[2:7:2] == [2, 4, 6]


# Generated at 2022-06-13 19:57:37.157933
# Unit test for function chunk
def test_chunk():
    xs = list(chunk(2, range(5)))
    assert xs == [[0, 1], [2, 3], [4]]
    assert len(xs) == 3
    assert xs[0] == [0, 1]
    assert xs[1] == [2, 3]
    assert xs[2] == [4]



# Generated at 2022-06-13 19:57:50.539940
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    for _ in range(1000):
        end = random.randint(-20, 20)
        r = Range(end)
        for i in range(end):
            assert r[i] == i
        assert r[10:] == [i for i in range(10, end)]
        assert r[10:5] == []
        assert r[:5] == [i for i in range(5)]
        assert r[-5:] == [i for i in range(end-5, end)]
        assert r[-5:-7] == []
        assert r[1:9:2] == [i for i in range(1, 9, 2)]
        assert r[7:1:-2] == [7, 5, 3]
        assert r[-3:-7:-2] == [end - 3, end - 5]
        assert r

# Generated at 2022-06-13 19:58:01.436291
# Unit test for function drop_until
def test_drop_until():
    a = [1, 2, 3]
    it = iter(a)
    assert list(drop_until(lambda x: x==2, a)) == [2, 3]
    try:
        assert list(drop_until(lambda x: x==2, it)) == [2, 3]
        assert list(it) == []
    except StopIteration:
        assert False

# Helper function

# Generated at 2022-06-13 19:58:03.999597
# Unit test for function drop_until
def test_drop_until():
    xs = [2,4,5,6,7,8]
    assert list(drop_until(lambda x: x > 5, xs)) == [6,7,8]


# Generated at 2022-06-13 19:58:14.648664
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    from hypothesis import given
    from .testutil import RandomIterable
    from hypothesis.extra.numpy import arrays

    @given(RandomIterable, arrays(int, (5, 10), unique=True, elements=(-10, 10)))
    def test(iterable, indices):
        lst = LazyList(iterable)
        idx_lst = indices.tolist()
        for i in idx_lst:
            assert lst[i] == list(iterable)[i]
        assert list(lst[:]) == list(iterable)
        assert list(lst) == list(iterable)
        assert lst[:] == list(iterable)
    test()



# Generated at 2022-06-13 19:58:20.301018
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    a = [1, 2, 3, 4, 5]
    assert(MapList(lambda x: x + 1, a)[2] == 4)
    assert(MapList(lambda x: x + 1, a)[:2] == [2, 3])


# Generated at 2022-06-13 19:58:30.885683
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    s = LazyList(range(1000))
    assert s[:10] == list(range(10))
    assert s[1:11] == list(range(1, 11))
    assert s[:10] == list(range(10))
    assert s[100] == 100
    assert s[100:110] == list(range(100, 110))
    assert s[999] == 999
    with pytest.raises(IndexError):
        s[1000]

# Generated at 2022-06-13 19:58:41.962851
# Unit test for function split_by
def test_split_by():
    s = 'Split by separator'
    assert list(split_by(s, criterion = lambda x: x == ' ')) == [['S', 'p', 'l', 'i', 't'],
                                                                 ['b', 'y', 's', 'e', 'p', 'a', 'r', 'a', 't', 'o', 'r']]
    assert list(split_by(s, criterion = lambda x: x == ' ')) == [['S', 'p', 'l', 'i', 't'],
                                                                 ['b', 'y', 's', 'e', 'p', 'a', 'r', 'a', 't', 'o', 'r']]

# Generated at 2022-06-13 19:58:57.584347
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    from doctest import testmod
    from varz import MapList
    from utils import assert_raises_message

    @overload
    def test(): ...

    @overload
    def test(s1: str) -> int: ...

    @overload
    def test(s1: str, s2: str) -> str: ...

    def test(s1='', s2=''):
        if s1 == 'a':
            return 0
        if s1 == 'b':
            return 1
        if s2 == 'c':
            return 'b'
        if s2 == 'd':
            return 'c'
        return ''

    def f(s: str) -> str:
        return s

    def g(s: str) -> int:
        return len(s)


# Generated at 2022-06-13 19:59:13.710495
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x > 3, range(2, 8))) == [4, 5, 6, 7]
    assert list(drop_until(lambda _: False, range(10))) == list(range(10))
    assert list(drop_until(lambda _: False, [])) == []
    assert list(drop_until(lambda x: x > 5, take(5, range(10)))) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x > 5, drop(5, range(10)))) == [6, 7, 8, 9]

# Generated at 2022-06-13 19:59:24.493978
# Unit test for function drop_until
def test_drop_until():
    xs = [1, 2, 3, 4, 5, 6, 7, 8]
    assert len(list(drop_until(lambda x: x > 5, xs))) == len(xs) - 5
    assert list(drop_until(lambda x: x <= 5, xs)) == [6, 7, 8]
    assert list(drop_until(lambda x: x % 2 == 0, xs)) == [2, 3, 4, 5, 6, 7, 8]
    assert list(drop_until(lambda x: x % 2 == 1, xs)) == [1, 2, 3, 4, 5, 6, 7, 8]
    assert list(drop_until(lambda x: False, xs)) == [1, 2, 3, 4, 5, 6, 7, 8]

# Generated at 2022-06-13 19:59:35.852006
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(5)
    assert [0, 1, 2, 3, 4] == [x for x in r]
    assert [0, 1, 2, 3, 4][::-1] == [x for x in r[::-1]]
    assert [1, 3] == [x for x in r[1::2]]
    assert [3, 1] == [x for x in r[1::-2]]
    print('Test for method __getitem__ of class Range... Pass')
print('Test for method __getitem__ of class Range... Pass')


# Generated at 2022-06-13 19:59:41.335948
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    import doctest
    doctest.testmod(verbose=True)

# Generated at 2022-06-13 19:59:51.414126
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    for (input1,),input2 in [(list,list),(range,range),(Range,Range)]:
        assert [i for i in input1(10)[input2(0,None,2)]] == [i for i in Range(10)[range(0,None,2)]]
        assert [i for i in input1(1, 10 + 1)[input2(0,None,2)]] == [i for i in Range(1, 10 + 1)[range(0,None,2)]]
        assert [i for i in input1(1, 11, 2)[input2(0,None,2)]] == [i for i in Range(1, 11, 2)[range(0,None,2)]]

# Generated at 2022-06-13 19:59:54.205992
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    try:
        MapList(lambda x: x, []).__getitem__(0)
        assert True
    except:
        assert False

# Generated at 2022-06-13 20:00:05.191781
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    class TestClass:
        def test_method__getitem__(self):
            a = [1, 2, 3, 4, 5]
            pos = bisect.bisect_left(MapList(lambda x: x * x, a), 10)
            assert pos == 3

            b = [2, 3, 4, 5, 6]
            pos = bisect.bisect_left(MapList(lambda i: a[i] * b[i], Range(len(a))), 10)
            assert pos == 2
            
    instance = TestClass()
    instance.test_method__getitem__()

test_MapList___getitem__()


# Generated at 2022-06-13 20:00:16.540447
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    seq = LazyList(range(5))
    assert seq[0] == 0
    assert seq[1:3] == [1, 2]
    assert seq[3:] == [3, 4]

    seq = LazyList(range(5))
    assert seq[-1] == 4
    assert seq[-2] == 3
    assert seq[:-1] == [0, 1, 2, 3]
    assert len(seq) == 5

    seq = LazyList(range(5))
    assert len(seq[:]) == 5
    assert len(seq[1:]) == 4
    assert len(seq[:-1]) == 4
    assert len(seq[2:-2]) == 1
    assert len(seq[3:3]) == 0



# Generated at 2022-06-13 20:00:25.532466
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    from .testing import assert_eq
    # Case 1
    r = Range(0, 10, 1)
    assert_eq(r[0], 0)
    # Case 2
    r = Range(0, 10, 1)
    assert_eq(r[1], 1)
    # Case 3
    r = Range(0, 10, 1)
    assert_eq(r[-1], 9)
    # Case 4
    r = Range(0, 10, 2)
    assert_eq(r[0], 0)
    # Case 5
    r = Range(0, 10, 2)
    assert_eq(r[1], 2)
    # Case 6
    r = Range(0, 10, 2)
    assert_eq(r[-1], 8)
    # Case 7

# Generated at 2022-06-13 20:00:26.998828
# Unit test for function drop_until
def test_drop_until():
    for n in range(10):
        drop_until(lambda x: x % 2 == 0, range(n))



# Generated at 2022-06-13 20:00:29.975179
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    assert MapList(lambda x: x * x, [1, 2, 3, 4, 5])[3] == 16
    assert MapList(lambda i: i, [1, 2, 3, 4, 5])[2:5] == [2, 3, 4]



# Generated at 2022-06-13 20:00:32.583059
# Unit test for function take
def test_take():
    assert list(take(-1, range(100))) == []
    assert list(take(0, range(100))) == []
    assert list(take(5, range(100))) == [0, 1, 2, 3, 4]
    assert list(take(100, range(100))) == [x for x in range(100)]
    assert list(take(1000, range(100))) == [x for x in range(100)]
test_take()



# Generated at 2022-06-13 20:00:34.757512
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x>5, range(10))) == [6,7,8,9]



# Generated at 2022-06-13 20:00:44.021004
# Unit test for function take
def test_take():
    for n in range(10):
        for it in ([], [1], [1, 2], range(5)):
            assert list(take(n, it)) == list(it)[:n]



# Generated at 2022-06-13 20:00:48.007868
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    l = MapList(lambda x: x + 1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    assert l[0] == 1
    assert l[-1] == 10
    assert l[:5] == [1, 2, 3, 4, 5]
    assert l[::2] == [1, 3, 5, 7, 9]


# Generated at 2022-06-13 20:00:54.395803
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(0, 10, 2)
    assert r[1] == 2
    assert r[3] == 6
    assert r[-1] == 8
    assert r[-3] == 4
    assert r[::2] == [0, 4, 8]
    assert r[1::2] == [2, 6]
    assert r[::-1] == [8, 6, 4, 2, 0]



# Generated at 2022-06-13 20:01:00.117069
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    ll = LazyList(range(10))
    assert ll[0] == 0
    assert ll[-1] == 9
    assert ll[-2] == 8

    with pytest.raises(IndexError):
        ll[10]

    assert ll[0:3] == range(3)
    assert ll[3:6] == range(3, 6)
    assert ll[-3:-1] == range(7, 9)



# Generated at 2022-06-13 20:01:04.807050
# Unit test for function drop_until
def test_drop_until():
    from src.utils import utils

    def drop_until_true(iterable):
        return utils.to_list(drop_until(lambda x: x == True, iterable))

    assert drop_until_true([False]) == []
    assert drop_until_true([False, True]) == [True]
    assert drop_until_true([True, False]) == [True]
    assert drop_until_true([False, False, False, True, False]) == [True, False]



# Generated at 2022-06-13 20:01:05.969546
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    assert LazyList([1, 2, 3])[2] == 3



# Generated at 2022-06-13 20:01:15.314324
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    import random
    import pytest
    rng = random.Random(42)
    for _ in range(100):
        start = rng.randint(-100, 100)
        step = rng.randint(-100, 100)
        if step == 0:
            step = 1
        end = rng.randint(start, 101 * step)
        c = Range(start, end, step)
        idx = rng.randint(-100, c.length + 100)
        c.__getitem__(idx)
        idx = slice(start=rng.randint(-100, 101), stop=rng.randint(-100, 101), step=rng.randint(-100, 101))
        c.__getitem__(idx)


# Generated at 2022-06-13 20:01:25.640696
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    a = LazyList(range(5))
    assert isinstance(a[0], int)
    assert len(a) == 5
    assert a[2] == 2
    assert a[-1] == 4
    a = LazyList(range(100000))
    assert a[0:0] == []
    assert a[0:5] == list(range(5))
    assert a[1:5:2] == [1, 3]
    assert a[4:4] == []
    assert a[4::-1] == [4, 3, 2, 1, 0]
    assert a[::2] == list(range(0, 100000, 2))
    assert a[::-1] == list(range(99999, -1, -1))

# Generated at 2022-06-13 20:01:28.402784
# Unit test for function drop_until
def test_drop_until():
    list(drop_until(lambda x: x > 5, [1,2,3,4,5,6,7]))



# Generated at 2022-06-13 20:01:39.744852
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    lst = LazyList(range(10))
    assert lst[0] == 0
    assert lst[1] == 1
    assert lst[2:4] == [2, 3]
    assert isinstance(lst[4:], list)
    assert lst[:4] == [0, 1, 2, 3]
    assert lst[:] == list(range(10))
    assert lst[:100] == list(range(10))
    assert lst[-1] == 9
    assert lst[-2:] == [8, 9]
    assert lst[-3:-1] == [7, 8]
    assert lst[:-1] == list(range(9))
    assert lst[-3:-3] == []



# Generated at 2022-06-13 20:01:54.932708
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    class Test:
        def __init__(self, func, lst):
            self.func = func
            self.list = lst

        def __getitem__(self, item):
            if isinstance(item, int):
                return self.func(self.list[item])
            return [self.func(x) for x in self.list[item]]
        
        def __iter__(self):
            return map(self.func, self.list)
        
        def __len__(self):
            return len(self.list)
    test = Test(lambda x: x * x, [1, 2, 3, 4, 5])
    assert test[4] == test.list[4] ** 2
    assert test[0] == test.list[0] ** 2

# Generated at 2022-06-13 20:01:58.763306
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(0, 10, 1)
    assert(r[0] == 0)
    assert(r[1] == 1)
    assert(r[-1] == 9)


# Generated at 2022-06-13 20:02:06.063180
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    rng = Range(10)
    idx = 0
    while idx < 10:
        assert rng[idx] == idx
        idx = idx + 1

rng = Range(10)
idx = 0
while idx < 10:
    assert rng[idx] == idx
    idx = idx + 1

