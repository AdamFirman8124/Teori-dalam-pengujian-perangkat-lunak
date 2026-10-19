

# Generated at 2022-06-14 06:46:16.866436
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = dict(foo=dict(bar=dict(baz='baz')))
    assert get_tree_node(mapping, 'foo:bar:baz') == 'baz'
    assert get_tree_node(mapping, 'foo:bar:baz:wow') is _sentinel
    assert get_tree_node(mapping, 'foo:bar:baz:wow', default='default') == 'default'

    mapping = dict(foo=dict(bar=dict(baz=dict(wow='lol'))))
    assert get_tree_node(mapping, 'foo:bar:baz:wow', default='default') == 'lol'

    mapping = dict(foo=dict(bar=dict(baz=dict(wow='lol'))))

# Generated at 2022-06-14 06:46:29.876760
# Unit test for function get_tree_node
def test_get_tree_node():
    tree = Tree({
        'a': {
            'b': {
                'c': {
                    'd': 'This is the value!'
                },
                'e': 'Another value!'
            }
        }
    })
    assert tree['a:b:c:d'] == 'This is the value!'
    assert tree['a:b:c:e'] == 'Another value!'
    assert tree['a:b:c', 'Good value'] == 'Good value'
    assert tree['a', 'Good value'] == 'Good value'
    assert tree.get('a:b:c:e') == 'Another value!'

# Generated at 2022-06-14 06:46:37.301125
# Unit test for function set_tree_node
def test_set_tree_node():
    test = {}

# Generated at 2022-06-14 06:46:49.260364
# Unit test for function get_tree_node
def test_get_tree_node():
    test_dict = {
        'stuff': {
            'ya': {
                'dont': {
                    'remember': {
                        'what': 'to do'
                    }
                }
            }
        }
    }

    assert get_tree_node(test_dict, 'stuff:ya:dont:remember:what') == 'to do'

    with pytest.raises(KeyError):
        get_tree_node(test_dict, 'stuff:ya:dont:remember:what:this:should:fail')

    assert get_tree_node(test_dict, 'stuff:ya:dont:remember:what:this:should:fail', default='This is OK') == 'This is OK'


# Generated at 2022-06-14 06:46:57.967349
# Unit test for function get_tree_node
def test_get_tree_node():
    assert get_tree_node({'foo': {'bar': {'baz': 1}}}, 'foo:bar:baz') == 1
    assert get_tree_node({'foo': {'bar': {'baz': 1}}}, 'foo:bar:baz:quux') is _sentinel
    assert get_tree_node({'foo': {'bar': {'baz': 1}}}, 'foo:bar:baz:quux', 'd') == 'd'



# Generated at 2022-06-14 06:47:01.405848
# Unit test for function set_tree_node
def test_set_tree_node():
    data = tree()
    set_tree_node(data, 'foo:bar', 'test')
    assert get_tree_node(data, 'foo')['bar'] == 'test'

# Generated at 2022-06-14 06:47:12.987852
# Unit test for function get_tree_node
def test_get_tree_node():
    """
    Test functionality of :func:`get_tree_node`
    """
    the_tree = tree()
    the_tree['one']['two']['three'] = 4
    assert get_tree_node(the_tree, 'one') == {'two': {'three': 4}}
    assert get_tree_node(the_tree, 'one:two') == {'three': 4}
    assert get_tree_node(the_tree, 'one:two:three') == 4
    assert get_tree_node(the_tree, 'one:two:three:four') is _sentinel

    with raises(KeyError):
        get_tree_node(the_tree, 'one:two:three:four')



# Generated at 2022-06-14 06:47:20.095004
# Unit test for function get_tree_node
def test_get_tree_node():
    tr = {'a': {'b': 'c'}, 'b': 2}

    # Good
    assert get_tree_node(tr, 'a') == {'b': 'c'}
    assert get_tree_node(tr, 'a:b') == 'c'
    assert get_tree_node(tr, 'a:b', parent=True) == {'b': 'c'}
    assert get_tree_node(tr, 'b') == 2

    # Bad
    with assert_raises(KeyError):
        get_tree_node(tr, 'no')
    with assert_raises(KeyError):
        get_tree_node(tr, 'a:no')

# Generated at 2022-06-14 06:47:30.487567
# Unit test for function set_tree_node
def test_set_tree_node():
    import sh
    import pprint
    tree = Tree()
    this_module_node = set_tree_node(tree, 'something:fancy:is:going:on', 'foo')
    this_module_node = set_tree_node(tree, 'something:else:is:going:on', 'bar')
    assert tree['something:fancy:is:going:on'] == 'foo'
    assert tree['something:else:is:going:on'] == 'bar'
    assert tree['something:else:is:going:on'] != 'foo'
    pprint.pprint(dict(tree))



# Generated at 2022-06-14 06:47:33.750582
# Unit test for function set_tree_node
def test_set_tree_node():
    t = tree()
    set_tree_node(t, 'a:b:c', 123)
    assert t['a']['b']['c'] is 123



# Generated at 2022-06-14 06:47:49.085053
# Unit test for function set_tree_node
def test_set_tree_node():
    _tree = tree()

    # Test setting node
    assert set_tree_node(_tree, 'foo:bar', 1) == {'bar': 1}
    assert _tree['foo'] == {'bar': 1}

    # Test setting node on a node
    assert set_tree_node(_tree['foo'], 'bar:herp', 2) == {'bar': {'herp': 2}}
    assert _tree['foo']['bar'] == {'herp': 2}

    # Test setting node on a node that doesn't exist
    assert set_tree_node(_tree['foo'], 'derp', 3) == {'derp': 3}
    assert _tree['foo'] == {'bar': {'herp': 2}, 'derp': 3}



# Generated at 2022-06-14 06:48:02.539669
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = {
        'b': {
            'c': {
                'd': 'e',
                'f': 'g'
            },
            'h': 'i'
        },
        'j': 'k',
        'l': 'm'
    }
    assert get_tree_node(mapping, 'b:c:d') == 'e'
    assert get_tree_node(mapping, 'b:c:f') == 'g'
    assert get_tree_node(mapping, 'b:h') == 'i'
    assert get_tree_node(mapping, 'j') == 'k'
    assert get_tree_node(mapping, 'l') == 'm'

# Generated at 2022-06-14 06:48:10.244695
# Unit test for function get_tree_node
def test_get_tree_node():

    # Setup
    tree_mapping = {
        'root_key': 'root_value',
        'level_1_1': {
            'level_2_1': 'leaf_node'
        },
        'level_1_2': {
            'level_2_1': 'leaf_node',
            'level_2_2': 'other_leaf_node',
        },
    }

    # Test
    fetched = get_tree_node(tree_mapping, 'root_key')
    assert fetched == 'root_value'

    # Test
    fetched = get_tree_node(tree_mapping, 'level_1_1:level_2_1')
    assert fetched == 'leaf_node'

    # Test

# Generated at 2022-06-14 06:48:18.368341
# Unit test for function set_tree_node
def test_set_tree_node():
    tree = {}
    set_tree_node(tree, 'key', 'value')
    assert tree['key'] == 'value'

    tree = {}
    set_tree_node(tree, 'key:key', 'value')
    assert tree['key']['key'] == 'value'

    tree = {}
    set_tree_node(tree, 'key:key:key', 'value')
    assert tree['key']['key']['key'] == 'value'



# Generated at 2022-06-14 06:48:28.388057
# Unit test for function get_tree_node
def test_get_tree_node():
    _mapping = {
        'a': {
            'b': {
                'c': 3
            }
        }
    }

    assert get_tree_node(_mapping, 'a:b:c', default=_sentinel) == 3
    assert get_tree_node(_mapping, 'a:b:z', default=_sentinel) is _sentinel
    assert get_tree_node(_mapping, 'a:b:z') == {}
    assert get_tree_node(_mapping, 'a:b:z', default=_sentinel) is _sentinel

    try:
        get_tree_node(_mapping, 'a:b:z')
    except KeyError:
        pass
    else:
        raise AssertionError("Why the hell didn't you raise a KeyError?")


# Unit test

# Generated at 2022-06-14 06:48:39.420217
# Unit test for function get_tree_node
def test_get_tree_node():
    tree = {
        'a': {
            'b': {
                'c': 'd'
            }
        }
    }
    assert get_tree_node(tree, 'a:b:c') == 'd'
    assert get_tree_node(tree, 'a:b:c', default='e') == 'd'
    assert get_tree_node(tree, 'a:b:d') == _sentinel
    assert get_tree_node(tree, 'a:b:d', default='e') == 'e'
    assert get_tree_node(tree, 'a:b:d', default=_sentinel) == _sentinel



# Generated at 2022-06-14 06:48:51.451624
# Unit test for function get_tree_node
def test_get_tree_node():
    data = {
        "a": {
            'another': {
                "b": 1,
                "d": [0, 1, 2],
                "e": {
                    'foo': 'bar'
                }
            },
            "c": 'foo'
        }
    }
    assert get_tree_node(data, '.a.another.e.foo', default=None) == 'bar'
    assert get_tree_node(data, 'a:another:e:foo', default=None) == 'bar'
    assert get_tree_node(data, 'a:another:foo', default=None) is None
    assert get_tree_node(data, 'a:another:e:foo', default=None) == 'bar'

# Generated at 2022-06-14 06:48:57.171957
# Unit test for function get_tree_node
def test_get_tree_node():
    assert get_tree_node({'a': {'b': {'c': 1}}}, 'a:b:c') == 1
    assert get_tree_node({'a': {'b': {'c': 1}}}, 'a:b:d', default=2) == 2
    assert get_tree_node({'a': {'b': {'c': 1}}}, 'a:b:d', default=2, parent=True) == {'c': 1}



# Generated at 2022-06-14 06:49:10.577076
# Unit test for function get_tree_node
def test_get_tree_node():
    one = {
        'one': {
            'two': 'three',
            'two_one': 'three_one',
            'two_two': {
                'three': 'four'
            }
        }
    }


# Generated at 2022-06-14 06:49:23.257825
# Unit test for function set_tree_node
def test_set_tree_node():
    tx = collections.OrderedDict()
    x = set_tree_node(tx, "a", "1")
    assert x == {"a": "1"}

    y = set_tree_node(tx, "b", "2")
    assert y == {"a": "1", "b": "2"}

    z = set_tree_node(tx, "c:d", "3")
    assert z == {"a": "1", "b": "2", "c": {"d": "3"}}

    set_tree_node(tx, "c:e:f:g:h", "4")
    assert tx == {"a": "1", "b": "2", "c": {"d": "3", "e": {"f": {"g": {"h": "4"}}}}}



# Generated at 2022-06-14 06:49:38.453593
# Unit test for function get_tree_node
def test_get_tree_node():
    test_tree = {
        'a': {
            'b': {
                'c': 'd',
                'e': 'f'
            }
        },
        'g': 'h'
    }

    assert(get_tree_node(test_tree, 'a:b:c') == 'd')
    assert(get_tree_node(test_tree, 'a:b') == {'c': 'd', 'e': 'f'})
    assert(get_tree_node(test_tree, 'd:e:f', default='f') == 'f')
    assert(get_tree_node(test_tree, 'g:h:f') == 'g')



# Generated at 2022-06-14 06:49:46.183128
# Unit test for function get_tree_node
def test_get_tree_node():
    import unittest
    from nose.tools import assert_equals

    class TestTree(unittest.TestCase):

        def setUp(self):
            self.tree = tree()
            self.tree['key']['dim1']['dim2'] = 'value'

        def test_get_tree_node_full_path(self):
            assert_equals(get_tree_node(self.tree, 'key:dim1:dim2'), 'value')

        def test_get_tree_node_with_parent(self):
            assert_equals(get_tree_node(self.tree, 'key:dim1:dim2', parent=True), self.tree['key'])


# Generated at 2022-06-14 06:49:52.313669
# Unit test for function set_tree_node
def test_set_tree_node():
    tree = Tree()
    assert tree.get('foo:bar:baz') == {}
    tree['foo:bar:baz'] = 'yes'
    assert tree.get('foo:bar:baz') == 'yes'

    assert tree.get('foo:bar:') == {}
    assert tree.get('foo:bar') == {'baz': 'yes'}

# Generated at 2022-06-14 06:50:02.803192
# Unit test for function get_tree_node
def test_get_tree_node():
    import unittest

    class GetTreeNodeTestCase(unittest.TestCase):

        def test_get_tree_node(self):

            test_data = {
                0: {
                    'a': {
                        'b': 1,
                    },
                    'b': {
                        'c': {
                            'd': 2
                        }
                    }
                }
            }

            self.assertEqual(get_tree_node(test_data, '0:a'), {'b': 1})
            self.assertEqual(get_tree_node(test_data, '0:b:c'), {'d': 2})
            self.assertEqual(get_tree_node(test_data, '0:b:c:d'), 2)

# Generated at 2022-06-14 06:50:08.909471
# Unit test for function get_tree_node
def test_get_tree_node():
    node = Tree({
        'level1': {
            'level2': {
                'level3': 'level3',
            }
        }
    })

    assert node['level1:level2:level3'] == 'level3'

    assert node.get('level1:level2:level3') == 'level3'



# Generated at 2022-06-14 06:50:18.519903
# Unit test for function set_tree_node
def test_set_tree_node():
    t = tree()
    set_tree_node(t, 'foo:bar', 'baz')
    assert t['foo']['bar'] == 'baz'

    # This proves we can set more than one level of keys.
    set_tree_node(t, 'foo:bar:baz', 'baz')
    assert t['foo']['bar']['baz'] == 'baz'
    set_tree_node(t, 'foo:bar:nested', 'nested')

    assert len(t) == 1
    assert len(t['foo']) == 2
    assert len(t['foo']['bar']) == 2



# Generated at 2022-06-14 06:50:24.812807
# Unit test for function get_tree_node
def test_get_tree_node():
    assert get_tree_node({'a': {'b': 'c'}}, 'a') == {'b': 'c'}
    assert get_tree_node({'a': {'b': 'c'}}, 'a:b') == 'c'
    assert get_tree_node({'a': 'b'}, 'a:b') is _sentinel



# Generated at 2022-06-14 06:50:32.799226
# Unit test for function get_tree_node
def test_get_tree_node():
    assert get_tree_node({'foo': {'bar': 'baz'}}, 'foo:bar') == 'baz'
    assert get_tree_node({'foo': {'bar': 'baz'}}, 'foo:bar', parent=True) == {'bar': 'baz'}
    assert get_tree_node({'foo': {'bar': 'baz'}}, 'foo:bar:fizz') == {}
    assert get_tree_node({'foo': {'bar': 'baz'}}, 'foo:bar:fizz', parent=True) == {'bar': 'baz'}
    assert get_tree_node({'foo': {'bar': {'baz': 'fizz'}}}, 'foo:bar') == {'baz': 'fizz'}
    assert get_tree_node

# Generated at 2022-06-14 06:50:37.048770
# Unit test for function set_tree_node
def test_set_tree_node():
    t = tree()
    set_tree_node(t, 'a:1:b', 'c')
    assert t['a']['1']['b'] == 'c'



# Generated at 2022-06-14 06:50:46.704035
# Unit test for function get_tree_node
def test_get_tree_node():
    """
    Test behavior of :py:func:`get_tree_node`
    """
    thing = {'a': {'b': 1}}
    assert get_tree_node(thing, 'a:b') == 1
    assert get_tree_node(thing, 'a:b1', default=2) == 2
    assert get_tree_node(thing, 'a:b1', default=2) == 2
    assert get_tree_node(thing, 'a:b:c', default=None) is None
    assert get_tree_node(thing, 'a:b', parent=True) == {'b': 1}

    try:
        get_tree_node(thing, 'a:b:c', default=_sentinel)
    except Exception:
        pass

# Generated at 2022-06-14 06:51:04.820229
# Unit test for function get_tree_node
def test_get_tree_node():
    assert get_tree_node({'a': 'b'}, 'a') == 'b'
    assert get_tree_node({'a': {'b': 'c'}}, 'a:b') == 'c'
    assert get_tree_node({'a': {'b': {'c': 'd'}}}, 'a:b:c') == 'd'

    try:
        get_tree_node({'a': {'b': 'c'}}, 'a:c')
    except KeyError:
        pass  # Silence the exception
    else:
        assert False, 'should have raised'

    assert get_tree_node({'a': {'b': 'c'}}, 'a:c', default='d') == 'd'


# Generated at 2022-06-14 06:51:15.707631
# Unit test for function get_tree_node
def test_get_tree_node():

    source = {
        'foo': {
            'bar': {
                'baz': {
                    'biz': {
                        'bob': 42,
                    }
                }
            }
        }
    }

    assert get_tree_node(source, 'foo:bar:baz:biz:bob') == 42
    assert get_tree_node(source, 'foo:bar:baz:biz:bob', default=420) == 42
    try:
        get_tree_node(source, 'foo:bar:baz:biz:bob:foo')
    except KeyError:
        # w00t!
        pass
    else:
        assert False, "Calling get_tree_node with an invalid key should raise KeyError"

# Generated at 2022-06-14 06:51:22.995767
# Unit test for function set_tree_node
def test_set_tree_node():
    d = {}
    set_tree_node(d, 'spam', 'eggs')
    assert get_tree_node(d, 'spam') == 'eggs'
    set_tree_node(d, 'spam:ham', 'pork')
    assert get_tree_node(d, 'spam:ham') == 'pork'
    assert get_tree_node(d, 'spam')['ham'] == 'pork'



# Generated at 2022-06-14 06:51:30.473848
# Unit test for function get_tree_node
def test_get_tree_node():
    from unittest import TestCase

    class TestGetTreeNode(TestCase):
        def setUp(self):
            self.data = {
                'foo': {
                    'bar': {
                        'baz': 'hello',
                        'qux': 'world'
                    },
                    'other': 'foobar',
                },
                'other': 'foobar',
            }

        def test_get_tree_node(self):
            self.assertEqual(get_tree_node(self.data, 'foo:bar:baz'), 'hello')
            self.assertEqual(get_tree_node(self.data, 'foo:bar:qux'), 'world')


# Generated at 2022-06-14 06:51:43.076651
# Unit test for function get_tree_node
def test_get_tree_node():
    assert get_tree_node({'a': {'b': {'c': 1}}, 'd': 2}, 'a:b:c') == 1
    assert get_tree_node({'a': {'b': {'c': 1}}, 'd': 2}, 'd') == 2
    assert get_tree_node({'a': {'b': {'c': 1}}, 'd': 2}, 'a:b') == {'c': 1}
    assert not get_tree_node({'a': {'b': {'c': 1}}, 'd': 2}, 'a:b', None)
    assert get_tree_node({'a': {'b': {'c': 1}}, 'd': 2}, 'a:b', parent=True) == {'b': {'c': 1}}
    assert get_tree

# Generated at 2022-06-14 06:51:50.064793
# Unit test for function set_tree_node
def test_set_tree_node():
    from types import ModuleType
    modules = ModuleType('__main__')
    set_tree_node(modules, 'os.path.abspath', '/usr')

    assert modules.os.path.abspath == '/usr'
    assert modules['os']['path']['abspath'] == '/usr'
    assert modules.os['path']['abspath'] == '/usr'



# Generated at 2022-06-14 06:51:58.176688
# Unit test for function get_tree_node
def test_get_tree_node():
    test_tree = {
        'child_a': {
            'grandchild_a': 'value',
            'grandchild_b': 'value'
        },
        'child_b': {
            'grandchild_a': 'value',
            'grandchild_b': 'value'
        }
    }
    assert get_tree_node(test_tree, 'child_a:grandchild_a') == 'value'



# Generated at 2022-06-14 06:52:07.140985
# Unit test for function get_tree_node
def test_get_tree_node():
    """Tests for get_tree_node"""
    test_tree = {
        'foo': {
            'bar': 'baz'
        },
        'qux': {
            'quux': {
                'corge': 'grault',
            }
        }
    }

    assert get_tree_node(test_tree, 'foo:bar') == 'baz'
    assert get_tree_node(test_tree, 'qux:quux:corge') == 'grault'



# Generated at 2022-06-14 06:52:11.420855
# Unit test for function set_tree_node
def test_set_tree_node():
    mapping = collections.defaultdict(dict)
    key = 'test::test2::test3'
    value = 'foo'
    set_tree_node(mapping, key, value)
    assert mapping['test']['test2']['test3'] == 'foo'

# Generated at 2022-06-14 06:52:16.231344
# Unit test for function set_tree_node
def test_set_tree_node():
    mapping = {}
    set_tree_node(mapping, 'foo:bar:baz', 'value')
    assert mapping['foo']['bar']['baz'] == 'value'
    assert mapping == {'foo': {'bar': {'baz': 'value'}}}

# Generated at 2022-06-14 06:52:45.869196
# Unit test for function get_tree_node
def test_get_tree_node():

    # Basic tree
    test = {'a': {'b': {'c': 'd'}}}

    # Basic test
    assert get_tree_node(test, 'a:b:c') == 'd'
    # Non-existing dimension
    assert get_tree_node(test, 'a:b:e') is _sentinel
    # Non-existing key
    assert get_tree_node(test, 'a:b:e', 'fuuuuuuuuuu') == 'fuuuuuuuuuu'
    # Non-existing key with default=_sentinel
    assert get_tree_node(test, 'a:b:e') is _sentinel



# Generated at 2022-06-14 06:52:55.885395
# Unit test for function get_tree_node
def test_get_tree_node():
    import itertools

    data = tree()
    data[1][2][3] = {'a': 1}
    data[1][2][4] = {'a': 2}
    data[2][2][3] = {'a': 3}
    data[3][2][3] = {'a': 4}
    data[4][2][3] = {'a': 5}
    data[6][2][3] = {'b': 6}
    data[1][2][3] = {'c': 7}


# Generated at 2022-06-14 06:53:05.388564
# Unit test for function set_tree_node
def test_set_tree_node():
    # Empty tree
    assert set_tree_node({}, 'a:b:c:d:e', 'value') == {'a': {'b': {'c': {'d': {'e': 'value'}}}}}
    # One level
    assert set_tree_node({'a': {'b': {}, 'c': {}}}, 'a:d', 'value') == {'a': {'b': {}, 'c': {}, 'd': 'value'}}
    # Multiple levels
    assert set_tree_node({'a': {'b': {}}}, 'a:c:d:e:f:g:h', 'value') == {'a': {'b': {}, 'c': {'d': {'e': {'f': {'g': {'h': 'value'}}}}}}}


#

# Generated at 2022-06-14 06:53:16.581996
# Unit test for function get_tree_node
def test_get_tree_node():
    """
    Test get_tree_node
    """
    mapping = {
        'key': {
            'subkey': 'Hello World',
            'subkey2': 'Foo Bar',
        }
    }
    assert get_tree_node(mapping, 'key:subkey') == 'Hello World'
    assert get_tree_node(mapping, 'key:subkey2') == 'Foo Bar'
    assert get_tree_node(mapping, 'nope:nothere:bye') is _sentinel

    # No error if a parent key is found
    assert get_tree_node(mapping, 'key:nope:nothere', default=None) is None



# Generated at 2022-06-14 06:53:22.034536
# Unit test for function get_tree_node
def test_get_tree_node():
    """
    Unit test for `get_tree_node`.

    Raises:
        AssertionError: Error messages specify failure cases.
    """
    tree = {'a': {'b': {'c': {'d': 'e'}}}}
    assert get_tree_node(tree, 'a:b:c:d') == 'e'
    assert get_tree_node(tree, 'a:b:c:d', default=_sentinel) == 'e'
    assert get_tree_node(tree, 'a:b:c:z', ':default:') == ':default:'
    with pytest.raises(KeyError):
        get_tree_node(tree, 'a:b:c:z')



# Generated at 2022-06-14 06:53:31.797893
# Unit test for function get_tree_node
def test_get_tree_node():
    base = {'a': {'b': {'c': 'test'}}}
    answer = get_tree_node(base, 'a:b:c')
    assert answer == 'test'

    answer = get_tree_node(base, 'a:b:c:d')
    assert answer is _sentinel

    answer = get_tree_node(base, 'a:b:c:d', default=None)
    assert answer is None

    answer = get_tree_node(base, 'a:b:c:d', default=False, parent=True)
    assert answer == {'c': 'test'}



# Generated at 2022-06-14 06:53:39.105890
# Unit test for function get_tree_node
def test_get_tree_node():
    test_dict = (
        {'A': {'B': {'C': 1, 'D': 2, 'E': 3}}},
        {'A': {'B': {'C': 1, 'D': 2, 'E': 3}}},
        {'A': {'B': {'C': 1, 'D': 2, 'E': 3}}},
    )
    assert gettree(test_dict, 'A:B:C') == 1
    assert gettree(test_dict, 'A:B:D') == 2
    assert gettree(test_dict, 'A:B:E') == 3
    assert gettree(test_dict, 'A:B:F') == None
    assert gettree(test_dict, 'A:B:F', default=1) == 1

# Generated at 2022-06-14 06:53:49.434414
# Unit test for function get_tree_node
def test_get_tree_node():
    tree = {'a': {'b': {'c': 'foo'}}}
    assert get_tree_node(tree, 'a:b:c') == 'foo'
    assert get_tree_node(tree, 'a:b:c', default=True) == 'foo'
    assert get_tree_node(tree, 'a:b:d', default=True) is True
    assert get_tree_node(tree, 'a:b:c', parent=True) == {'c': 'foo'}
    assert get_tree_node(tree, 'a:b:d', parent=True) == {'c': 'foo'}



# Generated at 2022-06-14 06:53:58.855916
# Unit test for function get_tree_node
def test_get_tree_node():
    tree = {'a': {'b': {'c': {'d': {'e': 'f'}}}}}
    assert get_tree_node(tree, 'a') == {'b': {'c': {'d': {'e': 'f'}}}}
    assert get_tree_node(tree, 'a:b') == {'c': {'d': {'e': 'f'}}}
    assert get_tree_node(tree, 'a:b:c') == {'d': {'e': 'f'}}
    assert get_tree_node(tree, 'a:b:c:d') == {'e': 'f'}
    assert get_tree_node(tree, 'a:b:c:d:e') == 'f'
    with pytest.raises(KeyError):
        get_

# Generated at 2022-06-14 06:54:04.245827
# Unit test for function get_tree_node
def test_get_tree_node():
    f = {'foo': {'bar': {'baz': 'ok'}}}
    assert get_tree_node(f, 'foo:bar:baz') == 'ok'

    f = {'foo': 'bar'}
    assert get_tree_node(f, 'foo:bar:baz', default='bogus') == 'bogus'
    assert get_tree_node(f, 'foo:bar:baz', default='bogus') == 'bogus'



# Generated at 2022-06-14 06:54:55.981738
# Unit test for function set_tree_node
def test_set_tree_node():
    d = {}
    d_copy = set_tree_node(d, 'a:b:c:d', 'A')
    assert d_copy == {'b': {'c': {'d': 'A'}}}



# Generated at 2022-06-14 06:55:01.612445
# Unit test for function get_tree_node
def test_get_tree_node():
    assert get_tree_node({'foo': {'bar': 'baz'}}, 'foo') == {'bar': 'baz'}
    assert get_tree_node({'foo': {'bar': 'baz'}}, 'foo:bar') == 'baz'



# Generated at 2022-06-14 06:55:10.474498
# Unit test for function get_tree_node
def test_get_tree_node():
    """
    Test `get_tree_node` on a `collections.defaultdict`.
    """
    tree = collections.defaultdict(tree)
    for i in range(3):
        tree[i]['e:e:e'][1] = 2
    assert get_tree_node(tree, '0:e:e:e:1') == 2
    assert get_tree_node(tree, '0:e:e:e:1', parent=True) == {1: 2}



# Generated at 2022-06-14 06:55:19.735330
# Unit test for function get_tree_node
def test_get_tree_node():
    assert(get_tree_node({}, 'a') is _sentinel)
    assert(get_tree_node({}, '') is _sentinel)
    assert(get_tree_node({'a': 1}, 'a') == 1)
    assert(get_tree_node({'a': 0}, 'a') == 0)
    assert(get_tree_node({'a': {'b': 1}}, 'a:b') == 1)
    assert(get_tree_node({'a': {'b': 0}}, 'a:b') == 0)
    assert(get_tree_node({'a': {'b': {'c': 1}}}, 'a:b:c') == 1)

# Generated at 2022-06-14 06:55:24.339748
# Unit test for function set_tree_node
def test_set_tree_node():
    a = tree()
    assert set_tree_node(a, 'a:b:c:d', 'e')['d'] == 'e'
    assert a['a']['b']['c']['d'] == 'e'

# Generated at 2022-06-14 06:55:29.583345
# Unit test for function set_tree_node
def test_set_tree_node():
    t = {}
    set_tree_node(t, 'root:parent:child:key', 'value')
    assert t['root']['parent']['child']['key'] == 'value'

    t = {}
    set_tree_node(t, 'root:parent:child:key:nope', 'value')
    assert t['root']['parent']['child']['key'] is None
    assert t['root']['parent']['child']['key']['nope'] == 'value'

    t = tree()
    set_tree_node(t, 'root:parent:child:key:nope', 'value')
    assert t['root']['parent']['child']['key']['nope'] == 'value'

# Generated at 2022-06-14 06:55:34.122645
# Unit test for function set_tree_node
def test_set_tree_node():
    # Test tree
    test_tree = Tree()

    # Assertion
    result = set_tree_node(test_tree, 'foo:bar:baz', 'Something')
    assert result['foo']['bar']['baz'] == 'Something'



# Generated at 2022-06-14 06:55:44.865482
# Unit test for function get_tree_node
def test_get_tree_node():
    tree = (('a:b:c:d', 1),
            ('f:g:h:i', 2),
            ('a:b:c:e', 3),
            ('f', 4))
    tree = dict(tree)

    assert get_tree_node(tree, 'f') == 4
    assert get_tree_node(tree, 'a:b:c:d') == 1
    assert get_tree_node(tree, 'a:b:c:d', parent=True) == {'d': 1, 'e': 3}
    assert get_tree_node(tree, 'f:g:h:i', parent=True) == {'h': {'i': 2}}

# Generated at 2022-06-14 06:55:57.349084
# Unit test for function get_tree_node
def test_get_tree_node():
    from collections import OrderedDict

    test_tree = OrderedDict([
        ('a', 'b'),
        ('c', OrderedDict([
            ('a', 'b'),
            ('c', 'd'),
            ('e', 'f'),
        ])),
        ('g', 'h')
    ])
    assert get_tree_node(test_tree, 'a') == 'b'
    assert get_tree_node(test_tree, 'c:a') == 'b'
    assert get_tree_node(test_tree, 'c:c') == 'd'
    assert get_tree_node(test_tree, 'c:e') == 'f'
    assert get_tree_node(test_tree, 'a:b') is _sentinel



# Generated at 2022-06-14 06:56:05.513542
# Unit test for function set_tree_node
def test_set_tree_node():
    from pprint import pprint
    from copy import deepcopy

    # Create dummy tree
    t = tree()

    # Modify tree
    set_tree_node(t, 'my:test:key', 'value')

    # Pretend we got the tree from storage of the modified tree
    t_modified = deepcopy(t)

    # Assert that the tree is the same
    assert (t_modified == t)

    # Assert that the tree has the right structure
    assert (t_modified['my']['test']['key'] == 'value')

