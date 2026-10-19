

# Generated at 2022-06-14 06:46:18.127533
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = {
        'foo': {
            'bar': {
                'baz': True
            }
        }
    }
    assert get_tree_node(mapping, 'foo:bar:baz')
    assert get_tree_node(mapping, 'foo:bar:baz', default=False) is True
    assert get_tree_node(mapping, 'foo:bar:baz', parent=True) == {'baz': True}

    with pytest.raises(KeyError):
        get_tree_node(mapping, 'foo:bar:bat')

    with pytest.raises(KeyError):
        get_tree_node(mapping, 'foo:bar:bat', default=False)



# Generated at 2022-06-14 06:46:24.842341
# Unit test for function set_tree_node
def test_set_tree_node():
    test_mapping = {}
    test_key = 'hello:there:my:friend'
    test_value = u'f00'

    result = set_tree_node(test_mapping, test_key, test_value)

    assert result == {'hello': {'there': {'my': {'friend': u'f00'}}}}



# Generated at 2022-06-14 06:46:32.815484
# Unit test for function set_tree_node
def test_set_tree_node():

    # test tree
    test_tree = collections.defaultdict(tree)

    # set node
    test_tree = set_tree_node(test_tree, 'foo:bar', 'baz')

    # set another node
    test_tree = set_tree_node(test_tree, 'foo:boo', 'boo')

    # assert things
    assert test_tree['foo']['bar'] == 'baz'
    assert test_tree['foo']['boo'] == 'boo'



# Generated at 2022-06-14 06:46:46.171689
# Unit test for function get_tree_node
def test_get_tree_node():
    tree = {
        'key1': 'This ',
        'key2': 'is ',
        'key3': {
            'key4': 'a ',
            'key5': {
                'key6': 'test'
            },
            'key7': '!'
        }
    }

    assert get_tree_node(tree, 'key1') == 'This '
    assert get_tree_node(tree, 'key1:key3:key5:key6') == 'test'
    assert get_tree_node(tree, 'key1:key3:key5:key6') == 'test'
    assert get_tree_node(tree, 'key1:key3:key5:key6', parent=True)[0]['key6'] == 'test'

# Generated at 2022-06-14 06:46:56.771267
# Unit test for function get_tree_node
def test_get_tree_node():
    """
    Test :func:`get_tree_node`.

    """
    assert get_tree_node({
        'a': {
            'b': {
                'c': 'd'
            }
        }
    }, 'a', default='a') == {
        'b': {
            'c': 'd'
        }
    }
    assert get_tree_node({
        'a': {
            'b': {
                'c': 'd'
            }
        }
    }, 'a:b', default='a:b') == {
            'c': 'd'
    }

# Generated at 2022-06-14 06:47:02.316077
# Unit test for function get_tree_node
def test_get_tree_node():
    assert get_tree_node({'hi': {'my': 'name'}}, 'hi:my') == 'name'
    assert get_tree_node({'hi': {'my': 'name'}}, 'hi:my:asdf', parent=True) == {'my': 'name'}



# Generated at 2022-06-14 06:47:14.721951
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = {"a" : {"b" : {"c": {"d" : 1}}}}
    assert get_tree_node(mapping, "a") == {"b" : {"c": {"d" : 1}}}
    assert get_tree_node(mapping, "a:b") == {"c": {"d" : 1}}
    assert get_tree_node(mapping, "a:b:c") == {"d" : 1}
    assert get_tree_node(mapping, "a:b:c:d") == 1
    assert get_tree_node(mapping, "a:b:c:d", default=2) == 1
    assert get_tree_node(mapping, "a:b:c:f", default=2) == 2

# Generated at 2022-06-14 06:47:23.416994
# Unit test for function get_tree_node
def test_get_tree_node():
    complex_dict = {
        'foo': {
            'bar': {
                'baz': 'zab',
            },
        },
    }

    assert get_tree_node(complex_dict, 'foo:bar:baz') == 'zab'

    try:
        get_tree_node(complex_dict, 'foo:bar:no:such:path')
    except KeyError:
        assert True
    else:
        assert False, "Expected KeyError"

    assert get_tree_node(complex_dict, 'foo:bar:no:such:path', default='zab') == 'zab'


# Unit Test for function set_tree_node

# Generated at 2022-06-14 06:47:35.399121
# Unit test for function set_tree_node
def test_set_tree_node():
    foo = tree()
    set_tree_node(foo, 'bar:baz', 'joe')
    assert foo['bar']['baz'] == 'joe'

    foo = tree()
    set_tree_node(foo, 'bar:baz:doot', 'joe')
    assert foo['bar']['baz']['doot'] == 'joe'

    foo = tree()
    set_tree_node(foo, 'bar:baz:doot', 'joe')
    set_tree_node(foo, 'bar:baz:doot', 'larry')
    assert foo['bar']['baz']['doot'] == 'larry'



# Generated at 2022-06-14 06:47:47.988055
# Unit test for function get_tree_node

# Generated at 2022-06-14 06:48:04.679175
# Unit test for function get_tree_node
def test_get_tree_node():
    a = {
        'a': {
            'b': {
                'c': 'd'
            },
            'e': {
                'f': 'g'
            }
        }
    }

    assert get_tree_node(a, 'a:b:c') == 'd'
    assert get_tree_node(a, 'a:e:f') == 'g'

    # Test default value
    # Error raised if default value == _sentinel
    assert get_tree_node(a, 'a:c:d', default=None) is None
    assert get_tree_node(a, 'a:c:d', default=_sentinel) is _sentinel

    with pytest.raises(KeyError):
        get_tree_node(a, 'a:c:d', default=_sentinel)

# Generated at 2022-06-14 06:48:14.514962
# Unit test for function get_tree_node
def test_get_tree_node():
    import pytest

    test_data = {
        "foo": {
            "bar": {
                "baz": 0
            },
            "qux": 1
        }
    }

    keys = {
        'foo:bar:baz': 0,
        'foo:bar': {'baz': 0},
        'foo:qux': 1,
        'foo:bar:baz:qux': None
    }

    for key, value in keys.items():

        try:
            result = get_tree_node(test_data, key, default=None)
        except KeyError as exc:
            pytest.fail(exc)

        assert result == value



# Generated at 2022-06-14 06:48:24.159902
# Unit test for function get_tree_node
def test_get_tree_node():
    """
    Unit test for function get_tree_node

    """
    # test simple dict
    mapping = {'k1': {'v1': {'k2': 'v2'}}}
    assert get_tree_node(mapping, 'k1:v1') == {'k2': 'v2'}
    assert get_tree_node(mapping, 'k1:v1:k2') == 'v2'
    assert get_tree_node(mapping, 'k1:v2') is None
    assert get_tree_node(mapping, 'k1:v2', default='v2') == 'v2'
    assert get_tree_node(mapping, 'k1:v2:k3') is None

# Generated at 2022-06-14 06:48:32.861781
# Unit test for function get_tree_node
def test_get_tree_node():
    t = {
        'a': {
            'b': {
                'c': 'd'
            }
        }
    }
    assert get_tree_node(t, 'a:b:c') == 'd'
    try:
        get_tree_node(t, 'a:e:c')
    except KeyError:
        pass
    else:
        raise AssertionError("Failed to raise KeyError on missing key")



# Generated at 2022-06-14 06:48:40.067903
# Unit test for function get_tree_node
def test_get_tree_node():
    with pytest.raises(KeyError):
        get_tree_node({}, 'test')

    tn = get_tree_node({'test': 'value'}, 'test')
    assert tn == 'value'

    tn = get_tree_node({'test': 'value'}, 'test', parent=True)
    assert tn == {}

    tn = get_tree_node({'test': 'value'}, 'test:foo')
    assert tn is _sentinel

    tn = get_tree_node({'test': 'value'}, 'test:foo', default=123)
    assert tn == 123

    tn = get_tree_node({'test': {'foo': 'bar'}}, 'test:foo', default=123)
    assert tn == 'bar'

    tn = get_

# Generated at 2022-06-14 06:48:52.864859
# Unit test for function get_tree_node
def test_get_tree_node():
    assert get_tree_node({'k': 'v'}, 'k') == 'v'
    assert get_tree_node({'k': {'k2': 'v'}}, 'k:k2') == 'v'
    assert get_tree_node({'k': {'k2': {'k3': 'v'}}}, 'k:k2:k3') == 'v'
    with pytest.raises(KeyError):
        assert get_tree_node({'k': {'k2': {'k3': 'v'}}}, 'k:k2:k4') == 'v'
    assert get_tree_node({'k': {'k2': {'k3': 'v'}}}, 'k:k2:k4', default=None) is None

# Generated at 2022-06-14 06:48:59.751751
# Unit test for function get_tree_node
def test_get_tree_node():
    test_obj = {
        'a': {
            'b': {
                'c': {
                    'd': 5
                }
            },
        },
    }
    assert get_tree_node(test_obj, 'a:b') == {'c': {'d': 5}}
    assert get_tree_node(test_obj, 'a:b:c') == {'d': 5}
    assert get_tree_node(test_obj, 'a:b:c:d') == 5

    assert get_tree_node(test_obj, 'a:b:c:d:f', default=None) is None
    try:
        get_tree_node(test_obj, 'a:b:c:d:f')
    except KeyError:
        pass

# Generated at 2022-06-14 06:49:09.790104
# Unit test for function get_tree_node
def test_get_tree_node():
    assert get_tree_node({'foo': 'bar'}, 'foo') == 'bar'
    with pytest.raises(KeyError):
        get_tree_node({'foo': 'bar'}, 'baz')
    assert get_tree_node({'foo': 'bar'}, 'baz', default=None) is None
    assert get_tree_node({'foo': {'bar': 1}}, 'foo:bar') == 1
    assert get_tree_node({'foo': {'bar': {'baz': None}}}, 'foo:bar:baz') is None



# Generated at 2022-06-14 06:49:16.759602
# Unit test for function get_tree_node
def test_get_tree_node():
    """
    Unit test for `get_tree_node`
    """
    test_dict = {
        'a': {'b': {'c': 'd'}},
        'x': {'y': {'z': 'a'}}
    }
    assert get_tree_node(test_dict, 'x:y:z') == 'a'
    return 0

# Generated at 2022-06-14 06:49:25.906259
# Unit test for function set_tree_node
def test_set_tree_node():
    # tree = {}
    tree = collections.defaultdict(tree)
    set_tree_node(tree, 'a', {})
    set_tree_node(tree, 'a:b', {})
    set_tree_node(tree, 'a:c', {})
    set_tree_node(tree, 'a:b:c:d:a:b:c', True)
    assert tree['a']['b']['c']['d']['a']['b']['c'] is True
    return tree



# Generated at 2022-06-14 06:49:39.071701
# Unit test for function set_tree_node
def test_set_tree_node():
    registry = collections.defaultdict(dict)
    set_tree_node(registry, 'foo:bar', 1)
    assert registry['foo']['bar'] == 1
    set_tree_node(registry, 'foo:bar', None)
    assert 'bar' not in registry['foo']

# Generated at 2022-06-14 06:49:41.038973
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = tree()
    get_tree_node(mapping, 'a')



# Generated at 2022-06-14 06:49:53.664643
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = {
        'a': {
            'b': {1, 2, 3},
            'c': {4, 5, 6},
        },
        'c':
        {7, 8, 9}
    }
    assert get_tree_node(mapping, 'a:b:1', default=_sentinel) == 1
    assert get_tree_node(mapping, 'a:c:5', default=_sentinel) == 5
    assert get_tree_node(mapping, 'c:8', default=_sentinel) == 8
    assert get_tree_node(mapping, 'c:9', default=_sentinel) == 9
    assert get_tree_node(mapping, 'c:10', default=_sentinel) is _sentinel

# Generated at 2022-06-14 06:50:00.673700
# Unit test for function set_tree_node
def test_set_tree_node():
    """Test setting a tree node."""
    tree = {}
    set_tree_node(tree, 'test', 'TESTTESTTEST')
    assert tree == {'test': 'TESTTESTTEST'}

    set_tree_node(tree, 'test2:test2', 'TESTTESTTEST')
    assert tree == {'test': 'TESTTESTTEST', 'test2': {'test2': 'TESTTESTTEST'}}

    set_tree_node(tree, 'test2:test2:test2', 'TESTTESTTEST')
    assert tree == {'test': 'TESTTESTTEST', 'test2': {'test2': {'test2': 'TESTTESTTEST'}}}


# Generated at 2022-06-14 06:50:13.348812
# Unit test for function get_tree_node
def test_get_tree_node():
    from nose.tools import assert_true, assert_equal, assert_raises
    import logging
    logging.basicConfig(format='%(message)s', level=logging.DEBUG)

    test_tree = tree()
    test_tree['a']['b']['c'] = 'd'
    x = get_tree_node(test_tree, 'a:b:c')
    # print(x)
    assert_equal(x, 'd')

    test_tree = tree()
    test_tree['a']['b']['c'] = 'd'
    # print(get_tree_node(test_tree, 'b'))
    assert_equal(get_tree_node(test_tree, 'b'), _sentinel)

    test_tree = tree()

# Generated at 2022-06-14 06:50:17.160487
# Unit test for function set_tree_node
def test_set_tree_node():
    x = {}

    set_tree_node(x, 'a:b:c:d', True)
    assert x['a']['b']['c']['d'] is True



# Generated at 2022-06-14 06:50:21.081705
# Unit test for function set_tree_node
def test_set_tree_node():
    tree = {}
    set_tree_node(tree, 'foo:bar:baz', 'dave')
    assert tree['foo']['bar']['baz'] == 'dave'



# Generated at 2022-06-14 06:50:30.877423
# Unit test for function get_tree_node
def test_get_tree_node():
    data = {
        'a': {
            'b': {
                'c': 'c',
                'd': {
                    'e': 'e',
                    'f': 'f',
                },
            },
        },
    }
    # Path to `c`
    assert get_tree_node(data, 'a:b:c') == 'c'
    # Path to `e`
    assert get_tree_node(data, 'a:b:d:e') == 'e'
    try:
        get_tree_node(data, 'a:b:q')
    except KeyError:
        pass
    else:
        raise AssertionError('Nonexistent path should raise KeyError')



# Generated at 2022-06-14 06:50:41.096203
# Unit test for function get_tree_node
def test_get_tree_node():
    assert get_tree_node({}, 'foo') == {}
    assert get_tree_node({'a': 'b'}, 'a') == 'b'
    # Test it raises an error properly
    with pytest.raises(KeyError):
        get_tree_node({'a': 'b'}, 'c')

    # Test for parent node
    assert get_tree_node({'a': 'b', 'c': {'d': 'e'}}, 'c:d', parent=True) == {'d': 'e'}

# Generated at 2022-06-14 06:50:49.220137
# Unit test for function get_tree_node
def test_get_tree_node():
    assert get_tree_node({'a': 1}, 'a') == 1
    assert get_tree_node({'a': {'b': 2}}, 'a:b') == 2
    assert get_tree_node({'a': {'b': {'c': 3}}}, 'a:b:c') == 3
    assert get_tree_node({'a': {'b': {'c': 3}}}, 'a:b:c:d') is _sentinel



# Generated at 2022-06-14 06:51:02.151815
# Unit test for function set_tree_node
def test_set_tree_node():
    t = tree()
    set_tree_node(t, 'a:b:c', 'foo value')
    assert t['a']['b']['c'] == 'foo value'



# Generated at 2022-06-14 06:51:14.098789
# Unit test for function get_tree_node
def test_get_tree_node():
    my_dict = {
        'a': 1,
        'b': 2,
        'c': {
            'd': 3,
            'e': {
                'f': 4,
                'g': 5,
                'h': {
                    'i': 6,
                    'j': 7
                }
            }
        }
    }
    assert get_tree_node(my_dict, 'c:e:h:i') == 6
    assert get_tree_node(my_dict, 'c:e:h:i', parent=True) == {
        'i': 6,
        'j': 7
    }
    assert get_tree_node(my_dict, 'c:e:h:i:j', parent=True) == {
        'i': 6,
        'j': 7
    }



# Generated at 2022-06-14 06:51:21.690834
# Unit test for function get_tree_node
def test_get_tree_node():

    # 1 Dimensional
    assert get_tree_node({'a': 'b'}, 'a') == 'b'

    # 2 Dimensional
    assert get_tree_node({'a': {'b': 'c'}}, 'a:b') == 'c'

    # 3 Dimensional
    assert get_tree_node({'a': {'b': {'c': 'd'}}}, 'a:b:c') == 'd'

    # 4 Dimensional
    assert get_tree_node({'a': {'b': {'c': {'d': 'e'}}}}, 'a:b:c:d') == 'e'

    # 5 Dimensional

# Generated at 2022-06-14 06:51:32.389610
# Unit test for function get_tree_node
def test_get_tree_node():
    assert get_tree_node({'foo': {'bar': {'baz': 'xyz'}}}, 'foo:bar:baz') == 'xyz'
    assert get_tree_node({'foo': {'bar': {'baz': 'xyz'}}}, 'foo:bar:baz', default='nope') == 'xyz'
    assert get_tree_node({'foo': {'bar': {'baz': 'xyz'}}}, 'foo:bar:baz', parent=True) == {'baz': 'xyz'}
    assert get_tree_node({'foo': {'bar': {'baz': 'xyz'}}}, 'foo:bar:baz', parent=True, default='nope') == {'baz': 'xyz'}

# Generated at 2022-06-14 06:51:42.982407
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = {
        'dimension1': {
            'dimension2': {
                'bob': 'hello',
                'joe': 'world'
            }
        }
    }
    assert get_tree_node(mapping, 'dimension1:dimension2:bob') == 'hello'
    assert get_tree_node(mapping, 'dimension1:dimension2:joe') == 'world'
    assert get_tree_node(mapping, 'dimension1:dimension2:jim') == _sentinel
    try:
        get_tree_node(mapping, 'dimension1:dimension2:jim')
    except KeyError:
        pass



# Generated at 2022-06-14 06:51:55.434614
# Unit test for function get_tree_node
def test_get_tree_node():
    tree = {
        'node1': {
            'node1_1': 'node1_1',
            'node1_2': {
                'node1_2_1': 'node1_2_1',
                'node1_2_2': 'node1_2_2',
            }
        },
        'node2': 'node2'
    }
    assert get_tree_node(tree, 'node1:node1_2:node1_2_2') == 'node1_2_2'
    assert get_tree_node(tree, 'node1:node1_2:node1_2_2', default=None) == 'node1_2_2'
    assert get_tree_node(tree, 'node1:node1_2:node1_2_4', default=None) is None


# Generated at 2022-06-14 06:52:05.516572
# Unit test for function get_tree_node
def test_get_tree_node():
    x = {'testing': {'testing_again': 'foo'}}
    assert get_tree_node(x, 'testing:testing_again') == 'foo'
    assert get_tree_node(x, 'testing:testing_again', parent=True) == {'testing_again': 'foo'}
    assert get_tree_node(x, 'testing:testing_again', default='bar') == 'foo'
    assert get_tree_node(x, 'does:not:exist:at:all', default='bar') == 'bar'
    assert get_tree_node(x, 'does:not:exist:at:all') == KeyError


if __name__ == "__main__":
    test_get_tree_node()

# Generated at 2022-06-14 06:52:09.276279
# Unit test for function set_tree_node
def test_set_tree_node():
    test = tree()
    assert set_tree_node(test, 'foo:bar:baz', 'Hello') == {'bar': {'baz': 'Hello'}}



# Generated at 2022-06-14 06:52:19.963271
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = {'users': {'bob': 'password', 'joe': 'drowssap'}}
    assert 'password' == get_tree_node(mapping, 'users:bob')
    assert 'drowssap' == get_tree_node(mapping, 'users:joe')

    # Test parent node
    assert get_tree_node(mapping, 'users:joe', parent=True) == {'joe': 'drowssap'}

    # Test key doesn't exist
    with pytest.raises(KeyError):
        get_tree_node(mapping, 'nope:nope')

    # Test default
    assert 'default' == get_tree_node(mapping, 'nope:nope', default='default')



# Generated at 2022-06-14 06:52:31.001394
# Unit test for function get_tree_node
def test_get_tree_node():
    import seaborn
    seaborn.set()
    import matplotlib.pyplot as plt

    tree = {
        'a': {
            'b': {
                'c': 1,
                'd': 2
            },
            'e': {
                'f': 3
            }
        },
        'g': {
            'h': {
                'i': 4
            },
            'j': 5
        }
    }

    plt.figure()
    plt.subplot(121)

    plt.title('get_tree_node test')
    plt.xlabel('treelib.get_tree_node')
    plt.ylabel('Result')

# Generated at 2022-06-14 06:53:05.246540
# Unit test for function set_tree_node
def test_set_tree_node():
    """
    Test function `set_tree_node` to ensure it does the right thing.
    """
    root = Tree()
    child = set_tree_node(root, 'a:b:c:d:e:f', 'value')
    assert child['f'] == 'value'
    assert root['a:b:c:d:e:f'] == 'value'

    # Set a key on a previously set tree node by passing it as the mapping
    set_tree_node(child, 'g', 'value2')
    assert child['g'] == 'value2'
    assert root['a:b:c:d:e:f:g'] == 'value2'



# Generated at 2022-06-14 06:53:10.645237
# Unit test for function set_tree_node
def test_set_tree_node():
    """
    Tests set_tree_node.
    """
    my_tree = tree()
    set_tree_node(my_tree, 'foo:bar:baz:brrr', 'value')
    assert my_tree['foo']['bar']['baz']['brrr'] == 'value'



# Generated at 2022-06-14 06:53:20.414249
# Unit test for function get_tree_node
def test_get_tree_node():
    """
    Fetch arbitrary node from a tree-like mapping structure with traversal help:
    Dimension can be specified via ':'

    Arguments:
        mapping collections.Mapping: Mapping to fetch from
        key str|unicode: Key to lookup, allowing for : notation
        default object: Default value. If set to `:module:_sentinel`, raise KeyError if not found.
        parent bool: If True, return parent node. Defaults to False.

    Returns:
        object: Value at specified key
    """
    o = {'a': {'b': {'c': 'd'}}}
    assert get_tree_node(o, 'a') == {'b': {'c': 'd'}}
    assert get_tree_node(o, 'a:b') == {'c': 'd'}
    assert get_tree

# Generated at 2022-06-14 06:53:33.709829
# Unit test for function set_tree_node
def test_set_tree_node():
    m = {}
    assert set_tree_node(m, 'foo', 'bar') == {'foo': 'bar'}
    assert m == {'foo': 'bar'}
    assert set_tree_node(m, 'foo', 'bar2') == {'foo': 'bar2'}
    assert m == {'foo': 'bar2'}
    assert set_tree_node(m, 'foo:foo2', 'bar') == {'foo': 'bar2', 'foo2': 'bar'}
    assert m == {'foo': 'bar2', 'foo2': 'bar'}
    assert set_tree_node(m, 'foo:foo2', 'bar2') == {'foo': 'bar2', 'foo2': 'bar2'}

# Generated at 2022-06-14 06:53:41.524951
# Unit test for function get_tree_node
def test_get_tree_node():
    sample_data = tree()
    sample_data['a:b'] = 'a:b'
    sample_data['a:c'] = 'a:c'
    sample_data['d'] = 'd'
    sample_data['e'] = 'e'

    assert get_tree_node(sample_data, 'a:b') == 'a:b'
    assert get_tree_node(sample_data, 'a:c') == 'a:c'
    assert get_tree_node(sample_data, 'd') == 'd'
    assert get_tree_node(sample_data, 'e') == 'e'
    with pytest.raises(KeyError):
        get_tree_node(sample_data, 'a:c:d')
    with pytest.raises(KeyError):
        get_tree

# Generated at 2022-06-14 06:53:51.400827
# Unit test for function get_tree_node
def test_get_tree_node():
    data = tree()
    data['test']['test']['test']['test'] = 1337
    assert get_tree_node(data, 'test:test:test:test') == 1337
    assert get_tree_node(data, 'test:test:test:test', default=1) == 1337
    assert get_tree_node(data, 'test:test:test:test2', default=1) == 1
    assert get_tree_node(data, 'test:test:test:test2') == KeyError



# Generated at 2022-06-14 06:54:00.480516
# Unit test for function get_tree_node
def test_get_tree_node():
    tree_dict = {
        'a': {'a': 1, 'b': 2, 'c': 3, 'd': {'a': 1, 'b': 2, 'c': 3}},
        'b': {'a': 1, 'b': 2, 'c': 3, 'd': {'a': 1, 'b': 2, 'c': 3}},
        'c': {'a': 1, 'b': 2, 'c': 3, 'd': {'a': 1, 'b': 2, 'c': 3}},
        'd': {'a': 1, 'b': 2, 'c': 3, 'd': {'a': 1, 'b': 2, 'c': 3}},
    }
    assert get_tree_node(tree_dict, 'a:a') == 1
    assert get_tree

# Generated at 2022-06-14 06:54:07.548512
# Unit test for function get_tree_node
def test_get_tree_node():
    tree_list = tree()
    tree_list['a']['b']['c'] = True
    tree_list['a']['d']['f'] = True
    tree_list['e'] = True
    # Test 1
    assert get_tree_node(tree_list, 'e') is True
    assert get_tree_node(tree_list, 'e', default=None) is True

    # Test 2
    assert get_tree_node(tree_list, 'a:b:c') is True
    assert get_tree_node(tree_list, 'a:b:c', default=None) is True

    # Test 3
    assert get_tree_node(tree_list, 'a:d:f') is True

# Generated at 2022-06-14 06:54:17.399311
# Unit test for function set_tree_node
def test_set_tree_node():
    test_tree = tree()
    test_tree['a_key'] = 'a_value'
    set_tree_node(test_tree, 'a_key2', 'a_value2')
    assert test_tree['a_key'] == 'a_value'
    assert test_tree['a_key2'] == 'a_value2'

    test_tree = tree()
    set_tree_node(test_tree, 'a:b:c:d:key', 'value')
    assert test_tree['a']['b']['c']['d']['key'] == 'value'



# Generated at 2022-06-14 06:54:27.354019
# Unit test for function get_tree_node
def test_get_tree_node():
    """
    Test suite for function :function:`get_tree_node`
    """
    base_tree = {
        'a': {
            'b': {
                'c': 'd'
            },
            'd': {
                'e': 'f'
            }
        }
    }
    assert get_tree_node(base_tree, 'a:b:c') == 'd'
    assert get_tree_node(base_tree, 'a:d:e') == 'f'
    assert get_tree_node(base_tree, 'a:d:e:f') == 'f'
    assert get_tree_node(base_tree, 'a:d:e:f', default='g') == 'g'

# Generated at 2022-06-14 06:55:16.566807
# Unit test for function get_tree_node
def test_get_tree_node():
    class A(object):
        pass

    a = A()
    a.b = A()
    a.b.c = A()
    a.b.c.d = 1

    # Correct usage
    assert get_tree_node(a, 'b:c') is a.b.c
    assert get_tree_node(a, 'b:c:d') == 1

    # Incorrect usage
    with pytest.raises(AttributeError):
        assert get_tree_node(a, 'e')
    with pytest.raises(AttributeError):
        assert get_tree_node(a, 'b:e')
    with pytest.raises(AttributeError):
        assert get_tree_node(a, 'b:c:e')

    # Incorrect usage with default

# Generated at 2022-06-14 06:55:22.346135
# Unit test for function get_tree_node
def test_get_tree_node():
    data = {
        'key_one': {
            'key_two': {
                'key_three': 3
            }
        }
    }

    assert get_tree_node(data, 'key_one:key_two:key_three') == 3
    assert get_tree_node(data, 'key_one:key_two:key_three:key_four', default=4) == 4



# Generated at 2022-06-14 06:55:29.902030
# Unit test for function set_tree_node
def test_set_tree_node():
    from copy import copy
    d = Tree()
    d = set_tree_node(d, 'a:b:c:d:e:f', 'g')
    assert(d['a']['b']['c']['d']['e']['f'] == 'g')
    _d = copy(d)
    _d['a']['b']['c']['d']['e']['f'] = 'g2'
    assert(d == _d)



# Generated at 2022-06-14 06:55:41.083441
# Unit test for function set_tree_node
def test_set_tree_node():
    mapping = {}
    set_tree_node(mapping, 'abc:def', 'ghi')
    assert mapping == {
        'abc': {'def': 'ghi'}
    }

    # Test with missing keys
    mapping = collections.defaultdict(dict)
    set_tree_node(mapping, 'abc:def', 'ghi')
    assert mapping == {
        'abc': {'def': 'ghi'}
    }

    # Test with existing keys
    mapping = collections.defaultdict(dict, abc={})
    set_tree_node(mapping, 'abc:def', 'ghi')
    assert mapping == {
        'abc': {'def': 'ghi'}
    }


# Generated at 2022-06-14 06:55:43.955166
# Unit test for function get_tree_node
def test_get_tree_node():
    assert get_tree_node(
        {'users': {
            'tom': 'likes cheese'
        }},
        'users:tom'
    ) == 'likes cheese'



# Generated at 2022-06-14 06:55:57.245070
# Unit test for function get_tree_node
def test_get_tree_node():
    fixture = {
        "foo": {
            "bar": {
                "baz": True,
            },
        },
    }

    # Basic key fetching
    assert get_tree_node(fixture, 'foo:bar:baz')

    # Fetching missing key should raise KeyError
    with pytest.raises(KeyError) as exc:
        get_tree_node(fixture, 'foo:baz')
    assert "'foo:baz'" in str(exc.value)
    assert exc.value.args[0] == 'foo:baz'

    # Fetching missing key with default should return default
    assert get_tree_node(fixture, 'foo:baz', default=False) is False

    # Fetching parent node

# Generated at 2022-06-14 06:56:08.155588
# Unit test for function set_tree_node
def test_set_tree_node():
    t = tree()
    set_tree_node(t, 'a:b:c', 1)
    # print "Setting root node to 1..."
    t['a']['b']['c'] = 1
    assert t['a']['b']['c'] == 1
    # print "Setting root node to 2..."
    t['a']['b']['c'] = 2
    assert t['a']['b']['c'] == 2
    # print "Checking root node is 2..."
    assert t['a']['b']['c'] == 2
    # print "Checking root node is 1..."
    assert t['a']['b']['c'] != 1
    # print "Checking root node is 2..."
    assert t['a']['b']['c'] == 2