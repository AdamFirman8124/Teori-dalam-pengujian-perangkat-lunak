

# Generated at 2022-06-13 19:52:31.385848
# Unit test for function chunk
def test_chunk():
    assert list(chunk(3, [1, 2, 3, 4, 5, 6, 7, 8, 9])) == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert list(chunk(3, [])) == []
    assert list(chunk(3, [1, 2, 3, 4, 5])) == [[1, 2, 3], [4, 5]]
    assert list(chunk(0, [1, 2, 3, 4, 5])) == ValueError
    with assert_raises(ValueError):
        list(chunk(-1, [1, 2, 3, 4, 5]))


# Generated at 2022-06-13 19:52:39.655035
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    test_cases = [
        (Range(1, 10), 0, 1),
        (Range(1, 10), 8, 9),
        (Range(1, 10), 0, 1),
        (Range(1, 10), 9, IndexError),
        (Range(1, 10), -1, 9),
        (Range(1, 10, 2), 2, 5),
        (Range(1, 10, 2), -1, 7),
        (Range(1, 10, 2), 0, 1),
        (Range(1, 10, 2), 9, IndexError),
        (Range(1, 10, 2), -1, 7),
        (Range(1, 10, 2), -3, 3),
    ]
    run_test_func(test_cases, lambda lst, idx: lst[idx])

# Unit

# Generated at 2022-06-13 19:52:43.113560
# Unit test for function take
def test_take():
    assert list(take(5, range(1000000))) == [0, 1, 2, 3, 4]
    try:
        list(take(-1, range(1000000)))
        assert False
    except:
        pass

    

# Generated at 2022-06-13 19:52:49.058228
# Unit test for function drop
def test_drop():
    assert list(drop(2, [1,2,3,4,5])) == [3,4,5]
    assert list(drop(0, [1,2,3,4,5])) == [1,2,3,4,5]
    #assert list(drop(-2, [1,2,3,4,5])) == ValueError


# Generated at 2022-06-13 19:52:57.606436
# Unit test for function take
def test_take():
    print("Test function take")
    print("Test:1")
    for i in take(3, range(5)):
        print(i, end=" ")
    print("")
    print("Test:2")
    for i in take(0, range(5)):
        print(i, end=" ")
    print("")
    print("Test:3")
    for i in take(-1, range(5)):
        print(i, end=" ")
    print("")
    print("Test:4")
    for i in take(100, range(5)):
        print(i, end=" ")
    print("")
    print("Test:5")
    for i in take(3, []):
        print(i, end=" ")
    print("")



# Generated at 2022-06-13 19:53:00.423988
# Unit test for function take
def test_take():
    assert list(take(5, "abcdefg")) == ['a', 'b', 'c', 'd', 'e']



# Generated at 2022-06-13 19:53:06.826990
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == list(range(6, 10))
    assert list(drop_until(lambda x: x < 0, range(10))) == []
    assert list(drop_until(lambda x: x == "bar", ["foo", "bar", "baz"])) == ["bar", "baz"]
    assert list(drop_until(lambda x: False, ["foo", "bar"])) == ["foo", "bar"]


# Generated at 2022-06-13 19:53:17.644948
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    # Test cases
    lst = [1, 2, 3, 4]
    # Arguments for the unit test
    arguments = [(MapList(int,lst),0), (MapList(lambda x: 2*x,lst),0), (MapList(lambda x: 2*x,lst),3), (MapList(lambda x: 2*x,lst),slice(0,2)), (MapList(lambda x: 2*x,lst),slice(-1,None)), (MapList(lambda x: 2*x,lst),slice(1,3))]
    results = [1, 2, 8, [0, 4], [8], [4, 6]]
    message = "Wrong answer for lst = {}, index = {}"

# Generated at 2022-06-13 19:53:31.493938
# Unit test for function split_by
def test_split_by():
    assert list(split_by(range(3))) == [[0, 1, 2]]
    assert list(split_by(range(7), criterion=lambda x: x % 3 == 0)) == [[1, 2], [4, 5]]
    assert list(split_by(range(7), criterion=lambda x: x % 3 == 0, empty_segments=True)) == [[], [1, 2], [], [4, 5], []]
    assert list(split_by("a.b.c.d", separator=".")) == [["a", "b", "c", "d"]]
    assert list(split_by("a.b.c.d", empty_segments=True, separator=".")) == [["a"], ["b"], ["c"], ["d"]]

# Generated at 2022-06-13 19:53:35.450431
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
test_drop_until()



# Generated at 2022-06-13 19:53:48.637543
# Unit test for function take
def test_take():
    try:
        list(take(-1, [1, 2, 3]))
        assert False
    except ValueError:
        assert True

    assert list(take(2, [1, 2, 3])) == [1, 2]
    assert list(take(5, [1, 2, 3])) == [1, 2, 3]
    assert list(take(0, [1, 2, 3])) == []



# Generated at 2022-06-13 19:54:00.033051
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    print("Testing function __getitem__ for class MapList")
    m = MapList(lambda x: x*x, range(5))
    ls = []
    for i in range(5):
        ls.append(m[i])
    assert ls == [0, 1, 4, 9, 16]
    assert m[1:3] == [1, 4]
    assert m[::2] == [0, 4, 16]
    assert m[1:5:2] == [1, 9]
    print("Testing function __getitem__ for class MapList: OK !")


# Generated at 2022-06-13 19:54:01.809513
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    assert Range(0, 10)[8] == 8
    assert Range(0, 10)[-2] == 8
    assert Range(0, 10)[3:6] == [3, 4, 5]
    assert Range(0, 10, 2)[3:6] == [6, 8, 10]



# Generated at 2022-06-13 19:54:04.324159
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(1, 2)
    assert r[0] == 1
    assert r[-1] == 1
    assert r[0:1] == [1]
    assert r[:-1] == []
    assert r[-1:] == [1]



# Generated at 2022-06-13 19:54:08.154244
# Unit test for method __iter__ of class LazyList
def test_LazyList___iter__():
    from util.mockio import mockio
    with mockio():
        lst = LazyList(range(10))
        for i in lst:
            print(i)

test_LazyList___iter__()


# Generated at 2022-06-13 19:54:13.962333
# Unit test for method __len__ of class LazyList
def test_LazyList___len__():
    # Test exception
    try:
        LazyList(range(10))
    except TypeError:
        pass
    else:
        assert False

    # Test success
    lazy_list = LazyList(range(10))
    _ = lazy_list[:]
    assert len(lazy_list) == 10



# Generated at 2022-06-13 19:54:22.849639
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    lst_1 = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    lst_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    lst_3 = [1, 3, 5, 7, 9]
    assert list(Range(1, 11)) == lst_1
    assert list(Range(11)) == lst_1
    assert list(Range(1, 11, step=2)) == lst_2
    assert list(Range(11, step=2)) == lst_3

    r = Range(1, 11)
    r_slice = r[2:6]
    r_slice_2 = r[:6]
    r_slice_3 = r[2:]
    r_slice_4 = r[:]
    r_

# Generated at 2022-06-13 19:54:28.781877
# Unit test for method __len__ of class LazyList
def test_LazyList___len__():
    # Test for TypeError
    try:
        ll = LazyList([])
        len(ll)
    except TypeError:
        pass
    else:
        raise AssertionError
    ll = LazyList([1])
    len(ll)
    ll = LazyList([1, 2, 3])
    len(ll)
    ll = LazyList(i for i in range(10))
    try:
        len(ll)
    except TypeError:
        pass
    else:
        raise AssertionError
    ll = list(ll)
    assert len(ll) == 10


# Generated at 2022-06-13 19:54:34.041683
# Unit test for method __iter__ of class LazyList
def test_LazyList___iter__():
    lst = LazyList(range(10))
    it = iter(lst)
    for i in range(10):
        assert next(it) == i
    try:
        next(it)
        assert False
    except StopIteration:
        pass

# Generated at 2022-06-13 19:54:42.535264
# Unit test for function split_by
def test_split_by():
    assert split_by([1, 2, 3, 4], criterion=lambda x: x % 2 == 0) == [[1], [3]]
    assert list(split_by([1, 2, 4, 5, 6, 7], empty_segments=True, criterion=lambda x: x % 2 == 0)) == [[], [], [5, 7]]
    assert split_by([1, 2], criterion=lambda x: x % 3 == 0) == [[1, 2]]
    assert split_by([3, 1, 2], criterion=lambda x: x % 3 == 0) == [[], [1, 2]]

# Iterator version of ``scanl``, which is used in ``LazyList``

# Generated at 2022-06-13 19:54:59.385834
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    # Testing method __getitem__ of class MapList
    lst = MapList(lambda x: x * x, range(10))
    # Check that the generated list has the expected length
    assert len(lst) == 10
    # Check that the generated list is the expected one
    assert lst[0] == 0
    assert lst[1] == 1
    assert lst[2] == 4
    assert lst[3] == 9
    assert lst[4] == 16
    assert lst[5] == 25
    assert lst[6] == 36
    assert lst[7] == 49
    assert lst[8] == 64
    assert lst[9] == 81
    # Check that referencing an index out of bounds raises an error

# Generated at 2022-06-13 19:55:03.639940
# Unit test for method __iter__ of class LazyList
def test_LazyList___iter__():
    foo = LazyList(range(10))
    assert len(list(foo)) == 10
    assert len(list(foo)) == 10  # can iterate again
    foo.exhausted = True
    assert list(foo) == list(range(10))


# TODO: write tests

# Generated at 2022-06-13 19:55:11.223134
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == list(range(6,10))
    assert list(drop_until(lambda x: x > 5, range(5))) == []
    assert list(drop_until(lambda x: x > 0, range(5))) == list(range(1,5))
    assert list(drop_until(lambda x: x > 0, range(-2,2))) == list(range(1,2))
    assert list(drop_until(lambda x: x > 0, range(-2,0))) == []
    assert list(drop_until(lambda x: x > 0, [])) == []
    assert list(drop_until(lambda x: x > 5, (x for x in range(10)))) == list(range(6,10))

# Generated at 2022-06-13 19:55:17.534913
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    lst = [1, 2, 3, 4, 5]
    double_lst = MapList(lambda x: x * 2, lst)
    assert double_lst[0] == 2
    assert double_lst[4] == 10
    assert double_lst[2:4] == [6, 8]
    assert list(double_lst) == [2, 4, 6, 8, 10]
    assert len(double_lst) == len(lst)


# Generated at 2022-06-13 19:55:21.550531
# Unit test for function split_by
def test_split_by():
    assert list(split_by(" Split by: ", empty_segments=True, separator='.')) == [[], ['S', 'p', 'l', 'i', 't'], ['b', 'y', ':'], []]
    assert list(split_by(range(10), criterion=lambda x: x % 3 == 0)) == [[1, 2], [4, 5], [7, 8]]
test_split_by()



# Generated at 2022-06-13 19:55:23.529416
# Unit test for method __iter__ of class LazyList
def test_LazyList___iter__():
    lst = LazyList([0, 1, 2, 3])
    assert len(list(lst)) == len(lst)



# Generated at 2022-06-13 19:55:26.887090
# Unit test for function split_by
def test_split_by():
    assert list(split_by('abcd', criterion=lambda x: x == 'b')) == [['a'], ['c', 'd']]



# Generated at 2022-06-13 19:55:29.585889
# Unit test for method __iter__ of class LazyList
def test_LazyList___iter__():
    expected = list(range(10))
    actual = list(LazyList(range(10)))
    assert actual == expected



# Generated at 2022-06-13 19:55:40.095274
# Unit test for function split_by
def test_split_by():
    assert list(split_by(" Split by: ", empty_segments=True, separator='.')) == [[], ['S', 'p', 'l', 'i', 't'], ['b', 'y', ':'], []]
    assert list(split_by(" Split by: ", empty_segments=False, separator='.')) == [['S', 'p', 'l', 'i', 't'], ['b', 'y', ':']]
    assert list(split_by(range(10), criterion=lambda x: x % 3 == 0)) == [[1, 2], [4, 5], [7, 8]]
    assert list(split_by(range(10), criterion=lambda x: x % 2 == 0)) == [[], [2, 3, 4], [6, 7, 8], []]



# Generated at 2022-06-13 19:55:40.948865
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    pass



# Generated at 2022-06-13 19:55:56.949135
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    assert Range(10)[0] == 0
    assert Range(10)[1] == 1
    assert Range(10)[-1] == 9
    assert Range(10)[-10] == 0
    assert Range(100, 200)[100] == 200
    assert Range(100, 200)[0] == 100
    assert Range(100, 200)[-100] == 100
    assert Range(100, 200)[99] == 199
    assert Range(100, 200, 5)[4] == 125
    assert Range(20, 10)[0] == 20
    assert Range(10, 20, -1)[-1] == 11
    assert Range(10, 20, -1)[-10] == 20
    assert Range(10, 20, -2)[-1] == 11
    assert Range(10, 20, -2)[-5] == 15

# Generated at 2022-06-13 19:56:05.725153
# Unit test for function take
def test_take():
    assert list(take(3, range(5))) == [0, 1, 2]
    assert list(take(-1, range(5))) == []
    assert list(take(5, range(5))) == [0, 1, 2, 3, 4]
    assert list(take(10, range(5))) == [0, 1, 2, 3, 4]
    assert list(take(0, range(5))) == []

test_take()



# Generated at 2022-06-13 19:56:15.869526
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    range1 = Range(10)
    assert range1[0] == 0
    range2 = Range(1, 10 + 1)
    assert range2[0] == 1
    assert range2[2] == 3
    assert range2[4] == 5
    range3 = Range(1, 11, 2)
    assert range3[0] == 1
    assert range3[2] == 5
    assert range3[4] == 9
    range4 = Range(0,100,10)
    assert range4[0] == 0
    assert range4[1] == 10
    assert range4[2] == 20
    assert range4[3] == 30
    assert range4[4] == 40
    assert range4[5] == 50
    assert range4[6] == 60
    assert range4[7] == 70
   

# Generated at 2022-06-13 19:56:21.495143
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    assert Range(10)[0] == 0
    assert Range(10)[4] == 4
    assert Range(10, 20)[0] == 10
    assert Range(10, 20)[4] == 14
    assert Range(10, 20, 2)[0] == 10
    assert Range(10, 20, 2)[1] == 12
    assert Range(10, 21, 2)[2] == 14


# Generated at 2022-06-13 19:56:24.417930
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    obj = Range(9)
    assert isinstance(obj[1], int)
    assert isinstance(obj[-1], int)
    assert isinstance(obj[1:4], list)
    assert isinstance(obj[-1:4], list)

# Generated at 2022-06-13 19:56:25.744956
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    #TODO: Implement unit test
    raise NotImplementedError()


# Generated at 2022-06-13 19:56:28.365653
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    x1 = MapList(lambda x: x * x, [1, 2, 3, 4, 5]);
    assert x1[2] == 9;
    assert x1[-1] == 25;
    assert x1[1:3] == [4, 9];

# Generated at 2022-06-13 19:56:33.133665
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    a = [1, 2, 3, 4, 5]
    lst = MapList(lambda x: x * x, a)
    assert lst[2] == 9
    assert lst[1:4] == [4, 9, 16]
    assert list(lst) == [1, 4, 9, 16, 25]



# Generated at 2022-06-13 19:56:45.284156
# Unit test for function scanl
def test_scanl():
    assert list(scanl(lambda x, y: x + y, [1, 2, 3, 4])) == [1, 3, 6, 10]
    assert list(scanl(lambda x, y: y + x, ['a', 'b', 'c', 'd'])) == ['a', 'ba', 'cba', 'dcba']
    assert list(scanl(lambda x, y: x + y, [1, 2, 3, 4], 5)) == [5, 6, 8, 11, 15]
    assert list(scanl(lambda x, y: x + y, [1, 2, 3, 4])) == list(scanl(lambda x, y: x + y, [1, 2, 3, 4], 0))

# Generated at 2022-06-13 19:56:53.300538
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    assert Range(1, 10, 2)[:4] == [1, 3, 5, 7]
    assert Range(1, 10, 2)[1:5:2] == [3, 7]
    assert Range(1, 10, 2)[1::] == [3, 5, 7, 9]
    assert Range(1, 10, 2)[::3] == [1, 7]
    assert Range(1, 10, 2)[:4:2] == [1, 5]
    assert Range(1, 10, 2)[::-1] == [9, 7, 5, 3, 1]
    assert Range(1, 10, 2)[4::-2] == [7, 3]
    assert Range(1, 10, 2)[5::-2] == [9, 5, 1]

# Generated at 2022-06-13 19:57:08.890159
# Unit test for function drop_until
def test_drop_until():
    a = list(drop_until(lambda x: x >= 2, [-1, 0, 1, 2, 3, 4]))
    assert len(a) == 4
    assert a[0] == 2
    a = list(drop_until(lambda x: x >= 5, [-1, 0, 1, 2, 3, 4]))
    assert len(a) == 0
    a = list(drop_until(lambda x: x >= 5, []))
    assert len(a) == 0
    a = list(drop_until(lambda x: x >= -5, [-1, 0, 1, 2, 3, 4]))
    assert len(a) == 6
    a = list(drop_until(lambda x: x < 1, [-1, 0, 1, 2, 3, 4]))
    print(a)

# Generated at 2022-06-13 19:57:14.419811
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(1, 10 + 1)
    print(r[0], r[2], r[4])
    r = Range(1, 11, 2)
    print(r[0], r[2], r[4])

if __name__ == '__main__':
    test_Range___getitem__()


# Generated at 2022-06-13 19:57:26.334973
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    a = [1, 2, 3, 4, 5]
    b = [2, 3, 4, 5, 6]
    lst = MapList(lambda x: a[x] * b[x], Range(len(a)))
    assert lst[0] == 2
    assert lst[1] == 6
    assert lst[2] == 12
    assert lst[3] == 20
    assert lst[4] == 30
    assert lst[:3] == [2, 6, 12]
    assert lst[2:5] == [12, 20, 30]
    assert lst[:] == [2, 6, 12, 20, 30]
    assert list(lst) == [2, 6, 12, 20, 30]



# Generated at 2022-06-13 19:57:36.586613
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    obj = Range(1, 10+1)
    assert [obj[i] for i in range(0, 10)] == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert [obj[i] for i in range(-10, 0)] == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert obj[10:20:2] == [11, 13, 15, 17, 19]
    assert obj[-1:] == [10]
    assert obj[:-1] == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert obj[-1:-10:-1] == [10, 9, 8, 7, 6, 5, 4, 3, 2]

# Generated at 2022-06-13 19:57:44.609677
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x % 2 == 0, range(10))) == list(range(0, 10, 2))
    assert list(drop_until(lambda x: x % 2 == 1, range(1, 10, 2))) == list(range(1, 10, 2))
    assert list(drop_until(lambda _: True, range(10))) == list(range(10))
    assert not list(drop_until(lambda _: False, range(10)))



# Generated at 2022-06-13 19:57:52.444621
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    obj = MapList(lambda x: x * x, [1, 2, 3, 4, 5])
    assert isinstance(obj[2], int)
    assert obj[2] == 9
    assert obj[-2] == 16
    assert obj[0:3] == [1, 4, 9]
    assert obj[:3] == [1, 4, 9]
    assert obj[3:] == [16, 25]
    assert obj[::2] == [1, 9, 25]
    return



# Generated at 2022-06-13 19:57:56.670553
# Unit test for function drop_until
def test_drop_until():
    iterable = [1,'a',4,6,4,4.4,4,4]
    test = drop_until(lambda x:x==4,iterable)
    assert next(test) == 4


# Generated at 2022-06-13 19:58:03.983444
# Unit test for function take
def test_take():
    print('Test Take 1:')
    print(list(take(5, range(1000000))))
    print('Test Take 2:')
    print(list(take(0, [3,4,5])))
    print('Test Take 3:')
    print(list(take(-1, [3,4,5])))


# Generated at 2022-06-13 19:58:08.275303
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
test_drop_until()



# Generated at 2022-06-13 19:58:15.745558
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(1, 10 + 1)
    assert r[0] == 1
    assert r[2] == 3
    assert r[-1] == 10

    assert r[5:8] == [6, 7, 8]
    assert r[:3] == [1, 2, 3]
    assert r[3:] == [4, 5, 6, 7, 8, 9, 10]
    assert r[::2] == [1, 3, 5, 7, 9]



# Generated at 2022-06-13 19:58:29.964332
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x>5, [1,2,3,4,5,6,7,8,9])) == [6,7,8,9]



# Generated at 2022-06-13 19:58:37.470523
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == list(range(6, 10))
    assert list(drop_until(lambda x: True, [])) == []
    assert list(drop_until(lambda x: False, range(10))) == list(range(10))
    assert list(drop_until(lambda x: x > -1, range(10))) == list(range(10))


# Generated at 2022-06-13 19:58:45.180218
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 0, range(-2, 10))) == list(range(1,10))
    # Test with empty array
    assert list(drop_until(lambda x: x > 0, range(0))) == list()
    # Test with full array
    assert list(drop_until(lambda x: x < 0, range(10))) == list(range(10))
    # Test with one element array
    assert list(drop_until(lambda x: x < 0, range(1))) == list()
    
test_drop_until()


# Generated at 2022-06-13 19:58:47.643696
# Unit test for function take
def test_take():
    try:
        assert(list(take(5, range(1000000))) == [0, 1, 2, 3, 4])
        print("take is correct")
    except:
        print("take is wrong")



# Generated at 2022-06-13 19:58:52.153849
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(10)
    assert r[4] == 4
    assert r[:4] == [0, 1, 2, 3]
    assert r[2:4] == [2, 3]
    assert r[::-1] == [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
    assert r[-2:] == [8, 9]
    assert r[:] == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# Generated at 2022-06-13 19:59:01.661648
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    print('test: [Range.__getitem__]')
    assert list(Range(1, 10, 3)[2:]) == [7]
    assert Range(10)[-1] == 9
    assert Range(10)[-1:][0] == 9
    assert Range(10)[:10:2] == list(range(0, 10, 2))
    assert Range(10)[::-1][:3] == [9, 8, 7]
    assert Range(10)[::-1][:3][2] == 7
    assert Range(10)[::-1][-2:] == [1, 0]

#Unit test for method __len__ of class Range

# Generated at 2022-06-13 19:59:08.788438
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(10)
    assert r[-1] == 9 and r[0] == 0 and r[3] == 3 and r[-2] == 8 and r[-5] == 5

    r = Range(5, 15)
    assert r[-1] == 14 and r[0] == 5 and r[3] == 8 and r[-2] == 13 and r[-5] == 10

    r = Range(5, 15, 2)
    assert r[-1] == 13 and r[0] == 5 and r[2] == 9 and r[-2] == 11 and r[-3] == 7


# Generated at 2022-06-13 19:59:12.516330
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    # start = None
    # step = None
    # stop = None
    for arg_1 in range(0, 100):
        for arg_2 in range(0, 100):
            for arg_3 in range(0, 100):
                actual = Range(start=None, step=None, stop=None)
                actual_outcome = actual[object()]
                assert actual_outcome == virtual_outcome



# Generated at 2022-06-13 19:59:22.377559
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():

    # Test arguments:
    # func: __getitem__
    # args: 
    # kwargs: {'idx': 0}
    # Output: 1
    # Expected output: 1
    assert Range(1, 11, 2).__getitem__("") == 1
    # Test arguments:
    # func: __getitem__
    # args: 
    # kwargs: {'idx': slice(None, None, None)}
    # Output: [1, 3, 5, 7, 9]
    # Expected output: [1, 3, 5, 7, 9]
    assert Range(1, 11, 2).__getitem__("") == [1, 3, 5, 7, 9]

# Generated at 2022-06-13 19:59:32.509380
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    # Test 3 of Range.__getitem__ with range as argument
    assert Range(0, 0, 1).__getitem__(range(1, 0, 1)) == []
    # Test 4 of Range.__getitem__ with range as argument
    assert Range(0, 0, 1).__getitem__(range(0, 0, 1)) == []
    # Test 4 of Range.__getitem__ with invalid argument
    with raises(TypeError):
        Range(0, 0, 1).__getitem__('x')
    # Test 4 of Range.__getitem__ with invalid argument
    with raises(TypeError):
        Range(0, 0, 1).__getitem__(1.0)
    # Test 4 of Range.__getitem__ with invalid argument
    with raises(TypeError):
        Range(0, 0, 1).__

# Generated at 2022-06-13 19:59:54.782561
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x, [1, 2, 0, 0, 1, 1, 2, 3, 4, 5])) == [1, 2, 0, 0, 1, 1, 2, 3, 4, 5]
    assert list(drop_until(lambda x: False, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) == []
    assert list(drop_until(lambda x: True, [])) == []
    assert list(drop_until(lambda x: x > 3, [0, 1, 2])) == []



# Generated at 2022-06-13 20:00:02.241446
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    assert Range(0, 10, 2)[1] == 2
    assert Range(0, 10, 2)[-1] == 8
    assert Range(1, 11, 2)[2] == 5
    assert Range(1, 11, 2)[-2] == 5
    assert Range(1, 10 + 1)[0::2] == [1, 3, 5, 7, 9]



# Generated at 2022-06-13 20:00:04.171636
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]


# Generated at 2022-06-13 20:00:15.794389
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(10)
    assert r[0] == 0
    assert r[2] == 2
    assert r[4] == 4
    assert r[-1] == 9
    assert r[-2] == 8
    assert r[-3] == 7
    assert r[:3] == [0, 1, 2]
    assert r[3:] == [3, 4, 5, 6, 7, 8, 9]
    assert r[1:3] == [1, 2]
    assert r[2:5] == [2, 3, 4]
    assert r[3:4] == [3]
    assert r[0:7:2] == [0, 2, 4, 6]
    assert r[::2] == [0, 2, 4, 6, 8]

# Generated at 2022-06-13 20:00:24.190124
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x > 10, range(10))) == []
    assert list(drop_until(lambda x: True, range(10))) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert list(drop_until(lambda x: False, range(10))) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert list(drop_until(lambda x: False, [])) == []
    assert list(drop_until(lambda x: x > 10, [])) == []



# Generated at 2022-06-13 20:00:28.082836
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x > 5, [])) == []
    assert list(drop_until(lambda x: x > 5, [6, 7, 8, 9])) == [6, 7, 8, 9]



# Generated at 2022-06-13 20:00:32.060734
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    xs = [1, 2, 3, 4, 5]
    mapl = MapList(lambda x: x * x, xs)
    assert mapl[2] == 9
    assert mapl[1:3] == [4, 9]

########################################################################################################################



# Generated at 2022-06-13 20:00:39.514481
# Unit test for function take
def test_take():
    assert list(take(3, [1, 2, 3, 4])) == [1, 2, 3]
    assert list(take(5, [])) == []
    assert list(take(0, [1, 2, 3])) == []
    assert list(take(0, [])) == []
    assert list(take(10, [1, 2, 3])) == [1, 2, 3]
    assert list(take(1, [1, 2, 3])) == [1]



# Generated at 2022-06-13 20:00:44.712451
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    assert Range(10)[0] == 0
    assert Range(10)[9] == 9
    assert Range(1, 10 + 1)[0] == 1
    assert Range(1, 10 + 1)[9] == 10
    assert Range(1, 11, 2)[0] == 1
    assert Range(1, 11, 2)[1] == 3
    assert Range(1, 11, 2)[4] == 9

# Generated at 2022-06-13 20:00:55.758369
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    from random import randint
    from random import choices
    from random import choice
    from random import randrange
    from random import uniform
    from cmath import phase
    from math import sqrt
    num_iter = 100 # The number of times to run this test
    num_test = 50 # Number of test cases to create in each iteration
    for test_num in range(num_iter):
        print("Running test #{0}".format(test_num + 1))
        num_elements = randint(1, 100)
        list_1 = [randint(-100, 100) for _ in range(num_elements)]
        num_elements = randint(1, 100)
        list_2 = [randint(0, 100) for _ in range(num_elements)]

# Generated at 2022-06-13 20:01:14.707183
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(0,10,2)
    assert r[1] == 2
    assert r[-1] == 8
    assert r[:4] == [0,2,4,6]
    assert r[3] == 6
    assert r[3:5] == [6,8]
    assert r[3:3] == []

# Generated at 2022-06-13 20:01:25.328604
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    lst = ["a", "b", "c"]
    assert MapList(lambda x: x.upper(), lst)[0] == "A"
    assert MapList(lambda x: x.upper(), lst)[1] == "B"
    assert MapList(lambda x: x.upper(), lst)[2] == "C"
    assert MapList(lambda x: x.upper(), lst)[:2] == ["A", "B"]
    assert MapList(lambda x: x.upper(), lst)[-2:] == ["B", "C"]
    assert MapList(lambda x: x.upper(), lst)[-1::-1] == ["C", "B", "A"]
    assert list(MapList(lambda x: x.upper(), lst)) == ["A", "B", "C"]


# Generated at 2022-06-13 20:01:35.004857
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r=Range(10)
    # Test indexing
    assert r[0] == 0
    assert isinstance(r[0],int)
    assert r[9] == 9
    assert isinstance(r[9],int)
    assert r[-1] == 9
    # Test slicing
    assert r[0:3] == [0,1,2]
    assert isinstance(r[0:3],list)
    assert r[0:10:2] == [0,2,4,6,8]
    assert isinstance(r[0:10:2],list)



# Generated at 2022-06-13 20:01:41.083733
# Unit test for function drop_until
def test_drop_until():
    l = list(range(10))
    for i in range(10):
        assert list(drop_until(lambda x: x > i, l)) == l[i + 1 :]
    l = ["a", "b", "c", True, 1, tuple()]
    for i in range(len(l)):
        assert list(drop_until(lambda x: x is l[i], l)) == l[i :]



# Generated at 2022-06-13 20:01:51.102153
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    for lst in [list(range(5)), list(range(10, 0, -1))]:
        lst = [x * x for x in lst]
        for i in range(len(lst)):
            assert MapList(lambda x: x * x, lst)[i] == lst[i]
        for i in range(len(lst)):
            assert MapList(lambda x: x * x, lst)[:i] == lst[:i]
        for i in range(len(lst)):
            assert MapList(lambda x: x * x, lst)[i:] == lst[i:]
        for i in range(len(lst)):
            assert MapList(lambda x: x * x, lst)[i:i] == lst[i:i]

# Generated at 2022-06-13 20:02:00.647144
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(10)
    assert isinstance(r, Range)
    assert r[0] == 0
    assert r[9] == 9

    r = Range(1, 10 + 1)
    assert isinstance(r, Range)
    assert r[0] == 1
    assert r[9] == 10

    r = Range(1, 11, 2)
    assert isinstance(r, Range)
    assert r[0] == 1
    assert r[2] == 5
    assert r[4] == 9



# Generated at 2022-06-13 20:02:09.863678
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x > 5, (x for x in range(10)))) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x > 5, range(3))) == []
    assert list(drop_until(lambda x: x > 5, (x for x in range(3)))) == []
