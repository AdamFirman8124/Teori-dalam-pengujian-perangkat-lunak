

# Generated at 2022-06-14 02:06:08.670906
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    def assertTransf(code, expected):
        t = SixMovesTransformer()
        res = t.preprocess(code)
        assert res == expected, res
    assertTransf("from six.moves import deque", "from six.moves import deque")
    assertTransf("from StringIO import StringIO", "from six.moves import StringIO")
    assertTransf("import StringIO", "from six.moves import StringIO")
    assertTransf("from urllib.parse import urlparse", "from six.moves.urllib_parse import urlparse")

# Unit tests for the eager factory _get_rewrites()

# Generated at 2022-06-14 02:06:11.392612
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    x = MovedAttribute('x', 'oldmod', 'newmod', 'oldattr', 'newattr')
    assert x.name == 'x'
    assert x.new_mod == 'newmod'
    assert x.new_attr == 'newattr'

# Generated at 2022-06-14 02:06:12.345392
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert SixMovesTransformer()

# Generated at 2022-06-14 02:06:23.272627
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert MovedAttribute("", "", "", "", "").name == ""
    assert MovedAttribute("test", "test2", "test3", "test4", "test5").name == "test"
    assert MovedAttribute("test", "test2", "test3", "test4", "test5").new_mod == "test3"
    assert MovedAttribute("test", "test2", "test3", "test4", "test5").new_attr == "test5"
    assert MovedAttribute("test", "test2", "test3", "test4").new_attr == "test4"
    assert MovedAttribute("test", "test2", "test3").new_attr == "test"
    assert MovedAttribute("test", "test2", "test3", new_attr="test4").new_attr == "test4"

# Generated at 2022-06-14 02:06:32.887357
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert MovedAttribute('foo', 'bar', None) == MovedAttribute('foo', 'bar', None)
    assert MovedAttribute('foo', 'bar', None) != MovedAttribute('bar', 'foo', None)
    assert MovedAttribute('foo', 'bar', 'baz', 'boo') == MovedAttribute('foo', 'bar', 'baz', 'boo')
    assert MovedAttribute('foo', 'bar', 'baz', 'boo') != MovedAttribute('bar', 'foo', 'baz', 'boo')
    assert MovedAttribute('foo', 'bar', 'baz', 'boo') != MovedAttribute('foo', 'bar', 'zab', 'boo')

# Generated at 2022-06-14 02:06:43.109408
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert MovedAttribute('name', 'old_mod', 'new_mod', 'old_attr', 'new_attr').name == 'name'
    assert MovedAttribute('name', 'old_mod', 'new_mod', 'old_attr', 'new_attr').new_mod == 'new_mod'
    assert MovedAttribute('name', 'old_mod', 'new_mod', 'old_attr', 'new_attr').new_attr == 'new_attr'
    assert MovedAttribute('name', 'old_mod', 'new_mod', 'old_attr', 'new_attr').name == 'name'


# Generated at 2022-06-14 02:06:46.142665
# Unit test for constructor of class MovedModule
def test_MovedModule():
    foo = MovedModule("foo", "bar")
    assert foo.name == "foo"
    assert foo.new == "foo"
    assert foo.old == "bar"

# Generated at 2022-06-14 02:06:58.070846
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    # test standard call
    m = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert m.name == "cStringIO"
    assert m.new_mod == "io"
    assert m.new_attr == "StringIO"

    # test with name and newmod only
    m = MovedAttribute("parse_qsl", "urlparse", "urllib.parse")
    assert m.name == "parse_qsl"
    assert m.new_mod == "urllib.parse"
    assert m.new_attr == "parse_qsl"

    # test with name and oldattr only
    m = MovedAttribute("input", "__builtin__", "builtins", "raw_input")
    assert m.name == "input"

# Generated at 2022-06-14 02:07:03.540535
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    # pylint: disable=W0212
    assert len(SixMovesTransformer.rewrites) == 34


if __name__ == '__main__':
    # pylint: disable=wrong-import-position
    from lib2to3.main import main
    main("lib2to3.fixes.fix_six_moves")

# Generated at 2022-06-14 02:07:06.335137
# Unit test for constructor of class MovedModule
def test_MovedModule():
    assert MovedModule('builtins', None, '__builtin__').name == 'builtins'
    assert MovedModule('builtins', None, '__builtin__').new == '__builtin__'



# Generated at 2022-06-14 02:07:18.922457
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert len(SixMovesTransformer.rewrites) == 35
    for prefix, moves in prefixed_moves:
        for move in moves:
            if isinstance(move, MovedAttribute):
                path = '{}.{}'.format(move.new_mod, move.new_attr)
                assert ('{}'.format(path), 'six.moves{}.{}'.format(prefix, move.name)) in SixMovesTransformer.rewrites
            elif isinstance(move, MovedModule):
                assert ('{}'.format(move.new), 'six.moves{}.{}'.format(prefix, move.name)) in SixMovesTransformer.rewrites

# Generated at 2022-06-14 02:07:23.100885
# Unit test for constructor of class MovedModule
def test_MovedModule():
    module_moved = MovedModule('name', 'old_name', 'new_name')
    assert module_moved.name == 'new_name'
    assert module_moved.old == 'old_name'
    assert module_moved.new == 'new_name'

# Generated at 2022-06-14 02:07:29.374153
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert len(_get_rewrites()) == len(set(_get_rewrites()))  # no repeats
    assert (u'urllib.parse.parse_qs', u'six.moves.urllib_parse.parse_qs') in _get_rewrites()
    assert (u'urllib.parse.unquote', u'six.moves.urllib_parse.unquote') in _get_rewrites()

# Generated at 2022-06-14 02:07:33.207943
# Unit test for constructor of class MovedModule
def test_MovedModule():
    # no 'new' passed
    mm = MovedModule('name', 'old')
    assert mm.name == 'name'
    assert mm.old == 'old'
    assert mm.new == 'name'

    # 'new' passed
    mm = MovedModule('name', 'old', 'new')
    assert mm.name == 'name'
    assert mm.old == 'old'
    assert mm.new == 'new'



# Generated at 2022-06-14 02:07:35.191188
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert SixMovesTransformer(None) is not None

# Generated at 2022-06-14 02:07:38.127509
# Unit test for constructor of class MovedModule
def test_MovedModule():
    assert MovedModule("new", "old").name == "new"
    assert MovedModule("new", "old").new == "new"



# Generated at 2022-06-14 02:07:42.849955
# Unit test for constructor of class MovedModule
def test_MovedModule():
    assert MovedModule('name', 'old').name == 'name'
    assert MovedModule('name', 'old').new == 'name'
    assert MovedModule('name', 'old', 'new').name == 'name'
    assert MovedModule('name', 'old', 'new').new == 'new'


# Generated at 2022-06-14 02:07:54.811780
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    attr = MovedAttribute('cStringIO', 'cStringIO', 'io', 'StringIO')
    assert attr.name == 'cStringIO'
    assert attr.new_mod == 'io'
    assert attr.new_attr == 'StringIO'
    attr = MovedAttribute('cStringIO', 'cStringIO', None, 'StringIO')
    assert attr.name == 'cStringIO'
    assert attr.new_mod == 'cStringIO'
    assert attr.new_attr == 'StringIO'
    attr = MovedAttribute('cStringIO', 'cStringIO', 'io', None)
    assert attr.name == 'cStringIO'
    assert attr.new_mod == 'io'
    assert attr.new_attr == 'cStringIO'

# Generated at 2022-06-14 02:07:57.622283
# Unit test for constructor of class MovedModule
def test_MovedModule():
    moved_module = MovedModule("foo", "bar", "baz")
    assert moved_module.name == "foo"
    assert moved_module.new == "baz"


# Generated at 2022-06-14 02:08:01.016334
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert len(_get_rewrites()) == len(SixMovesTransformer.rewrites)
    # test that the rewrites were filled properly
    for (path, rewrite) in SixMovesTransformer.rewrites:
        assert 'six.moves' in rewrite

# Generated at 2022-06-14 02:08:04.704359
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert SixMovesTransformer.rewrites is not None

# Generated at 2022-06-14 02:08:05.669241
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert SixMovesTransformer(None).rewrites

# Generated at 2022-06-14 02:08:08.030517
# Unit test for constructor of class MovedModule
def test_MovedModule():
    moved = MovedModule('test', 'old_name')
    assert moved.name == 'test'
    assert moved.new == 'test'
    assert moved.old == 'old_name'

# Generated at 2022-06-14 02:08:16.463302
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    result = set(_get_rewrites())

# Generated at 2022-06-14 02:08:20.906945
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert len(SixMovesTransformer.rewrites) > 0

    for path, replacement in SixMovesTransformer.rewrites:
        assert isinstance(path, str)
        assert isinstance(replacement, str)

# Generated at 2022-06-14 02:08:32.508839
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    a = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert a.name == "cStringIO"
    assert a.new_mod == "io"
    assert a.new_attr == "StringIO"
    b = MovedAttribute("filter", "itertools", "builtins", "ifilter", "filter")
    assert b.name == "filter"
    assert b.new_mod == "builtins"
    assert b.new_attr == "filter"
    c = MovedAttribute("input", "__builtin__", "builtins", "raw_input", "input")
    assert c.name == "input"
    assert c.new_mod == "builtins"
    assert c.new_attr == "input"
    # test for new_attr == None

# Generated at 2022-06-14 02:08:48.923589
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert MovedAttribute('a', 'b', 'c', 'd', 'e') == MovedAttribute('a', 'b', 'c', 'd', 'e')
    assert MovedAttribute('a', 'b', 'c', 'd', 'e') != MovedAttribute('a', 'b', 'c', 'd', 'f')
    assert MovedAttribute('a', 'b', 'c', 'd') == MovedAttribute('a', 'b', 'c', 'd')
    assert MovedAttribute('a', 'b', 'c', 'd') != MovedAttribute('a', 'b', 'c', 'e')
    assert MovedAttribute('a', 'b', 'c', new_attr='e') == MovedAttribute('a', 'b', 'c', 'd', 'e')

# Generated at 2022-06-14 02:08:53.139894
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    s = SixMovesTransformer()
    assert not hasattr(s, 'rewrites')
    assert hasattr(s, '_rewrites')
    assert s._rewrites == _get_rewrites()


# Generated at 2022-06-14 02:08:55.549119
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert MovedAttribute('input', '__builtin__', 'builtins', 'raw_input', 'input') is not None

# Generated at 2022-06-14 02:09:01.104217
# Unit test for constructor of class MovedModule
def test_MovedModule():
    mo = MovedModule('test1', 'test2')
    assert mo.name == 'test1'
    assert mo.old == 'test2'
    assert mo.new == 'test1'

    mo = MovedModule('test1', 'test2', 'test3')
    assert mo.name == 'test1'
    assert mo.old == 'test2'
    assert mo.new == 'test3'

# Generated at 2022-06-14 02:09:12.409769
# Unit test for constructor of class MovedModule
def test_MovedModule():
    # type: () -> None
    m1 = MovedModule('name', 'old')
    assert m1.name == 'name'
    assert m1.old == 'old'
    assert m1.new == 'name'

    m2 = MovedModule('name', 'old', 'new')
    assert m2.name == 'name'
    assert m2.old == 'old'
    assert m2.new == 'new'

# Generated at 2022-06-14 02:09:15.520028
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert not SixMovesTransformer.rewrites._value
    SixMovesTransformer.rewrites
    assert SixMovesTransformer.rewrites._value


if __name__ == '__main__':
    SixMovesTransformer.print_differences()

# Generated at 2022-06-14 02:09:17.959328
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert MovedAttribute('cStringIO', 'cStringIO', 'io', 'StringIO').__str__() == \
        "cStringIO : cStringIO.StringIO --> io.cStringIO"



# Generated at 2022-06-14 02:09:21.642558
# Unit test for constructor of class MovedModule
def test_MovedModule():
    m = MovedModule("name1", "old1")
    assert m.name == "name1"
    assert m.new == "name1"
    m = MovedModule("name2", "old2", "new2")
    assert m.name == "name2"
    assert m.new == "new2"


# Generated at 2022-06-14 02:09:30.976423
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    x = MovedAttribute('name', 'old', 'new')
    assert x.name == 'name'
    assert x.new_mod == 'new'
    assert x.new_attr == 'name'
    x = MovedAttribute('name', 'old', 'new', 'oldattr')
    assert x.new_attr == 'oldattr'
    x = MovedAttribute('name', 'old', 'new', 'oldattr', 'newattr')
    assert x.new_attr == 'newattr'
    y = MovedAttribute('name', 'old', 'new', new_attr='newattr')
    assert y.new_attr == 'newattr'
    with pytest.raises(TypeError):
        MovedAttribute('name', 'old', 'new', new_attr='newattr', old_attr='oldattr')

# Generated at 2022-06-14 02:09:40.224423
# Unit test for constructor of class MovedModule
def test_MovedModule():
    assert MovedModule("test_module1", "test_old1", "test_new1") == \
           MovedModule("test_module1", "test_old1", "test_new1")
    assert str(MovedModule("test_module2", "test_old2", "test_new2")) == \
           "MovedModule(name='test_module2', old='test_old2', new='test_new2')"

# Generated at 2022-06-14 02:09:48.772942
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert MovedAttribute('X', 'a', 'b', 'c', 'd').__dict__ == {
        'name': 'X', 'old_mod': 'a', 'new_mod': 'b', 'old_attr': 'c', 'new_attr': 'd'
    }
    assert MovedAttribute('X', 'a', 'b', 'c').__dict__ == {
        'name': 'X', 'old_mod': 'a', 'new_mod': 'b', 'old_attr': 'c', 'new_attr': 'c'
    }
    assert MovedAttribute('X', 'a', 'b').__dict__ == {
        'name': 'X', 'old_mod': 'a', 'new_mod': 'b', 'old_attr': None, 'new_attr': 'X'
    }

#

# Generated at 2022-06-14 02:09:58.246995
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    # Passing wrong number of arguments.
    with pytest.raises(TypeError):
        MovedAttribute("cStringIO")

    # Passing wrong argument types.
    with pytest.raises(ValueError):
        MovedAttribute("cStringIO", 10, 2, 3, 4)

    # Passing wrong argument types for new_mod and new_attr.
    with pytest.raises(ValueError):
        MovedAttribute("cStringIO", "cStringIO", 10, 3, 4)

    # Expecting no exception to be raised.
    MovedAttribute("cStringIO", "cStringIO", "io", "StringIO", "StringIO")

# Generated at 2022-06-14 02:10:02.572398
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    rewrite = SixMovesTransformer()
    assert rewrite.rewrites == _get_rewrites()

if __name__ == '__main__':
    from unittest import main
    main()

# Generated at 2022-06-14 02:10:08.539067
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    moved_attribute = MovedAttribute(name="cStringIO", old_mod="cStringIO", new_mod="io", old_attr="StringIO")
    assert moved_attribute.name == "cStringIO"
    assert moved_attribute.new_mod == "io"
    assert moved_attribute.new_attr == "StringIO"


# Generated at 2022-06-14 02:10:16.255718
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    """Test SixMovesTransformer constructor"""
    transformer = SixMovesTransformer('six')
    assert transformer


# Generated at 2022-06-14 02:10:20.529284
# Unit test for constructor of class SixMovesTransformer

# Generated at 2022-06-14 02:10:25.461690
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    move = MovedAttribute("name", "old_mod", "new_mod", "old_attr", "new_attr")
    assert move.name=="name"
    assert move.new_mod=="new_mod"
    assert move.new_attr=="new_attr"

# Generated at 2022-06-14 02:10:31.789913
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    MovedAttribute("name", "old_mod", "new_mod")
    MovedAttribute("name", "old_mod", "new_mod", "old_attr")
    MovedAttribute("name", "old_mod", "new_mod", "old_attr", "new_attr")
    MovedAttribute("name", "old_mod", "new_mod", new_attr="new_attr")
    MovedAttribute("name", "old_mod", "new_mod", "old_attr", new_attr="new_attr")

# Generated at 2022-06-14 02:10:38.678402
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    smt = SixMovesTransformer()
    # Assert that all target modules are rewritable
    modules = [rewrite[0] for rewrite in smt.rewrites]
    for module in modules:
        assert smt.is_rewrite_needed(module)
    # Test that the module translator can translate modules
    assert smt.get_module_name(module) == 'six.moves'

# Generated at 2022-06-14 02:10:51.323980
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    att = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert att.name == "cStringIO"
    assert att.new_mod == "io"
    assert att.new_attr == "StringIO"
    att = MovedAttribute("cStringIO", "cStringIO", "io")
    assert att.name == "cStringIO"
    assert att.new_mod == "io"
    assert att.new_attr == "cStringIO"
    att = MovedAttribute("cStringIO", "cStringIO", "io", new_attr="newStringIO")
    assert att.name == "cStringIO"
    assert att.new_mod == "io"
    assert att.new_attr == "newStringIO"


# Generated at 2022-06-14 02:10:54.955323
# Unit test for constructor of class MovedModule
def test_MovedModule():
    moved_module_test = MovedModule('a', 'b')
    assert moved_module_test.name == 'a'
    assert moved_module_test.new == 'b'

# Generated at 2022-06-14 02:11:04.198205
# Unit test for constructor of class MovedModule
def test_MovedModule():
    assert MovedModule("configparser", "ConfigParser").name == "configparser"
    assert MovedModule("configparser", "ConfigParser", "configparser").name == "configparser"
    assert MovedModule("configparser", "ConfigParser", "configparser").new == "configparser"
    assert MovedModule("configparser", "ConfigParser").old == "ConfigParser"
    assert MovedModule("configparser", "ConfigParser", "confuparser").old == "ConfigParser"
    assert MovedModule("configparser", "ConfigParser", None).new == "configparser"
    assert MovedModule("configparser", "ConfigParser", None).old == "ConfigParser"



# Generated at 2022-06-14 02:11:05.045362
# Unit test for constructor of class MovedModule
def test_MovedModule():
    MovedModule("builtins", "__builtin__")

# Generated at 2022-06-14 02:11:08.755155
# Unit test for constructor of class MovedModule
def test_MovedModule():
    try:
        t = MovedModule("tkinter", "Tkinter")
    except:
        assert False
    else:
        assert True


# Generated at 2022-06-14 02:11:23.189387
# Unit test for constructor of class MovedModule
def test_MovedModule():
    attr = MovedModule("queue", "Queue")
    assert attr.name == 'queue'
    assert attr.new == 'Queue'


# Generated at 2022-06-14 02:11:29.224491
# Unit test for constructor of class MovedModule
def test_MovedModule():
    move = MovedModule("builtins", "__builtin__")
    assert move.name == "builtins"
    assert move.new == "builtins"

    move = MovedModule("builtins", "__builtin__", "blt")
    assert move.name == "builtins"
    assert move.new == "blt"

# Generated at 2022-06-14 02:11:39.753939
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    x = MovedAttribute("cStringIO", "cStringIO", "io")
    y = MovedAttribute("reload_module", "__builtin__", "imp", "reload")
    z = MovedAttribute("reload_module", "__builtin__", "importlib", "reload")
    assert x.name == "cStringIO"
    assert y.name == "reload_module"
    assert z.name == "reload_module"
    assert x.new_mod == "io"
    assert x.new_attr == "cStringIO"
    assert y.new_mod == "imp"
    assert y.new_attr == "reload"
    assert z.new_mod == "importlib"
    assert z.new_attr == "reload"


# Generated at 2022-06-14 02:11:42.765063
# Unit test for constructor of class MovedModule
def test_MovedModule():
    moved_module = MovedModule("winreg", "_winreg")
    assert moved_module.name == "winreg"
    assert moved_module.new == "_winreg"

# Generated at 2022-06-14 02:11:54.532014
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert MovedAttribute('foobar', 'a', 'b').__dict__ == {'name': 'foobar', 'new_mod': 'b', 'new_attr': 'foobar'}
    assert MovedAttribute('foobar', 'a', 'b', 'c').__dict__ == {'name': 'foobar', 'new_mod': 'b', 'new_attr': 'c'}
    assert MovedAttribute('foobar', 'a', 'b', 'c', 'd').__dict__ == {'name': 'foobar', 'new_mod': 'b', 'new_attr': 'd'}
    assert MovedAttribute('foobar', 'a', 'b', 'c', None).__dict__ == {'name': 'foobar', 'new_mod': 'b', 'new_attr': 'c'}
    assert Moved

# Generated at 2022-06-14 02:12:07.294418
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    move1 = MovedAttribute('test_MovedAttribute', 'six.moves', 'six.moves', 'test_MovedAttribute', 'test_MovedAttribute')
    move2 = MovedAttribute('test_MovedAttribute', 'six.moves', 'six.moves', 'test_MovedAttribute')
    move3 = MovedAttribute('test_MovedAttribute', 'six.moves', 'six.moves', new_attr='test_MovedAttribute')
    move4 = MovedAttribute('test_MovedAttribute', 'six.moves', 'six.moves')
    move5 = MovedAttribute('test_MovedAttribute', 'six.moves')

    assert move1.name == 'test_MovedAttribute'
    assert move1.new_mod == 'six.moves'
    assert move1.old_attr

# Generated at 2022-06-14 02:12:13.628761
# Unit test for constructor of class MovedModule
def test_MovedModule():
    x = MovedModule('name', None, None)
    assert x.name == 'name'
    assert x.new == 'name'
    y = MovedModule('name', None, 'new')
    assert y.name == 'name'
    assert y.new == 'new'
    z = MovedModule('name', None)
    assert z.name == 'name'
    assert z.new == 'name'

# Generated at 2022-06-14 02:12:18.223711
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    move = MovedAttribute('cStringIO', 'cStringIO', 'io', 'StringIO')
    assert move.name == 'cStringIO'
    assert move.new_mod == 'io'
    assert move.new_attr == 'StringIO'

# Generated at 2022-06-14 02:12:21.044430
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert SixMovesTransformer('urllib.parse.urljoin').rewrites == [('urllib.parse.urljoin',
                                                                     'six.moves.urllib_parse.urljoin')]

# Generated at 2022-06-14 02:12:24.740952
# Unit test for constructor of class MovedModule
def test_MovedModule():
    foo = MovedModule('moved_name', 'old_name', 'new_name')
    assert foo.name == 'moved_name'
    assert foo.new == 'new_name'
    assert foo.old == 'old_name'

# Generated at 2022-06-14 02:12:55.588406
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    # This is an example of how to test a constructor.
    # Method __init__ has 5 arguments, 4 of them are optional.
    # We can provide any subset of these arguments.
    # We are testing different types of the arguments.
    # 1. Only one argument. In this case it is supposed to be name.
    a = MovedAttribute('name')
    # 2. Only 2 arguments. In this case name and new_mod.
    b = MovedAttribute('name', 'new_mod')
    # 3. Only 3 arguments. In this case name, new_mod and new_attr.
    c = MovedAttribute('name', 'new_mod', 'new_attr')
    # 4. Three arguments and old_attr.
    d = MovedAttribute('name', 'new_mod', 'new_attr', 'old_attr')
    # 5

# Generated at 2022-06-14 02:12:58.740004
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    transformer = SixMovesTransformer()
    assert transformer.target == (2, 7)
    assert transformer.rewrites == _get_rewrites()
    assert transformer.dependencies == [
        'six']

# Generated at 2022-06-14 02:13:01.673072
# Unit test for constructor of class MovedModule
def test_MovedModule():
    assert MovedModule("") == MovedModule("", "", "")

# Generated at 2022-06-14 02:13:10.305941
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert MovedAttribute("name", "old_mod", "new_mod").__dict__ == \
        {"name": "name", "new_mod": "new_mod", "new_attr": "name"}
    assert MovedAttribute("name", "old_mod", "new_mod", 
                          "old_attr", "new_attr").__dict__ == \
        {"name": "name", "new_mod": "new_mod", "new_attr": "new_attr"}

# Unit tests for constructor of class MovedModule

# Generated at 2022-06-14 02:13:20.370547
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    import six.moves.urllib.error
    import six.moves.urllib.request
    import six.moves.urllib.response
    import six.moves.urllib.robotparser
    from .test_six_moves import _urllib_error_moved_attributes, _urllib_request_moved_attributes, \
        _urllib_response_moved_attributes, _urllib_robotparser_moved_attributes
    for attribute in _urllib_error_moved_attributes:
        path = '{}.{}'.format('six.moves.urllib.error', attribute.name)
        assert getattr(six.moves.urllib.error, attribute.name, path)

# Generated at 2022-06-14 02:13:27.830002
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert MovedAttribute("cStringIO", "cStringIO", "io", "StringIO", "StringIO") == \
        MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert MovedAttribute("cStringIO", "cStringIO", "io", "StringIO") == \
        MovedAttribute("cStringIO", "cStringIO", "io", None, "StringIO")


# Generated at 2022-06-14 02:13:32.473375
# Unit test for constructor of class MovedModule
def test_MovedModule():
    mod = MovedModule("new", "old")
    assert mod.name == "new"
    assert mod.new == "new"
    assert mod.old == "old"
    mod2 = MovedModule("new2", "old2", "m")
    assert mod2.name == "new2"
    assert mod2.new == "m"
    assert mod2.old == "old2"

# Unit tests for constructor of class MovedAttribute

# Generated at 2022-06-14 02:13:44.341959
# Unit test for constructor of class SixMovesTransformer

# Generated at 2022-06-14 02:13:54.333672
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    new_mod = 'new_mod'
    new_attr = 'new_attr'
    old_mod = 'old_mod'
    old_attr = 'old_attr'

    # Check that when we have name, new_mod, and new_attr,
    # old_mod and old_attr are None
    ma = MovedAttribute('name', new_mod, new_attr)
    assert ma.new_mod == new_mod
    assert ma.new_attr == new_attr
    assert ma.old_mod == None
    assert ma.old_attr == None

    # Check that when we have name, new_mod, new_attr, and old_mod,
    # old_attr is None
    ma = MovedAttribute('name', new_mod, new_attr, old_mod)
    assert ma.new_mod == new

# Generated at 2022-06-14 02:13:55.377107
# Unit test for constructor of class MovedModule
def test_MovedModule():
    moved_module = MovedModule('name', 'old')

# Generated at 2022-06-14 02:14:52.416653
# Unit test for constructor of class MovedModule
def test_MovedModule():
    mm = MovedModule("foo", "bar")
    assert mm.name == "foo"
    assert mm.old == "bar"
    assert mm.new == "foo"
    mm = MovedModule("foo", "bar", "baz")
    assert mm.name == "foo"
    assert mm.old == "bar"
    assert mm.new == "baz"

# Generated at 2022-06-14 02:15:05.185019
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert MovedAttribute('cStringIO', 'cStringIO', 'io', 'StringIO').name == 'cStringIO'
    assert MovedAttribute('cStringIO', 'cStringIO', 'io', 'StringIO').new_mod == 'io'
    assert MovedAttribute('cStringIO', 'cStringIO', 'io', 'StringIO').new_attr == 'StringIO'
    assert MovedAttribute('filter', 'itertools', 'builtins', 'ifilter', 'filter').name == 'filter'
    assert MovedAttribute('filter', 'itertools', 'builtins', 'ifilter', 'filter').new_mod == 'builtins'
    assert MovedAttribute('filter', 'itertools', 'builtins', 'ifilter', 'filter').new_attr == 'filter'

# Generated at 2022-06-14 02:15:15.650334
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    MovedAttribute('cStringIO', 'cStringIO', 'io', 'StringIO')
    MovedAttribute('cStringIO', 'cStringIO', 'io', 'StringIO', 'StringIO')
    MovedAttribute('cStringIO', 'cStringIO', 'io')
    MovedAttribute('cStringIO', 'cStringIO')
    # Original test in six:
    # MovedAttribute('cStringIO', 'cStringIO', 'io', old_attr='StringIO',
    # new_mod='io', new_attr='StringIO')
    # MovedAttribute('cStringIO', 'cStringIO', 'io', old_attr='StringIO')
    # MovedAttribute('cStringIO', 'cStringIO', new_attr='StringIO')
    # MovedAttribute('cStringIO', 'cStringIO')


# Unit

# Generated at 2022-06-14 02:15:20.167726
# Unit test for constructor of class MovedModule
def test_MovedModule():
    global _moved_attributes
    for m in _moved_attributes:
        if isinstance(m, MovedModule):
            assert m.name
            assert isinstance(m.name, str)
            assert m.new
            assert isinstance(m.new, str)


# Generated at 2022-06-14 02:15:30.456740
# Unit test for constructor of class MovedModule
def test_MovedModule():
    # Test the basic constructor
    test_move_module = MovedModule("test_name", "test_old")
    assert test_move_module.name == "test_name"
    assert test_move_module.new == "test_name"
    assert test_move_module.old == "test_old"

    # Test the constructor with new
    test_move_module = MovedModule("test_name", "test_old", "test_new")
    assert test_move_module.name == "test_name"
    assert test_move_module.new == "test_new"
    assert test_move_module.old == "test_old"

    # Test auto naming
    test_move_module = MovedModule("test_name")
    assert test_move_module.name == "test_name"
    assert test

# Generated at 2022-06-14 02:15:41.574477
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert MovedAttribute('x', 'y', 'z').name == 'x'
    assert MovedAttribute('x', 'y', 'z').new_mod == 'z'
    assert MovedAttribute('x', 'y', 'z').new_attr == 'x'
    assert MovedAttribute('x', 'y', 'z', 'a', 'b').name == 'x'
    assert MovedAttribute('x', 'y', 'z', 'a', 'b').new_mod == 'z'
    assert MovedAttribute('x', 'y', 'z', 'a', 'b').new_attr == 'b'
    assert MovedAttribute('x', 'y', 'z', 'a').name == 'x'
    assert MovedAttribute('x', 'y', 'z', 'a').new_mod == 'z'
    assert MovedAttribute

# Generated at 2022-06-14 02:15:52.064139
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    transformer = SixMovesTransformer()

# Generated at 2022-06-14 02:15:53.180219
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert len(_get_rewrites()) > 0

# Generated at 2022-06-14 02:15:55.842143
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    transformer = SixMovesTransformer()
    assert transformer.rewrites == _get_rewrites()
    assert transformer.target == (2, 7)