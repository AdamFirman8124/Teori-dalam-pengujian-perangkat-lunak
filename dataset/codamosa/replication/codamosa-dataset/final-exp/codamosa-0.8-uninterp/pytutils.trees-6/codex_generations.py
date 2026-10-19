

# Generated at 2022-06-14 06:46:14.168396
# Unit test for function get_tree_node
def test_get_tree_node():
    data = tree()
    data['foo']['bar'] = "bar"
    data['baz']['bar'] = "bar"
    assert get_tree_node(data, "foo:bar") == "bar"
    assert get_tree_node(data, "baz:bar") == "bar"
    assert get_tree_node(data, "qux:bar") == _sentinel
    assert get_tree_node(data, "a", default="b") == "b"
    assert get_tree_node(data, "a", default="b", parent=True) == {}

# Generated at 2022-06-14 06:46:28.329075
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = {
        'a': {
            'b': {
                'c': 'hi!'
            }
        }
    }

    assert mapping['a']['b']['c'] == 'hi!'

    assert get_tree_node(mapping, 'a:b:c') == 'hi!'
    assert get_tree_node(mapping, 'a:b:c:d', default='ohai!') == 'ohai!'

    with pytest.raises(KeyError):
        get_tree_node(mapping, 'a:b:c:d')

    assert get_tree_node(mapping, 'a:b:c:d', parent=True) == {'c': 'hi!'}

# Generated at 2022-06-14 06:46:32.058979
# Unit test for function set_tree_node
def test_set_tree_node():
    dct = {}
    dct['a:b:c'] = 'test'
    assert dct['a']['b']['c'] == 'test'



# Generated at 2022-06-14 06:46:45.537746
# Unit test for constructor of class RegistryTree
def test_RegistryTree():
    class Unicorn(Exception): pass
    def handler(exc, unicorn_type=Unicorn):
        raise unicorn_type('Whelp, good thing we\'re in a unit test, eh?')
    exc_context = sys.exc_info()
    exc_info = (Unicorn, Unicorn('foo'), sys.exc_info()[2])
    data = [
        (Unicorn, {'exc': exc_context, 'code': 42}, 42),
        (Unicorn, {'exc': exc_info}, 42),
        (None, {}, None),
        (Exception, {'exc': exc_info, 'code': 42}, None),
        (Exception, {'exc': exc_context, 'code': 42}, None),
    ]


# Generated at 2022-06-14 06:46:51.113310
# Unit test for function set_tree_node
def test_set_tree_node():
    """Test that the set_tree_node function properly sets the value on a tree."""
    tr = tree()
    assert set_tree_node(tr, 'a:b:c:d', 123) == {'d': 123}
    assert tr == {'a': {'b': {'c': {'d': 123}}}}



# Generated at 2022-06-14 06:46:55.647811
# Unit test for constructor of class RegistryTree
def test_RegistryTree():
    assert isinstance(RegistryTree(), RegistryTree) is True
    assert isinstance(RegistryTree().register, collections.defaultdict.__setitem__)
    assert isinstance(RegistryTree().register({}), collections.defaultdict.__setitem__)

# Generated at 2022-06-14 06:47:07.478631
# Unit test for function get_tree_node
def test_get_tree_node():
    import unittest

    class Test(unittest.TestCase):
        def test_delve_single_node(self):
            tree = {'a': {'b': {'c': 'd'}}}
            self.assertEqual(get_tree_node(tree, 'a:b:c'), 'd')

        def test_delve_multiple_nodes(self):
            tree = {'a': {'b': {'c': 'd'}}, 'e': {'f': {'g': 'h'}}}
            self.assertEqual(len(get_tree_node(tree, 'e:f')), 1)


# Generated at 2022-06-14 06:47:21.103678
# Unit test for function get_tree_node
def test_get_tree_node():

    # Basic
    mapping = {
        'foo': {
            'bar': 'value'
        }
    }
    assert get_tree_node(mapping, 'foo:bar') == 'value'

    # Tree traversal
    mapping = {
        'foo': {
            'bar': {
                'foobar': 'value'
            }
        }
    }
    assert get_tree_node(mapping, 'foo:bar:foobar') == 'value'

    # Default value
    mapping = {
        'foo': {
            'bar': {
                'foobar': 'value'
            }
        }
    }
    assert get_tree_node(mapping, 'foo:baz:foobar', default=42) == 42

    # Parent node

# Generated at 2022-06-14 06:47:33.552109
# Unit test for function get_tree_node
def test_get_tree_node():
    # Setup
    d = {'a': {'1': {'x': 'foo',
                     'y': 'bar'},
              '2': 'val2'},
         'b': 'val3',
         'c': {'1': {'z': 'blah'},
               '2': 'val5'},
         'x': 'foo',
         'y': 'bar',
         'z': 'blah'}
    # Test
    assert get_tree_node(d, 'a:1:x') == 'foo'
    assert get_tree_node(d, 'a:1:y') == 'bar'
    assert get_tree_node(d, 'a:2') == 'val2'
    assert get_tree_node(d, 'z') == 'blah'
    assert get_tree_

# Generated at 2022-06-14 06:47:45.829285
# Unit test for function get_tree_node
def test_get_tree_node():
    tree = {
        'foo': {
            'bar': {
                'baz': 'INSERT BEEF HERE'
            },
            'qux': 'INSERT BACON HERE'
        }
    }

    assert 'INSERT BEEF HERE' == get_tree_node(tree, 'foo:bar:baz')
    assert 'INSERT BACON HERE' == get_tree_node(tree, 'foo:qux')
    assert tree['foo']['bar'] == get_tree_node(tree, 'foo:bar', parent=True)
    assert tree['foo']['bar'] == get_tree_node(tree, 'foo:bar:baz', parent=True)



# Generated at 2022-06-14 06:47:52.775516
# Unit test for function set_tree_node
def test_set_tree_node():
    mapping = {}
    set_tree_node(mapping, 'foo:bar', 'apple')
    assert mapping['foo']['bar'] == 'apple'



# Generated at 2022-06-14 06:47:59.422222
# Unit test for function get_tree_node
def test_get_tree_node():
    assert get_tree_node(dict(a=1, b=2), 'a') == 1
    assert get_tree_node(dict(a=dict(b=2, c=3)), 'a:b') == 2
    assert get_tree_node(dict(a=dict(b=2, c=3)), 'a:b:c') is _sentinel



# Generated at 2022-06-14 06:48:06.094760
# Unit test for function set_tree_node
def test_set_tree_node():
    """
    Tests set_tree_node and get_tree_node
    """
    mapping = {}
    set_tree_node(mapping, 'a:b:c', 123)
    set_tree_node(mapping, 'a:b:d', 321)
    set_tree_node(mapping, 'a:b:d', 321)
    assert mapping == {'a': {'b': {'c': 123, 'd': 321}}}



# Generated at 2022-06-14 06:48:12.129290
# Unit test for function get_tree_node
def test_get_tree_node():
    t = tree()
    t['a']['b'] = '2'
    print(get_tree_node(t, 'a:b'))
    assert get_tree_node(t, 'a:b') == '2'


if __name__ == '__main__':
    test_get_tree_node()

# Generated at 2022-06-14 06:48:16.009919
# Unit test for function get_tree_node
def test_get_tree_node():
    """Unit test for function get_tree_node."""
    assert get_tree_node({'a': {'b': 'c'}}, 'a:b') == 'c'


# Generated at 2022-06-14 06:48:27.276997
# Unit test for function get_tree_node
def test_get_tree_node():
    data = Tree({
        'foo': {
            'bar': 123,
            'baz': {
                'bar': 321,
            }
        }
    })

    assert data.get('foo:bar') == 123
    assert data.get('foo:baz:bar') == 321

    # Should raise an error
    with pytest.raises(KeyError):
        assert data.get('foo:baz:bar:123')

    # Should return default value
    assert data.get('foo:baz:bar:123:456:789', default=1) == 1
    assert data.get('foo:baz:bar:123:456:789', default=None) is None

    # Should return the parent node.
    assert data.get('foo:bar', parent=True) == data['foo']
    assert data.get

# Generated at 2022-06-14 06:48:37.906841
# Unit test for function get_tree_node
def test_get_tree_node():
    # Simple nested tree
    tree = {'1': {'2': {'3': '4'}}}

    # Test for single level key
    assert get_tree_node(tree, '1') == {'2': {'3': '4'}}

    # Test for multiple level key
    assert get_tree_node(tree, '1:2') == {'3': '4'}

    # Test for multiple level key, but returning parent
    assert get_tree_node(tree, '1:2', parent=True) == {'2': {'3': '4'}}

    # Test for non-existent key
    with pytest.raises(KeyError):
        get_tree_node(tree, '5')

    # Test for non-existent key, but default value is specified

# Generated at 2022-06-14 06:48:44.840885
# Unit test for function set_tree_node
def test_set_tree_node():
    mapping = collections.defaultdict(lambda: collections.defaultdict(tuple))
    node = set_tree_node(mapping, 'hoi:doei', 'foo:bar:baz')
    assert node == {'hoi': {'doei': 'foo:bar:baz'}}


if __name__ == '__main__':
    test_set_tree_node()

# Generated at 2022-06-14 06:48:55.123518
# Unit test for function get_tree_node
def test_get_tree_node():
    foo = {'bar': {'baz': 'foo'}}
    bar = {'bar:baz': 'foo'}

    assert get_tree_node(foo, 'bar:baz') == 'foo'
    assert get_tree_node(foo, 'bar') == {'baz': 'foo'}
    assert get_tree_node(bar, 'bar:baz') == 'foo'
    with pytest.raises(KeyError):
        assert get_tree_node(bar, 'baz:bar') is None
    with pytest.raises(KeyError):
        assert get_tree_node(bar, 'baz') is None



# Generated at 2022-06-14 06:49:07.186971
# Unit test for function get_tree_node
def test_get_tree_node():
    tree_data = {
        'a': {
            'blank': '',
            'b': 3,
            'c': {
                'd': {
                    'e': 'f'
                }
            }
        }
    }

    assert get_tree_node(tree_data, 'a:blank') == ''
    assert get_tree_node(tree_data, 'a:unset', default='r') == 'r'
    assert get_tree_node(tree_data, 'a:unset') is _sentinel
    assert get_tree_node(tree_data, 'a:c:d:e') == 'f'
    assert get_tree_node(tree_data, 'a:c:d:e:unset', default='r') == 'r'

# Generated at 2022-06-14 06:49:26.299895
# Unit test for function set_tree_node
def test_set_tree_node():
    class mapping(object):
        def __init__(self):
            self.tree = {}

        def __setitem__(self, key, value):
            self.tree[key] = value

        def __getitem__(self, key):
            return self.tree[key]

    test_data = mapping()
    set_tree_node(test_data, 'foo:bar:baz', 42)
    assert test_data['foo']['bar']['baz'] == 42
    set_tree_node(test_data, 'foo:bar:spam', 'eggs')
    assert test_data['foo']['bar']['spam'] == 'eggs'
    set_tree_node(test_data, 'foo:spam', 'ham')
    assert test_data['foo']['spam']

# Generated at 2022-06-14 06:49:38.568245
# Unit test for function get_tree_node
def test_get_tree_node():

    assert(get_tree_node({"foo": 1}, "foo") == 1)  # Simple
    assert(get_tree_node({"foo": {"bar": 1}}, "foo:bar") == 1)  # Complex
    assert(get_tree_node({"foo": {"bar": 1}}, "foo:bar", default=3) == 1)  # Complex w/ default
    assert(get_tree_node({"foo": {"bar": 1}}, "foo:baz") == 3)  # Complex w/ default that returns default

    with pytest.raises(KeyError):
        get_tree_node({"foo": 1}, "bar")  # Simple that raises exception

    with pytest.raises(KeyError):
        get_tree_node({"foo": {"bar": 1}}, "foo:baz")  # Complex

# Generated at 2022-06-14 06:49:41.697974
# Unit test for function get_tree_node
def test_get_tree_node():
    t = Tree({
        'a': {
            'b': {
                'c': 1
            }
        }
    })
    assert get_tree_node(t, 'a:b:c') == 1
    assert get_tree_node(t, 'a:b') == {'c': 1}


# Generated at 2022-06-14 06:49:46.892172
# Unit test for function set_tree_node
def test_set_tree_node():
    assert 'x' == set_tree_node({}, 'foo/bar/x', 'x')['foo']['bar']['x']
    assert 'x' == set_tree_node({'foo': {}}, 'foo/bar/x', 'x')['foo']['bar']['x']



# Generated at 2022-06-14 06:49:58.641502
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = {
        'a': {
            'a1': 'value',
            'a2': {
                'a21': 'value2'
            }
        },
        'b': 'value3'
    }

    assert get_tree_node(mapping, 'b') == 'value3'
    assert get_tree_node(mapping, 'a:a2:a21') == 'value2'
    assert get_tree_node(mapping, 'a:a21', default=None) is None
    with pytest.raises(AssertionError):
        get_tree_node(mapping, 'a:a21')



# Generated at 2022-06-14 06:50:02.680257
# Unit test for function set_tree_node
def test_set_tree_node():
    mapping = {}
    set_tree_node(mapping, 'a:b:c', 'test')
    assert mapping['a']['b']['c'] == 'test'



# Generated at 2022-06-14 06:50:14.505807
# Unit test for function get_tree_node
def test_get_tree_node():
    assert get_tree_node({}, 'a') == _sentinel

    assert get_tree_node({'a': 'b'}, 'a') == 'b'
    assert get_tree_node({'a': {'b': 'c'}}, 'a:b') == 'c'

    try:
        get_tree_node({'a': {'b': 'c'}}, 'a:x')
        assert False, 'Should have raised KeyError'
    except KeyError:
        pass

    assert get_tree_node({'a': {'b': 'c'}}, 'a:x', default=None) is None

    # Test parent
    assert get_tree_node({'a': {'b': 'c'}}, 'a:b', parent=True) == {'b': 'c'}



# Generated at 2022-06-14 06:50:24.580326
# Unit test for function get_tree_node
def test_get_tree_node():
    test_mapping = {'top1': {'mid1': {'leaf1': 'leaf2'}, 'mid2': {'leaf2': {'leaf3': 'leaf4'}, 'leaf3': 'leaf5'}}}
    assert get_tree_node(test_mapping, 'mid1:leaf1') == 'leaf2'
    assert get_tree_node(test_mapping, 'mid2:leaf2:leaf3') == 'leaf4'
    get_tree_node(test_mapping, 'mid2:leaf2:leaf4', default='default_value') == 'default_value'


# Generated at 2022-06-14 06:50:30.907288
# Unit test for function set_tree_node
def test_set_tree_node():
    """Unit test for function set_tree_node"""
    d = tree()
    # Test list handling
    d['a:b:c'].append(123)
    assert d['a']['b']['c'] == [123]

    # Test int handling
    d['x:y:z'] = 999
    assert d['x']['y']['z'] == 999
    return



# Generated at 2022-06-14 06:50:33.038877
# Unit test for function get_tree_node
def test_get_tree_node():
    pass



# Generated at 2022-06-14 06:50:50.374492
# Unit test for function get_tree_node

# Generated at 2022-06-14 06:51:01.829423
# Unit test for function get_tree_node
def test_get_tree_node():
    from random import randint
    from time import time

    start_time = time()
    # test1
    tree = {'a': {'aa': 2}, 'b': {'bb': 3}}
    assert get_tree_node(tree, 'a:aa') == 2
    assert get_tree_node(tree, 'b:bb') == 3
    # test2
    tree = {'a': {'aa': 2, 'ab': 3}, 'b': {'bb': 4, 'bc': 5}}
    assert get_tree_node(tree, 'a:aa') == 2
    assert get_tree_node(tree, 'a:ab') == 3
    assert get_tree_node(tree, 'b:bb') == 4
    assert get_tree_node(tree, 'b:bc') == 5
    # test3

# Generated at 2022-06-14 06:51:13.747135
# Unit test for function get_tree_node
def test_get_tree_node():
    test_mapping = collections.OrderedDict({
        "key1": "value1",
        "key2": {"key3": "value3"},
        "key4": {"key5": {"key6": "value6"}}
    })

    def test_get_node(key, value, default=_sentinel):
        assert get_tree_node(test_mapping, key, default) == value

    test_get_node("key1", "value1")
    test_get_node("key2:key3", "value3")
    test_get_node("key4:key5:key6", "value6")
    try:
        test_get_node("key7", "value7")
        assert False, "KeyError not raised"
    except KeyError:
        assert True

    test_get_node

# Generated at 2022-06-14 06:51:23.488690
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = tree()
    mapping['foo']['bar']['baz'] = 'spam'
    assert get_tree_node(mapping, 'foo:bar:baz') == 'spam'
    assert get_tree_node(mapping, 'foo:bar') == {'baz': 'spam'}
    assert get_tree_node(mapping, 'xx:yy:zz', default='spam') == 'spam'

    # Test parent node fetching
    assert get_tree_node(mapping, 'foo:bar:baz', parent=True) == {'baz': 'spam'}


# Generated at 2022-06-14 06:51:30.639707
# Unit test for function set_tree_node
def test_set_tree_node():
    test = collections.OrderedDict()
    assert set_tree_node(test, 'a', 'A') == test
    assert set_tree_node(test, 'b:b1', 'B1') == {'b': {'b1': 'B1'}}
    assert set_tree_node(test, 'b:b2:b21', 'B21') == {
        'b': {'b1': 'B1', 'b2': {'b21': 'B21'}}
    }
    assert test == {
        'a': 'A',
        'b': {
            'b1': 'B1',
            'b2': {
                'b21': 'B21',
            },
        },
    }


# Generated at 2022-06-14 06:51:36.954860
# Unit test for function set_tree_node
def test_set_tree_node():
    tree = {}
    set_tree_node(tree, 'foo:bar:baz', 'value')
    assert tree['foo']['bar']['baz'] == 'value'

    try:
        set_tree_node(tree, 'foo:bar:baz:wtf', 'value')
    except KeyError:
        pass



# Generated at 2022-06-14 06:51:40.969883
# Unit test for function set_tree_node
def test_set_tree_node():
    mapping = {'foo': {'bar': 'baz'}}
    set_tree_node(mapping, 'foo:bar:taz', 'taz')
    assert mapping['foo']['bar']['taz'] == 'taz'



# Generated at 2022-06-14 06:51:54.137366
# Unit test for function get_tree_node
def test_get_tree_node():
    # Define our tree
    t = tree()

    # Set some dimensions
    t['a']['b']['c'] = 1
    t['a']['b']['d'] = 2

    # Check some values
    assert t['a']['b']['c'] == 1
    assert t['a']['b']['d'] == 2

    # Check the whole thing
    assert t == {
        'a': {
            'b': {
                'c': 1,
                'd': 2
            }
        }
    }

    # Return a couple of things.
    assert get_tree_node(t, 'a') == {'b': {'c': 1, 'd': 2}}

# Generated at 2022-06-14 06:52:05.439609
# Unit test for function get_tree_node
def test_get_tree_node():
    data = {
        'a': {
            'b': {
                'c': 1,
            }
        }
    }

    assert get_tree_node(data, 'a:b:c') == get_tree_node(data, 'a')['b']['c']
    try:
        get_tree_node(data, 'a:b:c:d')
    except KeyError:
        pass
    else:
        assert False

    assert get_tree_node(data, 'a:b:c:d', 'foo') == 'foo'
    assert get_tree_node(data, 'a:b:c:d', 0) == 0
    assert get_tree_node(data, 'a:b:c:d', default=0) == 0

# Generated at 2022-06-14 06:52:15.792559
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = {
        'home': {
            'usr': {
                'local': {
                    'bin': 'foo'
                }
            }
        }
    }
    result = get_tree_node(mapping, 'home:usr:local:bin')
    expected = 'foo'
    assert result == expected

    result = get_tree_node(mapping, 'home:usr:local:bin:alpha:beta', parent=True)
    expected = {
        'bin': 'foo',
        'alpha': {
            'beta': None
        }
    }
    assert result == expected

# Generated at 2022-06-14 06:52:34.328721
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = {
        'a': {
            'b': 'c',
        }
    }

    assert get_tree_node(mapping, 'a:b') == 'c'
    try:
        get_tree_node(mapping, 'a:c')
        assert False, 'Expected KeyError'
    except KeyError:
        pass
    assert get_tree_node(mapping, 'a:c', default='d') == 'd'
    assert get_tree_node(mapping, 'a:c', parent=True) == {'b': 'c'}



# Generated at 2022-06-14 06:52:47.256081
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = {
        'foo': 123,
        'bar': {
            'baz': 'buzz',
        },
    }

    # Simple
    assert get_tree_node(mapping, 'foo') == 123

    # Nested
    assert get_tree_node(mapping, 'bar:baz') == 'buzz'

    # Parent
    assert get_tree_node(mapping, 'bar:baz', parent=True) == {'baz': 'buzz'}

    # Default
    assert get_tree_node(mapping, 'bar:cux', default=456) == 456

    # No default
    with pytest.raises(KeyError):
        get_tree_node(mapping, 'cux')


# Unit tests for function set_tree_node

# Generated at 2022-06-14 06:53:00.299666
# Unit test for function get_tree_node
def test_get_tree_node():
    tree = RegistryTree()
    tree['a'] = 'A'
    tree['b'] = 'B'
    tree['c'] = 'C'
    tree['d:a'] = 'D:A'
    tree['d:b'] = 'D:B'
    tree['d:c'] = 'D:C'
    tree['e:a'] = 'E:A'
    tree['e:b'] = 'E:B'
    tree['e:c'] = 'E:C'

    assert get_tree_node(tree, 'a') == 'A'
    assert get_tree_node(tree, 'd') == {'a': 'D:A', 'b': 'D:B', 'c': 'D:C'}

# Generated at 2022-06-14 06:53:09.626617
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = {
        'a': {
            'b': {
                'c': 'abc def',
            },
            'd': 1,
            'e': 2,
        },
        'f': {
            'g': 3,
        },
    }

    assert get_tree_node(mapping, 'a') == {'b': {'c': 'abc def'}, 'd': 1, 'e': 2}
    assert get_tree_node(mapping, 'a:b') == {'c': 'abc def'}
    assert get_tree_node(mapping, 'a:b:c') == 'abc def'
    assert get_tree_node(mapping, 'a:d') == 1
    assert get_tree_node(mapping, 'a:e') == 2
    assert get_tree_

# Generated at 2022-06-14 06:53:20.050880
# Unit test for function set_tree_node
def test_set_tree_node():
    class AutoTree(collections.defaultdict):
        def __missing__(self, key):
            self[key] = super(AutoTree, self).__missing__(self.__class__())
            return self[key]

    # Initialize test tree
    n = AutoTree()

    # Assert
    n['a']['b']['c'] = 'd'
    n['a']['b']['d'] = 'e'

    # Assert
    n['a']['b']['c'] = 'd'
    n['a']['b']['d'] = 'e'

    # Assert
    set_tree_node(n, 'a:b:c', 'd')
    set_tree_node(n, 'a:b:d', 'e')

    # Assert

# Generated at 2022-06-14 06:53:33.323917
# Unit test for function get_tree_node
def test_get_tree_node():
    assert get_tree_node(
        {'foo': {'bar': 'baz'}},
        'foo:bar',
    ) == 'baz'
    assert get_tree_node(
        {'foo': {'bar': 'baz'}},
        'foo:bar',
        default='not baz',
    ) == 'baz'
    assert get_tree_node(
        {'foo': {'bar': 'baz'}},
        'does:not:exist',
        default='not baz',
    ) == 'not baz'
    try:
        get_tree_node(
            {'foo': {'bar': 'baz'}},
            'does:not:exist',
        )
    except KeyError:
        pass

# Generated at 2022-06-14 06:53:36.970036
# Unit test for function set_tree_node
def test_set_tree_node():
    d = {'a': {'b': {}}}
    set_tree_node(d, 'a:b:c', 123)
    assert d == {'a': {'b': {'c': 123}}}



# Generated at 2022-06-14 06:53:47.728740
# Unit test for function set_tree_node
def test_set_tree_node():
    """
    Unit test.

    Run with `TEST=registry python -m pyfarm.apps.agent.registry`
    """
    import string
    from nose.tools import assert_equal

    letters = '%s%s' % (string.digits, string.ascii_letters)
    alphabet = letters * 10

    for length in range(1, len(alphabet)):
        for offset in range(len(alphabet) / length):
            key = alphabet[offset:offset + length]
            container = tree()

            set_tree_node(container, key, key)
            assert_equal(container[key], key)



# Generated at 2022-06-14 06:53:55.001836
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = {
        'a': 1,
        'b': 1,
        'c': {
            'a': 1,
            'b': 1
        }
    }
    assert get_tree_node(mapping, 'a') == 1
    assert get_tree_node(mapping, 'c:a') == 1
    assert get_tree_node(mapping, 'c:a', default=2) == 1
    assert get_tree_node(mapping, 'c:f', default=2) == 2
    assert get_tree_node(mapping, 'c:f') == None



# Generated at 2022-06-14 06:54:01.514562
# Unit test for function get_tree_node
def test_get_tree_node():
    key = 'key:hello:world'
    mapping = {
        'key': {
            'hello': {
                'world': 'hello world!'
            }
        }
    }

    assert get_tree_node(mapping, key) == 'hello world!'

    # Parent node
    assert get_tree_node(mapping, key, parent=True) == mapping['key']['hello']

# Generated at 2022-06-14 06:54:24.160494
# Unit test for function set_tree_node
def test_set_tree_node():
    my_tree = tree()
    set_tree_node(my_tree, 'a:b:c', 3)
    assert my_tree['a']['b']['c'] == 3



# Generated at 2022-06-14 06:54:30.093122
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = {
        'key': {
            'dimension1': {
                'dimension2': 'VALUEEE'
            }
        }
    }
    key = 'key:dimension1:dimension2'
    value = get_tree_node(mapping, key)
    assert value == 'VALUEEE'



# Generated at 2022-06-14 06:54:42.906770
# Unit test for function get_tree_node

# Generated at 2022-06-14 06:54:55.281152
# Unit test for function get_tree_node
def test_get_tree_node():
    a = {
        'one': 'b',
        'two': {
            'three': 'c',
            'four': {
                'five': {
                    'six': 'd'
                }
            }
        }
    }
    assert get_tree_node(a, 'one') == 'b'
    assert get_tree_node(a, 'two:three') == 'c'
    assert get_tree_node(a, 'two:four:five:six') == 'd'
    with pytest.raises(KeyError):
        get_tree_node(a, 'two:four:five:seven')
    assert get_tree_node(a, 'two:four:five:seven', default='z') == 'z'

# Generated at 2022-06-14 06:55:07.892488
# Unit test for function set_tree_node
def test_set_tree_node():
    tree = collections.defaultdict(collections.defaultdict)
    assert set_tree_node(tree, 'a:b:c:d', 0) == {'d': 0}
    assert tree['a']['b']['c']['d'] == 0

    # Update.
    test_set_tree_node.tree = tree
    assert set_tree_node(tree, 'a:b:c:d', 1) == {'d': 1}
    assert tree == {'a': {'b': {'c': {'d': 1}}}}

    # Overwrite.
    assert set_tree_node(tree, 'a:b:c:d:e', 2) == {'e': 2}

# Generated at 2022-06-14 06:55:18.991972
# Unit test for function get_tree_node
def test_get_tree_node():
    data = Tree({
        'foo': {
            'bar': {
                'baz': True,
            },
        },
    })

    assert True is get_tree_node(data, 'foo:bar:baz')
    try:
        get_tree_node(data, 'foo:bar:baz:bar')
        assert False, "The following line should raise a `KeyError`"
    except KeyError:
        pass

    try:
        get_tree_node(data, 'foo:bar:baz:bar', _sentinel)
        assert False, "The following line should raise a `KeyError`"
    except KeyError:
        pass

    assert _sentinel is get_tree_node(data, 'foo:bar:baz:bar', default=_sentinel)
    assert None is get_tree_

# Generated at 2022-06-14 06:55:23.150054
# Unit test for function set_tree_node
def test_set_tree_node():
    tree = {}
    set_tree_node(tree, 'key:key:key', 'value')
    assert tree == {'key': {'key': {'key': 'value'}}}



# Generated at 2022-06-14 06:55:35.961671
# Unit test for function set_tree_node
def test_set_tree_node():
    tree = {}
    set_tree_node(tree, 'a', 'val1')
    assert tree == {'a': 'val1'}
    set_tree_node(tree, 'a', 'val2')
    assert tree == {'a': 'val2'}
    set_tree_node(tree, 'a', 'val3')
    assert tree == {'a': 'val3'}
    set_tree_node(tree, 'a:b', 'val4')
    assert tree == {'a': {'b': 'val4'}}
    set_tree_node(tree, 'a:b', 'val5')
    assert tree == {'a': {'b': 'val5'}}
    set_tree_node(tree, 'a:b:c', 'val6')

# Generated at 2022-06-14 06:55:43.501798
# Unit test for function get_tree_node
def test_get_tree_node():
    """
    Unit test function for function :func:`~candy_path.configuration.get_tree_node`
    """
    config = Tree()
    assert get_tree_node(config, 'key') == {}
    config.update(dict(alpha=dict(beta='gamma')))
    assert get_tree_node(config, 'alpha:beta') == 'gamma'
    assert get_tree_node(config, 'delta') == {}
    with pytest.raises(KeyError):
        get_tree_node(config, 'delta', _sentinel)



# Generated at 2022-06-14 06:55:50.211689
# Unit test for function get_tree_node
def test_get_tree_node():
    d = {'a': {'b': {'c': 'test'}}}
    e = get_tree_node(d, 'a:b:c')
    assert e == 'test'


__all__ = [
    'get_tree_node',
    'set_tree_node',
    'Tree',
    'RegistryTree',
    'tree',
]