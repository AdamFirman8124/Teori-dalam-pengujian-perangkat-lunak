

# Generated at 2022-06-14 06:25:12.748192
# Unit test for function join_each
def test_join_each():
    assert os.path.join('a', 'b') == next(join_each('a', ['b']))
    assert [os.path.join('a', 'b'), os.path.join('a', 'c')] == list(join_each('a', ['b', 'c']))

# Generated at 2022-06-14 06:25:15.033949
# Unit test for function join_each
def test_join_each():
    assert tuple(join_each("foo", ("bar", "baz"))) == ("foo/bar", "foo/baz")

# Generated at 2022-06-14 06:25:23.170209
# Unit test for function join_each
def test_join_each():
    assert list(join_each('C:\\temp', 'abc')) == ['C:\\temp\\a', 'C:\\temp\\b', 'C:\\temp\\c']
    assert list(join_each('/home/temp', 'abc')) == ['/home/temp/a', '/home/temp/b', '/home/temp/c']
    assert list(join_each('C:\\temp', ['a', 'b', 'c'])) == ['C:\\temp\\a', 'C:\\temp\\b', 'C:\\temp\\c']
    assert list(join_each('/home/temp', ['a', 'b', 'c'])) == ['/home/temp/a', '/home/temp/b', '/home/temp/c']


if __name__ == '__main__':
    test_join_each()

# Generated at 2022-06-14 06:25:30.014926
# Unit test for function join_each
def test_join_each():
    paths = [
        ['parent', 'child'],
        ['parent', 'child2', 'child'],
        ['parent', 'child3', 'child', 'child'],
    ]
    joined = [os.path.join(*p) for p in paths]
    assert list(join_each('parent', ['child', 'child2/child', 'child3/child/child'])) == joined



# Generated at 2022-06-14 06:25:33.236368
# Unit test for function join_each
def test_join_each():
    assert list(join_each('/', ('a', 'b'))) == ['/a', '/b']



# Generated at 2022-06-14 06:25:36.045669
# Unit test for function join_each
def test_join_each():
    assert tuple(join_each("/", ["usr", "local", "bin"])) == ("/usr", "/local", "/bin")



# Generated at 2022-06-14 06:25:40.427443
# Unit test for function join_each
def test_join_each():
    assert [(os.path.join('abc', 'cde'), 'efg')] == list(join_each('abc', ['cde', 'efg']))


# Return the number of hours since Jan 1st, 1970 (UNIX time)

# Generated at 2022-06-14 06:25:47.307579
# Unit test for function join_each
def test_join_each():
    files = ["file1.txt", "file2.txt", "file3.txt"]
    parent = "hello"
    files_joined = list(join_each(parent, files))
    expected_files_joined = ["hello/file1.txt", "hello/file2.txt",
                             "hello/file3.txt"]
    assert files_joined == expected_files_joined


# Creates a list of the files in the working directory
# that are not in the .git directory

# Generated at 2022-06-14 06:25:50.149630
# Unit test for function join_each
def test_join_each():
    assert list(join_each('/tmp', ['file1', 'file2'])) == [
        '/tmp/file1', '/tmp/file2']

# Generated at 2022-06-14 06:25:55.745631
# Unit test for function join_each
def test_join_each():
    a = join_each(".", ["a", "b", "c"])
    for n in a:
        print(n)


if __name__ == '__main__':
    # test_join_each()
    pass