

# Generated at 2022-06-14 02:06:10.798325
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    a = MovedAttribute("name", "old_mod", "new_mod", "old_attr", "new_attr")
    assert a.name == "name"
    assert a.new_mod == "new_mod"
    assert a.new_attr == "new_attr"
    b = MovedAttribute("name", "old_mod", "new_mod", "old_attr")
    assert b.name == "name"
    assert b.new_mod == "new_mod"
    assert b.new_attr == "old_attr"
    c = MovedAttribute("name", "old_mod", "new_mod")
    assert c.name == "name"
    assert c.new_mod == "name"
    assert c.new_attr == "name"

# Generated at 2022-06-14 02:06:16.524894
# Unit test for constructor of class MovedModule
def test_MovedModule():
    assert MovedModule("name", "old") == MovedModule("name", "old", "name")
    assert MovedModule("name", "old", None) == MovedModule("name", "old", "name")
    assert MovedModule("name", "old", "name") == MovedModule("name", "old", "name")
    assert MovedModule("name", "old", "new") == MovedModule("name", "old", "new")

# Generated at 2022-06-14 02:06:19.481332
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():  # type: () -> None
    assert SixMovesTransformer.__name__ == 'SixMovesTransformer'
    assert SixMovesTransformer.__doc__ is not None

# Generated at 2022-06-14 02:06:24.306378
# Unit test for constructor of class MovedModule
def test_MovedModule():
    moved_module = MovedModule("xmlrpc_client", "xmlrpclib", "xmlrpc.client")
    assert(moved_module.name == "xmlrpc_client")
    assert(moved_module.old == "xmlrpclib")
    assert(moved_module.new == "xmlrpc.client")



# Generated at 2022-06-14 02:06:28.302706
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    moved_attr = MovedAttribute("name", "old_mod", "new_mod", "old_attr", "new_attr")
    assert(moved_attr.name == "name")
    assert(moved_attr.new_mod == "new_mod")
    assert(moved_attr.new_attr == "new_attr")



# Generated at 2022-06-14 02:06:32.698037
# Unit test for constructor of class MovedModule
def test_MovedModule():
    move_module = MovedModule(name="xx", old="x", new="x")
    assert move_module.name == "xx"
    assert move_module.new == "x"
    move_module = MovedModule(name="xx", old="x")
    assert move_module.name == "xx"
    assert move_module.new == "xx"


# Generated at 2022-06-14 02:06:39.874448
# Unit test for constructor of class MovedModule
def test_MovedModule():
    obj = MovedModule('name', 'old', 'new')
    assert obj.name == 'name'
    assert obj.old == 'old'
    assert obj.new == 'new'
    obj = MovedModule('name', 'old')
    assert obj.name == 'name'
    assert obj.old == 'old'
    assert obj.new == 'name'


# Generated at 2022-06-14 02:06:48.258349
# Unit test for constructor of class MovedModule
def test_MovedModule():
    # In Python 2.6, `import unittest2` doesn't work due to the package
    # layout changed in 2.7. So we write the unit test in this way.
    mm = MovedModule("builtins", "__builtin__")
    assert "{0.name}, {0.old}, {0.new}".format(mm) == "builtins, __builtin__, builtins"
    mm = MovedModule("builtins", "__builtin__", "__builtins__")
    assert "{0.name}, {0.old}, {0.new}".format(mm) == "builtins, __builtin__, __builtins__"

# Generated at 2022-06-14 02:06:51.020981
# Unit test for constructor of class MovedModule
def test_MovedModule():
    module = MovedModule('name', 'old', 'new')
    assert module.name == 'name'
    assert module.new == 'new'
    module = MovedModule('name', 'old')
    assert module.new == 'name'

# Unit test to check moves are correct

# Generated at 2022-06-14 02:06:58.069423
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    name = 'name'
    old_mod = 'old_mod'
    new_mod = 'new_mod'
    old_attr = 'old_attr'
    new_attr = 'new_attr'
    test_class = MovedAttribute(name, old_mod, new_mod, old_attr, new_attr)

    assert test_class.name == name
    assert test_class.new_mod == new_mod
    assert test_class.new_attr == new_attr

# Generated at 2022-06-14 02:07:04.150641
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    obj = MovedAttribute("attr_name", "mod_name", "new_mod_name", "old_attr", "new_attr")

    assert obj.name == "attr_name"
    assert obj.new_mod == "new_mod_name"
    assert obj.new_attr == "new_attr"


# Generated at 2022-06-14 02:07:10.831957
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    for prefix, moves in prefixed_moves:
        for move in moves:
            if isinstance(move, MovedAttribute):
                path = '{}.{}'.format(move.new_mod, move.new_attr)
                result = 'six.moves{}.{}'.format(prefix, move.name)
                assert SixMovesTransformer.rewrites[path] == result
            elif isinstance(move, MovedModule):
                result = 'six.moves{}.{}'.format(prefix, move.name)
                assert SixMovesTransformer.rewrites[move.new] == result

# Generated at 2022-06-14 02:07:13.874107
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    transformer = SixMovesTransformer()
    assert transformer.rewrites is _get_rewrites()

# Generated at 2022-06-14 02:07:29.737116
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    obj = [MovedAttribute("name", "old_mod", "new_mod"),
           MovedAttribute("name", "old_mod", "new_mod", "old_attr"),
           MovedAttribute("name", "old_mod", "new_mod", "old_attr", "new_attr"),
           MovedAttribute("name", "old_mod", "new_mod", new_attr="new_attr"),
           MovedAttribute("name", "old_mod", "new_mod", "old_attr", None),
           MovedAttribute("name", "old_mod", None),
           MovedAttribute("name", "old_mod", None, None, None)]

    assert obj[0].name == "name"
    assert obj[0].new_mod == "new_mod"

# Generated at 2022-06-14 02:07:42.531300
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    a = MovedAttribute("name", "old_mod", "new_mod")
    assert a.name == "name"
    assert a.old_mod == "old_mod"
    assert a.new_mod == "new_mod"
    assert a.old_attr == "name"
    assert a.new_attr == "name"
    b = MovedAttribute("name", "old_mod", "new_mod", "old_attr", "new_attr")
    assert b.name == "name"
    assert b.old_mod == "old_mod"
    assert b.new_mod == "new_mod"
    assert b.old_attr == "old_attr"
    assert b.new_attr == "new_attr"

# Generated at 2022-06-14 02:07:54.764530
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    from .base import BaseImportRewrite
    from ..utils.helpers import eager
    from ..utils.helpers import has_elements
    assert SixMovesTransformer.__bases__ == (BaseImportRewrite,)
    assert not hasattr(SixMovesTransformer, 'rewrites')
    assert hasattr(SixMovesTransformer, '_get_rewrites')
    assert has_elements(SixMovesTransformer.dependencies, 'six')
    assert hasattr(SixMovesTransformer, '__dict__')
    assert hasattr(SixMovesTransformer, '__doc__')
    # Let's test what happens when the _get_rewrites is not lazy
    instance = SixMovesTransformer()
    assert instance.target == (2, 7)

# Generated at 2022-06-14 02:08:04.664125
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    import sys
    # Test no old_attr and no old_mod
    try:
        ma = MovedAttribute("name", None, "new_mod", None, None)
        assert False
    except ValueError:
        assert True
    # Test no old_mod
    try:
        ma = MovedAttribute("name", None, "new_mod", "old_attr", "new_attr")
        assert False
    except ValueError:
        assert True
    # Test no new_mod
    try:
        ma = MovedAttribute("name", "old_mod", None, "old_attr", "new_attr")
        assert False
    except ValueError:
        assert True
    # Test no new_attr

# Generated at 2022-06-14 02:08:07.709547
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    # This test only checks that the MovedAttribute constructor accepts the correct arguments,
    # even if the values are not sensible
    MovedAttribute("name", "old_mod", "new_mod", "old_attr", "new_attr")



# Generated at 2022-06-14 02:08:15.284642
# Unit test for constructor of class MovedModule
def test_MovedModule():
    assert MovedModule("tkinter", "Tkinter").name == "tkinter"
    assert MovedModule("tkinter", "Tkinter").new == "tkinter"
    assert MovedModule("tkinter", "Tkinter", "new").name == "tkinter"
    assert MovedModule("tkinter", "Tkinter", "new").new == "new"
    assert MovedModule("tkinter", new="new").new == "new"
    assert MovedModule("tkinter", new="new").name == "tkinter"
    assert MovedModule("tkinter", new="new").new is not None
    assert MovedModule("tkinter", new="new").name is not None



# Generated at 2022-06-14 02:08:19.917830
# Unit test for constructor of class MovedModule
def test_MovedModule():
    assert MovedModule("builtins", "__builtin__").name == "builtins"
    assert MovedModule("builtins", "__builtin__").new == "builtins"



# Generated at 2022-06-14 02:08:35.070243
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    t = SixMovesTransformer()

# Generated at 2022-06-14 02:08:39.959331
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert str(MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")) \
        == "MovedAttribute(name='cStringIO', old_mod='cStringIO', " \
        "new_mod='io', old_attr='StringIO', new_attr='cStringIO')"


# Generated at 2022-06-14 02:08:45.014399
# Unit test for constructor of class MovedModule
def test_MovedModule():
    # type: () -> None
    m = MovedModule("name", "old", "new")
    assert m.name == "name"
    assert m.new == "new"



# Generated at 2022-06-14 02:08:49.454860
# Unit test for constructor of class MovedModule
def test_MovedModule():
    from .sixmoves import MovedModule
    mm = MovedModule("TestModule", "OldModule", "NewModule")
    assert mm.name == "TestModule"
    assert mm.new == "NewModule"

# Generated at 2022-06-14 02:08:53.695463
# Unit test for constructor of class MovedModule
def test_MovedModule():
    # Assert that `MovedModule(name, old, new)` is equivalent to `MovedModule(name, old)`.
    assert MovedModule("modules", "modules").new == "modules"

# Generated at 2022-06-14 02:08:58.730019
# Unit test for constructor of class MovedModule
def test_MovedModule():
    name = "configparser"
    old = "ConfigParser"
    new = "configparser"
    mm = MovedModule(name, old, new)
    assert mm.__dict__ == {"name": name, "old": old, "new": new}


# Generated at 2022-06-14 02:09:05.868111
# Unit test for constructor of class MovedModule
def test_MovedModule():
    assert MovedModule("name", "old", "new") == MovedModule("name",
                                                            "old", "new")
    assert MovedModule("name", "old") == MovedModule("name", "old", "name")
    assert MovedModule("name", "old") != MovedModule("name", "new")
    assert MovedModule("name", "old") != MovedModule("name2", "old")
    assert MovedModule("name", "old") != MovedModule("name", "old", "new")
    assert MovedModule("name", "old") != object()
    assert MovedModule("name", "old") != None

# Generated at 2022-06-14 02:09:06.831295
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert SixMovesTransformer

# Generated at 2022-06-14 02:09:19.628262
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    with raises(AssertionError):
        MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    with raises(AssertionError):
        MovedAttribute("filter", "itertools", "io", "filter", "filter")
    with raises(AssertionError):
        MovedAttribute("filterfalse", "itertools", "itertools", "filterfalse", "ifilterfalse")
    with raises(AssertionError):
        MovedAttribute("input", "__builtin__", "builtins", "raw_input", "raw_input")
    with raises(AssertionError):
        MovedAttribute("intern", "__builtin__", "sys", "intern", "intern")

# Generated at 2022-06-14 02:09:25.298580
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    a = MovedAttribute("test_attr", "benchmark.test", "benchmark.test")
    assert a.new_mod == "benchmark.test"
    assert a.new_attr == "test_attr"


# Unit tests for constructor of class MovedModule

# Generated at 2022-06-14 02:09:44.695890
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    from libmodernize.fixes.six_moves import SixMovesTransformer
    assert SixMovesTransformer.rewrites[0] ==\
        ('csv.register_dialect', 'six.moves.csv.register_dialect')


# Code copied from six:
if sys.version_info[:2] < (2, 7):
    import commands
    import ConfigParser
    import copy_reg
    import cPickle
    import cStringIO
    import Queue
    import repr
    import SocketServer
    import _dummy_thread
    import thread
    import Tkinter
    import tkColorChooser
    import tkCommonDialog
    import tkFileDialog
    import tkFont
    import tkMessageBox
    import tkSimpleDialog
    import ttk

    import cookielib
    import Cookie


# Generated at 2022-06-14 02:09:50.364910
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    # Constructor should not fail
    MovedAttribute('abc', 'abc')
    MovedAttribute('abc', 'abc', 'def')
    MovedAttribute('abc', 'abc', new_attr='def')
    MovedAttribute('abc', 'abc', old_attr='def')
    MovedAttribute('abc', 'abc', 'def', 'ghi')
    MovedAttribute('abc', 'abc', new_attr='def', old_attr='ghi')



# Generated at 2022-06-14 02:09:56.346156
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert MovedAttribute("name", "old_mod", "new_mod").new_attr == "name"
    assert MovedAttribute("name", "old_mod", "new_mod", old_attr="old_attr").new_attr == "old_attr"
    assert MovedAttribute("name", "old_mod", "new_mod", new_attr="new_attr").new_attr == "new_attr"


# Generated at 2022-06-14 02:09:58.645117
# Unit test for constructor of class MovedModule
def test_MovedModule():
    assert MovedModule("builtins", "__builtin__") is not None


# Generated at 2022-06-14 02:10:11.138518
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    attr = MovedAttribute("name", "module_name", "module_name")
    assert attr.name == "name"
    assert attr.new_attr == "name"
    assert attr.new_mod == "module_name"

    attr = MovedAttribute("name", "module_name", "module_name", "old_attr")
    assert attr.name == "name"
    assert attr.new_attr == "old_attr"
    assert attr.new_mod == "module_name"

    attr = MovedAttribute("name", "module_name", "module_name", "old_attr", "new_attr")
    assert attr.name == "name"
    assert attr.new_attr == "new_attr"
    assert attr.new_mod == "module_name"



# Generated at 2022-06-14 02:10:19.265350
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    from sys import modules
    from ..utils.helpers import eager
    import six

    # The condition is for tests in Python 2.6.
    if six.PY2:
        from six import moves
        modules['six.moves'] = moves

    transformer = SixMovesTransformer()

    assert transformer.target == (2, 7)
    assert len(transformer.rewrites) > 0
    assert transformer.dependencies == ['six']

    assert isinstance(transformer.rewrites, eager)

# Generated at 2022-06-14 02:10:23.538601
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    mo = MovedAttribute('x', 'a', 'b', 'y', 'z')
    assert mo.name == 'x'
    assert mo.new_mod == 'b'
    assert mo.new_attr == 'z'

# Generated at 2022-06-14 02:10:26.134438
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    obj = SixMovesTransformer()
    assert obj.target == (2, 7)
    assert obj.rewrites == _get_rewrites()
    assert obj.dependencies == ['six']

# Generated at 2022-06-14 02:10:29.733194
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    """Unit test for constructor of class SixMovesTransformer"""
    # pylint: disable=unused-argument
    # https://github.com/PyCQA/pylint/issues/73
    obj = SixMovesTransformer(None)

# Generated at 2022-06-14 02:10:42.622909
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    att = MovedAttribute('name', 'old_mod', 'new_mod', 'old_attr', 'new_attr')
    assert att.name == 'name'
    assert att.new_mod == 'new_mod'
    assert att.new_attr == 'new_attr'
    att = MovedAttribute('name', 'old_mod', 'new_mod', 'old_attr')
    assert att.name == 'name'
    assert att.new_mod == 'new_mod'
    assert att.new_attr == 'old_attr'
    att = MovedAttribute('name', 'old_mod', 'new_mod')
    assert att.name == 'name'
    assert att.new_mod == 'new_mod'
    assert att.new_attr == 'name'


# Generated at 2022-06-14 02:11:04.011039
# Unit test for constructor of class MovedModule
def test_MovedModule():
    moved_module = MovedModule(name='test_name', old='test_old', new='test_new')
    assert(moved_module.name == 'test_name')
    assert(moved_module.old == 'test_old')
    assert(moved_module.new == 'test_new')
    moved_module = MovedModule(name='test_name2', old='test_old2')
    assert(moved_module.name == 'test_name2')
    assert(moved_module.old == 'test_old2')
    assert(moved_module.new == 'test_name2')


# Generated at 2022-06-14 02:11:08.868915
# Unit test for constructor of class MovedModule
def test_MovedModule():
    test = MovedModule('foo', 'bar')
    assert test.name == 'foo'
    assert test.old == 'bar'
    assert test.new == 'foo'



# Generated at 2022-06-14 02:11:20.917016
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    from .base import BaseImportRewrite
    from ..utils.helpers import eager
    from .base import BaseImportRewrite
    import sys
    assert not (SixMovesTransformer.__bases__[0] is BaseImportRewrite)
    assert SixMovesTransformer.dependencies == ['six']
    assert SixMovesTransformer.rewrites == _get_rewrites()
    assert SixMovesTransformer.target == (2, 7)
    assert (SixMovesTransformer('./', './', ['./'], False, False, None).target == (2, 7))
    assert (SixMovesTransformer('./', './', ['./'], False, False, None).dependencies == ['six'])

# Generated at 2022-06-14 02:11:22.113754
# Unit test for constructor of class MovedModule
def test_MovedModule():
    """Case shouldn't raise an exception"""
    MovedModule('', '')

# Generated at 2022-06-14 02:11:35.329106
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert MovedAttribute('a', 'b', 'c') == MovedAttribute('a', 'b', 'c')
    assert MovedAttribute('a', 'b', 'c').name == 'a'
    assert MovedAttribute('a', 'b', 'c').new_mod == 'c'
    assert MovedAttribute('a', 'b', 'c').new_attr == 'a'

    assert MovedAttribute('a', 'b', 'c', 'd', 'e') == MovedAttribute('a', 'b', 'c', 'd', 'e')
    assert MovedAttribute('a', 'b', 'c', 'd', 'e').name == 'a'
    assert MovedAttribute('a', 'b', 'c', 'd', 'e').new_mod == 'c'

# Generated at 2022-06-14 02:11:37.676542
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    # type: () -> None
    assert isinstance(SixMovesTransformer.rewrites, list)

# Generated at 2022-06-14 02:11:40.787082
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    transformer = SixMovesTransformer()
    assert transformer.rewrites == _get_rewrites()

# Generated at 2022-06-14 02:11:48.013827
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert len(SixMovesTransformer.rewrites) == 106
    assert isinstance(SixMovesTransformer.rewrites, list)
    assert isinstance(SixMovesTransformer.rewrites[0], tuple)
    assert SixMovesTransformer.rewrites[0][0] == 'io.StringIO'
    assert SixMovesTransformer.rewrites[0][1] == 'six.moves.cStringIO'

# Generated at 2022-06-14 02:11:52.936085
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    moved_attribute = MovedAttribute(
        "cStringIO", "cStringIO", "io", "StringIO")
    assert moved_attribute.name == "cStringIO"
    assert moved_attribute.new_mod == "io"
    assert moved_attribute.new_attr == "StringIO"


# Generated at 2022-06-14 02:11:55.124989
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert MovedAttribute("cStringIO", "cStringIO", "io", "StringIO").new_attr == "StringIO"

# Generated at 2022-06-14 02:12:20.562809
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    SixMovesTransformer()
    assert True

# Generated at 2022-06-14 02:12:26.718738
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    import six.moves
    from ..utils.helpers import eager
    @eager
    def _get_rewrites():
        for prefix, moves in prefixed_moves:
            for move in moves:
                if isinstance(move, MovedAttribute):
                    path = '{}.{}'.format(move.new_mod, move.new_attr)
                    yield (path, 'six.moves{}.{}'.format(prefix, move.name))
                elif isinstance(move, MovedModule):
                    yield (move.new, 'six.moves{}.{}'.format(prefix, move.name))
    assert _get_rewrites() == SixMovesTransformer.rewrites

# Generated at 2022-06-14 02:12:31.859091
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    a = MovedAttribute("filter", "itertools", "builtins", "ifilter", "filter")
    assert a.name == "filter"
    assert a.new_mod == "builtins"
    assert a.new_attr == "filter"



# Generated at 2022-06-14 02:12:41.146791
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert MovedAttribute('foo', 'foo').new_attr == 'foo'
    assert MovedAttribute('foo', 'foo').new_mod == 'foo'
    assert MovedAttribute('foo', 'bar', 'bar').new_mod == 'bar'
    assert MovedAttribute('foo', 'bar', 'bar').new_attr == 'foo'
    assert MovedAttribute('foo', 'bar', 'baz', 'baz').new_attr == 'baz'
    assert MovedAttribute('foo', 'bar', 'baz', 'baz', 'buz').new_attr == 'buz'



# Generated at 2022-06-14 02:12:45.746320
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    tests = (
        ('StringIO', 'six.moves.cStringIO.StringIO'),
        ('filter', 'six.moves.filter'),
    )
    for import_, expected in tests:
        assert SixMovesTransformer.rewrites[import_] == expected

# Generated at 2022-06-14 02:12:52.103839
# Unit test for constructor of class MovedModule
def test_MovedModule():
    test = MovedModule("test", "test_old")
    assert test.name == "test"
    assert test.new == "test"
    test2 = MovedModule("test2", "test2_old", "test2_new")
    assert test2.name == "test2"
    assert test2.new == "test2_new"

# Unit tests for constructor of class MovedAttribute

# Generated at 2022-06-14 02:12:55.085960
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    t = SixMovesTransformer(None)
    assert t.rewrites == SixMovesTransformer.rewrites
    assert t.dependencies == SixMovesTransformer.dependencies

# Generated at 2022-06-14 02:12:57.972199
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    m = MovedAttribute('cStringIO', 'cStringIO', 'io', 'StringIO', 'StringIO')
    assert m.name == 'cStringIO'
    assert m.new_mod == 'io'
    assert m.new_attr == 'StringIO'

# Generated at 2022-06-14 02:13:01.198682
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert len(_get_rewrites()) == len(six.moves.__all__) + 40

# Generated at 2022-06-14 02:13:06.100271
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    attribute = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert attribute.name == "cStringIO"
    assert attribute.new_mod == "io"
    assert attribute.new_attr == "StringIO"



# Generated at 2022-06-14 02:14:03.015327
# Unit test for constructor of class MovedModule
def test_MovedModule():
    mm = MovedModule("abc")
    assert mm.name == "abc"
    assert mm.new == "abc"

    mm = MovedModule("abc", "def")
    assert mm.name == "abc"
    assert mm.new == "def"

# Generated at 2022-06-14 02:14:08.758682
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    attr = MovedAttribute('foo', 'bar', 'baz', 'old_foo', 'new_foo')
    assert attr.name == 'foo'
    assert attr.new_mod == 'baz'
    assert attr.new_attr == 'new_foo'


# Generated at 2022-06-14 02:14:12.426150
# Unit test for constructor of class MovedModule
def test_MovedModule():
    assert MovedModule('UserList', 'UserList', 'collections').name == 'UserList'
    assert MovedModule('UserList', 'UserList', 'collections').new == 'collections'



# Generated at 2022-06-14 02:14:22.760852
# Unit test for constructor of class MovedModule
def test_MovedModule():
    # "moved_module" is the instantiation of MovedModule
    moved_module = MovedModule("builtins", "__builtin__")
    assert moved_module.name == "builtins"
    assert moved_module.new == "builtins"

    moved_module = MovedModule("configparser", "ConfigParser")
    assert moved_module.name == "configparser"
    assert moved_module.new == "configparser"

    moved_module = MovedModule("dbm_gnu", "gdbm", "dbm.gnu")
    assert moved_module.name == "dbm_gnu"
    assert moved_module.new == "dbm.gnu"


# Generated at 2022-06-14 02:14:32.561038
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    _moved_attribute = MovedAttribute("name", "old_mod", "new_mod", "old_attr", "new_attr")
    assert _moved_attribute.name == "name"
    assert _moved_attribute.old_mod == "old_mod"
    assert _moved_attribute.new_mod == "new_mod"
    assert _moved_attribute.old_attr == "old_attr"
    assert _moved_attribute.new_attr == "new_attr"

# Generated at 2022-06-14 02:14:40.549216
# Unit test for constructor of class MovedModule
def test_MovedModule():
    assert MovedAttribute("cStringIO", "cStringIO", "io", "StringIO").new_attr == "StringIO"
    assert MovedAttribute("filter", "itertools", "builtins", "ifilter", "filter").new_attr == "filter"
    assert MovedAttribute("filterfalse", "itertools", "itertools", "ifilterfalse", "filterfalse").new_attr == "filterfalse"
    assert MovedAttribute("input", "__builtin__", "builtins", "raw_input", "input").new_attr == "input"
    assert MovedAttribute("intern", "__builtin__", "sys").new_attr == "intern"
    assert MovedAttribute("map", "itertools", "builtins", "imap", "map").new_attr == "map"

# Generated at 2022-06-14 02:14:51.656951
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    with pytest.raises(TypeError):
        MovedAttribute()
    with pytest.raises(TypeError):
        MovedAttribute(name='')
    MovedAttribute('name', 'oldmod', 'newmod')
    MovedAttribute('name', 'oldmod', 'newmod', 'oldattr', 'newattr')
    MovedAttribute('name', 'oldmod', None, 'oldattr')
    MovedAttribute('name', None, 'newattr')
    MovedAttribute('name', None, None)


# Generated at 2022-06-14 02:15:04.836002
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    rewrites = _get_rewrites()
    assert len(rewrites) == 89
    assert ('robotparser.RobotFileParser', 'six.moves.urllib.robotparser.RobotFileParser') in rewrites, \
        "MovedModule with prefix not handled properly"
    assert ('email.mime.base.MIMEBase', 'six.moves.email_mime_base.MIMEBase') in rewrites, \
        "MovedModule without prefix not handled properly"
    assert ('configparser.ConfigParser', 'six.moves.configparser.ConfigParser') in rewrites, \
        "MovedModule without prefix not handled properly"

# Generated at 2022-06-14 02:15:15.495152
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    from lib2to3 import fixer_base
    from lib2to3.patcomp import PatternCompiler
    from . import base
    from . import utils
    from test.test_six import six_moves_tests

    rewrites = _get_rewrites()
    six_moves_tests.validate_moves(rewrites)

    result = rewrites['six.moves.html_entities']
    assert result == 'html.entities'

    result = rewrites['six.moves.http_cookiejar']
    assert result == 'http.cookiejar'

    result = rewrites['six.moves.urllib.parse.urlparse']
    assert result == 'urllib.parse.urlparse'


# Generated at 2022-06-14 02:15:24.139910
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    before = '''
import six.moves.urllib.parse as parse
import six.moves.urllib.error as error
import six.moves.urllib as urllib
'''
    after = '''
import urllib.parse as parse
import urllib.error as error
import urllib as urllib
'''
    transformer = SixMovesTransformer(before)
    assert transformer.result == after


if __name__ == '__main__':
    import sys
    SixMovesTransformer(sys.stdin.read())