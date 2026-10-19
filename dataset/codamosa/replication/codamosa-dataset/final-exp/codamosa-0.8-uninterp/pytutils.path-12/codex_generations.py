

# Generated at 2022-06-14 06:25:11.870107
# Unit test for function join_each
def test_join_each():
    start = '/home'
    paths = ('me', '/bin', 'junk')
    expected = ('/home/me', '/bin', '/junk')
    actual = join_each(start, paths)
    print(list(actual))


# Generated at 2022-06-14 06:25:19.199611
# Unit test for function join_each
def test_join_each():
    assert list(join_each('/', ['', 'tmp', '1'])) == [
        '/', '/tmp', '/1']
    assert list(join_each('/tmp', ['', '1'])) == [
        '/tmp', '/tmp/1']
    assert list(join_each('/tmp/', ['', '1'])) == [
        '/tmp/', '/tmp/1']
    assert list(join_each('/tmp/', ['', '1'])) == [
        '/tmp/', '/tmp/1']

# Generated at 2022-06-14 06:25:25.760399
# Unit test for function join_each
def test_join_each():
    parent = os.path.abspath(os.path.dirname(__file__))
    target = [os.path.join(parent, "a.txt"), os.path.join(parent, "b.txt")]
    it = join_each(parent, ["a.txt", "b.txt"])
    assert list(it) == target



# Generated at 2022-06-14 06:25:32.124593
# Unit test for function join_each
def test_join_each():
    assert list(join_each('a/b', ['c', os.path.join('d', 'e')])) == [
        os.path.join('a', 'b', 'c'),
        os.path.join('a', 'b', 'd', 'e')
    ]

# Generated at 2022-06-14 06:25:34.418064
# Unit test for function join_each
def test_join_each():
    assert list(join_each('/home', ['usr', 'local'])) == ['/home/usr', '/home/local']


import os
import os.path
import sys



# Generated at 2022-06-14 06:25:39.873629
# Unit test for function join_each
def test_join_each():
    parent = ['/home', '/lib']
    children = ['1.txt', '2.txt']
    results = list(join_each(parent, children))
    assert results == ['/home/1.txt', '/home/2.txt', '/lib/1.txt', '/lib/2.txt']



# Generated at 2022-06-14 06:25:45.829597
# Unit test for function join_each
def test_join_each():
    paths = ["..", "..", ".."]
    joined = []
    for _ in join_each(os.getcwd(), paths):
        joined.append(_)
    from unittest import TestCase
    TestCase().assertListEqual(joined, list(map(os.path.join, [os.getcwd()] * 3, paths)))
    print("OK")



# Generated at 2022-06-14 06:25:49.736521
# Unit test for function join_each
def test_join_each():
    parent = '/tmp'
    iterable = ['a', 'b', 'c']
    assert list(join_each(parent, iterable)) == ['/tmp/a', '/tmp/b', '/tmp/c']

# Generated at 2022-06-14 06:25:54.462089
# Unit test for function join_each
def test_join_each():
    parent = '/abc'
    iterable = ('def', 'ghi', 'jkl')

    result = join_each(parent, iterable)
    assert isinstance(result, Iterator)
    assert list(result) == [
        '/abc/def',
        '/abc/ghi',
        '/abc/jkl'
    ]



# Generated at 2022-06-14 06:25:57.363331
# Unit test for function join_each
def test_join_each():
    assert list(join_each('a', ('bb', 'cc'))) == ['a/bb', 'a/cc']
