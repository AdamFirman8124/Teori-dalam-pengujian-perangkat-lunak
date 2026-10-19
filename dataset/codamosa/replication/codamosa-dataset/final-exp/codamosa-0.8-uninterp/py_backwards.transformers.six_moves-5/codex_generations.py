

# Generated at 2022-06-14 02:05:58.946875
# Unit test for constructor of class SixMovesTransformer

# Generated at 2022-06-14 02:05:59.923193
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert type(SixMovesTransformer.rewrites) == list


# Generated at 2022-06-14 02:06:13.455679
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert(SixMovesTransformer.target == (2, 7))
    assert(SixMovesTransformer.dependencies == ['six'])
    assert(len(SixMovesTransformer.rewrites) == 266)
    assert(SixMovesTransformer.rewrites[0][0] == 'builtins.filter')
    assert(SixMovesTransformer.rewrites[0][1] == 'six.moves.filter')
    assert(SixMovesTransformer.rewrites[1][0] == 'builtins.input')
    assert(SixMovesTransformer.rewrites[1][1] == 'six.moves.input')
    assert(SixMovesTransformer.rewrites[2][0] == 'builtins.map')

# Generated at 2022-06-14 02:06:17.209198
# Unit test for constructor of class MovedModule
def test_MovedModule():
    module = MovedModule("name", "old", "new")
    assert module.name == "name"
    assert module.old == "old"
    assert module.new == "new"

# Unit tests for constructor of class MovedAttribute

# Generated at 2022-06-14 02:06:26.709240
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    translator = SixMovesTransformer()
    assert translator.target == (2, 7)

# Generated at 2022-06-14 02:06:31.547692
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert MovedAttribute('cStringIO', 'cStringIO', 'io', 'StringIO') == MovedAttribute('cStringIO', 'cStringIO', 'io', 'StringIO')


# Generated at 2022-06-14 02:06:33.645059
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert SixMovesTransformer.rewrites == _get_rewrites()
    assert 'six' in SixMovesTransformer.dependencies

# Generated at 2022-06-14 02:06:38.014064
# Unit test for constructor of class MovedModule
def test_MovedModule():
    assert MovedModule('tkinter', 'Tkinter').__dict__ == {'name': 'tkinter', 'old': 'Tkinter', 'new': 'tkinter'}
    assert MovedModule('tkinter', 'Tkinter', 'tkinter.name').__dict__ == {'name': 'tkinter', 'old': 'Tkinter', 'new': 'tkinter.name'}


# Generated at 2022-06-14 02:06:41.445393
# Unit test for constructor of class MovedModule
def test_MovedModule():
    mvmd = MovedModule("name", "old")
    assert mvmd.name == "name" and mvmd.old == "old" and mvmd.new == "name"
    mvmd = MovedModule("name", "old", "new")
    assert mvmd.name == "name" and mvmd.old == "old" and mvmd.new == "new"


# Generated at 2022-06-14 02:06:43.430327
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    import pytest
    with pytest.raises(TypeError):
        MovedAttribute()



# Generated at 2022-06-14 02:06:52.372835
# Unit test for constructor of class SixMovesTransformer

# Generated at 2022-06-14 02:06:58.781066
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert isinstance(SixMovesTransformer, object)


if __name__ == "__main__":
    import pytest
    pytest.main(str(__file__.replace('\\', '/')) + ' -v')

# Generated at 2022-06-14 02:07:01.107482
# Unit test for constructor of class MovedModule
def test_MovedModule():
    mm = MovedModule("a", "b")
    assert mm.name == "a"
    assert mm.new == mm.name

# Generated at 2022-06-14 02:07:03.564161
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    transformer = SixMovesTransformer(None)
    assert transformer.dependencies == ['six']
    assert transformer.rewrites == _get_rewrites()



# Generated at 2022-06-14 02:07:05.911223
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    p = SixMovesTransformer()
    assert p.target == (2, 7)
    assert p.rewrites == _get_rewrites()
    assert p.dependencies == ['six']

# Generated at 2022-06-14 02:07:13.037413
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    a = MovedAttribute('name', 'mod', 'new')
    assert a.name == 'name'
    assert a.new_mod == 'new'
    assert a.new_attr == 'name'
    assert repr(a) == 'MovedAttribute(name, mod, new, name, name)'



# Generated at 2022-06-14 02:07:28.878735
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer(): # pylint: disable=invalid-name
    rewrites = list(SixMovesTransformer.rewrites)

# Generated at 2022-06-14 02:07:41.723178
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    m = MovedAttribute('a', 'b', 'c')
    assert m.name == 'a'
    assert m.new_mod == 'c'
    assert m.new_attr == 'a'
    m = MovedAttribute('a', 'b', 'c', 'd', 'e')
    assert m.name == 'a'
    assert m.new_mod == 'c'
    assert m.new_attr == 'e'
    m = MovedAttribute('a', 'b', 'c', 'd', None)
    assert m.name == 'a'
    assert m.new_mod == 'c'
    assert m.new_attr == 'd'
    m = MovedAttribute('a', 'b', None, 'd', 'e')
    assert m.name == 'a'
    assert m.new_mod

# Generated at 2022-06-14 02:07:54.811272
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    import ast
    from transform.six_moves import SixMovesTransformer
    from transform.six_moves import MovedAttribute
    from transform.six_moves import MovedModule

    # Test when rewrites is None
    assert SixMovesTransformer.rewrites is None
    assert SixMovesTransformer.dependencies == ['six']

    # Test when rewrites is not None
    SixMovesTransformer._rewrites = {'six.moves.urllib.parse': 'urllib.parse'}
    assert SixMovesTransformer.rewrites is not None
    assert SixMovesTransformer.rewrites == {'six.moves.urllib.parse': 'urllib.parse'}
    assert SixMovesTransformer.dependencies == ['six']

# Generated at 2022-06-14 02:08:04.486651
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert MovedAttribute("cStringIO", "cStringIO", "io", "StringIO").name == "cStringIO"
    assert MovedAttribute("filter", "itertools", "builtins", "ifilter", "filter").name == "filter"
    assert MovedAttribute("filterfalse", "itertools", "itertools", "ifilterfalse", "filterfalse").name == "filterfalse"
    assert MovedAttribute("input", "__builtin__", "builtins", "raw_input", "input").name == "input"
    assert MovedAttribute("intern", "__builtin__", "sys").name == "intern"
    assert MovedAttribute("map", "itertools", "builtins", "imap", "map").name == "map"

# Generated at 2022-06-14 02:08:15.954503
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    MovedAttribute("a", "b", "c")
    MovedAttribute("a", "b", "c", "d", "e")
    MovedAttribute("a", "c", None)
    MovedAttribute("a", "c")
    MovedAttribute("a", "c", "c", "a", "a")
    MovedAttribute("a", "c", "c", "a")
    MovedAttribute("a", "c", "c", None, "c")
    MovedAttribute("a", "b", "c", "d")
    MovedAttribute("a", "b", "c", None, "e")
    MovedAttribute("a", "b", None, None, "d")
    MovedAttribute("a", "b", None, "c", "d")

# Generated at 2022-06-14 02:08:21.180447
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    move = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert move.name == "cStringIO"
    assert move.new_mod == "io"
    assert move.new_attr == "StringIO"

# Generated at 2022-06-14 02:08:32.650275
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    ma = MovedAttribute("new_attr", "new_mod", "new_attr", "old_attr", None)
    assert ma.name == 'new_attr'
    assert ma.new_mod == 'new_mod'
    assert ma.new_attr == 'new_attr'

    ma = MovedAttribute("new_attr", "new_mod", "new_attr", None, None)
    assert ma.name == 'new_attr'
    assert ma.new_mod == 'new_attr'
    assert ma.new_attr == 'new_attr'

    ma = MovedAttribute("new_attr", "new_mod", None, "old_attr", None)
    assert ma.name == 'new_attr'
    assert ma.new_mod == 'new_attr'

# Generated at 2022-06-14 02:08:48.358536
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
    move = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO", "StringIO2")
    assert move.name == "cStringIO"
    assert move.new_mod == "io"
    assert move.new_attr == "StringIO2"


# Generated at 2022-06-14 02:08:57.735160
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    name = 'test_name'
    old_mod = 'test_mod'
    new_mod = 'test_new_mod'
    old_attr = 'test_old_attr'
    new_attr = 'test_new_attr'
    move = MovedAttribute(name, old_mod, new_mod, old_attr, new_attr)
    assert(move.name == name)
    assert(move.new_mod == new_mod)
    assert(move.new_attr == new_attr)


# Generated at 2022-06-14 02:09:00.764414
# Unit test for constructor of class MovedModule
def test_MovedModule():
    mm = MovedModule("foo.bar", "foo.bar")
    assert mm.name == "foo.bar"
    assert mm.new == "foo.bar"



# Generated at 2022-06-14 02:09:11.920144
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    ma = MovedAttribute('name', 'old', 'new')
    assert ma.name == 'name' and ma.new_mod == 'new' and ma.new_attr == 'name'

    ma = MovedAttribute('name', 'old', 'new', 'old_attr')
    assert ma.name == 'name' and ma.new_mod == 'new' and ma.new_attr == 'old_attr'

    ma = MovedAttribute('name', 'old', 'new', new_attr='new_attr')
    assert ma.name == 'name' and ma.new_mod == 'new' and ma.new_attr == 'new_attr'

    ma = MovedAttribute('name', 'old', 'new', 'old_attr', 'new_attr')

# Generated at 2022-06-14 02:09:14.137485
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    transformer = SixMovesTransformer({})
    assert transformer.rewrites == _get_rewrites()

# Generated at 2022-06-14 02:09:24.350488
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    result = _get_rewrites()

# Generated at 2022-06-14 02:09:31.053388
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    a = MovedAttribute('a', 'b', 'c')
    assert a.name == 'a'
    assert a.new_attr == 'a'
    assert a.new_mod == 'c'

    a = MovedAttribute('a', 'b', 'c', 'd')
    assert a.name == 'a'
    assert a.new_attr == 'd'
    assert a.new_mod == 'c'

    a = MovedAttribute('a', 'b', 'c', 'd', 'e')
    assert a.name == 'a'
    assert a.new_attr == 'e'
    assert a.new_mod == 'c'


# Generated at 2022-06-14 02:09:43.848842
# Unit test for constructor of class MovedModule
def test_MovedModule():
    """Creating instances of class MovedModule works as expected."""
    assert MovedModule('name', 'old').name == 'name'
    assert MovedModule('name', 'old').old == 'old'
    assert MovedModule('name', 'old', 'new').new == 'new'
    assert MovedModule('name', 'old').new == 'name'
    assert MovedModule('name', 'old', 'new').old == 'old'


# Generated at 2022-06-14 02:09:52.665499
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    foo = MovedAttribute("filename", "__builtin__", "io")
    assert foo.name == "filename"
    assert foo.new_mod == "io"
    assert foo.new_attr == "filename"

    foo = MovedAttribute("StringIO", "cStringIO", "io")
    assert foo.name == "StringIO"
    assert foo.new_mod == "io"
    assert foo.new_attr == "StringIO"

# Generated at 2022-06-14 02:09:53.794199
# Unit test for constructor of class MovedModule
def test_MovedModule():
    assert MovedModule('parser', 'ConfigParser')

# Generated at 2022-06-14 02:09:58.138956
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    moved_attribute = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert isinstance(moved_attribute, MovedAttribute)


# Generated at 2022-06-14 02:10:01.573461
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert SixMovesTransformer.rewrites == _get_rewrites()


transformers = [SixMovesTransformer]

# Generated at 2022-06-14 02:10:06.560161
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    m = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert m.name == "cStringIO"
    assert m.new_mod == "io"
    assert m.new_attr == "StringIO"


# Generated at 2022-06-14 02:10:13.060492
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    MovedAttribute("cStringIO", "cStringIO", "io", "StringIO", "StringIO")
    MovedAttribute("cStringIO", "cStringIO", "io")
    MovedAttribute("cStringIO", "cStringIO", "io", new_attr="StringIO")



# Generated at 2022-06-14 02:10:18.461345
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    from tree_transformer import TreeRewriter
    from transformer_test import validate_transformer
    from .. import transforms
    from . import sixmoves

    transformer = TreeRewriter(transforms.import_rewrites, None)

    validate_transformer(sixmoves.SixMovesTransformer, transformer)

# Generated at 2022-06-14 02:10:29.014188
# Unit test for constructor of class SixMovesTransformer

# Generated at 2022-06-14 02:10:32.643086
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert len(_get_rewrites()) == len(SixMovesTransformer.rewrites)


__transformer__ = SixMovesTransformer()

# Generated at 2022-06-14 02:10:43.063162
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    ma = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert ma.name == "cStringIO"
    assert ma.new_mod == "io"
    assert ma.new_attr == "StringIO"


# Generated at 2022-06-14 02:10:56.506324
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    a = MovedAttribute("name", "old_mod", "new_mod", "old_attr", "new_attr")
    assert a.name == "name"
    assert a.old_mod == "old_mod"
    assert a.new_mod == "new_mod"
    assert a.old_attr == "old_attr"
    assert a.new_attr == "new_attr"
    b = MovedAttribute("name", "old_mod", "new_mod", "old_attr")
    assert b.new_attr == "old_attr"
    c = MovedAttribute("name", "old_mod", "new_mod")
    assert c.old_mod == "old_mod"
    assert c.new_mod == "name"
    d = MovedAttribute("name", "old_mod")
    assert d

# Generated at 2022-06-14 02:10:58.759207
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert list(_get_rewrites())[0] == ("builtins.cStringIO", "six.moves.cStringIO")

# Generated at 2022-06-14 02:11:08.137202
# Unit test for constructor of class MovedModule
def test_MovedModule():
    mm = MovedModule("a", "b", "c")
    assert mm.name == "a"
    assert mm.old == "b"
    assert mm.new == "c"
    mm = MovedModule("a", "b", new="c")
    assert mm.name == "a"
    assert mm.old == "b"
    assert mm.new == "c"
    mm = MovedModule("a", "b", "c")
    assert mm.name == "a"
    assert mm.old == "b"
    assert mm.new == "c"
    mm = MovedModule("a", "b", "c")
    assert mm.name == "a"
    assert mm.old == "b"
    assert mm.new == "c"


# Generated at 2022-06-14 02:11:15.785316
# Unit test for constructor of class MovedModule
def test_MovedModule():
    # Make sure that the constructor of MovedModule works properly.  It
    # should return the arguments provided to it in a tuple, but shrunk
    # if possible.  It should also handle invalid arguments.

    # Return 2-tuples.
    def assertTuple(expectedTuple, *args):
        assert len(expectedTuple) == len(args)
        actualTuple = MovedModule(*args)
        assert actualTuple == expectedTuple

    assertTuple(('foo', 'bar', 'baz'), 'foo', 'bar', 'baz')
    assertTuple(('foo', 'bar'), 'foo', 'bar')
    assertTuple(('foo', 'foo'), 'foo')
    assertTuple(('foo', 'foo'), 'foo', None)
    assertTuple(('foo', 'foo'), 'foo', '')



# Generated at 2022-06-14 02:11:20.030296
# Unit test for constructor of class MovedModule
def test_MovedModule():
    moved_module = MovedModule('TestModule', 'test.module.TestModule', 'test.module.newModule')
    assert moved_module.name == 'TestModule'
    assert moved_module.new == 'test.module.newModule'


# Generated at 2022-06-14 02:11:31.050844
# Unit test for constructor of class MovedModule
def test_MovedModule():
    data = [('os', 'os', 'os'),
            ('configparser', 'ConfigParser', 'configparser'),
            ('copyreg', 'copy_reg', 'copyreg'),]
    for data_item in data:
        assert MovedModule(data_item[0], data_item[1], data_item[2]).name == data_item[0]
        assert MovedModule(data_item[0], data_item[1], data_item[2]).old == data_item[1]
        assert MovedModule(data_item[0], data_item[1], data_item[2]).new == data_item[2]

# Generated at 2022-06-14 02:11:34.850340
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    # pylint: disable=unused-variable
    from lib2to3.fixes import six_moves
    from libmodernize.fixes.fix_six_moves import SixMovesTransformer

# Generated at 2022-06-14 02:11:39.892617
# Unit test for constructor of class MovedModule
def test_MovedModule():
    name = "test_name"
    old_mod = "test_old_mod"
    new_mod = "test_new_mod"
    mod = MovedModule(name, old_mod, new_mod)
    assert mod.name == name
    assert mod.old == old_mod
    assert mod.new == new_mod

# Generated at 2022-06-14 02:11:42.982370
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert 2 == len(SixMovesTransformer.rewrites)
    assert 2 == len(SixMovesTransformer(None).rewrites)

# Generated at 2022-06-14 02:11:57.876503
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
    move = MovedAttribute("cStringIO", "cStringIO", None)
    assert move.name == "cStringIO"
    assert move.new_mod == "cStringIO"
    assert move.new_attr == "cStringIO"



# Generated at 2022-06-14 02:12:10.397583
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    testMovedAttribute = MovedAttribute("name", "old_mod", "new_mod")
    assert testMovedAttribute.name == "name"
    assert testMovedAttribute.new_mod == "new_mod"
    assert testMovedAttribute.new_attr == "name"

    testMovedAttribute2 = MovedAttribute("name", "old_mod", "new_mod", "old_attr")
    assert testMovedAttribute2.name == "name"
    assert testMovedAttribute2.new_mod == "new_mod"
    assert testMovedAttribute2.new_attr == "old_attr"

    testMovedAttribute3 = MovedAttribute("name", "old_mod", "new_mod", "old_attr", "new_attr")
    assert testMovedAttribute3.name == "name"
    assert testM

# Generated at 2022-06-14 02:12:16.300597
# Unit test for constructor of class MovedModule
def test_MovedModule():
    mod1 = MovedModule("os","os")
    mod2 = MovedModule("os","os","newos")
    assert mod1.name == "os"
    assert mod1.old == "os"
    assert mod1.new == "os"
    assert mod2.name == "os"
    assert mod2.old == "os"
    assert mod2.new == "newos"

# Generated at 2022-06-14 02:12:17.729707
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")

# Generated at 2022-06-14 02:12:22.985231
# Unit test for constructor of class MovedModule
def test_MovedModule():
    moved = MovedModule('example', 'example.old', 'example.new')
    assert moved.name == 'example'
    assert moved.new == 'example.new'
    moved = MovedModule('example', 'example.old')
    assert moved.name == 'example'
    assert moved.new == 'example'



# Generated at 2022-06-14 02:12:33.973003
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    import six
    from .sixmodule_test import test_SixMovesTransformer
    from .sixmodule_test.six.moves import urllib_parse
    from .sixmodule_test.six.moves.urllib.parse import quote
    from .sixmodule_test.six.moves.urllib.parse import quote_plus
    from .sixmodule_test.six.moves.urllib.parse import unquote
    from .sixmodule_test.six.moves.urllib.parse import unquote_plus
    from .sixmodule_test.six.moves.urllib.parse import urlencode
    from .sixmodule_test.six.moves.urllib.parse import urljoin
    from .sixmodule_test.six.moves.urllib.parse import urlparse

# Generated at 2022-06-14 02:12:39.247282
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    ma = MovedAttribute("name", "old_mod", "new_mod", "old_attr", "new_attr")
    assert ma.name == "name"
    assert ma.new_mod == "new_mod"
    assert ma.new_attr == "new_attr"



# Generated at 2022-06-14 02:12:50.615636
# Unit test for constructor of class SixMovesTransformer

# Generated at 2022-06-14 02:12:57.288804
# Unit test for constructor of class MovedModule
def test_MovedModule():
    assert MovedModule('name','old','new').name == 'name'
    assert MovedModule('name','old','new').old == 'old'
    assert MovedModule('name','old','new').new == 'new'
    assert MovedModule('name', 'old').name == 'name'
    assert MovedModule('name', 'old').old == 'old'
    assert MovedModule('name', 'old').new == 'name'


# Unit tests for SixMovesTransformer

# Generated at 2022-06-14 02:13:10.954257
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    '''Tests if constructor of class MovedAttribute works correctly'''
    # test if all properties are correctly set and if the constructor
    # works correctly with all different input combinations.
    attr = MovedAttribute('foo', 'bar', 'baz', 'steve', 'maria')
    assert attr.name == 'foo'
    assert attr.new_mod == 'baz'
    assert attr.new_attr == 'maria'

    attr = MovedAttribute('foo', 'bar', None, 'steve', 'maria')
    assert attr.name == 'foo'
    assert attr.new_mod == 'foo'
    assert attr.new_attr == 'maria'

    attr = MovedAttribute('foo', 'bar', None, 'steve', 'maria')
    assert attr.name

# Generated at 2022-06-14 02:13:32.115618
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    a = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert a.name == "cStringIO"
    assert a.new_mod == "io"
    assert a.new_attr == "StringIO"

    b = MovedAttribute("cStringIO", "cStringIO", "io", old_attr="StringIO")
    assert b.name == "cStringIO"
    assert b.new_mod == "io"
    assert b.new_attr == "StringIO"

    c = MovedAttribute("cStringIO", "cStringIO", "io")
    assert c.name == "cStringIO"
    assert c.new_mod == "io"
    assert c.new_attr == "cStringIO"


# Generated at 2022-06-14 02:13:35.752943
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert len(_moved_attributes) > 2
    assert len(prefixed_moves) > 3

if __name__ == '__main__':  # pragma: no cover
    test_SixMovesTransformer()

# Generated at 2022-06-14 02:13:38.741438
# Unit test for constructor of class MovedModule
def test_MovedModule():
    try:
        MovedModule("builtins", "__builtin__")
    except Exception:
        raise Exception("MovedModule constructor test failed")

# Generated at 2022-06-14 02:13:40.520802
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    """Test that the constructor of class SixMovesTransformer
    works as expected."""
    p = SixMovesTransformer()
    assert p

# Generated at 2022-06-14 02:13:44.551695
# Unit test for constructor of class MovedModule
def test_MovedModule():
    move = MovedModule('name', 'old', 'new')
    assert move.name == 'name'
    assert move.old == 'old'
    assert move.new == 'new'

# Generated at 2022-06-14 02:13:50.711090
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    moved_attribute = MovedAttribute('name', 'old_mod', 'new_mod', 'old_attr', 'new_attr')
    assert moved_attribute.name == 'name'
    assert moved_attribute.old_mod == 'old_mod'
    assert moved_attribute.new_mod == 'new_mod'
    assert moved_attribute.old_attr == 'old_attr'
    assert moved_attribute.new_attr == 'new_attr'


# Generated at 2022-06-14 02:13:59.327857
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    from .typeshed import _typeshed
    import unittest
    from .utils.type_mock import type_mock

    class TestSixMovesTransformer(unittest.TestCase):
        def test_rewrites(self):
            t = SixMovesTransformer()

# Generated at 2022-06-14 02:14:01.540461
# Unit test for constructor of class MovedModule
def test_MovedModule():
    m = MovedModule('a', 'b')
    assert m.name == 'a'
    assert m.new == 'b'


# Generated at 2022-06-14 02:14:06.819111
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert MovedAttribute("cStringIO", "cStringIO", "io", "StringIO").new_attr == "StringIO"
    assert MovedAttribute("cStringIO", "cStringIO", "io").new_attr == "cStringIO"
    assert MovedAttribute("cStringIO", "cStringIO", "io", "StringIO").name == "cStringIO"
    assert MovedAttribute("cStringIO", "cStringIO", "io", "StringIO").new_mod == "io"

# Generated at 2022-06-14 02:14:11.725300
# Unit test for constructor of class MovedModule
def test_MovedModule():
    # Case: New module name
    assert MovedModule('new', 'old') == MovedModule('new', 'old', 'new')

    # Case: New and old module name
    assert MovedModule('old', 'old', 'new') == MovedModule('old', 'old', 'new')

# Generated at 2022-06-14 02:14:47.233780
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    """Test constructor of class MovedAttribute."""
    m = MovedAttribute('cStringIO', 'cStringIO', 'io', 'StringIO')
    assert m.name == 'cStringIO'
    assert m.new_mod == 'io'
    assert m.new_attr == 'StringIO'



# Generated at 2022-06-14 02:15:00.674212
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

    move = MovedAttribute("cStringIO", "cStringIO", None)
    assert move.name == "cStringIO"
    assert move.new_mod == "cStringIO"
    assert move.new_attr == "cStringIO"

# Generated at 2022-06-14 02:15:02.066450
# Unit test for constructor of class MovedModule
def test_MovedModule():
    pass


# Generated at 2022-06-14 02:15:05.547454
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    am = SixMovesTransformer()
    assert am.rewrites == _get_rewrites()
    assert am.dependencies == ['six']

# Generated at 2022-06-14 02:15:11.118281
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert len(SixMovesTransformer.rewrites) == len(_moved_attributes + _urllib_parse_moved_attributes + _urllib_error_moved_attributes + _urllib_request_moved_attributes + _urllib_response_moved_attributes + _urllib_robotparser_moved_attributes)

# Generated at 2022-06-14 02:15:23.466811
# Unit test for constructor of class SixMovesTransformer

# Generated at 2022-06-14 02:15:32.306051
# Unit test for constructor of class MovedModule
def test_MovedModule():
    mm = MovedModule("name","old","new")
    assert mm.name == "name"
    assert mm.old == "old"
    assert mm.new == "new"
    mm = MovedModule("name2","old2")
    assert mm.name == "name2"
    assert mm.old == "old2"
    assert mm.new == "name2"
    mm = MovedModule("name3")
    assert mm.name == "name3"
    assert mm.old == "name3"
    assert mm.new == "name3"
    with pytest.raises(TypeError):
        mm = MovedModule(None, "oldvalue")
    with pytest.raises(TypeError):
        mm = MovedModule("name", None, "newvalue")

# Generated at 2022-06-14 02:15:43.715896
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    x = MovedAttribute('a', 'b', 'c', 'd', 'e')
    y = MovedAttribute('aa', 'bb', 'cc', 'dd', 'ee')
    z = MovedAttribute('aaa', 'bbb', 'ccc', 'ddd', 'eee')
    assert x.name == 'a', "name"
    assert x.new_mod == 'c', "new_mod"
    assert x.new_attr == 'e', "new_attr"
    assert x.__dict__ == {'name': 'a', 'new_mod': 'c', 'new_attr': 'e'}, "__dict__"
    assert x.__str__() == '<MovedAttribute: name="a", new_mod="c", new_attr="e">'

# Generated at 2022-06-14 02:15:47.293105
# Unit test for constructor of class MovedModule
def test_MovedModule():
    moves = [MovedModule('test', 'oldtest', 'newtest'),
             MovedModule('test2', 'oldtest2')]
    for move in moves:
        assert move.name == move.new
        assert move.old


# Generated at 2022-06-14 02:15:57.363949
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    try:
        import six
    except ImportError:
        return

    assert isinstance(SixMovesTransformer, type)
    assert isinstance(SixMovesTransformer.rewrites, list)
    assert isinstance(SixMovesTransformer.dependencies, list)
    assert all(isinstance(x, tuple) for x in SixMovesTransformer.rewrites)
    assert all(len(x) == 2 for x in SixMovesTransformer.rewrites)
    assert SixMovesTransformer.rewrites
    assert all(isinstance(x, str) for x in SixMovesTransformer.dependencies)
    assert SixMovesTransformer.dependencies
    assert SixMovesTransformer.target == (2, 7)