

# Generated at 2022-06-14 06:25:08.465720
# Unit test for function join_each
def test_join_each():
    actual = list(join_each("abc", ["", "def", "ghi"]))
    assert actual == ["abc/", "abc/def", "abc/ghi"]

# Generated at 2022-06-14 06:25:14.753819
# Unit test for function join_each
def test_join_each():
    inputs = [
        (('/home', ['a', 'b', 'c']), ['/home/a', '/home/b', '/home/c']),
        (('/home', ['a', 'b']), ['/home/a', '/home/b']),
    ]
    for pairs in inputs:
        assert list(join_each(*pairs[0])) == pairs[1]

# Generated at 2022-06-14 06:25:20.634005
# Unit test for function join_each
def test_join_each():
    expected = [
        './a/b.py',
        './a/c.py',
        './a/d.py',
    ]
    assert list(join_each('.', ['a/b.py', 'a/c.py', 'a/d.py'])) == expected


if __name__ == "__main__":
    test_join_each()


# Line: 140
# Function: get_signature()

# Generated at 2022-06-14 06:25:25.445661
# Unit test for function join_each
def test_join_each():
    assert tuple(join_each('/root', ['one', 'two', 'three'])) == tuple(os.path.join('/root', p) for p in
                                                                        ['one', 'two', 'three'])



# Generated at 2022-06-14 06:25:30.679500
# Unit test for function join_each
def test_join_each():
    assert list(join_each('/', 'a', 'b', 'c')) == ['/a', '/b', '/c']
    assert list(join_each('/', 'a', 'b', 'c', r'\d')) == ['/a', '/b', '/c', r'\d']

# Generated at 2022-06-14 06:25:36.104799
# Unit test for function join_each
def test_join_each():
    assert join_each('/home', ['a', 'b', 'c']) == [
        os.path.join('/home', 'a'),
        os.path.join('/home', 'b'),
        os.path.join('/home', 'c')
    ]



# Generated at 2022-06-14 06:25:46.160038
# Unit test for function join_each
def test_join_each():
    current_dir = os.path.dirname(__file__)
    parent = os.path.dirname(current_dir)
    files = os.listdir(current_dir)

    components = list(join_each(parent, files))
    print(components)
    assert len(components) == len(files)

    for p in components:
        assert os.path.isfile(p) is False

    # os.path.join(parent, None) won't raise exception 'TypeError',
    # but just return parent
    assert list(join_each(parent, [None])) == [parent]



# Generated at 2022-06-14 06:25:50.093756
# Unit test for function join_each
def test_join_each():
    assert list(join_each('c:/', ['a', 'b'])) == ['c:/a', 'c:/b']
    assert list(join_each('c:/', [])) == []

# Generated at 2022-06-14 06:25:56.169318
# Unit test for function join_each
def test_join_each():
    parent = "/tmp"
    files = [
        "a",
        "b",
        "c",
    ]
    files = join_each(parent, files)
    assert next(files) == os.path.join(parent, "a")
    assert next(files) == os.path.join(parent, "b")
    assert next(files) == os.path.join(parent, "c")
    with pytest.raises(StopIteration):
        next(files)



# Generated at 2022-06-14 06:26:06.198539
# Unit test for function join_each
def test_join_each():
    # Case: No parent directory, no iteration, result should be empty
    assert not list(join_each('', []))

    # Case: No parent directory, iterate over empty, result should be empty
    assert not list(join_each('', [[], list()]))

    # Case: parent directory, iterate over empty sequence, result should be empty
    assert not list(join_each(os.path.join('foo', 'bar', 'baz'), []))

    # Case: parent directory, iterate over sequence, result should be the right full paths