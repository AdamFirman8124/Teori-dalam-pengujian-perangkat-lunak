

# Generated at 2022-06-14 06:25:13.251922
# Unit test for function join_each
def test_join_each():
    p = '/tmp'
    paths = ['foo', 'bar', 'baz']
    result = list(join_each(p, paths))
    assert result == [
        '/tmp/foo',
        '/tmp/bar',
        '/tmp/baz',
    ]

# Generated at 2022-06-14 06:25:21.178114
# Unit test for function join_each
def test_join_each():
    # Test that join_each join with parent and non-empty iterable
    parent = "parent"
    iterable = ["child1", "child2"]
    join_result = join_each(parent, iterable)
    assert join_result.__next__() == os.path.join(parent, iterable[0])
    assert join_result.__next__() == os.path.join(parent, iterable[1])
    # Test that join_each joins with parent and empty iterable
    join_result = join_each(parent, [])
    with pytest.raises(StopIteration):
        join_result.__next__()

# Generated at 2022-06-14 06:25:27.424269
# Unit test for function join_each
def test_join_each():
    import tempfile
    d = tempfile.mkdtemp()
    expected = [os.path.join(d, p) for p in ['one', 'two', 'three']]
    assert(list(join_each(d, ['one', 'two', 'three'])) == expected)



# Generated at 2022-06-14 06:25:31.380690
# Unit test for function join_each
def test_join_each():
    parent = 'path/to'
    iterable = ['foo', 'bar', 'baz']
    joined = list(join_each(parent, iterable))
    assert joined == ['path/to/foo', 'path/to/bar', 'path/to/baz']



# Generated at 2022-06-14 06:25:38.083375
# Unit test for function join_each
def test_join_each():
    parent = ".."
    iterable = ["file1", "file2", "file3"]
    output = list(join_each(parent, iterable))
    assert output == [os.path.abspath('../file1'), os.path.abspath('../file2'), os.path.abspath('../file3')]



# Generated at 2022-06-14 06:25:41.767072
# Unit test for function join_each
def test_join_each():
    assert list(join_each("/home/test", ["file1", "file2"])) == [
        "/home/test/file1",
        "/home/test/file2",
    ]



# Generated at 2022-06-14 06:25:44.874129
# Unit test for function join_each
def test_join_each():
    assert list(join_each('/a/b', ['c', 'd'])) == ['/a/b/c', '/a/b/d']



# Generated at 2022-06-14 06:25:48.697898
# Unit test for function join_each
def test_join_each():
    assert list(join_each('/tmp', [
        'a',
        'b'
    ])) == [
        '/tmp/a',
        '/tmp/b'
    ]



# Generated at 2022-06-14 06:25:51.805756
# Unit test for function join_each
def test_join_each():
    assert list(join_each('', ['a', 'b'])) == ['a', 'b']
    assert list(join_each('foo', ['a', 'b'])) == ['foo/a', 'foo/b']

# Generated at 2022-06-14 06:25:57.556469
# Unit test for function join_each
def test_join_each():
    parent = 'parent'
    iterable = ['a', 'b', 'c']
    expected = ['parent/a', 'parent/b', 'parent/c']
    actual = list(join_each(parent, iterable))
    assert actual == expected