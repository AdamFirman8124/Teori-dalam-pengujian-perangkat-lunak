

# Generated at 2022-06-14 06:25:13.595586
# Unit test for function join_each
def test_join_each():
    tests = [
        (("", ["a", "b"]), ["a", "b"]),
        (("a", ["b", "c"]), ["a/b", "a/c"]),
        (("a", []), []),
    ]
    for ((parent, iterable), expected) in tests:
        actual = list(join_each(parent, iterable))
        assert actual == expected



# Generated at 2022-06-14 06:25:18.234309
# Unit test for function join_each
def test_join_each():
    assert list(join_each("/path/to", ["file1", "file2"])) == [
        "/path/to/file1",
        "/path/to/file2",
    ]
    assert list(join_each("/path/to", [])) == []



# Generated at 2022-06-14 06:25:22.284947
# Unit test for function join_each
def test_join_each():
    iterable = ['a', 'b', 'c']
    parent = '/'
    
    for i in iterable:
        assert join_each(parent, iterable).next() == os.path.join(parent, i)



# Generated at 2022-06-14 06:25:25.388687
# Unit test for function join_each
def test_join_each():
    assert isinstance(join_each('.', ['']), types.GeneratorType)
    assert [i for i in join_each('.', [''])] == [os.path.join('.', ''), ]



# Generated at 2022-06-14 06:25:32.137315
# Unit test for function join_each
def test_join_each():
    first = "C:/Users"
    second = ["Andrew", "Mike", "Richard", "Sarah"]

    result = list(join_each(first, second))

    assert result == [
        "C:/Users\\Andrew",
        "C:/Users\\Mike",
        "C:/Users\\Richard",
        "C:/Users\\Sarah",
    ]


if __name__ == "__main__":
    test_join_each()

# Generated at 2022-06-14 06:25:33.778968
# Unit test for function join_each
def test_join_each():
    assert list(join_each('foo', ['bar', 'baz'])) == ['foo/bar', 'foo/baz']

# Generated at 2022-06-14 06:25:37.276940
# Unit test for function join_each
def test_join_each():
    start = "C:/test"
    ll = ["hello", "world"]
    for p in join_each(start, ll):
        assert(p.startswith(start))



# Generated at 2022-06-14 06:25:40.984871
# Unit test for function join_each
def test_join_each():
    p = '/foo'
    x = 'bar'
    f = join_each(p, [x])
    assert next(f) == os.path.join(p, x)



# Generated at 2022-06-14 06:25:48.142632
# Unit test for function join_each
def test_join_each():
    # Base path without backslash
    file1 = join_each("test", ["file1.txt", "file2.txt"])
    # Base path with backslash
    file2 = join_each("test\\", ["file1.txt", "file2.txt"])

    assert next(file1) == "test\\file1.txt"
    assert next(file2) == "test\\file1.txt"
    assert next(file1) == "test\\file2.txt"
    assert next(file2) == "test\\file2.txt"

# Generated at 2022-06-14 06:25:52.861528
# Unit test for function join_each
def test_join_each():
    parent = 'home'
    iterable = ['.', '..', 'files', 'dir']
    expected = ['home/.', 'home/..', 'home/files', 'home/dir']
    result = list(join_each(parent, iterable))
    assert expected == result

