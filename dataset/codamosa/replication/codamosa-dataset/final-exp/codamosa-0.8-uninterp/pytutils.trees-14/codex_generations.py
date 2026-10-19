

# Generated at 2022-06-14 06:46:14.814026
# Unit test for function set_tree_node
def test_set_tree_node():
    my_dict = {}
    set_tree_node(my_dict, 'a:b:c', 'hello')
    assert my_dict == {'a': {'b': {'c': 'hello'}}}, "set_tree_node() should set the new tree node."



# Generated at 2022-06-14 06:46:28.598862
# Unit test for function get_tree_node
def test_get_tree_node():
    """Tests for `get_tree_node`"""
    from nose.tools import assert_equals
    from nose.tools import assert_raises
    from nose.tools import assert_true
    from nose.tools import assert_is
    from nose.tools import assert_false

    # Test for existing keys
    mapping = {
        'foo': {
            'bar': 'baz',
        },
    }
    assert_equals(get_tree_node(mapping, 'foo:bar'), 'baz')
    assert_equals(get_tree_node(mapping, 'foo:bar', default=None), 'baz')
    assert_true(get_tree_node(mapping, 'foo:bar', default=None) is not None)

# Generated at 2022-06-14 06:46:34.559479
# Unit test for function get_tree_node
def test_get_tree_node():
    tree = {
        'one':
            {'two':
                 {'three': 'four'}
             },
        'five': 'six'
    }

    assert get_tree_node(tree, 'one:two:three') == 'four'
    assert get_tree_node(tree, 'one:two', parent=True) == {'two': {'three': 'four'}}



# Generated at 2022-06-14 06:46:47.135115
# Unit test for function set_tree_node
def test_set_tree_node():
    data = {}
    set_tree_node(data, 'foo', 'bar')
    assert data['foo'] == 'bar'

    set_tree_node(data, 'bar', 'baz')
    assert data['bar'] == 'baz'

    data = {}
    set_tree_node(data, 'foo:bar', 'baz')
    assert data['foo']['bar'] == 'baz'

    data = {}
    set_tree_node(data, 'foo:bar:baz', [1, 2, 3])
    assert data['foo']['bar']['baz'] == [1, 2, 3]

    data = {}
    set_tree_node(data, 'foo', {'bar': 'baz'})
    assert data['foo']['bar'] == 'baz'

# Generated at 2022-06-14 06:46:57.279951
# Unit test for constructor of class RegistryTree
def test_RegistryTree():
    """
    Test that `RegistryTree`'s constructor is sane.
    """
    from six import PY3
    from copy import copy

    if PY3:
        from importlib import reload

    # Ensure that a namespace is supplied to __init__, and works
    t = RegistryTree(namespace='foo')
    t.register(':bar', 'baz')
    assert t.get(':') == {'bar': 'baz'}

    # Test if updating a namespace works
    t.namespace = 'bar'
    t.register(':', 'bar')
    t.register(':foo', 'baz')
    assert t.get(':') == {'bar': 'foo', 'foo': 'baz'}

    t.register(':foo:bar:baz', 'bar')
    assert t.get

# Generated at 2022-06-14 06:47:08.079731
# Unit test for function get_tree_node

# Generated at 2022-06-14 06:47:21.314122
# Unit test for function get_tree_node
def test_get_tree_node():
    """Test :func:`get_tree_node`"""
    # Setup test data
    test_data = tree()
    test_data['one']['two']['three'] = 'four'

    # Test single-dimension access
    assert get_tree_node(test_data, 'one') == {'two': {'three': 'four'}}
    assert get_tree_node(test_data, 'nonexistent') is _sentinel

    # Test multi-dimension access
    assert get_tree_node(test_data, 'one:two:three') == 'four'
    assert get_tree_node(test_data, 'nonexistent:one:two:three') is _sentinel
    assert get_tree_node(test_data, 'one:nonexistent:two') is _sentinel

    # Test parent node

# Generated at 2022-06-14 06:47:33.682512
# Unit test for function get_tree_node
def test_get_tree_node():
    """Test function :func:`get_tree_node`"""
    from nose.tools import assert_equal
    from librarian.core.utils import tree

    data = tree(initial={
        'a': {
            'b': {
                'c': 'd',
                'e': 'f'
            }
        }
    })

    # No namespace
    assert_equal(get_tree_node(data, 'a:b:c'), 'd')
    assert_equal(get_tree_node(data, 'a:b:e'), 'f')
    # Namespace
    assert_equal(get_tree_node(data, 'b:c', namespace='a'), 'd')
    assert_equal(get_tree_node(data, 'b:e', namespace='a'), 'f')



# Generated at 2022-06-14 06:47:42.092589
# Unit test for function get_tree_node
def test_get_tree_node():
    node = get_tree_node({'a': {'b': 2}}, 'a:b')
    assert node == 2

    node = get_tree_node({'a': {'b': 2}}, 'a:c')
    assert node is _sentinel

    # With keyerror suppressed
    node = get_tree_node({'a': {'b': 2}}, 'a:c', default=None)
    assert node is None



# Generated at 2022-06-14 06:47:44.792868
# Unit test for constructor of class Tree
def test_Tree():
    test = Tree()
    assert test == {u'namespace': None}
    assert test.namespace == None


# Generated at 2022-06-14 06:48:03.432828
# Unit test for function get_tree_node
def test_get_tree_node():
    """Test tree node getter."""
    test_data = {
        'foo': {
            'bar': {
                'baz': 42
            }
        }
    }
    assert get_tree_node(test_data, 'foo:bar:baz') == 42
    assert get_tree_node(test_data, 'foo:bar') == {'baz': 42}
    assert get_tree_node(test_data, 'foo:bar:baz', default='asdf') == 42
    assert get_tree_node(test_data, 'foo:bar:baz:asdf') is None
    assert get_tree_node(test_data, 'foo:bar:baz:asdf', default='asdf') == 'asdf'



# Generated at 2022-06-14 06:48:15.218714
# Unit test for function set_tree_node
def test_set_tree_node():
    x = {}
    assert set_tree_node(x, 'a:b:c', 3) == {'a': {'b': {'c': 3}}}
    assert set_tree_node(x, 'a:b:c:d', 4) == {'a': {'b': {'c': {'d': 4}}}}
    assert set_tree_node(x, 'foo:bar:baz', 'qux') == {'foo': {'bar': {'baz': 'qux'}}}
    assert set_tree_node(x, 'foo:bar', [1, 2, 3]) == {'foo': {'bar': [1, 2, 3]}}

# Generated at 2022-06-14 06:48:22.367094
# Unit test for function set_tree_node
def test_set_tree_node():
    # GIVEN
    test_tree_dict = {
        'test1': {},
        'test2': {
            'test2_a': {},
            'test2_b': [],
        },
        'test3': True,
    }
    test_tree = set_tree_node(test_tree_dict, 'test4:test4_a:test4_a_1', True)
    assert test_tree is test_tree_dict['test4']



# Generated at 2022-06-14 06:48:31.456160
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = tree()
    mapping['foo']['bar'] = 'baz'
    assert 'foo' == get_tree_node(mapping, 'foo')
    assert 'baz' == get_tree_node(mapping, 'foo:bar')

    try:
        get_tree_node(mapping, 'foo:quux')
        assert False
    except KeyError:
        assert True

    assert None is get_tree_node(mapping, 'foo:quux', default=None)



# Generated at 2022-06-14 06:48:39.045115
# Unit test for function get_tree_node
def test_get_tree_node():
    tree = {'a': {'b': {'c': 'foo'}}}
    assert get_tree_node(tree, 'a:b') is tree['a']
    assert get_tree_node(tree, 'a:b:c') is 'foo'
    assert get_tree_node(tree, 'a:b:does_not_exist') is _sentinel
    assert get_tree_node(tree, 'a:b:does_not_exist', default='bar') is 'bar'

# Generated at 2022-06-14 06:48:44.658865
# Unit test for function get_tree_node
def test_get_tree_node():
    assert get_tree_node({'pokemon': {'charmander': 'dragon'}}, 'pokemon:charmander') == 'dragon'
    assert get_tree_node({'pokemon': {'charmander': 'dragon'}}, 'pokemon:charmander:flame') is _sentinel



# Generated at 2022-06-14 06:48:56.213268
# Unit test for function get_tree_node
def test_get_tree_node():
    """
    Tests for get_tree_node. Tree structure is as follows.

    .. code-block:: python

        tree = {
            '1': 'a1',
            '2': {
                '2.1': 'a2.1',
                '2.2': 'a2.2'
            }
        }

    """
    tree = {
        '1': 'a1',
        '2': {
            '2.1': 'a2.1',
            '2.2': 'a2.2'
        }
    }
    # Simple flat lookup
    assert get_tree_node(tree, '1') == 'a1'
    # Nested lookup
    assert get_tree_node(tree, '2:2.1') == 'a2.1'
    # No key. Should raise KeyError

# Generated at 2022-06-14 06:49:02.922231
# Unit test for function set_tree_node
def test_set_tree_node():
    input_dict = {
        'things': {
            'a': {
                'foo': 'bar',
            },
            'b': {
                'foo': 'baz',
            },
        },
        'stuff': 'cool',
    }

    output_dict = set_tree_node(input_dict, 'stuff:foo', 'yep')
    assert output_dict == input_dict['stuff']

# Generated at 2022-06-14 06:49:13.873848
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = {
        'foo': 'bar',
        'one': {
            'two': {
                'three': {
                    'four': 'bing',
                    'five': 'bong',
                },
            },
        },
        'bar': {
            'baz': 'bing'
        }
    }

    assert get_tree_node(mapping, 'foo') == 'bar'
    assert get_tree_node(mapping, 'one:two:three:four') == 'bing'
    assert get_tree_node(mapping, 'foo:bar:baz') == collections.defaultdict(dict, {'foo': 'bar', 'bar': {'baz': 'bing'}})

# Generated at 2022-06-14 06:49:26.824757
# Unit test for function get_tree_node
def test_get_tree_node():
    """
    Test function get_tree_node

    Returns:
        int: Number of failed tests (0 = succes)
    """
    import sys
    import nose
    import types

    # Mock up the data
    tree_data = {
        'main': {
            'fantasy': {
                'dragon': {
                    'color': 'green'
                },
                'unicorn': {
                    'color': 'white'
                }
            }
        },
        'deeply_nested': 'deeply_nested_value',
        'not_deeply_nested': 'not_deeply_nested_value'
    }

    # First assert, an exact match

# Generated at 2022-06-14 06:49:37.335766
# Unit test for function get_tree_node
def test_get_tree_node():
    assert get_tree_node({'a': {'': {'b': 2}}}, 'a:b') == 2
    assert get_tree_node({'a': {'': {'b': 2}}}, 'a:b:c', default='d') == 'd'
    assert get_tree_node({'a': {'': {'b': 2}}}, 'a:b:c', default='d', parent=True) == {'c': 'd'}

# Generated at 2022-06-14 06:49:45.566181
# Unit test for function get_tree_node
def test_get_tree_node():
    registry = collections.defaultdict(dict)

    registry['foo'] = 'bar'
    registry['a']['b']['c'] = 'd'

    assert get_tree_node(registry, 'foo') == 'bar'
    assert get_tree_node(registry, 'a:b:c') == 'd'
    # TODO Test default
    # with pytest.raises(KeyError) as exc:
    #     get_tree_node(registry, 'a:b:e')
    try:
        get_tree_node(registry, 'a:b:e')
    except KeyError as exc:
        pass


if __name__ == '__main__':
    test_get_tree_node()

# Generated at 2022-06-14 06:49:57.107531
# Unit test for function get_tree_node
def test_get_tree_node():
    # create test tree
    tree = {
        '1': {'2': {
            '3': {'4': '4'},
            '5': '5'
        }}
    }

    # test when all levels exist
    assert get_tree_node(
        tree, '1:2:3:4') == '4'

    # test when a level does not exist
    with pytest.raises(KeyError):
        get_tree_node(tree, '1:2:3:4:5')

    # test when a level does not exist and default is specified
    assert get_tree_node(
        tree, '1:2:3:4:5:6:7',
        default='default') == 'default'

    # test when a level does not exist and default is specified

# Generated at 2022-06-14 06:50:02.465649
# Unit test for function get_tree_node
def test_get_tree_node():
    assert (get_tree_node({'a': {'b': 1}}, 'a:b') == 1)
    assert (get_tree_node({'a': {'b': 1}}, 'a:b', parent=True) == {'b': 1})

# Generated at 2022-06-14 06:50:07.995851
# Unit test for function get_tree_node
def test_get_tree_node():
    obj = {
        'foo': {'bar': 'baz'},
    }
    assert get_tree_node(obj, 'foo:bar') == 'baz'
    assert get_tree_node(obj, 'foo:baz', default='not found') == 'not found'



# Generated at 2022-06-14 06:50:12.063511
# Unit test for function get_tree_node
def test_get_tree_node():
    assert get_tree_node({'a': {'b': {'c': 'd'}}}, 'a:b:c') == 'd'



# Generated at 2022-06-14 06:50:25.745624
# Unit test for function get_tree_node
def test_get_tree_node():
    test_tree = tree()
    test_tree['a'] = {'b': {'c': 'd'}}
    assert get_tree_node(test_tree, 'a') == {'b': {'c': 'd'}}
    assert get_tree_node(test_tree, 'a:b') == {'c': 'd'}
    assert get_tree_node(test_tree, 'a:b:c') == 'd'
    assert get_tree_node(test_tree, 'a:b:c', parent=True) == {'c': 'd'}
    assert get_tree_node(test_tree, 'a:b:c', default='default') == 'd'
    assert get_tree_node(test_tree, 'a:b:c:d', default='default') == 'default'

# Generated at 2022-06-14 06:50:30.055889
# Unit test for function get_tree_node
def test_get_tree_node():
    from pprint import pprint as pp
    mapping = {
        'a': {
            'b': {
                'c': 'val'
            }
        }
    }
    assert get_tree_node(mapping, 'a:b:c') == 'val'



# Generated at 2022-06-14 06:50:43.580716
# Unit test for function get_tree_node
def test_get_tree_node():
    from pytest import raises
    from pprint import pprint

    test_data = {'a': {'1': '2', '3': '4', '5': {'6': '7'}}}

    # Basic access
    assert get_tree_node(test_data, 'a:1', default='default') == '2'

    # Default value
    assert get_tree_node(test_data, 'a:2', default='default') == 'default'
    with raises(KeyError):
        get_tree_node(test_data, 'a:2', default=_sentinel)
    with raises(KeyError):
        get_tree_node(test_data, 'a:2')

    # Traverse

# Generated at 2022-06-14 06:50:48.148541
# Unit test for function set_tree_node
def test_set_tree_node():
    tree = {'a': {}}
    set_tree_node(tree, 'a:b:c', 'value')
    assert tree == {'a': {'b': {'c': 'value'}}}



# Generated at 2022-06-14 06:51:03.878475
# Unit test for function set_tree_node
def test_set_tree_node():
    test_data = tree()
    test_data['a']['b']['c'] = 1
    assert test_data['a']['b']['c'] == 1
    set_tree_node(test_data, 'a:b:c', 2)
    assert test_data['a']['b']['c'] == 2
    assert set_tree_node(test_data, 'a:b:c', 3)['c'] == 3



# Generated at 2022-06-14 06:51:12.767071
# Unit test for function get_tree_node
def test_get_tree_node():
    """
    Unit test for `get_tree_node`.
    """
    tree = {'A': {'1': 1, '2': 2}}
    get_tree_node(tree, 'A:1') == 1
    get_tree_node(tree, 'A:2') == 2
    get_tree_node(tree, 'A:1:1', default=False) is False
    assert_raises(KeyError, get_tree_node, tree, 'A:3')


if __name__ == '__main__':
    import nose
    nose.runmodule()

# Generated at 2022-06-14 06:51:19.756386
# Unit test for function set_tree_node
def test_set_tree_node():
    d = tree()
    set_tree_node(d, 'foo:bar', 'baz')
    assert d['foo']['bar'] == 'baz'
    set_tree_node(d, 'foo:bar:baz:quux', 'quiiii')
    assert d['foo']['bar']['baz']['quux'] == 'quiiii'



# Generated at 2022-06-14 06:51:22.175899
# Unit test for function get_tree_node
def test_get_tree_node():
    value = get_tree_node({'foo': {'bar': 'baz'}}, 'foo:bar')
    assert value == 'baz'



# Generated at 2022-06-14 06:51:26.367726
# Unit test for function get_tree_node
def test_get_tree_node():
    s = {'foo': {'bar': 'spam'}}
    assert get_tree_node(s, 'foo:bar') == 'spam'
    assert get_tree_node(s, 'foo:bar:not:real') is _sentinel



# Generated at 2022-06-14 06:51:32.878793
# Unit test for function set_tree_node
def test_set_tree_node():
    mapping = tree()
    set_tree_node(mapping, 'test:test2:test3', 23)
    assert 'test' in mapping, "test not in mapping"
    assert 'test2' in mapping['test'], "test2 not in mapping"
    assert 'test3' in mapping['test']['test2'], "test3 not in mapping"
    assert mapping['test']['test2']['test3'] == 23, "Wrong value returned"



# Generated at 2022-06-14 06:51:44.420241
# Unit test for function set_tree_node
def test_set_tree_node():
    a = tree()
    set_tree_node(a, "key", "value")
    assert (a['key'] == "value")
    set_tree_node(a, "key:key2", "value2")
    assert (a['key']['key2'] == "value2")

    # Try to set tree node without key
    b = tree()
    try:
        set_tree_node(b, "", "")
    except ValueError:
        pass
    else:
        assert (False)

    # Try to set tree node with wrong type
    b = tree()
    try:
        set_tree_node(b, 42, 42)
    except TypeError:
        pass
    else:
        assert (False)



# Generated at 2022-06-14 06:51:56.578236
# Unit test for function set_tree_node
def test_set_tree_node():
    test_data = {'foo': 'bar', 'a': {'sub': {'subsub': 'subsubsubsubsubsubsubsubsubsubsubsubsubsubsub'}}}

# Generated at 2022-06-14 06:51:59.636919
# Unit test for function set_tree_node
def test_set_tree_node():
    d = tree()
    set_tree_node(d, 'a:b:c:d', 'value')
    assert d['a']['b']['c']['d'] == 'value'



# Generated at 2022-06-14 06:52:12.478456
# Unit test for function get_tree_node
def test_get_tree_node():
    assert(get_tree_node({'a': {'b': {'c': 'foo'}}}, 'a:b:c') == 'foo')
    assert(get_tree_node({'a': {'b': {'c': 'foo'}}}, 'a:b:c', parent=True) == {'b': {'c': 'foo'}})
    assert(get_tree_node({'a': {'b': {'c': 'foo'}}}, 'a:b:c', default='def') == 'foo')
    assert(get_tree_node({'a': {'b': {'c': 'foo'}}}, 'a:b:c:d') == None)

# Generated at 2022-06-14 06:52:45.098716
# Unit test for function get_tree_node
def test_get_tree_node():
    m = {
        'a': {
            'b': 1
        }
    }

    # Standard lookup
    assert get_tree_node(m, 'a:b') == 1

    # Standard lookup with parent requested
    assert get_tree_node(m, 'a:b', parent=True) == {'b': 1}

    # Unknown key
    try:
        get_tree_node(m, 'a:c')
    except KeyError:
        pass

    # Unknown key with default
    assert get_tree_node(m, 'a:c', default=2) == 2



# Generated at 2022-06-14 06:52:47.933269
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = {
        'foo': {'bar': {
            'baz': 'buz'
        }}
    }
    assert get_tree_node(mapping, 'foo:bar:baz') == 'buz'



# Generated at 2022-06-14 06:52:52.708831
# Unit test for function set_tree_node
def test_set_tree_node():
    test = {}
    set_tree_node(test, 'a:b:c:d', 'e')
    assert test['a']['b']['c']['d'] == 'e'



# Generated at 2022-06-14 06:53:02.417276
# Unit test for function set_tree_node
def test_set_tree_node():
    a = {}
    assert set_tree_node(a, 'a:b:c', '4')['a']['b'] == {'c': '4'}
    assert set_tree_node(a, 'a:b:c', '5')['a']['b'] == {'c': '5'}

    a = {}
    assert set_tree_node(a, 'a:b:c:d', '5') == {'c': {'d': '5'}}
    assert set_tree_node(a, 'a:b:c:d', '6') == {'c': {'d': '6'}}



# Generated at 2022-06-14 06:53:14.910684
# Unit test for function get_tree_node
def test_get_tree_node():
    node = {
          'foo': {
            'bar': {
              'baz': 'bingo'
            },
            'bang': 'boom'
          },
          'Quux': 'quxx'
        }

    assert node['foo']['bang'] == get_tree_node(node, 'foo:bang')
    assert node['foo']['bar']['baz'] == get_tree_node(node, 'foo:bar:baz')
    assert node['foo']['bar'] == get_tree_node(node, 'foo:bar', parent=True)
    assert node['foo'] == get_tree_node(node, 'foo:bar:baz', parent=True)
    assert node is get_tree_node(node, 'foo:bar:baz', parent=True, default=node)



# Generated at 2022-06-14 06:53:26.524958
# Unit test for function get_tree_node
def test_get_tree_node():
    base = {
        'this': {
            'is': {
                'a': 'tree'
            }
        }
    }

    assert get_tree_node(base, 'this') == {'is': {'a': 'tree'}}
    assert get_tree_node(base, 'this:is') == {'a': 'tree'}
    assert get_tree_node(base, 'this:is:a') == 'tree'
    assert get_tree_node(base, 'this:is:a') == 'tree'
    assert get_tree_node(base, 'this:is:a:key', default='default') == 'default'  # Test default
    try:
        get_tree_node(base, 'this:is:a:key')
    except KeyError:
        pass

# Generated at 2022-06-14 06:53:38.371426
# Unit test for function get_tree_node

# Generated at 2022-06-14 06:53:50.949814
# Unit test for function get_tree_node

# Generated at 2022-06-14 06:53:55.002459
# Unit test for function set_tree_node
def test_set_tree_node():
    """Unit test for function set_tree_node"""
    assert set_tree_node(tree(), 'a:b:c', 'c') == {'a': {'b': {'c': 'c'}}}
    assert set_tree_node(tree(), 'c:b:a', 'a') == {'c': {'b': {'a': 'a'}}}



# Generated at 2022-06-14 06:53:59.063764
# Unit test for function set_tree_node
def test_set_tree_node():
    mapping = {}
    set_tree_node(mapping, 'foo', 1)
    assert mapping == {'foo': 1}

    set_tree_node(mapping, 'foo:bar', 2)
    assert mapping == {'foo': {'bar': 2}}



# Generated at 2022-06-14 06:54:52.221804
# Unit test for function get_tree_node
def test_get_tree_node():
    tree = {
        'a': {
            'b': {
                'c': 'Works',
            }
        }
    }

    assert get_tree_node(tree, ['a', 'b'], default=_sentinel) == 'Works'



# Generated at 2022-06-14 06:54:59.711093
# Unit test for function get_tree_node
def test_get_tree_node():
    """
    >>> data = tree()
    >>> data['A']['B']['C'] = 10
    >>> data['A']['B']['C:D'] = 10
    >>> assert get_tree_node(data, 'A:B:C') == 10
    >>> assert get_tree_node(data, 'A:B:C:') == 10
    >>> assert get_tree_node(data, 'A:B:C:D') == 10
    >>> assert get_tree_node(data, 'A:B:C:D:') == 10

    >>> assert get_tree_node(data, 'A:B:C:D', parent=True) == {'C': 10, 'C:D': 10}
    """
    pass



# Generated at 2022-06-14 06:55:13.251003
# Unit test for function get_tree_node
def test_get_tree_node():
    # Type check
    with pytest.raises(TypeError) as excinfo:
        get_tree_node(None)

    assert 'mapping' in str(excinfo.value)

    # KeyError check
    with pytest.raises(KeyError):
        get_tree_node({}, 'a')

    # Type check
    with pytest.raises(TypeError) as excinfo:
        get_tree_node({}, 1)

    assert 'key' in str(excinfo.value)

    # KeyError check
    with pytest.raises(KeyError) as excinfo:
        get_tree_node({}, 'a')

    assert "Key 'a' not found" in str(excinfo.value)

    # KeyError check
    with pytest.raises(KeyError) as excinfo:
        get

# Generated at 2022-06-14 06:55:14.341388
# Unit test for function get_tree_node
def test_get_tree_node():
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 06:55:25.833034
# Unit test for function get_tree_node
def test_get_tree_node():
    # Test a regular, working dictionary
    mapping = {
        'a': 1,
        'b': {
            'z': False
        }
    }
    assert get_tree_node(mapping, 'a') == 1
    assert get_tree_node(mapping, 'b:z') is False

    # Test missing nodes
    with pytest.raises(KeyError):
        get_tree_node(mapping, 'b:z:y')

    assert get_tree_node(mapping, 'b:z:y', default=True) is True

    try:
        get_tree_node(mapping, 'b:z:y')
    except KeyError as exc:
        assert 'y not found.' in str(exc)
        assert 'b:z:y' in str(exc)

    assert get_tree

# Generated at 2022-06-14 06:55:37.886676
# Unit test for function get_tree_node
def test_get_tree_node():
    tree = {
        'parent': {
            'child': {
                'grandchild': True,
            },
            'sibling': 'foobar'
        }
    }
    assert get_tree_node(tree, 'parent:child:grandchild')
    assert get_tree_node(tree, 'parent:sibling') == 'foobar'
    assert get_tree_node(tree, 'parent:child')['grandchild']
    assert get_tree_node(tree, 'parent:child', parent=True)['sibling']
    assert get_tree_node(tree, 'parent:child:grandchild:foobar') is None
    assert get_tree_node(tree, 'parent:child:grandchild:foobar', default=False) is False

# Generated at 2022-06-14 06:55:45.998381
# Unit test for function get_tree_node
def test_get_tree_node():
    # Setup
    node = {'parent': {'child': 'val'}}

    # Tests
    assert get_tree_node(node, 'parent:child') == 'val'
    assert get_tree_node(node, 'parent') == {'child': 'val'}
    assert get_tree_node(node, 'parent:child', default='hello') == 'val'
    assert get_tree_node(node, 'does_not_exist', default='hello') == 'hello'
    assert get_tree_node(node, 'parent:child:3', default='hello') == 'hello'
    assert get_tree_node(node, 'parent', default='hello') == {'child': 'val'}
    assert get_tree_node(node, 'parent', parent=True) == node

# Generated at 2022-06-14 06:55:55.719824
# Unit test for function get_tree_node
def test_get_tree_node():
    data = {
        'a': {'b': {'c': 3.14}},
        'b': 2,
        'c': 'three'
    }
    assert get_tree_node(data, 'a:b:c') == 3.14
    assert get_tree_node(data, 'b') == 2
    assert get_tree_node(data, 'a:b:c:d:e') is _sentinel
    assert get_tree_node(data, 'a:b:c:d:e', default=None) is None



# Generated at 2022-06-14 06:56:06.598651
# Unit test for function get_tree_node
def test_get_tree_node():
    """Unit test for function get_tree_node"""
    tree = Tree()
    tree['node:subnode'] = 7

    assert get_tree_node(tree, 'node:subnode') == 7
    assert get_tree_node(tree, 'node')['subnode'] == 7
    assert get_tree_node(tree, 'quux', default=9) == 9
    assert get_tree_node(tree, 'node:quux', default=9) == 9
    assert get_tree_node(tree, 'node:quux') is KeyError
    assert get_tree_node(tree, 'node:quux', default=9) == 9

# Run unit tests if module run directly
if __name__ == '__main__':
    test_get_tree_node()