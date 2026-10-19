

# Generated at 2022-06-14 06:25:09.286852
# Unit test for function join_each
def test_join_each():
    assert list(join_each('/home', ['user/', 'init.d/'])) == [
        '/home/user/',
        '/home/init.d/'
    ]



# Generated at 2022-06-14 06:25:14.085870
# Unit test for function join_each
def test_join_each():
    r1 = list(join_each('c:/', ['foo', 'bar']))
    assert r1 == ['c:/foo', 'c:/bar']

    r2 = list(join_each('', ['foo', 'bar']))
    assert r2 == ['foo', 'bar']



# Generated at 2022-06-14 06:25:16.388575
# Unit test for function join_each
def test_join_each():
    assert list(join_each('/', ('tmp', 'etc'))) == ['/tmp', '/etc']



# Generated at 2022-06-14 06:25:22.532966
# Unit test for function join_each
def test_join_each():
    assert list(join_each('/home/pi', 'README.md')) == ['/home/pi/README.md']
    assert list(join_each('/home/pi', ('README.md', 'LICENSE'))) == ['/home/pi/README.md', '/home/pi/LICENSE']



# Generated at 2022-06-14 06:25:28.159788
# Unit test for function join_each
def test_join_each():
    parent = '/home/user/Documents'
    iterable = ['folder', 'file.txt']
    result = join_each(parent, iterable)

    assert list(result) == ['/home/user/Documents/folder',
                            '/home/user/Documents/file.txt']



# Generated at 2022-06-14 06:25:33.105685
# Unit test for function join_each
def test_join_each():
    parent = "/a/b/c"
    paths = ["x", "y", "z"]
    actual = join_each(parent, paths)
    expected = ["/a/b/c/x", "/a/b/c/y", "/a/b/c/z"]
    assert actual == expected



# Generated at 2022-06-14 06:25:38.083630
# Unit test for function join_each
def test_join_each():
    p = '/a/b'
    iterable = ['c', 'd', 'e']
    expected = ['/a/b/c', '/a/b/d', '/a/b/e']
    actual = list(join_each(p, iterable))
    assert actual == expected

# Generated at 2022-06-14 06:25:43.230105
# Unit test for function join_each
def test_join_each():
    parent = 'foo/'
    ls = ['a.txt', 'b.txt', 'c.txt']
    expect = ['foo/a.txt', 'foo/b.txt', 'foo/c.txt']
    result = list(join_each(parent, ls))
    assert expect == result



# Generated at 2022-06-14 06:25:48.204321
# Unit test for function join_each
def test_join_each():
    parent = 'parent'
    iterable = ['a', 'b', 'c']
    expected = ['parent/a', 'parent/b', 'parent/c']
    result = list(join_each(parent, iterable))
    assert result == expected

# Generated at 2022-06-14 06:25:51.362898
# Unit test for function join_each
def test_join_each():
    parent = "cat"
    iterable = ["dog", "bird"]
    expected = ["cat/dog", "cat/bird"]
    assert list(join_each(parent, iterable)) == expected

