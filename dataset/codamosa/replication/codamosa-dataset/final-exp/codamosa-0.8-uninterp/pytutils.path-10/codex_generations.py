

# Generated at 2022-06-14 06:25:13.001959
# Unit test for function join_each
def test_join_each():
    parent = '/etc'
    iterable = ('resolv.conf', 'passwd', 'shadow')
    result = tuple(join_each(parent, iterable))
    expected = ('/etc/resolv.conf', '/etc/passwd', '/etc/shadow')
    assert result == expected



# Generated at 2022-06-14 06:25:17.330922
# Unit test for function join_each
def test_join_each():
    assert list(join_each('example', ['file1', 'file2', 'file3'])) ==\
        ['example/file1', 'example/file2', 'example/file3']


# List files in a directory

# Generated at 2022-06-14 06:25:23.207063
# Unit test for function join_each
def test_join_each():
    # Setup
    parent = tmp_path / 'parent'
    parent.mkdir()
    child = tmp_path / 'child'
    child.mkdir()
    items = [child]

    # Execute
    result = [item for item in join_each(parent, items)]

    # Verify
    assert result[0] == os.path.join(parent, child)

# Generated at 2022-06-14 06:25:26.728991
# Unit test for function join_each
def test_join_each():
    assert list(join_each('foo', ['bar', 'baz'])) == ['foo/bar', 'foo/baz']


# Returns a string link like 'foo/bar/baz''

# Generated at 2022-06-14 06:25:31.131263
# Unit test for function join_each
def test_join_each():
    assert list(join_each('/a', ['b', 'c', 'd'])) == \
        ['/a/b', '/a/c', '/a/d']



# Generated at 2022-06-14 06:25:39.811883
# Unit test for function join_each
def test_join_each():
    """
    Join strings in iterable to parent
    """
    parent = 'the/parent'
    children = ['child1', 'child2', 'child3']
    output = []
    for child in join_each(parent, children):
        output.append(child)
    assert output[0] == 'the/parent/child1'
    assert output[1] == 'the/parent/child2'
    assert output[2] == 'the/parent/child3'



# Generated at 2022-06-14 06:25:42.137784
# Unit test for function join_each
def test_join_each():
    iterable = ('a', 'b', 'c')
    parent = 'test'
    assert tuple(join_each(parent, iterable)) == ('test/a', 'test/b', 'test/c')



# Generated at 2022-06-14 06:25:45.018446
# Unit test for function join_each
def test_join_each():
    parent = '/'
    iterable = ['User', 'bin', 'bash']
    expected = ['/User', '/bin', '/bash']
    result = [i for i in join_each(parent, iterable)]
    assert expected == result



# Generated at 2022-06-14 06:25:48.427528
# Unit test for function join_each
def test_join_each():
    assert list(join_each('foo', ['a', 'b', 'c'])) == [
        'foo/a', 'foo/b', 'foo/c'
    ]



# Generated at 2022-06-14 06:25:50.735450
# Unit test for function join_each
def test_join_each():
    assert list(join_each("foo", ["bar", "baz"])) == ["foo/bar", "foo/baz"]

