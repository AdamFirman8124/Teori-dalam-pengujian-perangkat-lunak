

# Generated at 2022-06-14 02:05:58.636447
# Unit test for constructor of class MovedModule
def test_MovedModule():
    good_test = MovedModule("name", "old")
    assert good_test.name == "name"
    assert good_test.old == "old"
    assert good_test.new == "name"

    bad_test = MovedModule("name", "old", "new")
    assert bad_test.name == "name"
    assert bad_test.old == "old"
    assert bad_test.new == "new"

# Generated at 2022-06-14 02:06:12.004403
# Unit test for constructor of class MovedModule
def test_MovedModule():
    moved_module_one = MovedModule('tkinter', 'Tkinter')
    assert moved_module_one.name == 'tkinter'
    assert moved_module_one.old == 'Tkinter'
    assert moved_module_one.new == 'tkinter'
    moved_module_two = MovedModule('tkinter', 'Tkinter', 'tkinter')
    assert moved_module_two.name == 'tkinter'
    assert moved_module_two.old == 'Tkinter'
    assert moved_module_two.new == 'tkinter'
    moved_module_three = MovedModule('abcd', 'abcd')
    assert moved_module_three.name == 'abcd'
    assert moved_module_three.old == 'abcd'
    assert moved_module_three.new == 'abcd'

# Generated at 2022-06-14 02:06:13.793549
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    MovedAttribute("cStringIO", "cStringIO", "io", "StringIO", "StringIO")

# Generated at 2022-06-14 02:06:22.341709
# Unit test for constructor of class MovedModule
def test_MovedModule():
    moved_module = MovedModule('name', 'old')
    assert moved_module.name == 'name'
    assert moved_module.old == 'old'
    assert moved_module.new == 'name'

    moved_module = MovedModule('name', 'old', 'new')
    assert moved_module.name == 'name'
    assert moved_module.old == 'old'
    assert moved_module.new == 'new'

    moved_module = MovedModule('name', new='new')
    assert moved_module.old == 'name'
    assert moved_module.new == 'new'



# Generated at 2022-06-14 02:06:27.337444
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert SixMovesTransformer().target == (2, 7)  # copied from the class
    assert len(SixMovesTransformer().rewrites) == len(_get_rewrites())
    assert list(SixMovesTransformer().rewrites)[0] == ('subprocess.getstatusoutput')
    assert len(SixMovesTransformer().dependencies) == 1
    assert SixMovesTransformer().dependencies[0] == 'six'

# Generated at 2022-06-14 02:06:29.619299
# Unit test for constructor of class MovedModule
def test_MovedModule():
    MovedModule("builtins", "__builtin__")

# Generated at 2022-06-14 02:06:38.368545
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert MovedAttribute('cStringIO', 'cStringIO', 'io', 'StringIO').new_attr == 'StringIO'
    assert MovedAttribute('cStringIO', 'cStringIO', 'io', old_attr='StringIO').new_attr == 'StringIO'
    assert MovedAttribute('cStringIO', 'cStringIO', 'io', new_attr='StringIO').new_attr == 'StringIO'
    assert MovedAttribute('cStringIO', 'cStringIO', 'io', old_attr='StringIO', new_attr='StringIO').new_attr == 'StringIO'
    assert MovedAttribute('cStringIO', 'cStringIO', 'io').new_attr == 'cStringIO'
    assert MovedAttribute('cStringIO', 'cStringIO', 'io', 'StringIO').name == 'cStringIO'

# Generated at 2022-06-14 02:06:45.315537
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    mv_attr = MovedAttribute('new_name',
                             'new_mod',
                             'old_mod',
                             'old_attr',
                             'new_attr')

    assert mv_attr.name == 'new_name'
    assert mv_attr.new_mod == 'new_mod'
    assert mv_attr.new_attr == 'new_attr'


# Generated at 2022-06-14 02:06:55.583337
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    _get_rewrites()
# _get_rewrites has side effect that creates SixMovesTransformer.rewrites:
    for prefix, moves in prefixed_moves:
        for move in moves:
            if isinstance(move, MovedAttribute):
                path = '{}.{}'.format(move.new_mod, move.new_attr)
                yield (path, 'six.moves{}.{}'.format(prefix, move.name))
            elif isinstance(move, MovedModule):
                yield (move.new, 'six.moves{}.{}'.format(prefix, move.name))
    assert SixMovesTransformer.rewrites == _get_rewrites()

# Generated at 2022-06-14 02:07:00.112227
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    new_attr = MovedAttribute("Integer", "__builtin__", "sys")
    assert new_attr.name == "Integer"
    assert new_attr.new_mod == "sys"
    assert new_attr.new_attr == "Integer"

# Generated at 2022-06-14 02:07:10.473512
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    """Function to test SixMovesTransformer."""
    # pylint: disable=W0612, W0613
    from lib2to3.pgen2 import token
    from lib2to3 import pytree, fixer_base
    from libfuturize.fixes.fix_six_moves import SixMovesTransformer
    # dummy syntax tree
    a = pytree.Node(syms.simple_stmt, [pytree.Leaf(token.NAME, u'b')])
    b = pytree.Node(syms.trailer, [pytree.Leaf(token.DOT, u'.'),
                                   pytree.Leaf(token.NAME, u'c')])
    c = pytree.Node(syms.power, [a, b])

# Generated at 2022-06-14 02:07:22.768127
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    """Test SixMovesTransformer."""
    transformer = SixMovesTransformer("", "", "", "", "")

# Generated at 2022-06-14 02:07:35.364629
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    moved = MovedAttribute("name", "old_mod", "new_mod", "old_attr", "new_attr")
    assert moved.name == "name"
    assert moved.new_mod == "new_mod"
    assert moved.new_attr == "new_attr"
    moved = MovedAttribute("name", "old_mod", "new_mod", "old_attr")
    assert moved.name == "name"
    assert moved.new_mod == "new_mod"
    assert moved.new_attr == "old_attr"
    moved = MovedAttribute("name", "old_mod", "new_mod")
    assert moved.name == "name"
    assert moved.new_mod == "new_mod"
    assert moved.new_attr == "name"

# Generated at 2022-06-14 02:07:40.598267
# Unit test for constructor of class MovedModule
def test_MovedModule():
    a = MovedModule('abc', 'xyz')
    assert a.name == 'abc'
    assert a.old == 'xyz' and a.new == 'abc'
    a = MovedModule('abc', 'xyz', 'pqr')
    assert a.name == 'abc'
    assert a.old == 'xyz' and a.new == 'pqr'
    

# Generated at 2022-06-14 02:07:53.663809
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    import ast
    import sys
    from .. import utils
    from .. import transforms

    with utils.tempdir() as d:
        d.gen('__init__.py')
        d.gen('six.py', "")
        d.gen('spam.py',
              """\
from six.moves import cStringIO
import six.moves.urllib.parse
from six.moves.urllib.request import urlopen
import six.moves.urllib.response
import six.moves.urllib.robotparser

print('spam.py:', cStringIO, six.moves.urllib.parse, urlopen,
      six.moves.urllib.response, six.moves.urllib.robotparser)
""")

# Generated at 2022-06-14 02:08:04.143451
# Unit test for constructor of class MovedModule
def test_MovedModule():
    moved_module = MovedModule('builtins', '__builtin__')
    assert moved_module.name == 'builtins'
    assert moved_module.new == 'builtins'
    assert moved_module.old == '__builtin__'
    moved_module = MovedModule('builtins', '__builtin__', 'builtins')
    assert moved_module.name == 'builtins'
    assert moved_module.new == 'builtins'
    assert moved_module.old == '__builtin__'
    moved_module = MovedModule('builtins', '__builtin__', '__builtin__')
    assert moved_module.name == 'builtins'
    assert moved_module.new == '__builtin__'
    assert moved_module.old == '__builtin__'



# Generated at 2022-06-14 02:08:08.650681
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    test = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert test.name == "cStringIO"
    assert test.new_mod == "io"
    assert test.new_attr == "StringIO"


# Generated at 2022-06-14 02:08:10.953467
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    trns = SixMovesTransformer()
    assert trns.rewrites == _get_rewrites()
    assert trns.dependencies == ['six']

# Generated at 2022-06-14 02:08:19.245828
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    for prefix, moves in prefixed_moves:
        for move in moves:
            if isinstance(move, MovedAttribute):
                path = '{}.{}'.format(move.new_mod, move.new_attr)
                assert path in SixMovesTransformer.rewrites
                assert SixMovesTransformer.rewrites[path] == 'six.moves{}.{}'.format(prefix, move.name)
            elif isinstance(move, MovedModule):
                new = move.new
                assert new in SixMovesTransformer.rewrites
                assert SixMovesTransformer.rewrites[new] == 'six.moves{}.{}'.format(prefix, move.name)

# Generated at 2022-06-14 02:08:31.228975
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    t = SixMovesTransformer()

# Generated at 2022-06-14 02:08:35.477065
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    from .base import BaseRewrite

    assert issubclass(SixMovesTransformer, BaseRewrite)

# Generated at 2022-06-14 02:08:37.100428
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    SixMovesTransformer()

# Generated at 2022-06-14 02:08:40.085594
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert MovedAttribute("xrange", "__builtin__", "builtins", "xrange", "range").__dict__ == {'name': 'xrange', 'new_mod': 'builtins', 'new_attr': 'range'}

# Generated at 2022-06-14 02:08:54.307667
# Unit test for constructor of class MovedModule
def test_MovedModule():
    test_data = [['a', 'b'], ['a', 'b', 'c'], [], ['a']]
    for test_datum in test_data:
        if len(test_datum) == 1:
            assert MovedModule(*test_datum).name == 'a', 'incorrect name'
            assert MovedModule(*test_datum).new == 'a', 'incorrect old'
        if len(test_datum) == 2:
            assert MovedModule(*test_datum).name == 'a', 'incorrect name'
            assert MovedModule(*test_datum).new == 'b', 'incorrect new'
        if len(test_datum) == 0:
            assert MovedModule(*test_datum) == 0, 'incorrect length'

# Generated at 2022-06-14 02:08:57.450981
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    move = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")

    assert move.name == "cStringIO"
    assert move.new_mod == "io"
    assert move.new_attr == "StringIO"


# Generated at 2022-06-14 02:09:06.524013
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    move = MovedAttribute('name', 'old_mod', 'new_mod', 'old_attr', 'new_attr')
    assert move.name == 'name'
    assert move.new_mod == 'new_mod'
    assert move.new_attr == 'new_attr'

    move2 = MovedAttribute('name2', 'old_mod', 'new_mod')
    assert move2.name == 'name2'
    assert move2.new_mod == 'new_mod'
    assert move2.new_attr == 'name2'

    move3 = MovedAttribute('name3', 'old_mod', 'new_mod', 'old_attr')
    assert move3.name == 'name3'
    assert move3.new_mod == 'new_mod'
    assert move3.new_attr == 'old_attr'

# Generated at 2022-06-14 02:09:19.431692
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    move1 = MovedAttribute('name', 'old_mod', 'new_mod')
    assert move1.name == 'name'
    assert move1.new_mod == 'new_mod'
    assert move1.new_attr == 'name'
    move2 = MovedAttribute('name', 'old_mod', 'new_mod', 'old_attr')
    assert move2.name == 'name'
    assert move2.new_mod == 'new_mod'
    assert move2.new_attr == 'old_attr'
    move3 = MovedAttribute('name', 'old_mod', 'new_mod', 'old_attr', 'new_attr')
    assert move3.name == 'name'
    assert move3.new_mod == 'new_mod'
    assert move3.new_attr == 'new_attr'


# Generated at 2022-06-14 02:09:24.172987
# Unit test for constructor of class MovedModule
def test_MovedModule():
    temp = MovedModule("winreg", "_winreg")
    assert temp.name == "winreg"
    assert temp.new == "winreg"
    assert temp.old == "_winreg"


# Generated at 2022-06-14 02:09:29.746629
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert SixMovesTransformer.rewrites == _get_rewrites()
    assert SixMovesTransformer.dependencies == ['six']
    assert _get_rewrites()[0] == ('builtins.filter', 'six.moves.filter')
    assert _get_rewrites()[5] == ('builtins.range', 'six.moves.range')

# Generated at 2022-06-14 02:09:33.272723
# Unit test for constructor of class MovedModule
def test_MovedModule():
    mm = MovedModule("new_name", "old")
    assert mm.name == "new_name"
    assert mm.new == "new_name"


# Generated at 2022-06-14 02:09:38.694888
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    moved_attribute = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert moved_attribute.new_attr == "StringIO"
    assert moved_attribute.new_mod == "io"

# Generated at 2022-06-14 02:09:40.139529
# Unit test for constructor of class MovedModule
def test_MovedModule():
    assert MovedModule("test", "Test", "test").new == "test"

# Generated at 2022-06-14 02:09:50.408990
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    mp1 = MovedAttribute('cStringIO', 'cStringIO', 'io', 'StringIO')
    assert mp1._name == 'cStringIO'
    assert mp1.old_mod == 'cStringIO'
    assert mp1.new_mod == 'io'
    assert mp1.old_attr == 'StringIO'
    assert mp1.new_attr == 'cStringIO'

    mp2 = MovedAttribute('input', '__builtin__', 'builtins', 'raw_input', 'input')
    assert mp2._name == 'input'
    assert mp2.old_mod == '__builtin__'
    assert mp2.new_mod == 'builtins'
    assert mp2.old_attr == 'raw_input'
    assert mp2.new_attr == 'input'



# Generated at 2022-06-14 02:09:54.674788
# Unit test for constructor of class MovedModule
def test_MovedModule():
    movedModule = MovedModule("urllib_robotparser", __name__ + ".moves.urllib_robotparser",
                              "urllib.robotparser")
    assert movedModule.name == "urllib_robotparser"
    assert movedModule.new == "urllib.robotparser"
    assert movedModule.old == __name__ + ".moves.urllib_robotparser"


# Generated at 2022-06-14 02:10:08.244410
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    obj = SixMovesTransformer()
    assert obj.target == (2, 7)

# Generated at 2022-06-14 02:10:17.395401
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    t = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert t.name == "cStringIO"
    assert t.new_mod == "io"
    assert t.new_attr == "StringIO"
    t = MovedAttribute("cStringIO", "cStringIO", "io")
    assert t.name == "cStringIO"
    assert t.new_mod == "io"
    assert t.new_attr == "cStringIO"


# test SixMovesTransformer.rewrites
from lib2to3.fixes.fix_import import FixImport
from lib2to3 import pytree
from lib2to3.pgen2 import token
import textwrap



# Generated at 2022-06-14 02:10:22.142950
# Unit test for constructor of class MovedModule
def test_MovedModule():
    class_MovedModule = MovedModule('name', 'old', 'new')
    assert class_MovedModule.name == 'name'
    assert class_MovedModule.old == 'old'
    assert class_MovedModule.new == 'new'

# Generated at 2022-06-14 02:10:27.492114
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    attr = MovedAttribute("name", "mod", "new_mod", "attribute", "new_attr")

    assert attr.name == "name"
    assert attr.new_mod == "new_mod"
    assert attr.new_attr == "new_attr"


# Generated at 2022-06-14 02:10:29.110967
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    from six import moves
    assert moves.filter is filter
    assert moves.reduce is functools.reduce

# Generated at 2022-06-14 02:10:31.426459
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert SixMovesTransformer.rewrites == _get_rewrites()

# Generated at 2022-06-14 02:10:40.868464
# Unit test for constructor of class MovedModule
def test_MovedModule():
    test1 = MovedModule("builtins", "__builtin__")
    assert test1.name == "builtins"
    assert test1.new == "builtins"

    test2 = MovedModule("urllib.request", "urllib2")
    assert test2.name == "urllib.request"
    assert test2.new == "urllib.request"


# Generated at 2022-06-14 02:10:48.014886
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    MovedAttribute("cStringIO", "cStringIO", "io")
    MovedAttribute("cStringIO", "cStringIO", None)
    MovedAttribute("cStringIO", None, "io")
    MovedAttribute("cStringIO", None, None)


# Generated at 2022-06-14 02:10:52.570010
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    value = MovedAttribute("A", "B", "C", "D", "E")

    assert value.name == "A"
    assert value.new_mod == "B"
    assert value.new_attr == "E"

# Generated at 2022-06-14 02:10:59.507045
# Unit test for constructor of class MovedModule
def test_MovedModule():
    move = MovedModule('unicodedata', 'unicodedata')
    assert move.name == 'unicodedata'
    assert move.new == 'unicodedata'
    move = MovedModule('unicodedata', 'unicodedata', 'unicodedata')
    assert move.name == 'unicodedata'
    assert move.new == 'unicodedata'


# Generated at 2022-06-14 02:11:02.851727
# Unit test for constructor of class MovedModule
def test_MovedModule():
    assert MovedModule('name', 'old', 'new') == MovedModule('name', 'old', 'new')
    assert MovedModule('name', 'old') == MovedModule('name', 'old', 'name')

# Generated at 2022-06-14 02:11:16.901442
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    a = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert a.name == "cStringIO"
    assert a.new_mod == "io"
    assert a.new_attr == "StringIO"

    b = MovedAttribute("cStringIO")
    assert b.name == "cStringIO"
    assert b.new_mod == "cStringIO"
    assert b.new_attr == "cStringIO"

    c = MovedAttribute("cStringIO", "cStringIO", "io")
    assert c.name == "cStringIO"
    assert c.new_mod == "io"
    assert c.new_attr == "cStringIO"

    d = MovedAttribute("cStringIO", new_attr="StringIO")

# Generated at 2022-06-14 02:11:21.835891
# Unit test for constructor of class MovedModule
def test_MovedModule():
    mod = MovedModule("builtins", "__builtin__")
    assert mod.name == "builtins"
    assert mod.new == "builtins"
    mod2 = MovedModule("builtins", "__builtin__", "builtins")
    assert mod2.name == "builtins"
    assert mod2.new == "builtins"


# Generated at 2022-06-14 02:11:31.638154
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    # Dummy function to run the test
    def f():
        MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    # Test for missing attribute
    try:
        MovedAttribute("cStringIO", "cStringIO", "io")
    except AssertionError:
        pass
    else:
        raise AssertionError('missing attr name should raise')
    # Test for non missing attribute
    try:
        f()
    except AssertionError:
        raise AssertionError('attr name should not raise')
    else:
        pass

# Generated at 2022-06-14 02:11:34.175888
# Unit test for constructor of class MovedModule
def test_MovedModule():
    movedModule = MovedModule('runpy', 'runpy')
    assert movedModule.name == 'runpy' and movedModule.new == 'runpy'



# Generated at 2022-06-14 02:11:38.024064
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    from ..fixes import SixMovesTransformer
    test_string = "import os"
    expected_string = "import six.moves.os"
    assert SixMovesTransformer().transform_string(test_string) == expected_string

# Generated at 2022-06-14 02:11:45.091465
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    SixMovesTransformer()

# Generated at 2022-06-14 02:11:49.408783
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    t = SixMovesTransformer()
    for path, new in _get_rewrites():
        assert t.rewrites[path] == new
    assert list(t.rewrites)[0] == 'urllib.parse.ParseResult'



# Generated at 2022-06-14 02:11:58.690016
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    with pytest.raises(TypeError):
        MovedAttribute()
    with pytest.raises(TypeError):
        MovedAttribute('name')
    with pytest.raises(TypeError):
        MovedAttribute('name', 'old_mod')
    ma = MovedAttribute('name', 'old_mod', 'new_mod')
    assert ma.name == 'name'
    assert ma.new_mod == 'new_mod'
    assert ma.new_attr == 'name'
    ma = MovedAttribute('name', 'old_mod', 'new_mod', 'old_attr')
    assert ma.name == 'name'
    assert ma.new_mod == 'new_mod'
    assert ma.new_attr == 'old_attr'

# Generated at 2022-06-14 02:12:09.954213
# Unit test for constructor of class MovedModule
def test_MovedModule():
    class SubClass(MovedModule):
        """Subclass of MovedModule for testing."""
        pass
    test_cases = [
        (SubClass('a', 'b', 'c'), 'b', 'a'),
        (SubClass('a', 'b'), 'b', 'a'),
        (SubClass('a', 'a', 'd'), 'a', 'd'),
        (SubClass('a', 'a'), 'a', 'a'),
        (SubClass('a', None, 'c'), 'a', 'c'),
        (SubClass('a', None), 'a', 'a'),
    ]
    for test_case in test_cases:
        mod, expected_old, expected_new = test_case
        assert mod.name == expected_new
        assert mod.new == expected_new
        assert mod.old == expected_

# Generated at 2022-06-14 02:12:11.624572
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert len(_get_rewrites()) == 55

# Generated at 2022-06-14 02:12:23.720413
# Unit test for constructor of class SixMovesTransformer

# Generated at 2022-06-14 02:12:28.700715
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert tuple(SixMovesTransformer.get_rewrites()) == SixMovesTransformer.rewrites


if __name__ == '__main__':
    # Test Code
    SixMovesTransformer.run_main()

# Generated at 2022-06-14 02:12:41.418801
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    old_mod, new_mod, old_attr, new_attr, name = 'old_mod', 'new_mod', 'old_attr', 'new_attr', 'name'
    ma1 = MovedAttribute(name, old_mod, new_mod, old_attr, new_attr)
    ma2 = MovedAttribute(name, old_mod)
    ma3 = MovedAttribute(name, old_mod, new_mod, old_attr)
    assert ma1.name == ma2.name == ma3.name == name
    assert ma1.new_mod == ma2.new_mod == ma3.new_mod == new_mod
    assert ma1.new_attr == ma2.new_attr == ma3.new_attr == new_attr
    assert ma2.new_attr == name
    assert ma3.new_

# Generated at 2022-06-14 02:12:46.209420
# Unit test for constructor of class MovedModule
def test_MovedModule():
    mm = MovedModule('name', 'old')
    assert mm.name == 'name'
    assert mm.old == 'old'
    assert mm.new == 'name'

    mm = MovedModule('name', 'old', new='new')
    assert mm.name == 'name'
    assert mm.old == 'old'
    assert mm.new == 'new'



# Generated at 2022-06-14 02:12:55.534784
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    moved_attr = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert moved_attr.name == "cStringIO"
    assert moved_attr.new_mod == "io"
    assert moved_attr.new_attr == "StringIO"

    moved_attr = MovedAttribute("input", "__builtin__", "builtins", "raw_input", "input")
    assert moved_attr.name == "input"
    assert moved_attr.new_mod == "builtins"
    assert moved_attr.new_attr == "input"

    moved_attr = MovedAttribute("intern", "__builtin__", "sys")
    assert moved_attr.name == "intern"
    assert moved_attr.new_mod == "sys"

# Generated at 2022-06-14 02:13:12.026496
# Unit test for constructor of class MovedModule
def test_MovedModule():
    assert MovedModule('name', 'old').name == 'name'
    assert MovedModule('name', 'old').new == 'name'
    assert MovedModule('name', 'old', 'new').name == 'name'
    assert MovedModule('name', 'old', 'new').new == 'new'


# Generated at 2022-06-14 02:13:24.672333
# Unit test for constructor of class MovedModule
def test_MovedModule():
    obj1 = MovedModule('builtins', '__builtin__')
    assert obj1.name == 'builtins'
    assert obj1.old == '__builtin__'
    assert obj1.new == 'builtins'
    obj1 = MovedModule('configparser', 'ConfigParser')
    assert obj1.name == 'configparser'
    assert obj1.old == 'ConfigParser'
    assert obj1.new == 'configparser'
    obj1 = MovedModule('queue', 'Queue')
    assert obj1.name == 'queue'
    assert obj1.old == 'Queue'
    assert obj1.new == 'queue'
    obj1 = MovedModule('copyreg', 'copy_reg', 'copyreg')
    assert obj1.name == 'copyreg'

# Generated at 2022-06-14 02:13:26.453799
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    transformer = SixMovesTransformer()
    assert transformer.dependencies == ['six']

# Generated at 2022-06-14 02:13:30.299944
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    move = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert move.name == "cStringIO"
    assert move.new_mod == "io"
    assert move.new_attr == "StringIO"

# Generated at 2022-06-14 02:13:34.166155
# Unit test for constructor of class MovedModule
def test_MovedModule():
    test_MovedModule = MovedModule("builtins", "__builtin__")
    assert isinstance(test_MovedModule, MovedModule)

# Generated at 2022-06-14 02:13:38.271701
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    move = MovedAttribute('cStringIO', 'cStringIO', 'io', 'StringIO')
    assert move.name == 'cStringIO'
    assert move.new_mod == 'io'
    assert move.new_attr == 'cStringIO'

# Generated at 2022-06-14 02:13:47.014591
# Unit test for constructor of class MovedModule
def test_MovedModule():
    monkeypatch = MonkeyPatch()
    try:
        assert MovedModule('monkey', 'monkey1', 'monkey2') == MovedModule('monkey', 'monkey1', 'monkey2')
        assert MovedModule('monkey', 'monkey1') == MovedModule('monkey', 'monkey1', 'monkey')
        assert MovedModule('monkey1', 'monkey2') != MovedModule('monkey2', 'monkey1')
        # monkeypatch.setattr(MovedModule.__init__, 'name', 'monkey')
        # assert MovedModule('monkey', 'monkey1', 'monkey2') == MovedModule('monkey', 'monkey1')
    finally:
        monkeypatch.undo()



# Generated at 2022-06-14 02:13:51.611391
# Unit test for constructor of class MovedModule
def test_MovedModule():
    original_module_name = 'module'
    replacement_module_name = 'module2'
    mod = MovedModule(original_module_name, replacement_module_name)
    # assert that the correct attributes were set
    assert mod.new == replacement_module_name
    assert mod.name == original_module_name


# Generated at 2022-06-14 02:13:59.866562
# Unit test for constructor of class MovedModule
def test_MovedModule():
    assert MovedModule("name", "old") == MovedModule("name", "old")
    assert MovedModule("name", "old", "new") == MovedModule("name", "old", "new")
    assert MovedModule("name", "old", None) == MovedModule("name", "old")
    assert MovedModule("name", "old") == MovedModule("name", "old", None)
    assert MovedModule("name", "old", "new") != MovedModule("name", "old")
    assert MovedModule("name", "old") != MovedModule("name", "old", "new")
    assert MovedModule("name", "old") != MovedModule("name1", "old", "new")
    assert MovedModule("name", "old") != MovedModule("name1", "old")

# Generated at 2022-06-14 02:14:02.814200
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    from .test_utils import module_test
    testmod = """
    from six.moves.tkinter import tkinter
    """
    module_test(testmod, SixMovesTransformer)

# Generated at 2022-06-14 02:14:37.419834
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert len(_get_rewrites()) == len(_moved_attributes) + len(_urllib_parse_moved_attributes) + len(_urllib_error_moved_attributes) + len(_urllib_request_moved_attributes) + len(_urllib_response_moved_attributes) + len(_urllib_robotparser_moved_attributes)
    assert list(_get_rewrites())[0] == ('filter', 'six.moves.filter')
    assert list(_get_rewrites())[-1] == ('robotparser.RobotFileParser', 'six.moves.urllib.robotparser.RobotFileParser')

# Generated at 2022-06-14 02:14:42.895982
# Unit test for constructor of class MovedModule
def test_MovedModule():
    assert MovedModule('X', 'Y').name == 'X'
    assert MovedModule('X', 'Y').new == 'Y'
    assert MovedModule('X', 'Y').old is None
    assert MovedModule('X', 'Y', 'Z').old == 'Z'



# Generated at 2022-06-14 02:14:54.596616
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    from .. import FixerTestCase
    from ..fixer_util import Name, Call

    class Test(FixerTestCase):
        fixer = "sixmoves"

        def test_normal(self):
            b = "from foo import bar and baz"
            a = "from six.moves import foo"
            self.check(b, a)

        def test_multiple(self):
            b = "from foo import bar and baz, biz and boz"
            a = "from six.moves import foo, biz"
            self.check(b, a)

        def test_empty_name(self):
            b = "from . import bar and baz"
            a = "from six.moves import"
            self.check(b, a)


# Generated at 2022-06-14 02:15:06.648350
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    class TestMovedAttribute(MovedAttribute):
        def __init__(self, name, old_mod, new_mod, old_attr=None, new_attr=None):
            super().__init__(name, old_mod, new_mod, old_attr, new_attr)
            self.old_mod = old_mod
            self.new_mod = new_mod
            self.old_attr = old_attr
            self.new_attr = new_attr
    testMovedAttribute1 = TestMovedAttribute('test1', 'test_old_mod', 'test_new_mod', 'test_old_attr', 'test_new_attr')
    assert testMovedAttribute1.name == 'test1'
    assert testMovedAttribute1.old_mod == 'test_old_mod'
    assert testMovedAttribute1

# Generated at 2022-06-14 02:15:16.383494
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    from .base import BaseImportRewrite

    from ..utils import PY35
    from ..utils.helpers import eager

    assert isinstance(SixMovesTransformer, BaseImportRewrite)
    assert isinstance(SixMovesTransformer, type)
    assert SixMovesTransformer.target == (2, 7)
    assert SixMovesTransformer.dependencies == ['six']
    if PY35:
        assert sorted(SixMovesTransformer.rewrites.items()) == sorted(_get_rewrites().items())
    else:
        assert sorted(list(SixMovesTransformer.rewrites)) == sorted(list(_get_rewrites()))
    assert SixMovesTransformer.__name__ == 'SixMovesTransformer'
    assert SixMovesTransformer.__qualname__ == 'SixMovesTransformer'

# Generated at 2022-06-14 02:15:25.383616
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    x = MovedAttribute("name", "old_mod", "new_mod", "old_attr", "new_attr")
    assert x.name == "name"
    assert x.new_mod == "new_mod"
    assert x.new_attr == "new_attr"
    x = MovedAttribute("name", "old_mod", "new_mod", "old_attr")
    assert x.new_attr == "old_attr"
    x = MovedAttribute("name", "old_mod", "new_mod")
    assert x.new_attr == "name"



# Generated at 2022-06-14 02:15:32.537843
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    obj = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert obj.name == "cStringIO"
    assert obj.old_mod == "cStringIO"
    assert obj.new_mod == "io"
    assert obj.old_attr == "StringIO"
    assert obj.new_attr == "StringIO"


# Generated at 2022-06-14 02:15:42.235336
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    move = MovedAttribute("attr", "a", "b", "x", "y")
    assert move.name == 'attr'
    assert move.new_mod == 'b'
    assert move.new_attr == 'y'

    move = MovedAttribute("attr", "a", "b", "x")
    assert move.name == 'attr'
    assert move.new_mod == 'b'
    assert move.new_attr == 'x'

    move = MovedAttribute("attr", "a", "b")
    assert move.name == 'attr'
    assert move.new_mod == 'b'
    assert move.new_attr == 'attr'


# Generated at 2022-06-14 02:15:45.818000
# Unit test for constructor of class MovedModule
def test_MovedModule():
    mm = MovedModule('builtins', '__builtin__')
    assert mm.name == 'builtins'
    assert mm.new == 'builtins'
    assert mm.old == '__builtin__'


# Generated at 2022-06-14 02:15:54.463481
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    for prefix, moves in prefixed_moves:
        for move in moves:
            if isinstance(move, MovedAttribute):
                # Test move.new_mod
                if move.new_mod is None:
                    assert move.new_mod == move.name
                # Test move.new_attr
                if move.new_attr is None:
                    assert move.new_attr == move.name
                if move.new_attr is None and move.old_attr is not None:
                    assert move.new_attr == move.old_attr