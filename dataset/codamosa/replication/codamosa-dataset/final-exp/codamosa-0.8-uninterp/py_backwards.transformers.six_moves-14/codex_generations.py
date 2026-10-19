

# Generated at 2022-06-14 02:06:05.781774
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert "six.moves.urllib_parse" not in SixMovesTransformer().rewrites
    assert "six.moves.urllib_error" not in SixMovesTransformer().rewrites
    assert "six.moves.urllib" not in SixMovesTransformer().rewrites
    assert "six.moves.urllib.parse" in SixMovesTransformer().rewrites
    assert "six.moves.urllib.error" in SixMovesTransformer().rewrites
    assert "six.moves.urllib.request" in SixMovesTransformer().rewrites
    assert "six.moves.urllib.response" in SixMovesTransformer().rewrites
    assert "six.moves.urllib.robotparser" in SixMovesTransformer().rewrites

# Generated at 2022-06-14 02:06:15.713454
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    transformer = SixMovesTransformer()
    assert transformer.targets == {(2, 7)}
    assert transformer.dependencies == ['six']

# Generated at 2022-06-14 02:06:25.426221
# Unit test for constructor of class MovedModule
def test_MovedModule():
    # Test for first 2.7 moved module
    first_moved_module = MovedModule("builtins", "__builtin__")
    assert first_moved_module.name == "builtins"
    assert first_moved_module.new == "builtins"
    # Test for last 2.7 moved module
    last_moved_module = MovedModule("tkinter", "Tkinter")
    assert last_moved_module.name == "tkinter"
    assert last_moved_module.new == "tkinter"
    # Test for first 3 moved module
    fm_moved_module = MovedModule("urllib_robotparser", "robotparser", "urllib.robotparser")
    assert fm_moved_module.name == "urllib_robotparser"
    assert f

# Generated at 2022-06-14 02:06:36.240195
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    from . import base
    import astor
    class DummyNode(ast.AST):
        def __init__(self, value):
            self.value = value
    node = DummyNode(1)
    node2 = DummyNode(2)
    dummy_rewrites = {('a.b', 'c.d'): node,
                      ('e.f', 'g.h'): node2}
    smt = SixMovesTransformer(name='SixMovesTransformer',
                              dependencies=['six'],
                              rewrites=dummy_rewrites)
    smt.version = None
    smt.node = node
    smt.log = True
    smt.visitor = base.HelperTransformer()
    smt.visit(node)
    assert smt.visitor.counter == 5


# Generated at 2022-06-14 02:06:39.481988
# Unit test for constructor of class MovedModule
def test_MovedModule():
    arg = 'test'
    expected = 'test'
    actual = MovedModule(arg, arg).new
    assert actual == expected, 'Test failed'

# Generated at 2022-06-14 02:06:42.046368
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert len(list(SixMovesTransformer.rewrites)) == 142

# Test to check that we get the correct number of rewrites added

# Generated at 2022-06-14 02:06:45.961817
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    move = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert move.name == "cStringIO"
    assert move.new_mod == "io"
    assert move.new_attr == "StringIO"

# Generated at 2022-06-14 02:06:48.949490
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    rewrites = dict(_get_rewrites())
    assert len(rewrites) > 0
    assert SixMovesTransformer.rewrites == rewrites

# Generated at 2022-06-14 02:06:52.661613
# Unit test for constructor of class MovedModule
def test_MovedModule():
    assert MovedModule("name", "old").name == "name"
    assert MovedModule("name", "old").new == "name"
    assert MovedModule("name", "old", "new").new == "new"

# Generated at 2022-06-14 02:06:56.224441
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert 'six.moves' in SixMovesTransformer.rewrites[0][1]

# Generated at 2022-06-14 02:07:03.765240
# Unit test for constructor of class MovedModule
def test_MovedModule():
    assert MovedModule("builtins", "__builtin__").name == "builtins"
    assert MovedModule("builtins", "__builtin__").new == "builtins"
    assert MovedModule("configparser", "ConfigParser").name == "configparser"
    assert MovedModule("configparser", "ConfigParser").new == "configparser"


# Generated at 2022-06-14 02:07:06.422503
# Unit test for constructor of class MovedModule
def test_MovedModule():
    test = MovedModule("TestModule", "Test")
    assert test.name == "TestModule"
    assert test.old == "Test"
    assert test.new == "TestModule"



# Generated at 2022-06-14 02:07:20.401233
# Unit test for constructor of class SixMovesTransformer

# Generated at 2022-06-14 02:07:24.267753
# Unit test for constructor of class MovedModule
def test_MovedModule():
    m = MovedModule("name", "old")
    assert m.name == "name"
    assert m.old == "old"
    assert m.new == "name"

# Generated at 2022-06-14 02:07:27.361779
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert MovedAttribute("cStringIO", "cStringIO", "io")

# Generated at 2022-06-14 02:07:31.275528
# Unit test for constructor of class MovedModule
def test_MovedModule():
    moved = MovedModule("string", "str", "str")
    assert moved.name == "string"
    assert moved.old == "str"
    assert moved.new == "str"


# Unit tests for the constructor of class MovedAttribute

# Generated at 2022-06-14 02:07:33.381876
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    item = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert ite

# Generated at 2022-06-14 02:07:35.340763
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    print(SixMovesTransformer.rewrites)
    assert len(SixMovesTransformer.rewrites) == 753

# Generated at 2022-06-14 02:07:46.266529
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    ma = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert ma.name == "cStringIO"
    assert ma.new_mod == "io"
    assert ma.new_attr == "StringIO"

    ma = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO", "cStringIO")
    assert ma.name == "cStringIO"
    assert ma.new_mod == "io"
    assert ma.new_attr == "cStringIO"

    ma = MovedAttribute("cStringIO", "cStringIO", "io")
    assert ma.name == "cStringIO"
    assert ma.new_mod == "io"
    assert ma.new_attr == "cStringIO"


# Generated at 2022-06-14 02:07:56.211816
# Unit test for constructor of class MovedModule
def test_MovedModule():
    module1 = MovedModule(name=None, old=None, new=None)
    module2 = MovedModule(name=None, old=None)
    module3 = MovedModule(name=None, new=None)
    module4 = MovedModule(name="test", old="a", new="b")
    assert module1.name is None
    assert module1.old is None
    assert module1.new is None
    assert module2.name is None
    assert module2.old is None
    assert module2.new is None
    assert module3.name is None
    assert module3.old is None
    assert module3.new is None
    assert module4.name == "test"
    assert module4.old == "a"
    assert module4.new == "b"
    assert module4.name == module4

# Generated at 2022-06-14 02:08:01.459971
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert 1==1

# Generated at 2022-06-14 02:08:04.977584
# Unit test for constructor of class MovedModule
def test_MovedModule():
    s = MovedModule('a', 'b', 'c')
    assert s.name == 'a'
    assert s.new == 'c'
    assert s.old == 'b'

# Generated at 2022-06-14 02:08:06.620208
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    from import_rewrite import SixMovesTransformer
    assert len(SixMovesTransformer.rewrites) == 90

# Generated at 2022-06-14 02:08:11.706801
# Unit test for constructor of class MovedModule
def test_MovedModule():
    import pytest
    mm = MovedModule("name", "old", "new")
    assert mm.name == "name"
    assert mm.new == "new"
    with pytest.raises(AttributeError):
        mm.name = "name2"
    with pytest.raises(AttributeError):
        mm.new = "new2"
    with pytest.raises(AttributeError):
        mm.other = "other"


# Generated at 2022-06-14 02:08:16.677958
# Unit test for constructor of class MovedModule
def test_MovedModule():
    movedModule1 = MovedModule('foo', 'bar')
    assert movedModule1.name == 'foo'
    assert movedModule1.old == 'bar'
    assert movedModule1.new == 'foo'

    movedModule2 = MovedModule('foo', 'bar', 'baz')
    assert movedModule2.name == 'foo'
    assert movedModule2.old == 'bar'
    assert movedModule2.new == 'baz'


# Unit tests for class MovedAttribute

# Generated at 2022-06-14 02:08:17.801538
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert SixMovesTransformer.rewrites == _get_rewrites()

# Generated at 2022-06-14 02:08:24.094892
# Unit test for constructor of class MovedModule
def test_MovedModule():
    obj = MovedModule("name", "old")
    assert obj.name == 'name'
    assert obj.new == 'name'
    assert not hasattr(obj, 'old')
    obj = MovedModule("name", "old", "new")
    assert obj.name == 'name'
    assert obj.new == 'new'
    obj = MovedModule(name="name", old="old")
    assert obj.name == 'name'
    assert obj.new == 'name'
    assert not hasattr(obj, 'old')
    obj = MovedModule(name="name", old="old", new="new")
    assert obj.name == 'name'
    assert obj.new == 'new'

# Generated at 2022-06-14 02:08:25.201937
# Unit test for constructor of class MovedModule
def test_MovedModule():
    assert False, "TODO"

# Generated at 2022-06-14 02:08:28.215936
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    transformer = SixMovesTransformer()
    assert transformer.rewrites == _get_rewrites()
    assert transformer.dependencies == ['six']

# Generated at 2022-06-14 02:08:38.622499
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    st = SixMovesTransformer()
    assert st.target == (2, 7)

# Generated at 2022-06-14 02:08:55.865043
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    attr = MovedAttribute('rStringIO', 'rStringIO', 'rstringio')
    assert attr.name == 'rStringIO'
    assert attr.new_mod == 'rstringio'
    assert attr.new_attr == 'rStringIO'

    attr = MovedAttribute('rStringIO', 'rStringIO', 'rstringio',
                          'StringIO', 'StringIO')
    assert attr.name == 'rStringIO'
    assert attr.new_mod == 'rstringio'
    assert attr.new_attr == 'StringIO'


# Generated at 2022-06-14 02:08:59.140627
# Unit test for constructor of class MovedModule
def test_MovedModule():
    mm = MovedModule("name", "old")
    assert mm.name == "name"
    assert mm.old == "old"
    assert mm.new == "name"


# Generated at 2022-06-14 02:09:05.717585
# Unit test for constructor of class MovedModule
def test_MovedModule():
    # type: () -> None
    mod = MovedModule("name", "old")
    assert mod.name == "name"
    assert mod.new == "name"
    assert mod.old == "old"

    mod = MovedModule("name", "old", "new")
    assert mod.name == "name"
    assert mod.new == "new"
    assert mod.old == "old"

# Generated at 2022-06-14 02:09:11.578082
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    a = MovedAttribute('a', 'b', 'c')
    assert a.name == 'a'
    assert a.new_mod == 'c'
    assert a.new_attr == 'a'

    a = MovedAttribute('a', 'b', 'c', 'd', 'e')
    assert a.name == 'a'
    assert a.new_mod == 'c'
    assert a.new_attr == 'e'


# Generated at 2022-06-14 02:09:19.088438
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    MOVED_ATTRIBUTES = [
        MovedAttribute("cStringIO", "cStringIO", "io", "StringIO"),
        MovedAttribute("filter", "itertools", "builtins", "ifilter", "filter"),
        MovedAttribute("filterfalse", "itertools", "itertools", "ifilterfalse", "filterfalse")
    ]

    for i in MOVED_ATTRIBUTES:
        assert i.name == i.new_attr

# Generated at 2022-06-14 02:09:32.135931
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    moved = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert moved.name == "cStringIO"
    assert moved.new_mod == "io"
    assert moved.new_attr == "StringIO"

    moved = MovedAttribute("cStringIO", "cStringIO", "io")
    assert moved.name == "cStringIO"
    assert moved.new_mod == "io"
    assert moved.new_attr == "StringIO"

    moved = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO", "replaced")
    assert moved.name == "cStringIO"
    assert moved.new_mod == "io"
    assert moved.new_attr == "replaced"


# Generated at 2022-06-14 02:09:37.325151
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    move = MovedAttribute('name', 'old', 'new')
    assert move.name == 'name'
    assert move.old_mod is None
    assert move.new_mod == 'new'
    assert move.old_attr is None
    assert move.new_attr == 'name'


# Generated at 2022-06-14 02:09:40.203333
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    import ast
    # There are 18 moves of modules and 82 moves of attributes
    expected_rewrites = 100

    # Test that constructor of class SixMovesTransformer
    # generates expected number of rewrites
    # Do not use assertEqual directly because this gives
    # too verbose output on error
    SixMovesTransformer()
    assert len(SixMovesTransformer.rewrites) == expected_rewrites

# Generated at 2022-06-14 02:09:45.082806
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    class_instance = SixMovesTransformer(None, None, None)
    assert isinstance(class_instance, BaseImportRewrite)
    assert class_instance.target == (2, 7)
    assert class_instance.rewrites == _get_rewrites()
    assert class_instance.dependencies == ['six']

# Generated at 2022-06-14 02:09:53.863666
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert MovedAttribute("cStringIO", "cStringIO", "io", "StringIO").name == "cStringIO"
    assert MovedAttribute("cStringIO", "cStringIO", "io", "StringIO").new_mod == "io"
    assert MovedAttribute("cStringIO", "cStringIO", "io", "StringIO").new_attr == "StringIO"
    assert MovedAttribute("cStringIO", "cStringIO", "io", "StringIO").old_attr == "StringIO"
    assert MovedAttribute("cStringIO", "cStringIO", "io").name == "cStringIO"
    assert MovedAttribute("cStringIO", "cStringIO", "io").new_mod == "io"

# Generated at 2022-06-14 02:10:08.620390
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    transformer = SixMovesTransformer()
    for rewrite in transformer.rewrites:
        assert rewrite[0].startswith('six.moves')

# Generated at 2022-06-14 02:10:11.971962
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    t = SixMovesTransformer()
    assert t.target == (2, 7)
    assert t.rewrites
    assert t.dependencies



# Generated at 2022-06-14 02:10:15.212878
# Unit test for constructor of class MovedModule
def test_MovedModule():
    cm = MovedModule('a', 'b', 'c')
    assert cm.name == 'a'
    assert cm.new == 'c'

# Generated at 2022-06-14 02:10:19.873194
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert len(_get_rewrites()) > 0
    # Do this to ensure that the eager decorator was applied
    assert len(_SixMovesTransformer__idx_to_rewrites0) > 0
    assert len(_SixMovesTransformer__idx_to_rewrites1) > 0

# Generated at 2022-06-14 02:10:29.227906
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    a = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert a.name == "cStringIO"
    assert a.new_mod == "io"
    assert a.new_attr == "StringIO"
    b = MovedAttribute("filter", "itertools", "builtins")
    assert b.name == "filter"
    assert b.new_mod == "builtins"
    assert b.new_attr == "filter"
    c = MovedAttribute("filter", "itertools", "builtins", "ifilter", "filter")
    assert c.name == "filter"
    assert c.new_mod == "builtins"
    assert c.new_attr == "filter"

# Generated at 2022-06-14 02:10:36.219359
# Unit test for constructor of class MovedModule
def test_MovedModule():
    mm = MovedModule('x', 'y')
    assert mm.name == 'x'
    assert mm.old == 'y'
    assert mm.new == 'x'

    mm = MovedModule('x', 'y', 'z')
    assert mm.name == 'x'
    assert mm.old == 'y'
    assert mm.new == 'z'



# Generated at 2022-06-14 02:10:39.325428
# Unit test for constructor of class MovedModule
def test_MovedModule():
    mm = MovedModule('foo', 'bar')
    assert mm.name == 'foo'
    assert mm.new == 'bar'

# Generated at 2022-06-14 02:10:48.781775
# Unit test for constructor of class MovedModule
def test_MovedModule():
    assert MovedModule("a", "b", "c") == MovedModule("a", "b", "c")
    assert MovedModule("a", "b", "c") != MovedModule("a", "b", "d")
    assert MovedModule("a", "b", "c") != MovedModule("b", "b", "c")
    assert MovedModule("a", "b", "c") != MovedModule("d", "b", "c")
    assert MovedModule("a", "b", "a") == MovedModule("a", "b")
    assert MovedModule("a", "a", "c") == MovedModule("a", "a", "c")
    assert hash(MovedModule("a", "b", "c")) == hash(MovedModule("a", "b", "c"))

# Generated at 2022-06-14 02:10:55.455963
# Unit test for constructor of class MovedModule
def test_MovedModule():
    move1 = MovedModule("CGIHTTPServer", "CGIHTTPServer", "http.server")
    move2 = MovedModule("configparser", "ConfigParser")
    assert move1.name == "CGIHTTPServer"
    assert move1.new == "http.server"
    assert move2.name == "configparser"
    assert move2.new == "configparser"
    assert move2.old == "ConfigParser"

# Generated at 2022-06-14 02:11:02.257272
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    ma = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert ma.__dict__ == {
        'name': 'cStringIO',
        'old_mod': 'cStringIO',
        'new_mod': 'io',
        'old_attr': 'StringIO',
        'new_attr': 'StringIO',
    }


# Generated at 2022-06-14 02:11:35.526324
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    moved_attribute = MovedAttribute('name', 'old', 'new')
    assert moved_attribute.name == 'name'
    assert moved_attribute.old_mod == None
    assert moved_attribute.new_mod == 'new'
    assert moved_attribute.old_attr == None
    assert moved_attribute.new_attr == 'name'

    moved_attribute = MovedAttribute('name', 'old', 'new', 'old_attr')
    assert moved_attribute.name == 'name'
    assert moved_attribute.old_mod == None
    assert moved_attribute.new_mod == 'new'
    assert moved_attribute.old_attr == 'old_attr'
    assert moved_attribute.new_attr == 'old_attr'

# Generated at 2022-06-14 02:11:45.477283
# Unit test for constructor of class MovedAttribute

# Generated at 2022-06-14 02:11:56.418560
# Unit test for constructor of class MovedModule
def test_MovedModule():
    m1 = MovedModule("builtins", "__builtin__")
    m2 = MovedModule("queue", "Queue")
    m3 = MovedModule("queue", "Queue", "queue")
    m4 = MovedModule("tkinter", "Tkinter")
    assert m1.name == "builtins"
    assert m1.old == "__builtin__"
    assert m1.new == "builtins"
    assert m2.name == "queue"
    assert m2.old == "Queue"
    assert m2.new == "queue"
    assert m3.name == "queue"
    assert m3.old == "Queue"
    assert m3.new == "queue"
    assert m4.name == "tkinter"
    assert m4.old == "Tkinter"
    assert m4

# Generated at 2022-06-14 02:11:59.761802
# Unit test for constructor of class MovedModule
def test_MovedModule():
    moved_module = MovedModule("queue", "Queue")
    assert moved_module.name == "Queue"
    assert moved_module.new == "queue"


# Generated at 2022-06-14 02:12:10.947763
# Unit test for constructor of class MovedModule
def test_MovedModule():
    module = MovedModule("AA", "BB", "CC")
    assert module.name == "AA"
    assert module.old == "BB"
    assert module.new == "CC"

    module = MovedModule("AA", "BB")
    assert module.name == "AA"
    assert module.old == "BB"

    # Test error handling
    try:
        MovedModule()
    except TypeError:
        pass
    else:
        assert False

    try:
        MovedModule(1)
    except TypeError:
        pass
    else:
        assert False

    try:
        MovedModule(1, 2, 3, 4)
    except TypeError:
        pass
    else:
        assert False


# Generated at 2022-06-14 02:12:13.582137
# Unit test for constructor of class MovedModule
def test_MovedModule():
    import_ = MovedModule("builtins", "__builtin__")
    assert import_.name == 'builtins'
    assert import_.new == 'builtins'



# Generated at 2022-06-14 02:12:18.166262
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    ma = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO", "StringIO")
    assert ma.name == "cStringIO"
    assert ma.new_mod == "io"
    assert ma.new_attr == "StringIO"


# Generated at 2022-06-14 02:12:22.526615
# Unit test for constructor of class MovedModule
def test_MovedModule():
    x = MovedModule("Modulename", "Oldname")
    assert x.name == "Modulename"
    assert x.new == "Oldname"
    x = MovedModule("Modulename", "Oldname", "Newname")
    assert x.name == "Modulename"
    assert x.new == "Newname"

# Generated at 2022-06-14 02:12:29.274006
# Unit test for constructor of class MovedModule
def test_MovedModule():
    # Test no input
    m = MovedModule("func", "func")
    assert m.name == "func"
    assert m.new == "func"

    # Test with input module name
    m = MovedModule("func", "func", "new_func")
    assert m.name == "func"
    assert m.new == "new_func"


# Generated at 2022-06-14 02:12:39.919573
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    move = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert move.new_mod == 'io'
    assert move.new_attr == 'StringIO'

    move = MovedAttribute("range", "__builtin__", "builtins", "xrange", "range")
    assert move.new_mod == 'builtins'
    assert move.new_attr == 'range'

    move = MovedAttribute("map", "itertools", "builtins", "imap", "map")
    assert move.new_mod == 'builtins'
    assert move.new_attr == 'map'



# Generated at 2022-06-14 02:13:34.890847
# Unit test for constructor of class MovedModule
def test_MovedModule():
    assert MovedModule("name", "old", "new") == MovedModule("name", "old", "new")
    assert MovedModule("name", "old", "new") != MovedModule("nam", "old", "new")
    assert MovedModule("name", "old", "new") != MovedModule("name", "ol", "new")
    assert MovedModule("name", "old", "new") != MovedModule("name", "old", "ne")
    assert str(MovedModule("name", "old", "new")) == "MovedModule(name, old, new)"


# Generated at 2022-06-14 02:13:38.474149
# Unit test for constructor of class MovedModule
def test_MovedModule():
    moved_module = MovedModule("foo", "bar", "baz")
    assert moved_module.name == "foo"
    assert moved_module.old == "bar"
    assert moved_module.new == "baz"

# Generated at 2022-06-14 02:13:44.601066
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    move = MovedAttribute('foo', 'oldmod', 'newmod', 'oldattr', 'newattr')
    assert move.name == 'foo'
    assert move.new_mod == 'newmod'
    assert move.new_attr == 'newattr'
    move = MovedAttribute('foo', 'oldmod', 'newmod', 'oldattr')
    assert move.name == 'foo'
    assert move.new_mod == 'newmod'
    assert move.new_attr == 'oldattr'
    move = MovedAttribute('foo', 'oldmod', 'newmod')
    assert move.name == 'foo'
    assert move.new_mod == 'newmod'
    assert move.new_attr == 'foo'

# Generated at 2022-06-14 02:13:47.716274
# Unit test for constructor of class MovedModule
def test_MovedModule():
    obj = MovedModule('name', 'old', 'new')
    assert (obj.name == 'name')
    assert (obj.old == 'old')
    assert (obj.new == 'new')

# Generated at 2022-06-14 02:13:51.161614
# Unit test for constructor of class MovedModule
def test_MovedModule():
    module = MovedModule("tokenize", "tokenize", "token")
    assert module.name == "tokenize"
    assert module.old == "tokenize"
    assert module.new == "token"



# Generated at 2022-06-14 02:13:55.332689
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert MovedAttribute("cStringIO", "cStringIO", "io", "StringIO").new_attr == "StringIO"
    assert MovedAttribute("cStringIO", "cStringIO", "io", "StringIO").new_mod == "io"


# Generated at 2022-06-14 02:13:59.054007
# Unit test for constructor of class MovedModule
def test_MovedModule():
    test_obj = MovedModule("test", "oldtest")
    assert test_obj.name == "test"
    assert test_obj.old == "oldtest"
    assert test_obj.new == "test"

# Generated at 2022-06-14 02:14:01.683192
# Unit test for constructor of class MovedModule
def test_MovedModule():
    mm = MovedModule('winreg', '_winreg')
    assert mm.name == 'winreg'
    assert mm.new == 'winreg'



# Generated at 2022-06-14 02:14:06.164164
# Unit test for constructor of class MovedModule
def test_MovedModule():
    move = MovedModule("name", "old", "new")
    assert move.name == 'name'
    assert move.new == 'new'


# Generated at 2022-06-14 02:14:09.527026
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    from lib2to3.main import StdoutRefactoringTool
    rt = StdoutRefactoringTool([SixMovesTransformer])
    assert rt