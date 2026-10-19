

# Generated at 2022-06-14 06:25:14.212444
# Unit test for function join_each
def test_join_each():
    # Test when parent is empty string
    assert list(join_each('', ['a', 'b', 'c'])) == [
        os.path.join('', 'a'),
        os.path.join('', 'b'),
        os.path.join('', 'c'),
    ]

    # Test when parent is non-empty string
    assert list(join_each('p', ['a', 'b', 'c'])) == [
        os.path.join('p', 'a'),
        os.path.join('p', 'b'),
        os.path.join('p', 'c'),
    ]

# Generated at 2022-06-14 06:25:16.506432
# Unit test for function join_each
def test_join_each():
    assert list(join_each('/', ['x', 'y'])) == ['/x', '/y']



# Generated at 2022-06-14 06:25:22.573786
# Unit test for function join_each
def test_join_each():
    assert list(join_each('a', ['b', 'c'])) == ['a/b', 'a/c']
    assert list(join_each('a', [])) == []
    assert list(join_each('a', ['b/c'])) == ['a/b/c']



# Generated at 2022-06-14 06:25:29.114285
# Unit test for function join_each
def test_join_each():
    d = os.path.dirname
    assert list(join_each(d(__file__), ('foo', 'bar', 'baz'))) == \
        [os.path.join(d(__file__), 'foo'),
         os.path.join(d(__file__), 'bar'),
         os.path.join(d(__file__), 'baz')]



# Generated at 2022-06-14 06:25:39.102857
# Unit test for function join_each
def test_join_each():
    # Test case 1
    # Expected result:
    #  ['/home/A/B/C', '/home/A/B/D', '/home/A/B/E']
    assert list(join_each('/home/A/B', ['C', 'D', 'E'])) == \
           ['/home/A/B/C', '/home/A/B/D', '/home/A/B/E']

    # Test case 2
    # Expected result:
    #  ['C:\\A\\B\\C', 'C:\\A\\B\\D', 'C:\\A\\B\\E']

# Generated at 2022-06-14 06:25:41.686077
# Unit test for function join_each
def test_join_each():
    parent = "parent"
    iterable = ['a', 'b']
    assert [p for p in join_each(parent, iterable)] == [
        "parent/a",
        "parent/b"
    ]

# Generated at 2022-06-14 06:25:44.364249
# Unit test for function join_each
def test_join_each():
    assert list(join_each("foo", ["bar", "baz"])) == ["foo/bar", "foo/baz"]



# Generated at 2022-06-14 06:25:48.142759
# Unit test for function join_each
def test_join_each():
    assert list(join_each('/', [])) == [], 'join_each should work for empty list'
    assert list(join_each('/', ['usr', 'local', 'bin'])) == ['/usr', '/local', '/bin'], \
        'join_each should work for non-empty list'



# Generated at 2022-06-14 06:25:53.382715
# Unit test for function join_each
def test_join_each():
    result = join_each('test', ['a', 'b', 'c'])
    assert next(result) == 'test/a'
    assert next(result) == 'test/b'
    assert next(result) == 'test/c'
    with pytest.raises(StopIteration):
        next(result)



# Generated at 2022-06-14 06:26:00.608113
# Unit test for function join_each
def test_join_each():
    result = list(join_each('/chrc', [
        'binary', 'resources', 'manifest.json',
        os.path.join('resources', 'l10n')
    ]))
    assert result == [
        '/chrc/binary',
        '/chrc/resources',
        '/chrc/manifest.json',
        '/chrc/resources/l10n'
    ]