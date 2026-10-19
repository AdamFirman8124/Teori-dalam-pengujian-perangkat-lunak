

# Generated at 2022-06-14 06:25:11.681759
# Unit test for function join_each
def test_join_each():
    assert list(join_each("a", ["b", "c"])) == ["a/b", "a/c"]
    assert list(join_each("a", [])) == []



# Generated at 2022-06-14 06:25:16.506370
# Unit test for function join_each
def test_join_each():
    assert list(join_each("/tmp", ["foo", "bar", "baz"])) == [
        '/tmp/foo',
        '/tmp/bar',
        '/tmp/baz',
    ]
    assert list(join_each("/tmp", [])) == [
    ]

# Generated at 2022-06-14 06:25:25.903747
# Unit test for function join_each
def test_join_each():
    parent = '/dir'
    items = ['a', 'b', 'c']
    expected = [os.path.join(parent, item) for item in items]
    assert list(join_each(parent, items)) == expected


if __name__ == '__main__':
    import sys
    import nose

    module_name = sys.modules[__name__].__file__

    result = nose.run(argv=[sys.argv[0],
                            module_name,
                            '-s', '-v'])

# Generated at 2022-06-14 06:25:32.494779
# Unit test for function join_each
def test_join_each():
    # default path separator is '/'
    assert list(join_each('/tmp', ['a', 'b', 'c'])) == ['/tmp/a',
                                                        '/tmp/b',
                                                        '/tmp/c']
    assert list(join_each('\\tmp', ['a', 'b', 'c'])) == ['\\tmp\\a',
                                                         '\\tmp\\b',
                                                         '\\tmp\\c']



# Generated at 2022-06-14 06:25:43.293245
# Unit test for function join_each
def test_join_each():
    photo_dir = '~/Pictures'

    # Test with a list
    assert list(join_each(photo_dir, ['a.jpg', 'b.png'])) == [
        '~/Pictures/a.jpg',
        '~/Pictures/b.png'
    ]

    # Test with a generator expression

# Generated at 2022-06-14 06:25:48.912164
# Unit test for function join_each
def test_join_each():
    assert list(join_each('/tmp', ['a', 'b', 'c'])) == ['/tmp/a', '/tmp/b', '/tmp/c']
    assert list(join_each('/tmp', [])) == []



# Generated at 2022-06-14 06:25:58.501613
# Unit test for function join_each
def test_join_each():
    # Can we iterate over all the elements?
    '''
    assert list(join_each("foo/bar/baz.py", ["baz.py", "foo.py", "bam.py", "bar.py"])) == [
        "foo/bar/baz.py/baz.py",
        "foo/bar/baz.py/foo.py",
        "foo/bar/baz.py/bam.py",
        "foo/bar/baz.py/bar.py",
    ]
    '''
    # Can we iterate over all the elements?

# Generated at 2022-06-14 06:26:02.287381
# Unit test for function join_each
def test_join_each():
    assert list(join_each('a', ['b', 'c' 'd'])) == ['a/b', 'a/c', 'a/d']
    assert list(join_each('a', [])) == []



# Generated at 2022-06-14 06:26:07.932436
# Unit test for function join_each
def test_join_each():
    parent = os.path.join('a', 'b', 'c')
    iterable = ['d', 'e', 'f']
    assert list(join_each(parent, iterable)) == [os.path.join(parent, i) for i in iterable]


# This function is to replace the os.walk function
# os.walk does not necessarily return the files in sorted order

# Generated at 2022-06-14 06:26:19.822305
# Unit test for function join_each
def test_join_each():
    parent_path = r"C:\path\to"
    sub_paths = ["path", "to", "file.txt"]
    expected = [r"C:\path\to\path", r"C:\path\to\to", r"C:\path\to\file.txt"]

    actual = list(join_each(parent_path, sub_paths))

    assert expected == actual, "join_each returns unexpected result."