

# Generated at 2022-06-14 06:25:12.687209
# Unit test for function join_each
def test_join_each():
    parent = "Parent"
    iterable = ["1", "2", "3"]
    expected = ["Parent/1", "Parent/2", "Parent/3"]
    actual = [x for x in join_each(parent, iterable)]
    assert expected == actual

# Generated at 2022-06-14 06:25:15.464178
# Unit test for function join_each
def test_join_each():
    assert join_each('/etc/', ['dir1', 'dir2']) == ['/etc/dir1', '/etc/dir2']

# Generated at 2022-06-14 06:25:24.469470
# Unit test for function join_each
def test_join_each():
    for parent, iterable in [
            (".", ["a", "b/c"]),
            ("..", [".", "..", "test"]),
            ("/a/b", ["c", "d/e"])]:
        actual_iterable = join_each(parent, iterable)
        actual = list(actual_iterable)
        expected = list(map(lambda x: os.path.join(parent, x), iterable))
        assert actual == expected


if __name__ == "__main__":
    pytest.main(["-v", __file__])

# Generated at 2022-06-14 06:25:32.773512
# Unit test for function join_each
def test_join_each():
    assert list(join_each("tmp", ["a.txt", "b.txt"])) == [os.path.join("tmp", "a.txt"), os.path.join("tmp", "b.txt")]
    assert list(join_each("tmp", ["a", "b"])) == [os.path.join("tmp", "a"), os.path.join("tmp", "b")]
    assert list(join_each("tmp", {"a", "b"})) == [os.path.join("tmp", "a"), os.path.join("tmp", "b")]



# Generated at 2022-06-14 06:25:41.401348
# Unit test for function join_each

# Generated at 2022-06-14 06:25:44.530810
# Unit test for function join_each
def test_join_each():
    assert list(join_each('/etc', ['passwd', 'hosts'])) == [
        '/etc/passwd', '/etc/hosts']



# Generated at 2022-06-14 06:25:47.985457
# Unit test for function join_each
def test_join_each():
    files = ['a.txt', 'b.txt', 'c.svg']
    expected = ['./a.txt', './b.txt', './c.svg']
    result = list(join_each('./', files))
    assert result == expected



# Generated at 2022-06-14 06:25:53.581938
# Unit test for function join_each
def test_join_each():
    # Given
    parent = "/a/b/c"
    paths = ["d/e", "f", "g/"]

    # When
    results = join_each(parent, paths)

    # Then
    assert list(results) == ["/a/b/c/d/e", "/a/b/c/f", "/a/b/c/g/"]



# Generated at 2022-06-14 06:25:58.556956
# Unit test for function join_each
def test_join_each():
    from tests.support import strings
    actual = join_each(strings.test_dir, ["a", "b", "c"])
    expected = [os.path.join(strings.test_dir, f"{i}") for i in "abc"]
    assert actual == expected

# Generated at 2022-06-14 06:26:07.891464
# Unit test for function join_each
def test_join_each():
    assert list(join_each('foo', ['bar', 'fuz'])) == ['foo/bar', 'foo/fuz']
    assert list(join_each('foo', ['bar', '', 'fuz'])) == ['foo/bar', 'foo/', 'foo/fuz']
    assert list(join_each('', ['bar', 'fuz'])) == ['/bar', '/fuz']
    assert list(join_each('foo', [])) == []
    assert list(join_each('', [])) == []
    assert list(join_each('', ['', '', ''])) == ['//', '/', '/']


if __name__ == '__main__':
    test_join_each()