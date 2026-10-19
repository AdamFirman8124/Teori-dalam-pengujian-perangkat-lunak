

# Generated at 2024-06-01 18:50:55.856360
# Unit test for function drop_until
def test_drop_until():    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]

# Generated at 2024-06-01 18:50:58.888277
# Unit test for method __iter__ of class LazyList
def test_LazyList___iter__():    data = range(10)

# Generated at 2024-06-01 18:51:02.328088
# Unit test for function split_by
def test_split_by():    assert list(split_by(range(10), criterion=lambda x: x % 3 == 0)) == [[1, 2], [4, 5], [7, 8]]

# Generated at 2024-06-01 18:51:05.227936
# Unit test for method __next__ of class Range
def test_Range___next__():    r = Range(1, 10, 2)

# Generated at 2024-06-01 18:51:07.775268
# Unit test for function drop_until
def test_drop_until():    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]

# Generated at 2024-06-01 18:51:10.381624
# Unit test for function drop_until
def test_drop_until():    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]

# Generated at 2024-06-01 18:51:15.311682
# Unit test for function drop_until
def test_drop_until():    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]

# Generated at 2024-06-01 18:51:17.419371
# Unit test for function take
def test_take():    assert list(take(5, range(10))) == [0, 1, 2, 3, 4]

# Generated at 2024-06-01 18:51:19.974799
# Unit test for function drop
def test_drop():    assert list(drop(3, [1, 2, 3, 4, 5])) == [4, 5]

# Generated at 2024-06-01 18:51:21.625809
# Unit test for method __len__ of class LazyList
def test_LazyList___len__():    # Test with a finite iterable
    ll = LazyList(range(5))
    assert len(ll) == 5

    # Test with an empty iterable
    ll = LazyList(iter([]))
    assert len(ll) == 0

    # Test with an infinite iterable
    import itertools
    ll = LazyList(itertools.count())
    try:
        len(ll)
        assert False, "Expected TypeError"
    except TypeError:
        pass


# Generated at 2024-06-01 18:51:36.678055
# Unit test for method __len__ of class LazyList
def test_LazyList___len__():    # Test with an iterable that has a known length
    lazy_list = LazyList(range(10))
    try:
        len(lazy_list)
    except TypeError as e:
        assert str(e) == "__len__ is not available before the iterable is depleted"
    list(lazy_list)  # Exhaust the iterable
    assert len(lazy_list) == 10

    # Test with an empty iterable
    lazy_list = LazyList(iter([]))
    try:
        len(lazy_list)
    except TypeError as e:
        assert str(e) == "__len__ is not available before the iterable is depleted"
    list(lazy_list)  # Exhaust the iterable
    assert len(lazy_list) == 0

    # Test with a large iterable
    lazy_list = LazyList(range(1000))

# Generated at 2024-06-01 18:51:40.756018
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():    data = range(10)

# Generated at 2024-06-01 18:51:43.608171
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():    lst = [1, 2, 3, 4, 5]

# Generated at 2024-06-01 18:51:46.472652
# Unit test for method __len__ of class LazyList
def test_LazyList___len__():    # Test with a finite iterable
    lazy_list = LazyList(range(5))
    assert len(lazy_list) == 5

    # Test with an empty iterable
    lazy_list = LazyList(iter([]))
    assert len(lazy_list) == 0

    # Test with an infinite iterable
    import itertools
    lazy_list = LazyList(itertools.count())
    try:
        len(lazy_list)
    except TypeError as e:
        assert str(e) == "__len__ is not available before the iterable is depleted"


# Generated at 2024-06-01 18:51:47.590416
# Unit test for method __iter__ of class LazyList
def test_LazyList___iter__():    data = range(10)

# Generated at 2024-06-01 18:51:52.343774
# Unit test for function split_by
def test_split_by():    assert list(split_by(range(10), criterion=lambda x: x % 3 == 0)) == [[1, 2], [4, 5], [7, 8]]

# Generated at 2024-06-01 18:51:56.496598
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():    lst = [1, 2, 3, 4, 5]

# Generated at 2024-06-01 18:51:59.916423
# Unit test for method __len__ of class LazyList
def test_LazyList___len__():    # Test with a finite iterable
    lazy_list = LazyList(range(5))
    with pytest.raises(TypeError):
        len(lazy_list)
    list(lazy_list)  # Exhaust the iterable
    assert len(lazy_list) == 5

    # Test with an empty iterable
    lazy_list = LazyList(iter([]))
    with pytest.raises(TypeError):
        len(lazy_list)
    list(lazy_list)  # Exhaust the iterable
    assert len(lazy_list) == 0

    # Test with an infinite iterable
    def infinite_iter():
        i = 0
        while True:
            yield i
            i += 1

    lazy_list = LazyList(infinite_iter())
    with pytest.raises(TypeError):
        len(lazy_list)
    for _ in range(100):  # Partially exhaust the iterable
        next(iter(lazy_list))

# Generated at 2024-06-01 18:52:02.974676
# Unit test for function drop_until
def test_drop_until():    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]

# Generated at 2024-06-01 18:52:06.240894
# Unit test for function drop_until
def test_drop_until():    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]

# Generated at 2024-06-01 18:52:16.382608
# Unit test for function chunk
def test_chunk():    assert list(chunk(3, range(10))) == [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]

# Generated at 2024-06-01 18:52:19.844015
# Unit test for function split_by
def test_split_by():    assert list(split_by(range(10), criterion=lambda x: x % 3 == 0)) == [[1, 2], [4, 5], [7, 8]]

# Generated at 2024-06-01 18:52:23.286952
# Unit test for function split_by
def test_split_by():    assert list(split_by(range(10), criterion=lambda x: x % 3 == 0)) == [[1, 2], [4, 5], [7, 8]]

# Generated at 2024-06-01 18:52:26.149657
# Unit test for function split_by
def test_split_by():    assert list(split_by(range(10), criterion=lambda x: x % 3 == 0)) == [[1, 2], [4, 5], [7, 8]]

# Generated at 2024-06-01 18:52:29.025057
# Unit test for function split_by
def test_split_by():    # Test case 1: Split by criterion
    result = list(split_by(range(10), criterion=lambda x: x % 3 == 0))
    assert result == [[1, 2], [4, 5], [7, 8]], f"Unexpected result: {result}"

    # Test case 2: Split by separator
    result = list(split_by(" Split by: ", separator=' '))
    assert result == [['S', 'p', 'l', 'i', 't'], ['b', 'y', ':']], f"Unexpected result: {result}"

    # Test case 3: Split by separator with empty segments
    result = list(split_by(" Split by: ", empty_segments=True, separator=' '))
    assert result == [[], ['S', 'p', 'l', 'i', 't'], ['b', 'y', ':'], []], f"Unexpected result: {result}"

    # Test

# Generated at 2024-06-01 18:52:32.063579
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():    lazy_list = LazyList(range(10))

# Generated at 2024-06-01 18:52:35.907828
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():    r = Range(1, 10, 2)

# Generated at 2024-06-01 18:52:39.236496
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():    lst = [1, 2, 3, 4, 5]

# Generated at 2024-06-01 18:52:41.914549
# Unit test for function drop_until
def test_drop_until():    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]

# Generated at 2024-06-01 18:52:44.176965
# Unit test for function drop_until
def test_drop_until():    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]

# Generated at 2024-06-01 18:52:53.271285
# Unit test for function split_by
def test_split_by():    assert list(split_by(range(10), criterion=lambda x: x % 3 == 0)) == [[1, 2], [4, 5], [7, 8]]

# Generated at 2024-06-01 18:52:56.224130
# Unit test for function drop_until
def test_drop_until():    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]

# Generated at 2024-06-01 18:52:59.478560
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():    r = Range(1, 10, 2)

# Generated at 2024-06-01 18:53:05.365635
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():    r = Range(1, 11, 2)

# Generated at 2024-06-01 18:53:08.789937
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():    lst = [1, 2, 3, 4, 5]

# Generated at 2024-06-01 18:53:12.251651
# Unit test for function split_by
def test_split_by():    assert list(split_by(range(10), criterion=lambda x: x % 3 == 0)) == [[1, 2], [4, 5], [7, 8]]

# Generated at 2024-06-01 18:53:16.374489
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():    lst = [1, 2, 3, 4, 5]

# Generated at 2024-06-01 18:53:19.346264
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():    data = range(10)

# Generated at 2024-06-01 18:53:22.680376
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():    r = Range(1, 10, 2)

# Generated at 2024-06-01 18:53:25.791150
# Unit test for function split_by
def test_split_by():    assert list(split_by(range(10), criterion=lambda x: x % 3 == 0)) == [[1, 2], [4, 5], [7, 8]]

# Generated at 2024-06-01 18:53:39.238776
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():    lazy_list = LazyList(range(10))

# Generated at 2024-06-01 18:53:43.202543
# Unit test for function split_by
def test_split_by():    assert list(split_by(range(10), criterion=lambda x: x % 3 == 0)) == [[1, 2], [4, 5], [7, 8]]

# Generated at 2024-06-01 18:53:45.900064
# Unit test for function split_by
def test_split_by():    assert list(split_by(range(10), criterion=lambda x: x % 3 == 0)) == [[1, 2], [4, 5], [7, 8]]

# Generated at 2024-06-01 18:53:49.310412
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():    r = Range(1, 10, 2)

# Generated at 2024-06-01 18:53:52.497213
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():    r = Range(1, 10, 2)

# Generated at 2024-06-01 18:53:56.654575
# Unit test for function drop_until
def test_drop_until():    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]

# Generated at 2024-06-01 18:54:02.466130
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():    lst = [1, 2, 3, 4, 5]

# Generated at 2024-06-01 18:54:05.120720
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():    lst = [1, 2, 3, 4, 5]

# Generated at 2024-06-01 18:54:08.168147
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():    r = Range(1, 10, 2)

# Generated at 2024-06-01 18:54:11.581503
# Unit test for function scanl
def test_scanl():    assert list(scanl(lambda x, y: x + y, [1, 2, 3, 4], 0)) == [0, 1, 3, 6, 10]

# Generated at 2024-06-01 18:54:48.602719
# Unit test for function split_by
def test_split_by():    assert list(split_by(range(10), criterion=lambda x: x % 3 == 0)) == [[1, 2], [4, 5], [7, 8]]

# Generated at 2024-06-01 18:54:50.732649
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():    lazy_list = LazyList(range(10))

# Generated at 2024-06-01 18:54:53.911414
# Unit test for function drop_until
def test_drop_until():    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]

# Generated at 2024-06-01 18:54:57.101210
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():    r = Range(1, 10, 2)

# Generated at 2024-06-01 18:54:59.973489
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():    lazy_list = LazyList(range(10))

# Generated at 2024-06-01 18:55:02.941355
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():    r = Range(1, 10, 2)

# Generated at 2024-06-01 18:55:05.975126
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():    r = Range(1, 10, 2)

# Generated at 2024-06-01 18:55:09.850816
# Unit test for function split_by
def test_split_by():    assert list(split_by(range(10), criterion=lambda x: x % 3 == 0)) == [[1, 2], [4, 5], [7, 8]]

# Generated at 2024-06-01 18:55:13.874750
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():    data = range(10)

# Generated at 2024-06-01 18:55:16.850907
# Unit test for function drop_until
def test_drop_until():    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]

# Generated at 2024-06-01 18:56:03.008042
# Unit test for function drop_until
def test_drop_until():    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]

# Generated at 2024-06-01 18:56:07.966679
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():    data = range(10)

# Generated at 2024-06-01 18:56:10.579206
# Unit test for function drop_until
def test_drop_until():    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]

# Generated at 2024-06-01 18:56:13.899509
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():    lst = [1, 2, 3, 4, 5]

# Generated at 2024-06-01 18:56:17.658364
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():    lazy_list = LazyList(range(10))

# Generated at 2024-06-01 18:56:20.712784
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():    lazy_list = LazyList(range(10))

# Generated at 2024-06-01 18:56:24.188592
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():    r = Range(1, 10, 2)

# Generated at 2024-06-01 18:56:27.796013
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():    r = Range(1, 10, 2)

# Generated at 2024-06-01 18:56:29.967454
# Unit test for function drop_until
def test_drop_until():    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]

# Generated at 2024-06-01 18:56:33.304193
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():    r = Range(1, 10, 2)

# Generated at 2024-06-01 18:58:10.811050
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():    lst = [1, 2, 3, 4, 5]

# Generated at 2024-06-01 18:58:13.705024
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():    lst = [1, 2, 3, 4, 5]

# Generated at 2024-06-01 18:58:15.875793
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():    lazy_list = LazyList(range(10))

# Generated at 2024-06-01 18:58:19.225542
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():    lst = [1, 2, 3, 4, 5]

# Generated at 2024-06-01 18:58:22.402531
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():    lst = [1, 2, 3, 4, 5]

# Generated at 2024-06-01 18:58:26.120848
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():    lst = [1, 2, 3, 4, 5]

# Generated at 2024-06-01 18:58:29.264131
# Unit test for function drop_until
def test_drop_until():    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]

# Generated at 2024-06-01 18:58:31.916738
# Unit test for function drop_until
def test_drop_until():    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]

# Generated at 2024-06-01 18:58:35.294582
# Unit test for function drop_until
def test_drop_until():    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]

# Generated at 2024-06-01 18:58:38.842478
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():    r = Range(1, 10, 2)