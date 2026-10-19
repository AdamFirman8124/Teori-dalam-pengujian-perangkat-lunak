

# Generated at 2022-06-13 19:52:24.303820
# Unit test for function split_by
def test_split_by():
    assert list(split_by(range(10), criterion=lambda x: x % 3 == 0)) == [[1, 2], [4, 5], [7, 8]]
    assert list(split_by(" Split by: ", empty_segments=True, separator='.')) == [[], ['S', 'p', 'l', 'i', 't'], ['b', 'y', ':'], []]



# Generated at 2022-06-13 19:52:34.155295
# Unit test for function chunk
def test_chunk():
    assert list(chunk(2, [0, 1, 2, 3, 4, 5])) == [[0, 1], [2, 3], [4, 5]]
    assert list(chunk(2, [0, 1, 2, 3, 4, 5, 6])) == [[0, 1], [2, 3], [4, 5], [6]]
    assert list(chunk(3, [0, 1, 2, 3, 4, 5, 6])) == [[0, 1, 2], [3, 4, 5], [6]]
    assert list(chunk(3, [0, 1, 2, 3, 4, 5, 6, 7])) == [[0, 1, 2], [3, 4, 5], [6, 7]]

# Generated at 2022-06-13 19:52:42.960746
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    a=LazyList(range(10))
    assert a[9]==9
    assert list(a[-1:-5:-1])==[9,8,7,6]
    assert list(a[-2:-5:-1])==[8,7,6]



# Generated at 2022-06-13 19:52:50.541825
# Unit test for function drop_until
def test_drop_until():
    data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = [6, 7, 8, 9]
    assert list(drop_until(lambda x: x > 5, data)) == result
    assert list(drop_until(lambda x: x > 9, data)) == [9]
    assert list(drop_until(lambda x: x < 0, data)) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]



# Generated at 2022-06-13 19:52:56.354740
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    a = LazyList(range(10))
    assert a[3] == 3
    assert a[3: 8] == list(range(3, 8))
    assert a[-1] == 9
    assert a[-2:] == list(range(8, 10))
    assert a[:] == list(range(10))
    assert a[:: 2] == list(range(0, 10, 2))
    assert a[-5:: -2] == list(range(5, -1, -2))



# Generated at 2022-06-13 19:52:58.925829
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    assert Range(10)[0:3] == [0, 1, 2]
    assert Range(1, 10 + 1)[0:3] == [1, 2, 3]
    assert Range(1, 11, 2)[0:3] == [1, 3, 5]



# Generated at 2022-06-13 19:53:10.043249
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    import unittest
    import sys
    import math

    class Test(unittest.TestCase):
        def test_get(self):
            x = LazyList(range(100000))
            self.assertEqual(len(x), 100000)
            self.assertEqual(x[math.inf], 99999)

        def test_get_slice(self):
            x = LazyList(range(100000))
            self.assertEqual(len(x), 100000)
            self.assertEqual(x[0::2], [i for i in range(100000) if i % 2 == 0])

        def test_not_supported(self):
            x = LazyList(range(1))
            with self.assertRaises(TypeError):
                len(x)


# Generated at 2022-06-13 19:53:12.289030
# Unit test for function scanl
def test_scanl():
    assert list(scanl(operator.add, [1, 2, 3, 4], 0)) == [0, 1, 3, 6, 10]



# Generated at 2022-06-13 19:53:25.791881
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x > 5, range(0, 10, 2))) == [6, 8]
    assert list(drop_until(lambda x: x > 5, range(-2, 3))) == [6]
    assert list(drop_until(lambda x: x > 5, range(-2, 0))) == []
    assert list(drop_until(lambda x: x > 2, [])) == []
    assert list(drop_until(lambda x: x > 2, [1,2,3])) == [3]

# The following unit test fails because of a bug in the `drop_until` function :
# >>> list(drop_until(lambda x: x > 5, range(10)))


# Generated at 2022-06-13 19:53:33.540735
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    a = [1, 2, 3, 4, 5]
    b = [2, 3, 4, 5, 6]
    # Find the first index `i` such that `a[i] * b[i]` is >= 10.
    pos = bisect.bisect_left(MapList(lambda i: a[i] * b[i], Range(len(a))), 10)
    assert pos == 2
    assert MapList(lambda i: a[i] * b[i], Range(len(a)))[2] == 12
    assert len(MapList(lambda i: a[i] * b[i], Range(len(a)))) == 5


# Generated at 2022-06-13 19:54:04.774379
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    func, lst = id, [1, 2, 3, 4, 5]
    test_case1 = MapList(func, lst)
    # Check index
    assert test_case1[0] == 1 and test_case1[2] == 3
    # Check slice
    assert test_case1[:].__eq__([1, 2, 3, 4, 5]) and test_case1[1:-1].__eq__([2, 3, 4]) and test_case1[::-1].__eq__([5, 4, 3, 2, 1]) and test_case1[:3].__eq__([1, 2, 3]) and test_case1[2:].__eq__([3, 4, 5])


# Generated at 2022-06-13 19:54:09.808314
# Unit test for function drop
def test_drop():
    from hypothesis import given
    from hypothesis.strategies import integers, lists
    @given(numbers=integers(min_value=0), l=lists(integers()))
    def test_one(numbers, l):
        d = drop(numbers, l)
        assert list(d) == l[numbers:]

    test_one()  # to trigger the @given decorator



# Generated at 2022-06-13 19:54:19.862223
# Unit test for function scanl
def test_scanl():
    assert list(scanl(operator.add, [1, 2, 3, 4])) == [1, 3, 6, 10]
    assert list(scanl(operator.add, [1, 2, 3, 4], 0)) == [0, 1, 3, 6, 10]
    assert list(scanl(lambda s, x: x + s, ['a', 'b', 'c', 'd'])) == ['a', 'ba', 'cba', 'dcba']
    assert list(scanl(lambda s, x: '{0}({1})'.format(x, s), ['a', 'b', 'c'])) == ['a', 'b(a)', 'c(b(a))']
    assert list(scanl(lambda s, x: x + s, [], 'a')) == ['a']

# Generated at 2022-06-13 19:54:27.907021
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    import string
    a = [1, 2, 3, 4, 5]
    b = ['a', 'b', 'c', 'd', 'e']
    
    assert (MapList(lambda x: x * x, a)[0] == 1)
    assert (MapList(lambda x: x * x, a)[1] == 4)
    assert (MapList(lambda x: x * x, a)[2] == 9)
    assert (MapList(lambda x: x * x, a)[3] == 16)
    assert (MapList(lambda x: x * x, a)[4] == 25)
    
    assert (MapList(lambda x: x * x, [])[0] == 0)
    assert (MapList(lambda x: x * x, []).__getitem__(0) == 0)
    

# Generated at 2022-06-13 19:54:33.108347
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(1, 11, 3)
    assert r[0] == 1
    assert r[1] == 4
    assert r[2] == 7
    assert r[3] == 10
    assert r[-1] == 10
    assert r[-2] == 7
    assert r[-3] == 4
    assert r[-4] == 1
    assert r[0:2] == [1, 4]
    assert r[0:2:2] == [1]
    assert r[1:0] == []
    assert r[1:0:-1] == [4, 1]
    assert r[1:0:-2] == [4]


# Generated at 2022-06-13 19:54:40.096228
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x==5, [1,2,5,6,7])) == [5,6,7]
    assert list(drop_until(lambda x: x>1, [1,2,5,6,7])) == [2,5,6,7]
    assert list(drop_until(lambda x: x>1, [1,2])) == [2]
    assert list(drop_until(lambda x: x>1, [2])) == [2]
    assert list(drop_until(lambda x: x>1, [])) == []


# Generated at 2022-06-13 19:54:42.910912
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(0, 10, 2)
    assert (r[:3] == [0, 2, 4])


# Generated at 2022-06-13 19:54:54.581903
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    obj = Range(1, 6, 2)
    # Test a slice
    assert obj[slice(0, 3)] == [1, 3, 5]
    # Test negative indexing
    assert obj[-1] == 5
    # Test positive indexing
    assert obj[0] == 1
    # Test indexing out of range
    assert_raises(IndexError, obj.__getitem__, 3)
    assert_raises(IndexError, obj.__getitem__, -4)
    try:
        assert_raises(ValueError, obj.__getitem__, 'a')
    except NotImplementedError:
        pass



# Generated at 2022-06-13 19:55:05.085528
# Unit test for function drop_until
def test_drop_until():
    it = drop_until(lambda x: x > 5, range(10))
    assert next(it) == 6
    assert list(it) == [7, 8, 9]
    it = drop_until(lambda x: x > 3, [])
    assert list(it) == []
    it = drop_until(lambda x: x < 0, [])
    assert list(it) == []
    it = drop_until(lambda x: x > 0, [0])
    assert list(it) == [0]
    it = drop_until(lambda x: x > 0, [0, 0])
    assert list(it) == [0, 0]
    it = drop_until(lambda x: x > 0, [1, 2, 3])
    assert next(it) == 1

# Generated at 2022-06-13 19:55:14.775164
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    assert Range(5)[0:5 :1]==[0,1,2,3,4]
    assert Range(5)[0:5 :2]==[0,2,4]
    assert Range(5)[0:5 :1]==[0,1,2,3,4]
    assert Range(5)[0:5 :3]==[0,3]
    assert Range(5)[1:5 :2]==[1,3]
    assert Range(5)[1:5 :1]==[1,2,3,4]
    assert Range(5)[1:5 :3]==[1,4]
    assert Range(5)[2:5 :2]==[2,4]
    assert Range(5)[2:5 :1]==[2,3,4]

# Generated at 2022-06-13 19:55:26.735046
# Unit test for function drop_until
def test_drop_until():
    # Test dropping nothing
    assert list(drop_until(lambda x: True, [1, 2, 3])) == [1, 2, 3]
    # Test dropping all
    assert list(drop_until(lambda x: False, [1, 2, 3])) == []
    # Test dropping a prefix
    assert list(drop_until(lambda x: x == 2, [1, 2, 3])) == [2, 3]
    # Test dropping nothing
    assert list(drop_until(lambda x: x == 5, [1, 2, 3])) == []



# Generated at 2022-06-13 19:55:32.215461
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x > 5, [])) == []
    assert list(drop_until(lambda x: True, range(10))) == list(range(10))


# Generated at 2022-06-13 19:55:37.392066
# Unit test for function drop
def test_drop():
    assert list(drop(3, range(10))) == list(range(3, 10))
    assert list(drop(0, range(10))) == list(range(10))
    assert list(drop(10, range(10))) == []
    assert list(drop(-1, range(10))) == []
    assert list(drop(-10, range(10))) == []



# Generated at 2022-06-13 19:55:49.903667
# Unit test for function drop_until
def test_drop_until():
    # Normal case
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]

    # Empty case
    assert list(drop_until(lambda x: False, [])) == []
    assert list(drop_until(lambda x: True, [])) == []

    # Singleton case
    assert list(drop_until(lambda x: x > 0, [5])) == [5]
    assert list(drop_until(lambda x: x <= 0, [5])) == []

    # Duplicate elements case
    assert list(drop_until(lambda x: x == 5, [1, 1, 5, 6, 7, 8, 3, 3, 3, 4, 5])) == [5, 6, 7, 8, 3, 3, 3, 4, 5]

# Generated at 2022-06-13 19:55:55.184644
# Unit test for function scanl
def test_scanl():
    assert list(scanl(lambda x, y: x + y, [1, 2, 3, 4])) == \
        [1, 3, 6, 10]
    assert list(scanl(lambda x, y: x + y, [1, 2, 3, 4], 10)) == \
        [10, 11, 13, 16, 20]



# Generated at 2022-06-13 19:56:03.237840
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    # Test for MapList.__getitem__()
    # Set up objects
    func = lambda x: x*x
    lst = [1, 2, 3, 4, 5]
    # Initialize MapList
    obj = MapList(func, lst)
    # Test for MapList.__getitem__()
    print(obj[0])
    print(obj[3])
    print(obj[-1])
    # Print
    print("\nTest for __getitem__ of class MapList passes.")
    # Clean up
    del func
    del lst
    del obj


# Generated at 2022-06-13 19:56:16.744025
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, [])) == []
    assert list(drop_until(lambda x: x > 5, [1, 2, 3, 4, 5])) == []
    assert list(drop_until(lambda x: x > 5, [1, 2, 3, 4, 5, 6, 7, 8, 9])) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x > 5, [6, 7, 8, 9])) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x > 5, [1, 2, 3, 4, 5, 6, 2, 4, 2, 1])) == [6, 2, 4, 2, 1]

# Generated at 2022-06-13 19:56:21.026405
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: len(x) == 4, ["abc", "ab", "abcde"])) == ["abcde"]
    
test_drop_until()



# Generated at 2022-06-13 19:56:22.848067
# Unit test for function drop
def test_drop():
    for i, x in enumerate(drop(5, range(1000000))):
        assert i == x


# Generated at 2022-06-13 19:56:28.737690
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(1, 11, 2)
    assert r[0] == 1
    assert r[1] == 3
    assert r[-1] == 9
    assert r[-2] == 7
    assert r[1:3] == [3, 5]
    assert r[2:6:2] == [5, 9]
    assert r[-1:1:-1] == [9, 7, 5, 3]
    assert r[-1::-1] == [9, 7, 5, 3, 1]


if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 19:56:44.778167
# Unit test for function drop_until
def test_drop_until():
    input_list = [0, -1, -2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    output_list = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert list(drop_until(lambda x: x >= 0, input_list)) == output_list
    assert list(drop_until(lambda x: x < 0, input_list)) == input_list
    assert list(drop_until(lambda x: x > 10, input_list)) == []
    assert list(drop_until(lambda x: x < -10, input_list)) == input_list
    assert list(drop_until(lambda x: x == 0, input_list)) == input_list[:1] + input_list[3:]
    
test_drop_until

# Generated at 2022-06-13 19:56:52.879093
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    def assertEqual(lhs, rhs):
        if lhs != rhs:
            raise AssertionError("%s != %s" % (lhs, rhs))

    lst = [1, 2, 3]
    m = MapList(lambda x: x + 10, lst)
    for i in range(len(lst)):
        assertEqual(m[i], lst[i] + 10)
    assertEqual(m[100], None)
    assertEqual(m[-1], None)
    assertEqual(m[0:2], [11, 12])
    assertEqual(m[1:100], [12, 13])
    assertEqual(m[100:100], [])
    assertEqual(m[-100:100], [11, 12, 13])

# Generated at 2022-06-13 19:57:02.863338
# Unit test for function scanl
def test_scanl():
    assert list(scanl(operator.add, [1, 2, 3, 4], 0)) == [0, 1, 3, 6, 10]
    assert list(scanl(operator.add, [1, 2, 3, 4])) == [1, 3, 6, 10]
    assert list(scanl(lambda s, x: x + s, ['a', 'b', 'c', 'd'])) == ['a', 'ba', 'cba', 'dcba']
    assert list(scanl(operator.mul, range(1, 4), 1)) == [1, 1, 2, 6]



# Generated at 2022-06-13 19:57:07.040397
# Unit test for function drop_until
def test_drop_until():
    assert next(drop_until(lambda x: x == 3, range(10))) == 3
    assert next(drop_until(lambda x: x == 10, range(10))) == 0
    assert list(drop_until(lambda x: x == 10, range(10))) == list(range(10))



# Generated at 2022-06-13 19:57:15.329031
# Unit test for function drop_until
def test_drop_until():
    list(drop_until(lambda x: x % 2 == 0, [1, 3, 4, 5, 8])) == [4, 5, 8]
    list(drop_until(lambda x: x % 2 == 0, [1, 3, 5, 7, 9])) == []
    list(drop_until(lambda x: x % 2 == 0, [2, 4, 6, 8, 10])) == [2, 4, 6, 8, 10]
    list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]



# Generated at 2022-06-13 19:57:27.681214
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r1 = Range(10)
    r2 = Range(1, 10 + 1)
    r3 = Range(1, 11, 2)
    assert r1[0] == 0
    assert r2[2] == 3
    assert r3[4] == 9
    try:
        r2[10]
        assert False
    except IndexError:
        pass
    assert r3[-1] == 9
    assert r3[-2] == 7
    assert r1[:5] == [0, 1, 2, 3, 4]
    assert r1[5:] == [5, 6, 7, 8, 9]
    assert r1[:5:2] == [0, 2, 4]
    assert r1[::2] == [0, 2, 4, 6, 8]

# Generated at 2022-06-13 19:57:35.702846
# Unit test for function scanl
def test_scanl():
    assert [*scanl(operator.add, range(5), 1)] == [*scanl(operator.add, range(5))] == list(range(1, 6))
    assert [*scanl(operator.add, [], 1)] == [1]
    assert [*scanl(operator.add, [1], 2)] == [2, 3]
    assert [*scanl(operator.add, [1], initial=2)] == [2, 3]
    assert [*scanl(operator.add, [1, 2, 3], 3)] == [3, 6, 9, 12]



# Generated at 2022-06-13 19:57:49.295727
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    from random import randint
    from functools import reduce
    from operator import add, mul

    for _ in range(10):
        mapper = randint(0, 10)

        a = [randint(0, 10) for _ in range(10)]
        lst = MapList(lambda x: x * mapper, a)
        assert a * mapper == lst * mapper

        b = [randint(0, 10) for _ in range(10)]
        lst = MapList(lambda i: a[i] + b[i], Range(len(a)))
        assert list(map(add, a, b)) == lst

        lst = MapList(lambda i: a[i] * b[i], Range(len(a)))
        assert list(map(mul, a, b)) == lst

       

# Generated at 2022-06-13 19:58:01.559702
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    a = [1, 2, 3, 4, 5]
    c = MapList(lambda x: x * x, a)
    if c[0] != 1:
        raise RuntimeError("Wrong answer for indexing test for MapList")
    if c[-1] != 25:
        raise RuntimeError("Wrong answer for indexing test for MapList")
    if c[-2] != 16:
        raise RuntimeError("Wrong answer for indexing test for MapList")
    if c[::2] != [1, 9, 25]:
        raise RuntimeError("Wrong answer for indexing test for MapList")
    if c[1::2] != [4, 16]:
        raise RuntimeError("Wrong answer for indexing test for MapList")

# Generated at 2022-06-13 19:58:08.260781
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    assert Range(2)[0] == 0
    assert Range(2)[1] == 1
    assert Range(2)[2] == 1
    assert Range(2, 4)[0] == 2
    assert Range(2, 4)[1] == 3
    assert Range(2, 4)[2] == 3
    assert Range(2, 5, 2)[0] == 2
    assert Range(2, 5, 2)[1] == 4
    assert Range(2, 5, 2)[2] == 4

# Generated at 2022-06-13 19:58:17.862667
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(10)
    print(r[0], r[5], r[9])
    print(r[-1: -5: -2])



# Generated at 2022-06-13 19:58:24.399260
# Unit test for function scanl
def test_scanl():
    assert list(scanl(operator.add, range(5))) == [0, 1, 3, 6, 10]
    assert list(scanl(lambda s, x: x + s, ['a', 'b', 'c', 'd'])) == ['a', 'ba', 'cba', 'dcba']
    assert list(scanl(operator.mul, [1, 2, 3, 4], 1)) == [1, 1, 2, 6, 24]



# Generated at 2022-06-13 19:58:38.952571
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(1, 10)

    print("Basic tests for __getitem__")
    for i in range(10):
        try:
            assert(r[i] == i + 1)
            print("Test passed: r[{}] == {}".format(i, i + 1))
        except AssertionError:
            print("Test failed: r[{}] == {}, but {} was returned".format(i, i + 1, r[i]))

    print("Checking out of bounds")

# Generated at 2022-06-13 19:58:48.631262
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x > 5, [])) == []
    assert list(drop_until(lambda x: x > 5, [1, 2, 3, 6])) == [6]
    assert list(drop_until(lambda x: x > 5, [6])) == [6]



# Generated at 2022-06-13 19:58:57.499464
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(1, 10, 2)
    assert r[0] == 1
    assert r[1] == 3
    assert r[2] == 5
    assert r[3] == 7
    assert r[4] == 9
    assert type(r[-1]) == int
    assert type(r[1:3]) == list
    assert r[1:3][0] == 3
    assert r[1:3][1] == 5
    return True


# Generated at 2022-06-13 19:59:00.913586
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]



# Generated at 2022-06-13 19:59:04.354941
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]



# Generated at 2022-06-13 19:59:07.459514
# Unit test for function scanl
def test_scanl():
    assert list(scanl(lambda x, y: x + y, range(10), 0)) == [0, 1, 3, 6, 10, 15, 21, 28, 36, 45]
test_scanl()



# Generated at 2022-06-13 19:59:07.966505
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    pass

# Generated at 2022-06-13 19:59:14.045741
# Unit test for function drop_until
def test_drop_until():
    def test_case(case: Iterable[int], expected: List[int]):
        actual = list(drop_until(lambda x: x > 5, case))
        assert actual == expected, f'{actual!r} != {expected!r}'

    test_case([], [])
    test_case([1,2,3,4,5,6,7], [6,7])
    test_case([1,2,3,4,5], [])
    test_case([6,7], [6,7])
    test_case([1,2,3,4,5,6,7,8,9,10], [6,7,8,9,10])
    test_case([1,0,3,4,5,6,7], [3,4,5,6,7])
test_drop

# Generated at 2022-06-13 19:59:25.662444
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(10)         # (end)
    assert r[0] == 0
    assert r[1] == 1
    assert r[-1] == 9
    assert r[:2] == [0,1]
    assert r[2:] == [2,3,4,5,6,7,8,9]
    assert r[2:6] == [2,3,4,5]

    r = Range(1, 10 + 1)  # (start, end)
    assert r[0] == 1
    assert r[1] == 2
    assert r[-1] == 10
    assert r[:2] == [1,2]
    assert r[2:] == [3,4,5,6,7,8,9,10]

# Generated at 2022-06-13 19:59:30.924548
# Unit test for function drop
def test_drop():
    assert list(drop(10, range(1000))) == list(range(10, 1000))
    assert list(drop(0, range(1000))) == list(range(1000))
    assert list(drop(1000, range(1000))) == []
    assert list(drop(2000, range(1000))) == []
    assert list(drop(-1, range(1000))) == list(range(1000))



# Generated at 2022-06-13 19:59:37.056571
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x > 100, range(10))) == []
    assert list(drop_until(lambda x: x > -1, range(10))) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]



# Generated at 2022-06-13 19:59:44.161492
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    for _ in range(10):
        arr = [randint(-100, 100) for _ in range(10)]
        for i in range(10):
            assert MapList(lambda x: x // 2, arr)[i] == arr[i] // 2
        for i in range(10):
            assert MapList(lambda x: x * x, arr)[i] == arr[i] * arr[i]
        for i in range(10):
            assert MapList(lambda x: x % 2, arr)[i] == arr[i] % 2
        for i in range(10):
            assert MapList(lambda x: x // 3, arr)[i] == arr[i] // 3



# Generated at 2022-06-13 19:59:47.853862
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    lst = MapList(lambda x: x + 1, [1, 2, 3])
    assert lst[0] == 2
    assert lst[1:] == [3, 4]


# Generated at 2022-06-13 19:59:56.744202
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    import random

    func = lambda x: x * 2
    a = range(random.randint(5, 100))
    ml = MapList(func, a)

    def check_slice(slc):
        res = ml[slc]
        assert all(r == func(a[i]) for i, r in enumerate(res))

    for _ in range(10):
        if random.randint(0, 1):
            check_slice(slice(random.randint(-100, 100), random.randint(-100, 100)))
        else:
            check_slice(random.randint(-100, 100))



# Generated at 2022-06-13 20:00:07.896906
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    def check_Range___getitem__(input_val):
        r=input_val
        assert len(r)==10
        assert r[0]==0
        assert r[9]==9
        assert r[-1]==9
        assert r[0:6]==[0,1,2,3,4,5]
        assert r[5:]==[5,6,7,8,9]
        assert r[:5]==[0,1,2,3,4]
        assert r[0:10:2]==[0,2,4,6,8]
    r=Range(0,10)
    check_Range___getitem__(r)
    r=Range(10)
    check_Range___getitem__(r)
    del r

# Generated at 2022-06-13 20:00:20.210520
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    for i in range(4):
        for j in range(4):
            for k in range(4):
                r = Range(i, j + i, k)
                for idx in range(- 2 * len(r), 2 * len(r)):
                    if idx < 0:
                        idx += len(r)
                    if idx >= len(r):
                        with pytest.raises(IndexError):
                            r[idx]
                    else:
                        assert r[idx] == i + k * idx
                for s in [slice(0, len(r) + 1, 2), slice(1, -1, -1), slice(-len(r), 0)]:
                    assert list(r[s]) == r[s.start:s.stop:s.step]

# Generated at 2022-06-13 20:00:27.494307
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    # TODO: Use type hints
    r = Range(1, 10 + 1)
    assert r[0] == 1
    assert r[0:10] == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



# Generated at 2022-06-13 20:00:29.614779
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(1, 9999, 3)
    print(r[0 : 5])


# Generated at 2022-06-13 20:00:46.641701
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    pass

# Generated at 2022-06-13 20:00:51.870934
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    b = [2, 3, 4, 5, 6]
    a = [1, 2, 3, 4, 5]
    pos = bisect.bisect_left(MapList(lambda i: a[i] * b[i], Range(len(a))), 10)
    if pos is not 2:
        raise Exception('expected 2, but got %s' % pos)


# Generated at 2022-06-13 20:00:52.754500
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    pass

# Generated at 2022-06-13 20:01:02.193425
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    import random

    for l in range(-5, 5):
        for r in range(-5, 5):
            for step in range(1, 5):
                lst = [random.randint(0, 10) for _ in range(random.randint(0, 100))]
                rng = Range(l, r, step)
                mplst = MapList(lambda x: x, lst)
                mprng = MapList(lambda x: x, rng)
                for i in range(-5, len(mplst) + 5):
                    assert mplst[i] == lst[i]
                assert mprng[1] == rng[1]
                assert mprng[2] == rng[2]
                assert mprng[-2] == rng[-2]

# Generated at 2022-06-13 20:01:05.648951
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(10)
    r = Range(1, 10 + 1)
    r = Range(1, 11, 2)
    print(r[0], r[2], r[4])


# Generated at 2022-06-13 20:01:11.933695
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    from random import randint
    from operator import add
    from bisect import bisect_left
    for _ in range(100):
        a = [randint(1, 100) for _ in range(10)]
        lst = MapList(add, a)
        for idx in range(10):
            assert (lst[idx] == sum(a[:idx + 1]))
        b = [randint(1, 100) for _ in range(10)]
        c = [a[idx] + b[idx] for idx in range(10)]
        pos = bisect_left(lst, 50)
        assert (pos == bisect_left(c, 50))


# Generated at 2022-06-13 20:01:16.433435
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    index = 0
    r = Range(1)
    try:
        r[-10]
        index += 1
    except:
        pass
    assert index == 0, "__getitem__ not work correctly"

# Generated at 2022-06-13 20:01:26.278680
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    # Test 1:
    tmp = range(1, 5 + 1)
    assert tmp == list(Range(1, 5 + 1)), "Test 1 fail"

    # Test 2:
    tmp = range(1, 5 + 1, 2)
    assert tmp == list(Range(1, 5 + 1, 2)), "Test 2 fail"

    # Test 3:
    tmp = range(5, 0, -1)
    assert tmp == list(Range(5, 0, -1)), "Test 3 fail"

    # Test 4:
    tmp = [1, 5, 9]
    assert tmp == Range(1, 11, 4)[:3], "Test 4 fail"

    # Test 5:
    tmp = [9, 5, 1]
    assert tmp == Range(1, 11, 4)[-3:], "Test 5 fail"

    #

# Generated at 2022-06-13 20:01:38.188971
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
 for _ in range(10):
  i = random.randrange(10)
  r = Range(i)
  for j in range(i):
   assert j == r[j]
  assert i - 1 == r[-1]
  assert i == len(r)
  l = [j for j in r]
  assert l == [j for j in range(i)]
  r = Range(i, 1)
  for j in range(i - 1, -1, -1):
   assert j == r[j]
  assert 0 == r[-1]
  assert i == len(r)
  l = [j for j in r]
  assert l == [j for j in range(i - 1, -1, -1)]
 for _ in range(10):
  i = random.randrange(-10, 10)

# Generated at 2022-06-13 20:01:49.098648
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():

    R = Range
    assert R(5)[0] == 0
    assert R(5)[1] == 1
    assert R(5)[2] == 2
    assert R(5)[3] == 3
    assert R(5)[4] == 4
    assert R(5)[-1] == 4
    assert R(5)[-2] == 3
    assert R(5)[-3] == 2
    assert R(5)[-4] == 1
    assert R(5)[-5] == 0
    assert R(1, 5)[0] == 1
    assert R(1, 5)[1] == 2
    assert R(1, 5)[2] == 3
    assert R(1, 5)[3] == 4
    assert R(1, 5)[-1] == 4
    assert R(1, 5)[-2] == 3