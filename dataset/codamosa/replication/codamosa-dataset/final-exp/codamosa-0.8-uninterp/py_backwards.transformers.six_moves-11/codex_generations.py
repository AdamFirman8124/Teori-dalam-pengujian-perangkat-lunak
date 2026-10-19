

# Generated at 2022-06-14 02:06:06.705073
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    m = MovedAttribute("a", "b", "c")
    assert m.name == 'a'
    assert m.new_mod == 'c'
    assert m.new_attr == 'a'
    m = MovedAttribute("a", "b", "c", "aa", "bb")
    assert m.name == 'a'
    assert m.new_mod == 'c'
    assert m.new_attr == 'bb'

# Generated at 2022-06-14 02:06:17.014338
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert MovedAttribute("cStringIO", "cStringIO", "io", "StringIO").new_mod == "io"
    assert MovedAttribute("cStringIO", "cStringIO", "io", "StringIO").new_attr == "StringIO"
    assert MovedAttribute("cStringIO", "cStringIO", "io", "StringIO").name == "cStringIO"
    assert MovedAttribute("filter", "itertools", "builtins", "ifilter", "filter").new_mod == "builtins"
    assert MovedAttribute("filter", "itertools", "builtins", "ifilter", "filter").new_attr == "filter"
    assert MovedAttribute("filter", "itertools", "builtins", "ifilter", "filter").name == "filter"

# Generated at 2022-06-14 02:06:21.660536
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    move = MovedAttribute('name', 'old_mod', 'new_mod', 'old_attr', 'new_attr')
    assert move.name == 'name'
    assert move.new_mod == 'new_mod'
    assert move.new_attr == 'new_attr'



# Generated at 2022-06-14 02:06:25.039971
# Unit test for constructor of class MovedModule
def test_MovedModule():
    mm = MovedModule("test_name", "test_old", "test_new")
    assert mm.name == "test_name"
    assert mm.old == "test_old"
    assert mm.new == "test_new"

# Generated at 2022-06-14 02:06:27.645362
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert 'six' in SixMovesTransformer.dependencies
    assert 'itertools' in SixMovesTransformer.rewrites
    assert '__builtin__' in SixMovesTransformer.rewrites


# Generated at 2022-06-14 02:06:31.246427
# Unit test for constructor of class MovedModule
def test_MovedModule():
    move = MovedModule("copyreg", "copy_reg")
    assert move.name == "copyreg"
    assert move.new == "copyreg"


# Generated at 2022-06-14 02:06:37.311177
# Unit test for constructor of class MovedModule
def test_MovedModule():
  mm = MovedModule("something", "something.else")
  assert mm.name == "something"
  assert mm.new == "something"
  mm = MovedModule("something", "something.else", "else.something")
  assert mm.name == "something"
  assert mm.new == "else.something"
  #MM = MovedModule  # TypeError: MovedModule() takes at least 2 arguments (0 given)
  # MovedModule()  # TypeError: __init__() takes at least 3 arguments (1 given)

# Generated at 2022-06-14 02:06:39.823618
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    move = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert move.name == "cStringIO"
    assert move.new_mod == "io"
    assert move.new_attr == "StringIO"


# Generated at 2022-06-14 02:06:46.357800
# Unit test for constructor of class MovedModule
def test_MovedModule():
    mm = MovedModule('foo', 'old_mod')
    assert mm.name == 'foo'
    assert mm.new == 'foo'
    assert mm.old == 'old_mod'

    mm = MovedModule('foo', 'old_mod', 'new_mod')
    assert mm.name == 'foo'
    assert mm.new == 'new_mod'
    assert mm.old == 'old_mod'



# Generated at 2022-06-14 02:06:58.314648
# Unit test for constructor of class SixMovesTransformer

# Generated at 2022-06-14 02:07:09.018359
# Unit test for constructor of class SixMovesTransformer

# Generated at 2022-06-14 02:07:11.481310
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    st = SixMovesTransformer()
    assert st.rewrites == _get_rewrites()

# Generated at 2022-06-14 02:07:17.641117
# Unit test for constructor of class MovedModule
def test_MovedModule():
    module = MovedModule("name", "old")
    assert module.name == "name"
    assert module.old == "old"
    assert module.new == "name"
    module = MovedModule("name", "old", "new")
    assert module.name == "name"
    assert module.old == "old"
    assert module.new == "new"


# Generated at 2022-06-14 02:07:23.035515
# Unit test for constructor of class MovedModule
def test_MovedModule():
    # type: () -> None
    import sys
    assert sys.version_info[0:2] == (2, 7)
    assert MovedModule('builtins', '__builtin__').new == 'builtins'


# Generated at 2022-06-14 02:07:29.319142
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert len(SixMovesTransformer.rewrites) == len(set(SixMovesTransformer.rewrites))
    def check_one(a):
        return a[0] == 'six.moves.urllib.request' and a[1] == 'urllib.request'
    assert any(check_one(a) for a in SixMovesTransformer.rewrites)  # any will short-circuit

# Generated at 2022-06-14 02:07:35.481869
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert (('urllib.parse.ParseResult', 'six.moves.urllib_parse.ParseResult')
            in SixMovesTransformer._get_rewrites())


# Run the unit tests in this module.
if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 02:07:39.742005
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    MovedAttribute('test', 'old', 'test')
    MovedAttribute('test', 'old', 'test', 't')
    MovedAttribute('test', 'old', 'test', old_attr='t')


# Generated at 2022-06-14 02:07:52.823667
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    import six
    import six.moves

    source = """
        from six.moves import UserList
        from six.moves import xrange
        from six.moves import http_cookies
        from six import moves
        import six
    """
    imports = ['six.moves.UserList', 'six.moves.xrange', 'six.moves.http_cookies',
               'six.moves', 'six']
    imports_res = ['six.moves.UserList', 'six.moves.xrange', 'six.moves.http_cookies',
               'six.moves', 'six']

    code = SixMovesTransformer.rewrite(source, imports)
    assert code == source
    assert imports == imports_res


# Generated at 2022-06-14 02:08:03.970341
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert MovedAttribute('a', 'b', 'c').name == 'a', "name attribute is not set correctly"
    assert MovedAttribute('a', 'b', 'c').new_mod == 'c', "new_mod attribute is not set correctly"
    assert MovedAttribute('a', 'b', 'c').new_attr == 'a', "new_attr attribute is not set correctly"
    assert MovedAttribute('a', 'b', 'c', 'd', 'e').name == 'a', "name attribute is not set correctly"
    assert MovedAttribute('a', 'b', 'c', 'd', 'e').new_mod == 'c', "new_mod attribute is not set correctly"

# Generated at 2022-06-14 02:08:05.990417
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    six_moves_transformer = SixMovesTransformer()
    assert isinstance(six_moves_transformer, BaseImportRewrite)

# Generated at 2022-06-14 02:08:13.579753
# Unit test for constructor of class MovedModule
def test_MovedModule():
    mm = MovedModule('foo', 'bar')
    assert mm.name == 'foo'
    assert mm.old == 'bar'
    assert mm.new == 'foo'
    mm = MovedModule('foo', 'bar', 'baz')
    assert mm.name == 'foo'
    assert mm.old == 'bar'
    assert mm.new == 'baz'



# Generated at 2022-06-14 02:08:15.449000
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    SixMovesTransformer()

# Generated at 2022-06-14 02:08:17.248420
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    SixMovesTransformer()

# Generated at 2022-06-14 02:08:29.805676
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    move = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert move.name == "cStringIO"
    assert move.new_mod == "io"
    assert move.new_attr == "StringIO"
    move = MovedAttribute("cStringIO", "cStringIO", "io")
    assert move.name == "cStringIO"
    assert move.new_mod == "io"
    assert move.new_attr == "cStringIO"
    move = MovedAttribute("filter", "itertools", "builtins", "ifilter", "filter")
    assert move.name == "filter"
    assert move.new_mod == "builtins"
    assert move.new_attr == "filter"

# Generated at 2022-06-14 02:08:40.347562
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():

    # Tests some static properties
    assert SixMovesTransformer.target == (2, 7)
    assert isinstance(SixMovesTransformer.rewrites, dict)
    assert len(SixMovesTransformer.rewrites) >= _urllib_request_moved_attributes + \
        _urllib_response_moved_attributes + \
        _urllib_parse_moved_attributes + \
        _urllib_error_moved_attributes + \
        _urllib_robotparser_moved_attributes
    assert isinstance(SixMovesTransformer.dependencies, list)
    assert 'six' in SixMovesTransformer.dependencies
    assert len(SixMovesTransformer.dependencies) == 1

# Generated at 2022-06-14 02:08:45.203029
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert MovedAttribute('cStringIO', "cStringIO", "io", "StringIO").new_attr == "StringIO"
    assert MovedAttribute('cStringIO', "cStringIO", "io", "StringIO").name == "cStringIO"

# Generated at 2022-06-14 02:08:50.888262
# Unit test for constructor of class MovedModule
def test_MovedModule():
    name = 'name'
    old = 'old'
    new = 'new'
    m = MovedModule(name, old, new)
    assert name == m.name
    assert old == m.old
    assert new == m.new


# Generated at 2022-06-14 02:08:57.387048
# Unit test for constructor of class MovedModule
def test_MovedModule():
    assert MovedModule("name", "old_name").name == "name"
    assert MovedModule("name", "old_name").new == "name"

    assert MovedModule("name", "old_name", "new_name").name == "name"
    assert MovedModule("name", "old_name", "new_name").new == "new_name"


# Generated at 2022-06-14 02:09:06.440748
# Unit test for constructor of class SixMovesTransformer

# Generated at 2022-06-14 02:09:13.086301
# Unit test for constructor of class MovedModule
def test_MovedModule():
    mm = MovedModule("name", "old", "new")
    assert mm.name == "name"
    assert mm.old == "old"
    assert mm.new == "new"

    mm = MovedModule("name", "old")
    assert mm.name == "name"
    assert mm.old == "old"
    assert mm.new == "name"



# Generated at 2022-06-14 02:09:23.096474
# Unit test for constructor of class MovedModule
def test_MovedModule():
    for mod in _moved_attributes:
        if isinstance(mod, MovedModule):
            assert mod.new == mod.name
            assert mod.name in mod.new



# Generated at 2022-06-14 02:09:26.230050
# Unit test for constructor of class MovedModule
def test_MovedModule():
    assert MovedModule("foo", "bar").name == "foo"
    assert MovedModule("foo", "bar").new == "foo"


# Generated at 2022-06-14 02:09:27.952709
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert len(SixMovesTransformer.rewrites) == 119



# Generated at 2022-06-14 02:09:31.705849
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    obj = SixMovesTransformer()

    # Test for class attributes
    assert obj.target == (2, 7)
    assert len(obj.rewrites) == 70
    assert obj.dependencies == ['six']

# Generated at 2022-06-14 02:09:34.973518
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    for (path, rewrite) in _get_rewrites():
        assert path in SixMovesTransformer.rewrites
        assert rewrite in SixMovesTransformer.rewrites.values()

# Generated at 2022-06-14 02:09:39.312841
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    ma = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert ma.name == "cStringIO"
    assert ma.new_mod == "io"
    assert ma.new_attr == "StringIO"



# Generated at 2022-06-14 02:09:51.416576
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    ma = MovedAttribute('a', 'A', 'B')
    assert ma.name == 'a'
    assert ma.new_mod == 'A'
    assert ma.new_attr == 'a'

    ma = MovedAttribute('a', 'A', 'B', 'b')
    assert ma.name == 'a'
    assert ma.new_mod == 'A'
    assert ma.new_attr == 'b'

    ma = MovedAttribute('a', 'A', 'B', 'b', 'c')
    assert ma.name == 'a'
    assert ma.new_mod == 'A'
    assert ma.new_attr == 'c'


# Generated at 2022-06-14 02:09:58.245802
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert MovedAttribute('zip', 'itertools', 'builtins', 'izip', 'zip') == MovedAttribute('zip',
                                                                                           'itertools',
                                                                                           'builtins',
                                                                                           'izip',
                                                                                           'zip')

    class MyException(Exception):
        pass

    with pytest.raises(MyException):
        MovedAttribute('zip', 'itertools', 1, 'izip', 'zip')



# Generated at 2022-06-14 02:10:00.050473
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert SixMovesTransformer.rewrites


# Generated at 2022-06-14 02:10:03.213521
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    obj = SixMovesTransformer()
    assert obj.target == (2, 7)
    assert obj.rewrites[0] == ('builtins.cStringIO', 'six.moves.cStringIO')

# Generated at 2022-06-14 02:10:22.851717
# Unit test for constructor of class MovedModule
def test_MovedModule():
    """Test for MovedModule constructor."""
    moved_modules = [
        MovedModule('statistics', 'statistics'),
        MovedModule('statistics', 'statistics', 'statistics')
    ]
    assert moved_modules[0].name == 'statistics'
    assert moved_modules[0].new is None
    assert moved_modules[1].name == 'statistics'
    assert moved_modules[1].new == 'statistics'


# Generated at 2022-06-14 02:10:25.878743
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    for _, tm in prefixed_moves:
        for mt in tm:
            if isinstance(mt, MovedModule):
                assert mt.name in SixMovesTransformer.rewrites

# Generated at 2022-06-14 02:10:35.636188
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    # pylint: disable=unused-variable
    # pylint: disable=expression-not-assigned
    a = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    b = MovedAttribute("filter", "itertools", "builtins", "ifilter", "filter")
    c = MovedAttribute("input", "__builtin__", "builtins", "raw_input", "input")
    d = MovedAttribute("intern", "__builtin__", "sys")
    e = MovedAttribute("map", "itertools", "builtins", "imap", "map")
    f = MovedAttribute("getcwd", "os", "os", "getcwdu", "getcwd")

# Generated at 2022-06-14 02:10:39.188846
# Unit test for constructor of class MovedModule
def test_MovedModule():
    from . import base
    from .base import BaseImportRewrite
    assert base
    assert BaseImportRewrite
    assert SixMovesTransformer

# Generated at 2022-06-14 02:10:44.115652
# Unit test for constructor of class MovedModule
def test_MovedModule():
    mm = MovedModule("foo", "bar", "baz")
    assert mm.name == "foo"
    assert mm.old == "bar"
    assert mm.new == "baz"


# Generated at 2022-06-14 02:10:45.915079
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    transformer = SixMovesTransformer()
    assert transformer is not None


# Generated at 2022-06-14 02:10:51.559970
# Unit test for constructor of class MovedModule
def test_MovedModule():
    n = MovedModule('hello', 'foo', 'bar')
    assert n.name == 'hello'
    assert n.new == 'bar'

    n = MovedModule('hello', 'foo')
    assert n.name == 'hello'
    assert n.new == 'hello'



# Generated at 2022-06-14 02:10:59.705512
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert MovedAttribute('cStringIO', 'cStringIO', 'io', 'StringIO').name == 'cStringIO'
    assert MovedAttribute('reduce', '__builtin__', 'functools').new_mod == 'functools'
    assert MovedAttribute('range', '__builtin__', 'builtins', 'xrange', 'range').old_attr == 'xrange'
    assert MovedAttribute('zip', 'itertools', 'builtins', 'izip', 'zip').new_attr == 'zip'


# Generated at 2022-06-14 02:11:05.701687
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    # Check if len(_get_rewrites) == len(SixMovesTransformer.rewrites)
    num_items_1 = len(_get_rewrites())
    num_items_2 = len(SixMovesTransformer.rewrites)
    assert num_items_1 == num_items_2
    # Check if len(SixMovesTransformer.rewrites) > 0
    assert len(SixMovesTransformer.rewrites) > 0

# Generated at 2022-06-14 02:11:07.694068
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert six.moves.urllib.parse == 'six.moves.urllib_parse'

# Generated at 2022-06-14 02:11:40.511469
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    # Test for successful initialization
    SixMovesTransformer()
    # Test for TypeError
    type_test = False
    try:
        SixMovesTransformer(3)
    except TypeError:
        type_test = True
    assert type_test
    # Test for ValueError
    value_test = False
    try:
        SixMovesTransformer((3,))
    except ValueError:
        value_test = True
    assert value_test
    # Test for ValueError
    value_test = False
    try:
        SixMovesTransformer((3, 2))
    except ValueError:
        value_test = True
    assert value_test
    # Test for ValueError
    value_test = False
    try:
        SixMovesTransformer((2, 3, 1))
    except ValueError:
        value

# Generated at 2022-06-14 02:11:53.380880
# Unit test for constructor of class SixMovesTransformer

# Generated at 2022-06-14 02:11:57.705926
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    moves_test = MovedAttribute(name='test', old_mod='test', new_mod='test', old_attr='test', new_attr='test')
    assert moves_test.name == 'test'
    assert moves_test.new_mod == 'test'
    assert moves_test.new_attr == 'test'


# Generated at 2022-06-14 02:11:58.501207
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert True

# Generated at 2022-06-14 02:12:02.660375
# Unit test for constructor of class MovedModule
def test_MovedModule():
    mm = MovedModule("name", "old", "new")
    assert mm.name == 'name'
    assert mm.new == 'new'
    mm = MovedModule("name", "old")
    assert mm.name == 'name'
    assert mm.new == 'name'

# Generated at 2022-06-14 02:12:05.439151
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    # Test if SixMovesTransformer is instance of BaseImportRewrite
    assert isinstance(SixMovesTransformer(), BaseImportRewrite)

# Generated at 2022-06-14 02:12:16.760409
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    a = MovedAttribute("test1", "test2", "test3")
    assert a.name == "test1"
    assert a.new_mod == "test2"
    assert a.new_attr == "test1"
    assert str(a) == "test1"
    a = MovedAttribute("test1", "test2", "test3", old_attr="test4")
    assert a.name == "test1"
    assert a.new_mod == "test2"
    assert a.old_attr == "test4"
    assert a.new_attr == "test4"
    assert str(a) == "test1"
    a = MovedAttribute("test1", "test2", "test3", new_attr="test4")
    assert a.name == "test1"
    assert a.new_

# Generated at 2022-06-14 02:12:21.318696
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    six_moves_transformer = SixMovesTransformer()

    assert six_moves_transformer.target == (2, 7)
    assert six_moves_transformer.rewrites == _get_rewrites()
    assert six_moves_transformer.dependencies == ['six']

# Generated at 2022-06-14 02:12:26.727796
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    m = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert m.name == "cStringIO"
    assert m.new_mod == "io"
    assert m.new_attr == "StringIO"

    m = MovedAttribute("cStringIO", "cStringIO", "io")
    assert m.name == "cStringIO"
    assert m.new_mod == "io"
    assert m.new_attr == "cStringIO"

    m = MovedAttribute("cStringIO", "cStringIO", "io", None, "foo")
    assert m.name == "cStringIO"
    assert m.new_mod == "io"
    assert m.new_attr == "foo"


# Generated at 2022-06-14 02:12:31.922342
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    if sys.version_info < (2, 7):
        assert SixMovesTransformer.rewrites == []
    else:
        assert SixMovesTransformer.rewrites

if __name__ == '__main__':
    print(SixMovesTransformer.rewrites)

# Generated at 2022-06-14 02:13:26.897317
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    move = MovedAttribute("string", "__builtin__", "builtins", "x", "y")
    assert(move.name == "string")
    assert(move.new_mod == "builtins")
    assert(move.new_attr == "y")
    move = MovedAttribute("string", "builtins", None)
    assert(move.new_mod == "string")
    assert(move.new_attr == "string")

# Generated at 2022-06-14 02:13:30.625493
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert hasattr(SixMovesTransformer, 'rewrites')
    assert isinstance(SixMovesTransformer.rewrites, dict)
    assert SixMovesTransformer.rewrites == _get_rewrites()


# Generated at 2022-06-14 02:13:36.814744
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    import six
    source = '''
import six.moves.cStringIO.StringIO
'''
    expect = '''
import StringIO
'''
    result, info = SixMovesTransformer.rewrite(source, options={})
    assert info.get('error') is None
    assert result == expect

# Generated at 2022-06-14 02:13:38.145312
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    a = SixMovesTransformer()
    assert not a.rewrites

# Generated at 2022-06-14 02:13:44.016815
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert(MovedAttribute('name', 'old_mod', 'new_mod').name == 'name')
    assert(MovedAttribute('name', 'old_mod', 'new_mod').new_mod == 'new_mod')
    assert(MovedAttribute('name', 'old_mod', 'new_mod').new_attr == 'name')

# Unit tests for constructors for class MovedModule

# Generated at 2022-06-14 02:13:46.712731
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    from lib2to3.fixes import FixerError
    with pytest.raises(FixerError):
        SixMovesTransformer("invalid", None, None, None)

# Generated at 2022-06-14 02:13:53.134576
# Unit test for constructor of class MovedModule
def test_MovedModule():
    mod = MovedModule("builtins", "__builtin__")
    assert mod.name == "builtins"
    assert mod.new == "builtins"

    mod = MovedModule("foo", "bar", "baz")
    assert mod.name == "foo"
    assert mod.new == "baz"


# Unit tests for constructor of class MovedAttribute

# Generated at 2022-06-14 02:13:58.051846
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    import types
    assert isinstance(SixMovesTransformer, type)
    assert isinstance(SixMovesTransformer(), BaseImportRewrite)
    assert isinstance(SixMovesTransformer.dependencies, types.TupleType)

# Unit tests for SixMovesTransformer.rewrites

# Generated at 2022-06-14 02:14:03.321750
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    attribute = MovedAttribute('name', 'old_mod', 'new_mod', 'old_attr', 'new_attr')
    assert attribute.name == 'name'
    assert attribute.old_mod == 'old_mod'
    assert attribute.new_mod == 'new_mod'
    assert attribute.old_attr == 'old_attr'
    assert attribute.new_attr == 'new_attr'


# Generated at 2022-06-14 02:14:08.057350
# Unit test for constructor of class MovedModule
def test_MovedModule():
    moved_module = MovedModule('tkinter', 'Tkinter')
    assert moved_module.name == 'tkinter'
    assert moved_module.old == 'Tkinter'
    assert moved_module.new == 'tkinter'


# Generated at 2022-06-14 02:16:00.038146
# Unit test for constructor of class MovedModule
def test_MovedModule():
    assert MovedModule('test_name', 'old').name == 'test_name'
    assert MovedModule('test_name', 'old').new == 'test_name'
    assert MovedModule('test_name', 'old', 'new').new == 'new'


# Generated at 2022-06-14 02:16:06.195300
# Unit test for constructor of class MovedModule
def test_MovedModule():
    assert MovedModule("foo", "bar").name == "foo"
    assert MovedModule("foo", "bar").old == "bar"
    assert MovedModule("foo", "bar").new == "foo"
    assert MovedModule("foo", "bar", "baz").name == "foo"
    assert MovedModule("foo", "bar", "baz").old == "bar"
    assert MovedModule("foo", "bar", "baz").new == "baz"

