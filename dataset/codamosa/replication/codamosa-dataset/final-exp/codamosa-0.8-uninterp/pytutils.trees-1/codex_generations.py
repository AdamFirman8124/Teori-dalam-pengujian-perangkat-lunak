

# Generated at 2022-06-14 06:46:17.078803
# Unit test for function get_tree_node
def test_get_tree_node():
    t = tree()
    t['a']['b']['c'] = 'd'
    t['a']['b']['e'] = 'f'
    t['a']['j']['g'] = 'h'
    t['k']['l']['m']['n'] = 'o'
    t['k']['l']['p'] = 'q'
    t['z'] = 'y'
    assert(''.join(t['a']['b']['c'])) == 'd'
    assert(''.join(t['a']['b']['e'])) == 'f'
    assert(''.join(t['a']['j']['g'])) == 'h'

# Generated at 2022-06-14 06:46:22.821431
# Unit test for function get_tree_node
def test_get_tree_node():
    tree = {
        'a': {
            'b': {
                'c': 'Hello!',
            }
        }
    }
    assert get_tree_node(tree, 'a:b:c') == 'Hello!'
    assert get_tree_node(tree, 'a:b:d') == _sentinel

# Generated at 2022-06-14 06:46:30.251063
# Unit test for function set_tree_node
def test_set_tree_node():
    d = {}
    set_tree_node(d, 'foo', 'bar')
    assert d['foo'] == 'bar'

    d = {}
    set_tree_node(d, 'foo:bar', 'baz')
    assert d['foo']['bar'] == 'baz'

    d = {}
    set_tree_node(d, 'food:baz', 'barg')
    assert d['food']['baz'] == 'barg'



# Generated at 2022-06-14 06:46:37.458544
# Unit test for function get_tree_node
def test_get_tree_node():
    tree1 = collections.defaultdict()
    tree1['arr'][0] = 1
    tree1['arr'][1] = 2
    tree1['arr'][2] = 3

    tree2 = collections.defaultdict()
    tree2['arr']['2'] = 3

    tree3 = collections.defaultdict()
    tree3['arr'][0]['a'] = 1
    tree3['arr'][0]['b'] = 2
    tree3['arr'][1]['a'] = 3
    tree3['arr'][1]['b'] = 4
    tree3['arr'][2]['a'] = 5
    tree3['arr'][2]['b'] = 6

    assert get_tree_node(tree1, 'arr:0') == 1

# Generated at 2022-06-14 06:46:39.896553
# Unit test for function set_tree_node
def test_set_tree_node():
    test_dict = dict()
    test_key = 'item:sub:sub2'
    test_value = 'test'
    set_tree_node(test_dict, test_key, test_value)
    assert test_dict['item']['sub']['sub2'] == test_value



# Generated at 2022-06-14 06:46:51.785127
# Unit test for function get_tree_node
def test_get_tree_node():
    def assert_get_tree_node(mapping, key, expected, default=_sentinel, parent=False):
        actual = get_tree_node(mapping, key, default=default, parent=parent)
        assert actual == expected, "testing {!r} -> {!r}".format(mapping, key)

    # Empty mapping
    assert_get_tree_node(
        {},
        'foo:bar',
        _sentinel,
        default=_sentinel
    )

    # root only
    assert_get_tree_node(
        {
            'baz': 'baz'
        },
        'baz',
        'baz'
    )

    # single level

# Generated at 2022-06-14 06:47:05.245565
# Unit test for function get_tree_node
def test_get_tree_node():
    """Tests for :func:ghci.utils.get_tree_node"""
    m = {'foo': {'bar': 'baz'}}
    assert get_tree_node(m, 'foo:bar') == 'baz'
    assert get_tree_node(m, 'foo:bar', default='DNE') == 'baz'
    assert get_tree_node(m, 'foo:bar:baz', default='DNE') == 'DNE'
    assert get_tree_node(m, 'foo:bar:baz') == 'DNE'
    assert get_tree_node(m, 'foo:bar:baz:foo', default='DNE') == 'DNE'
    assert get_tree_node(m, 'foo:bar:baz:foo', default='DNE') == 'DNE'


# Generated at 2022-06-14 06:47:16.685545
# Unit test for function get_tree_node
def test_get_tree_node():
    import pytest
    t = Tree()
    t['a'] = 1
    t['b:c'] = 2
    t['b:d:e'] = 3
    t['b:d:f'] = 4
    with pytest.raises(KeyError):
        get_tree_node(t, 'x', _sentinel)

    assert get_tree_node(t, 'a') == 1
    assert get_tree_node(t, 'b:c') == 2
    assert get_tree_node(t, 'b:d:e') == 3
    assert get_tree_node(t, 'b:d:f') == 4
    assert get_tree_node(t, 'b:d', parent=True) == {'e': 3, 'f': 4}



# Generated at 2022-06-14 06:47:30.816907
# Unit test for function set_tree_node
def test_set_tree_node():
    dct = dict()
    assert set_tree_node(dct, 'a', 1) == {'a': 1}
    assert dct == {'a': 1}
    assert set_tree_node(dct, 'a:b', 2) == {'a': {'b': 2}}
    assert dct == {'a': {'b': 2}}
    assert set_tree_node(dct, 'a:b:c', 3) == {'a': {'b': {'c': 3}}}
    assert dct == {'a': {'b': {'c': 3}}}
    assert set_tree_node(dct, 'a:b:c:d', 4) == {'a': {'b': {'c': {'d': 4}}}}

# Generated at 2022-06-14 06:47:33.649106
# Unit test for function set_tree_node
def test_set_tree_node():
    mapping = {}
    set_tree_node(mapping, 'foo:bar:baz', 'qux')
    assert mapping['foo']['bar']['baz'] == 'qux'



# Generated at 2022-06-14 06:47:43.168628
# Unit test for function set_tree_node
def test_set_tree_node():
    """
    Test set_tree_node unit.
    """
    to_test = {
        'foo': {},
        'bar': {},
        'baz': {},
    }
    set_tree_node(to_test, 'foo:bar:baz', 'yep')
    assert to_test['foo']['bar']['baz'] == 'yep'



# Generated at 2022-06-14 06:47:49.622101
# Unit test for function set_tree_node
def test_set_tree_node():
    obj = {}
    set_tree_node(obj, 'foo:bar:baz', 'foobarbaz')
    assert obj['foo']['bar']['baz'] == 'foobarbaz'
    set_tree_node(obj, 'foo', 'foobarbaz')
    assert obj['foo'] == 'foobarbaz'
    set_tree_node(obj, '', 'foobarbaz')
    assert obj == 'foobarbaz'



# Generated at 2022-06-14 06:48:02.999862
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = {
        'foo': {
            'bar': 'baz',
            'sum': {
                'sub': 'subdir'
            }
        },
        'numbers': {
            '1': 'one',
            '2': {
                '3': 'three'
            }
        }
    }
    assert get_tree_node(mapping, 'foo:bar') == 'baz'
    assert get_tree_node(mapping, 'foo:sum:sub') == 'subdir'
    assert get_tree_node(mapping, 'numbers:1', 'none') == 'one'
    assert get_tree_node(mapping, 'numbers:2:3', 'none') == 'three'

# Generated at 2022-06-14 06:48:07.607818
# Unit test for function set_tree_node
def test_set_tree_node():
    test = {}
    set_tree_node(test, 'foo:bar:baz', 'arglebargle')
    assert test == {'foo': {'bar': {'baz': 'arglebargle'}}}



# Generated at 2022-06-14 06:48:16.545840
# Unit test for function set_tree_node
def test_set_tree_node():
    tree = Tree()
    tree.update({
        'level1_0': {
            'level2_0': {
                'level3_0': {
                    'level4_0': 'value',
                }
            }
        }
    })
    set_tree_node(tree, 'level1_1:level2_1:level3_1:level4_1', 'value')
    assert tree['level1_1:level2_1:level3_1:level4_1'] == 'value'

# Generated at 2022-06-14 06:48:21.929524
# Unit test for function set_tree_node
def test_set_tree_node():
    cfg = {}
    ret = set_tree_node(cfg, 'a:n:s:s:k:s:s', 't e s t')
    assert ret['n']['s']['k']['s'] == 't e s t'



# Generated at 2022-06-14 06:48:35.478491
# Unit test for function get_tree_node
def test_get_tree_node():
    """Unit test for `get_tree_node`"""
    mapping = {'foo': {'bar': {'baz': 'foobar'}}}
    assert get_tree_node(mapping, 'foo:bar:baz') == 'foobar'
    assert get_tree_node(mapping, 'foo:bar') == {'baz': 'foobar'}
    assert get_tree_node(mapping, 'foo') == {'bar': {'baz': 'foobar'}}
    assert get_tree_node(mapping, 'foo:bar:whatever', default='nope') == 'nope'
    assert get_tree_node(mapping, 'foo:bar:baz', parent=True) == {'baz': 'foobar'}

# Generated at 2022-06-14 06:48:41.011337
# Unit test for function set_tree_node
def test_set_tree_node():
    mapping = {}
    set_tree_node(mapping, 'a', 1)
    set_tree_node(mapping, 'a:b', 2)
    set_tree_node(mapping, 'a:b:c', 3)

    assert mapping == {
        'a': {
            'b': {
                'c': 3
            }
        }
    }



# Generated at 2022-06-14 06:48:53.303157
# Unit test for function set_tree_node
def test_set_tree_node():
    import unittest

    class TestTreeNode(unittest.TestCase):

        def test_set_node(self):
            # Basic test tree:
            test_tree = {
                'id': 'root',
                'value': 'A',
                'children': [
                    {
                        'id': 'child1',
                        'value': 'A1',
                        'children': []
                    },
                    {
                        'id': 'child2',
                        'value': 'A2',
                        'children': []
                    }
                ]
            }

# Generated at 2022-06-14 06:49:06.031075
# Unit test for function get_tree_node
def test_get_tree_node():
    """
    Unit test for `get_tree_node`.

    """
    mapping = {
        'foo': 'bar',
        'baz': {
            'shmoo': {
                'moo': 'cow'
            }
        }
    }

    assert get_tree_node(mapping, 'foo') == 'bar'
    assert get_tree_node(mapping, 'baz') == mapping['baz']
    assert get_tree_node(mapping, 'baz:shmoo:moo') == 'cow'

    assert get_tree_node(mapping, 'baz:shmoo:moo', default='nope') == 'cow'
    assert get_tree_node(mapping, 'baz:shmoo:nope', default='nope') == 'nope'


# Generated at 2022-06-14 06:49:23.252267
# Unit test for function get_tree_node
def test_get_tree_node():
    """
    Testing function get_tree_node
    """
    test_dict = {
        'a': {'b': {
            'c': '1',
            'd': {
                'e': '2',
                'f': '3',
            }
        }},
        'g': {
            'b': {
                'c': '4',
                'd': {
                    'e': '5',
                    'f': '6',
                }
            }
        },
        'h': 7
    }

    # 1. Check that a correct path will return correct value
    assert get_tree_node(test_dict, 'a:b:d:e') == '2'

    # 2. Check that an invalid path will raise KeyError
    with pytest.raises(KeyError):
        get_tree

# Generated at 2022-06-14 06:49:32.678461
# Unit test for function get_tree_node
def test_get_tree_node():
    mappings = [
        {
            'test': {
                'test1': {
                    'test11': 'test',
                    'test12': 1,
                    'test13': 'test_get_tree_node:test:test1',
                },
                'test2': 'test2',
                'test3': 'test3',
            },
        },
        tree(),
    ]

    for mapping in mappings:
        mapping['test']['test1']['test11'] = 'test'
        mapping['test']['test1']['test12'] = 1
        mapping['test']['test1']['test13'] = 'test_get_tree_node:test:test1'
        mapping['test']['test2'] = 'test2'

# Generated at 2022-06-14 06:49:40.432606
# Unit test for function get_tree_node
def test_get_tree_node():
    # Test behavior with a flat namespace
    mapping = {'one': 1, 'two': 2, 'three': 3}
    assert get_tree_node(mapping, 'one') is 1
    assert get_tree_node(mapping, 'one:') is 1
    assert get_tree_node(mapping, 'one:two') is 2
    assert get_tree_node(mapping, 'nonexistent') is _sentinel
    try:
        get_tree_node(mapping, 'nonexistent')
    except KeyError:
        pass
    else:
        raise AssertionError('Must raise KeyError')

    # Test with a nested namespace
    mapping = {'root': {'one': 1, 'two': 2, 'three': 3}}
    assert get_tree_node(mapping, 'root')['one']

# Generated at 2022-06-14 06:49:53.502725
# Unit test for function set_tree_node
def test_set_tree_node():
    """
    Regression test for set_tree_node.
    """
    value = {'a': 1}
    node = set_tree_node(value, 'b:c:d:e:f', 5)
    assert node == {'a': 1, 'b': {'c': {'d': {'e': {'f': 5}}}}}

    value = {'a': 1}
    node = set_tree_node(value, 'b:c:d:e:f', 5)
    assert value == {'a': 1, 'b': {'c': {'d': {'e': {'f': 5}}}}}

    node = set_tree_node(value, 'b:c:d:e:f:g', 10)

# Generated at 2022-06-14 06:50:03.205591
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = {
        'key0': {
            'key0.key1': {
                'key0.key1.key2': 'value'
            }
        },
        'key4': 'value4'
    }
    assert get_tree_node(mapping, 'key0:key0.key1.key2') == 'value'
    assert get_tree_node(mapping, 'key0:key0.key1.key2', default='default') == 'value'
    assert get_tree_node(mapping, 'key0:key0.key1.key2', parent=True) == {'key0.key1.key2': 'value'}
    assert get_tree_node(mapping, 'key0:key0.key1.key3', default='default') == 'default'
    assert get

# Generated at 2022-06-14 06:50:09.751056
# Unit test for function get_tree_node
def test_get_tree_node():  # pragma: no cover
    tree = {'root': {
        'a': {
            'b': {
                'c': 'd'
            }
        }
    }}
    assert get_tree_node(tree, 'a:b:c') == 'd'


if __name__ == '__main__':
    test_get_tree_node()

# Generated at 2022-06-14 06:50:19.432169
# Unit test for function get_tree_node
def test_get_tree_node():
    """
    Get specific node in a tree without having to know the structure of the tree.
    """
    import json
    import os

    fixture_file = os.path.join(os.path.dirname(__file__), 'fixtures/eslint-rules.json')
    with open(fixture_file, 'r') as f:
        data = json.loads(f.read(-1))

    # TODO Swap this with somthing more generic.
    expected = {'options': ['as-needed'],
                'severity': 'warning'}
    actual = get_tree_node(data, 'no-multi-spaces:options')

    assert(expected == actual)


if __name__ == '__main__':
    test_get_tree_node()

# Generated at 2022-06-14 06:50:25.086542
# Unit test for function set_tree_node
def test_set_tree_node():
    mapping = collections.defaultdict(dict)
    result = set_tree_node(mapping, 'a:b:c:d', 'foo')
    assert result == {'d': 'foo'}
    assert mapping == {'a': {'b': {'c': {'d': 'foo'}}}}



# Generated at 2022-06-14 06:50:27.433064
# Unit test for function set_tree_node
def test_set_tree_node():
    mapping = {}
    set_tree_node(mapping, 'a:b:c:d:e:f', 1)
    assert mapping == {'a': {'b': {'c': {'d': {'e': {'f': 1}}}}}}



# Generated at 2022-06-14 06:50:34.622383
# Unit test for function get_tree_node
def test_get_tree_node():
    tree_data = {
        'a': {
            'b': {
                'c': 'd',
            },
        },
    }

    assert get_tree_node(tree_data, 'a:b:c', default='x') == 'd'
    assert get_tree_node(tree_data, 'a:b:c') == 'd'
    assert get_tree_node(tree_data, 'a:b:c:d', default='x') == 'x'
    assert get_tree_node(tree_data, 'a:b:c:d') == 'x'



# Generated at 2022-06-14 06:50:48.275155
# Unit test for function get_tree_node
def test_get_tree_node():
    tree = {
        'a': {
            'b': {
                'c': 55
            }
        }
    }
    assert get_tree_node(tree, 'a:b:c') == 55



# Generated at 2022-06-14 06:50:59.313454
# Unit test for function get_tree_node
def test_get_tree_node():
    # Setup data
    mapping = {
        'a': {
            'b': {
                'c': 'foo'}}
    }

    # Test simple key retrieval
    assert get_tree_node(mapping, 'a') == {'b': {'c': 'foo'}}

    # Test simple key retrieval with default
    assert get_tree_node(mapping, 'TWO', default='bar') == 'bar'

    # Test multidimension retrieval
    assert get_tree_node(mapping, 'a:b') == {'c': 'foo'}

    # Test multidimension value retrieval
    assert get_tree_node(mapping, 'a:b:c') == 'foo'

# Generated at 2022-06-14 06:51:05.825440
# Unit test for function get_tree_node
def test_get_tree_node():
    assert get_tree_node({'a': {'b': 1}}, 'b') == 1
    assert get_tree_node({'a': {'b': 1}}, 'b:c') == 1
    assert get_tree_node({'a': {'b': 1}}, 'b', default=None) is None

    with pytest.raises(KeyError):
        get_tree_node({'a': {'b': 1}}, 'c')

    assert get_tree_node({'a': {'b': 1}}, 'c', default='d') == 'd'

    with pytest.raises(KeyError):
        get_tree_node({'a': {'b': 1}, 'ab': {'cd': 2}}, 'a:cd')


# Generated at 2022-06-14 06:51:17.070411
# Unit test for function get_tree_node
def test_get_tree_node():
    class Test:
        pass

    test = Test()
    test.tree = tree()
    test.tree['a']['b']['c']['d'] = 1

    # Test for standard non-nested node
    assert get_tree_node(test.tree, 'a') == {'b': {'c': {'d': 1}}}

    # Test for nested node
    assert get_tree_node(test.tree, 'a:b:c') == {'d': 1}

    # Test for deeply nested node
    assert get_tree_node(test.tree, 'a:b:c:d') == 1

    # Test for parent node (non-nested)
    assert get_tree_node(test.tree, 'a', parent=True) == test.tree

    # Test for parent node (nested)

# Generated at 2022-06-14 06:51:23.000753
# Unit test for function get_tree_node
def test_get_tree_node():
    # Test most basic functionality
    test_mapping = {
        'hello': 'world',
        'foo': {
            'bar': 'baz',
        },
    }
    assert get_tree_node(test_mapping, 'hello') == 'world'
    assert get_tree_node(test_mapping, 'foo:bar') == 'baz'

    # Test default value
    assert get_tree_node(test_mapping, 'spam:ham:eggs', default='spam') == 'spam'

    # Test parent node
    assert get_tree_node(test_mapping, 'foo:bar', parent=True) == test_mapping['foo']

    # Test ValueError

# Generated at 2022-06-14 06:51:26.321292
# Unit test for function set_tree_node
def test_set_tree_node():
    test_mapping = Tree()
    set_tree_node(test_mapping, "a:b", 5)
    assert test_mapping["a"] == {"b": 5}



# Generated at 2022-06-14 06:51:36.632821
# Unit test for function get_tree_node
def test_get_tree_node():
    assert (
        get_tree_node(
            tree({
                'a': {
                    'b': {
                        'c': {
                            'd': 'e'
                        }
                    }
                }
            }),
            'a:b:c:d'
        )
    ) == 'e'

    # Test default
    assert (
        get_tree_node(
            tree({
                'a': {
                    'b': {
                        'c': {
                            'd': 'e'
                        }
                    }
                }
            }),
            'a:b:c:f',
            default='g'
        )
    ) == 'g'


# Generated at 2022-06-14 06:51:48.581652
# Unit test for function get_tree_node
def test_get_tree_node():
    data = {
        'a': 1,
        'key': {
            'version': 2,
            'value': 'val',
        }
    }
    # Test it exists
    assert get_tree_node(data, 'a') == 1
    assert get_tree_node(data, 'a:b') is _sentinel
    # Test it does not exist
    assert get_tree_node(data, 'b', default='default') == 'default'
    assert get_tree_node(data, 'b') is _sentinel
    # Test traversal
    assert get_tree_node(data, 'key:version') == 2
    # Test traversal down a path that does not exist
    assert get_tree_node(data, 'key:version:fucker') is _sentinel

# Generated at 2022-06-14 06:51:56.479497
# Unit test for function set_tree_node
def test_set_tree_node():
    x = tree()

    set_tree_node(x, 'key', 'value')
    assert x['key'] == 'value'

    set_tree_node(x, 'foo:bar:baz', 'value')
    assert x['foo']['bar']['baz'] == 'value'

    set_tree_node(x, 'foo:bar:baz:bam', 'value')
    assert x['foo']['bar']['baz']['bam'] == 'value'



# Generated at 2022-06-14 06:52:06.283150
# Unit test for function set_tree_node
def test_set_tree_node():
    """Test ``set_tree_node`` function."""
    mapping = tree()
    set_tree_node(mapping, 'foo:bar:baz', 'test')
    assert mapping['foo']['bar']['baz'] == 'test'
    mapping['foo']['bar']['baz'] = 'test2'
    assert mapping['foo']['bar']['baz'] == 'test2'

    mapping = {}
    set_tree_node(mapping, 'foo:bar:baz', 'test')
    assert mapping['foo']['bar']['baz'] == 'test'
    mapping['foo']['bar']['baz'] = 'test2'
    assert mapping['foo']['bar']['baz'] == 'test2'

# Generated at 2022-06-14 06:52:29.052629
# Unit test for function get_tree_node
def test_get_tree_node():
    test_data = {
        "test": {
            "two": {
                "three": 3,
            },
        },
    }
    assert get_tree_node(test_data, "test:two:three") == 3



# Generated at 2022-06-14 06:52:35.310204
# Unit test for function set_tree_node
def test_set_tree_node():
    import yaml
    test_tree = tree()
    set_tree_node(test_tree, 'test:t:e:s:t', 'test')
    assert yaml.safe_dump(test_tree, default_flow_style=False) == """
test:
  t:
    e:
      s:
        t: test
""".lstrip()



# Generated at 2022-06-14 06:52:36.994820
# Unit test for function get_tree_node

# Generated at 2022-06-14 06:52:46.827836
# Unit test for function get_tree_node
def test_get_tree_node():
    tree = {
        'foo': {
            'bar': {
                'baz': 42
            }
        }
    }
    assert get_tree_node(tree, 'foo:bar:baz') == 42
    assert get_tree_node(tree, 'foo') == {'bar': {'baz': 42}}
    with pytest.raises(KeyError):
        get_tree_node(tree, 'foo:bar:baz:qux')
    assert get_tree_node(tree, 'foo:bar:baz:qux', default='moop') == 'moop'

# Generated at 2022-06-14 06:52:57.432228
# Unit test for function get_tree_node
def test_get_tree_node():
    a = tree()
    a['a1']['a2'] = 'test'
    assert get_tree_node(a, 'a1:a2') == 'test'
    assert get_tree_node(a, 'a1:a2', default='test2') == 'test'
    try:
        get_tree_node(a, 'a1:a2:a3')
    except KeyError:
        assert True
    else:
        assert False

    # Test that it returns parent node
    assert get_tree_node(a, 'a1:a2', parent=True) == a['a1']



# Generated at 2022-06-14 06:53:03.922706
# Unit test for function get_tree_node
def test_get_tree_node():
    d = tree()
    set_tree_node(d, 'a:b:c', 'C')
    set_tree_node(d, 'a:d', 'D')
    assert get_tree_node(d, 'a:b:c') == 'C'
    assert get_tree_node(d, 'a:d') == 'D'
    assert get_tree_node(d, 'f', default='F') == 'F'
    assert get_tree_node(d, 'g', default=_sentinel)



# Generated at 2022-06-14 06:53:16.583073
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = {
        'animal': {
            'mammal': {
                'canine': {
                    'dog': 'woof'
                }
            },
            'primate': {
                'hominid': {
                    'human': 'i am a panda'
                }
            },
            'panda': {
                'bear': 'i am a panda'
            },
            'bear': 'i am a panda'
        }
    }
    assert get_tree_node(mapping, 'animal:mammal:canine:dog') == 'woof'
    assert get_tree_node(mapping, 'animal:bear', default='no bear') == 'i am a panda'

# Generated at 2022-06-14 06:53:20.341734
# Unit test for function set_tree_node
def test_set_tree_node():
    from pprint import pprint
    tree = {}
    set_tree_node(tree, 'a:b:c:d', 'Value!')
    pprint(tree)



# Generated at 2022-06-14 06:53:29.061253
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = tree()
    mapping['a']['b']['c'] = 12
    assert get_tree_node(mapping, 'a:b') == {'c': 12}
    assert get_tree_node(mapping, 'a:b:c') == 12
    assert get_tree_node(mapping, 'a:b:c', parent=True) == {'c': 12}
    assert get_tree_node(mapping, 'a:b', default=None, parent=True) is None



# Generated at 2022-06-14 06:53:37.200491
# Unit test for function set_tree_node
def test_set_tree_node():
    """
    The following code should produce the following mapping:

        {
            'key': {
                'name': 'value'
            }
        }

    :return:
    """

    # Arrange
    mapping = {}
    key = 'key:name'
    value = 'value'

    # Act
    set_tree_node(mapping, key, value)

    # Assert
    assert mapping == {
        'key': {
            'name': 'value'
        }
    }



# Generated at 2022-06-14 06:54:24.419589
# Unit test for function get_tree_node
def test_get_tree_node():
    pass
    # assert get_tree_node({'a': {'b': {'c': 1}}}, 'a:b:c') == 1
    # assert get_tree_node({'a': {'b': {'c': 1}}}, 'a:b:c', default=2) == 1
    # assert get_tree_node({'a': {'b': {'c': 1}}}, 'a:b:c', default=2, parent=True) == {'c': 1}
    # assert get_tree_node({'a': {'b': {'c': 1}}}, 'a:b:bogus', default=2) == 2
    #
    # with pytest.raises(KeyError):
    #     assert get_tree_node({'a': {'b': {'c': 1}}}, '

# Generated at 2022-06-14 06:54:29.442749
# Unit test for function set_tree_node
def test_set_tree_node():
    registry = Tree()
    registry['foo'] = 'bar'
    registry['foo:bar:bazonk'] = 123
    assert registry['foo:bar:bazonk'] == 123
    assert registry['foo'] == 'bar'



# Generated at 2022-06-14 06:54:39.473369
# Unit test for function get_tree_node
def test_get_tree_node():
    """
    For the following tree structure::

        {
          "lorem": {
            "ipsum": {
              "dolor": "sit amet",
              "consetetur": "sadipscing"
            }
          }
        }

    """
    tree = {
        "lorem": {
            "ipsum": {
                "dolor": "sit amet",
                "consetetur": "sadipscing",
            },
        },
    }

    # Fetch the requested node
    assert get_tree_node(tree, "lorem:ipsum:dolor") == "sit amet"

    # Fetch a node that does not exist, triggering a KeyError exception

# Generated at 2022-06-14 06:54:47.889071
# Unit test for function get_tree_node
def test_get_tree_node():
    # Setup
    tree_dict = {
        'x': {
            'y': {
                'z': 1
            }
        }
    }

    # Verify
    assert get_tree_node(tree_dict, 'x:y:z') == 1
    assert get_tree_node(tree_dict, 'x:y:z:w') is _sentinel
    assert get_tree_node(tree_dict, 'x:y:z:w', default=None) is None



# Generated at 2022-06-14 06:54:54.521673
# Unit test for function set_tree_node
def test_set_tree_node():
    tree = {}
    set_tree_node(tree, "1", 9)
    set_tree_node(tree, "x:y:z", 42)
    set_tree_node(tree, "x:y:a", 6)

    assert tree == {
        "1": 9,
        "x": {
            "y": {
                "z": 42,
                "a": 6
            }
        }
    }



# Generated at 2022-06-14 06:55:00.079200
# Unit test for function set_tree_node
def test_set_tree_node():
    tree = {}
    set_tree_node(tree, 'foo', 'bar')
    set_tree_node(tree, 'bar:foo', 'baz')
    assert tree == {'foo': 'bar', 'bar': {'foo': 'baz'}}



# Generated at 2022-06-14 06:55:08.444356
# Unit test for function set_tree_node
def test_set_tree_node():
    _tree = tree()
    assert _tree.setdefault('foo', 'bar') == 'bar'
    assert _tree.setdefault('foo', 'baz') == 'bar'
    assert _tree['foo'] == 'bar'
    # Double check we don't get the default value
    assert _tree.setdefault('foobar', 'baz') == 'baz'
    assert _tree['foobar'] == 'baz'


# Test for function remove_tree_node

# Generated at 2022-06-14 06:55:15.342602
# Unit test for function set_tree_node
def test_set_tree_node():
    """
    Test for setting arbitrary node on tree-like data structure
    """
    # TODO Write better tests! Really.
    assert set_tree_node(
        {'a': {'b': {'c': {'d': True}}}},
        'a:b:c:e',
        True
    ) == {'a': {'b': {'c': {'d': True, 'e': True}}}}



# Generated at 2022-06-14 06:55:25.294561
# Unit test for function get_tree_node
def test_get_tree_node():
    t = Tree({'a': {'b': {'c': 1}}})
    assert get_tree_node(t, 'a:b:c') == 1
    assert get_tree_node(t, 'a:b') == {'c': 1}
    assert get_tree_node(t, 'a') == {'b': {'c': 1}}
    assert get_tree_node(t, 'a:b:d') == _sentinel
    try:
        get_tree_node(t, 'a:b:d')
    except KeyError:
        pass
    else:
        raise AssertionError('Expected KeyError.')
    assert get_tree_node(t, 'a:b:d', []) == []



# Generated at 2022-06-14 06:55:35.249735
# Unit test for function get_tree_node
def test_get_tree_node():
    my_dict = {'a': {'b': {'c': 1}}}
    assert get_tree_node(my_dict, 'a:b:c') == 1
    try:
        get_tree_node(my_dict, 'a:b:c:d')
        # Should not get here, expected KeyError
        assert False
    except KeyError:
        pass
    assert get_tree_node(my_dict, 'a:b:c:d', default=42) == 42
    assert get_tree_node(my_dict, 'a', default=42) == {'b': {'c': 1}}

