

# Generated at 2022-06-13 19:52:42.127573
# Unit test for function drop_until
def test_drop_until():
    for i in range(20):
        assert list(drop_until(lambda x: x >= 5, range(i))) == list(range(5, i))



# Generated at 2022-06-13 19:52:45.148287
# Unit test for function drop
def test_drop():
    it = [1,2,3,4,5]
    for x in drop(2,it):
        print(x)

test_drop()


# Generated at 2022-06-13 19:52:55.589327
# Unit test for function chunk
def test_chunk():
    assert list(chunk(3, range(10))) == [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]
    assert list(chunk(10, range(10))) == [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]
    assert list(chunk(11, range(10))) == [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]
    assert list(chunk(1, range(10))) == [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]]
    assert list(chunk(0, range(10))) == []

# Generated at 2022-06-13 19:53:04.168522
# Unit test for function take
def test_take():
    assert list(take(5, range(10))) == list(take(15, range(10))) == list(take(5, range(5))) == [0, 1, 2, 3, 4]
    assert list(take(0, range(10))) == []
    assert list(take(-1, range(10))) == []
    assert list(take(-10, range)) == []
    assert list(take(-10, [])) == []
    assert list(take(0, [])) == []
    assert list(take(-100, range(10))) == []
    assert list(take(-100, [])) == []


# Generated at 2022-06-13 19:53:11.984922
# Unit test for method __iter__ of class LazyList
def test_LazyList___iter__():
    lst = LazyList(range(100))

# Generated at 2022-06-13 19:53:17.329544
# Unit test for method __next__ of class Range
def test_Range___next__():
    assert next(Range(10)) == 0
    assert next(Range(0, 10, 2)) == 0
    assert next(Range(3, 10, 2)) == 3
    assert next(Range(10, -10, -2)) == 10
    with pytest.raises(StopIteration):
        next(Range(1, 0, -1))



# Generated at 2022-06-13 19:53:31.424331
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    assert list(LazyList(range(0, 5))[:]) == [0, 1, 2, 3, 4]
    assert list(LazyList(range(0, 5))[:3]) == [0, 1, 2]
    assert list(LazyList(range(0, 5))[:3:2]) == [0, 2]
    assert list(LazyList(range(0, 5))[0]) == [0]
    assert list(LazyList(range(0, 5))[0:2]) == [0, 1]
    assert list(LazyList(range(0, 5))[0:2:2]) == [0]
    assert list(LazyList(range(0, 5))[0:2:3]) == []
    assert list(LazyList(range(0, 5))[1])

# Generated at 2022-06-13 19:53:35.831257
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    lst = MapList(lambda x: x * x, [1, 2, 3, 4, 5])
    print(lst[2], lst[3], lst[2:4])


# Generated at 2022-06-13 19:53:49.254290
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x < 5, range(10))) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert list(drop_until(lambda x: x > 10, range(10))) == []
    assert list(drop_until(lambda x: x > -1, range(10))) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert list(drop_until(lambda x: x == 'a', 'abc')) == ['a']
    assert list(drop_until(lambda x: x == 'a', 'bc')) == []

# Generated at 2022-06-13 19:54:00.232790
# Unit test for function drop_until
def test_drop_until():
    # Test case 1
    result = drop_until(lambda x: x > 5, range(10))
    assert list(result) == [6, 7, 8, 9]

    # Test case 2
    result = drop_until(lambda x: x > 10, range(10))
    assert list(result) == []

    # Test case 3
    result = drop_until(
        lambda x: x % 2 == 0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    assert list(result) == [2, 3, 4, 5, 6, 7, 8, 9]



# Generated at 2022-06-13 19:54:27.768023
# Unit test for function split_by
def test_split_by():
    def split(l, criterion):
        return list(split_by(l, criterion=criterion))

    assert split([1, 2, 3, 4, 1, 2, 3, 4, 1, 2], lambda x: x == 3) == [[1, 2], [4], [1, 2], [4], [1, 2]]

    assert split([1, 2, 3, 4, 1, 2, 3, 4, 1, 2], lambda x: x == 3) == [[1, 2], [4], [1, 2], [4], [1, 2]]
    assert split([1, 2, 3], lambda x: x == 3) == [[1, 2]]
    assert split([1, 2], lambda x: x == 3) == [[1, 2]]
    assert split([], lambda x: x == 1) == []

# Generated at 2022-06-13 19:54:30.844354
# Unit test for function drop
def test_drop():
    a=5
    iterable = range(10)
    for i in drop(a, iterable):
        print(i)


# Generated at 2022-06-13 19:54:37.712169
# Unit test for function drop_until
def test_drop_until():
    it = drop_until(lambda x: x > 2, range(10))
    assert next(it) == 3
    assert next(it) == 4
    assert next(it) == 5
    assert next(it) == 6
    assert next(it) == 7
    assert next(it) == 8
    assert next(it) == 9
    try:
        next(it)
        assert False, "Expected StopIteration"
    except StopIteration:
        pass



# Generated at 2022-06-13 19:54:42.664408
# Unit test for function drop
def test_drop():
    # iterable is an iterator which is an instance of KStream
    iterable = drop(2, KStream([]))
    # this is the final result we expect
    correct_result = KStream([])
    assert next(iterable) == correct_result


# Generated at 2022-06-13 19:54:45.489372
# Unit test for function drop
def test_drop():
    x = list(drop(2, range(5)))
    assert x == [2, 3, 4]


# Generated at 2022-06-13 19:54:49.677381
# Unit test for function drop_until
def test_drop_until():
    itr = drop_until(lambda x: x > 5, range(10))
    # print(list(itr))
    assert list(itr) == [6, 7, 8, 9]



# Generated at 2022-06-13 19:54:55.622446
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    ll = LazyList(range(1000))
    assert ll[0] == 0
    assert ll[1] == 1
    assert ll[3] == 3
    assert isinstance(ll[3:9], list)
    assert ll[3:9] == [3, 4, 5, 6, 7, 8]



# Generated at 2022-06-13 19:54:59.436598
# Unit test for method __next__ of class Range
def test_Range___next__():
    r = Range(1, 11, 2)
    assert next(r) == 1
    assert next(r) == 3
    assert next(r) == 5
    assert next(r) == 7
    assert next(r) == 9

# Generated at 2022-06-13 19:55:04.446144
# Unit test for method __next__ of class Range
def test_Range___next__():
    range1 = Range(10)
    assert list(range1) == list(range(10))
    range1 = Range(1, 10 + 1)
    assert list(range1) == list(range(1, 10 + 1))
    range1 = Range(1, 11, 2)
    assert list(range1) == list(range(1, 11, 2))

# Generated at 2022-06-13 19:55:11.250927
# Unit test for function drop_until
def test_drop_until():
    l = [1,2,3,4,5,6,7,8,9,10,11]
    assert list(drop_until(lambda x: x > 5, l)) == [6,7,8,9,10,11]
    assert list(drop_until(lambda x: x > 2, l)) == [3,4,5,6,7,8,9,10,11]
    assert list(drop_until(lambda x: x > 11, l)) == []
    assert list(drop_until(lambda x: x > 0, l)) == [1,2,3,4,5,6,7,8,9,10,11]
    assert list(drop_until(lambda x: x > 12, l)) == []



# Generated at 2022-06-13 19:55:20.773592
# Unit test for function drop_until
def test_drop_until():
    assert (list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9])
    assert (list(drop_until(lambda x: x > 5, range(5))) == [])
    assert (list(drop_until(lambda x: x > 5, range(6))) == [5])



# Generated at 2022-06-13 19:55:23.131245
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    assert list(Range(0,11,1)) == [0,1,2,3,4,5,6,7,8,9,10]


# Generated at 2022-06-13 19:55:35.537563
# Unit test for function split_by
def test_split_by():
    list(split_by(["a", "b", "c", "d", "e", "f", "g"], criterion=lambda x: x == "c"))
    list(split_by(["a", "b", "c", "d", "e", "f", "g"], criterion=lambda x: x == "c", empty_segments=True))
    list(split_by(["a", "b", "c", "d", "e", "f", "g"], separator="c"))
    list(split_by(["a", "b", "c", "d", "e", "f", "g"], separator="c", empty_segments=True))
    list(split_by(" Split by: ", empty_segments=True, separator='.'))



# Generated at 2022-06-13 19:55:39.022158
# Unit test for method __next__ of class Range
def test_Range___next__():
    r = Range(1, 4)     # (start, end)
    assert next(r) == 1
    assert next(r) == 2
    assert next(r) == 3
    with pytest.raises(StopIteration):
        next(r)
        

# Generated at 2022-06-13 19:55:51.657181
# Unit test for function split_by
def test_split_by():
    # Call split_by with criterion specified
    assert list(split_by([1, 2, 3, 4, 5, 6], criterion=lambda x: x % 3 == 0)) == [[1, 2], [4, 5]]
    assert list(split_by(range(10), criterion=lambda x: x % 3 == 0)) == [[1, 2], [4, 5], [7, 8]]
    assert list(split_by(range(10), criterion=lambda x: x % 3 == 0, empty_segments=True)) == [[1, 2], [], [4, 5], [], [7, 8], []]
    assert list(split_by(range(10), criterion=lambda x: x % 3 == 0, empty_segments=True)) == [[1, 2], [], [4, 5], [], [7, 8], []]


# Generated at 2022-06-13 19:55:57.522661
# Unit test for method __next__ of class Range
def test_Range___next__():
    r = Range(0,0,0)
    assert r.__next__() == 0
    try:
        r.__next__()
        assert False
    except StopIteration:
        assert True
    r = Range(1,2,1)
    assert r.__next__() == 1
    try:
        r.__next__()
        assert False
    except StopIteration:
        assert True


# Generated at 2022-06-13 19:55:59.909691
# Unit test for function drop
def test_drop():
    assert list(drop(5, range(10))) == [5, 6, 7, 8, 9]
    assert list(drop(15, range(10))) == []



# Generated at 2022-06-13 19:56:04.617014
# Unit test for function split_by
def test_split_by():
    assert list(split_by(range(10), criterion=lambda x: x % 3 == 0)) == [[1, 2], [4, 5], [7, 8]]
    assert list(split_by(" Split by: ", empty_segments=True, criterion=lambda x: x.isspace())) == \
           [['S', 'p', 'l', 'i', 't'], ['b', 'y', ':']]



# Generated at 2022-06-13 19:56:15.017761
# Unit test for method __next__ of class Range
def test_Range___next__():
    # Test return value and exception
    assert list(Range(2)) == [0, 1, 2]
    assert list(Range(1, 2)) == [1, 2]
    assert list(Range(1, 3, 2)) == [1, 3]
    assert list(Range(3, 2, 1)) == []
    # Test thread safety
    r = Range(2)
    it = iter(r)
    assert list(it) == [0, 1, 2]
    assert list(it) == [0, 1, 2]
    # Test stopping criteria
    r = Range(1)
    it = iter(r)
    assert next(it) == 0
    with pytest.raises(StopIteration):
        next(it)
    # Test starting point
    r = Range(1, 3)

# Generated at 2022-06-13 19:56:19.732398
# Unit test for method __next__ of class Range
def test_Range___next__():
  # Test User Input:
  stop = 2
  # Expected Output:
  expectedOutput = 1
  # Test Code
  test = Range(stop)
  test.__next__()
  result = test.__next__()
  # Test Implementation
  assert result==expectedOutput

# Generated at 2022-06-13 19:56:31.275866
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    tests = [
        {'name' : 'test_Range___getitem___0', 'args' : [], 'expect' : []},
    ]

    for test in tests:
        r = Range(*test['args'])

# Generated at 2022-06-13 19:56:43.703169
# Unit test for function split_by
def test_split_by():
    assert list(split_by([], criterion=lambda x: x % 3 == 0)) == []
    assert list(split_by([1], criterion=lambda x: x % 3 == 0)) == [[1]]
    assert list(split_by([1, 2], criterion=lambda x: x % 3 == 0)) == [[1, 2]]
    assert list(split_by([1, 2, 3], criterion=lambda x: x % 3 == 0)) == [[1, 2]]
    assert list(split_by([1, 2, 3, 4], criterion=lambda x: x % 3 == 0)) == [[1, 2], [4]]
    assert list(split_by([1, 2, 3, 4, 5], criterion=lambda x: x % 3 == 0)) == [[1, 2], [4, 5]]

# Generated at 2022-06-13 19:56:54.638488
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    assert Range(4)[0] == 0
    assert Range(4)[1] == 1
    assert Range(4)[-1] == 3
    assert Range(4)[-2] == 2
    assert not ([0, 1, 2] == Range(4))
    assert not ([1, 2, 3] == Range(4))
    assert [0, 1, 2, 3] == Range(4)
    assert not ([0, 1, 2, 3, 4] == Range(4))
    assert [0, 2, 4] == Range(4)[0:3:2]
    assert [0, 2] == Range(4)[0:3:2]
    assert [0, 2] == Range(4)[:3:2]
    assert [0, 1, 2, 3] == Range(4)[::2]

# Generated at 2022-06-13 19:57:03.467176
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 1, range(1, 10))) == [2, 3, 4, 5, 6, 7, 8, 9]
    assert list(drop_until(lambda x: x > 1, range(1, 5))) == [2, 3, 4]
    assert list(drop_until(lambda x: x > 1, range(1, 2))) == []



# Generated at 2022-06-13 19:57:07.953498
# Unit test for function drop_until
def test_drop_until():
    import operator as op
    import random

    for k in range(5):
        for n in range(0, 10):
            a = list(range(n))
            random.shuffle(a)
            b = list(drop_until(lambda x: x <= k, a))
            assert b == [x for x in a if x >= k]



# Generated at 2022-06-13 19:57:15.943250
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    assert Range(0,10).__getitem__(0)==0
    assert Range(1,10,2).__getitem__(2)==5
    assert Range(0,10).__getitem__(5)==5
    assert Range(0,10).__getitem__(-1)==9
    assert Range(0,10).__getitem__(slice(2,5,1))==[2, 3, 4]
    assert Range(0,10).__getitem__([5,6,7])==[5, 6, 7]

# Generated at 2022-06-13 19:57:23.457626
# Unit test for function scanl
def test_scanl():
    assert list(scanl(operator.add, ())) == []
    assert list(scanl(operator.add, ())) == []
    assert list(scanl(operator.add, [1, 2, 3, 4], 0)) == [0, 1, 3, 6, 10]
    assert list(scanl(lambda s, x: x + s, ['a', 'b', 'c', 'd'])) == ['a', 'ba', 'cba', 'dcba']



# Generated at 2022-06-13 19:57:32.840749
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(1, 10, 2)
    assert r[0] == 1
    assert r[4] == 9
    assert r[-1] == 9
    assert r[0:3] == [1, 3, 5]
    assert r[3:0:-1] == [7, 5, 3]
    assert r[0:7:2] == [1, 5, 9]
    assert r[7:0:-2] == [9, 5, 1]
    r = Range(0, 10)
    assert r[0:7:2] == [0, 2, 4, 6]
    assert r[7:0:-2] == [8, 6, 4, 2]
    assert r[7:0:-3] == [7, 4, 1]
    r = Range(1, 10, 3)

# Generated at 2022-06-13 19:57:37.228673
# Unit test for method __next__ of class Range
def test_Range___next__():
    assert next(Range(1, 11, 2)) == 1
    assert next(Range(1, 11, 2)) == 3
    assert next(Range(1, 11, 2)) == 5
    assert next(Range(1, 11, 2)) == 7
    assert next(Range(1, 11, 2)) == 9
    assert_raises(StopIteration, next, Range(1, 11, 2))


# Generated at 2022-06-13 19:57:50.598921
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
  r = Range(0, 10)
  assert r[1] == 1, "r[1] == 1"
  assert r[-2] == -2, "r[-2] == -2"
  assert r[1:3] == [1, 2], "r[1:3] == [1, 2]"
  assert r[-2:-4:-1] == [8, 7], "r[-2:-4:-1] == [8, 7]"
  assert r[0:0] == [], "r[0:0] == []"
  assert r[0:0:1] == [], "r[0:0:1] == []"
  assert r[0:0:2] == [], "r[0:0:2] == []"

# Generated at 2022-06-13 19:58:01.599975
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(10)
    assert r[1] == 1
    assert r[-3] == 7
    r = Range(1, 10 + 1)
    assert r[1] == 2
    assert r[-3] == 8
    r = Range(1, 11, 2)
    assert r[1] == 3
    assert r[-3] == 7

# Generated at 2022-06-13 19:58:11.082442
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
	r = Range(1, 10+1)
	assert r[0]==1
	assert r[9]==10
	assert r[-1]==10
	assert r[0:10]==[1,2,3,4,5,6,7,8,9,10]
	assert r[5:10]==[6,7,8,9,10]
	assert r[3::3]==[4,7,10]
	assert r[-2::-2]==[9,7,5,3,1]
	assert r[-2:0:-1]==[9,8,7,6,5,4,3,2]
test_Range___getitem__()


# Generated at 2022-06-13 19:58:22.353413
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    a = Range(5)
    assert [a[i] for i in range(5)] == [0, 1, 2, 3, 4]
    assert a[:] == [0, 1, 2, 3, 4]
    assert a[:3] == [0, 1, 2]
    assert a[:3:2] == [0, 2]
    assert a[2:] == [2, 3, 4]
    assert a[::-1] == [4, 3, 2, 1, 0]
    assert a[2:4] == [2, 3]
    assert a[2:4:-1] == []
    assert a[3:1:-1] == [3, 2]
    assert a[3:0:-1] == [3, 2, 1]

# Generated at 2022-06-13 19:58:28.308004
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(1, 10 + 1)
    assert [r[2], r[4], r[6], r[8]] == [3, 5, 7, 9]
    r = Range(0, 10, 2)
    assert [r[0], r[1], r[2]] == [0, 2, 4]
    assert r[3:] == [6, 8]
    assert r[-3:] == [4, 6, 8]
    assert r[1::2] == [2, 6]


# Generated at 2022-06-13 19:58:36.589212
# Unit test for function drop_until
def test_drop_until():
    d = drop_until(lambda x: x > 5, range(10))
    assert list(d) == [6, 7, 8, 9]
    d = drop_until(lambda x: x > 10, range(10))
    assert list(d) == []
    d = drop_until(lambda x: x > 0, [-10])
    assert list(d) == [-10]
test_drop_until()



# Generated at 2022-06-13 19:58:46.648767
# Unit test for method __next__ of class Range

# Generated at 2022-06-13 19:58:51.767466
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x > 5, range(5))) == []



# Generated at 2022-06-13 19:58:58.026133
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x > 5, [5, 5, 5, 6, 7, 8, 9])) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x > 5, [5, 5, 5])) == []



# Generated at 2022-06-13 19:59:04.029227
# Unit test for method __next__ of class Range
def test_Range___next__():
    # Test for method __next__ of class Range
    assert Raises(StopIteration, lambda: Range(1, 0).__next__())
    assert Range(10, 20).__next__() == 10 and Range(10, 20).__next__() == 11

# Generated at 2022-06-13 19:59:10.884089
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    import random
    r = Range(random.randint(1, 10 ** 6))
    for i in range(10):
        idx = random.randint(0, 1e5)
        assert idx < len(r)
        assert r[idx] == idx
        assert r[idx + len(r)] == idx
        assert r[-idx] == len(r) - 1 - idx
        if idx < len(r) // 2:
            assert r[idx : idx + 5] == range(idx, idx + 5)
        else:
            assert r[idx - 5: idx] == range(idx - 5, idx)
    for i in range(10):
        idx = random.randint(0, 1e5)

# Generated at 2022-06-13 19:59:24.387166
# Unit test for function drop_until
def test_drop_until():
    seq = ["abc", "def", "ghi", "jkl", "mno"]
    fn = lambda x: len(x) > 3
    assert list(drop_until(fn, seq)) == ["jkl", "mno"]



# Generated at 2022-06-13 19:59:27.926868
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]


# Generated at 2022-06-13 19:59:34.967722
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    assert list(Range(10)) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert list(Range(1, 10 + 1)) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert list(Range(1, 11, 2)) == [1, 3, 5, 7, 9]
    for i in range(4):
        for j in range(4):
            for start, end in [(0, 6), (-3, 3), (-3, 0), (0, 0)]:
                lst = list(Range(start, end))
                assert lst[i:j] == lst[slice(i, j)]
    # Test if indexing and slicing is supported

# Generated at 2022-06-13 19:59:39.409094
# Unit test for method __next__ of class Range
def test_Range___next__():
    rng = Range(1, 10 + 1)
    next(rng) == 1
    next(rng) == 2
    next(rng) == 3

    rng = Range(-10, -1)
    next(rng) == -10
    next(rng) == -9
    next(rng) == -8


# Generated at 2022-06-13 19:59:42.945809
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x>5, range(10))) == [6,7,8,9]
    assert list(drop_until(lambda x: x>10, range(10))) == []



# Generated at 2022-06-13 19:59:46.350457
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
test_drop_until()



# Generated at 2022-06-13 19:59:49.124093
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
  r = Range(0,1)
  assert r[0] == 0, "test_Range___getitem__: __getitem__ failed"


import random


# Generated at 2022-06-13 19:59:55.723172
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(5)
    assert r[0] == 0
    assert r[2] == 2
    assert r[-1] == 4
    assert r[:-1] == [0, 1, 2, 3]
    assert r[1:0] == []
    assert r[1:3:2] == [1]
    assert r[::-1] == [4, 3, 2, 1, 0]
    return True


# Generated at 2022-06-13 20:00:02.538351
# Unit test for method __next__ of class Range
def test_Range___next__():
    assert next(Range(0, 10, 2)) == 0
    assert next(Range(0, 10, 2)) == 2
    try:
        next(Range(0, 10, 2))
        next(Range(0, 10, 2))
        next(Range(0, 10, 2))
        assert False
    except StopIteration:
        assert True

# Generated at 2022-06-13 20:00:05.149431
# Unit test for method __next__ of class Range
def test_Range___next__():
    for i in range(1,4):
        r = Range(i, i*1+1, 1)
        n = r.__next__()
        assert n == i, "Unexpected value"

# Generated at 2022-06-13 20:00:19.349326
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x % 3 == 0, range(10))) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert list(drop_until(lambda x: x > 0, range(10))) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert list(drop_until(lambda x: x > 10, range(10))) == []



# Generated at 2022-06-13 20:00:25.874515
# Unit test for function drop_until
def test_drop_until():
    it = iter(range(10))
    assert list(drop_until(lambda x: x > 5, it)) == [6,7,8,9]
    assert list(drop_until(lambda x: x > 5, it)) == []



# Generated at 2022-06-13 20:00:33.306787
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    from hypothesis import given
    from hypothesis.strategies import builds, lists, integers

    @given(lists(integers(min_value=0)))
    def test_equivalence(l):
        assert l == Range(*l)[:]
        assert all(i in Range(*l) for i in l)

    @given(integers(min_value=0), integers(min_value=0), integers(min_value=1))
    def test_no_zero_division(start, stop, step):
        Range(start, stop, step)

    @given(integers(min_value=0), integers(min_value=0), integers(min_value=1))
    def test_length(start, stop, step):
        assert len(Range(start, stop, step)) == (stop - start) // step


# Generated at 2022-06-13 20:00:36.600010
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    Range(10)[3] == 3
    Range(10)[-1] == 9
    Range(10)[0: 2] == [0, 1]


# Generated at 2022-06-13 20:00:40.069162
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    x=Range(1, 5+1)
    print(x[0], x[2], x[4])
if __name__ == "__main__":
    test_Range___getitem__()

# Generated at 2022-06-13 20:00:45.208343
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(10)
    assert r[0] == 0
    assert r[3] == 3

    r = Range(1, 10 + 1)
    assert r[0] == 1
    assert r[-1] == 10

    r = Range(1, 11, 2)
    assert r[0] == 1
    assert r[2] == 5
    assert r[-1] == 9



# Generated at 2022-06-13 20:00:50.122671
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x == 1, [1, 2, 3])) == [1, 2, 3]
    assert list(drop_until(lambda x: x == 1, [])) == []
    assert list(drop_until(lambda x: x == 1, [0, 0, 0, 1, 2])) == [1, 2]



# Generated at 2022-06-13 20:00:58.393614
# Unit test for method __next__ of class Range
def test_Range___next__():
    assert next(Range(1)) == 0
    assert next(Range(1, 3 + 1)) == 1
    assert next(Range(1, 4 + 1, 2)) == 1
    with raises(StopIteration):
        next(Range(1))
    with raises(StopIteration):
        next(Range(1, 3 + 1))
    with raises(StopIteration):
        next(Range(1, 4 + 1, 2))
    assert next(Range(1)) == 0
    assert next(Range(1, 3 + 1)) == 1
    assert next(Range(1, 4 + 1, 2)) == 1

# Generated at 2022-06-13 20:01:05.536747
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(1, 10 + 1)
    assert r[0] == 1
    assert r[2] == 3
    assert r[4] == 5
    assert r[-1] == 10
    assert r[-2] == 9
    assert r[::2] == [1, 3, 5, 7, 9]
    assert r[1::2] == [2, 4, 6, 8, 10]
    assert r[1:-1:2] == [2, 4, 6, 8]
    assert r[10:15] == []
    assert r[10:10:1] == []
    with pytest.raises(IndexError):
        assert r[-11]
    with pytest.raises(IndexError):
        assert r[11]



# Generated at 2022-06-13 20:01:07.809915
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x < 0, range(10))) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert list(drop_until(lambda x: x > 0, range(10))) == []
    assert list(drop_until(lambda x: x > 10, range(10))) == []

test_drop_until()



# Generated at 2022-06-13 20:01:30.465402
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    def assert_getitem(rng, i, expected):
        if isinstance(i, int):
            res = rng[i]
            assert res == expected
        else:
            res = rng[i.start:i.stop:i.step]
            assert res == expected

    assert_getitem(Range(10), 0, 0)
    assert_getitem(Range(10), 1, 1)
    assert_getitem(Range(10), -1, 9)
    assert_getitem(Range(10), -2, 8)
    assert_getitem(Range(10), 9, 9)
    assert_getitem(Range(10), 10, IndexError)
    assert_getitem(Range(10), -10, IndexError)

# Generated at 2022-06-13 20:01:37.698334
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(1, 4)
    assert type(r[0]) == int
    assert type(r[:2]) == list
    assert r[0] == 1
    assert r[0:2] == [1, 2]
    r = Range(0, 10, 2)
    assert type(r[0]) == int
    assert type(r[:2]) == list
    assert r[0] == 0
    assert r[0:2] == [0, 2]


# Generated at 2022-06-13 20:01:48.487918
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    print(list(Range(10))[:])
    print(list(Range(10))[0])
    print(list(Range(10))[5])
    print(list(Range(10))[9])
    print(list(Range(10))[:2])
    print(list(Range(10))[:10])
    print(list(Range(10))[2:])
    print(list(Range(10))[2:8])
    print(list(Range(10))[2:10])
    print(list(Range(10))[:2:2])
    print(list(Range(10))[2::2])
    print(list(Range(10))[:10:2])
    print(list(Range(10))[2:8:2])

# Generated at 2022-06-13 20:02:02.485374
# Unit test for function drop_until
def test_drop_until():
    # Iterable is empty
    assert list(drop_until(lambda x: x>0, [])) == []
    # All elements satisfy
    assert list(drop_until(lambda x: x>0, [1,2,3,4])) == [1,2,3,4]
    # None satisfies
    assert list(drop_until(lambda x: x>0, [0,0,0,0])) == []
    # The first element satisfies
    assert list(drop_until(lambda x: x>1, [2,3,4,5,6])) == [2,3,4,5,6]
    # The last element satisfies
    assert list(drop_until(lambda x: x>1, [0,0,0,0,2])) == [2]
    # Elements in the middle satisfy
    assert list