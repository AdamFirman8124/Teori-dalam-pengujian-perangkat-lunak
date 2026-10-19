

# Generated at 2022-06-14 06:25:12.307188
# Unit test for function join_each
def test_join_each():
    iterable = ['ball', 'cat', 'tree']
    parent = '/home/user/'
    expected = ['/home/user/ball', '/home/user/cat', '/home/user/tree']
    assert list(join_each(parent, iterable)) == expected



# Generated at 2022-06-14 06:25:19.159589
# Unit test for function join_each
def test_join_each():
    parent = '/home/user'
    iterable = ['a', 'b', 'c']
    expected_result = ['/home/user/a', '/home/user/b', '/home/user/c']
    assert list(join_each(parent, iterable)) == expected_result
    # equiv of `assert`:
    # result = list(join_each(parent, iterable))
    # if not result == expected_result:
    #     raise AssertionError(result)

# Generated at 2022-06-14 06:25:21.186799
# Unit test for function join_each
def test_join_each():
    assert list(join_each('/', ['a', 'b'])) == ['/a', '/b']



# Generated at 2022-06-14 06:25:24.479214
# Unit test for function join_each
def test_join_each():
    assert list(join_each('/', 'test1 test2'.split())) == [
        '/test1', '/test2'
    ]



# Generated at 2022-06-14 06:25:31.782905
# Unit test for function join_each
def test_join_each():
    parent = "/home/dave"
    f1 = "foo.txt"
    f2 = "bar.py"
    f3 = "foo"
    iterable = [f1, f2, f3]
    expected_result = [os.path.join(parent, f1), os.path.join(parent, f2),
                       os.path.join(parent, f3)]

    result = list(join_each(parent, iterable))
    assert result == expected_result

# Generated at 2022-06-14 06:25:41.461787
# Unit test for function join_each
def test_join_each():
    assert list(join_each('a', ['b', 'c'])) == ['a/b', 'a/c']
    assert list(join_each('a', ['b/c', 'd'])) == ['a/b/c', 'a/d']
    assert list(join_each('a', ['b', 'c/d'])) == ['a/b', 'a/c/d']
    assert list(join_each('a/b', ['c', 'd'])) == ['a/b/c', 'a/b/d']

# Generated at 2022-06-14 06:25:44.128467
# Unit test for function join_each
def test_join_each():
    assert list(join_each('root', ['one', 'two'])) == \
        ['root/one', 'root/two']



# Generated at 2022-06-14 06:25:47.484587
# Unit test for function join_each
def test_join_each():
    assert list(join_each('a', ['b', 'c'])) == ['a/b', 'a/c']
    assert list(join_each('', ['b', 'c'])) == ['/b', '/c']



# Generated at 2022-06-14 06:25:57.829435
# Unit test for function join_each
def test_join_each():
    assert list(join_each('a', ['b', 'c'])) == ['a/b', 'a/c']
    assert list(join_each('/', ['b', 'c'])) == ['/b', '/c']
    assert list(join_each('a/', ['b', 'c'])) == ['a/b', 'a/c']
    assert list(join_each('/a', ['b', 'c'])) == ['/a/b', '/a/c']
    assert list(join_each('a', [])) == []
    assert list(join_each('', [])) == []
    assert list(join_each('', ['b', 'c'])) == ['b', 'c']
    assert list(join_each('a', ['b/', '/c'])) == ['a/b/', '/c']
   

# Generated at 2022-06-14 06:25:59.069992
# Unit test for function join_each