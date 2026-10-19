

# Generated at 2022-06-13 19:52:40.708533
# Unit test for function drop
def test_drop():
    assert list(drop(0, range(10))) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert list(drop(2, range(10))) == [2, 3, 4, 5, 6, 7, 8, 9]
    assert list(drop(10, range(10))) == []


# Generated at 2022-06-13 19:52:45.726339
# Unit test for method __iter__ of class LazyList
def test_LazyList___iter__():
    assert list(LazyList(range(5))) == list(range(5))
    assert list(LazyList(range(5))[:2]) == list(range(5))[:2]
    assert list(LazyList(range(0, 5, 2))) == [0, 2, 4]



# Generated at 2022-06-13 19:52:48.372738
# Unit test for function take
def test_take():
    # Should not raise any exception.
    take(-1, [1])
    take(-2, [1])



# Generated at 2022-06-13 19:52:49.827230
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    assert Range(1, 2).__getitem__(0) == 1
    

# Generated at 2022-06-13 19:52:51.566207
# Unit test for function take
def test_take():
    assert list(take(5,range(1000000)))==[0, 1, 2, 3, 4]


# Generated at 2022-06-13 19:52:57.975312
# Unit test for method __iter__ of class LazyList
def test_LazyList___iter__():
    m1 = LazyList(range(0, 100, 2))
    m2 = LazyList(range(0, 100, 2))
    # check that the iterators do not terminate
    m1.__iter__()
    m2.__iter__()
    # check if both iterators are the same
    for i, j in zip(m1, m2):
        assert i == j
    # check if both iterators iterate from scratch
    for i, j in zip(m1, m2):
        assert i == j
    # use the iterators as expected
    assert list(m1) == list(m2)



# Generated at 2022-06-13 19:53:00.223461
# Unit test for function drop
def test_drop():
    assert list(drop(2, range(5))) == [2, 3, 4]



# Generated at 2022-06-13 19:53:09.184382
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    import bisect

    # Find index of the first element in `a` whose square is >= 10.
    a = [1, 2, 3, 4, 5]
    pos = bisect.bisect_left(MapList(lambda x: x * x, a), 10)
    assert 3 == pos

    # Find the first index `i` such that `a[i] * b[i]` is >= 10.
    b = [2, 3, 4, 5, 6]
    pos = bisect.bisect_left(MapList(lambda i: a[i] * b[i], Range(len(a))), 10)
    assert 2 == pos



# Generated at 2022-06-13 19:53:14.839249
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(1, 10)
    assert r[0] == 1
    assert r[9] == 10
    assert r[-1] == 10
    assert r[-10] == 1
    assert r[2:4] == [3, 5]
    assert r[2:10:2] == [3, 7, 9]
    with pytest.raises(IndexError):
        _ = r[100]



# Generated at 2022-06-13 19:53:21.577555
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    def trans(x): return x * 2
    a = [1, 2, 3, 4, 5]
    m = MapList(trans, a)
    assert m[0] == 2
    assert m[2] == 6
    assert m[4] == 10
    assert m[-1] == 10
    assert m[2:4] == [6, 8]


# Generated at 2022-06-13 19:53:35.369139
# Unit test for function split_by
def test_split_by():
    assert list(split_by(" Split by: ", empty_segments=True, separator='.')) \
        == [[], ['S', 'p', 'l', 'i', 't'], ['b', 'y', ':'], []]



# Generated at 2022-06-13 19:53:46.509254
# Unit test for function split_by

# Generated at 2022-06-13 19:53:53.815215
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    a = [1, 2, 3, 4, 5]
    ml = MapList(lambda x: x * x, a)
    assert ml[0] == 1
    assert ml[1] == 4
    assert ml[3] == 16
    assert ml[-1] == 25

    assert ml[0:3] == [1, 4, 9]
    assert ml[1:-1] == [4, 9, 16]
    assert ml[:-2] == [1, 4, 9]
    assert ml[-1:-4:-1] == [25, 16, 9]
    assert ml[:] == [1, 4, 9, 16, 25]

    assert ml[::2] == [1, 9, 25]
    assert ml[::-1] == [25, 16, 9, 4, 1]

# Generated at 2022-06-13 19:53:57.199628
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
test_drop_until()



# Generated at 2022-06-13 19:54:06.932422
# Unit test for function chunk
def test_chunk():
    assert list(chunk(1, range(10))) == [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]]
    assert list(chunk(2, range(10))) == [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]]
    assert list(chunk(3, range(10))) == [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]
    assert list(chunk(4, range(10))) == [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9]]
    assert list(chunk(5, range(10))) == [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]


# Generated at 2022-06-13 19:54:12.931418
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    lst = LazyList(range(10))
    assert lst[-1] == 9 and len(lst.list) == 1
    assert lst[:5] == list(range(5)) and len(lst.list) == 5
    assert lst[::-1] == list(range(5))[::-1] + list(range(5, 10))[::-1] and len(lst.list) == 10
    assert lst[9] == 9 and lst[10] is None and lst[10:] == [] and lst[:-1] == list(range(9))
    assert lst[:-100] == []

# Generated at 2022-06-13 19:54:15.828348
# Unit test for function drop_until
def test_drop_until():
    it = drop_until(lambda x: x>5, range(10))
    assert next(it) == 6
    assert next(it) == 7
    assert next(it) == 8


# Generated at 2022-06-13 19:54:20.896416
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x == "b", "a b c d e f g".split())) == ["b", "c", "d", "e", "f", "g"]
    assert list(drop_until(lambda x: x == "b", iter([]))) == []



# Generated at 2022-06-13 19:54:28.050057
# Unit test for function split_by
def test_split_by():
    def split_by1(l: List[int], empty_segments: bool = False) -> Iterator[List[int]]:
        return split_by(l, empty_segments=empty_segments, criterion=lambda x: x % 3 == 0)

    assert list(split_by1([1, 2, 3, 4, 5, 6, 7, 8, 9])) == [[1, 2], [4, 5], [7, 8]]
    assert list(split_by1([1, 2, 3, 4, 5, 6, 7, 8, 9], empty_segments=True)) == [[1, 2], [], [4, 5], [], [7, 8], []]
    assert list(split_by1([1, 2, 3])) == [[1, 2]]

# Generated at 2022-06-13 19:54:34.126978
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    for i in range(4):
        for j in range(4):
            ll = LazyList(range(i))
            assert ll[j] == j if j < i else IndexError
            assert ll[-j] == i - j if j > 0 and j <= i else IndexError
            assert ll[0:j] == list(range(j)) if j <= i else IndexError
            assert ll[0:j:i] == list(range(0, j, i)) if j // i <= i else IndexError
            assert ll[0:j:2] == list(range(0, j, 2)) if j // 2 <= i else IndexError
            assert ll[i:j] == [] if j == i else IndexError
            assert ll[j:i] == [] if j == i else IndexError



# Generated at 2022-06-13 19:54:49.215059
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x % 2 == 0, range(10))) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x % 2 == 0, range(10, 15))) == [10, 11, 12, 13, 14]
    assert list(drop_until(lambda x: x == 10, range(10))) == [10]


# Generated at 2022-06-13 19:54:54.916652
# Unit test for function take
def test_take():
    assert list(take(0,range(10)))==[]
    assert list(take(10,range(10)))==list(range(10))
    assert list(take(10,range(5)))==list(range(5))
    assert list(take(-1,range(10)))==[]


# Generated at 2022-06-13 19:54:56.851107
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]



# Generated at 2022-06-13 19:55:02.006495
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    from random import randint
    r = Range(100)
    for _ in range(100):
        i = randint(0, 99)
        assert r[i] == i
        assert len(r[i:i+10]) == 10
    print("test_Range___getitem__() passed.")
test_Range___getitem__()


# Generated at 2022-06-13 19:55:04.908560
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6,7,8,9]
    assert list(drop_until(lambda x: x > 5, range(1))) == []


# Generated at 2022-06-13 19:55:07.235972
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x < 0, range(10))) == []



# Generated at 2022-06-13 19:55:09.954942
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    from bisect import bisect_left
    lst = Range(10)
    pos = bisect_left(MapList(lambda x: x * x, lst), 10)
    assert pos == 3


# Generated at 2022-06-13 19:55:12.671978
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]



# Generated at 2022-06-13 19:55:20.886614
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    import operator
    import random
    r = Range(1,10,2)
    assert isinstance(r[0],int)
    assert isinstance(r[slice(1,3)],list)
    assert [1,3,5,7,9] == r[slice(0,None)]
    assert [1,3,5,7] == r[slice(0,5,2)]
    assert [5,7] == r[slice(2,6,2)]
    assert [3,5] == r[slice(1,None,2)]
    for i in range(10):
        start = random.randint(1,10)
        step = random.randint(1,3)
        r = Range(start,30,step)
        assert [x*step+start for x in range(15)] == r[:]

# Generated at 2022-06-13 19:55:27.140709
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(10)
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


# Generated at 2022-06-13 19:55:40.521295
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    import random
    import math
    import string
    from random import shuffle

    def gen_seq(size, low, high):
        seq = []
        for i in range(size):
            # from http://code.activestate.com/recipes/135970-random-hex-string/
            seq.append(random.randint(low, high))
        return seq

    for size in range(1, 6):
        for low in range(1, 6):
            for high in range(low, 6):
                seq = gen_seq(size, low, high)
                keys = list(range(size))
                shuffle(keys)
                for key in keys:
                    assert seq[key] == Range(low, high + 1)[key], \
                            "Error of Range::__getitem__(int)"


# Generated at 2022-06-13 19:55:42.774295
# Unit test for function drop_until
def test_drop_until():
    list(drop_until(lambda x: x == 6, [7, 8, 6, 9, 10]))



# Generated at 2022-06-13 19:55:51.556135
# Unit test for function drop_until
def test_drop_until():
    iter1=[1,2,3,4,5,7]
    iter2=[1,2,3,4,6,7]
    iter3=[1,2,3,5,7]

    assert list(drop_until(lambda x: x>5,iter1))==[7]
    assert list(drop_until(lambda x: x>5,iter2))==[6,7]
    assert list(drop_until(lambda x: x>5,iter3))==[5,7]
test_drop_until()


# Generated at 2022-06-13 19:55:57.949427
# Unit test for function drop_until
def test_drop_until():
    l = list(range(10))

    assert list(drop_until(lambda x: x > 5, l)) == l[6:]
    assert list(drop_until(lambda x: x % 2 == 0, l)) == l[1:]
    assert list(drop_until(lambda x: x > 9, l)) == []
    assert list(drop_until(lambda x: False, l)) == []
    assert list(drop_until(lambda x: True, l)) == l
    assert list(drop_until(lambda x: x > 20, l)) == []



# Generated at 2022-06-13 19:56:07.558080
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    a = [1, 2, 3]
    b = [2, 3, 4]
    m = MapList(lambda i: a[i] * 2 + b[i], range(len(a)))
    assert m[0] == 2 + 1 * 2 + 2
    assert m[1] == 2 + 2 * 2 + 3
    assert m[2] == 2 + 3 * 2 + 4
    assert m[:] == [2 + 1 * 2 + 2, 2 + 2 * 2 + 3, 2 + 3 * 2 + 4]
    assert m[1:3] == [2 + 2 * 2 + 3, 2 + 3 * 2 + 4]
    assert m[:1] == [2 + 1 * 2 + 2]
    assert m[2:] == [2 + 3 * 2 + 4]

# Generated at 2022-06-13 19:56:17.800782
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(10)
    s = r[0]
    assert (s == 0)
    s = r[0:1]
    assert (s == [0])
    r = Range(1, 10 + 1)
    s = r[0]
    assert (s == 1)
    s = r[0:1]
    assert (s == [1])
    r = Range(1, 11, 2)
    s = r[0]
    assert (s == 1)
    s = r[0:1]
    assert (s == [1])
    import pytest
    with pytest.raises(ValueError):
        Range()
    with pytest.raises(ValueError):
        Range(1, 2, 3, 4)

# Generated at 2022-06-13 19:56:26.311091
# Unit test for method __getitem__ of class Range

# Generated at 2022-06-13 19:56:35.572155
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    for start, stop, step in [(1, 11, 2), (0, 9, 3), (5, -1, 4), (5, -1, -4)]:
        r = Range(start, stop, step)
        assert r[0] == r.l
        assert r[1] == r.l + r.step
        assert r[2] == r.l + 2 * r.step
        assert r[1:3] == [r.l + r.step, r.l + 2 * r.step]
        assert r[-1] == r.r - r.step
        assert r[-2] == r.r - 2 * r.step
        assert r[-3:-1] == [r.r - 2 * r.step, r.r - r.step]
test_Range___getitem__()



# Generated at 2022-06-13 19:56:43.704764
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x % 2 == 0, [1, 2, 3, 4])) == [2, 3, 4]
    assert list(drop_until(lambda x: x % 2 == 0, [1, 3, 5])) == []
    assert list(drop_until(lambda x: x % 2 == 0, [])) == []
    assert list(drop_until(lambda x: x % 2 == 0, [2, 3, 4])) == [2, 3, 4]



# Generated at 2022-06-13 19:56:48.142523
# Unit test for function scanl
def test_scanl():
    assert list(scanl(operator.add, [1, 2, 3, 4])) == [1, 3, 6, 10]
    assert list(scanl(lambda s, x: x + s, ['a', 'b', 'c', 'd'])) == ['a', 'ba', 'cba', 'dcba']


# Generated at 2022-06-13 19:56:56.809811
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    assert Range(10)[2] == 2
    assert Range(10)[-4] == 6
    assert Range(1, 10, 3)[2] == 7
    

# Generated at 2022-06-13 19:57:09.751567
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    # Make sure we can iterate through an instance of class Range
    r = Range(10)
    assert all(x == i for i, x in enumerate(r))
    # Make sure we can index elements of an instance of class Range
    r = Range(10)
    for i in range(10):
        assert r[i] == i
    # Make sure we can index elements with a slice of an instance of class Range
    r = Range(10)
    for i in range(10):
        assert r[i * 2:(i + 2) * 2] == [i * 2 + j for j in range(2)]
    # Make sure we can index negative elements of an instance of class Range
    r = Range(10)
    for i in range(10):
        assert r[-i - 1] == 9 - i
    # Make sure we

# Generated at 2022-06-13 19:57:16.407576
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    '''
    input:
        item:
            int
            slice
    output:
        return:
            int
            list
    '''
    r = Range(10)         # (end)
    # r = Range(1, 10 + 1)  # (start, end)
    # r = Range(1, 11, 2)   # (start, end, step)
    # print(r[2])
    print(r[0:2:1])

if __name__ == '__main__':
    test_Range___getitem__()

# Generated at 2022-06-13 19:57:21.555980
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(1,10)
    assert(r[0] == 1)
    assert(r[-1] == 9)
    assert(r[0:2] == [1,2])
    assert(r[:2] == [1,2])
    
    

# Generated at 2022-06-13 19:57:22.828136
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    # Nothing to test
    pass


# Generated at 2022-06-13 19:57:27.078644
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    obj = MapList(lambda x: x * x, [1, 2, 3, 4])
    assert obj[2] == 9
    assert obj[0:2] == [1, 4]
    assert obj[:] == [1, 4, 9, 16]

# Generated at 2022-06-13 19:57:32.875618
# Unit test for function drop_until
def test_drop_until():
    # Tests an iterable in which elements satisfy the predicate
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
    # Tests an iterable in which no element satisfies the predicate
    assert list(drop_until(lambda x: x > 5, range(3))) == []
    # Tests an iterable in which the first element satisfies the predicate
    assert list(drop_until(lambda x: x > 5, [6, 7, 8, 9])) == [6, 7, 8, 9]



# Generated at 2022-06-13 19:57:39.673754
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    obj = Range(1, 10)
    result = obj[0]
    assert result == 1
    obj = Range(2, 11, 2)
    result = obj[0]
    assert result == 2
    result = obj[2]
    assert result == 6
    obj = Range(1, 10, 2)
    result = obj[1]
    assert result == 3
    result = obj[3]
    assert result == 7
    obj = Range(2, 10, 2)
    result = obj[1]
    assert result == 4
    result = obj[3]
    assert result == 8
    result = obj[5]
    assert result == 10
    obj = Range(2, 11, 2)
    result = obj[1]
    assert result == 4
    result = obj[3]
    assert result == 8
   

# Generated at 2022-06-13 19:57:44.390581
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x == "", "")) == []



# Generated at 2022-06-13 19:57:47.935173
# Unit test for function drop_until
def test_drop_until():
    """
    >>> list(drop_until(lambda x: x > 5, range(10)))
    [6, 7, 8, 9]
    """



# Generated at 2022-06-13 19:57:57.998439
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    assert MapList(lambda x: x + 1, [1, 2, 3])[0] == 2


# Generated at 2022-06-13 19:58:05.606306
# Unit test for function drop_until
def test_drop_until():
    for lst, ret in [(list(range(10)), list(range(6, 10))),
                     ([], []),
                     ([1], [1]),
                     ([0, 1], [1])]:
        assert list(drop_until(lambda x: x > 5, lst)) == ret
# End unit test for function drop_until



# Generated at 2022-06-13 19:58:12.788237
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 0, range(3))) == [1, 2]
    assert list(drop_until(lambda x: x >= 3, range(3))) == [3]
    assert list(drop_until(lambda x: False, range(3))) == [0, 1, 2]
    assert list(drop_until(lambda x: True, range(3))) == [0, 1, 2]
    assert list(drop_until(lambda x: x > 3, range(3))) == []



# Generated at 2022-06-13 19:58:19.615791
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    import bisect

    a = [1, 2, 3, 4, 5]
    pos = bisect.bisect_left(MapList(lambda x: x * x, a), 10)
    assert pos == 3

    b = [2, 3, 4, 5, 6]
    pos = bisect.bisect_left(MapList(lambda i: a[i] * b[i], Range(len(a))), 10)
    assert pos == 2

# Generated at 2022-06-13 19:58:23.019163
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    # Given
    from sys import maxsize
    r = Range(maxsize)
    # When
    r[0]

# Generated at 2022-06-13 19:58:27.719837
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    print("Testing method __getitem__() of class MapList")
    def f(x):return 2 * x
    a = MapList(f,[1,2,3,4])
    assert a[2] == 6
    assert a[:2] == [2,4]
    for i in a:
        assert i % 2 ==0
    print(" PASSED")

# Generated at 2022-06-13 19:58:33.003811
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    assert Range(10)[7] == 7
    assert Range(10)[0] == 0
    assert Range(1, 11)[2] == 3
    assert Range(1, 11, 2)[3] == 7

# Generated at 2022-06-13 19:58:44.116684
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x > 0, range(10)))[0] == 1
    assert list(drop_until(lambda x: x > 0, range(10)))[-1] == 9
    assert list(drop_until(lambda x: x > -0.5, range(10)))[0] == 0
    assert list(drop_until(lambda x: x > -0.5, range(10)))[-1] == 9
    assert list(drop_until(lambda x: x > 0.5, range(10)))[0] == 1
    assert list(drop_until(lambda x: x > 0.5, range(10)))[-1] == 9

# Generated at 2022-06-13 19:58:47.210703
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(11, step=2)
    assert r[-1] == r[5]


# Generated at 2022-06-13 19:58:48.762490
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]



# Generated at 2022-06-13 19:59:04.450198
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    # import builtins
    # import typing
    #
    # Range = typing.cast(typing.Type[typing.Any], Range)
    #
    r1 = Range(10)
    assert r1[0] == 0
    assert r1[1] == 1
    assert r1[-1] == 9
    assert r1[slice(0, 3)] == [0, 1, 2]
    assert r1[slice(4, 7)] == [4, 5, 6]
    assert r1[slice(1, -1)] == [1, 2, 3, 4, 5, 6, 7, 8]
    assert r1[slice(1, -1, 2)] == [1, 3, 5, 7]

# Generated at 2022-06-13 19:59:06.894436
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
test_drop_until()



# Generated at 2022-06-13 19:59:11.292419
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    d = MapList(lambda x: x * x, [1, 2, 3, 4, 5])
    assert d[0] == 1
    assert d[2] == 9
    assert d[-1] == 25
    assert tuple(d[1:3]) == (4, 9)



# Generated at 2022-06-13 19:59:16.575883
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x < 0, range(10))) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
test_drop_until()

# Generated at 2022-06-13 19:59:18.955095
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]



# Generated at 2022-06-13 19:59:24.153129
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 2, range(10))) == list(range(3,10))
    assert list(drop_until(lambda x: x > 10, range(10))) == list(range(10))


# Generated at 2022-06-13 19:59:33.096234
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(0, 9 + 1, 2)
    assert r[0] == 0
    assert r[4] == 8
    assert r[-2] == 6
    assert r[-1] == 8
    assert r[slice(0, 5, 2)] == [0, 4, 8]
    assert r[slice(None, None, -1)] == [8, 6, 4, 2, 0]


# Generated at 2022-06-13 19:59:43.046051
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    assert ([1, 2, 3] == Range(1, 4)[:])
    assert ([2, 3] == Range(1, 4)[1:])
    assert ([1, 2] == Range(1, 4)[:2])
    assert ([2, 3, 4] == Range(1, 5)[1:])
    assert ([1, 3, 5] == Range(1, 6, 2)[:])
    assert ([2, 4, 6] == Range(2, 7, 2)[:])
    assert ([1, 3, 5] == Range(1, 6, 2)[:3])
    assert ([1, 3, 5] == Range(1, 6, 2)[:-1])
    assert ([1, 3, 5] == Range(1, 6, 2)[0:3])

# Generated at 2022-06-13 19:59:48.608031
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x > 50, range(10))) == []
    assert list(drop_until(lambda x: True, range(10))) == list(range(10))


# Generated at 2022-06-13 19:59:58.732304
# Unit test for function split_by
def test_split_by():
    assert list(split_by([1, 2, 3, 4, 5, 6], criterion=lambda x: x % 3 == 0)) == [[1, 2], [4, 5]]
    assert list(split_by([1, 2, 3, 4, 5, 6], criterion=lambda x: x % 3 == 0, empty_segments=True)) == [[1, 2], [], [4, 5]]
    assert list(split_by(" Split by: ", separator='.')) == [['S', 'p', 'l', 'i', 't'], ['b', 'y', ':']]
    assert list(split_by(" Split by: ", separator='.', empty_segments=True)) == [[], ['S', 'p', 'l', 'i', 't'], ['b', 'y', ':'], []]



# Generated at 2022-06-13 20:00:06.258369
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    lst = []
    range1 = Range(0, 11, 2)
    assert range1[3] == 6
    assert len(range1[1:6]) == 5
    return True


# Generated at 2022-06-13 20:00:11.021286
# Unit test for function drop_until
def test_drop_until():
    for i in range(1000):
        l = np.random.randint(0, i, size=i)
        print(i)
        print(list(l))
        print(list(drop_until(lambda x: x > 0.5, l)))

test_drop_until()


# Generated at 2022-06-13 20:00:22.364398
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(10)         # (end)
    assert r[0] == 0
    assert r[2] == 2
    assert r[4] == 4

    r = Range(1, 10 + 1)  # (start, end)
    assert r[0] == 1
    assert r[2] == 3
    assert r[4] == 5

    r = Range(1, 11, 2)   # (start, end, step)
    assert r[0] == 1
    assert r[2] == 5
    assert r[4] == 9

    r = Range(1, 11, 2)   # (start, end, step)
    assert r[0:5] == [1, 5, 9]
    assert r[0:-2] == [1, 5]

# Generated at 2022-06-13 20:00:34.102719
# Unit test for function drop_until
def test_drop_until():
    # Case 1: No elements to drop
    inputs = [
        ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], lambda x: x % 2 == 0),
        ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], lambda x: x > 5),
        ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], lambda x: x < 10)
    ]
    for x, pred in inputs:
        assert all([a == b for a, b in zip(drop_until(pred, x), x)])

    # Case 2: All elements to drop

# Generated at 2022-06-13 20:00:40.484052
# Unit test for function drop_until
def test_drop_until():
    test_data = range(10)
    zero_three = drop_until(lambda x: x == 3, test_data)
    zero_five = drop_until(lambda x: x == 5, test_data)
    assert next(zero_three) == 3
    assert next(zero_five) == 5
    assert list(zero_three) == list(zero_five)



# Generated at 2022-06-13 20:00:48.699181
# Unit test for function drop_until
def test_drop_until():
    from copy import copy
    from random import randint
    from itertools import islice
    from functools import partial

    for _ in range(100):
        # Generate a list of random numbers
        def r():
            return randint(0, 9)
        full_lst = [r() for _ in range(1000)]

        # Pick some random subset of the list
        def pick_subset(lst):
            rng = range(len(lst))
            idxs = set(islice(rng, randint(0, len(lst))))
            return [copy(lst[i]) for i in idxs]

        # The subset satisfies a predicate if the original list does
        def pred(x):
            return full_lst[x] > 5

# Generated at 2022-06-13 20:00:51.400482
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]



# Generated at 2022-06-13 20:00:56.347857
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
	"""
	# Test for method __getitem__ of class Range
	>>> a = Range(3)
	>>> a[0]
	0
	>>> a[-1]
	2
	>>> a[0:1]
	[0]
	>>> a[0:-1]
	[0, 1]
	"""
	pass


# Generated at 2022-06-13 20:00:59.186103
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(0, 100, 5)[0:3]
    assert r[0] == 0
    assert r[1] == 5
    assert r[2] == 10



# Generated at 2022-06-13 20:01:08.627841
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    e1 = (1, 5, 3, 2) # type: int
    r = Range(0, 10, 2) # type: Range[int]

    t1 = r.__getitem__(0) # type: int
    assert t1 == 1
    t2 = r.__getitem__(2) # type: int
    assert t2 == 5
    t3 = r.__getitem__(3) # type: int
    assert t3 == 2
    t4 = r.__getitem__(slice(None)) # type: List[int]
    assert t4 == [0, 2, 4, 6, 8]
    t5 = r.__getitem__(slice(1)) # type: List[int]
    assert t5 == [2, 4, 6, 8]
    t6 = r.__getitem

# Generated at 2022-06-13 20:01:24.556687
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(10)
    assert(r[0] == 0)
    assert(r[3] == 3)
    assert(r[-1] == 9)
    r = Range(0, 10, 2)
    assert(r[0] == 0)
    assert(r[3] == 6)
    assert(r[-1] == 8)
    r = Range(0, 10, 2)
    assert(r[0:2] == [0, 2])
    assert(r[1:3] == [2, 4])
    r = Range(0, 10, 2)
    assert(r[:2] == [0, 2])
    assert(r[1:] == [2, 4, 6, 8])
    assert(r[:-1] == [0, 2, 4, 6])


# Generated at 2022-06-13 20:01:30.145014
# Unit test for function drop_until
def test_drop_until():
    seq = list(range(10))
    for fn in [lambda x: x > 5, lambda x: x < 5, lambda x: x == 0, lambda x: x == 9]:
        assert drop_until(fn, seq) == filter(fn, seq)
    assert drop_until(lambda x: x < 0, seq) == seq



# Generated at 2022-06-13 20:01:32.891677
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]



# Generated at 2022-06-13 20:01:42.479298
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: True, range(10))) == list(range(10))
    assert list(drop_until(lambda x: False, range(10))) == []
    assert list(drop_until(lambda x: x % 2 == 0, range(10))) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert list(drop_until(lambda x: x % 3 == 0, range(10))) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]



# Generated at 2022-06-13 20:01:52.021495
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x > 1, range(10))) == [2, 3, 4, 5, 6, 7, 8, 9]
    assert list(drop_until(lambda x: x > 0, range(10))) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert list(drop_until(lambda x: x > -1, range(10))) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert list(drop_until(lambda x: x > -2, range(10))) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Generated at 2022-06-13 20:02:01.830181
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(5)
    assert (r == [0, 1, 2, 3, 4])
    assert (r[0] == r[None:1][0])
    assert (r[3:1:-1] == [3, 2])
    assert (r[-1] == r[-1:][0])
    assert (r[-5] == r[:5][-1])
    assert (r[-5:-1] == [0, 1, 2, 3])
    assert (r[2:1:-1] == [2])


# Generated at 2022-06-13 20:02:06.270672
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    c = Range(10)
    c = Range(1, 10 + 1)
    c = Range(1, 11, 2)
    print(c[0], c[2], c[4])
