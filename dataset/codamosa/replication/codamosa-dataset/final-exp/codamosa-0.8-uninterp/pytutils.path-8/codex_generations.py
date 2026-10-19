

# Generated at 2022-06-14 06:25:14.694185
# Unit test for function join_each
def test_join_each():
    parent = 'test'
    iterable = ['a', 'b', 'c']

    result = join_each(parent, iterable)
    expected_result = [
        os.path.join(parent, 'a'),
        os.path.join(parent, 'b'),
        os.path.join(parent, 'c')
    ]
    assert list(result) == expected_result



# Generated at 2022-06-14 06:25:20.547951
# Unit test for function join_each
def test_join_each():
    # Test an iterator that is empty
    assert list(join_each('/', [])) == []

    # Test an iterator with one element
    assert list(join_each('/', ['/'])) == ['/']

    # Test an iterator that is not empty
    assert list(join_each('/', ['a', 'b', 'c'])) == [
        '/', '/a', '/a/b', '/a/b/c']
    pass


# Reversing the split function

# Generated at 2022-06-14 06:25:23.959267
# Unit test for function join_each
def test_join_each():
    assert list(join_each('/home', ['local', 'user'])) == ['/home/local', '/home/user']



# Generated at 2022-06-14 06:25:29.062683
# Unit test for function join_each
def test_join_each():
    result = join_each("/Users", ["apple", "google"])
    assert next(result) == '/Users/apple'
    assert next(result) == '/Users/google'
    try:
        next(result)
        assert False
    except StopIteration:
        assert True

# Generated at 2022-06-14 06:25:34.498777
# Unit test for function join_each
def test_join_each():
    file_name = "file.txt"
    temp_dir = tempfile.gettempdir()
    file_paths = join_each(temp_dir, (file_name, os.pardir, "..", file_name))
    for fp in file_paths:
        assert os.path.isfile(fp) is True
        assert os.path.basename(fp) == file_name

# Generated at 2022-06-14 06:25:39.014190
# Unit test for function join_each
def test_join_each():
    assert list(join_each('/foo', ['/bar'])) == ['/foo/bar']
    assert list(join_each('/foo', ['/bar', 'baz'])) == ['/foo/bar', '/foo/baz']



# Generated at 2022-06-14 06:25:42.197873
# Unit test for function join_each
def test_join_each():
    assert ['a/b', 'a/c', 'a/d'] == list(join_each('a', ['b', 'c', 'd']))



# Generated at 2022-06-14 06:25:45.311945
# Unit test for function join_each
def test_join_each():
    assert [os.path.join('foo', 'bar'),
            os.path.join('foo', 'baz')] == list(join_each('foo', ['bar', 'baz']))


#--------------------------------------------------------------------------
# Tests utils.py
#--------------------------------------------------------------------------


# Generated at 2022-06-14 06:25:50.423294
# Unit test for function join_each
def test_join_each():
    print('Test join_each')
    assert list(join_each('/', [])) == []
    assert list(join_each('/', ['a', 'b', 'c'])) == ['/a', '/b', '/c']


if __name__ == '__main__':
    test_join_each()

# Generated at 2022-06-14 06:25:54.408047
# Unit test for function join_each
def test_join_each():
    # One item
    assert list(join_each("parent", ["child"])) == ["parent/child"]

    # Two items
    assert list(join_each("parent", ["child1", "child2"])) == [
        "parent/child1", "parent/child2",
    ]