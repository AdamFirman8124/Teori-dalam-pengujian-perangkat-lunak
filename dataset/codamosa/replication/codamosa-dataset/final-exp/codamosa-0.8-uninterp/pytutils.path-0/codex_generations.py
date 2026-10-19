

# Generated at 2022-06-14 06:25:09.491678
# Unit test for function join_each
def test_join_each():
    parent = 'test'
    iterable = ['test1', 'test2', 'test4']

    for i in join_each(parent, iterable):
        assert isinstance(i, str)



# Generated at 2022-06-14 06:25:13.076622
# Unit test for function join_each
def test_join_each():
    assert list(join_each('/', ['a', 'b'])) == ['/a', '/b']
    assert list(join_each('/x', ['a', 'b'])) == ['/x/a', '/x/b']



# Generated at 2022-06-14 06:25:19.930338
# Unit test for function join_each
def test_join_each():
    tests = [
        {
            'parent': '/a/b/c',
            'iterable': ['/d/e/f', '/g/h/i'],
            'expected': ['/a/b/c/d/e/f', '/a/b/c/g/h/i']
        },
    ]

    for test in tests:
        actual = list(join_each(test['parent'], test['iterable']))
        assert actual == test['expected']



# Generated at 2022-06-14 06:25:23.215157
# Unit test for function join_each
def test_join_each():
    assert list(join_each("/a", ("b", "c"))) == ["/a/b", "/a/c"]



# Generated at 2022-06-14 06:25:26.245276
# Unit test for function join_each
def test_join_each():
    assert(list(join_each("/", ["tmp", "foo", "bar"])) == ["/tmp", "/foo", "/bar"])


# Create the path for a file using the temporary directory

# Generated at 2022-06-14 06:25:29.430581
# Unit test for function join_each
def test_join_each():
    assert list(join_each('foo', ['bar', 'baz'])) == ['foo/bar', 'foo/baz']



# Generated at 2022-06-14 06:25:33.059173
# Unit test for function join_each
def test_join_each():
    parent_dir = '/some'
    iterable = ('dir', 'directory', 'dirs')

    real = [
        os.path.join(parent_dir, child_dir)
        for child_dir in iterable
    ]

    

# Generated at 2022-06-14 06:25:37.547262
# Unit test for function join_each
def test_join_each():
    assert tuple(join_each('a/b/c', ('d', 'e', 'f'))) == ('a/b/c/d', 'a/b/c/e', 'a/b/c/f')



# Generated at 2022-06-14 06:25:45.044012
# Unit test for function join_each
def test_join_each():
    assert tuple(join_each("/", ("a", "b", "c"))) == ("/a", "/b", "/c")
    assert tuple(join_each("/a", ("b", "c"))) == ("/a/b", "/a/c")
    assert tuple(join_each("/a/b", ("c",))) == ("/a/b/c",)
    assert tuple(join_each("/a/b/c", ())) == ()



# Generated at 2022-06-14 06:25:49.737147
# Unit test for function join_each
def test_join_each():
    parent = 'parent'
    iterable = ('a', 'b', 'c')

    expected_results = ('parent/a', 'parent/b', 'parent/c')

    result = tuple(join_each(parent, iterable))

    assert result == expected_results

