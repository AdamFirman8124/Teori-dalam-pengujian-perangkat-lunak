

# Generated at 2022-06-14 02:05:59.177124
# Unit test for constructor of class MovedModule
def test_MovedModule():
    MovedModule('builtins', '__builtin__')

# Generated at 2022-06-14 02:06:05.963022
# Unit test for constructor of class MovedModule
def test_MovedModule():
    module = MovedModule(name="test_module", old="test_old", new="test_new")
    assert module.name == "test_module"
    assert module.old == "test_old"
    assert module.new == "test_new"


# Generated at 2022-06-14 02:06:10.091029
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    mod = "test_module"
    attr = "test_attribute"
    move = MovedAttribute(mod, None, None, attr, attr)
    assert move.name == mod
    assert move.new_mod == mod
    assert move.new_attr == attr

# Generated at 2022-06-14 02:06:13.990010
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    a = MovedAttribute("input", "__builtin__", "builtins", "raw_input", "input")
    # pylint: disable=protected-access
    assert a.name == "input"
    assert a.new_mod == "builtins"
    assert a.new_attr == "input"

# Generated at 2022-06-14 02:06:19.693586
# Unit test for constructor of class MovedModule
def test_MovedModule():
    assert MovedModule("test", "original_module", "new_module") == \
        {"name": "test", "old": "original_module", "new": "new_module"}
    assert MovedModule("test", "original_module") == {"name": "test",
                                                      "old": "original_module",
                                                      "new": "test"}

# Generated at 2022-06-14 02:06:24.158577
# Unit test for constructor of class MovedModule
def test_MovedModule():
    from _pytest.warnings import _issue_warning_captured
    from .test_util import transform, assert_transform_result

    with _issue_warning_captured(DeprecationWarning, clear=['six']):
        @transform(MovedModule)
        class Test(MovedModule):
            pass

    Test('x', 'y')

# Generated at 2022-06-14 02:06:32.433558
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert MovedAttribute("foo", "mod", None).name == "foo"
    assert MovedAttribute("foo", "mod", None).new_mod == "foo"
    assert MovedAttribute("foo", "mod", None).new_attr == "foo"
    assert MovedAttribute("foo", "mod", None, "old", "new").name == "foo"
    assert MovedAttribute("foo", "mod", None, "old", "new").new_mod == "foo"
    assert MovedAttribute("foo", "mod", None, "old", "new").new_attr == "new"
    assert MovedAttribute("foo", "mod", None, "old").name == "foo"
    assert MovedAttribute("foo", "mod", None, "old").new_mod == "foo"

# Generated at 2022-06-14 02:06:35.888710
# Unit test for constructor of class MovedModule
def test_MovedModule():
    a = MovedModule('queue', 'Queue')
    assert a.new == 'queue'
    assert a.name == a.name


# Generated at 2022-06-14 02:06:47.627705
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert MovedAttribute('foo', 'foo', 'bar').name == 'foo'
    assert MovedAttribute('foo', 'foo', 'bar').new_mod == 'bar'
    assert MovedAttribute('foo', 'foo', 'bar').new_attr == 'foo'

    assert MovedAttribute('foo', 'foo', 'bar', 'fred').name == 'foo'
    assert MovedAttribute('foo', 'foo', 'bar', 'fred').new_mod == 'bar'
    assert MovedAttribute('foo', 'foo', 'bar', 'fred').new_attr == 'fred'

    assert MovedAttribute('foo', 'foo', 'bar', 'fred', 'wilma').name == 'foo'
    assert MovedAttribute('foo', 'foo', 'bar', 'fred', 'wilma').new_mod == 'bar'
    assert Moved

# Generated at 2022-06-14 02:06:52.092076
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    attr = MovedAttribute('test', 'x', 'y')
    assert str(attr) == 'MovedAttribute(name=test, old_mod=x, new_mod=y, old_attr=None, new_attr=None)'


# Generated at 2022-06-14 02:06:55.415203
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert SixMovesTransformer().rewrites == _get_rewrites()

if __name__ == '__main__':
    # unit tests for this module
    import sys
    import doctest

    doctest.testmod()
    sys.exit(0)

# Generated at 2022-06-14 02:06:59.935156
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    mo = MovedAttribute("filter", "itertools", "builtins", "ifilter", "filter")
    assert mo.name == "filter"
    assert mo.new_mod == "builtins"
    assert mo.new_attr == "filter"

# Generated at 2022-06-14 02:07:02.492183
# Unit test for constructor of class MovedModule
def test_MovedModule():
    from .base import BaseImportRewrite
    assert BaseImportRewrite(
    ).rewrite_import('tkinter', 'foo.bar') == ['tkinter.foo.bar']

# Generated at 2022-06-14 02:07:03.472380
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert SixMovesTransformer.rewrites

# Generated at 2022-06-14 02:07:06.524529
# Unit test for constructor of class MovedModule
def test_MovedModule():
    Move = MovedModule("", "", "")
    assert Move.name == ""
    assert Move.new == ""
    Move = MovedModule("", "old", "")
    assert Move.new == "old"

# Generated at 2022-06-14 02:07:20.455899
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    import sys
    import six
    sys.path.insert(0, 'src')
    from py2to3.fixes import SixMovesTransformer
    from . import settings
    from lib2to3.pgen2.parse import ParseError
    from lib2to3.fixer_util import BlankLine, Comment
    from lib2to3.pygram import python_symbols as syms
    from lib2to3.pytree import Leaf, Node
    from lib2to3.pygram import python_symbols as syms

    # Cases we want to pass through unchanged
    class DummySettings(object):
        def __init__(self):
            self.verbose = False

# Generated at 2022-06-14 02:07:25.674348
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    x = MovedAttribute("name", "old_mod", "new_mod", "old_attr", "new_attr")
    assert x.name == "name"
    assert x.new_mod == "new_mod"
    assert x.new_attr == "new_attr"

# Generated at 2022-06-14 02:07:38.652797
# Unit test for constructor of class MovedModule
def test_MovedModule():
    m1 = MovedModule('a', 'b')
    assert m1.__dict__ == {'name': 'a', 'new': 'a', 'old': 'b'}
    m2 = MovedModule('a.b', 'c.d.e')
    assert m2.__dict__ == {'name': 'a.b', 'new': 'a.b', 'old': 'c.d.e'}
    m3 = MovedModule('a.b', 'c.d.e', 'a.b.c')
    assert m3.__dict__ == {'name': 'a.b', 'new': 'a.b.c', 'old': 'c.d.e'}
    m4 = MovedModule('a.b', 'c.d.e', None)
    assert m4.__dict__

# Generated at 2022-06-14 02:07:48.896253
# Unit test for constructor of class MovedModule
def test_MovedModule():
    # Check for the two variants of MovedModule:
    mod_1 = MovedModule('functools', '_functools', 'functools')
    mod_2 = MovedModule('abc', 'abc')
    assert mod_1.name == 'functools'
    assert mod_1.new == 'functools'
    assert mod_1.old == '_functools'
    assert mod_2.name == 'abc'
    assert mod_2.new == 'abc'
    assert mod_2.old == 'abc'


# Generated at 2022-06-14 02:07:58.900611
# Unit test for constructor of class SixMovesTransformer

# Generated at 2022-06-14 02:08:12.406588
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    import inspect
    import ast
    obj = SixMovesTransformer.__new__(SixMovesTransformer)
    assert isinstance(obj, BaseImportRewrite)
    assert isinstance(obj, ast.NodeTransformer)
    assert obj.target == (2, 7)
    assert isinstance(obj.rewrites, tuple)
    for rewrite in obj.rewrites:
        assert isinstance(rewrite, tuple)
        assert len(rewrite) == 2
        assert isinstance(rewrite[0], str)
        assert isinstance(rewrite[1], str)
    assert isinstance(obj.dependencies, tuple)
    for dep in obj.dependencies:
        assert isinstance(dep, str)
    assert inspect.getsource(obj.visit_Import)

# Generated at 2022-06-14 02:08:14.059414
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert len(SixMovesTransformer.rewrites) == len(_get_rewrites())

# Generated at 2022-06-14 02:08:20.719688
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    move1 = MovedAttribute('name', 'old_mod', 'new_mod', 'old_attr', 'new_attr')
    assert move1.name == 'name'
    assert move1.new_mod == 'new_mod'
    assert move1.new_attr == 'new_attr'



# Generated at 2022-06-14 02:08:32.366276
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    f = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert f.name == "cStringIO"
    assert f.new_mod == "io"
    assert f.new_attr == "StringIO"
    f = MovedAttribute("cStringIO", "cStringIO", "io")
    assert f.name == "cStringIO"
    assert f.new_mod == "io"
    assert f.new_attr == "cStringIO"
    f = MovedAttribute("filterfalse", "itertools", "itertools", "ifilterfalse", "filterfalse")
    assert f.name == "filterfalse"
    assert f.new_mod == "itertools"
    assert f.new_attr == "ifilterfalse"

# Generated at 2022-06-14 02:08:48.762481
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert MovedAttribute("cStringIO", "cStringIO", None).name == "cStringIO"
    assert MovedAttribute("cStringIO", "cStringIO", None).new_mod == "cStringIO"
    assert MovedAttribute("cStringIO", "cStringIO", None).new_attr == "cStringIO"
    assert MovedAttribute("cStringIO", "cStringIO", "io").name == "cStringIO"
    assert MovedAttribute("cStringIO", "cStringIO", "io").new_mod == "io"
    assert MovedAttribute("cStringIO", "cStringIO", "io").new_attr == "cStringIO"
    assert MovedAttribute("cStringIO", "cStringIO", "io", "StringIO").name == "cStringIO"

# Generated at 2022-06-14 02:09:01.906037
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    moved_attribute = MovedAttribute('TestName','TestOldMod','TestNewMod','TestOldAttr','TestNewAttr')
    assert moved_attribute.name == 'TestName'
    assert moved_attribute.new_mod == 'TestNewMod'
    assert moved_attribute.new_attr == 'TestNewAttr'
    moved_attribute = MovedAttribute('TestName','TestOldMod','TestNewMod','TestOldAttr')
    assert moved_attribute.name == 'TestName'
    assert moved_attribute.new_mod == 'TestNewMod'
    assert moved_attribute.new_attr == 'TestOldAttr'
    moved_attribute = MovedAttribute('TestName','TestOldMod')
    assert moved_attribute.name == 'TestName'
    assert moved_attribute.new_mod == 'TestName'
    assert moved_attribute

# Generated at 2022-06-14 02:09:05.080321
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    trans = SixMovesTransformer( {}, {} )
    # Test for rewrites
    assert trans.rewrites == _get_rewrites()
    # Test for six_path
    assert trans.six_path == 'six.moves'



# Generated at 2022-06-14 02:09:09.442104
# Unit test for constructor of class MovedModule
def test_MovedModule():
    m = MovedModule('configparser', 'ConfigParser')
    assert m.name == 'configparser'
    assert m.old == 'ConfigParser'
    assert m.new == 'configparser'


# Generated at 2022-06-14 02:09:20.923788
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    MovedAttribute('cStringIO', 'cStringIO', 'io', 'StringIO')
    MovedAttribute('filter', 'itertools', 'builtins', 'ifilter', 'filter')
    MovedAttribute('filterfalse', 'itertools', 'itertools', 'ifilterfalse', 'filterfalse')
    MovedAttribute('input', '__builtin__', 'builtins', 'raw_input', 'input')
    MovedAttribute('intern', '__builtin__', 'sys')
    MovedAttribute('map', 'itertools', 'builtins', 'imap', 'map')
    MovedAttribute('getcwd', 'os', 'os', 'getcwdu', 'getcwd')
    MovedAttribute('getcwdb', 'os', 'os', 'getcwd', 'getcwdb')
   

# Generated at 2022-06-14 02:09:26.395236
# Unit test for constructor of class MovedModule
def test_MovedModule():
    assert isinstance(MovedModule('name', 'old'), MovedModule)
    assert isinstance(MovedModule('name', 'old', 'new'), MovedModule)
    assert isinstance(MovedModule('name', 'old', new=None), MovedModule)


# Generated at 2022-06-14 02:09:37.072163
# Unit test for constructor of class MovedModule
def test_MovedModule():
    import inspect
    # noinspection PyUnusedLocal,PyShadowingNames
    class MyClass:
        pass
    for name in ['MyClass', '__builtins__', 'builtins']:
        f = MovedModule(name, 'old_mod', 'new_mod')
        assert inspect.isclass(f)
        assert f.name == name
        assert f.old == 'old_mod'
        assert f.new == 'new_mod'



# Generated at 2022-06-14 02:09:41.146397
# Unit test for constructor of class MovedModule
def test_MovedModule():
    if sys.version_info.major > 2:
        try:
            assert SixMovesTransformer.rewrites == _get_rewrites()
        except AssertionError:
            pytest.xfail('this test fails on py3, but it is likely a problem in six')

# Generated at 2022-06-14 02:09:47.419692
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    """ Unit test for constructor of class MovedAttribute
        Tests to make sure that the default behaviour is the same as
        one of the possible call signatures.
    """
    move = MovedAttribute(name="name", old_mod="old_mod", new_mod="new_mod")
    assert move.name == "name"
    assert move.new_mod == "new_mod"
    assert move.new_attr == "name"



# Generated at 2022-06-14 02:09:53.041169
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

# Generated at 2022-06-14 02:09:56.448108
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    transformer = SixMovesTransformer({})
    assert transformer is not None

# Generated at 2022-06-14 02:09:59.794916
# Unit test for constructor of class MovedModule
def test_MovedModule():
    move = MovedModule('bar', 'foo', 'baz')
    assert move.name == 'bar'
    assert move.new == 'baz'


# Generated at 2022-06-14 02:10:08.244617
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    move = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert move.name == "cStringIO"
    assert move.new_mod == "io"
    assert move.new_attr == "StringIO"
    move = MovedAttribute("filter", "itertools", "builtins", "ifilter", "filter")
    assert move.name == "filter"
    move = MovedAttribute("winreg", "_winreg")
    assert move.name == "winreg"

# Generated at 2022-06-14 02:10:12.963411
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    ma = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert ma.name == 'cStringIO'
    assert ma.new_mod == 'io'
    assert ma.new_attr == 'StringIO'



# Generated at 2022-06-14 02:10:25.949859
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    transformer = SixMovesTransformer((2, 7))
    actual = {from_name: to_name for (from_name, to_name) in transformer.rewrites()}

# Generated at 2022-06-14 02:10:35.674258
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    from six import moves

    with pytest.raises(ValueError):
        MovedAttribute("hello", "hello", "world", "name", "name")

    m = MovedAttribute("hello", "hello", "world", "name", "name")
    assert m.new_mod == "world"
    assert m.new_attr == "name"
    assert m.name == "hello"

    m = MovedAttribute("hello", "hello", "world", "name")
    assert m.new_mod == "world"
    assert m.new_attr == "name"
    assert m.name == "hello"

    m = MovedAttribute("hello", "hello", "world")
    assert m.new_mod == "world"
    assert m.new_attr == "hello"
    assert m.name == "hello"

    m

# Generated at 2022-06-14 02:10:43.104571
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert isinstance(SixMovesTransformer(), SixMovesTransformer)


# Generated at 2022-06-14 02:10:49.447638
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert MovedAttribute("cStringIO", "cStringIO", "io", "StringIO").name == "cStringIO"
    assert MovedAttribute("cStringIO", "cStringIO", "io", "StringIO").new_mod == "io"
    assert MovedAttribute("cStringIO", "cStringIO", "io", "StringIO").new_attr == "StringIO"



# Generated at 2022-06-14 02:10:56.830683
# Unit test for constructor of class MovedModule
def test_MovedModule():
    x = MovedModule("name", "obj", "nobj")
    assert x.name == "name"
    assert x.old == "obj"
    assert x.new == "nobj"
    x = MovedModule("name", "obj")
    assert x.name == "name"
    assert x.old == "obj"
    assert x.new == "name"


# Generated at 2022-06-14 02:10:59.904570
# Unit test for constructor of class MovedModule
def test_MovedModule():
    moved = MovedModule('old_name', 'old')
    assert moved.name == 'old_name'
    assert moved.old == 'old'
    assert moved.new == 'old_name'

# Generated at 2022-06-14 02:11:03.587967
# Unit test for constructor of class MovedModule
def test_MovedModule():
    moved_module = MovedModule("new", "old", "new")
    assert moved_module.name == "new"
    assert moved_module.old == "old"
    assert moved_module.new == "new"


# Generated at 2022-06-14 02:11:17.801874
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    attr = MovedAttribute("new_attr", "old_mod", "new_mod")
    assert attr.name == "new_attr"
    assert attr.old_mod == "old_mod"
    assert attr.new_mod == "new_mod"
    assert attr.new_attr == "new_attr"
    assert not hasattr(attr, 'old_attr')

    attr = MovedAttribute("old_attr", "old_mod", "new_mod", "old_attr", "new_attr")
    assert attr.name == "old_attr"
    assert attr.old_mod == "old_mod"
    assert attr.new_mod == "new_mod"
    assert attr.new_attr == "new_attr"

# Generated at 2022-06-14 02:11:22.229093
# Unit test for constructor of class MovedModule
def test_MovedModule():
    movedModule = MovedModule("winreg", "_winreg")
    assert movedModule.name == "winreg"
    assert movedModule.new == "winreg"
    movedModule2 = MovedModule("configparser", "ConfigParser", "configparser")
    assert movedModule2.name == "configparser"
    assert movedModule2.new == "configparser"



# Generated at 2022-06-14 02:11:28.806367
# Unit test for constructor of class MovedModule
def test_MovedModule():
    assert MovedModule("name", "old").name == "name"
    assert MovedModule("name", "old").new == "name"
    assert MovedModule("name", "old", "new").name == "name"
    assert MovedModule("name", "old", "new").new == "new"

# Unit tests for constructor of class MovedAttribute

# Generated at 2022-06-14 02:11:39.560645
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    import six

    t = SixMovesTransformer()
    assert 'six' in t.dependencies
    assert 'six.moves.urllib_parse.urlsplit' in t.rewrites.keys()
    assert t.rewrites['six.moves.urllib_parse.urlsplit'] == 'six.moves.urlsplit'

    assert hasattr(six, 'moves')
    assert hasattr(six.moves, 'urllib_parse')
    assert hasattr(six.moves.urllib_parse, 'urlsplit')
    assert hasattr(six.moves.urllib_parse, 'urlencode')
    assert hasattr(six.moves.urllib_parse, 'ParseResult')
    assert hasattr(six.moves, 'urllib_error')
    assert has

# Generated at 2022-06-14 02:11:43.678174
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    rewrites = {'argparse': 'six.moves.argparse'}
    s = SixMovesTransformer(rewrites)
    assert s.rewrites == rewrites



# Generated at 2022-06-14 02:11:59.137985
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert SixMovesTransformer._get_rewrites() == [('http.cookies', 'six.moves.http_cookies'), 
                                                    ('urllib.parse', 'six.moves.urllib_parse')]


# Generated at 2022-06-14 02:12:08.809907
# Unit test for constructor of class MovedModule
def test_MovedModule():
    obj = MovedModule(name="test_name", old="test_old", new="test_new")
    assert obj.__dict__["name"] == "test_name"
    assert obj.__dict__["old"] == "test_old"
    assert obj.__dict__["new"] == "test_new"

    obj1 = MovedModule(name="test_name1", old="test_old1")
    assert obj1.__dict__["name"] == "test_name1"
    assert obj1.__dict__["old"] == "test_old1"
    assert obj1.__dict__["new"] == obj1.__dict__["name"]


# Generated at 2022-06-14 02:12:13.990974
# Unit test for constructor of class MovedModule
def test_MovedModule():
    m = MovedModule("a", "b")
    assert m.name == "a"
    assert m.old == "b"
    assert m.new == "a"
    m = MovedModule("a", "b", "c")
    assert m.name == "a"
    assert m.old == "b"
    assert m.new == "c"


# Generated at 2022-06-14 02:12:20.477247
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    c = MovedAttribute("a", "b", "c", "d", "e")
    assert c.name == "a"
    assert c.new_mod == "c"
    assert c.new_attr == "e"
    # parameter old_attr should not be used:
    c = MovedAttribute("a", "b", "c", "d")
    assert c.new_attr == "a"

# Generated at 2022-06-14 02:12:26.958193
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    from lib2to3 import pygram, pytree, fixer_base
    from lib2to3.pgen2 import token
    from lib2to3.fixer_util import Name, Call, Comma, String, Attr
    from pytree_utils import Node
    from typing import List, Iterable

    class FakeFixer(fixer_base.BaseFix):
        _accept_type = token.NAME

        def transform(self, node, results):
            # type: (Node, List[Node]) -> Iterable[Node]
            assert False, 'This should not be called'


# Generated at 2022-06-14 02:12:29.469787
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    transformer = SixMovesTransformer(None)
    assert transformer.rewrites is not None
    assert len(transformer.rewrites) == 80

# Generated at 2022-06-14 02:12:34.673395
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    checker = SixMovesTransformer()
    assert 'six' in checker.dependencies
    assert checker.rewrites
    checker.target = (2, 7)
    assert 'six' in checker.dependencies
    assert checker.rewrites

# Generated at 2022-06-14 02:12:40.504826
# Unit test for constructor of class MovedModule
def test_MovedModule():
    m = MovedModule("name", "old")
    assert m.name == 'name'
    assert m.old == 'old'
    assert m.new == 'name'

    m = MovedModule("name", "old", "new")
    assert m.name == 'name'
    assert m.old == 'old'
    assert m.new == 'new'

# Generated at 2022-06-14 02:12:51.605762
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    attributes = MovedAttribute('test_name', 'test', None)
    # type:MovedAttribute
    assert attributes.name == 'test_name'
    assert attributes.old_mod == 'test'
    assert attributes.new_mod == 'test_name'
    assert attributes.name == 'test_name'
    assert attributes.old_attr == None
    assert attributes.new_attr == 'test_name'
    attributes = MovedAttribute('test_name', 'test', 'test_test', 'test_attr')
    assert attributes.name == 'test_name'
    assert attributes.old_mod == 'test'
    assert attributes.new_mod == 'test_test'
    assert attributes.name == 'test_name'
    assert attributes.old_attr == 'test_attr'

# Generated at 2022-06-14 02:13:00.237117
# Unit test for constructor of class MovedModule
def test_MovedModule():
    """Test for MovedModule class."""
    assert MovedModule("builtins", "__builtin__").__dict__ == {'name': 'builtins',
                                                                'old': '__builtin__',
                                                                'new': 'builtins'}
    assert MovedModule("configparser", "ConfigParser").__dict__ == {'name': 'configparser',
                                                                    'old': 'ConfigParser',
                                                                    'new': 'configparser'}
    assert MovedModule("copyreg", "copy_reg").__dict__ == {'name': 'copyreg',
                                                           'old': 'copy_reg',
                                                           'new': 'copyreg'}

# Generated at 2022-06-14 02:13:27.320938
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    """Test SixMovesTransformer."""
    transformer = SixMovesTransformer()
    assert transformer.target == (2, 7)
    assert transformer.rewrites == frozenset(_get_rewrites())

# Generated at 2022-06-14 02:13:31.763242
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    for prefix, moves in prefixed_moves:
        for move in moves:
            if isinstance(move, MovedAttribute):
                path = '{}.{}'.format(move.new_mod, move.new_attr)
                assert path in SixMovesTransformer.rewrites
            elif isinstance(move, MovedModule):
                assert move.new in SixMovesTransformer.rewrites

# Generated at 2022-06-14 02:13:34.594980
# Unit test for constructor of class MovedModule
def test_MovedModule():
    moved_module = MovedModule("name", "old", "new")
    assert  moved_module.new == "new"


# Generated at 2022-06-14 02:13:40.387731
# Unit test for constructor of class MovedModule
def test_MovedModule():
    movedModule = MovedModule('queue', 'Queue')
    assert movedModule.name == 'queue'
    assert movedModule.old == 'Queue'
    assert movedModule.new == 'queue'
    movedModule = MovedModule('queue', 'Queue', 'newQueue')
    assert movedModule.name == 'queue'
    assert movedModule.old == 'Queue'
    assert movedModule.new == 'newQueue'



# Generated at 2022-06-14 02:13:52.018152
# Unit test for constructor of class SixMovesTransformer

# Generated at 2022-06-14 02:13:53.478397
# Unit test for constructor of class MovedModule
def test_MovedModule():
    assert isinstance(MovedModule('builtins', '__builtin__'), MovedModule)

# Generated at 2022-06-14 02:13:55.936606
# Unit test for constructor of class MovedModule
def test_MovedModule():
    module = MovedModule('__builtin__', 'six.moves')
    assert module.name == '__builtin__'
    assert module.new == 'six.moves'

# Generated at 2022-06-14 02:14:03.448054
# Unit test for constructor of class MovedModule
def test_MovedModule():
    mm = MovedModule('name')
    assert mm.name == 'name'
    assert mm.new == 'name'
    mm = MovedModule('name', 'old')
    assert mm.name == 'name'
    assert mm.new == 'old'
    mm = MovedModule('name', 'old', 'new')
    assert mm.name == 'name'
    assert mm.new == 'new'
    mm = MovedModule('name', new='new')
    assert mm.name == 'name'
    assert mm.new == 'new'

# Generated at 2022-06-14 02:14:11.339870
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert MovedAttribute("test", "test_old", "test_new", "test_old_attr", "test_new_attr").name == "test"
    assert MovedAttribute("test", "test_old", "test_new", "test_old_attr", "test_new_attr").new_mod == "test_new"
    assert MovedAttribute("test", "test_old", "test_new", "test_old_attr", "test_new_attr").new_attr == "test_new_attr"

    assert MovedAttribute("test", "test_old", "test_new").name == "test"
    assert MovedAttribute("test", "test_old", "test_new").new_mod == "test_new"

# Generated at 2022-06-14 02:14:12.198112
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert len(_moved_attributes) > 0

# Generated at 2022-06-14 02:15:15.003871
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    MovedAttribute("name", "old_mod", "new_mod", "old_attr", "new_attr")
    MovedAttribute("name", "old_mod", "new_mod", "old_attr", None)
    MovedAttribute("name", "old_mod", "new_mod", None, "new_attr")
    MovedAttribute("name", "old_mod", "new_mod")
    MovedAttribute("name", "old_mod", None)
    MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    MovedAttribute("filter", "itertools", "builtins", "ifilter", "filter")
    MovedAttribute("filterfalse", "itertools", "itertools", "ifilterfalse", "filterfalse")

# Generated at 2022-06-14 02:15:19.126637
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    # type: () -> None
    rewrites = list(_get_rewrites())
    assert len(rewrites) == 157
    rewrite = rewrites[0]
    expected = ('sys.intern', 'six.moves.intern')
    assert rewrite == expected

# Generated at 2022-06-14 02:15:22.176725
# Unit test for constructor of class MovedModule
def test_MovedModule():
    new = MovedModule("name", "old")
    assert new.name == "name"
    assert new.new == "name"



# Generated at 2022-06-14 02:15:29.157515
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    ma = MovedAttribute('input', '__builtin__', 'builtins', 'raw_input', 'input')
    assert ma.name == 'input'
    assert ma.old_mod is None
    assert ma.new_mod == 'builtins'
    assert ma.old_attr == 'raw_input'
    assert ma.new_attr == 'input'
    assert str(ma) == "MovedAttribute(name='input', old_mod=None, new_mod='builtins', old_attr='raw_input', new_attr='input')"


# Generated at 2022-06-14 02:15:31.624429
# Unit test for constructor of class MovedModule
def test_MovedModule():
    """Test MovedModule constructor."""
    MovedModule('mod', 'old', 'new')

# Generated at 2022-06-14 02:15:34.661298
# Unit test for constructor of class MovedModule
def test_MovedModule():
    m = MovedModule("test", "test_old", "test_new")
    assert m.name == "test"
    assert m.old == "test_old"
    assert m.new == "test_new"

# Generated at 2022-06-14 02:15:37.010017
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    expected_rewrites = _get_rewrites()
    assert SixMovesTransformer.rewrites == expected_rewrites



# Generated at 2022-06-14 02:15:44.822819
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    """Test the constructor of the class SixMovesTransformer."""
    x = SixMovesTransformer()
    assert x.rewrites[0][0] == 'email.mime.base'
    assert x.rewrites[0][1] == 'six.moves.email_mime_base'
    assert x.rewrites[-1][0] == 'urllib.robotparser'
    assert x.rewrites[-1][1] == 'six.moves.urllib_robotparser'

# Generated at 2022-06-14 02:15:49.624506
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    a = MovedAttribute('a', 'b', 'c', 'd', 'e')
    assert a.name == 'a'
    assert a.new_mod == 'c'
    assert a.new_attr == 'e'

# Generated at 2022-06-14 02:15:52.831203
# Unit test for constructor of class MovedModule
def test_MovedModule():
    assert MovedModule("abc", "abc").new == 'abc'
    assert MovedModule("abc", "ABC", "xyz").new == 'xyz'