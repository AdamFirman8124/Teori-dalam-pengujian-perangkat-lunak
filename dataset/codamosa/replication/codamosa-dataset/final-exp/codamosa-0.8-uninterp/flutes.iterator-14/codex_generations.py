

# Generated at 2022-06-13 19:52:39.575099
# Unit test for function drop
def test_drop():
    l = [1,2,3,4,5,6]
    res = (i+3 for i in l)
    assert tuple(drop(3, l)) == res



# Generated at 2022-06-13 19:52:43.340943
# Unit test for function drop
def test_drop():
    assert list(drop(1, [1])) == []
    assert list(drop(1, [1, 2])) == [2]
    assert list(drop(0, [1, 2])) == [1, 2]
    assert list(drop(2, [1, 2])) == []



# Generated at 2022-06-13 19:52:47.477693
# Unit test for method __iter__ of class LazyList
def test_LazyList___iter__():
    print("Testing LazyList.__iter__")
    obj = LazyList(range(10))
    for i, x in enumerate(obj.__iter__()):
        print(i, x)
        assert(i == x)



# Generated at 2022-06-13 19:52:50.110983
# Unit test for function drop
def test_drop():
    assert list(drop(1, [1,2,3])) == [2,3]
    assert list(drop(5, range(5))) == []

# Generated at 2022-06-13 19:52:53.703465
# Unit test for function drop_until
def test_drop_until():
    dropped = drop_until(lambda x: x > 5, range(10))
    assert isinstance(dropped, Iterator)
    dropped_list = list(dropped)
    assert dropped_list == [6, 7, 8, 9]



# Generated at 2022-06-13 19:52:56.975206
# Unit test for method __len__ of class LazyList
def test_LazyList___len__():
    assert (LazyList([1, 2, 3])).__len__() == 3


# Generated at 2022-06-13 19:53:03.674496
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: True, range(10))) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert list(drop_until(lambda x: False, range(10))) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]



# Generated at 2022-06-13 19:53:06.985682
# Unit test for function split_by
def test_split_by():
    assert list(split_by(" Split by: ", empty_segments=True, separator='.')) == [[], ['S', 'p', 'l', 'i', 't'], ['b', 'y', ':'], []]



# Generated at 2022-06-13 19:53:10.793642
# Unit test for function drop
def test_drop():
    try:
        it = drop(-1,range(10))
        next(it)
    except ValueError as e:
        print(e)
    else:
        print('Drop Succeed')

test_drop()



# Generated at 2022-06-13 19:53:14.620788
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    a = list(take(100, range(1000000)))
    b = LazyList(take(100, range(1000000)))
    assert a == b
    assert a[5: 10] == b[5: 10]
    assert a[50] == b[50]



# Generated at 2022-06-13 19:53:22.496948
# Unit test for function drop_until
def test_drop_until():
    def fake_predicate(x):
        return x % 3 == 0
    fake_iterable = [1, 2, 3, 4, 5, 6]
    expected = [3, 4, 5, 6]
    assert list(drop_until(fake_predicate, fake_iterable)) == expected



# Generated at 2022-06-13 19:53:33.559902
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    # Create LazyList with specified iterator
    lst = LazyList(range(5))
    # test __getitem__ with index as int
    assert lst[0] == 0
    assert lst[1] == 1
    assert lst[2] == 2
    assert lst[3] == 3
    assert lst[4] == 4
    # test __getitem__ with index as slice
    assert lst[0:1] == [0]
    assert lst[1:2] == [1]
    assert lst[2:3] == [2]
    assert lst[3:4] == [3]
    assert lst[4:5] == [4]
    assert lst[0:2] == [0, 1]
    assert lst[1:3] == [1, 2]


# Generated at 2022-06-13 19:53:47.651724
# Unit test for function chunk
def test_chunk():
    assert list(chunk(3, range(10))) == [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]
    assert list(chunk(5, range(10))) == [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]
    assert list(chunk(30, range(10))) == [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]
    assert list(chunk(3, [])) == []
    assert list(chunk(3, [1, 2, 3, 4, 5])) == [[1, 2, 3], [4, 5]]
    assert list(chunk(1, [])) == []

# Generated at 2022-06-13 19:53:52.400198
# Unit test for method __len__ of class LazyList
def test_LazyList___len__():
    obj = LazyList([1,1,2,2,2,2,3,3,3,3,3,3,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,5,5])
    expected = 30
    actual = obj.__len__()
    assert actual == expected
    obj = LazyList(range(10))
    with pytest.raises(TypeError):
        obj.__len__()

# Generated at 2022-06-13 19:54:06.782327
# Unit test for method __len__ of class LazyList
def test_LazyList___len__():
    import unittest.mock as mock
    import builtins
    iterable = mock.Mock()
    iterable.__iter__ = lambda self: self
    iterable.__next__ = mock.Mock(side_effect=[1, 2, 3, 4, StopIteration])
    l = LazyList(iterable)
    assert iter(l) is l
    assert list(l) == [1, 2, 3, 4]
    assert iterable.mock_calls == [mock.call.__iter__(iterable), mock.call.__next__(iterable), mock.call.__next__(iterable), mock.call.__next__(iterable), mock.call.__next__(iterable)]
    assert len(l) == 4
    assert l[0] == 1
    assert l[3]

# Generated at 2022-06-13 19:54:13.666118
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    from pytest import raises

    lst = LazyList(range(5))
    for i in range(5):
        assert lst[i] == i
    assert lst.list == [0, 1, 2, 3, 4]

    lst = LazyList(range(5))
    assert lst[:3] == [0, 1, 2]
    assert lst.list == [0, 1, 2]
    assert lst[3:5] == [3, 4]
    assert lst.list == [0, 1, 2, 3, 4]

    lst = LazyList(range(5))
    assert lst[2:] == [2, 3, 4]
    assert lst.list == [0, 1, 2, 3, 4]

    lst = LazyList(range(5))


# Generated at 2022-06-13 19:54:17.763953
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x>1, [1,2,3])) == [2,3]
    assert list(drop_until(lambda x: x > 1, [1, 0, 3])) == [3]
    assert list(drop_until(lambda x: x > 1, [1, 0])) == []



# Generated at 2022-06-13 19:54:21.955528
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    x = MapList(lambda x: x * x, [1, 2, 3])
    if x[1] != 4:
        raise RuntimeError
    if x[:2] != [1, 4]:
        raise RuntimeError


# Generated at 2022-06-13 19:54:25.738074
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    l1 = Range(1,6).__getitem__(0)
    l2 = Range(1,10,2).__getitem__(2)
    l3 = Range(10,-10,-2).__getitem__(slice(3,5,2))
    assert(l1==1)
    asser

# Generated at 2022-06-13 19:54:34.589380
# Unit test for method __iter__ of class LazyList
def test_LazyList___iter__():
    my_list = LazyList(range(10))
    assert len(my_list) == 10
    for i, v in enumerate(my_list):
        assert v == i
    assert len(my_list) == 10

    my_list = LazyList(range(10))
    assert len(my_list) == 10
    assert sum(my_list) == 45
    assert len(my_list) == 10
    # Unit test for method __getitem__ of class LazyList

# Generated at 2022-06-13 19:54:48.782231
# Unit test for method __iter__ of class LazyList
def test_LazyList___iter__():
    import random
    import string
    random_list = lambda: [random.choice(string.ascii_letters) for _ in range(random.randint(5, 20))]
    for _ in range(10):
        for f in [list, LazyList.from_list, reversed]:
            s = f(random_list())
            assert [t for t in s] == [t for t in iter(s)]

LazyList.from_list = lambda lst: LazyList(iter(lst))

# Generated at 2022-06-13 19:54:54.533151
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    a = Range(3, 9, step=2)
    assert a[0] == 3
    assert a[1] == 5
    assert a[2] == 7
    assert a[:2] == [3,5]
    assert a[1:3] == [5,7]
    assert a[2:] == [7]
    assert a[2::-1] == [7,5,3]
    assert a[:1:-1] == [7,5]
    assert a[1::-1] == [5,3]
    assert a[::-1] == [7,5,3]
    assert a[-1] == 7
    assert a[-2] == 5
    assert a[-3] == 3
    assert a[-4] == 7
    assert a[-5] == 5
   

# Generated at 2022-06-13 19:55:05.042070
# Unit test for method __iter__ of class LazyList
def test_LazyList___iter__():
    for test_case in (
        # Empty list
        [],
        # Normal list
        [0, 1, 2, 3],
        # Empty iterable
        iter(()),
        # Normal iterable
        iter(range(100)),
        # Iterator exhausted by iteration
        iter(range(100)),
        # Iterator exhausted by len()
        iter(range(100)),
        # Iterator exhausted by getitem
        iter(range(100)),
    ):
        iterable = test_case if isinstance(test_case, list) else list(test_case)
        iterable_size = len(iterable)
        lazy_list = LazyList(test_case)
        assert list(lazy_list) == iterable
        assert isinstance(lazy_list.list, list)

# Generated at 2022-06-13 19:55:14.686920
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    ll = LazyList(range(5))
    assert ll[0] == 0
    assert ll == [0]
    assert ll[4] == 4
    assert ll == [0, 1, 2, 3, 4]

    assert ll[:2] == [0, 1]
    assert ll[1:] == [1, 2, 3, 4]
    assert ll[:-1] == [0, 1, 2, 3]
    assert ll[1:-1] == [1, 2, 3]
    assert ll[3:3] == []
    assert ll == [0, 1, 2, 3, 4]

    assert ll[1::2] == [1, 3]
    assert ll[1:-1:2] == [1, 3]
    assert ll == [0, 1, 2, 3, 4]


# Generated at 2022-06-13 19:55:24.632370
# Unit test for function drop_until
def test_drop_until():
    from pytest import raises
    assert list(drop_until(Lambda.is_positive, [])) == []
    assert list(drop_until(Lambda.is_positive, [1])) == [1]
    assert list(drop_until(Lambda.is_positive, [1, 2, 3])) == [1, 2, 3]
    assert list(drop_until(Lambda.is_positive, [-1, -2])) == []
    assert list(drop_until(Lambda.is_positive, [-1, 1])) == [1]
    assert list(drop_until(Lambda.is_positive, [0, 0, 0, 1, 1])) == [1, 1]

# Generated at 2022-06-13 19:55:32.985476
# Unit test for function drop_until
def test_drop_until():
    for tup in itertools.product(range(5), range(5), range(5), range(5), range(5), range(5), range(5), range(5), range(5)):
        it = drop_until(lambda x: x == 1, tup)
        try:
            assert next(it) == 1
            assert list(it) == list(tup[1:])
        except StopIteration:
            pass



# Generated at 2022-06-13 19:55:37.590902
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    lst = LazyList(range(10000))
    assert lst[0] == 0
    assert lst[0] == 0
    del lst.list[:1]
    assert lst[0] == 0
    assert lst[-1] == 9999
    assert lst[:5:2] == [0, 2, 4]


# Generated at 2022-06-13 19:55:39.830821
# Unit test for method __iter__ of class LazyList
def test_LazyList___iter__():
    for val in LazyList([0, 1, 2, 3, 4]):
        print(val)

# Generated at 2022-06-13 19:55:46.554063
# Unit test for method __iter__ of class LazyList
def test_LazyList___iter__():
    # Given
    iterable = (1, 2, 3)
    lst = LazyList(iterable)

    # When
    # Then
    assert next(iter(lst)) == 1
    assert next(iter(lst)) == 2
    assert next(iter(lst)) == 3
    with pytest.raises(StopIteration):
        next(iter(lst))



# Generated at 2022-06-13 19:55:55.894286
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    assert list(Range(10)[:2]) == [0, 1]
    assert list(Range(1, 10)[2:]) == [3, 4, 5, 6, 7, 8, 9]
    assert list(Range(3, 20, 4)[::-1]) == [16, 12, 8, 4]
    assert list(Range(2, 10, 2)[::2]) == [2, 6]
    assert list(Range(1, 4)[::-1]) == [3, 2, 1]
    assert Range(2, 9, 3)[2:] == [8]
    assert Range(23, 50, 5)[::-1] == [45, 40, 35, 30, 25]


# Generated at 2022-06-13 19:56:09.047135
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    lst = [1,2,3]
    assert MapList(lambda x: x * 10, lst)[0] == 10
    assert MapList(lambda x: x * 10, lst)[1] == 20
    assert MapList(lambda x: x * 10, lst)[2] == 30
    assert MapList(lambda x: x * 10, lst)[-1] == 30


# Generated at 2022-06-13 19:56:11.064451
# Unit test for method __len__ of class LazyList
def test_LazyList___len__():
    assert len(LazyList(range(100))) == 100
    assert len(LazyList(range(100))) == 100

# Generated at 2022-06-13 19:56:21.112024
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    def gen(n):
        yield from (x for x in range(n) if x % 2 == 0)
    lst = LazyList(gen(10))
    assert lst[0] == 0
    assert lst[1:3] == [0, 2]
    assert lst[2:5] == [0, 2, 4]
    assert lst[:5] == [0, 2, 4, 6, 8]
    assert lst[5:] == [0, 2, 4, 6, 8]
    assert list(lst[5:]) == [0, 2, 4, 6, 8]
    assert lst == [0, 2, 4, 6, 8]
    assert list(lst) == [0, 2, 4, 6, 8]

# Generated at 2022-06-13 19:56:28.735683
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(10)
    # start = 0, stop = 10, step = 1
    assert(r[0] == 0)
    assert(r[1] == 1)
    assert(r[9] == 9)
    assert(r[-1] == 9)
    assert(r[-2] == 8)
    assert(r[-10] == 0)

    r = Range(10, 20)
    # start = 10, stop = 20, step = 1
    assert(r[0] == 10)
    assert(r[1] == 11)
    assert(r[9] == 19)
    assert(r[-1] == 19)
    assert(r[-2] == 18)
    assert(r[-10] == 10)

    r = Range(10, 20, 2)
    # start

# Generated at 2022-06-13 19:56:31.708867
# Unit test for method __len__ of class LazyList
def test_LazyList___len__():
    l = LazyList(range(100))
    assert len(l.list) == 0
    assert len(l) == 100
# Test if method __len__ of class LazyList throws an exception when iterable is not depleted

# Generated at 2022-06-13 19:56:44.600250
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    obj = MapList(lambda x: 2 * x, [1, 2, 3, 4, 5])
    assert len(obj) == 5
    assert obj[0] == 2
    assert obj[1] == 4
    assert obj[2] == 6
    assert obj[3] == 8
    assert obj[4] == 10
    assert obj[2 : 4] == [6, 8]
    assert obj[2 : 5] == [6, 8, 10]
    assert obj[3 : 4] == [8]
    assert obj[0 : 1] == [2]
    assert obj[0 : 0] == []
    assert obj[: 5] == [2, 4, 6, 8, 10]
    assert obj[2 :] == [6, 8, 10]
    assert obj[: 3] == [2, 4, 6]

# Generated at 2022-06-13 19:56:49.325394
# Unit test for method __len__ of class LazyList
def test_LazyList___len__():
    from unittest.mock import MagicMock
    from pyrogram.api.core import TLObject
    from pyrogram.client.ext import BaseClient
    from . .__main__ import Client
    client = Client()
    TLObject.__len__ = MagicMock()
    client.get_messages(chat_id=1, offset_id=2, limit=3)
    assert TLObject.__len__.call_count == 1

# Generated at 2022-06-13 19:56:54.739436
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    def t(idx, expected):
        lst = LazyList(range(10))
        actual = lst[idx]
        assert actual == expected

    t(0, 0)
    t(-1, 9)
    t(slice(0, 2), [0, 1])
    t(slice(-1, None), [9])
    t(slice(-3, -1), [7, 8])
    assert len(LazyList(range(10))) == 10
    with pytest.raises(TypeError):
        len(LazyList(range(5)))



# Generated at 2022-06-13 19:57:01.863100
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    assert MapList(lambda x: x + 5, [0, 1, 2, 3, 4, 5])[3] == 8
    assert MapList(lambda x: x + 5, [0, 1, 2, 3, 4, 5])[:3] == [5, 6, 7]



# Generated at 2022-06-13 19:57:06.755817
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    ll = LazyList(range(10))
    assert ll[2] == 2
    assert ll[-1] == 9
    assert ll[0:5] == [0, 1, 2, 3, 4]
    assert ll[2:5:2] == [2, 4]
    assert ll[-1:0] == []



# Generated at 2022-06-13 19:57:29.487885
# Unit test for function split_by
def test_split_by():
    assert list(split_by(range(10))) == [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]
    assert list(split_by(range(10), criterion=lambda x: x % 3 == 0)) == [[1, 2], [4, 5], [7, 8]]
    assert list(split_by(" Split by: ", separator='.')) == [['S', 'p', 'l', 'i', 't', 'b', 'y', ':']]
    assert list(split_by(" Split by: ", empty_segments=True, separator='.')) == [[], ['S', 'p', 'l', 'i', 't'], ['b', 'y', ':'], []]



# Generated at 2022-06-13 19:57:38.365719
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(10)
    assert r[0] == 0
    assert r[9] == 9
    assert r[-1] == 9
    assert list(r[:]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert list(r[:0]) == []
    assert list(r[:9]) == [0, 1, 2, 3, 4, 5, 6, 7, 8]
    assert list(r[9:]) == [9]
    assert list(r[1:-1]) == [1, 2, 3, 4, 5, 6, 7, 8]
    assert list(r[1:-2]) == [1, 2, 3, 4, 5, 6, 7]

# Generated at 2022-06-13 19:57:52.221207
# Unit test for function drop_until
def test_drop_until():
    # Basic test
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x > 5, [])) == []
    # Test with equality predicate
    assert list(drop_until(lambda x: x == 5, range(10))) == [5, 6, 7, 8, 9]
    # Test with predicate that is always true
    assert list(drop_until(lambda x: True, range(10))) == list(range(10))
    # Test with predicate that is always false
    assert list(drop_until(lambda x: False, range(10))) == []
    # Test with exception raised by predicate

# Generated at 2022-06-13 19:58:00.389470
# Unit test for method __len__ of class LazyList
def test_LazyList___len__():
    _0 = LazyList(range(10))
    assert len(_0) == 10
    try:
        len(_0)
        assert False, "should raise TypeError"
    except TypeError:
        pass


    _1 = LazyList([])
    assert len(_1) == 0

    _2 = LazyList(range(10))
    assert len(_2[:5]) == 5
    assert len(_2[4:]) == 6

# Generated at 2022-06-13 19:58:10.836335
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    def assert_getter_equals(getter, expected_values, expected_length):
        assert isinstance(getter, MapList)
        assert list(getter) == expected_values
        assert list(getter[:]) == expected_values
        assert list(getter[::2]) == expected_values[::2]
        assert getter[0] == expected_values[0]
        assert getter[1] == expected_values[1]
        assert getter[-2] == expected_values[-2]
        assert getter[-1] == expected_values[-1]
        assert getter[:3] == expected_values[:3]
        assert getter[3:] == expected_values[3:]
        assert getter[:-1] == expected_values[:-1]

# Generated at 2022-06-13 19:58:12.958805
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]



# Generated at 2022-06-13 19:58:20.116657
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(1, 10 + 1)
    print(r[0], r[2], r[4])
    print(r[-1], r[-3], r[-5])
    print(r[0:3])
    print(r[2:5])
    print(r[-3:-1])
    print(r[-3:3])
    print(r[:3])
    print(r[2:])
    print(r[::2])



# Generated at 2022-06-13 19:58:26.260254
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    if __name__ == '__main__':
        r = Range(1, 2 + 1)
        print(r)
        print(r[0], r[1], r[2])
        print(r[:] == [1, 2, 3])
        print(r[1:3])
        r[1] = 1
        assert r[0] == 1 and r[1] == 2 and r[2] == 3


# Generated at 2022-06-13 19:58:39.685073
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    test = Range(10)
    assert test[3] == 3
    assert test[9] == 9
    assert test[0] == 0
    assert test[-1] == 9
    assert test[-2] == 8
    assert test[1] == 1
    assert test[-10] == 0
    assert test[-11] == Exception
    assert test[10] == Exception
    assert test[-1:2] == [9, 0, 1]
    assert test[slice(2, None)] == [2, 3, 4, 5, 6, 7, 8, 9]
    assert test[slice(None, None, 2)] == [0, 2, 4, 6, 8]
    assert test[slice(-2, 2)] == [8, 9, 0, 1]

# Generated at 2022-06-13 19:58:56.650542
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    # Create an instance
    instance = Range(1,1,1)
    # Test for various types of indices
    item0 = 0
    expected0 = 1
    actual0 = instance.__getitem__(item0)
    assert expected0 == actual0
    item1 = 'abc'
    expected1 = 1
    actual1 = instance.__getitem__(item1)
    assert expected1 == actual1
    item2 = [1,2,3]
    expected2 = 1
    actual2 = instance.__getitem__(item2)
    assert expected2 == actual2
    item3 = slice(1,1,1)
    expected3 = 1
    actual3 = instance.__getitem__(item3)
    assert expected3 == actual3
    item4 = slice('abc','abc','abc')

# Generated at 2022-06-13 19:59:16.452018
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    l1 = LazyList(range(100))
    for i in range(100):
        assert l1[i] == i
    assert l1[99] == 99
    assert isinstance(l1[99:100], list)
    assert l1[99:100] == [99]

    l2 = LazyList(map(str, range(100)))
    assert l2[99] == '99'

# Generated at 2022-06-13 19:59:28.109828
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    lst = MapList(lambda x: x * x, [2, 3, 5])
    # * Call function with index of existing element
    idx = 1
    assert lst[idx] == (3 * 3)
    # * Call function with index of non-existing element
    idx = 3
    try:
        lst[idx]
    except IndexError:
        assert True
    else:
        assert False
    # * Call function with slice of valid indices
    idx = slice(1, 3, 1)
    assert lst[idx] == [3 * 3, 5 * 5]
    # * Call function with slice of invalid indices
    idx = slice(1, 3, 1)
    try:
        lst[idx]
    except IndexError:
        assert True
    else:
        assert False

# Generated at 2022-06-13 19:59:31.071445
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    lst = Range(3)
    assert lst[1:-1] == [1]
    assert lst[1:-2] == []
    assert lst[-2] == 1
    assert lst[-4] == -1



# Generated at 2022-06-13 19:59:38.317237
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    a = [1, 2, 3, 4, 5]
    from bisect import bisect_left
    pos = bisect_left(__main__.MapList(lambda x: x * x, a), 10)
    assert pos == 3
    b = [2, 3, 4, 5, 6]
    pos = bisect_left(__main__.MapList(lambda i: a[i] * b[i], __main__.Range(len(a))), 10)
    assert pos == 2


# Generated at 2022-06-13 19:59:43.808068
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    from pprint import pprint
    def split_by_numbers_3(lst):
        for i in lst:
            if i % 3 == 0:
                yield [i]
            else:
                yield i
    l = LazyList(split_by_numbers_3(range(100)))
    pprint([l[i] for i in range(0, 10)])
    pprint([l[i] for i in range(0, 10)])
    pprint([l[i] for i in range(10, 20)])


# Generated at 2022-06-13 19:59:50.606238
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x == 5, range(10))) == [5, 6, 7, 8, 9]
    assert list(drop_until(lambda x: x > 5,  range(10))) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x == 30, range(10))) == []
    assert list(drop_until(lambda x: x > 30,  range(10))) == []



# Generated at 2022-06-13 20:00:00.077192
# Unit test for method __iter__ of class LazyList
def test_LazyList___iter__():
    class StreamingSequence:
        def __init__(self, it: Iterable[T]):
            self.it = iter(it)

        def __getitem__(self, idx: object) -> T:
            if isinstance(idx, int):
                self.it = drop(idx, self.it)
            elif isinstance(idx, slice):
                self.it = drop(idx.stop if idx.stop is not None and idx.stop >= 0 else float('inf'), self.it)
            else:
                raise TypeError("`idx` should be an `int` or a `slice` object")
            return next(self.it)

    def test(it: Iterable[T], expected: Sequence[T]) -> None:
        ll = LazyList(StreamingSequence(it))
       

# Generated at 2022-06-13 20:00:10.231810
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    from random import choice
    from pytest import raises
    from itertools import chain
    for i in chain([-1, 0, 1], range(0, 10, 2)):
        lst = list(range(i))
        m = MapList(lambda x: x * i, lst)
        assert [x * i for x in lst] == m[:]
        assert [x * i for x in lst[::i]] == m[::i]
        assert [x * i for x in lst[:i]] == m[:i]
        assert [x * i for x in lst[i:]] == m[i:]
        assert [x * i for x in lst[i::i]] == m[i::i]

# Generated at 2022-06-13 20:00:15.995347
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    t = Range(1,2)
    assert t[0] == 1
    t = Range(1,2, 0)
    assert t[0] == 1
    t = Range(0)
    assert t[0] == 0
    t = Range(1,2, 2)
    assert t[0] == 1


# Generated at 2022-06-13 20:00:21.302732
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    v = MapList(lambda x: x * 2, [1, 2, 3, 4, 5])
    assert v[0] == 2
    assert v[1] == 4
    assert v[2] == 6
    assert v[3] == 8
    assert v[4] == 10
    assert v[0:3] == [2, 4, 6]

# Generated at 2022-06-13 20:00:50.252722
# Unit test for method __iter__ of class LazyList
def test_LazyList___iter__():
    # type: () -> None
    lst = LazyList(range(3))
    assert list(lst) == [0, 1, 2]
    assert list(lst) == [0, 1, 2]  # no need to iterate again
    assert list(lst.__iter__()) == [0, 1, 2]
    assert list(lst) == [0, 1, 2]  # no need to iterate again
    assert list(lst.__iter__()) == [0, 1, 2]


# Generated at 2022-06-13 20:00:51.398958
# Unit test for method __iter__ of class LazyList
def test_LazyList___iter__():
    pass  # TODO


# Generated at 2022-06-13 20:01:01.363824
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(0, 10)
    assert len(r) == 10
    assert r[0] == r[-10] == 0
    assert r[2] == r[-8] == 2
    assert r[3:7] == [3, 4, 5, 6]
    assert r[5:2:-1] == [5, 4, 3]
    assert r[::-1] == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert r[::-2] == [9, 7, 5, 3, 1]
    assert r[1::2] == [1, 3, 5, 7, 9]
    r = Range(1, 10)
    assert len(r) == 9
    assert r[0] == r[-9] == 1

# Generated at 2022-06-13 20:01:10.442765
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    a = Range(-3, 0, 1)
    assert a[0] == -3
    assert a[-1] == -3
    assert a[-3] == -3
    assert [a[i] for i in range(0, len(a), 1)] == [-3, -2, -1]
    assert [a[i] for i in range(0, len(a) + 1, 1)] == [-3, -2, -1]
    assert [a[i] for i in range(-3, 0, 1)] == [-3, -2, -1]
    assert [a[i] for i in range(-10, 0, 1)] == [-3, -2, -1]
    assert [a[i] for i in range(-10, -3, 1)] == [-3, -2, -1]

# Generated at 2022-06-13 20:01:19.009104
# Unit test for method __len__ of class LazyList
def test_LazyList___len__():
    lst = LazyList(range(1000000))
    assert len(lst) == 1000000
    assert lst[:10] == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert len(lst) == 1000000
    assert lst[999990:] == [999990, 999991, 999992, 999993, 999994, 999995, 999996, 999997, 999998, 999999]
    assert len(lst) == 1000000



# Generated at 2022-06-13 20:01:25.157154
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    import bisect
    a = [1, 2, 3, 4, 5]
    pos = bisect.bisect_left(MapList(lambda x: x * x, a), 10)
    assert pos == 3
    b = [2, 3, 4, 5, 6]
    pos = bisect.bisect_left(MapList(lambda i: a[i] * b[i], Range(len(a))), 10)
    assert pos == 2



# Generated at 2022-06-13 20:01:34.800066
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    range1 = Range(10)
    assert range1[-6] == 4
    assert range1[-10] == 0
    assert range1[-11] == IndexError
    assert range1[0] == 0
    assert range1[-1] == 9
    assert range1[1] == 1
    assert range1[-2] == 8
    assert range1[2] == 2
    assert range1[3] == 3
    assert range1[5] == 5
    assert range1[10] == IndexError
    assert range1[11] == IndexError



# Generated at 2022-06-13 20:01:37.872373
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    assert MapList(lambda x: x * x, [1, 2, 3, 4, 5])[2] == 9


# Generated at 2022-06-13 20:01:41.820649
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(100)
    assert r[0] == 0
    assert r[1] == 1
    assert r[50] == 50
    assert r[-1] == 99
    assert r[-2] == 98



# Generated at 2022-06-13 20:01:50.402944
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    # Find index of the first element in `a` whose square is >= 10.
    a = [1, 2, 3, 4, 5]
    pos, = [i for i, x in enumerate(MapList(lambda x: x * x, a)) if x >= 10]
    assert pos == 3
    
    # Find the first index i such that a[i] * b[i] >= 10.
    b = [2, 3, 4, 5, 6]
    pos, = [i for i, x in enumerate(MapList(lambda i: a[i] * b[i], Range(len(a)))) if x >= 10]
    assert pos == 2

# Generated at 2022-06-13 20:02:14.299999
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    # pylint: disable=unused-variable
    if False:
        from typing import List, Sequence, Tuple
    if False:
        from typing import TypeVar
    T = TypeVar('T')
    R = TypeVar('R')
    def func(i: T) -> R:
        ...
    lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # TypeChecks the value returned by method __getitem__ of class MapList.
    # If false, then the type is wrong.
    # If true, then the type is correct.
    # val is the correct type
    # TypeChecks the type of the arguments of method __getitem__ of class MapList.
    # If false, then the type is wrong.
    # If true, then the type is correct.
   