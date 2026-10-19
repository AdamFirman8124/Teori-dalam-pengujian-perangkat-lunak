

# Generated at 2022-06-14 06:46:16.815883
# Unit test for constructor of class Tree
def test_Tree():
    # Tree creation
    t = Tree([('a', 1), ('b:c', 2), ('b:d', 3)])
    assert t.viewitems() == [('a', 1), ('b', {'c': 2, 'd': 3})], t

    # Tree creation from another tree, specifying namespace
    t2 = Tree(t, 'foo')
    assert t2.viewitems() == [('foo:a', 1), ('foo:b', {'c': 2, 'd': 3})], t2

    # Tree creation from another tree, specifying namespace, but with initial_is_ref=True
    t2 = Tree(t, 'foo', initial_is_ref=True)
    assert t2.viewitems() == [('foo:a', 1), ('foo:b', {'c': 2, 'd': 3})], t2

# Generated at 2022-06-14 06:46:24.714619
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = {
        'foo': {
            'bar': 'baz'
        }
    }
    assert get_tree_node(mapping, 'foo:bar') == 'baz'
    assert get_tree_node(mapping, 'foo:bar', default='doh') == 'baz'
    assert get_tree_node(mapping, 'doh:bar', default='doh') == 'doh'



# Generated at 2022-06-14 06:46:29.552344
# Unit test for function get_tree_node
def test_get_tree_node():
    data = {'foo': {'bar': 1}}
    assert get_tree_node(data, 'foo:bar') == 1
    assert get_tree_node(data, 'foo:baz', default=2) == 2


if __name__ == '__main__':
    test_get_tree_node()

# Generated at 2022-06-14 06:46:33.089242
# Unit test for function set_tree_node
def test_set_tree_node():
    tree = dict()
    set_tree_node(tree, 'this.is.a.test', 'this is a test')
    assert tree['this']['is']['a']['test'] == 'this is a test'



# Generated at 2022-06-14 06:46:42.721513
# Unit test for function set_tree_node
def test_set_tree_node():
    test_tree = tree()
    set_tree_node(test_tree, "a:a", 1)
    assert test_tree["a"]["a"] == 1
    set_tree_node(test_tree, "b:b:b", 2)
    assert test_tree["b"]["b"]["b"] == 2
    set_tree_node(test_tree, "b:b:c", 3)
    assert test_tree["b"]["b"]["c"] == 3

# Generated at 2022-06-14 06:46:48.657507
# Unit test for function get_tree_node
def test_get_tree_node():
    with pytest.raises(KeyError):
        assert get_tree_node({}, 'foo')
    assert get_tree_node({'foo': 'bar'}, 'foo') == 'bar'
    assert get_tree_node({'foo': 'bar'}, 'foo', default=None) is None



# Generated at 2022-06-14 06:46:51.975904
# Unit test for function set_tree_node
def test_set_tree_node():
    m = tree()
    set_tree_node(m, 'foo', 'bar')
    assert get_tree_node(m, 'foo') == 'bar'



# Generated at 2022-06-14 06:47:05.419412
# Unit test for function get_tree_node

# Generated at 2022-06-14 06:47:16.793884
# Unit test for function get_tree_node
def test_get_tree_node():
    tree = {
        'a': {
            'b': {
                'c': 1,
            },
            'd': 2,
        },
        'e': 3,
    }

    assert get_tree_node(tree, 'a:b:c') == 1
    assert get_tree_node(tree, 'a:b:c', parent=True) == {'c': 1}
    assert get_tree_node(tree, 'a:b:c', parent=True)['c'] == 1
    assert get_tree_node(tree, 'a:e', default=4) == 4
    assert get_tree_node(tree, 'a:e') == 4
    assert get_tree_node(tree, 'a:b:c', parent=True) == {'c': 1}
    assert get_tree_node

# Generated at 2022-06-14 06:47:23.219578
# Unit test for function set_tree_node
def test_set_tree_node():
    tree = Tree()
    tree.set_tree_node({
        'foo': {
            'bar': 'quux',
        }
    }, 'foo:bar:baz', 'quuz')
    assert tree['foo']['bar']['baz'] == 'quuz'



# Generated at 2022-06-14 06:47:38.457445
# Unit test for function get_tree_node
def test_get_tree_node():
    x = Tree()

    x['test1'] = 'value1'
    x['test2'] = 'value2'
    x['test:test2'] = 'value2'
    x['test:test3:test4'] = 'value3'
    x['test:something:else:value'] = 'something'

    assert x['test1'] == 'value1'
    assert x['test2'] == 'value2'
    assert x['test:test3:test4'] == 'value3'
    assert x['test:something'] == Tree(namespace='test:something')
    assert x['test:something:else'] == Tree(namespace='test:something:else')
    assert x['test:something:else:value'] == 'something'
    assert x.get('nothing', 'nothing') == 'nothing'
    assert x

# Generated at 2022-06-14 06:47:48.673508
# Unit test for function get_tree_node
def test_get_tree_node():
    import pytest
    tree = Tree({'a': {'b': {'c': 'd'}}})
    assert get_tree_node(tree, 'a:b:c') == 'd'
    assert get_tree_node(tree, 'a') == {'b': {'c': 'd'}}
    assert get_tree_node(tree, 'b') == Tree()
    assert get_tree_node(tree, 'b', default='waffles', parent=True) == tree
    assert get_tree_node(tree, 'b', default='waffles') == 'waffles'
    with pytest.raises(KeyError):
        get_tree_node(tree, 'b')



# Generated at 2022-06-14 06:47:57.799793
# Unit test for function get_tree_node

# Generated at 2022-06-14 06:48:08.644169
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = {
        'foo': {
            'bar': 'baz',
        },
        'bar': 'baz',
    }

    # Check non-existent node
    try:
        get_tree_node(mapping, 'foo:bar:baz')
        assert False
    except KeyError as exc:
        assert str(exc) == "'foo:bar:baz'"

    # Check non-existent node with default arg
    assert get_tree_node(mapping, 'foo:bar:baz', default='foobar') == 'foobar'

    # Check parent node
    assert get_tree_node(mapping, 'foo:bar:baz', parent=True) == {'baz': 'baz'}

    # Check parent node without default arg

# Generated at 2022-06-14 06:48:16.685187
# Unit test for function get_tree_node
def test_get_tree_node():
    t = tree()
    t['foo']['bar']['baz'] = 'bam'
    assert get_tree_node(t, 'foo:bar:baz') == 'bam'
    assert get_tree_node(t, 'foo:bar:baz:bat', default='bat') == 'bat'
    try:
        get_tree_node(t, 'foo:bar:baz:bat')
    except KeyError:
        pass
    else:
        raise AssertionError



# Generated at 2022-06-14 06:48:25.460593
# Unit test for function get_tree_node
def test_get_tree_node():
    tree = {
        u'entities': {
            u'nodes': {
                u'node_type': {
                    u'index': u'index1',
                    u'type': u'type1'
                }
            }
        },
        u'indices': {
            u'index1': {
                u'aliases': [
                    u'alias1'
                ],
                u'name': u'index1'
            }
        }
    }

    assert get_tree_node(tree, u'indices:index1') is tree[u'indices'][u'index1']
    assert get_tree_node(tree, u'indices:index1:aliases') is tree[u'indices'][u'index1'][u'aliases']

# Generated at 2022-06-14 06:48:35.912787
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = {
        'a': {
            'b': {
                'c': 'TEST'
            }
        }
    }
    assert get_tree_node(mapping, 'a:b:c') == 'TEST'
    assert get_tree_node(mapping, 'a:b:c:d') is _sentinel

    assert get_tree_node(mapping, 'a:b:c', default='DEFAULT') == 'TEST'
    assert get_tree_node(mapping, 'a:b:c:d', default='DEFAULT') == 'DEFAULT'

# Generated at 2022-06-14 06:48:44.273546
# Unit test for function get_tree_node
def test_get_tree_node():
    test_dict = {
        'key1': 'value1',
        'key2': {
            'key2.1': {
                'key2.1.1': 'value2.1.1'
            },
            'key2.2': 'value2.2'
        },
        'key3': 'value3'
    }
    assert get_tree_node(test_dict, 'key1') == 'value1', 'Test root value'
    assert get_tree_node(test_dict, 'key2') == test_dict['key2'], 'Test returning parent node'
    assert get_tree_node(test_dict, 'key2:key2.1') == test_dict['key2']['key2.1'], 'Test deep parent node'

# Generated at 2022-06-14 06:48:55.698383
# Unit test for function set_tree_node
def test_set_tree_node():
    d = {}
    set_tree_node(d, 'key', 1)
    set_tree_node(d, 'key2', 2)
    set_tree_node(d, 'key:a', 3)
    set_tree_node(d, 'key:b', 4)
    set_tree_node(d, 'key2:a', 5)
    set_tree_node(d, 'key2:b', 6)
    set_tree_node(d, 'key2:b:c', 7)
    set_tree_node(d, 'key2:b:d', 8)

# Generated at 2022-06-14 06:49:02.652167
# Unit test for function set_tree_node
def test_set_tree_node():
    test = tree()
    set_tree_node(test, 'foo:bar:baz', 'spam')
    assert test['foo']['bar']['baz'] == 'spam'
    test = Tree()
    test.set_tree_node('foo:bar:baz', 'spam')
    assert test['foo']['bar']['baz'] == 'spam'



# Generated at 2022-06-14 06:49:14.711092
# Unit test for function get_tree_node
def test_get_tree_node():

    d = {'a': {'b': {'c': 'd'}}}

    assert get_tree_node(d, 'a:b:c') == 'd'
    assert get_tree_node(d, 'a:b:c', parent=True) == {'c': 'd'}
    assert get_tree_node(d, 'a:b:d') == _sentinel
    assert get_tree_node(d, 'a:b:d', default='e') == 'e'



# Generated at 2022-06-14 06:49:24.517368
# Unit test for function get_tree_node
def test_get_tree_node():
    tree = {
        'lorem': 'ipsum',
        'foo': {
            'bar': {
                'baz': 'buz'
            }
        }
    }

    # Specify deep node
    assert get_tree_node(tree, 'foo:bar:baz') == 'buz'

    # Specify root node
    assert get_tree_node(tree, 'lorem') == 'ipsum'

    # Specify missing node
    with pytest.raises(KeyError):
        get_tree_node(tree, 'not:a:node')



# Generated at 2022-06-14 06:49:30.295894
# Unit test for function get_tree_node
def test_get_tree_node():
    tree = {
        'asd': {
            'asdad': {
                'asdasd': 'value',
            },
        },
    }
    assert get_tree_node(tree, 'asd:asdad:asdasd') == 'value'
    assert get_tree_node(tree, 'asd:asdad:asdasd:asda') == _sentinel



# Generated at 2022-06-14 06:49:38.566657
# Unit test for function get_tree_node
def test_get_tree_node():
    assert get_tree_node({'foo': {'bar': True}}, 'foo:bar')
    assert get_tree_node({'foo': {'bar': True}}, 'foo:bar', default=False)
    assert not get_tree_node({'foo': {'bar': True}}, 'foo:not_bar', default=False)
    with pytest.raises(KeyError):
        get_tree_node({'foo': {'bar': True}}, 'foo:not_bar')

# Generated at 2022-06-14 06:49:43.927886
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = {
        'a': 1,
        'b': {
            'c': 2,
        },
    }

    # Test that we get the correct value from a tree
    assert get_tree_node(mapping, 'a') == 1
    assert get_tree_node(mapping, 'b:c') == 2

    # Test that we get the correct KeyError
    with pytest.raises(KeyError):
        get_tree_node(mapping, 'a:b')
    with pytest.raises(KeyError):
        get_tree_node(mapping, 'a:b:c')

    # Test that we get the correct default
    assert get_tree_node(mapping, 'a:b:c', default=3) == 3

# Generated at 2022-06-14 06:49:52.103061
# Unit test for function set_tree_node
def test_set_tree_node():
    """
    Test for set_tree_node that verifies that it creates missing keys.
    """

    test_mapping = dict()

    # Test 1: Key does not exist
    assert set_tree_node(test_mapping, 'foo:bar', 'baz') == {'foo': {'bar': 'baz'}}

    # Test 2: Key already exists
    assert set_tree_node(test_mapping, 'foo:bar', 'qux') == {'foo': {'bar': 'qux'}}

# Generated at 2022-06-14 06:50:02.362938
# Unit test for function get_tree_node
def test_get_tree_node():
    """Function get_tree_node"""

    # Standard test
    v = get_tree_node({'a': 'b', 'c': {'d': 'e'}}, 'c:d', default='f')
    assert v == 'e'

    # Test default
    v = get_tree_node({'a': 'b', 'c': {'d': 'e'}}, 'c:f', default='f')
    assert v == 'f'

    # Test exception
    try:
        get_tree_node({'a': 'b', 'c': {'d': 'e'}}, 'c:f')
    except KeyError:
        pass
    else:
        raise AssertionError('Expected exception not raised')

# Generated at 2022-06-14 06:50:14.333449
# Unit test for function get_tree_node
def test_get_tree_node():
    _test_data = {
        'test': {
            'sub': {
                'sub': {
                    'sub': 'foo'
                }
            }
        },
        'bar': 'baz',
        'qux': {
            'quux': 'quuz',
            'corge': 'grault'
        }
    }
    assert get_tree_node(_test_data, 'test:sub:sub:sub') == 'foo'
    assert get_tree_node(_test_data, 'test') == {u'sub': {u'sub': {u'sub': u'foo'}}}
    assert get_tree_node(_test_data, 'bar') == 'baz'
    assert get_tree_node(_test_data, 'qux:quux') == 'quuz'



# Generated at 2022-06-14 06:50:23.461851
# Unit test for function set_tree_node
def test_set_tree_node():
    test_data = {'foo': {'bar': 'baz'}}
    set_tree_node(test_data, 'foo:bar', 'quux')
    assert test_data == {'foo': {'bar': 'quux'}}

    # Test a deeper node
    set_tree_node(test_data, 'foo:baz:bux', 'quux')
    assert test_data == {'foo': {'bar': 'quux', 'baz': {'bux': 'quux'}}}



# Generated at 2022-06-14 06:50:34.060963
# Unit test for function get_tree_node
def test_get_tree_node():
    tree = collections.OrderedDict()
    tree['a'] = collections.OrderedDict()
    tree['a']['b'] = collections.OrderedDict()
    tree['a']['b']['c'] = collections.OrderedDict()
    tree['a']['b']['c']['d'] = 'test'
    tree['a']['b']['c']['e'] = {'f': {'g': 'test'}}

    assert get_tree_node(tree, 'a:b:c:d') == 'test'
    assert get_tree_node(tree, 'a:b:c:e:f:g') == 'test'
    assert get_tree_node(tree, 'a:b:c:e:f:h') is _sentinel




# Generated at 2022-06-14 06:50:48.968203
# Unit test for function set_tree_node
def test_set_tree_node():
    mount = tree()
    set_tree_node(mount, 'root:node:sub-node', 'value')
    assert mount['root']['node']['sub-node'] == 'value'



# Generated at 2022-06-14 06:51:01.240438
# Unit test for function get_tree_node
def test_get_tree_node():
    # Basic tests
    mapping = {
        'a': 1,
        'b': {
            'c': 2,
            'd': 3,
        },
        'c': [
            1,
            2,
        ],
    }
    result = get_tree_node(mapping, 'a', default=None)
    assert result == 1
    result = get_tree_node(mapping, 'b:c', default=None)
    assert result == 2
    result = get_tree_node(mapping, 'c:0', default=None)
    assert result == 1

    # Error should be raised if not found
    try:
        get_tree_node(mapping, 'e')
    except KeyError:
        pass
    else:
        raise AssertionError('KeyError not raised')

    # Parent

# Generated at 2022-06-14 06:51:12.918892
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = {'a': {'b': {'c': 1, 'd': 2, '3': 3}}}
    assert get_tree_node(mapping, 'a:b:c') == 1

    try:
        get_tree_node(mapping, 'a:b:e')
    except Exception:
        pass
    else:
        raise AssertionError("Expected exception when executing get_tree_node({mapping}, 'a:b:e')".format(**locals()))

    assert get_tree_node(mapping, 'a:b:e', default=False) is False

    try:
        get_tree_node(mapping, 'a:b:3:3:3:3:3:3:3:3:3:3:3')
    except KeyError:
        pass

# Generated at 2022-06-14 06:51:22.476726
# Unit test for function get_tree_node
def test_get_tree_node():
    """Unit test for function `get_tree_node`."""
    test_tree = {'a': {'b': {'c': 3}}}
    assert get_tree_node(test_tree, 'a:b:c') == 3

    test_tree['a']['b']['d'] = 4

    assert get_tree_node(test_tree, 'a:b:d') == 4
    assert get_tree_node(test_tree, 'd:e:f') == _sentinel
    assert get_tree_node(test_tree, 'd:e:f', default=5) == 5



# Generated at 2022-06-14 06:51:28.516868
# Unit test for function get_tree_node
def test_get_tree_node():
    test_data = {
        'level1': {
            'level2': {
                'level3': 20
            }
        }
    }

    assert get_tree_node(test_data, 'level1:level2:level3') == 20
    assert get_tree_node(test_data, 'level1:level2:level3', default='nothing') == 20
    assert get_tree_node(test_data, 'level1:level2:level4', default='nothing') == 'nothing'



# Generated at 2022-06-14 06:51:32.032028
# Unit test for function set_tree_node
def test_set_tree_node():
    """Test set_tree_node function."""
    test = Tree()
    test.register('test:test:test', 'value')
    assert test.get('test:test:test') == 'value'



# Generated at 2022-06-14 06:51:39.093932
# Unit test for function get_tree_node
def test_get_tree_node():
    """Unit test for function `:func:get_tree_node`."""
    my_tree = tree()
    my_tree['a']['b']['c'] = 'd'
    # my_tree = get_tree_node(my_tree, 'a:b:c')
    assert get_tree_node(my_tree, 'a:b:c') == 'd'



# Generated at 2022-06-14 06:51:43.633742
# Unit test for function set_tree_node
def test_set_tree_node():
    """
    Test set_tree_node function.
    """
    tree = collections.defaultdict(tree)
    tree = {}
    path = 'one:two:three'
    set_tree_node(tree, path, 'thingy')
    assert tree['one']['two']['three'] == 'thingy'

# Generated at 2022-06-14 06:51:54.726993
# Unit test for function get_tree_node
def test_get_tree_node():
    # TODO Test for different kinds of mappings
    mapping = {
        'foo': {
            'bar': 'baz',
            'bom': {
                'boom': 'bloom',
            },
        },
        'foom': 'baz',
    }

    assert get_tree_node(mapping, 'foo:bar') == 'baz'
    assert get_tree_node(mapping, 'foo:bom:boom') == 'bloom'
    assert get_tree_node(mapping, 'bar', 'default') == 'default'
    try:
        get_tree_node(mapping, 'bar')
    except KeyError:
        pass



# Generated at 2022-06-14 06:52:05.713218
# Unit test for function get_tree_node
def test_get_tree_node():
    tree = {'a': {'b': {'c': {'d': {'e': 'f'}}}}}
    # Test exists
    assert get_tree_node(tree, 'a:b:c:d:e') == 'f'
    assert get_tree_node(tree, 'a:b:c:d:e', parent=True) == tree['a']['b']['c']['d']

    # Test override
    assert get_tree_node(tree, 'a:b:c:d:e', default=None) == 'f'
    assert get_tree_node(tree, 'b:c:d:e', default=None) is None

    # Test no override
    tree = {'a': {'b': {'c': {'d': {'e': 'f'}}}}}


# Generated at 2022-06-14 06:52:26.515074
# Unit test for function get_tree_node
def test_get_tree_node():
    d = {'a': {'b': 'c'}}
    assert get_tree_node(d, 'a:b') == 'c'
    assert get_tree_node(d, 'x:y', default='z') == 'z'

# Generated at 2022-06-14 06:52:32.859233
# Unit test for function set_tree_node
def test_set_tree_node():
    # Set up
    mapping = tree()
    key = 'k1:k2:k3'
    value = 'v1'
    # Test
    set_tree_node(mapping, key, value)
    # Assert
    expected = {'k1': {'k2': {'k3': 'v1'}}}
    assert mapping == expected



# Generated at 2022-06-14 06:52:36.098510
# Unit test for function get_tree_node
def test_get_tree_node():
    tree = {
        'foo': {
            'bar': 'baz'
        }
    }
    assert get_tree_node(tree, 'foo:bar') == 'baz'



# Generated at 2022-06-14 06:52:36.880581
# Unit test for function get_tree_node
def test_get_tree_node():
    pass



# Generated at 2022-06-14 06:52:48.652446
# Unit test for function get_tree_node
def test_get_tree_node():
    # Given

    nodes = {
        'file': 'test.txt',
        'meta': {
            'author': 'Benjamin',
            'size': 123
        },
        'log': {
            'message': 'MESSAGE',
            'errors': {
                'error4': 'ERROR4',
                'error5': {
                    'error6': 'ERROR6'
                }
            }
        }
    }

    # When
    res = get_tree_node(nodes, 'meta:size')

    # Then
    assert res == 123

    # When
    res = get_tree_node(nodes, 'meta:size:sub')

    # Then
    assert res == _sentinel

    # When

# Generated at 2022-06-14 06:53:01.385696
# Unit test for function get_tree_node
def test_get_tree_node():
    m = dict(
        a=1, b=dict(
            c=2, d=dict(e=3),
        ),
    )
    assert get_tree_node(m, 'a') == 1
    assert get_tree_node(m, 'b:c') == 2
    assert get_tree_node(m, 'b:d:e') == 3
    assert get_tree_node(m, 'b:d:e:f') == _sentinel

    r = dict(
        a=dict(f=1),
        b=dict(c=2, d=dict(e=3)),
    )
    assert get_tree_node(r, 'a:f:g:h') == _sentinel
    assert get_tree_node(r, 'a:f') == 1
    assert get_tree_

# Generated at 2022-06-14 06:53:08.853724
# Unit test for function get_tree_node
def test_get_tree_node():
    """Unit test"""
    mapping = {
        'n1': {
            'n2': {
                'n3': 'value'
            }
        }
    }

    assert get_tree_node(mapping, 'n1:n2:n3') == 'value'
    assert get_tree_node(mapping, 'n1:n2') == {'n3': 'value'}
    assert get_tree_node(mapping, 'n1:n2:n3:n4', default=None) is None
    assert get_tree_node(mapping, 'n1:n2:n3:n4') is _sentinel

# Generated at 2022-06-14 06:53:13.902632
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = {'foo': {'bar': 'baz'}}
    assert get_tree_node(mapping, 'foo:bar') == 'baz'


if __name__ == '__main__':
    import pytest
    pytest.main(__file__)

# Generated at 2022-06-14 06:53:21.469714
# Unit test for function get_tree_node
def test_get_tree_node():
    from pprint import pformat
    from copy import deepcopy

    import sys
    import os

    def print_failure_reason(reason, failure_reactions=None):
        failure_reactions = failure_reactions or ['pformat', 'pprint', 'pdb']
        for failure_reaction in failure_reactions:
            if failure_reaction == 'pformat':
                sys.stdout.write('Reason:\n')
                sys.stdout.write(pformat(reason))
                sys.stdout.write('\n')
            elif failure_reaction == 'pprint':
                import pprint
                pprint.pprint(reason)
            elif failure_reaction == 'pdb':
                import pdb
                pdb.set_trace()
            else:
                return


# Generated at 2022-06-14 06:53:31.749476
# Unit test for function get_tree_node
def test_get_tree_node():
    """Test function get_tree_node"""
    # Test all values except default
    my_tree = {"foo": {}}
    my_tree["foo"]["bar"] = "bar"

    assert get_tree_node(my_tree, "foo") == my_tree["foo"]
    assert get_tree_node(my_tree, "foo:bar") == "bar"

    # Test default value
    assert get_tree_node(my_tree, "foo:baz", default="abc") == "abc"

    # Test default value unset
    with pytest.raises(KeyError):
        get_tree_node(my_tree, "foo:baz")



# Generated at 2022-06-14 06:53:53.511628
# Unit test for function set_tree_node
def test_set_tree_node():
    test = {}
    set_tree_node(test, 'a:a', 'value')
    set_tree_node(test, 'a:b', 'value')
    set_tree_node(test, 'a:c:c', 'value')

    assert test['a'] == {'a': 'value', 'b': 'value', 'c': {'c': 'value'}}



# Generated at 2022-06-14 06:54:04.974188
# Unit test for function get_tree_node
def test_get_tree_node():
    import pytest
    tree = {
        'a': {
            'b': {
                'c': {
                    'd': 'hello world',
                    'e': 'goodbye world',
                }
            }
        }
    }

    assert get_tree_node(tree, 'a:b:c:d') == 'hello world'
    assert get_tree_node(tree, 'a:b:c:e') == 'goodbye world'

    with pytest.raises(KeyError):
        get_tree_node(tree, 'a:b:c:f')

    assert get_tree_node(tree, 'a:b:c:f', default=True) is True



# Generated at 2022-06-14 06:54:12.929606
# Unit test for function get_tree_node
def test_get_tree_node():
    test_tree = {'he': 'llo'}
    value = get_tree_node(test_tree, 'he')
    assert value == test_tree['he']  # Value

    test_tree = {
        'one': {
            'two': {
                'three': {
                    'four': 'five'
                }
            }
        }
    }
    value = get_tree_node(test_tree, 'one:two:three:four')
    assert value == test_tree['one']['two']['three']['four']
    assert value == 'five'
    value = get_tree_node(test_tree, 'one:two:three')
    assert value == test_tree['one']['two']['three']

# Generated at 2022-06-14 06:54:23.939694
# Unit test for function get_tree_node
def test_get_tree_node():
    """
    Test for get_tree_node, using a tree as a fixture.
    """
    tree = {'a': {'b': {'c': 'd'}}}
    assert get_tree_node(tree, 'a:b:c') == 'd'
    assert get_tree_node(tree, 'a:b') == {'c': 'd'}
    assert get_tree_node(tree, 'a') == {'b': {'c': 'd'}}


if __name__ == '__main__':
    print('Tree: %s' % (Tree))
    t = Tree()
    print('t: %s' % (t))
    t['a:b:c'] = 'd'
    print('t: %s' % (t))

# Generated at 2022-06-14 06:54:36.560863
# Unit test for function get_tree_node
def test_get_tree_node():
    data = collections.OrderedDict([
        ('a', collections.OrderedDict([
            ('b', collections.OrderedDict([
                ('c', collections.OrderedDict([
                    ('d', 1),
                    ('e', 2),
                ])),
            ])),
        ])),
    ])

    # Test no level specified
    assert get_tree_node({}, 'a') is _sentinel

    # Test first level
    assert get_tree_node(data, 'a') == data['a']

    # Test second level
    assert get_tree_node(data, 'a:b') == data['a']['b']

    # Test third level
    assert get_tree_node(data, 'a:b:c') == data['a']['b']['c']

    # Test non-existent

# Generated at 2022-06-14 06:54:45.435744
# Unit test for function set_tree_node
def test_set_tree_node():
    expected = {
        'level1': {
            'level2': {
                'level3': {
                    'name': 'Bob',
                    'job': 'programmer'
                },
                'level3a': {
                    'name': 'Alice',
                    'job': 'programmer'
                }
            },
            'level2a': {
                'level3': {
                    'name': 'Bob',
                    'job': 'programmer'
                }
            }
        }
    }

    mapping = tree()
    node = set_tree_node(mapping, 'level1:level2:level3:name', 'Bob')
    node = set_tree_node(mapping, 'level1:level2:level3:job', 'programmer')

# Generated at 2022-06-14 06:54:55.540465
# Unit test for function get_tree_node
def test_get_tree_node():
    """Test function get_tree_node for correct behavior."""
    mapping = {
        'a': {
            'b': {
                'c': {
                    'd': 'foo'
                }
            }
        }
    }

    assert get_tree_node(mapping, 'a:b') == {'c': {'d': 'foo'}}
    assert get_tree_node(mapping, 'a:b:c') == {'d': 'foo'}
    assert get_tree_node(mapping, 'a:b:c:d', default='bar') == 'foo'
    assert get_tree_node(mapping, 'a:b:c:d:e', default='bar') == 'bar'



# Generated at 2022-06-14 06:55:08.136537
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = tree()
    mapping['test']['in']['deep'] = 'test'
    assert mapping == {'test': {'in': {'deep': 'test'}}}
    assert get_tree_node(mapping, 'test:in:deep') == 'test'
    assert get_tree_node(mapping, 'test:in:deep', default='nope') == 'test'
    mapping['test']['in']['deep'] = {'again': 'nope'}
    assert get_tree_node(mapping, 'test:in:deep:again') == 'nope'
    assert get_tree_node(mapping, 'test:in:deep:again', default='yup') == 'nope'

# Generated at 2022-06-14 06:55:13.072771
# Unit test for function get_tree_node
def test_get_tree_node():
    test_data = {
        "outer": {
            "inner": {
                "value": "1"
            }
        }
    }
    assert get_tree_node(test_data, "outer:inner:value") == "1"



# Generated at 2022-06-14 06:55:24.956646
# Unit test for function set_tree_node
def test_set_tree_node():
    """Test set_tree_node function."""
    test_data = {
        'foo': 'bar',
        'fiz': {
            'bazz': 'qux',
        },
    }

    assert set_tree_node(test_data, 'foo', 'baz') == test_data
    assert test_data == {
        'foo': 'baz',
        'fiz': {
            'bazz': 'qux',
        },
    }

    assert set_tree_node(test_data, 'fiz:bazz', 'mux') == test_data['fiz']
    assert test_data == {
        'foo': 'baz',
        'fiz': {
            'bazz': 'mux',
        },
    }


# Generated at 2022-06-14 06:56:11.899928
# Unit test for function get_tree_node
def test_get_tree_node():
    """Test get_tree_node."""
    # Prepare our test data
    bigtree = {
        'level0': {
            'level1': {
                'level2': 'I\'m level 2',
            },
            'level1b': {
                'level1b_1': 'I\'m level 1b_1',
                'level1b_2': 'I\'m level 1b_2',
                'level1b_3': 'I\'m level 1b_3',
                'level1b_4': 'I\'m level 1b_4',
            },
        },
    }

    # Test all the things
    assert get_tree_node(bigtree, 'level0') == bigtree['level0']