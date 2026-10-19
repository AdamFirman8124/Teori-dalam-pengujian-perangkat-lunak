

# Generated at 2022-06-14 06:25:06.375553
# Unit test for function join_each
def test_join_each():
    a = [1, 2, 3]
    result = list(join_each("", a))
    assert result == ["1", "2", "3"]



# Generated at 2022-06-14 06:25:12.370279
# Unit test for function join_each
def test_join_each():
    assert list(join_each('/home/user', ['foo', 'bar'])) == ['/home/user/foo', '/home/user/bar']
    assert list(join_each('foo', ['bar', 'baz'])) == ['foo/bar', 'foo/baz']



# Generated at 2022-06-14 06:25:21.996695
# Unit test for function join_each
def test_join_each():
    from nose.tools import assert_equal
    # Note that __file__ is the path to the file with the tests
    # __file__ = tests/test_sample
    # __name__ = tests.test_sample
    # os.path.dirname(__file__) = tests
    # os.path.dirname(os.path.dirname(__file__)) = current directory
    # os.path.dirname(os.path.dirname(os.path.dirname(__file__))) = parent directory

# Generated at 2022-06-14 06:25:25.942818
# Unit test for function join_each
def test_join_each():
    dir = os.getcwd()
    assert os.path.join(dir, "src") in join_each(dir, ["src", "test"])
    assert os.path.join(dir, "test") in join_each(dir, ["src", "test"])



# Generated at 2022-06-14 06:25:31.104295
# Unit test for function join_each
def test_join_each():
    parent = '/a/b/c'
    iterable = ('d/e', 'e/f/g')
    expected = ('/a/b/c/d/e', '/a/b/c/e/f/g')
    assert list(join_each(parent, iterable)) == expected

# Generated at 2022-06-14 06:25:36.646355
# Unit test for function join_each
def test_join_each():
    assert list(join_each('/home/user/', ['somedir', 'anotherdir', 'test.txt'])) == [
        '/home/user/somedir',
        '/home/user/anotherdir',
        '/home/user/test.txt'
    ]



# Generated at 2022-06-14 06:25:39.997031
# Unit test for function join_each
def test_join_each():
    assert list(join_each("foo", ["bar", "baz"])) == [
        "foo/bar",
        "foo/baz",
    ]



# Generated at 2022-06-14 06:25:47.342710
# Unit test for function join_each
def test_join_each():
    iterable = join_each('test/testfolder', ['test1/test.txt', 'test2/test2.txt'])
    unit_test_asserts = []
    # Test
    for file_path in iterable:
        file_name = file_path.replace(os.path.sep, '_')
        unit_test_asserts.append(os.path.exists(os.path.join('test', 'testfolder', file_name)))

    assert all(unit_test_asserts)

# Generated at 2022-06-14 06:25:50.579841
# Unit test for function join_each
def test_join_each():
    assert list(join_each('a', ['b', 'c', 'd'])) == ['a/b', 'a/c', 'a/d']



# Generated at 2022-06-14 06:25:54.735096
# Unit test for function join_each
def test_join_each():
    assert list(join_each('a', ['b', 'c'])) == ['a/b', 'a/c']

