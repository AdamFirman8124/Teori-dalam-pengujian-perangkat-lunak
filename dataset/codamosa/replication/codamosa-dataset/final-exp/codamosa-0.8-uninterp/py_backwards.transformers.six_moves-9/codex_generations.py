

# Generated at 2022-06-14 02:06:05.016804
# Unit test for constructor of class MovedModule
def test_MovedModule():
    mm = MovedModule('name', 'old' , 'new')
    assert mm.name == 'name'
    assert mm.old == 'old'
    assert mm.new == 'new'

    mm2 = MovedModule('name', 'old')
    assert mm2.new == 'name'


# Generated at 2022-06-14 02:06:10.791319
# Unit test for constructor of class MovedModule
def test_MovedModule():
    moved = MovedModule('foo', '_foo')
    assert moved.name == 'foo'
    assert moved.old == '_foo'
    assert moved.new == 'foo'

    moved = MovedModule('foo', '_foo', 'bar')
    assert moved.name == 'foo'
    assert moved.old == '_foo'
    assert moved.new == 'bar'



# Generated at 2022-06-14 02:06:14.026182
# Unit test for constructor of class MovedModule
def test_MovedModule():
    """ Test constructor of class MovedModule

        >>> x=MovedModule("builtins", "__builtin__")
        >>> x.new
        'builtins'
        >>> x.name
        'builtins'
    """


# Generated at 2022-06-14 02:06:17.272345
# Unit test for constructor of class MovedModule
def test_MovedModule():
    m = MovedModule("name", "old", "new")
    assert(m.name == "name")
    assert(m.new == "new")

# Generated at 2022-06-14 02:06:24.672181
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert len(SixMovesTransformer.rewrites) == len(set(SixMovesTransformer.rewrites))
    assert len(SixMovesTransformer.rewrites) == len(_moved_attributes) + len(_urllib_parse_moved_attributes) + len(_urllib_error_moved_attributes) + len(_urllib_request_moved_attributes) + len(_urllib_response_moved_attributes) + len(_urllib_robotparser_moved_attributes)

# Generated at 2022-06-14 02:06:33.180644
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    from lib2to3.pgen2 import token

    for prefix, moves in prefixed_moves:
        for move in moves:
            if isinstance(move, MovedAttribute):
                path = '{}.{}'.format(move.new_mod, move.new_attr)
                # check rewrite of import X => six.moves.X
                assert SixMovesTransformer.rewrites[path] == 'six.moves{}.{}'.format(prefix, move.name)
                # check ImportFrom of six.moves.X was added
                assert SixMovesTransformer.froms[move.name] == 'six.moves{}'.format(prefix)
            elif isinstance(move, MovedModule):
                # check rewrite of import X => six.moves.X
                assert SixMovesTransformer.rewrites

# Generated at 2022-06-14 02:06:46.009132
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    class MovedAttributes:
        def __init__(self, name, old_mod, new_mod, old_attr=None, new_attr=None):
            self.name = name
            if new_mod is None:
                new_mod = name
            self.new_mod = new_mod
            if new_attr is None:
                if old_attr is None:
                    new_attr = name
                else:
                    new_attr = old_attr
            self.new_attr = new_attr
        def assert_equal(self,name,old_mod,new_mod,old_attr=None,new_attr=None):
            assert self.name == name
            if new_mod is None:
                new_mod = name
            assert self.new_mod == new_mod

# Generated at 2022-06-14 02:06:48.098288
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    t = SixMovesTransformer()
    assert t.rewrites == _get_rewrites()

# Generated at 2022-06-14 02:06:54.134193
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    x = SixMovesTransformer()
    assert 'six' in x.dependencies
    assert x.dependencies == ['six']
    assert x.__doc__ == "Replaces moved modules with ones from `six.moves`."
    assert 'filter' in x.rewrites
    assert '_winreg' in x.rewrites
    assert '_winreg' not in x._orig_rewrites
    assert 'getoutput' in x.rewrites
    assert 'getoutput' not in x._orig_rewrites
    assert 'robotparser' in x.rewrites
    assert 'robotparser' not in x._orig_rewrites
    assert 'filter' in x.rewrites
    assert 'filter' not in x._orig_rewrites

# Following test cases were added at later time...


# Generated at 2022-06-14 02:07:06.307343
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    smt = SixMovesTransformer
    assert smt.target == (2, 7)
    assert len(smt.rewrites) == 57
    assert len(smt.dependencies) == 1
    assert smt.dependencies[0] == 'six'

# Generated at 2022-06-14 02:07:12.525748
# Unit test for constructor of class MovedModule
def test_MovedModule():
    assert MovedModule("builtins", "__builtin__")
    assert MovedModule("moves.urllib_parse", "urlparse")
    assert MovedModule("moves.urllib", "urllib")


# Generated at 2022-06-14 02:07:28.352896
# Unit test for constructor of class MovedModule
def test_MovedModule():
    assert MovedModule("builtins", "__builtin__").name == "builtins"
    assert MovedModule("builtins", "__builtin__").new == "builtins"
    assert MovedModule("queue", "Queue").name == "queue"
    assert MovedModule("queue", "Queue").new == "queue"
    assert MovedModule("tkinter", "Tkinter").name == "tkinter"
    assert MovedModule("tkinter", "Tkinter").new == "tkinter"
    assert MovedModule("copyreg", "copy_reg").name == "copyreg"
    assert MovedModule("copyreg", "copy_reg").new == "copyreg"
    assert MovedModule("urllib.parse", __name__ + ".moves.urllib_parse").name == "urllib.parse"
   

# Generated at 2022-06-14 02:07:41.297467
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert MovedAttribute("name", "old_mod", "new_mod", "old_attr", "new_attr").name == "name"
    assert MovedAttribute("name", "old_mod", "new_mod", "old_attr", "new_attr").new_mod == "new_mod"
    assert MovedAttribute("name", "old_mod", "new_mod", "old_attr", "new_attr").new_attr == "new_attr"
    assert MovedAttribute("name", "old_mod", "new_mod", None, "new_attr").new_attr == "new_attr"
    assert MovedAttribute("name", "old_mod", "new_mod", None, None).new_attr == "name"

# Generated at 2022-06-14 02:07:46.798993
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    moved_att = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert moved_att.name == "cStringIO"
    assert moved_att.new_mod == "io"
    assert moved_att.new_attr == "StringIO"


# Generated at 2022-06-14 02:07:48.597057
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    st = SixMovesTransformer()
    assert st.rewrites == _get_rewrites()

# Generated at 2022-06-14 02:07:58.373263
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert MovedAttribute("parse", "urlparse", "urllib.parse").name == 'parse'
    # Check that `new_attr` defaults to `name` if not specified.
    assert MovedAttribute("parse_qs", "urlparse", "urllib.parse").new_attr == 'parse_qs'
    # Check that `new_attr` defaults to `name` if `old_attr` is specified.
    assert MovedAttribute("parse_qs", "urlparse", "urllib.parse", old_attr='parse_qsl').new_attr == 'parse_qs'
    # Check that `new_attr` defaults to `old_attr` if `new_attr == None`.

# Generated at 2022-06-14 02:08:07.837628
# Unit test for constructor of class SixMovesTransformer

# Generated at 2022-06-14 02:08:16.282044
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    ma = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert ma.name == 'cStringIO'
    assert ma.new_mod == 'io'
    assert ma.new_attr == 'StringIO'

    ma = MovedAttribute("filter", "itertools", "builtins", "ifilter", "filter")
    assert ma.name == 'filter'
    assert ma.new_mod == 'builtins'
    assert ma.new_attr == 'filter'

    ma = MovedAttribute("input", "__builtin__", "builtins", "raw_input", "input")
    assert ma.name == 'input'
    assert ma.new_mod == 'builtins'
    assert ma.new_attr == 'input'


# Generated at 2022-06-14 02:08:18.781127
# Unit test for constructor of class MovedModule
def test_MovedModule():
    MovedModule('builtins', '__builtin__')


# Generated at 2022-06-14 02:08:28.491806
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
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

# Generated at 2022-06-14 02:08:41.392591
# Unit test for constructor of class MovedModule
def test_MovedModule():
    assert MovedModule('module_name', 'old_name').name == 'module_name'
    assert MovedModule('module_name', 'old_name').new == 'module_name'
    assert MovedModule('module_name', 'old_name').old == 'old_name'
    assert MovedModule('module_name', 'old_name', 'new_name').name == 'module_name'
    assert MovedModule('module_name', 'old_name', 'new_name').new == 'new_name'
    assert MovedModule('module_name', 'old_name', 'new_name').old == 'old_name'
    assert MovedModule('module_name', None, 'new_name').name == 'module_name'

# Generated at 2022-06-14 02:08:46.340229
# Unit test for constructor of class MovedModule
def test_MovedModule():
    obj = MovedModule('test', 'before', 'after')

    assert obj.name == 'test'
    assert obj.old == 'before'
    assert obj.new == 'after'



# Generated at 2022-06-14 02:08:50.330765
# Unit test for constructor of class MovedModule
def test_MovedModule():
    m = MovedModule("name", "old", "new")
    assert m.name == "name"
    assert m.old == "old"
    assert m.new == "new"

# Generated at 2022-06-14 02:08:57.387133
# Unit test for constructor of class MovedModule
def test_MovedModule():
    '''__init__(name, old, new=None)'''

    assert MovedModule("queue", "Queue").name == "queue"
    assert MovedModule("queue", "Queue").new == "queue"
    assert MovedModule("queue", "Queue", "foo").name == "queue"
    assert MovedModule("queue", "Queue", "foo").new == "foo"


# Generated at 2022-06-14 02:09:00.096019
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert hasattr(SixMovesTransformer, 'target')
    assert hasattr(SixMovesTransformer, 'rewrites')
    assert hasattr(SixMovesTransformer, 'dependencies')

# Generated at 2022-06-14 02:09:09.159532
# Unit test for constructor of class MovedModule
def test_MovedModule():
    object = MovedModule('name', 'old')
    assert object.name == 'name'
    assert object.old == 'old'
    assert object.new == 'name'
    assert str(object) == (
        "MovedModule(name='name', old='old', new=None)")
    object = MovedModule('name', 'old', 'new')
    assert object.name == 'name'
    assert object.old == 'old'
    assert object.new == 'new'
    assert str(object) == (
        "MovedModule(name='name', old='old', new='new')")

# Generated at 2022-06-14 02:09:14.076258
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    x = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert x.name == "cStringIO"
    assert x.new_mod == "cStringIO"
    assert x.new_attr == "StringIO"


# Generated at 2022-06-14 02:09:16.733407
# Unit test for constructor of class MovedModule
def test_MovedModule():
    obj = MovedModule("name", "old")
    assert obj.name == "name"
    assert obj.new == "name"



# Generated at 2022-06-14 02:09:20.298673
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    rewrites = _get_rewrites()

    # Test the constructor
    SixMovesTransformer()

    # Then the rewrites
    assert 'urllib.parse.unquote_to_bytes' in rewrites
    assert '.urllib.response.addbase' in rewrites
    assert '.urllib.robotparser.RobotFileParser' in rewrites

# Generated at 2022-06-14 02:09:22.835168
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    """Test constructor of class SixMovesTransformer."""
    SixMovesTransformer()

# Generated at 2022-06-14 02:09:28.769538
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    pass

# Generated at 2022-06-14 02:09:33.440142
# Unit test for constructor of class MovedModule
def test_MovedModule():
    my_instance = MovedModule('name', 'old', 'new')
    assert my_instance.name == 'name'
    assert my_instance.new == 'new'
    my_instance = MovedModule('name', 'old')
    assert my_instance.new == 'name'

# Generated at 2022-06-14 02:09:40.597607
# Unit test for constructor of class MovedModule
def test_MovedModule():
    move = MovedModule('test', 'oldtest', 'newtest')
    assert move.name == 'test'
    assert move.new == 'newtest'
    move = MovedModule('test2', 'oldtest2', 'test2')
    assert move.name == 'test2'
    assert move.new == 'test2'
    move = MovedModule('test3', 'oldtest3')
    assert move.name == 'test3'
    assert move.new == 'test3'

# Generated at 2022-06-14 02:09:46.980834
# Unit test for constructor of class MovedModule
def test_MovedModule():
    got = MovedModule("name","old")
    expected = ("name", "old", "name")
    assert got.name == expected[0]
    assert got.old == expected[1]
    assert got.new == expected[2]

    got = MovedModule("name","old","new")
    assert got.name == expected[0]
    assert got.old == expected[1]
    assert got.new == "new"

# Generated at 2022-06-14 02:09:55.060265
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    m = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert m.name == "cStringIO" and m.new_mod == "io" and m.new_attr == "StringIO"

    m = MovedAttribute("cStringIO", "cStringIO", "io")
    assert m.name == "cStringIO" and m.new_mod == "io" and m.new_attr == "cStringIO"

# Generated at 2022-06-14 02:10:02.673243
# Unit test for constructor of class MovedModule
def test_MovedModule():
    import six
    mod = MovedModule("builtins", "__builtin__")
    assert mod.name == "builtins"
    assert mod.new == "builtins"
    assert mod.old == "__builtin__"
    mod = MovedModule("configparser", "ConfigParser", "configparser")
    assert mod.name == "configparser"
    assert mod.new == "configparser"
    assert mod.old == "ConfigParser"

# Generated at 2022-06-14 02:10:13.218948
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    # Test constructor without arguments
    try:
        move = MovedAttribute()
    # AssertionError is raised if no arguments are passed.
    except AssertionError:
        # Do nothing, it is expected
        pass

    # Test constructor with exactly one argument
    try:
        move = MovedAttribute('test')
    # AssertionError is raised if exactly one argument is passed.
    except AssertionError:
        # Do nothing, it is expected
        pass

    # Test constructor with exactly two arguments
    try:
        move = MovedAttribute('test', 'test')
    # AssertionError is raised if exactly two arguments are passed.
    except AssertionError:
        # Do nothing, it is expected
        pass

    # Test constructor with exactly three arguments

# Generated at 2022-06-14 02:10:17.518882
# Unit test for constructor of class MovedModule
def test_MovedModule():
    a = MovedModule("a", "b")
    assert a.name == "a"
    assert a.new == "a"

    b = MovedModule("b", "d", "e")
    assert b.name == "b"
    assert b.new == "e"

# Generated at 2022-06-14 02:10:22.246475
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert not hasattr(SixMovesTransformer, 'rewrites')
    assert len(SixMovesTransformer._get_rewrites()) == len(_get_rewrites())
    assert len(SixMovesTransformer.rewrites) == len(_get_rewrites())

# Generated at 2022-06-14 02:10:23.762986
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert list(_get_rewrites()) == SixMovesTransformer.rewrites

# Generated at 2022-06-14 02:10:45.095287
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    moved_attr = MovedAttribute("zip", "itertools", "builtins", "izip", "zip")
    assert moved_attr.name == "zip"
    assert moved_attr.new_attr == "zip"
    assert moved_attr.new_mod == "builtins"

    moved_attr = MovedAttribute("zip", "itertools", "builtins")
    assert moved_attr.name == "zip"
    assert moved_attr.new_attr == "zip"
    assert moved_attr.new_mod == "builtins"

    moved_attr = MovedAttribute("zip", "itertools", "builtins", "izip")
    assert moved_attr.name == "zip"
    assert moved_attr.new_attr == "izip"
    assert moved_attr.new_mod == "builtins"

   

# Generated at 2022-06-14 02:10:47.505862
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    """Transformer should have rewrites"""
    assert SixMovesTransformer().rewrites is not None

# Generated at 2022-06-14 02:11:01.286787
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

# Generated at 2022-06-14 02:11:11.689508
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    def check_expected_rewrites(expected_rewrites):
        for i, rewrite in enumerate(SixMovesTransformer.rewrites):
            assert rewrite == expected_rewrites[i]

    # Check that the expected six moves import rewrites are in place

# Generated at 2022-06-14 02:11:15.521636
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    a = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert a.name == "cStringIO"
    assert a.new_mod == "io"
    assert a.new_attr == "StringIO"

# Generated at 2022-06-14 02:11:17.990669
# Unit test for constructor of class MovedModule
def test_MovedModule():
    with pytest.raises(ValueError):
        MovedModule("builtins", "__builtin__", "builtins")

# Generated at 2022-06-14 02:11:20.803315
# Unit test for constructor of class MovedModule
def test_MovedModule():
    moved_module = MovedModule('foo', 'bar')
    assert moved_module.name == 'foo'
    assert moved_module.old == 'bar'
    assert moved_module.new == 'foo'

# Generated at 2022-06-14 02:11:26.368199
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    a = MovedAttribute('cStringIO', 'cStringIO', 'io', 'StringIO')
    assert 'cStringIO' == a.name
    assert 'io' == a.new_mod
    assert 'StringIO' == a.new_attr
    assert 'StringIO' == a.new_attr



# Generated at 2022-06-14 02:11:37.343426
# Unit test for constructor of class SixMovesTransformer

# Generated at 2022-06-14 02:11:42.983061
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    l = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert l.name == "cStringIO"
    assert l.new_mod == "io"
    assert l.new_attr == "StringIO"

# Generated at 2022-06-14 02:12:07.418171
# Unit test for constructor of class MovedModule
def test_MovedModule():
    assert MovedModule("foo", "bar").name == "foo"
    assert MovedModule("foo", "bar").old == "bar"
    assert MovedModule("foo", "bar").new == "foo"
    assert MovedModule("foo", "bar", "baz").new == "baz"

# Generated at 2022-06-14 02:12:10.976940
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    x = MovedAttribute("abc", "def", "ghi")
    assert x.name == "abc"
    assert x.new_mod == "ghi"
    assert x.new_attr == "abc"

# Generated at 2022-06-14 02:12:15.803709
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    mov = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert mov.name == "cStringIO"
    assert mov.new_mod == "io"
    assert mov.new_attr == "StringIO"
    assert mov.old_mod is None
    assert mov.old_attr is None

# Test constructor of class MovedModule

# Generated at 2022-06-14 02:12:23.029591
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    for prefix, moves in prefixed_moves:
        for move in moves:
            if isinstance(move, MovedAttribute):
                path = '{}.{}'.format(move.new_mod, move.new_attr)
                six_path = 'six.moves{}.{}'.format(prefix, move.name)
                assert (path, six_path) in _get_rewrites()
            elif isinstance(move, MovedModule):
                assert (move.new, 'six.moves{}.{}'.format(prefix, move.name)) in _get_rewrites()

# Generated at 2022-06-14 02:12:27.990594
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    transformer = SixMovesTransformer()
    # Check that constructor of class BaseImportRewrite has worked properly:
    assert transformer.rewrites == _get_rewrites()
    assert transformer.dependencies == ['six']

# Generated at 2022-06-14 02:12:40.885431
# Unit test for constructor of class SixMovesTransformer

# Generated at 2022-06-14 02:12:44.589073
# Unit test for constructor of class MovedModule
def test_MovedModule():
    name = 'builtins'
    old = '__builtin__'
    new = 'builtins'
    mm = MovedModule(name, old, new)
    assert mm.name == name
    assert mm.old == old
    assert mm.new == new


# Generated at 2022-06-14 02:12:47.263478
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    from libmodernize.fixes.sixmoves import SixMovesTransformer
    assert SixMovesTransformer.rewrites == _get_rewrites()

# Generated at 2022-06-14 02:12:58.119041
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    from .base import TransformationTestCase
    from .util import write_and_run_program
    from .lower_builtin import LowerBuiltin, lower_builtin


    class TestCase(TransformationTestCase):
        transformations = [SixMovesTransformer, LowerBuiltin]


        @classmethod
        def setUpClass(cls):
            super().setUpClass()
            cls.moves = [move.name for _, moves in prefixed_moves for move in moves]


    # First, generate a test case for each moved module. We test whether
    # that module, plus all of the moved modules, are loaded from six.moves,
    # and whether the module is imported as expected.
    with__ = set()

# Generated at 2022-06-14 02:13:02.059507
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    transformer = SixMovesTransformer()
    assert transformer.target == (2, 7)
    assert len(transformer.rewrites) == 137

# Generated at 2022-06-14 02:13:54.859300
# Unit test for constructor of class MovedModule
def test_MovedModule():
    # Create object of class MovedModule
    moved_module = \
        MovedModule("BaseHTTPServer", "BaseHTTPServer")
    # Check for the name of the module
    assert moved_module.name == "BaseHTTPServer"
    # Check which object 'old' points to
    assert moved_module.old == "BaseHTTPServer"
    # Check which object 'new' points to
    assert moved_module.new == "BaseHTTPServer"


# Generated at 2022-06-14 02:13:58.421278
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    data = '''import io
from six.moves import io'''
    expected_output = 'import io'
    assert SixMovesTransformer().transform_source(data) == expected_output



# Generated at 2022-06-14 02:14:06.093330
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert MovedAttribute('name', 'old', 'new').name == 'name'
    assert MovedAttribute('name', 'old', 'new').new_mod == 'new'
    assert MovedAttribute('name', 'old', 'new', 'old_attr', 'new_attr').new_attr == 'new_attr'
    assert MovedAttribute('name', 'old', 'new', 'old_attr').new_attr == 'old_attr'
    assert MovedAttribute('name', 'old', 'new').new_attr == 'name'
    assert MovedAttribute('name', 'old', None, 'old_attr').new_attr == 'name'
    assert MovedAttribute('name', 'old', None, 'old_attr', 'new_attr').new_attr == 'new_attr'



# Generated at 2022-06-14 02:14:11.897944
# Unit test for constructor of class MovedModule
def test_MovedModule():
    assert MovedModule("moved", "old").name == "moved"
    assert MovedModule("moved", "old").new == "moved"
    assert MovedModule("moved", "old", "new").name == "moved"
    assert MovedModule("moved", "old", "new").new == "new"


# Generated at 2022-06-14 02:14:13.995127
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    transformer = SixMovesTransformer()
    assert transformer.rewrites == _get_rewrites()

# Generated at 2022-06-14 02:14:22.367227
# Unit test for constructor of class MovedModule
def test_MovedModule():
    assert MovedModule("module", "oldmodule") == MovedModule("module", "oldmodule")
    assert MovedModule("module", "oldmodule", "newmodule") == MovedModule("module", "oldmodule", "newmodule")
    assert MovedModule("module", "oldmodule") != 1
    assert MovedModule("module", "oldmodule") == MovedModule("module", "oldmodule", "module")
    assert MovedModule("module", "oldmodule") != MovedModule("module", "oldmodule", "newmodule")


# Generated at 2022-06-14 02:14:37.447341
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    move = MovedAttribute('name', 'old_mod', None)
    assert move.name == 'name'
    assert move.new_mod == 'name'
    assert move.new_attr == 'name'

    move = MovedAttribute('name', 'old_mod', 'new_mod')
    assert move.name == 'name'
    assert move.new_mod == 'new_mod'
    assert move.new_attr == 'name'

    move = MovedAttribute('name', 'old_mod', 'new_mod', 'old_attr')
    assert move.name == 'name'
    assert move.new_mod == 'new_mod'
    assert move.new_attr == 'old_attr'

    move = MovedAttribute('name', 'old_mod', 'new_mod', 'old_attr', 'new_attr')

# Generated at 2022-06-14 02:14:42.247193
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    move = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert move.name == "cStringIO"
    assert move.new_mod == "io"
    assert move.new_attr == "StringIO"
    move = MovedAttribute("cStringIO", "cStringIO", "io")
    assert move.new_attr == "cStringIO"

# Generated at 2022-06-14 02:14:48.709661
# Unit test for constructor of class MovedModule
def test_MovedModule():
    mod = MovedModule('module')
    assert mod.name == 'module'
    assert mod.new == 'module'

    mod = MovedModule('module', 'name')
    assert mod.name == 'module'
    assert mod.new == 'name'

# Unit tests for constructor of class MovedAttribute

# Generated at 2022-06-14 02:15:01.472507
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert MovedAttribute("cStringIO", "cStringIO", "io", "StringIO").name == "cStringIO"
    assert MovedAttribute("cStringIO", "cStringIO", "io", "StringIO").new_mod == "io"
    assert MovedAttribute("cStringIO", "cStringIO", "io", "StringIO").new_attr == "StringIO"
    assert MovedAttribute("filter", "itertools", "builtins", "ifilter", "filter").name == "filter"
    assert MovedAttribute("filter", "itertools", "builtins", "ifilter", "filter").new_mod == "builtins"
    assert MovedAttribute("filter", "itertools", "builtins", "ifilter", "filter").new_attr == "filter"