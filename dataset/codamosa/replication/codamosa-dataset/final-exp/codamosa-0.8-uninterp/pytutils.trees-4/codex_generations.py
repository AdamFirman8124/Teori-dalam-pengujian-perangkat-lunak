

# Generated at 2022-06-14 06:46:17.271514
# Unit test for function set_tree_node
def test_set_tree_node():
    d = {}
    set_tree_node(d, 'key1', 1)
    assert(d['key1'] == 1)
    set_tree_node(d, 'key2', 2)
    assert(d['key2'] == 2)
    set_tree_node(d, 'key3:key4', 4)
    assert(set_tree_node(d, 'key3')['key4'] == 4)
    set_tree_node(d, 'key3:key5:key6', 6)
    assert(set_tree_node(d, 'key3')['key5']['key6'] == 6)



# Generated at 2022-06-14 06:46:27.354788
# Unit test for function get_tree_node
def test_get_tree_node():
    import unittest
    import simplejson as json
    class Test(unittest.TestCase):
        def setUp(self):
            self.mapping = json.loads('{'
                                      '"amulet": {'
                                      '  "fire": {'
                                      '    "damage": {"raw": 1, "res": 2, "add": 3},'
                                      '    "area": 1'
                                      '  },'
                                      '  "ice": {'
                                      '    "damage": {"raw": 2, "res": 3, "add": 4},'
                                      '    "area": 2'
                                      '  }'
                                      '}'
                                      '}')


# Generated at 2022-06-14 06:46:36.080915
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = {
        'users': {
            'noise': {
                'name': 'Noise',
                'email': 'noise@disroot.org'
            },
            'sailor': {
                'name': 'Sailor',
                'email': 'sailor@disroot.org'
            }
        }
    }
    # It's namespaced by default
    assert get_tree_node(mapping, 'users:noise:name') == 'Noise'
    # ...but you can hit it as a flat key
    assert get_tree_node(mapping, 'users:noise:name', namespace=False) == 'Noise'



# Generated at 2022-06-14 06:46:41.949707
# Unit test for function get_tree_node
def test_get_tree_node():
    test_tree = {
        'foo': {
            'bar': {
                'baz': 'hello'
            }
        }
    }

    assert get_tree_node(test_tree, 'foo:bar:baz') == 'hello'
    assert get_tree_node(test_tree, 'foo:bar:baz', default='world') == 'hello'
    assert get_tree_node(test_tree, 'foo:bar:hello', default='world') == 'world'
    assert get_tree_node(test_tree, 'foo:bar', default='world', parent=True) == {'baz': 'hello'}
    assert get_tree_node(test_tree, 'foo:bar:baz', default='world', parent=True) == {'baz': 'hello'}
    assert get_tree

# Generated at 2022-06-14 06:46:54.482475
# Unit test for function set_tree_node
def test_set_tree_node():
    tree = {}
    set_tree_node(tree, 'foo', 'bar')
    assert tree['foo'] == 'bar'

    set_tree_node(tree, 'foo:bar', 'bla')
    assert tree['foo']['bar'] == 'bla'

    set_tree_node(tree, 'foo:bar:bla', 'blub')
    assert tree['foo']['bar']['bla'] == 'blub'

    set_tree_node(tree, 'baz:bar:bla', 'blub2')
    assert tree['baz']['bar']['bla'] == 'blub2'

    set_tree_node(tree, 'baz:bla', 'blub3')
    assert tree['baz']['bla'] == 'blub3'




# Generated at 2022-06-14 06:47:06.904537
# Unit test for function get_tree_node
def test_get_tree_node():
    """Unit tests for get_tree_node to demonstrate usecases."""
    # pylint: disable=line-too-long
    tree = {
        "": "Root",
        "foo": {
            "bar": {
                "baz": "Baz"
            }
        }
    }
    try:
        get_tree_node(tree, "")
    except KeyError:
        pass
    else:
        return "get_tree_node should raise KeyError on non-existent keys"
    try:
        get_tree_node(tree, "nonexistent")
    except KeyError:
        pass
    else:
        return "get_tree_node should raise KeyError on non-existent keys"
    if get_tree_node(tree, "nonexistent", default=None) is not None:
        return

# Generated at 2022-06-14 06:47:18.077798
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = {
        'foo': {
            'bar': 'baz',
        }
    }

    assert get_tree_node(mapping, 'foo:bar') == 'baz'

    # Test with parent=True
    parent_node = get_tree_node(mapping, 'foo:bar', parent=True)
    assert isinstance(parent_node, dict)
    assert parent_node == {'bar': 'baz'}

    try:
        get_tree_node(mapping, 'bar')
        assert False, 'Did not raise KeyError as expected.'
    except KeyError:
        pass



# Generated at 2022-06-14 06:47:23.586602
# Unit test for function set_tree_node
def test_set_tree_node():
    tree = {}
    set_tree_node(tree, '/foo/bar/baz', 'zap')
    assert tree == {
        'foo': {
            'bar': {
                'baz': 'zap'
            }
        }
    }

# Generated at 2022-06-14 06:47:32.728717
# Unit test for function get_tree_node
def test_get_tree_node():
    """Test fetching top-level node"""
    # Boring straight forward test
    tree_node = {'node': 'value'}
    assert get_tree_node(tree_node, 'node') == 'value'
    # Fancy-schmancy nested test
    tree_node['level1'] = {'level2': 'value'}
    assert get_tree_node(tree_node, 'level1:level2') == 'value'
    # Test KeyError
    with pytest.raises(KeyError):
        get_tree_node(tree_node, 'level3')



# Generated at 2022-06-14 06:47:44.793430
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = {
        'key': {
            'level_one': 'foo'
        }
    }

    # Test if level one works:
    assert get_tree_node(mapping, 'key:level_one') == 'foo'
    assert get_tree_node(mapping, 'key:level_two', False) is False

    # Test if level two works:
    assert get_tree_node(mapping, 'key:level_one:level_two', False) is False

    # Test that it raises on a non-existant key:
    with pytest.raises(KeyError):
        get_tree_node(mapping, 'key:level_two')



# Generated at 2022-06-14 06:47:53.327431
# Unit test for function set_tree_node
def test_set_tree_node():
    assert set_tree_node({}, 'test:one:two:three:four', 'five') == {
        'test': {
            'one': {
                'two': {
                    'three': {
                        'four': 'five',
                    },
                },
            },
        },
    }
    assert set_tree_node({}, 'test', 5)
    assert set_tree_node({}, 'test:one', 5)



# Generated at 2022-06-14 06:48:05.442974
# Unit test for function get_tree_node
def test_get_tree_node():
    import unittest
    class GetTreeNodeTestCase(unittest.TestCase):
        def test_get_tree_node(self):
            mapping = tree()

            mapping[1][2][3][4] = 'foo'
            self.assertEqual(get_tree_node(mapping, '1:2:3:4'), 'foo')

            try:
                get_tree_node(mapping, '1:2:3:5')
            except KeyError:
                pass
            else:
                self.fail('KeyError not raised on failed lookup')

            self.assertEqual(get_tree_node(mapping, '1:2:3:5', default='foo'), 'foo')

# Generated at 2022-06-14 06:48:08.131365
# Unit test for function set_tree_node
def test_set_tree_node():
    d = {}
    set_tree_node(d, 'a:b:c', 6)
    assert d['a']['b']['c'] == 6



# Generated at 2022-06-14 06:48:13.009881
# Unit test for function set_tree_node
def test_set_tree_node():
    mapping = {'a': 1}
    set_tree_node(mapping, 'b:c:d', 2)
    assert mapping == {'a': 1, 'b': {'c': {'d': 2}}}



# Generated at 2022-06-14 06:48:21.791718
# Unit test for function get_tree_node
def test_get_tree_node():
    tree = {
        'foo': {
            'bar': {
                'baz': 1
            }
        },
        'baz': 'asdf'
    }

    assert get_tree_node(tree, 'foo:bar:baz') == 1
    assert get_tree_node(tree, 'baz') == 'asdf'
    assert get_tree_node(tree, 'baz:foo') is None
    try:
        get_tree_node(tree, 'baz:foo', default=_sentinel)
    except KeyError:
        pass



# Generated at 2022-06-14 06:48:30.063325
# Unit test for function get_tree_node
def test_get_tree_node():
    sample_dict = {'foo': {'bar': {'baz': 'qux'}}}
    assert get_tree_node(sample_dict, 'foo:bar:baz') == 'qux'
    assert get_tree_node(sample_dict, 'foo:baz:bar', default='quux') == 'quux'
    assert get_tree_node(sample_dict, 'foo:bar') == {'baz': 'qux'}



# Generated at 2022-06-14 06:48:36.255629
# Unit test for function get_tree_node
def test_get_tree_node():
    tree = Tree({
        'simple': 'leaf',
        'deeper': {
            'leaf': 'leaf',
            'other': 'leaf',

            'deeper': {
                'leaf': 'leaf',
                'other': 'leaf',

                'deeper': {
                    'leaf': 'leaf',
                    'other': 'leaf',
                }
            }
        }
    })

    tree['simple'] = 'leaf'
    tree['deeper:leaf'] = 'leaf'
    tree['deeper:deeper:leaf'] = 'leaf'
    tree['deeper:deeper:deeper:leaf'] = 'leaf'

    assert tree['simple'] == 'leaf'
    assert tree['deeper:leaf'] == 'leaf'
    assert tree['deeper:deeper:leaf'] == 'leaf'

# Generated at 2022-06-14 06:48:44.383796
# Unit test for function get_tree_node
def test_get_tree_node():
    tree = {
        'a': {
            'b': {
                'c': 'foo',
            },
            'd': {
                'e': 'bar',
            },
        },
        'f': {
            'g': {
                'h': {
                    'i': 'baz',
                    'j': 'ban',
                }
            }
        }
    }
    assert get_tree_node(tree, 'f:g:h:i') == 'baz'
    assert get_tree_node(tree, 'a:d:e') == 'bar'
    assert get_tree_node(tree, 'a:b') == {'c': 'foo'}
    assert get_tree_node(tree, 'a:b', parent=True) == {'b': {'c': 'foo'}}

# Generated at 2022-06-14 06:48:56.068639
# Unit test for function get_tree_node
def test_get_tree_node():
    """Unit testing for `get_tree_node`."""
    assert get_tree_node({}, 'meow') == {}.get('meow')
    assert get_tree_node({'foo': {'bar': 'baz'}}, 'foo:bar') == get_tree_node({'foo': {'bar': 'baz'}}, 'foo').get('bar')

    # Test parent
    assert get_tree_node({'foo': {'bar': 'baz'}}, 'foo:bar', parent=True) == get_tree_node({'foo': {'bar': 'baz'}}, 'foo')

    # Test default
    assert get_tree_node({'foo': {'bar': 'baz'}}, 'foo:meow', default='woof') == 'woof'

    # Test default sentinel

# Generated at 2022-06-14 06:49:07.480295
# Unit test for function get_tree_node
def test_get_tree_node():
    test_data = {
        'a': {
            'b': [
                'c'
            ],
            'd': {
                'e': 'butts'
            }
        }
    }
    assert get_tree_node(test_data, 'a') == test_data['a']
    assert get_tree_node(test_data, 'a:b') == test_data['a']['b']
    assert get_tree_node(test_data, 'a:b:0') == test_data['a']['b'][0]
    assert get_tree_node(test_data, 'a:b:0', default='wow') == test_data['a']['b'][0]

# Generated at 2022-06-14 06:49:18.451732
# Unit test for function get_tree_node
def test_get_tree_node():
    d = {'a': {'a': 1, 'b': 2}, 'b': 3}
    assert get_tree_node(d, 'a', 0) == d['a']
    assert get_tree_node(d, 'a:b', 3) == d['a']['b']



# Generated at 2022-06-14 06:49:24.335000
# Unit test for function get_tree_node
def test_get_tree_node():
    """
    Test for existence of core module.
    """
    from . import parse
    from .exceptions import MissingModule
    from .exports import register_module

    def test_tree():
        """Create test tree."""
        tree = Tree()
        tree['a'] = 1
        tree['b'] = 2
        tree['c']['ca'] = 3
        tree['c']['cb'] = 4
        tree['d']['da']['daa'] = 5
        tree['d']['da']['dab'] = 6
        return tree

    def register_test_modules(tree):
        register_module(parse, tree)

    def test_missing():
        """Test missing."""

# Generated at 2022-06-14 06:49:33.079956
# Unit test for function get_tree_node
def test_get_tree_node():
    assert get_tree_node({'foo': {'bar': 'baz'}}, 'foo:bar') == 'baz'
    assert get_tree_node({'foo': {'bar': 'baz'}}, 'foo:bar:qux') is _sentinel
    assert get_tree_node({'foo': {'bar': 'baz'}}, 'foo:bar:qux', default='default') == 'default'


###
# Taken from http://code.activestate.com/recipes/578231-probably-the-fastest-memoization-decorator-in-the-/
# Then modified slightly to fit into my project.

# Generated at 2022-06-14 06:49:40.402821
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = {
        'k1': {
            'k2': {
                'k3': 'lol'
            }
        }
    }
    assert get_tree_node(mapping, 'k1:k2:k3') == 'lol'
    assert get_tree_node(mapping, 'k1', default='derp') == {'k2': {'k3': 'lol'}}
    assert get_tree_node(mapping, 'k1:k2') == {'k3': 'lol'}
    assert get_tree_node(mapping, 'k1:k2:k3:k4', default=None) is None
    assert get_tree_node(mapping, 'k1:k2:k3:k4') is ValueError

# Generated at 2022-06-14 06:49:53.502725
# Unit test for function get_tree_node
def test_get_tree_node():
    """Test get_tree_node function."""
    import pytest
    mapping = tree()
    mapping['root']['sub'] = 'value'
    assert get_tree_node(mapping, 'root:sub') == 'value'
    assert get_tree_node(mapping, 'root') == {'sub': 'value'}
    assert get_tree_node(mapping, 'root:foo', default=None) is None
    with pytest.raises(KeyError):
        get_tree_node(mapping, 'root:foo')

    # Test parent fetching
    parent = get_tree_node(mapping, 'root:sub', parent=True)
    assert parent == {'sub': 'value'}
    parent = get_tree_node(mapping, 'root', parent=True)

# Generated at 2022-06-14 06:49:59.418205
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = tree()
    mapping['a']['b']['c'] = {'1': '2'}

    assert get_tree_node(mapping, 'a:b:c') == {'1': '2'}
    assert get_tree_node(mapping, 'a:b:c:1') == '2'

    with pytest.raises(KeyError):
        assert get_tree_node(mapping, 'a:b:c:1:1')

    assert get_tree_node(mapping, 'a:b:c:1:1', default={}) == {}



# Generated at 2022-06-14 06:50:04.423914
# Unit test for function set_tree_node
def test_set_tree_node():
    mapping = {}
    key = 'a:b:c'
    value = 5
    set_tree_node(mapping, key, value)
    assert mapping == {'a': {'b': {'c': value}}}



# Generated at 2022-06-14 06:50:14.436312
# Unit test for function set_tree_node
def test_set_tree_node():
    test_data_1 = {
        'foo': {
            'bar': {
                'baz': 'qux'
            }
        }
    }

    set_tree_node(test_data_1, 'foo:bar:baz', 'quux')
    assert test_data_1['foo']['bar']['baz'] == 'quux'

    set_tree_node(test_data_1, 'foo:bar:foobar', 'quuz')
    assert test_data_1['foo']['bar']['foobar'] == 'quuz'

    set_tree_node(test_data_1, 'foo:bar:foobaz:quuz', 'quuz')



# Generated at 2022-06-14 06:50:23.046915
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = {
        'a': {
            'b': {
                'c': 1
            }
        }
    }
    assert get_tree_node(mapping, 'a:b:c') == 1
    assert get_tree_node(mapping, 'a:b:d') is _sentinel
    assert get_tree_node(mapping, 'a:b:d', []) == []


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 06:50:29.113336
# Unit test for function get_tree_node
def test_get_tree_node():
    assert get_tree_node({'a': 'b'}, 'a') == 'b'
    assert get_tree_node({'a': {'b': 'c'}}, 'a:b') == 'c'
    assert get_tree_node({'a': {'b': {'c': 'd'}}}, 'a:b:c') == 'd'
    assert get_tree_node({'a': {'b': {'c': 'd'}}}, 'a') == {'b': {'c': 'd'}}
    assert get_tree_node({'a': {'b': {'c': 'd'}}}, 'a:') == {'b': {'c': 'd'}}

# Generated at 2022-06-14 06:50:50.773083
# Unit test for function get_tree_node
def test_get_tree_node():
    test_tree = {
        'level1': {
            'level2': {
                'value': 1,
            },
            'other': 2
        },
        'level1.1': 3
    }

    # Value
    assert get_tree_node(test_tree, 'level1:level2:value') == 1
    assert get_tree_node(test_tree, 'level1.1') == 3
    # Parents
    assert get_tree_node(test_tree, 'level1:level2:value', parent=True) == test_tree['level1']['level2']
    assert get_tree_node(test_tree, 'level1.1', parent=True) == test_tree
    # Default
    assert get_tree_node(test_tree, 'level1.2', default=5) == 5

# Generated at 2022-06-14 06:51:02.032172
# Unit test for function get_tree_node
def test_get_tree_node():
    """Tests whether get_tree_node works as expected."""

    # Valid tree
    assert get_tree_node({'foo': {'bar': 'baz'}}, 'foo:bar') == 'baz'

    # Valid tree, default value
    assert get_tree_node({'foo': {'bar': 'baz'}}, 'foo:bean', default='mocha') == 'mocha'

    # Valid tree, parent
    assert get_tree_node({'foo': {'bar': 'baz'}}, 'foo:bar', parent=True) == {'bar': 'baz'}

    # Invalid tree, no default
    with pytest.raises(KeyError) as exc_info:
        get_tree_node({'foo': {'bar': 'baz'}}, 'foo:bean')



# Generated at 2022-06-14 06:51:09.598090
# Unit test for function get_tree_node
def test_get_tree_node():
    node = tree()
    node['a']['b']['c'] = 3
    assert get_tree_node(node, 'a:b:c') == 3
    assert get_tree_node(node, '') == node
    assert get_tree_node(node, 'a:b') == node['a']['b']
    with pytest.raises(KeyError):
        get_tree_node(node, 'a:b:c:d')



# Generated at 2022-06-14 06:51:14.806823
# Unit test for function get_tree_node
def test_get_tree_node():
    tree = collections.defaultdict(lambda:collections.defaultdict(lambda:collections.defaultdict(list)))
    tree[1][2][3].append(4)
    assert get_tree_node(tree, '1:2:3') == [4]


# Generated at 2022-06-14 06:51:21.341964
# Unit test for function set_tree_node
def test_set_tree_node():
    out = {}
    set_tree_node(out, 'subsubsub:subsubsubsub', 'end')
    assert out['subsubsub']['subsubsubsub'] == 'end'
    out = {}
    set_tree_node(out, 'subsubsubsub:subsubsub', 'end')
    assert out['subsubsubsub']['subsubsub'] == 'end'



# Generated at 2022-06-14 06:51:32.037410
# Unit test for function get_tree_node
def test_get_tree_node():
    data = {
        'a': {
            'b': 'c',
        },
    }
    assert get_tree_node(data, 'a') == {'b': 'c'}
    assert get_tree_node(data, 'a:b') == 'c'
    assert get_tree_node(data, 'a:b:c', default=None) is None
    assert get_tree_node(data, 'a:b:c', parent=True) == {'b': 'c'}
    assert get_tree_node(data, 'a:b:c:d', parent=True) == {'b': 'c'}
    assert get_tree_node(data, 'a:b:c:d', parent=True) == get_tree_node(data, 'a:d', parent=True)




# Generated at 2022-06-14 06:51:44.336975
# Unit test for function set_tree_node
def test_set_tree_node():
    """Function set tree node."""
    mapping = {
        'foo': {
            'bar': 12,
            'baz': {
                'bing': 'bong'
            }
        }
    }
    set_tree_node(mapping, 'foo:bar', 'hello')
    assert mapping['foo']['bar'] == 'hello'
    mapping = {
        'foo': {
            'bar': 12,
            'baz': {
                'bing': 'bong'
            }
        }
    }
    set_tree_node(mapping, 'foo:baz:bing', 'hello')
    assert mapping['foo']['baz']['bing'] == 'hello'

# Generated at 2022-06-14 06:51:46.051947
# Unit test for function set_tree_node
def test_set_tree_node():
    mapping = tree()
    set_tree_node(mapping, 'foo', 'bar')
    assert mapping['foo'] == 'bar'



# Generated at 2022-06-14 06:51:53.375616
# Unit test for function get_tree_node
def test_get_tree_node():
    data = {
        'a': 'b',
        'c': {
            'd': {
                'e': 'f'
            }
        }
    }

    assert get_tree_node(data, 'a') == 'b'
    assert get_tree_node(data, 'c:d:e') == 'f'
    raises(KeyError, get_tree_node, data, 'c:d:z')



# Generated at 2022-06-14 06:52:05.126863
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = {'a': 'b'}
    assert get_tree_node(mapping, 'a') == 'b'
    assert get_tree_node(mapping, 'a:b') is _sentinel

    mapping['a'] = {
        'b': {
            'c': 'd'
        }
    }

    assert get_tree_node(mapping, 'a:b:c') == 'd'
    assert get_tree_node(mapping, 'a:b:c:d') is _sentinel

    mapping = {
        'a': {
            'b': {
                'c': {
                    'd': 'e'
                }
            }
        }
    }

    assert get_tree_node(mapping, 'a:b:c:d') == 'e'
    assert get

# Generated at 2022-06-14 06:52:34.160413
# Unit test for function get_tree_node
def test_get_tree_node():
    t = {
        'foo': {
            'bar': 1,
            'baz': 2,
        },
        'lol': 3,
    }

    assert get_tree_node(t, 'foo:bar') == 1
    assert get_tree_node(t, 'lol') == 3
    assert get_tree_node(t, 'lol:cats') is None
    assert get_tree_node(t, 'whatsis', default='lol') == 'lol'

    with pytest.raises(KeyError):
        get_tree_node(t, 'foo:who:cats')



# Generated at 2022-06-14 06:52:37.155846
# Unit test for function set_tree_node
def test_set_tree_node():
    mapping = tree()
    set_tree_node(mapping, 'foo:bar:aoeu', 'fdsa')
    assert 'fdsa' == mapping['foo']['bar']['aoeu']



# Generated at 2022-06-14 06:52:43.946373
# Unit test for function set_tree_node
def test_set_tree_node():
    mapping = {}
    for node, value in [
        ('a', 1),
        ('b:b', 2),
        ('c:c:c', 3),
    ]:
        set_tree_node(mapping, node, value)

    assert mapping['a'] == 1
    assert mapping['b']['b'] == 2
    assert mapping['c']['c']['c'] == 3



# Generated at 2022-06-14 06:52:48.057878
# Unit test for function get_tree_node
def test_get_tree_node():
    from veteres.database.objects import ItemDefinition
    items = ItemDefinition._items
    assert items.get_tree_node('99:30') == items[99][30]
    assert items.get_tree_node('99:0') == items[99][0]



# Generated at 2022-06-14 06:52:57.026063
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = {
        'test': {
            'test': {
                'test': 'fail',
            },
        },
    }

    assert get_tree_node(mapping, 'test:test:test') == 'fail'
    assert get_tree_node(mapping, 'test:test:test', default='fail') == 'fail'
    with pytest.raises(KeyError):
        get_tree_node(mapping, 'test:test:test:test')



# Generated at 2022-06-14 06:53:03.716251
# Unit test for function get_tree_node
def test_get_tree_node():
    from pprint import pprint
    my_tree = {
        'a': {
            'b': {
                'c': {
                    'd': 'e'
                }
            }
        }
    }
    pprint(get_tree_node(my_tree, 'a:b:c'))
    pprint(get_tree_node(my_tree, 'a:b:c:d'))
    pprint(get_tree_node(my_tree, 'a:b:b:d'))



# Generated at 2022-06-14 06:53:16.369484
# Unit test for function get_tree_node
def test_get_tree_node():
    import unittest2

    class GetTreeNodeTest(unittest2.TestCase):
        def test_get(self):
            test_mapping = {
                'user': {
                    'firstname': 'Janis',
                    'lastname': 'Michalovics'
                }
            }
            self.assertEqual(get_tree_node(test_mapping, 'user:firstname'), 'Janis')
            self.assertEqual(get_tree_node(test_mapping, 'user:lastname'), 'Michalovics')

        def test_keyerror(self):
            test_mapping = {
                'user': {
                }
            }
            self.assertRaises(KeyError, get_tree_node, test_mapping, 'user:lastname')


# Generated at 2022-06-14 06:53:21.812193
# Unit test for function get_tree_node
def test_get_tree_node():
    assert get_tree_node({'foo': 'bar'}, 'foo') == 'bar'
    assert get_tree_node({'foo': 'bar'}, 'spam', default='eggs') == 'eggs'
    assert get_tree_node({'foo': 'bar'}, 'spam', default=None) is None
    assert get_tree_node({'foo': 'bar'}, 'spam') is _sentinel
    assert get_tree_node({'foo': 'bar'}, 'foo:bar', parent=True) == 'bar'
    with pytest.raises(KeyError):
        get_tree_node({'foo': 'bar'}, 'spam')


# Generated at 2022-06-14 06:53:26.068475
# Unit test for function get_tree_node
def test_get_tree_node():
    assert(
        get_tree_node({'a': {'b': 'c'}, 'd': {'e': 'f'}}, 'd:e') == 'f'
    )

# Generated at 2022-06-14 06:53:33.769541
# Unit test for function get_tree_node
def test_get_tree_node():
    config = {'section1': {'var1': 'val1'},
              'section2': {'var1': 'val2'}}

    assert get_tree_node(config, 'section1:var1') == 'val1'
    assert get_tree_node(config, 'section2:var1') == 'val2'
    assert get_tree_node(config, 'section3:var1', default='default') == 'default'

# Generated at 2022-06-14 06:54:20.930771
# Unit test for function get_tree_node
def test_get_tree_node():
    '''
    >>> test = {'a':'b'}
    >>> test['a']
    'b'
    >>> get_tree_node(test, 'a', default='c')
    'b'
    >>> get_tree_node(test, 'b', default='c')
    'c'
    >>> get_tree_node({}, 'b', default='c')
    'c'
    '''
    pass

# Generated at 2022-06-14 06:54:27.192167
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = tree()
    mapping['foo']['bar'] = 'baz'
    mapping['foo']['foo'] = 'bar'
    mapping['foo']['baz']['foo'] = 'bar'
    mapping['foo']['baz']['baz'] = 'foo'

    assert 'baz' == get_tree_node(mapping, 'foo:baz')
    assert 'bar' == get_tree_node(mapping, 'foo:bar')
    assert 'foo' == get_tree_node(mapping, 'foo:baz:foo')
    assert 'baz' == get_tree_node(mapping, 'foo:baz:baz')
    assert 'foo' == get_tree_node(mapping, 'foo:baz', default='foo')


# Generated at 2022-06-14 06:54:38.434830
# Unit test for function get_tree_node
def test_get_tree_node():
    sample = {
        'a': {
            'b': {
                'c': 'C',
                'd': 'D',
            },
            'e': 'E',
        }
    }

    test = get_tree_node(sample, 'a:b:c')
    assert test == 'C'
    test = get_tree_node(sample, 'a:e')
    assert test == 'E'
    test = get_tree_node(sample, 'a:b:d', parent=True)
    assert test == {'c': 'C', 'd': 'D'}
    test = get_tree_node(sample, 'a:b:d:e')
    assert test is None
    test = get_tree_node(sample, 'a:b:d:e', default='D')
    assert test

# Generated at 2022-06-14 06:54:46.206187
# Unit test for function get_tree_node
def test_get_tree_node():
    d = {'foo': 'bar', 'baz': {'boo': 'far', 'bar': 'baz'}}
    assert get_tree_node(d, 'foo') == 'bar'
    assert get_tree_node(d, 'baz:boo') == 'far'
    assert get_tree_node(d, 'baz:foo', 'default') == 'default'
    assert get_tree_node(d, 'baz:bar', parent=True) == {'boo': 'far', 'bar': 'baz'}
    assert get_tree_node(d, 'baz:foo', parent=True) == 'bar'
    assert get_tree_node(d, 'baz:boo', parent=True) == {'boo': 'far', 'bar': 'baz'}

# Generated at 2022-06-14 06:54:51.266045
# Unit test for function get_tree_node
def test_get_tree_node():
    assert get_tree_node({}, 'a') is _sentinel
    assert get_tree_node({'a': {}}, 'a') == {}
    assert get_tree_node({'a': {}}, 'a:b') is _sentinel



# Generated at 2022-06-14 06:54:56.326438
# Unit test for function set_tree_node
def test_set_tree_node():
    """
    Unit test for function `set_tree_node`.
    """
    d = dict()

    set_tree_node(d, 'a:b:c', 'test')

    assert {'a': {'b': {'c': 'test'}}} == d
    print('Function "set_tree_node" is ok.')



# Generated at 2022-06-14 06:55:00.879634
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = {'foo': {'bar': {'baz': 'BAZ'}}}
    assert get_tree_node(mapping, 'foo:bar:baz') == 'BAZ'



# Generated at 2022-06-14 06:55:03.392853
# Unit test for function set_tree_node
def test_set_tree_node():
    # TODO: TESTS
    """ I think this is all covered by doctests. """
    pass



# Generated at 2022-06-14 06:55:15.641585
# Unit test for function get_tree_node
def test_get_tree_node():
    tree = {
        'foo': {
            'bar': 'BAR!',
            'baz': {
                'bob': 'BAZ!',
            }
        },
        'bar': {
            'foo': 'FOO!',
        }
    }

    assert get_tree_node(tree, 'bar:foo') == 'FOO!'
    assert get_tree_node(tree, 'foo:baz') == {'bob': 'BAZ!'}
    assert get_tree_node(tree, 'foo:bar') == 'BAR!'
    assert get_tree_node(tree, 'foo:baz:bob') == 'BAZ!'
    assert get_tree_node(tree, 'foo:baz:bob:foo') == _sentinel



# Generated at 2022-06-14 06:55:23.374023
# Unit test for function set_tree_node
def test_set_tree_node():
    tree = {}
    set_tree_node(tree, 'a:b:c', 'value')
    assert tree['a']['b']['c'] == 'value'

    tree = tree['a']
    set_tree_node(tree, 'b:c', 'value')
    assert tree['b']['c'] == 'value'

    try:
        set_tree_node(tree, 'b:c', 'value')
        raise Exception('Should have raised TypeError')
    except TypeError:
        pass
