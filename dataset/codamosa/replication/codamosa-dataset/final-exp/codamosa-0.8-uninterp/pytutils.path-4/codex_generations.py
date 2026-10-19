

# Generated at 2022-06-14 06:25:11.860961
# Unit test for function join_each
def test_join_each():
    iterable = join_each('/usr', ('lib', 'lib64'))
    assert next(iterable) == '/usr/lib'
    assert next(iterable) == '/usr/lib64'



# Generated at 2022-06-14 06:25:14.149131
# Unit test for function join_each
def test_join_each():
    assert list(join_each('/', ['test', 'path'])) == ['/test', '/path']



# Generated at 2022-06-14 06:25:17.069936
# Unit test for function join_each
def test_join_each():
    assert list(join_each('a', ['b', 'c'])) == ['a/b', 'a/c']



# Generated at 2022-06-14 06:25:19.441897
# Unit test for function join_each
def test_join_each():
    assert list(join_each('/', ['root', 'something'])) == ['/root', '/something']



# Generated at 2022-06-14 06:25:29.062252
# Unit test for function join_each
def test_join_each():
    expected = [
        os.path.join('/', 'tmp') + os.path.sep,
        os.path.join('/', 'var') + os.path.sep,
        os.path.join('/', 'etc') + os.path.sep,
    ]
    result = list(join_each('/', ('tmp', 'var', 'etc')))
    assert result == expected


if __name__ == '__main__':
    import pytest
    pytest.main(sys.argv)

# Generated at 2022-06-14 06:25:32.457175
# Unit test for function join_each
def test_join_each():
    expected = ['test/test1', 'test/test2', 'test/test3']
    assert list(join_each('test', ['test1', 'test2', 'test3'])) == expected



# Generated at 2022-06-14 06:25:36.764084
# Unit test for function join_each
def test_join_each():
    d = os.path.dirname(__file__)
    for f in join_each(d, ['../ghutils/__init__.py', '../setup.py']):
        print(f)
    assert True

# Generated at 2022-06-14 06:25:43.054664
# Unit test for function join_each
def test_join_each():
    assert list(
        join_each('/Users/Fred/Research/Owls', ['Hedwig', 'Harry'])
    ) == ['/Users/Fred/Research/Owls/Hedwig', '/Users/Fred/Research/Owls/Harry']
    assert list(join_each('/', ['/etc', '/var'])) == ['/etc', '/var']

# Generated at 2022-06-14 06:25:48.206266
# Unit test for function join_each
def test_join_each():
    # Path.joinpath
    res = list(join_each('a', ['b', 'c']))
    assert res == ['a/b', 'a/c']
    # Path.glob
    res = list(join_each('.', ['**/hdl', '**/sw', '**/python']))
    assert res == ['./**/hdl', './**/sw', './**/python']



# Generated at 2022-06-14 06:25:50.946509
# Unit test for function join_each
def test_join_each():
    actual = list(join_each('/home', ['data', 'user']))
    expected = ['/home/data', '/home/user']
    assert actual == expected

