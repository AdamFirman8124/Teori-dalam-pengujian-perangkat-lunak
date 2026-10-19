

# Generated at 2022-06-14 06:46:16.856132
# Unit test for function set_tree_node
def test_set_tree_node():
    """
    Test set_tree_node(mapping, key, value)
    """
    test_tree = {}
    set_tree_node(test_tree, 'key1', 'value1')
    set_tree_node(test_tree, 'key2:sub1:subsub1', 'value2')
    set_tree_node(test_tree, 'key3:sub1:subsub1:subsubsub1', 'value3')
    set_tree_node(test_tree, 'key3:sub1:subsub2', 'value4')
    set_tree_node(test_tree, 'key3:sub2', 'value5')
    set_tree_node(test_tree, 'key4:sub1', 'value6')

# Generated at 2022-06-14 06:46:29.866263
# Unit test for function get_tree_node
def test_get_tree_node():
    """Tests :function:`get_tree_node`"""
    from nose.tools import assert_equals
    test_tree = tree()
    test_tree['root_leaf'] = 'foo'
    test_tree['parent']['child'] = 'foo'
    test_tree['parent']['child_2'] = 'bar'
    test_tree['parent']['child_2']['child']['child'] = 'child_child'
    # Single node
    assert_equals('foo', get_tree_node(test_tree, 'root_leaf'))
    # Whole tree
    assert_equals(test_tree, get_tree_node(test_tree, ''))
    # No node
    assert_equals(None, get_tree_node(test_tree, 'no_node'))


# Generated at 2022-06-14 06:46:37.285279
# Unit test for function get_tree_node
def test_get_tree_node():
    t = {'h': {'e': {'l': {'l': {'o': 'World'}}}}}
    assert get_tree_node(t, 'h') == {'e': {'l': {'l': {'o': 'World'}}}}
    assert get_tree_node(t, 'h:e') == {'l': {'l': {'o': 'World'}}}
    assert get_tree_node(t, 'h:e:l:l:o') == 'World'
    assert get_tree_node(t, 'h:e:l:l') == {'o': 'World'}
    with pytest.raises(KeyError):
        get_tree_node(t, 'h:e:l:l:o:1')



# Generated at 2022-06-14 06:46:48.047831
# Unit test for function get_tree_node
def test_get_tree_node():
    # Create and fill the tree
    tree = {
        'progs': {
            'bash': {
                'path': '/bin/bash',
            },
            'vim': {
                'path': '/usr/bin/vim',
            },
            'test': {
                'test': {
                    'test': {
                        'test': 'test',
                    },
                },
            },
        },
    }

    # Test node exists
    assert get_tree_node(tree, 'progs:bash:path') == '/bin/bash'

    # Test node does not exist
    assert get_tree_node(tree, 'progs:noexist') is _sentinel

    # Test deep node exists
    assert get_tree_node(tree, 'progs:test:test:test:test') == 'test'

    # Test

# Generated at 2022-06-14 06:46:51.256338
# Unit test for function set_tree_node
def test_set_tree_node():
    a = tree()
    set_tree_node(a, 'a:b:c', 'C')
    set_tree_node(a, 'a:d:e:f', 'F')
    assert a['a']['d']['e']['f'] == 'F'



# Generated at 2022-06-14 06:46:55.330373
# Unit test for function set_tree_node
def test_set_tree_node():
    """Unit test for function set_tree_node"""
    mapping = collections.Mapping()
    set_tree_node(mapping, 'foo', 'bar')
    assert mapping['foo'] == 'bar'



# Generated at 2022-06-14 06:47:03.009383
# Unit test for function get_tree_node
def test_get_tree_node():
    # Given
    mapping = {
        'a': {
            'b': {
                'c': {
                    'e': 'f'
                },
                'd': 'g',
                'h': 'i'
            }
        }
    }

    # When
    result = get_tree_node(mapping, 'a:b:c')

    # Then
    assert(result == {'e': 'f'})



# Generated at 2022-06-14 06:47:10.009051
# Unit test for function set_tree_node
def test_set_tree_node():
    import unittest

    class TestCase(unittest.TestCase):
        tree = None
        keys = []

        def test_set_tree_node(self):
            for key in self.keys:
                set_tree_node(self.tree, key, None)
                for i in range(len(key.split(':'))):
                    self.assertIsInstance(get_tree_node(self.tree, key), dict)

    class TestCase1(TestCase):
        def setUp(self):
            self.tree = {}
            self.keys = ['a', 'b:c:d:e', 'f:g']

    class TestCase2(TestCase):
        def setUp(self):
            self.tree = tree()

# Generated at 2022-06-14 06:47:20.168503
# Unit test for function get_tree_node
def test_get_tree_node():
    t = tree()
    t['s']['s2']['s3']['s4'] = 'ipsum'
    assert get_tree_node(t, 's:s2:s3')['s4'] == 'ipsum'
    assert get_tree_node(t, 's:s2:s3:s4') == 'ipsum'
    assert get_tree_node(t, 's:s2:s4', default=None) is None
    assert get_tree_node(t, 's:s3:s4', default=None) is None

# Generated at 2022-06-14 06:47:32.800275
# Unit test for function set_tree_node
def test_set_tree_node():
    """
    Set arbitrary node on a tree-like mapping structure, allowing for : notation to signify dimension.

    Arguments:
        mapping collections.Mapping: Mapping to fetch from
        key str|unicode: Key to set, allowing for : notation
        value str|unicode: Value to set `key` to
        parent bool: If True, return parent node. Defaults to False.

    Returns:
        object: Parent node.

    """
    t = tree()
    set_tree_node(t, 'foo:bar:baz', 'foobarbaz')
    set_tree_node(t, 'bar', 'bar')
    assert t['foo']['bar']['baz'] == 'foobarbaz'
    assert t['bar'] == 'bar'



# Generated at 2022-06-14 06:47:47.800794
# Unit test for function get_tree_node
def test_get_tree_node():
    d = {
        'foo': {
            'boo': 'baz',
            'bar': {
                'r': 'r1',
                'g': 'g1',
                'b': 'b1',
                'cmy': {
                    'c': 'c1',
                    'm': 'm1',
                    'y': 'y1',
                    'k': 'k1',
                },
            },
        },
    }
    assert get_tree_node(d, 'foo') == {'boo': 'baz', 'bar': {'r': 'r1', 'g': 'g1', 'b': 'b1', 'cmy': {'c': 'c1', 'm': 'm1', 'y': 'y1', 'k': 'k1'}}}
    assert get_tree_node

# Generated at 2022-06-14 06:47:55.480481
# Unit test for function set_tree_node
def test_set_tree_node():
    assert set_tree_node(tree(), 'a', 1) == {'a': 1}
    assert set_tree_node(tree(), 'a:b', 1) == {'a': {'b': 1}}
    assert set_tree_node(tree(), 'a:b:c', 1) == {'a': {'b': {'c': 1}}}
    assert set_tree_node(tree(), 'a:b:c', 1) == {'a': {'b': {'c': 1}}}
    assert set_tree_node(tree(), 'a::c', 1) == {'a': {'c': 1}}



# Generated at 2022-06-14 06:48:00.186960
# Unit test for function set_tree_node
def test_set_tree_node():
    tree = Tree()
    set_tree_node(tree, 'first:second:third:fourth:fifth', 'sixth')
    assert tree['first']['second']['third']['fourth']['fifth'] == 'sixth'



# Generated at 2022-06-14 06:48:08.571665
# Unit test for function get_tree_node
def test_get_tree_node():
    test_tree = {'foo': {'bar': {'baz': {'biz': {'buz': 'blammo'}}}}}

    assert get_tree_node(test_tree, 'foo:bar:baz:biz:buz') == 'blammo'
    assert get_tree_node(test_tree, 'foo') == {'bar': {'baz': {'biz': {'buz': 'blammo'}}}}
    assert get_tree_node(test_tree, 'foo:bar:baz:biz') == {'buz': 'blammo'}
    assert get_tree_node(test_tree, 'foo:bar:baz:biz:buz:bang') is _sentinel

# Generated at 2022-06-14 06:48:15.272728
# Unit test for function set_tree_node
def test_set_tree_node():
    tree = Tree()
    tree['x'] = 'x'
    assert tree['x'] == 'x'
    tree['x:y:z'] = 'x:y:z'
    assert tree['x:y:z'] == 'x:y:z'
    tree['x:y:z'] = 'x:y:z:overridden'
    assert tree['x:y:z'] == 'x:y:z:overridden'



# Generated at 2022-06-14 06:48:25.622387
# Unit test for function set_tree_node
def test_set_tree_node():
    my_tree = Tree()
    my_tree.register('cat', 'felix')
    assert my_tree.get('cat') == 'felix'
    my_tree.register('cat:nano', 'fluffy')
    assert my_tree.get('cat:nano') == 'fluffy'
    assert my_tree.get('cat') == {'nano': 'fluffy'}
    my_tree.register('cat:paula', 'happy')
    assert my_tree.get('cat') == {'nano': 'fluffy', 'paula': 'happy'}


test_set_tree_node.__test__ = False



# Generated at 2022-06-14 06:48:38.960101
# Unit test for function get_tree_node
def test_get_tree_node():
    dct = dict(
        a=10,
        b=30,
        c=dict(
            d=40,
            e=50,
            f=60,
        )
    )

    assert 10 == get_tree_node(dct, 'a')
    assert 30 == get_tree_node(dct, 'b')
    assert 40 == get_tree_node(dct, 'c:d')
    assert 60 == get_tree_node(dct, 'c:f')
    assert _sentinel == get_tree_node(dct, 'c:g', _sentinel)

    # Unit test for function set_tree_node

# Generated at 2022-06-14 06:48:43.056491
# Unit test for function set_tree_node
def test_set_tree_node():
    t = tree()
    set_tree_node(t, 'foo:bar:baz', 'test')
    assert t['foo']['bar']['baz'] == 'test'



# Generated at 2022-06-14 06:48:55.240394
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = {
        'a': 'b',
        'c': {
            'd': 'e',
            'f': {
                'g': {
                    'h': 'i'
                }
            }
        }
    }

    assert get_tree_node(mapping, 'a') == 'b'
    assert get_tree_node(mapping, 'c:d') == 'e'
    assert get_tree_node(mapping, 'c:f:g:h') == 'i'

    # Parent nodes
    assert get_tree_node(mapping, 'c:f:g:h', parent=True) == {'h': 'i'}
    assert get_tree_node(mapping, 'c:f:g', parent=True) == {'g': {'h': 'i'}}



# Generated at 2022-06-14 06:49:08.215282
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = {'a': {'b': {'c': 'd'}} }
    assert get_tree_node(mapping, 'a') == {'b': {'c': 'd'}}
    assert get_tree_node(mapping, 'a:b') == {'c': 'd'}
    assert get_tree_node(mapping, 'a:b:c') == 'd'

    assert get_tree_node(mapping, 'a:b:c:d') == _sentinel

    assert get_tree_node(mapping, 'a:b:c:d', 'e') == 'e'
    assert get_tree_node(mapping, 'a:b:c:d', default='e') == 'e'

    mapping = {'a': {'b': 'c'} }

# Generated at 2022-06-14 06:49:19.307291
# Unit test for function get_tree_node
def test_get_tree_node():
    tree = {
        'one': {
            'two': {
                'three': 3
            }
        }
    }
    assert get_tree_node(tree, 'one:two:three') == 3
    assert get_tree_node(tree, 'one:two') == {'three': 3}
    assert get_tree_node(tree, 'one:two:four', default=-1) == -1
    with pytest.raises(KeyError):
        get_tree_node(tree, 'one:two:four')



# Generated at 2022-06-14 06:49:30.297877
# Unit test for function get_tree_node
def test_get_tree_node():
    assert get_tree_node({'foo': {'bar': 'baz'}}, 'foo:bar') == 'baz'
    assert get_tree_node({'foo': {'bar': 'baz'}}, 'foo:bar', default=None) == 'baz'
    assert get_tree_node({'foo': {'bar': 'baz'}}, 'foo:bar', parent=True) == 'baz'
    assert get_tree_node({'foo': {'bar': 'baz'}}, 'foo:bar:baz', default=None) is None
    assert get_tree_node({'foo': {'bar': 'baz'}}, 'foo:bar:baz', default='bazbaz') == 'bazbaz'
    with pytest.raises(KeyError):
        get_

# Generated at 2022-06-14 06:49:34.994967
# Unit test for function get_tree_node
def test_get_tree_node():
    assert get_tree_node({}, 'foo') is _sentinel
    assert get_tree_node({'foo': 1}, 'foo') == 1
    assert get_tree_node({'foo': {'bar': 1}}, 'foo:bar') == 1



# Generated at 2022-06-14 06:49:37.704089
# Unit test for function set_tree_node
def test_set_tree_node():
    test_dict = {}
    set_tree_node(test_dict, 'foo:bar:baz', 'hello world')
    assert test_dict == {'foo': {'bar': {'baz': 'hello world'}}}



# Generated at 2022-06-14 06:49:45.989469
# Unit test for function get_tree_node
def test_get_tree_node():
    import copy

    mapping = {
        'a': {
            'b': {
                'c': {
                    'd': 'test'
                }
            }
        }
    }

    # Test basic functionality
    assert get_tree_node(mapping, 'a:b:c:d') == 'test'

    # Test too many nodes
    with pytest.raises(KeyError):
        get_tree_node(mapping, 'a:b:c:d:e')

    # Test multiple levels, return parent
    parent = get_tree_node(mapping, 'a:b:c:d', parent=True)
    assert parent == {'d': 'test'}

    # Test default
    parent = get_tree_node(mapping, 'a:b:c:e', default='default')
   

# Generated at 2022-06-14 06:49:57.291678
# Unit test for function get_tree_node
def test_get_tree_node():
    x = {
        'first': {
            'second': {
                'third': 'leaf'
            }
        }
    }
    assert get_tree_node(x, 'first') == x['first']
    assert get_tree_node(x, 'first:second') == x['first']['second']
    assert get_tree_node(x, 'first:second:third') == x['first']['second']['third']
    assert get_tree_node(x, 'first:second:third', default='foo') == x['first']['second']['third']
    assert get_tree_node(x, 'first:second:third', parent=True) == x['first']['second']

# Generated at 2022-06-14 06:50:10.767039
# Unit test for function get_tree_node
def test_get_tree_node():
    assert get_tree_node(dict(a=dict(b=dict(c='d'))), 'a:b:c') == 'd'
    assert get_tree_node(dict(a=dict(b=dict(c='d'))), 'a:b:c', _sentinel) == 'd'
    assert get_tree_node(dict(a=dict(b=dict(c='d'))), 'a:b:c', default='e') == 'd'
    assert get_tree_node(dict(a=dict(b=dict(c='d'))), 'a:b:d', _sentinel)  # KeyError
    assert get_tree_node(dict(a=dict(b=dict(c='d'))), 'a:b:d', default='e') == 'e'
    assert get

# Generated at 2022-06-14 06:50:16.508815
# Unit test for function set_tree_node
def test_set_tree_node():
    top = tree()
    set_tree_node(top, 'foo', 'bar')
    set_tree_node(top, 'foo:baz:baz', 'baz')
    assert top['foo']['baz']['baz'] == 'baz'
    assert top['foo'] == 'bar'



# Generated at 2022-06-14 06:50:24.925684
# Unit test for function set_tree_node
def test_set_tree_node():
    test_dict = {}
    set_tree_node(test_dict, 'a:b:c', 10)
    assert test_dict['a']['b']['c'] == 10

    # Single level should still work
    set_tree_node(test_dict, 'b', 10)
    assert test_dict['b'] == 10

    # Try replacing a node
    set_tree_node(test_dict, 'a:c', 10)
    assert test_dict['a']['c'] == 10



# Generated at 2022-06-14 06:50:30.397138
# Unit test for function get_tree_node
def test_get_tree_node():
    test_vals = {
        'a': 'a',
        'b': 'b',
        'c': 'c',
        'd': {
            'a': 'a',
            'b': 'b',
            'c': 'c',
            'd': {
                'a': 'a',
                'b': 'b',
                'c': 'c',
                'd': {
                    'a': 'a',
                    'b': 'b',
                    'c': 'c',
                }
            }
        }
    }

    assert get_tree_node(test_vals, 'a') == 'a'
    assert get_tree_node(test_vals, 'd:c') == 'c'
    assert get_tree_node(test_vals, 'd:d:b') == 'b'


# Generated at 2022-06-14 06:50:43.580597
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = {
        'name': 'test',
        'foo': {
            'bar': 'baz',
            'bam': {
                'baz': 'qux'
            }
        }
    }

    assert get_tree_node(mapping, 'foo:bar') == 'baz'
    assert get_tree_node(mapping, 'foo:bam:baz') == 'qux'



# Generated at 2022-06-14 06:50:53.364907
# Unit test for function get_tree_node
def test_get_tree_node():
    assert get_tree_node(tree(), 'x:1:2:3') == {}
    assert get_tree_node(tree(), 'x:1:2:3', default=False) == False

    assert get_tree_node(tree(), 'x:1:2:3', parent=True) == {}

    # No default
    try:
        get_tree_node(tree(), 'x:1:2:3', default=None)
    except KeyError as exc:
        assert exc.args[0] == 'x'

    x = tree()
    x['1'] = 'bar'
    x['foo']['bar'] = 'baz'
    assert get_tree_node(x, '1') == 'bar'
    assert get_tree_node(x, 'foo:bar') == 'baz'

# Generated at 2022-06-14 06:51:03.914140
# Unit test for function set_tree_node
def test_set_tree_node():
    """Unit test for function set_tree_node."""
    nested = tree()

    set_tree_node(nested, 'one:two:three', 'three')

# Generated at 2022-06-14 06:51:13.170643
# Unit test for function get_tree_node
def test_get_tree_node():
    """Test function get_tree_node."""
    assert get_tree_node({}, 'foo', default=42) == 42
    # Test regular usage
    mapping = {'foo': {'bar': {'baz': 42}}}
    assert get_tree_node(mapping, 'foo:bar:baz') == 42
    # Test that it returns default value when key is not found
    assert get_tree_node({}, 'foo', default=42) == 42
    # Test that it raise KeyError when key is not found
    assert_raises(KeyError, get_tree_node, {}, 'foo')



# Generated at 2022-06-14 06:51:17.723771
# Unit test for function set_tree_node
def test_set_tree_node():
    mapping = tree()
    set_tree_node(mapping, 'foo:bar:baz', 1)
    set_tree_node(mapping, 'foo:bar:zoo', 2)
    assert mapping['foo']['bar']['baz'] == 1
    assert mapping['foo']['bar']['zoo'] == 2



# Generated at 2022-06-14 06:51:23.425927
# Unit test for function get_tree_node
def test_get_tree_node():
    """Unit test for get_tree_node"""
    tree = {
        'foo': {
            'bar': {
                'baz': True,
            }
        }
    }

    assert True is get_tree_node(tree, 'foo:bar:baz')
    assert True is get_tree_node(tree, 'FOO:BAR:BAZ', default=True)



# Generated at 2022-06-14 06:51:28.099548
# Unit test for function set_tree_node
def test_set_tree_node():
    d = {}
    set_tree_node(d, "a:b:c", "test")
    set_tree_node(d, "a:b:d", "test2")
    assert d.get('a').get('b').get('c') == 'test'
    assert d.get('a').get('b').get('d') == 'test2'


# Generated at 2022-06-14 06:51:30.806171
# Unit test for function set_tree_node
def test_set_tree_node():
    tree = {}
    set_tree_node(tree, 'abc:def', 'ghi')
    assert tree == {'abc': {'def': 'ghi'}}



# Generated at 2022-06-14 06:51:39.370465
# Unit test for function get_tree_node
def test_get_tree_node():
    data = {'foo': {'bar': {'baz': 'qux'}}}
    assert get_tree_node(data, 'foo:bar:baz') is 'qux'
    assert get_tree_node(data, 'foo:bar:baz:quux') is _sentinel
    try:
        get_tree_node(data, 'foo:bar:baz:quux')
    except KeyError:
        return
    raise AssertionError('Did not raise KeyError')



# Generated at 2022-06-14 06:51:43.841800
# Unit test for function set_tree_node
def test_set_tree_node():
    d = {}
    set_tree_node(d, 'a:b:c:d:e', 1)
    assert d['a']['b']['c']['d']['e'] == 1



# Generated at 2022-06-14 06:51:58.177820
# Unit test for function set_tree_node
def test_set_tree_node():
    import json
    mapping = tree()
    set_tree_node(mapping, 'foo:bar:baz:quux', 'quuz')
    data = json.dumps(mapping)
    assert data == '{"foo": {"bar": {"baz": {"quux": "quuz"}}}}'



# Generated at 2022-06-14 06:52:04.754170
# Unit test for function set_tree_node
def test_set_tree_node():
    root = {}
    assert set_tree_node(root, 'some:thing:some:where', 3) == {'thing': {'some': {'where': 3}}}
    assert set_tree_node(root, 'other:thing:elsewhere', 4) == {'thing': {'elsewhere': 4}}



# Generated at 2022-06-14 06:52:17.653724
# Unit test for function get_tree_node
def test_get_tree_node():
    tree = collections.defaultdict(dict)

    tree[1][2] = 3
    tree[4][5][6] = 7
    tree['8']['9'] = 0
    tree[10][11] = 12

    assert get_tree_node(tree, 1) == {2: 3}
    assert get_tree_node(tree, 4) == {5: {6: 7}}
    assert get_tree_node(tree, 8) == {9: 0}
    assert get_tree_node(tree, '10:11') == 12
    with pytest.raises(KeyError):
        get_tree_node(tree, 'bad:key')
    assert get_tree_node(tree, 'bad:key', default='') == ''



# Generated at 2022-06-14 06:52:30.340188
# Unit test for function set_tree_node
def test_set_tree_node():
    """
    Tests the function `set_tree_node` by ensuring the following:

    - Function creates missing node paths.
    - Function updates existing node paths.
    - Function can create trees with multiple dimensions.
    """
    test_data = {}
    # Test creation with a singular key
    set_tree_node(test_data, 'foo', 'bar')

    assert test_data['foo'] == 'bar'
    set_tree_node(test_data, 'foo', 'baz')
    assert test_data['foo'] == 'baz'

    # Test creation with multiple dimensions
    set_tree_node(test_data, 'foo:bar:baz', 'taz')
    assert test_data['foo']['bar']['baz'] == 'taz'

    # Test updates with multiple dimensions
    set_tree

# Generated at 2022-06-14 06:52:39.838440
# Unit test for function get_tree_node
def test_get_tree_node():
    root = {
        'foo': {
            'bar': {
                'baz': 'qux',
            }
        }
    }

    assert get_tree_node(root, 'foo:bar:baz') == 'qux'
    assert get_tree_node(root, 'foo:bar') == {'baz': 'qux'}
    assert get_tree_node(root, 'foo:bar:baz', default=False) == 'qux'
    assert get_tree_node(root, 'baz:baz:baz', default=False) is False

# Generated at 2022-06-14 06:52:45.096973
# Unit test for function get_tree_node
def test_get_tree_node():
    assert get_tree_node({'foo': {'bar': 'baz'}}, 'foo:bar') == 'baz'
    assert get_tree_node({'foo': {'bar': 'baz'}}, 'foo:bar:baz') is _sentinel, 'Should raise KeyError'



# Generated at 2022-06-14 06:52:55.458542
# Unit test for function get_tree_node
def test_get_tree_node():
    test_mapping = {
        'a': 'a',
        'b': {
            'a': 'ba',
            'b': {
                'a': 'bba',
                'b': 'bbb'
            }
        },
        'c': {
            'a': {
                'a': 'caa',
                'b': 'cab',
            }
        }
    }

    # Test base level key
    assert get_tree_node(test_mapping, 'a') == 'a'

    # Test nested key
    assert get_tree_node(test_mapping, 'b:b:b') == 'bbb'

    # Test non-existing key

# Generated at 2022-06-14 06:53:05.039776
# Unit test for function set_tree_node
def test_set_tree_node():
    from pprint import pprint

    # Define a tree-like object to test against
    tree = {}
    set_tree_node(tree, 'a', 1)
    set_tree_node(tree, 'b', 2)
    set_tree_node(tree, 'c:d', 3)
    set_tree_node(tree, 'c:e', 4)

    # Try to alter existing value - tree should not be affected
    set_tree_node(tree, 'c:d', 5)

    # Try to set an even deeper node
    set_tree_node(tree, 'f:g:h', 6)
    set_tree_node(tree, 'f:p:q:r', 7)

    # Check values
    assert tree['a'] == 1
    assert tree['b'] == 2

# Generated at 2022-06-14 06:53:17.110828
# Unit test for function get_tree_node
def test_get_tree_node():
    t = {
        'a': {'aa': 'foo',
              'ab': {'aba': 'bar',
                     'abb': None},
              'ac': 'baz'},
        'b': 'foobar'
    }

    assert get_tree_node(t, 'a:aa') == 'foo'
    assert get_tree_node(t, 'a:ab:aba') == 'bar'
    assert get_tree_node(t, 'a:ab:abb') is None


if __name__ == '__main__':
    import sys
    t = tree()
    t['foo']['bar']['baz'] = 1
    t['foo']['bar']['qux'] = 2

    pprint(t)
    print(sys.version)

# Generated at 2022-06-14 06:53:20.282878
# Unit test for function set_tree_node
def test_set_tree_node():
    assert set_tree_node({}, 'test:test:test:test', 'test') == {'test': {'test': {'test': 'test'}}}



# Generated at 2022-06-14 06:53:44.374235
# Unit test for function get_tree_node
def test_get_tree_node():
    """
    Test for function get_tree_node

    """

    t = tree()
    t['key1:key2']['key3'] = 'value'
    assert get_tree_node(t, 'key1:key2:key3') == 'value'
    assert get_tree_node(t, 'key1:key2:key3:key4', default='value2') == 'value2'



# Generated at 2022-06-14 06:53:51.897386
# Unit test for function get_tree_node
def test_get_tree_node():
    assert get_tree_node({'thing': {'otherthing': True}}, 'thing:otherthing') is True
    assert get_tree_node({'thing': {'otherthing': True}}, 'wrongo') is _sentinel

    try:
        get_tree_node({'thing': {'otherthing': True}}, 'wrongo')
    except KeyError:
        pass
    else:
        assert False, 'get_tree_node should raise KeyError on non-existent keys by default'



# Generated at 2022-06-14 06:54:04.654280
# Unit test for function set_tree_node
def test_set_tree_node():
    """Unit test for function `set_tree_node`."""
    from pprint import pprint  # noqa

    tree_ = {}

    set_tree_node(tree_, 'foo:bar', 'test')
    assert tree_ == {'foo': {'bar': 'test'}}

    set_tree_node(tree_, 'foo:bar:baz', 'test2')
    assert tree_ == {'foo': {'bar': {'baz': 'test2'}}}

    set_tree_node(tree_, 'foo:bar:baz:quux', 'test3')
    assert tree_ == {'foo': {'bar': {'baz': {'quux': 'test3'}}}}



# Generated at 2022-06-14 06:54:08.261586
# Unit test for function set_tree_node
def test_set_tree_node():
    test_tree = {}
    set_tree_node(test_tree, 'foo:bar', 'baz')
    assert test_tree == {'foo': {'bar': 'baz'}}



# Generated at 2022-06-14 06:54:15.856905
# Unit test for function set_tree_node
def test_set_tree_node():
    import unittest

    class TestSetTreeNode(unittest.TestCase):
        def test_set_tree_node(self):
            test = {}
            res = set_tree_node(test, 'lulz:huebr', 'hue')
            self.assertEqual(test, {'lulz': {'huebr': 'hue'}})
            self.assertEqual(res, {'huebr': 'hue'})

    unittest.main()



# Generated at 2022-06-14 06:54:20.189820
# Unit test for function set_tree_node
def test_set_tree_node():
    tree = {}
    set_tree_node(tree, 'a:b:c', 1)
    assert tree['a']['b']['c'] == 1



# Generated at 2022-06-14 06:54:28.059705
# Unit test for function get_tree_node
def test_get_tree_node():
    """Test tree node fetching."""
    mapping = {
        'a': {
            'b': {
                'c': {
                    'd': {
                        'e': 'E'
                    }
                }
            }
        }
    }

    # Test fault-tolerant traversal
    assert get_tree_node(mapping, 'a:b:c:d:e') == 'E'
    assert get_tree_node(mapping, 'a:x:c:d:e') is _sentinel
    assert get_tree_node(mapping, 'a:x:c:d:e', default='noop') == 'noop'
    assert get_tree_node(mapping, 'a:x:c:d:e', parent=True) is _sentinel

    # Test parent node lookup
   

# Generated at 2022-06-14 06:54:38.915123
# Unit test for function set_tree_node
def test_set_tree_node():
    # Setup
    mapping = {
        'a': {
            'b': {}
        }
    }
    test_values = (
        ('a:b:c:d:e', 'value'),
        ('a:b:c:f:g', 'value 2'),
        ('a:b:c:h:i', 'value 3'),
    )

    expected_result = {
        'a': {
            'b': {
                'c': {
                    'd': {
                        'e': 'value',
                        },
                    'f': {
                        'g': 'value 2',
                        },
                    'h': {
                        'i': 'value 3',
                        },
                    }
                }
            }
        }

    # Test

# Generated at 2022-06-14 06:54:45.738968
# Unit test for function get_tree_node
def test_get_tree_node():
    test_mapping = {
        'foo': {
            'bar': {
                'baz': 'bacon'
            }
        }
    }

    assert get_tree_node(test_mapping, 'foo:bar:baz') == 'bacon'
    assert get_tree_node(test_mapping, 'foo:bar:baz', parent=True) == {'baz': 'bacon'}

# Generated at 2022-06-14 06:54:54.431361
# Unit test for function get_tree_node
def test_get_tree_node():
    tree = {
        'a': {
            'b': {
                'c': 'd'
            }
        }
    }

    # Expected KeyError
    with pytest.raises(KeyError):
        get_tree_node(tree, 'a:b:c:d')

    # Expected None
    assert get_tree_node(tree, 'a:b:x', default=None) is None

    # Expected 'd'
    assert get_tree_node(tree, 'a:b:c') == 'd'



# Generated at 2022-06-14 06:55:32.153764
# Unit test for function set_tree_node
def test_set_tree_node():
    data = tree()
    set_tree_node(data, 'test:test', 'success')
    assert data['test']['test'] == 'success'

if __name__ == '__main__':
    test_set_tree_node()

# Generated at 2022-06-14 06:55:40.587006
# Unit test for function get_tree_node
def test_get_tree_node():
    d = {'a': {'b': {'c': 1}}}
    assert get_tree_node(d, 'a') == {'b': {'c': 1}}
    assert get_tree_node(d, 'a:b') == {'c': 1}
    assert get_tree_node(d, 'a:b:c') == 1
    assert get_tree_node(d, 'a:b:d', default=None) is None
    assert get_tree_node(d, 'a:b:d', parent=True) == {'c': 1}



# Generated at 2022-06-14 06:55:47.165279
# Unit test for function set_tree_node
def test_set_tree_node():
    d = {}
    set_tree_node(d, 'x', 1)
    assert d == {'x': 1}
    set_tree_node(d, 'y', 2)
    assert d == {'x': 1, 'y': 2}
    set_tree_node(d, 'a:b', 3)
    assert d == {'x': 1, 'y': 2, 'a': {'b': 3}}
    set_tree_node(d, 'a:b:c', 5)
    assert d == {'x': 1, 'y': 2, 'a': {'b': {'c': 5}}}
    set_tree_node(d, 'a:c:b', 6)

# Generated at 2022-06-14 06:55:53.359502
# Unit test for function set_tree_node
def test_set_tree_node():
    tree = {}
    set_tree_node(tree, "a:b:c", "cargo:c")
    set_tree_node(tree, "a:b:d", "cargo:d")
    assert tree == {"a": {"b": {"c": "cargo:c", "d": "cargo:d"}}}



# Generated at 2022-06-14 06:56:05.855405
# Unit test for function get_tree_node
def test_get_tree_node():
    assert 'c' == get_tree_node({'a': {'b': {'c': 'c'}}}, 'a:b:c')
    assert 'b' == get_tree_node({'a': {'b': {'c': 'c'}}}, 'a', parent=True)
    assert 1 == get_tree_node({'a': {'b': {'c': 'c'}}}, 'a:b:c:d', default=1)
    assert 'a' == get_tree_node({'a': {'b': {'c': 'c'}}}, 'a:a', default=1)
    try:
        get_tree_node({'a': {'b': {'c': 'c'}}}, 'a:b:d')
        assert False
    except KeyError:
        assert True

