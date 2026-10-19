

# Generated at 2022-06-14 02:05:57.611166
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    instance = SixMovesTransformer()

    assert instance.target == (2, 7)
    assert len(instance.rewrites) == len(_get_rewrites())
    assert set(instance.rewrites.keys()) == set(_get_rewrites().keys())
    assert instance.dependencies == ['six']

# Generated at 2022-06-14 02:06:01.894444
# Unit test for constructor of class MovedModule
def test_MovedModule():
    mm = MovedModule("builtins", "__builtin__", "six.moves.builtins")
    assert mm.name == 'builtins'
    assert mm.new == 'six.moves.builtins'


# Generated at 2022-06-14 02:06:06.139551
# Unit test for constructor of class MovedModule
def test_MovedModule():
    module = MovedModule("builtins", "__builtin__")
    assert module.name == "builtins"
    assert module.new == "builtins"
    module = MovedModule("builtins", "__builtin__", "builtin")
    assert module.name == "builtins"
    assert module.new == "builtin"



# Generated at 2022-06-14 02:06:09.551547
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert set(SixMovesTransformer.rewrites) == set(_get_rewrites())

if __name__ == '__main__':
    # Test for constructor
    test_SixMovesTransformer()

# Generated at 2022-06-14 02:06:15.705545
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    """Test for class SixMovesTransformer"""
    assert _get_rewrites() == SixMovesTransformer.rewrites
    assert (SixMovesTransformer.rewrites[0][0],
            SixMovesTransformer.rewrites[0][1]) == ('io.StringIO', 'six.moves.cStringIO')
    assert (SixMovesTransformer.rewrites[1][0],
            SixMovesTransformer.rewrites[1][1]) == ('builtins.ifilter', 'six.moves.filter')


# Generated at 2022-06-14 02:06:25.467176
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    ma = MovedAttribute("name", "old_mod", "new_mod")
    assert ma.name == "name"
    assert ma.new_mod == "new_mod"
    assert ma.new_attr == "name"
    ma = MovedAttribute("name", "old_mod", "new_mod", "old_attr")
    assert ma.new_attr == "old_attr"
    ma = MovedAttribute("name", "old_mod", "new_mod", old_attr="old_attr")
    assert ma.new_attr == "old_attr"
    ma = MovedAttribute("name", "old_mod", "new_mod", None, "new_attr")
    assert ma.new_attr == "new_attr"

# Generated at 2022-06-14 02:06:31.795990
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    obj = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert obj.name == "cStringIO"
    assert obj.new_mod == "io"
    assert obj.new_attr == "StringIO"

# Generated at 2022-06-14 02:06:39.795965
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    from ..utils.helpers import eager
    from ..utils.helpers import get_fullname

    transformer = SixMovesTransformer

    # The following list contains elements with the following structure:
    #  (type, expected output of get_fullname(), expected output of _get_rewrites())

# Generated at 2022-06-14 02:06:40.710737
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    """Unit test for constructor of class SixMovesTransformer."""

    assert SixMovesTransformer is not None

# Generated at 2022-06-14 02:06:49.183786
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    from libcst.testing.utils import UnitTest


    class _TestRewriteMovesAssignment(UnitTest):
        TRANSFORM = SixMovesTransformer

        def test_it(self) -> None:
            self.assert_transformation(
                """
                with mock.patch('sys.stdout', StringIO()) as mock_stdout:
                    print('foobar')
                    assert 'foobar' not in mock_stdout.getvalue()
                """,
                """
                with mock.patch('sys.stdout', StringIO()) as mock_stdout:
                    print('foobar')
                    assert 'foobar' not in mock_stdout.getvalue()
                """,
            )

# Generated at 2022-06-14 02:07:01.897587
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    """Note: this test does NOT test the behaviour of this transformer.
    It tests that the constructor of this transformer works properly."""

# Generated at 2022-06-14 02:07:05.343332
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    t = SixMovesTransformer()
    assert t.dependencies == ['six']
    assert not t.rewrites  # rewrites is eager evaluated
    assert t.target == (2, 7)

# Generated at 2022-06-14 02:07:10.622762
# Unit test for constructor of class MovedAttribute

# Generated at 2022-06-14 02:07:18.863952
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    from ..__main__ import SUPPORTED_VERSIONS
    from ..transformer import get_transformer
    # Since we are testing on Python 2.7 or higher, it
    # should be supported by the transformer
    assert (2, 7) in SUPPORTED_VERSIONS

    trans = get_transformer(2.7)
    assert trans.transformer_name == 'SixMovesTransformer'
    assert trans.target == (2, 7)
    assert len(trans.rewrites) == len(_get_rewrites())

# Generated at 2022-06-14 02:07:27.480454
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer(): # type: ignore
    """Tests that the SixMovesTransformer class is getting all the
    moved modules.

    The tests checks that a moved module or moved module with different
    name is included in the rewrites.
    """
    result = sorted(SixMovesTransformer(None).rewrites)
    assert len(result) == len(prefixed_moves)
    for (prefix, moves), (_, path) in zip(prefixed_moves, result):
        for move in moves:
            if isinstance(move, MovedAttribute):
                assert path.endswith('{}.{}'.format(move.name, move.new_attr))

# Generated at 2022-06-14 02:07:29.601550
# Unit test for constructor of class MovedModule
def test_MovedModule():
    moved = MovedModule("name", "name")
    assert moved.name == moved.new



# Generated at 2022-06-14 02:07:34.620587
# Unit test for constructor of class MovedModule
def test_MovedModule():
    moved_module = MovedModule('test_name', 'test_old', 'test_new')
    assert moved_module.name == 'test_name'
    assert moved_module.old == 'test_old'
    assert moved_module.new == 'test_new'


# Generated at 2022-06-14 02:07:45.850795
# Unit test for constructor of class MovedModule
def test_MovedModule():
    a = MovedModule('a')
    assert a.name == 'a'
    assert a.new == 'a'
    b = MovedModule('b', 'c')
    assert b.name == 'b'
    assert b.new == 'c'
    c = MovedModule('abc', 'xyz', 'pqr')
    assert c.name == 'abc'
    assert c.new == 'xyz'
    d = MovedModule('def', 'ghi')
    assert d.name == 'def'
    assert d.new == 'ghi'
    e = MovedModule('jkl')
    assert e.name == 'jkl'
    assert e.new == 'jkl'
    f = MovedModule('mno', 'pqr', 'stu')

# Generated at 2022-06-14 02:07:47.250079
# Unit test for constructor of class MovedModule
def test_MovedModule():
    _ = MovedModule('queue', 'Queue')

# Generated at 2022-06-14 02:07:53.051793
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    moved_attribute = MovedAttribute("name", "old_mod", "new_mod", "old_attr", "new_attr")
    assert moved_attribute.name == "name"
    assert moved_attribute.new_mod == "new_mod"
    assert moved_attribute.new_attr == "new_attr"


# Generated at 2022-06-14 02:07:56.040945
# Unit test for constructor of class MovedModule
def test_MovedModule():
    MovedModule("", "", "")

# Generated at 2022-06-14 02:08:09.399282
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    ma = MovedAttribute('n', 'nm', 'n')
    assert ma.name == 'n'
    assert ma.new_mod == 'n'
    assert ma.new_attr == 'n'

    ma = MovedAttribute('n', 'nm', 'nn', 'n')
    assert ma.name == 'n'
    assert ma.new_mod == 'nn'
    assert ma.new_attr == 'n'

    ma = MovedAttribute('n', 'nm', 'nn', new_attr='nn')
    assert ma.name == 'n'
    assert ma.new_mod == 'nn'
    assert ma.new_attr == 'nn'

    ma = MovedAttribute('n', 'nm', 'nn', old_attr='no', new_attr='nn')
    assert ma.name == 'n'

# Generated at 2022-06-14 02:08:15.305654
# Unit test for constructor of class MovedModule
def test_MovedModule():
    assert MovedModule('test', 'old').name == 'test'
    assert MovedModule('test', 'old').new == 'test'
    assert MovedModule('test', 'old', 'new').name == 'test'
    assert MovedModule('test', 'old', 'new').new == 'new'
    assert MovedModule('test', 'old', new=None).name == 'test'
    assert MovedModule('test', 'old', new=None).new == 'test'
    assert MovedModule('test', 'old', None).name == 'test'
    assert MovedModule('test', 'old', None).new == 'test'

# Generated at 2022-06-14 02:08:28.765514
# Unit test for constructor of class SixMovesTransformer

# Generated at 2022-06-14 02:08:32.107171
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    import six.moves.urllib.parse
    assert isinstance(six.moves.urllib.parse.ParseResult, six.moves.urllib.parse.ParseResult)

# Generated at 2022-06-14 02:08:48.438088
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert MovedAttribute('name', 'oldmod', 'newmod', 'oldattr', 'newattr') ==\
            MovedAttribute('name', 'oldmod', 'newmod', 'oldattr', 'newattr')
    assert MovedAttribute('name', 'oldmod', 'newmod', 'oldattr', None) ==\
            MovedAttribute('name', 'oldmod', 'newmod', 'oldattr', 'oldattr')
    assert MovedAttribute('name', 'oldmod', 'newmod', None, 'newattr') ==\
            MovedAttribute('name', 'oldmod', 'newmod', 'name', 'newattr')
    assert MovedAttribute('name', 'oldmod', None) ==\
            MovedAttribute('name', 'oldmod', 'name')
    assert MovedAttribute('name', None, None) ==\
            MovedAttribute

# Generated at 2022-06-14 02:08:55.805463
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    m = MovedAttribute('foo', 'mod1', 'mod2')
    assert m.name == 'foo'
    assert m.new_mod == 'mod2'
    assert m.new_attr == 'foo'
    m = MovedAttribute('foo', 'mod1', 'mod2', 'old_foo', 'new_foo')
    assert m.new_attr == 'new_foo'


# Generated at 2022-06-14 02:08:58.638383
# Unit test for constructor of class MovedModule
def test_MovedModule():
    t = MovedModule("name", "old", "new")
    assert t.name == "name"
    assert t.old == "old"
    assert t.new == "new"

# Generated at 2022-06-14 02:09:10.217948
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert MovedAttribute('cStringIO', 'cStringIO', 'io', 'StringIO').name == 'cStringIO'
    assert MovedAttribute('cStringIO', 'cStringIO', 'io', 'StringIO').new_mod == 'io'
    assert MovedAttribute('cStringIO', 'cStringIO', 'io', 'StringIO').new_attr == 'StringIO'
    # new_attr = None, old_attr = None
    assert MovedAttribute('cStringIO', 'cStringIO', 'io').name == 'cStringIO'
    assert MovedAttribute('cStringIO', 'cStringIO', 'io').new_mod == 'io'
    assert MovedAttribute('cStringIO', 'cStringIO', 'io').new_attr == 'cStringIO'
    # new_attr = None, old_attr is not None

# Generated at 2022-06-14 02:09:21.284130
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    ma = MovedAttribute('name', 'old_mod', 'new_mod', 'old_attr', 'new_attr')
    assert ma.name == 'name'
    assert ma.new_mod == 'new_mod'
    assert ma.new_attr == 'new_attr'
    ma = MovedAttribute('name', 'old_mod', 'new_mod', 'old_attr')
    assert ma.name == 'name'
    assert ma.new_mod == 'new_mod'
    assert ma.new_attr == 'old_attr'
    ma = MovedAttribute('name', 'old_mod', 'new_mod')
    assert ma.name == 'name'
    assert ma.new_mod == 'new_mod'
    assert ma.new_attr == 'name'

# Generated at 2022-06-14 02:09:27.162267
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    # This test is only to make sure that the constructor of this class
    # is working.
    SixMo

# Generated at 2022-06-14 02:09:32.552109
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    expected_moved_attribute = MovedAttribute(
        'cStringIO', 'cStringIO', 'io', 'StringIO')
    assert expected_moved_attribute.name == 'cStringIO'
    assert expected_moved_attribute.new_mod == 'io'
    assert expected_moved_attribute.new_attr == 'StringIO'

# Generated at 2022-06-14 02:09:43.570618
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    move = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert (move.name, move.new_mod, move.new_attr) == ('cStringIO', 'io', 'StringIO')
    move = MovedAttribute("cStringIO", "cStringIO", "io")
    assert (move.name, move.new_mod, move.new_attr) == ('cStringIO', 'io', 'cStringIO')
    move = MovedAttribute("cStringIO", "cStringIO", "io", old_attr='StringIO', new_attr='qqq')
    assert (move.name, move.new_mod, move.new_attr) == ('cStringIO', 'io', 'qqq')


# Generated at 2022-06-14 02:09:47.205033
# Unit test for constructor of class MovedModule
def test_MovedModule():
    mm = MovedModule('name', 'old', 'new')
    assert mm.new is 'new'
    assert mm.name is 'name'
    assert mm.old is 'old'

# Generated at 2022-06-14 02:09:53.176408
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    temp = MovedAttribute("name", "old_mod", "new_mod", "old_attr", "new_attr")
    assert temp.name == "name"
    assert temp.new_mod == "new_mod"
    assert temp.new_attr == "new_attr"

# Generated at 2022-06-14 02:09:58.081056
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    """Test if all the rewrites in SixMovesTransformer are valid.
    """
    _test_rewrites_for_class(SixMovesTransformer)

# Generated at 2022-06-14 02:10:09.041341
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert MovedAttribute(None, None, None, None, None).name is None
    assert MovedAttribute(None, None, None, None, None).new_mod is None
    assert MovedAttribute(None, None, None, None, None).new_attr is None
    assert MovedAttribute(None, None, None, None, 'a').new_attr == 'a'
    assert MovedAttribute(None, None, None, 'a').new_attr == 'a'
    assert MovedAttribute(None, None, 'b').new_mod == 'b'
    assert MovedAttribute(None, 'a').old_mod == 'a'
    assert MovedAttribute('b').name == 'b'

# Generated at 2022-06-14 02:10:17.732927
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert MovedAttribute("cStringIO", "cStringIO", "io").new_attr == "cStringIO"
    assert MovedAttribute("cStringIO", "cStringIO", "io", "StringIO").new_attr == "StringIO"
    assert MovedAttribute("cStringIO", "cStringIO", "io", None, "StringIO").new_attr == "StringIO"
    assert MovedAttribute("cStringIO", "cStringIO", "io", "StringIO", None).new_attr == "StringIO"
    assert MovedAttribute("cStringIO", "cStringIO", "io", None, None).new_attr == "cStringIO"

# Generated at 2022-06-14 02:10:28.568581
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    # pylint: disable=attribute-defined-outside-init
    class Test(SixMovesTransformer):
        class_names = SixMovesTransformer.class_names + ['SixMovesTransformer']

    instance = Test()

# Generated at 2022-06-14 02:10:35.108877
# Unit test for constructor of class MovedModule
def test_MovedModule():
    with pytest.raises(AttributeError):
        MovedModule("reprlib", "repr", "repr")

    assert MovedModule("reprlib", "reprlib", "reprlib")
    assert MovedModule("reprlib", "reprlib")


# Generated at 2022-06-14 02:10:43.544735
# Unit test for constructor of class MovedModule
def test_MovedModule():
    move = MovedModule("new", "old")
    assert move.name == "new"
    assert move.old == "old"
    assert move.new == "old"


# Generated at 2022-06-14 02:10:53.283393
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert MovedAttribute("cStringIO", "cStringIO", "io", "StringIO") == MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert MovedAttribute("cStringIO", "cStringIO", "io", "StringIO") != MovedAttribute("cStringIO", "cStringIO", "io", "stringIO")
    assert MovedAttribute("cStringIO", "cStringIO", "io", "StringIO") != MovedAttribute("xStringIO", "cStringIO", "io", "StringIO")


# Generated at 2022-06-14 02:11:04.154436
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    a = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    b = MovedAttribute("getcwd", "os", "os", "getcwdu", "getcwd")
    c = MovedAttribute("filter", "itertools", "builtins", "ifilter", "filter")
    d = MovedAttribute("filterfalse", "itertools", "itertools", "ifilterfalse", "filterfalse")
    assert a.name == "cStringIO"
    assert a.new_mod == "io"
    assert a.new_attr == "StringIO"
    assert b.name == "getcwd"
    assert b.new_mod == "os"
    assert b.new_attr == "getcwd"
    assert c.name == "filter"
    assert c

# Generated at 2022-06-14 02:11:08.127785
# Unit test for constructor of class MovedModule
def test_MovedModule():
    assert MovedModule('builtins', '__builtin__').name == 'builtins'
    assert MovedModule('builtins', '__builtin__').new == 'builtins'
    assert MovedModule('builtins', '__builtin__').old == '__builtin__'

# Generated at 2022-06-14 02:11:20.447804
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    a1 = MovedAttribute("cStringIO", "cStringIO", "io")
    assert a1.name == "cStringIO"
    assert a1.new_mod == "io"
    assert a1.new_attr == "cStringIO"

    a2 = MovedAttribute("cStringIO", "cStringIO", None)
    assert a2.name == "cStringIO"
    assert a2.new_mod == "cStringIO"
    assert a2.new_attr == "cStringIO"

    a3 = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert a3.new_attr == "StringIO"

    a4 = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO", "StringIO2")

# Generated at 2022-06-14 02:11:30.659345
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    for prefix, moves in prefixed_moves:
        for move in moves:
            if isinstance(move, MovedAttribute):
                path = '{}.{}'.format(move.new_mod, move.new_attr)
                test = 'six.moves{}.{}'.format(prefix, move.name)
                assert (path, test) in SixMovesTransformer.rewrites
            elif isinstance(move, MovedModule):
                test = 'six.moves{}.{}'.format(prefix, move.name)
                assert (move.new, test) in SixMovesTransformer.rewrites

# Generated at 2022-06-14 02:11:37.156533
# Unit test for constructor of class MovedModule
def test_MovedModule():
    x = MovedModule("builtins", "__builtin__")
    assert x.name == "builtins"
    assert x.new == "builtins"
    assert x.old == "__builtin__"
    x = MovedModule("configparser", "ConfigParser")
    assert x.name == "configparser"
    assert x.new == "configparser"
    assert x.old == "ConfigParser"

# Generated at 2022-06-14 02:11:41.080157
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    t = SixMovesTransformer
    assert t.target == (2, 7)
    assert t.dependencies == ['six']

# Generated at 2022-06-14 02:11:53.781899
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    from . import rewrite_import
    from .rewrite_test_support import SourceMapTestSupport, TestCase
    from .pgen2 import token
    from .. import utils

    class TestSixMovesTransformer(SourceMapTestSupport, TestCase):
        transformer = SixMovesTransformer
        # Note: no mapping for relative imports
        target = (2, 7)
        maxDiff = None

        @property
        def _expected_replace_count(self):
            if self.target < (3, 3):
                return 18
            if self.target < (3, 7):
                return 19
            if self.target < (3, 9):
                return 20
            if self.target < (3, 10):
                return 22
            return 27


# Generated at 2022-06-14 02:11:55.201949
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert SixMovesTransformer().rewrites == _get_rewrites()

# Generated at 2022-06-14 02:12:02.760788
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    move = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert move.name == "cStringIO"
    assert move.new_mod == "io"
    assert move.new_attr == "StringIO"

# Generated at 2022-06-14 02:12:13.858261
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    def MA(name, old_mod, new_mod, new_attr=None, old_attr=None):
        if new_attr is None:
            if old_attr is None:
                new_attr = name
            else:
                new_attr = old_attr
        return MovedAttribute(name, old_mod, new_mod, old_attr, new_attr)
    assert MA("name", "old_mod", "new_mod", new_attr='new_attr') == \
        MovedAttribute("name", "old_mod", "new_mod", None, "new_attr")
    assert MA("name", "old_mod", "new_mod", old_attr="old_attr") == \
        MovedAttribute("name", "old_mod", "new_mod", "old_attr", "old_attr")

# Generated at 2022-06-14 02:12:22.226362
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    from libcst.metadata import PositionProvider
    from libcst.matchers import Name
    from libcst.matchers import FullyQualifiedName
    from libcst.matchers import Module
    from libcst.testing.utils import data_provider

    for prefix, moves in prefixed_moves:
        for move in moves:
            if isinstance(move, MovedAttribute):
                _test_SixMovesTransformer_with_attributes(prefix, move)
            elif isinstance(move, MovedModule):
                _test_SixMovesTransformer_with_modules(prefix, move)


# Generated at 2022-06-14 02:12:28.584087
# Unit test for constructor of class MovedModule
def test_MovedModule():
    m = MovedModule("foo", "foo")
    assert m.name == "foo"
    assert m.new == "foo"
    m = MovedModule("foo", "foo", "bar")
    assert m.name == "foo"
    assert m.new == "bar"

# Generated at 2022-06-14 02:12:41.391714
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    moved_attribute = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert moved_attribute.name == "cStringIO"
    assert moved_attribute.new_mod == "io"
    assert moved_attribute.new_attr == "StringIO"

    moved_attribute = MovedAttribute("reload_module", "__builtin__", "importlib", "reload")
    assert moved_attribute.name == "reload_module"
    assert moved_attribute.new_mod == "importlib"
    assert moved_attribute.new_attr == "reload"

    moved_attribute = MovedAttribute("getstatusoutput", "commands", "subprocess")
    assert moved_attribute.name == "getstatusoutput"
    assert moved_attribute.new_mod == "subprocess"
    assert moved_attribute

# Generated at 2022-06-14 02:12:45.448656
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    move = MovedAttribute("filter", "itertools", "builtins", "ifilter", "filter")
    assert move.name == 'filter'
    assert move.new_mod == 'builtins'
    assert move.new_attr == 'filter'

# Generated at 2022-06-14 02:12:53.726276
# Unit test for constructor of class MovedModule
def test_MovedModule():
    move1 = MovedModule("builtins", "__builtin__")
    assert move1.name == "builtins"
    assert move1.new == "builtins"
    assert move1.old == "__builtin__"
    move2 = MovedModule("tkinter", "Tkinter", "tkinter")
    assert move2.name == "tkinter"
    assert move2.new == "tkinter"
    assert move2.old == "Tkinter"

# Unit tests for constructor of class MovedAttribute

# Generated at 2022-06-14 02:12:57.532543
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    test = MovedAttribute('name', 'old_mod', 'new_mod', 'old_attr', 'new_attr')
    assert test.name == "name"
    assert test.new_mod == "new_mod"
    assert test.new_attr == "new_attr"


# Generated at 2022-06-14 02:13:02.940721
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    x = SixMovesTransformer()
    assert (isinstance(x, BaseImportRewrite))

# Unit tests for _get_rewrites function.
# Necessary to test the rewrites attribute of SixMovesTransformer.

# Generated at 2022-06-14 02:13:11.085044
# Unit test for constructor of class MovedModule
def test_MovedModule():
    assert MovedModule('builtins', '') == MovedModule('builtins', '')
    assert MovedModule('builtins', '', 'foo') == MovedModule('builtins', '', 'foo')
    assert MovedModule('builtins', '__builtins__', '') == MovedModule('builtins', '__builtins__', '')
    assert MovedModule('builtins', '__builtins__', 'foo') == MovedModule('builtins', '__builtins__', 'foo')


# Generated at 2022-06-14 02:13:19.811048
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    obj = SixMovesTransformer()
    assert obj.rewrites
    assert obj.dependencies

# Generated at 2022-06-14 02:13:31.609978
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    trans = SixMovesTransformer()
    assert trans.dependencies == ['six']
    assert trans.target == (2, 7)
    assert len(trans.rewrites) == len(set(trans.rewrites))
    assert ('os.getcwd', 'six.moves.getcwd') not in trans.rewrites
    assert ('six.moves.range', 'six.moves.range') in trans.rewrites
    assert ('six.moves.urllib.parse.ParseResult', 'six.moves.ParseResult') in trans.rewrites
    assert ('six.moves.urllib.parse.parse_qs', 'six.moves.parse_qs') in trans.rewrites

# Generated at 2022-06-14 02:13:36.288432
# Unit test for constructor of class MovedModule
def test_MovedModule():
    """Unit test for constructor of class MovedModule.
    """
    mm = MovedModule("builtins", "__builtin__")
    assert mm.name == "builtins"
    assert mm.new == "builtins"
    assert mm.old == "__builtin__"

# Generated at 2022-06-14 02:13:38.350885
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert set(_get_rewrites()) == set(SixMovesTransformer.rewrites)

# Generated at 2022-06-14 02:13:45.067975
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    a = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert a.name == "cStringIO"
    assert a.new_mod == "io"
    assert a.new_attr == "StringIO"

    a = MovedAttribute("cStringIO", "cStringIO", "io")
    assert a.name == "cStringIO"
    assert a.new_mod == "io"
    assert a.new_attr == "cStringIO"

    a = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO", "cStringIO")
    assert a.name == "cStringIO"
    assert a.new_mod == "io"
    assert a.new_attr == "cStringIO"


# Generated at 2022-06-14 02:13:47.363813
# Unit test for constructor of class MovedModule
def test_MovedModule():
    m = MovedModule('hhh', 'ggg', 'kkk')
    assert m.name == 'hhh'
    assert m.new == 'kkk'

# Generated at 2022-06-14 02:13:59.133419
# Unit test for constructor of class MovedModule
def test_MovedModule():
    move1 = MovedModule("builtins", "__builtin__")
    assert move1.name == "builtins"
    assert move1.new == "builtins"
    assert move1.old == "__builtin__"
    move2 = MovedModule("tkinter", "Tkinter")
    assert move2.name == "tkinter"
    assert move2.new == "tkinter"
    assert move2.old == "Tkinter"
    move3 = MovedModule("tkinter.ttk", "tk.ttk")
    assert move3.name == "tkinter.ttk"
    assert move3.new == "tkinter.ttk"
    assert move3.old == "tk.ttk"


# Generated at 2022-06-14 02:14:00.971066
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    transformer = SixMovesTransformer()
    # This test only tests whether transformer is instantiated successfully.
    assert transformer

# Generated at 2022-06-14 02:14:05.718949
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert MovedAttribute("cStringIO", "cStringIO", "io", "StringIO").name == "cStringIO"
    assert MovedAttribute("cStringIO", "cStringIO", "io", "StringIO").new_mod == "io"
    assert MovedAttribute("cStringIO", "cStringIO", "io", "StringIO").new_attr == "StringIO"


# Generated at 2022-06-14 02:14:10.618596
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    m = MovedAttribute("abc", "xyz", "def")
    assert m.name == "abc"
    assert m.new_mod == "def"
    assert m.new_attr == "abc"
    m = MovedAttribute("abc", "xyz", "def", "ghi", "jkl")
    assert m.name == "abc"
    assert m.new_mod == "def"
    assert m.new_attr == "jkl"


# Generated at 2022-06-14 02:14:29.037755
# Unit test for constructor of class MovedModule
def test_MovedModule():
    a = MovedModule('a', 'b')
    assert a.name == 'a'


# Generated at 2022-06-14 02:14:37.602581
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    s = SixMovesTransformer()
    assert s.dependencies == ['six']

    assert ('collections.UserDict', 'six.moves.UserDict') in s.rewrites
    assert ('functools.reduce', 'six.moves.reduce') in s.rewrites
    assert ('subprocess.getstatusoutput', 'six.moves.getstatusoutput') in s.rewrites
    assert ('subprocess.getoutput', 'six.moves.getoutput') in s.rewrites
    assert ('shlex.quote', 'six.moves.shlex_quote') in s.rewrites
    assert ('robotparser', 'six.moves.urllib.robotparser') in s.rewrites

    assert ('urllib.parse', 'six.moves.urllib.parse') in s.rew

# Generated at 2022-06-14 02:14:49.365782
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    from ..tests.test_transforms.test_sixmoves import TestClass
    from ..ast_transforms.sixmoves import SixMovesTransformer, MovedAttribute, MovedModule
    s = TestClass()
    # Test for constructor of class MovedAttribute
    move = MovedAttribute('cStringIO', 'cStringIO', 'io', 'StringIO')
    s.assert_equals(move.name, 'cStringIO')
    s.assert_equals(move.new_mod, 'io')
    s.assert_equals(move.new_attr, 'StringIO')
    # Test for constructor of class MovedModule
    move = MovedModule('builtins', '__builtin__')
    s.assert_equals(move.name, 'builtins')

# Generated at 2022-06-14 02:14:52.862429
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    transformer = SixMovesTransformer()
    assert transformer.rewrites == _get_rewrites()
    assert transformer.dependencies == ['six']

# Generated at 2022-06-14 02:15:00.029510
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert MovedAttribute('name','old',None,None,'new').new_attr == 'new'
    assert MovedAttribute('name','old',None,None).new_attr == 'name'
    assert MovedAttribute('name','old',None,'old').new_attr == 'old'
    assert MovedAttribute('name','old',None,'new').new_attr == 'new'

# Generated at 2022-06-14 02:15:06.452027
# Unit test for constructor of class MovedModule
def test_MovedModule():
    m = MovedModule("name", "old")
    assert m.name == "name"
    assert m.old == "old"
    assert m.new == "name"

    m = MovedModule("name", "old", "new")
    assert m.name == "name"
    assert m.old == "old"
    assert m.new == "new"



# Generated at 2022-06-14 02:15:13.172535
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    move = MovedAttribute("HTTPError", "urllib2", "urllib.error")
    assert move.name == "HTTPError"
    assert move.new_mod == "urllib.error"
    assert move.new_attr == "HTTPError"
    assert move.old_mod is None
    assert move.old_attr is None

# Generated at 2022-06-14 02:15:15.075114
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert list(SixMovesTransformer.rewrites)



# Generated at 2022-06-14 02:15:19.192897
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    move_attribute = MovedAttribute("a", "aa", "aaa", "aaa", "aaaa")
    assert move_attribute.name == "a"
    assert move_attribute.new_mod == "aaa"
    assert move_attribute.new_attr == "aaaa"


# Generated at 2022-06-14 02:15:24.383139
# Unit test for constructor of class MovedModule
def test_MovedModule():
    mm = MovedModule("name", "old")
    assert mm.name == "name"
    assert mm.new == "name"

    mm = MovedModule("name", "old", "new")
    assert mm.name == "name"
    assert mm.new == "new"

