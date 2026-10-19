

# Generated at 2022-06-14 02:06:08.063156
# Unit test for constructor of class MovedModule
def test_MovedModule():
    def check(name, old, new):
        mm = MovedModule(name, old, new)
        assert mm.name == name
        assert mm.old == old
        assert mm.new == new

    yield check, 'name', 'old', 'new'
    yield check, 'name', 'old', None


# Generated at 2022-06-14 02:06:17.652647
# Unit test for constructor of class MovedModule
def test_MovedModule():
    mm = MovedModule('test', 'Test', 'test')
    assert mm.new == 'test'
    assert mm.name == 'test'
    mm = MovedModule('test', 'Test')
    assert mm.new == 'test'
    assert mm.name == 'test'
    mm = MovedModule('test', 'Test', None)
    assert mm.new == 'test'
    assert mm.name == 'test'
    mm = MovedModule('test', 'Test', False)
    assert mm.new == 'test'
    assert mm.name == 'test'
    mm = MovedModule('test', 'Test', True)
    assert mm.new == 'Test'
    assert mm.name == 'test'
    mm = MovedModule('test', 'Test', 'True')
    assert mm.new == 'True'

# Generated at 2022-06-14 02:06:25.313283
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    # type: () -> None
    obj = MovedAttribute("moved", "old", "new", "old_attr", "new_attr")
    assert obj.name == "moved"
    assert obj.new_attr == "new_attr"
    assert obj.new_mod == "new"
    obj = MovedAttribute("moved", "old", "new")
    assert obj.new_attr == "moved"
    obj = MovedAttribute("moved", "old", "new", "old_attr")
    assert obj.new_attr == "old_attr"


# Generated at 2022-06-14 02:06:34.220447
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    exposed_name_in_code = '_moved_attributes'
    code_lines = '''foo bar {0} baz qux'''.format(exposed_name_in_code)
    mapping = {exposed_name_in_code: ['abc']}
    transformer = SixMovesTransformer(code_lines, mapping, create_remap_dict=True)
    assert transformer.code.splitlines() == ['foo bar abc baz qux']

# Generated at 2022-06-14 02:06:39.818660
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    move = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert move.name == 'cStringIO'
    assert move.new_mod == 'io'
    assert move.new_attr == 'StringIO'


# Generated at 2022-06-14 02:06:42.428207
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    m_a = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert hasattr(m_a, 'name')
    assert hasattr(m_a, 'new_mod')
    assert hasattr(m_a, 'new_attr')


# Generated at 2022-06-14 02:06:45.961426
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert _get_rewrites() == SixMovesTransformer.rewrites
    assert SixMovesTransformer.dependencies == ['six']
    assert SixMovesTransformer.target == (2, 7)

# Generated at 2022-06-14 02:06:49.386057
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    transformer = SixMovesTransformer()
    assert transformer.target == (2, 7)
    assert transformer.rewrites == _get_rewrites()
    assert transformer.dependencies == ['six']

# Generated at 2022-06-14 02:07:00.628383
# Unit test for constructor of class SixMovesTransformer

# Generated at 2022-06-14 02:07:09.667662
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    mov_att = MovedAttribute("name", "old_mod", "new_mod")
    assert mov_att.name == "name"
    assert mov_att.new_mod == "new_mod"
    assert mov_att.new_attr == "name"
    mov_att = MovedAttribute("name", "old_mod", "new_mod", "old_attr")
    assert mov_att.name == "name"
    assert mov_att.new_mod == "new_mod"
    assert mov_att.new_attr == "old_attr"
    mov_att = MovedAttribute("name", "old_mod", "new_mod", "old_attr", "new_attr")
    assert mov_att.name == "name"
    assert mov_att.new_mod == "new_mod"
    assert mov_

# Generated at 2022-06-14 02:07:23.121606
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    t = SixMovesTransformer()
    assert t.target == (2, 7)
    assert t.dependencies == ['six']
    # six.moves.urllib.parse.urlencode -> six.moves.urlencode
    assert t.rewrites['urllib.parse.urlencode'] == 'six.moves.urlencode'
    # six.moves.urllib.request.urlretrieve -> six.moves.urlretrieve
    assert t.rewrites['urllib.request.urlretrieve'] == 'six.moves.urlretrieve'
    # six.moves.urllib.error.URLError -> six.moves.URLError

# Generated at 2022-06-14 02:07:27.951924
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    stmt = parse('import urllib.request')
    transformer = SixMovesTransformer(stmt.body[0])
    assert transformer.should_process(stmt.body[0])
    assert transformer.rewrite() == 'six.moves.urllib.request'



# Generated at 2022-06-14 02:07:33.325394
# Unit test for constructor of class MovedModule
def test_MovedModule():
    moved_module = MovedModule('name', 'old', 'new')
    assert moved_module.name == 'name'
    assert moved_module.old == 'old'
    assert moved_module.new == 'new'
    moved_module = MovedModule('name', 'old')
    assert moved_module.new == 'name'

# Generated at 2022-06-14 02:07:40.193547
# Unit test for constructor of class MovedModule
def test_MovedModule():
    move1 = MovedModule('bugs', 'ants')
    assert move1.name == 'bugs'
    assert move1.new == 'bugs'
    move2 = MovedModule('bugs', 'ants', 'roaches')
    assert move2.new == 'roaches'
    move3 = MovedModule('bugs')
    assert move3.new == 'bugs'

# Generated at 2022-06-14 02:07:53.335125
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    from types import ModuleType

    move = MovedAttribute('name', 'old_mod', 'new_mod')
    assert move.name == 'name'
    assert move.new_attr is None
    assert move.new_mod == 'new_mod'

    move = MovedAttribute('name', 'old_mod', 'new_mod', 'old_attr')
    assert move.new_attr == 'old_attr'

    move = MovedAttribute('name', 'old_mod', 'new_mod', new_attr='new_attr')
    assert move.new_attr == 'new_attr'

    move = MovedAttribute('name', 'old_mod', None)
    assert move.name == 'name'
    assert move.new_attr is None
    assert move.new_mod == 'name'


# Generated at 2022-06-14 02:07:56.555585
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert next(SixMovesTransformer.rewrites) == ('builtins.cStringIO', 'six.moves.cStringIO')

# Generated at 2022-06-14 02:07:59.711162
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    transformer = SixMovesTransformer(None)
    assert transformer.rewrites == _get_rewrites()

# Generated at 2022-06-14 02:08:11.989721
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert MovedAttribute("cStringIO", "cStringIO", "io", "StringIO").name == 'cStringIO'
    assert MovedAttribute("cStringIO", "cStringIO", "io", "StringIO").new_mod == 'io'
    assert MovedAttribute("cStringIO", "cStringIO", "io", "StringIO").new_attr == 'StringIO'
    assert MovedAttribute("map", "itertools", "builtins", "imap", "map").new_attr == 'map'
    assert MovedAttribute("getcwd", "os", "os", "getcwdu", "getcwd").new_attr == 'getcwd'
    assert MovedAttribute("reload_module", "__builtin__", "imp", "reload").new_attr == 'reload'

# Generated at 2022-06-14 02:08:16.605926
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    MovedAttribute("name", "old_mod", "new_mod", "old_attr", "new_attr")
    MovedAttribute("name", "old_mod", "new_mod", "old_attr", None)
    MovedAttribute("name", "old_mod", "new_mod", None)
    MovedAttribute("name", "old_mod", "new_mod")
    MovedAttribute("name", "old_mod", None)


# Generated at 2022-06-14 02:08:22.250406
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    """Test function for constructor of class MovedAttribute."""
    assert MovedAttribute("cStringIO", "cStringIO", "io", "StringIO").new_mod == "io"
    assert MovedAttribute("cStringIO", "cStringIO", "io", "StringIO").new_attr == "StringIO"
    assert MovedAttribute("cStringIO", "cStringIO", "io", "StringIO").name == "cStringIO"
    assert MovedAttribute("cStringIO", "cStringIO", "io").new_mod == "io"
    assert MovedAttribute("cStringIO", "cStringIO", "io").new_attr == "cStringIO"
    assert MovedAttribute("cStringIO", "cStringIO", "io").name == "cStringIO"

# Generated at 2022-06-14 02:08:33.494616
# Unit test for constructor of class MovedModule
def test_MovedModule():
    assert MovedModule('name', 'old', 'new').name == 'name'
    assert MovedModule('name', 'old', 'new').old == 'old'
    assert MovedModule('name', 'old', 'new').new == 'new'
    assert MovedModule('builtins', '__builtin__').new == 'builtins'
    assert MovedModule('builtins', '__builtin__').old == '__builtin__'
    assert MovedModule('builtins', '__builtin__').name == 'builtins'

# Generated at 2022-06-14 02:08:36.549028
# Unit test for constructor of class MovedModule
def test_MovedModule():
    test = MovedModule("builtins", "__builtin__")
    assert test.name == "builtins"
    assert test.new == "builtins"



# Generated at 2022-06-14 02:08:40.200931
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    t = SixMovesTransformer('')
    assert isinstance(t, BaseImportRewrite)
    assert t.target == (2, 7)
    assert t.dependencies == ['six']
    assert len(t.rewrites) == 188
    assert isinstance(t.rewrites[0], tuple)

# Generated at 2022-06-14 02:08:48.525526
# Unit test for constructor of class MovedModule
def test_MovedModule():
    for name in ('configparser', 'configparser', 'dbm_gnu', 'http_cookiejar', 'http_cookies', 'tkinter'):
        assert name == MovedModule(name, '__' + name + '__').name
    assert 'a.b.c' == MovedModule('foo', 'a.b.c', 'a.b.d').new

# Generated at 2022-06-14 02:09:01.682676
# Unit test for constructor of class SixMovesTransformer

# Generated at 2022-06-14 02:09:06.584054
# Unit test for constructor of class MovedModule
def test_MovedModule():
    module = MovedModule('name', 'name')
    assert module.name == 'name'
    assert module.new == 'name'

    module = MovedModule('name', 'name', 'new')
    assert module.name == 'name'
    assert module.new == 'new'



# Generated at 2022-06-14 02:09:08.887445
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    t = SixMovesTransformer()
    for rw in t.rewrites:
        assert len(rw) == 2

# Generated at 2022-06-14 02:09:20.738790
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert str(MovedAttribute("name", "mod", "mod2", "attr", "attr2")) == "MovedAttribute('name', 'mod', 'mod2', 'attr', 'attr2')"
    assert str(MovedAttribute("name", "mod", "mod2", "attr", None)) == "MovedAttribute('name', 'mod', 'mod2', 'attr')"
    assert str(MovedAttribute("name", "mod", "mod2", None, "attr2")) == "MovedAttribute('name', 'mod', 'mod2', 'attr2')"
    assert str(MovedAttribute("name", "mod", "mod2", None, None)) == "MovedAttribute('name', 'mod', 'mod2')"

# Generated at 2022-06-14 02:09:31.813917
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert MovedAttribute("name", "old module", "new module", "old attribute", "new attribute").name == "name"
    assert MovedAttribute("name", "old module", "new module", "old attribute", "new attribute").new_mod == "new module"
    assert MovedAttribute("name", "old module", "new module", "old attribute", "new attribute").new_attr == "new attribute"
    assert MovedAttribute("name", "old module", "new module", "old attribute", "new attribute").old_mod == "old module"
    assert MovedAttribute("name", "old module", "new module", "old attribute", "new attribute").old_attr == "old attribute"


# Generated at 2022-06-14 02:09:33.552126
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert len(SixMovesTransformer.get_rewrites()) == 159

# Generated at 2022-06-14 02:09:46.144961
# Unit test for constructor of class MovedModule
def test_MovedModule():
    test = MovedModule("test", "test")
    assert test.name == "test"
    assert test.new == "test"
    test = MovedModule("test", "testold", "testnew")
    assert test.name == "test"
    assert test.new == "testnew"
    assert test.old == "testold"


if __name__ == '__main__':
    test_MovedModule()

# Generated at 2022-06-14 02:09:50.777010
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    st = SixMovesTransformer()
    assert st.dependencies == ['six']
    assert st.target == (2, 7)
    assert len(st.rewrites) == 82

# Generated at 2022-06-14 02:10:00.835414
# Unit test for constructor of class SixMovesTransformer

# Generated at 2022-06-14 02:10:03.629863
# Unit test for constructor of class MovedModule
def test_MovedModule():
    mm = MovedModule("name", "old", "new")

    assert(mm.name == "name")
    assert(mm.new == "new")

# Generated at 2022-06-14 02:10:12.457381
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert MovedAttribute('test_name', 'test_old_mod', 'test_new_mod').name == 'test_name'
    assert MovedAttribute('test_name', 'test_old_mod', 'test_new_mod').new_mod == 'test_new_mod'
    assert MovedAttribute('test_name', 'test_old_mod', 'test_new_mod').new_attr == 'test_name'
    assert MovedAttribute('test_name', 'test_old_mod', 'test_new_mod', 'test_old_attr', 'test_new_attr').new_attr == 'test_new_attr'

# Generated at 2022-06-14 02:10:16.013392
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    t = SixMovesTransformer('')
    assert len(t.rewrites) > 0

import_transforms = {
    (2, 7): [SixMovesTransformer],
}

# Generated at 2022-06-14 02:10:19.640149
# Unit test for constructor of class MovedModule
def test_MovedModule():
    for prefix, moves in prefixed_moves:
        for move in moves:
            if isinstance(move, MovedModule):
                mm = MovedModule(move.name, move.old, move.new)

# Generated at 2022-06-14 02:10:21.455619
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    SixMovesTransformer()

# Generated at 2022-06-14 02:10:30.317205
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    with pytest.raises(TypeError):
        _ = MovedAttribute("name", "old_mod")

    with pytest.raises(TypeError):
        _ = MovedAttribute("name", "old_mod", "new_mod", "old_attr")

    assert MovedAttribute("name", "old_mod", "new_mod", "old_attr", "new_attr") == \
        MovedAttribute("name", "old_mod", "new_mod", "old_attr", "new_attr")

    assert MovedAttribute("name", "old_mod", "new_mod", old_attr="old_attr") == \
        MovedAttribute("name", "old_mod", "new_mod", old_attr="old_attr")


# Generated at 2022-06-14 02:10:34.483222
# Unit test for constructor of class MovedModule
def test_MovedModule():
    moved_module = MovedModule("queue", "Queue")
    assert moved_module.name == "queue"
    assert moved_module.new == "queue"
    assert moved_module.old == "Queue"

# Generated at 2022-06-14 02:11:00.394679
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    moved_attribute = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert moved_attribute.name == "cStringIO"
    assert moved_attribute.new_mod == "io"
    assert moved_attribute.new_attr == "StringIO"

    moved_attribute = MovedAttribute("cStringIO", "cStringIO", "io")
    assert moved_attribute.name == "cStringIO"
    assert moved_attribute.new_mod == "io"
    assert moved_attribute.new_attr == "cStringIO"

    moved_attribute = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO", "StringIO2")
    assert moved_attribute.name == "cStringIO"
    assert moved_attribute.new_mod == "io"
    assert moved_attribute

# Generated at 2022-06-14 02:11:04.692405
# Unit test for constructor of class MovedModule
def test_MovedModule():
    assert MovedModule('name', 'old').name == 'name'
    assert MovedModule('name', 'old').old == 'old'
    assert MovedModule('name', 'old').new == 'name'
    assert MovedModule('name', 'old', 'new').name == 'name'
    assert MovedModule('name', 'old', 'new').old == 'old'
    assert MovedModule('name', 'old', 'new').new == 'new'

# Generated at 2022-06-14 02:11:17.739989
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    move = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert move.name == "cStringIO"
    assert move.new_mod == "io"
    assert move.new_attr == "StringIO"

    move = MovedAttribute("filter", "itertools", "builtins", "ifilter", "filter")
    assert move.name == "filter"
    assert move.new_mod == "builtins"
    assert move.new_attr == "filter"

    move = MovedAttribute("input", "__builtin__", "builtins", "raw_input", "input")
    assert move.name == "input"
    assert move.new_mod == "builtins"
    assert move.new_attr == "input"


# Generated at 2022-06-14 02:11:20.590132
# Unit test for constructor of class MovedModule
def test_MovedModule():
    m = MovedModule("name", "old", "new")

    assert(m.name == "name")
    assert(m.old == "old")
    assert(m.new == "new")


# Generated at 2022-06-14 02:11:29.295943
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert MovedAttribute("cStringIO", "cStringIO", "io", "StringIO") == MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    with pytest.raises(AssertionError):
        assert MovedAttribute("a", "b", "b", "d") == MovedAttribute("c", "c", "e", "e")
        assert MovedAttribute("a", "b", "b", "d") == MovedAttribute("a", "b", "b", "e")

# Generated at 2022-06-14 02:11:39.974907
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    from .test_pgen2 import ParseError
    from lib2to3.pgen2 import token
    import lib2to3.fixer_util as fixer_util

    transformer = SixMovesTransformer(None, None)

    # Test case:
    # from six.moves.urllib.parse import urlparse
    #   ->
    # from six.moves.urllib.parse import urlparse
    parse_node = parser.suite("from six.moves.urllib.parse import urlparse").children[0]
    transformer.visit_import(parse_node)

    # Test case:
    # import six.moves.urllib.parse
    #   ->
    # import six.moves.urllib.parse

# Generated at 2022-06-14 02:11:47.213920
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert all(name in SixMovesTransformer.rewrites for name in [
        'range', 'zip_longest', 'urllib.parse.quote',
        'urllib.error.HTTPError', 'urllib.request.urlsplit'])
    assert 'StringIO' not in SixMovesTransformer.rewrites
    assert 'urllib.parse.error' not in SixMovesTransformer.rewrites

# Generated at 2022-06-14 02:11:52.652230
# Unit test for constructor of class MovedModule
def test_MovedModule():
    mod = MovedModule("tkinter", "Tkinter")
    assert mod.name == "tkinter"
    assert mod.new == "tkinter"

    mod = MovedModule("tkinter", "Tkinter", "foo.tkinter")
    assert mod.name == "tkinter"
    assert mod.new == "foo.tkinter"


# Generated at 2022-06-14 02:11:56.703421
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    transformer = SixMovesTransformer()
    assert transformer.rewrites[0] == ('configparser.ConfigParser', 'six.moves.configparser')
    assert transformer.rewrites[5] == ('urllib.robotparser.RobotFileParser', 'six.moves.urllib.robotparser.RobotFileParser')

# Generated at 2022-06-14 02:12:01.976791
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    mv = SixMovesTransformer()

# Generated at 2022-06-14 02:12:38.657422
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    # First case
    a = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert a.name == "cStringIO"
    assert a.new_mod == "io"
    assert a.new_attr == "StringIO"

    # Second case
    c = MovedAttribute("filter", "itertools", "builtins", "ifilter", "filter")
    assert c.name == "filter"
    assert c.new_mod == "builtins"
    assert c.new_attr == "filter"

    # Third case
    d = MovedAttribute("getcwd", "os", "os", "getcwdu", "getcwd")
    assert d.name == "getcwd"
    assert d.new_mod == "os"

# Generated at 2022-06-14 02:12:43.115284
# Unit test for constructor of class MovedModule
def test_MovedModule():
    class MovedModule_test(unittest.TestCase):
        def test_1(self):
            MMT = MovedModule('test', 'oldtest')
            self.assertEqual(MMT.name, 'test')
            self.assertEqual(MMT.new, 'test')
    unittest.main()


# Generated at 2022-06-14 02:12:55.144435
# Unit test for constructor of class MovedModule
def test_MovedModule():
    m = MovedModule('tkinter', 'Tkinter')
    assert m.name == 'tkinter'
    assert m.new == 'tkinter'
    assert m.old == 'Tkinter'
    m = MovedModule('tkinter', 'Tkinter', 'tkinter')
    assert m.name == 'tkinter'
    assert m.new == 'tkinter'
    assert m.old == 'Tkinter'
    m = MovedModule('tkinter', 'Tkinter', 'tk')
    assert m.name == 'tkinter'
    assert m.new == 'tk'
    assert m.old == 'Tkinter'
    try:
        m = MovedModule('tkinter', 'Tkinter', None)
        raise AssertionError
    except TypeError as e:
        assert str(e)

# Generated at 2022-06-14 02:12:58.905976
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    a = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert a.name == "cStringIO"
    assert a.new_mod == "io"
    assert a.new_attr == "StringIO"

# Generated at 2022-06-14 02:12:59.662714
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    SixMovesTransformer()

# Generated at 2022-06-14 02:13:08.680770
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    m = MovedAttribute("a", "b", "c", "d")
    assert m.name == "a"
    assert m.new_mod == "b"
    assert m.new_attr == "d"
    m = MovedAttribute("a", "b", "c")
    assert m.new_attr == "a"
    m = MovedAttribute("a", "b", "c", "d", "e")
    assert m.new_attr == "e"


# Generated at 2022-06-14 02:13:12.894749
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    ma = MovedAttribute('name', 'old_mod', 'new_mod', 'old_attr', 'new_attr')
    assert ma.name == 'name'
    assert ma.new_mod == 'new_mod'
    assert ma.new_attr == 'new_attr'

# Generated at 2022-06-14 02:13:25.697880
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    import six
    import six.moves
    import six.moves.urllib
    assert six.moves.urllib.parse.quote('abc') == 'abc'
    assert six.moves.urllib.parse.quote_plus('abc') == 'abc'
    assert six.moves.urllib.parse.unquote('abc') == 'abc'
    assert six.moves.urllib.parse.unquote_plus('abc') == 'abc'
    assert six.moves.urllib.parse.unquote_to_bytes('abc') == b'abc'
    assert six.moves.urllib.parse.urlencode({'abc': 'abc'}) == 'abc=abc'
    assert six.moves.urllib.parse.splitquery('abc') == ('abc', '')

# Generated at 2022-06-14 02:13:29.790873
# Unit test for constructor of class MovedModule
def test_MovedModule():
    for prefix, moves in prefixed_moves:
        for move in moves:
            if isinstance(move, MovedModule):
                assert move.new == ('six.moves{}.{}'.format(prefix, move.name))


# Generated at 2022-06-14 02:13:33.726408
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    pass

if __name__ == '__main__':
    test_SixMovesTransformer()

# Generated at 2022-06-14 02:14:33.267470
# Unit test for constructor of class MovedModule
def test_MovedModule():
    move = MovedModule('new', 'old')
    assert move.new == 'new'
    assert move.name == 'new'
    assert move.old is None


# Generated at 2022-06-14 02:14:36.175857
# Unit test for constructor of class MovedModule
def test_MovedModule():
    moved_test = MovedModule("name", "old_name" )
    assert moved_test.name == "name"
    assert moved_test.new == "name"
    assert moved_test.old == "old_name"

# Generated at 2022-06-14 02:14:38.190260
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert len(SixMovesTransformer.rewrites) == 33

# Generated at 2022-06-14 02:14:39.787314
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    result = SixMovesTransformer.rewrites

# Generated at 2022-06-14 02:14:50.827724
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    test_cases = [
        ("reload_module", "__builtin__", "imp", "reload", "reload_module"),
        ("reload_module", "__builtin__", "importlib", "reload", "reload_module"),
        ("xrange", "__builtin__", "builtins", "xrange", "range"),
        ("zip", "itertools", "builtins", "izip", "zip"),
        ("zip_longest", "itertools", "itertools", "izip_longest", "zip_longest"),
    ]
    for name, old_mod, new_mod, old_attr, new_attr in test_cases:
        move = MovedAttribute(name, old_mod, new_mod, old_attr, new_attr)
        assert move.name == name


# Generated at 2022-06-14 02:15:04.157622
# Unit test for constructor of class SixMovesTransformer

# Generated at 2022-06-14 02:15:12.237616
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    from ..testing.load_tests import Loader
    from ..testing import runner
    import sys
    import six

    test_dir = os.path.dirname(__file__)
    loader = Loader(sys.path, parallel=False)
    loaded = loader.discover(test_dir, pattern="test_*.py")
    suite = runner.get_suite(loader, loaded)
    result = runner.run_suite(suite)
    if not result.wasSuccessful():
        raise ValueError('SixMovesTransformer constructor is broken')

# Generated at 2022-06-14 02:15:13.819967
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    transformer = SixMovesTransformer()
    assert len(transformer.rewrites) > 0

# Generated at 2022-06-14 02:15:24.985619
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    attrib = MovedAttribute("filter", "itertools", "builtins", "ifilter", "filter")
    assert attrib.name == 'filter'
    assert attrib.new_mod == 'builtins'
    assert attrib.new_attr == 'filter'
    attrib = MovedAttribute("map", "itertools", "builtins", "imap", None)
    assert attrib.new_attr == 'map'
    attrib = MovedAttribute("getcwdb", "os", "os", "getcwd", None)
    assert attrib.new_attr == 'getcwdb'
    attrib = MovedAttribute("range", "__builtin__", "builtins", "xrange", "range")
    assert attrib.new_attr == 'range'


# Generated at 2022-06-14 02:15:30.709364
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    attribute = MovedAttribute('cStringIO', 'cStringIO', 'io', 'StringIO')
    assert attribute.name == 'cStringIO'
    assert attribute.new_mod == 'io'
    assert attribute.new_attr == 'StringIO'
