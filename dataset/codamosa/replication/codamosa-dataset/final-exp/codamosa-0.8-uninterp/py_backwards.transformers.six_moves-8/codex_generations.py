

# Generated at 2022-06-14 02:06:10.445245
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    a = MovedAttribute('cStringIO', 'cStringIO', 'io', 'StringIO')
    assert a.name == 'cStringIO'
    assert a.new_mod == 'io'
    assert a.new_attr == 'StringIO'

    a = MovedAttribute('cStringIO', 'cStringIO', 'io', old_attr='StringIO', new_attr='StringIO1')
    assert a.name == 'cStringIO'
    assert a.new_mod == 'io'
    assert a.new_attr == 'StringIO1'

    with pytest.raises(AssertionError):
        a = MovedAttribute('cStringIO', 'cStringIO', 'io', old_attr='StringIO')

# Generated at 2022-06-14 02:06:14.293895
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    my_class = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert my_class.name == "cStringIO"
    assert my_class.new_mod == "io"
    assert my_class.new_attr == "StringIO"


# Generated at 2022-06-14 02:06:16.030088
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert len(SixMovesTransformer.rewrites) == 45

# Generated at 2022-06-14 02:06:19.002718
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    s = SixMovesTransformer()
    assert s.target == (2, 7)
    assert s.rewrites == _get_rewrites()
    assert s.dependencies == ['six']

# Generated at 2022-06-14 02:06:28.215375
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    moved = MovedAttribute('name', 'old_mod', 'new_mod')
    assert moved.name == 'name'
    assert moved.new_mod == 'new_mod'
    assert moved.new_attr == 'name'
    moved = MovedAttribute('name', 'old_mod', 'new_mod', 'old_attr', 'new_attr')
    assert moved.name == 'name'
    assert moved.new_mod == 'new_mod'
    assert moved.new_attr == 'new_attr'
    moved = MovedAttribute('name', 'old_mod', 'new_mod', 'old_attr')
    assert moved.name == 'name'
    assert moved.new_mod == 'new_mod'
    assert moved.new_attr == 'old_attr'


# Generated at 2022-06-14 02:06:32.865544
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    attribute = MovedAttribute("name", "old_mod", "new_mod", "old_attr", "new_attr")
    assert attribute.name == "name", "name is not correctly set"
    assert attribute.new_mod == "new_mod", "new_mod is not correctly set"
    assert attribute.new_attr == "new_attr", "new_attr is not correctly set"


# Generated at 2022-06-14 02:06:42.670559
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert MovedAttribute("cStringIO", "cStringIO", "io", "StringIO") == MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert MovedAttribute("cStringIO", "cStringIO", "io", "StringIO") != MovedAttribute("cStringIO", "cStringIO", "io", "StringIO2")
    assert MovedAttribute("cStringIO", "cStringIO", "io", "StringIO") != MovedAttribute("cStringIO2", "cStringIO", "io", "StringIO")


# Generated at 2022-06-14 02:06:50.672551
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    a = MovedAttribute("name", "old", "new")
    assert a.name == "name"
    assert a.new_mod == "new"
    assert a.new_attr == "name"
    a = MovedAttribute("name", "old", "new", "old_attr")
    assert a.name == "name"
    assert a.new_mod == "new"
    assert a.new_attr == "old_attr"
    a = MovedAttribute("name", "old", "new", old_attr="old_attr", new_attr="new_attr")
    assert a.name == "name"
    assert a.new_mod == "new"
    assert a.new_attr == "new_attr"

# Generated at 2022-06-14 02:06:54.819303
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    expected = ('test.test_six.test_moves.dummy_func', 'six.moves.urllib.parse.dummy_func')
    actual = SixMovesTransformer.rewrites[2]
    assert actual == expected

# Generated at 2022-06-14 02:06:59.195537
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    m_atr = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert m_atr.name == "cStringIO"
    assert m_atr.new_mod == "io"
    assert m_atr.new_attr == "StringIO"


# Generated at 2022-06-14 02:07:09.141076
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    # Given
    import six
    import six.moves

    # When
    moved_attributes = [
        MovedAttribute("intern", "__builtin__", "sys"),
        MovedAttribute("getstatusoutput", "commands", "subprocess"),
        MovedAttribute("getoutput", "commands", "subprocess")
    ]

    # Then
    for move in moved_attributes:
        if isinstance(move, MovedAttribute):
            spec = 'six.moves{}.{}'.format('', move.name)
            __import__(spec)
            mod = locals()[spec]
            assert isinstance(getattr(mod, move.new_attr), type(getattr(six.moves, move.name)))

# Generated at 2022-06-14 02:07:11.612770
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert SixMovesTransformer.__name__ == "SixMovesTransformer"


# Generated at 2022-06-14 02:07:15.849678
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    ma = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert ma.name == "cStringIO"
    assert ma.new_mod == "io"
    assert ma.new_attr == "StringIO"

# Generated at 2022-06-14 02:07:22.509189
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    moved_attribute1 = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert moved_attribute1.name == "cStringIO"
    assert moved_attribute1.new_mod == "io"
    assert moved_attribute1.new_attr == "StringIO"


# Generated at 2022-06-14 02:07:31.691846
# Unit test for constructor of class MovedModule
def test_MovedModule():
    try:
        mod = MovedModule("test1", "test11")
    except TypeError:
        assert False, "MovedModule failed to instantiate"
    assert mod.name == "test1"
    assert mod.old == "test11"
    assert mod.new == "test1"
    try:
        mod = MovedModule("test2", "test21", "test22")
    except TypeError:
        assert False, "MovedModule failed to instantiate"
    assert mod.name == "test2"
    assert mod.old == "test21"
    assert mod.new == "test22"

# Generated at 2022-06-14 02:07:44.209377
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    from lib2to3.pygram import python_symbols as syms
    from lib2to3 import fixer_base
    from libfuturize.fixes.six_moves import SixMovesTransformer

    fixer = SixMovesTransformer(None)
    assert fixer.explicit
    assert fixer.run_order == 7
    assert fixer.syms == syms

# Generated at 2022-06-14 02:07:46.448783
# Unit test for constructor of class MovedModule
def test_MovedModule():
    assert MovedModule("name", "old") == MovedModule("name", "old", "name")


# Generated at 2022-06-14 02:07:51.537563
# Unit test for constructor of class MovedModule
def test_MovedModule():
    x = MovedModule('a', 'b', 'c')
    assert x.name == 'a'
    assert x.new == 'b'
    x = MovedModule('a', 'b')
    assert x.name == 'a'
    assert x.new == 'a'

# Generated at 2022-06-14 02:08:00.024090
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    # Should define `name`, `new_mod` and `new_attr`
    assert MovedAttribute('name', 'old_mod', 'new_mod', 'old_attr', 'new_attr').name == 'name'
    assert MovedAttribute('name', 'old_mod', 'new_mod', 'old_attr', 'new_attr').new_mod == 'new_mod'
    assert MovedAttribute('name', 'old_mod', 'new_mod', 'old_attr', 'new_attr').new_attr == 'new_attr'
    # Should take `name` for `new_mod` and `name` for `new_attr` when `new_mod` is None and `new_attr` is None
    assert MovedAttribute('name', 'old_mod', None).new_mod == 'name'

# Generated at 2022-06-14 02:08:12.194114
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    # pylint: disable=unused-variable
    a = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    b = MovedAttribute("filter", "itertools", "builtins", "ifilter", "filter")
    c = MovedAttribute("filterfalse", "itertools", "itertools", "ifilterfalse", "filterfalse")
    d = MovedAttribute("input", "__builtin__", "builtins", "raw_input", "input")
    e = MovedAttribute("intern", "__builtin__", "sys")
    f = MovedAttribute("map", "itertools", "builtins", "imap", "map")
    g = MovedAttribute("getcwd", "os", "os", "getcwdu", "getcwd")
    h

# Generated at 2022-06-14 02:08:20.911499
# Unit test for constructor of class MovedModule
def test_MovedModule():
    mm = MovedModule("builtins", "__builtin__")
    assert mm.name == "builtins"
    assert mm.new == "builtins"
    mm = MovedModule("builtins", "__builtin__", "builtins")
    assert mm.name == "builtins"
    assert mm.new == "builtins"


# Generated at 2022-06-14 02:08:33.140608
# Unit test for constructor of class MovedModule
def test_MovedModule():
    assert MovedModule("builtins", "__builtin__").name == "builtins"
    assert MovedModule("builtins", "__builtin__").new == "builtins"
    assert MovedModule("configparser", "ConfigParser").name == "configparser"
    assert MovedModule("configparser", "ConfigParser").new == "configparser"
    assert MovedModule("copyreg", "copy_reg").name == "copyreg"
    assert MovedModule("copyreg", "copy_reg").new == "copyreg"
    assert MovedModule("dbm_gnu", "gdbm", "dbm.gnu").name == "dbm_gnu"
    assert MovedModule("dbm_gnu", "gdbm", "dbm.gnu").new == "dbm.gnu"

# Generated at 2022-06-14 02:08:39.660017
# Unit test for constructor of class MovedModule
def test_MovedModule():
    m = MovedModule("name", "old")
    assert m.name == "name"
    assert m.new == "name"
    m = MovedModule("name", "old", "new")
    assert m.name == "name"
    assert m.new == "new"


# Generated at 2022-06-14 02:08:44.764339
# Unit test for constructor of class MovedModule
def test_MovedModule():
    m1 = MovedModule("dqd", "dqdu")
    m2 = MovedModule("dqd", "dqdu", "dqd")
    assert m1.name == "dqd"
    assert m1.new == "dqd"
    assert m1.old == "dqdu"
    assert m2.name == "dqd"
    assert m2.new == "dqd"
    assert m2.old == "dqdu"


# Generated at 2022-06-14 02:08:50.758202
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    ma = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert ma.name == "cStringIO"
    assert ma.new_mod == "io"
    assert ma.new_attr == "StringIO"


# Generated at 2022-06-14 02:08:58.494107
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    ma0 = MovedAttribute('a', 'b', 'c')
    assert ma0.name == 'a'
    assert ma0.new_mod == 'c'
    assert ma0.new_attr == 'a'

    ma1 = MovedAttribute('a', 'b', 'c', 'x', 'y')
    assert ma1.new_mod == 'c'
    assert ma1.new_attr == 'y'


# Generated at 2022-06-14 02:09:05.361252
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    ma = MovedAttribute('name', 'old_mod', 'new_mod', 'old_attr', 'new_attr')
    assert ma.name == 'name'
    assert ma.new_mod == 'new_mod'
    assert ma.new_attr == 'new_attr'
    # Test fallbacks
    ma = MovedAttribute('name', 'old_mod', 'new_mod', 'old_attr')
    assert ma.new_attr == 'old_attr'
    ma = MovedAttribute('name', 'old_mod', 'new_mod')
    assert ma.new_attr == 'name'


# Generated at 2022-06-14 02:09:18.626797
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    """SixMovesTransformer is a valid Transformation."""
    class_ = SixMovesTransformer
    assert issubclass(class_, BaseImportRewrite)
    assert class_.target == (2, 7)
    assert class_.rewrites[0] == ('io.StringIO', 'six.moves.cStringIO')
    assert class_.rewrites[1] == ('builtins.ifilter', 'six.moves.filter')
    assert class_.rewrites[2] == ('builtins.input', 'six.moves.input')
    assert class_.rewrites[3] == ('sys.intern', 'six.moves.intern')
    assert class_.rewrites[4] == ('builtins.imap', 'six.moves.map')

# Generated at 2022-06-14 02:09:26.148812
# Unit test for constructor of class MovedModule
def test_MovedModule():
    # Test moved module of type `MovedModule`
    mm = MovedModule('six_module', 'six')
    assert mm.name == 'six_module' and mm.new == 'six'
    mm = MovedModule('six_module', 'six', 'six_m')
    assert mm.name == 'six_module' and mm.new == 'six_m'


# Generated at 2022-06-14 02:09:35.929657
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
  import sys
  import unittest
  mod = sys.modules[__name__]
  transformer = SixMovesTransformer({__name__: mod})
  assert isinstance(transformer, SixMovesTransformer,
                     msg="transformer = {} is not an instance of class {}".format(
                         transformer, SixMovesTransformer))
  return


if __name__ == '__main__':
  test_SixMovesTransformer()
  print('Module {} passed all tests.'.format(__name__))

# Generated at 2022-06-14 02:09:47.354786
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    ma1 = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert ma1.name == "cStringIO"
    assert ma1.old_mod == "cStringIO"
    assert ma1.new_mod == "io"
    assert ma1.old_attr == "StringIO"
    assert ma1.new_attr == "StringIO"
    ma2 = MovedAttribute("cStringIO", "cStringIO", "io")
    assert ma2.name == "cStringIO"
    assert ma2.old_mod == "cStringIO"
    assert ma2.new_mod == "io"
    assert ma2.old_attr is None
    assert ma2.new_attr == "cStringIO"


# Generated at 2022-06-14 02:09:55.365396
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    x = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert(x.name == "cStringIO")
    assert(x.new_mod == "io")
    assert(x.new_attr == "StringIO")
    x = MovedAttribute("cStringIO", "cStringIO", "io")
    assert(x.new_attr == "cStringIO")


# Generated at 2022-06-14 02:09:58.262861
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert SixMovesTransformer().rewrites == _get_rewrites()
    assert SixMovesTransformer().dependencies == ['six']

# Generated at 2022-06-14 02:10:10.184290
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    st = SixMovesTransformer()
    assert st.target == (2, 7)

# Generated at 2022-06-14 02:10:16.629060
# Unit test for constructor of class MovedModule
def test_MovedModule():
    # test that the default constructor works
    mm = MovedModule("test")
    assert mm.name == "test"
    assert mm.new == "test"
    # test that the named constructor works
    mm = MovedModule("test", "test_old", "test_new")
    assert mm.name == "test"
    assert mm.new == "test_new"


# Generated at 2022-06-14 02:10:21.401365
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    attribute = MovedAttribute('cStringIO', 'cStringIO', 'io', 'StringIO')
    assert attribute.name == 'cStringIO'
    assert attribute.new_mod == 'io'
    assert attribute.new_attr == 'StringIO'

# Generated at 2022-06-14 02:10:32.945391
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    gen = SixMovesTransformer()

    assert len(list(gen.rewrites)) == 230

    rewrites = gen.rewrites
    assert rewrites['cStringIO.StringIO'] == 'six.moves.cStringIO'
    assert rewrites['builtins.ifilter'] == 'six.moves.filter'
    assert rewrites['builtins.input'] == 'six.moves.input'
    assert rewrites['sys.intern'] == 'six.moves.intern'
    assert rewrites['builtins.imap'] == 'six.moves.map'
    assert rewrites['os.getcwdu'] == 'six.moves.getcwd'
    assert rewrites['os.getcwd'] == 'six.moves.getcwdb'
    assert rewrit

# Generated at 2022-06-14 02:10:38.619484
# Unit test for constructor of class MovedModule
def test_MovedModule():
    name = 'name'
    old = 'old'
    new = 'new'
    assert MovedModule(name, old, new).__dict__ == {'name': name, 'new': new}
    assert MovedModule(name, old).__dict__ == {'name': name, 'new': old}


# Generated at 2022-06-14 02:10:51.551976
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

    move = MovedAttribute("getcwd", "os", "os", "getcwdu", "getcwd")
    assert move.name == "getcwd"
    assert move.new_mod == "os"
    assert move.new_attr == "getcwd"


# Generated at 2022-06-14 02:10:56.306142
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    a = MovedAttribute("a", "b", "c", "d", "e")
    assert a.name == "a"
    assert a.new_mod == "c"
    assert a.new_attr == "e"



# Generated at 2022-06-14 02:11:06.344288
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    from ..helpers import assert_include
    assert_include(__name__ + '.SixMovesTransformer',
                   ['six'])

# Generated at 2022-06-14 02:11:13.884219
# Unit test for constructor of class MovedModule
def test_MovedModule():
    assert MovedModule("builtins", "__builtin__").name == "builtins"
    assert MovedModule("builtins", "__builtin__").new == "builtins"
    assert MovedModule("builtins", "__builtin__", "__builtin__").name == "builtins"
    assert MovedModule("builtins", "__builtin__", "__builtin__").new == "__builtin__"



# Generated at 2022-06-14 02:11:24.134540
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert MovedAttribute(
        'cStringIO', 'cStringIO', 'io', 'StringIO').new_attr == 'StringIO'
    assert MovedAttribute(
        'filter', 'itertools', 'builtins', 'ifilter', 'filter').new_attr == 'filter'
    assert MovedAttribute(
        'filterfalse', 'itertools', 'itertools', 'ifilterfalse', 'filterfalse').new_attr == 'filterfalse'
    assert MovedAttribute('input', '__builtin__', 'builtins',
                          'raw_input', 'input').new_attr == 'input'
    assert MovedAttribute('intern', '__builtin__', 'sys').new_attr == 'intern'

# Generated at 2022-06-14 02:11:37.076320
# Unit test for constructor of class SixMovesTransformer

# Generated at 2022-06-14 02:11:39.069220
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    EightMovesTransformer()

# Generated at 2022-06-14 02:11:50.951534
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    c = MovedAttribute("c", "old", "new", "old_attr", "new_attr")
    assert c.name == "c"
    assert c.new_mod == "new"
    assert c.new_attr == "new_attr"
    c = MovedAttribute("c", "old", "new", "old_attr", None)
    assert c.new_attr == "old_attr"
    c = MovedAttribute("c", "old", "new", None, "new_attr")
    assert c.new_attr == "new_attr"
    c = MovedAttribute("c", "old", "new", None, None)
    assert c.new_attr == "c"


# Generated at 2022-06-14 02:11:54.113688
# Unit test for constructor of class MovedModule
def test_MovedModule():
    _new_mo = MovedModule("builtins", "__builtin__")
    assert _new_mo.new == "builtins"
    assert _new_mo.name == "builtins"

# Generated at 2022-06-14 02:12:04.012917
# Unit test for constructor of class MovedModule
def test_MovedModule():
    move = MovedModule("abcd", "abcd")
    assert move.name == "abcd"
    assert move.old == "abcd"
    assert move.new == "abcd"

    move = MovedModule("abc", "abc", "xyz")
    assert move.name == "abc"
    assert move.old == "abc"
    assert move.new == "xyz"

    move = MovedModule("abc", "abcd", "xyz")
    assert move.name == "abc"
    assert move.old == "abcd"
    assert move.new == "xyz"

# Generated at 2022-06-14 02:12:08.226825
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    """Test if class initializes correctly."""
    m = SixMovesTransformer()
    assert m.target == tuple([2, 7])
    assert m.rewrites == _get_rewrites()
    assert m.dependencies == ['six']

# Generated at 2022-06-14 02:12:12.411947
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    move = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO", 'foo')
    assert move.name == "cStringIO"
    assert move.new_mod == "io"
    assert move.new_attr == "foo"


# Generated at 2022-06-14 02:12:30.051461
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    obj = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert obj.name == "cStringIO"
    assert obj.new_mod == "io"
    assert obj.new_attr == "StringIO"

# Unit tests for the class MovedModule

# Generated at 2022-06-14 02:12:33.313904
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert all('six.moves' not in k for k, v in _get_rewrites())

# Generated at 2022-06-14 02:12:40.166812
# Unit test for constructor of class MovedModule
def test_MovedModule():
    moved_module = MovedModule("name", "old")
    assert moved_module.new == "name"
    assert moved_module.name == "name"
    assert moved_module.old == "old"

    moved_module = MovedModule("name", "old", "new")
    assert moved_module.new == "new"
    assert moved_module.name == "name"
    assert moved_module.old == "old"


# Generated at 2022-06-14 02:12:43.823744
# Unit test for constructor of class MovedModule
def test_MovedModule():
    foo = MovedModule('test', 'old', 'new')
    assert foo.name == 'test'
    assert foo.old == 'old'
    assert foo.new == 'new'


# Generated at 2022-06-14 02:12:54.031345
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():

    move = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert move.name == 'cStringIO'
    assert move.new_mod == 'io'
    assert move.new_attr == 'StringIO'

    move = MovedAttribute("cStringIO", "cStringIO", "io")
    assert move.name == 'cStringIO'
    assert move.new_mod == 'io'
    assert move.new_attr == 'cStringIO'

    move = MovedAttribute("filter", "itertools", "builtins", "ifilter", "filter")
    assert move.name == 'filter'
    assert move.new_mod == 'builtins'
    assert move.new_attr == 'filter'


# Generated at 2022-06-14 02:13:01.824881
# Unit test for constructor of class SixMovesTransformer

# Generated at 2022-06-14 02:13:13.528604
# Unit test for constructor of class MovedModule
def test_MovedModule():
    # Test constuctor of class MovedModule
    moved_module = MovedModule("builtins", "__builtin__")
    assert moved_module.name == "builtins"
    assert moved_module.old == "__builtin__"
    assert moved_module.new == "builtins"

    # Test constuctor of class MovedModule when new is not specified
    moved_module = MovedModule("builtins", "__builtin__")
    assert moved_module.name == "builtins"
    assert moved_module.old == "__builtin__"
    assert moved_module.new == "builtins"

    # Test constuctor of class MovedModule when old is not specified
    moved_module = MovedModule("builtins", new="__builtin__")
    assert moved_module.name == "builtins"
    assert moved

# Generated at 2022-06-14 02:13:21.093482
# Unit test for constructor of class MovedModule
def test_MovedModule():
    import six.moves
    test1 = MovedModule("test1", "test2")
    assert test1.name == "test1"
    assert test1.new == "test1"
    assert test1.old == "test2"
    test2 = MovedModule("test1", "test2", "test3")
    assert test2.name == "test1"
    assert test2.new == "test3"
    assert test2.old == "test2"
    # Test to make sure it shows up in Six
    assert six.moves.test1 is not None


# Generated at 2022-06-14 02:13:32.403519
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    moved_attribute1 = MovedAttribute('foo', 'bar', 'baz', 'qux', 'quux')
    assert moved_attribute1.name == 'foo'
    assert moved_attribute1.new_mod == 'baz'
    assert moved_attribute1.new_attr == 'quux'

    moved_attribute2 = MovedAttribute('foo', 'bar', 'baz', 'qux')
    assert moved_attribute2.name == 'foo'
    assert moved_attribute2.new_mod == 'baz'
    assert moved_attribute2.new_attr == 'qux'

    moved_attribute3 = MovedAttribute('foo', 'bar', 'baz')
    assert moved_attribute3.name == 'foo'
    assert moved_attribute3.new_mod == 'baz'
    assert moved_attribute3.new

# Generated at 2022-06-14 02:13:34.164962
# Unit test for constructor of class MovedModule
def test_MovedModule():
    with pytest.raises(TypeError):
        MovedModule()

# Generated at 2022-06-14 02:14:16.201176
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    from libcst.metadata import PositionProvider, QualifiedName
    from libcst.matchers import Attribute
    from libcst.matchers import Name
    from libcst.matchers import ImportFrom
    from libcst.matchers import Import
    import libcst as cst
    smt = SixMovesTransformer(None, None)
    v = smt.visit_ImportFrom(
        cst.ImportFrom(module='six.moves.urllib.parse',
                       names=[
                           cst.Alias(name='parse_qs', asname=None)
                       ],
                       level=0)
    )
    assert v.module == cst.Name(value='six.moves.urllib.parse')

# Generated at 2022-06-14 02:14:20.981496
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    test_attr = MovedAttribute("test", "test_mod", "new_mod")
    assert test_attr.name == 'test'
    assert test_attr.new_mod == 'new_mod'
    assert test_attr.new_attr == 'test'


# Generated at 2022-06-14 02:14:27.677907
# Unit test for constructor of class MovedModule
def test_MovedModule():
    module = MovedModule("name", "old", "new")
    assert module.name == "name"
    assert module.old == "old"
    assert module.new == "new"
    module = MovedModule("name", "old")
    assert module.name == "name"
    assert module.old == "old"
    assert module.new == "name"


# Generated at 2022-06-14 02:14:29.980068
# Unit test for constructor of class MovedModule
def test_MovedModule():
    moved_module = MovedModule("test", "test", "test")
    assert moved_module.name == "test"
    assert moved_module.new == "test"


# Generated at 2022-06-14 02:14:33.435255
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    attributes = MovedAttribute("StringIO", "cStringIO", "io", "StringIO")
    assert attributes.name == "StringIO"
    assert attributes.new_mod == "io"
    assert attributes.new_attr == "StringIO"


# Generated at 2022-06-14 02:14:36.607925
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    expected = dict(
        _get_rewrites()
    )
    actual = SixMovesTransformer.rewrites
    for key, value in expected.items():
        assert key in actual
        assert value == actual[key]
    assert expected.keys() == actual.keys()

# Generated at 2022-06-14 02:14:48.501583
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert MovedAttribute('cStringIO', 'cStringIO', 'io', 'StringIO') == \
        MovedAttribute('cStringIO', 'cStringIO', 'io', 'StringIO')
    assert MovedAttribute('cStringIO', 'cStringIO', 'io', 'StringIO') != \
        MovedAttribute('cStringIO', 'cStringIO', 'io', 'StringIO2')
    assert MovedAttribute('cStringIO', 'cStringIO', 'io', 'StringIO') != \
        MovedAttribute('cStringIO', 'cStringIO', 'io2', 'StringIO')
    assert MovedAttribute('cStringIO', 'cStringIO', 'io', 'StringIO') != \
        MovedAttribute('cStringIO', 'cStringIO2', 'io', 'StringIO')

# Generated at 2022-06-14 02:14:51.386807
# Unit test for constructor of class MovedModule
def test_MovedModule():
    assert MovedModule('builtins','__builtin__')
    assert MovedModule('tkinter_tix', 'Tix', 'tkinter.tix')

# Generated at 2022-06-14 02:14:58.931694
# Unit test for constructor of class MovedModule
def test_MovedModule():
    m = MovedModule('foo', 'bar')
    assert m.name == 'foo'
    assert m.new == 'bar'
    assert m.old == 'bar'
    m = MovedModule('foo', 'bar', 'baz')
    assert m.name == 'foo'
    assert m.new == 'baz'
    assert m.old == 'bar'

# Generated at 2022-06-14 02:15:10.484384
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    from lib2to3.pgen2.tokenize import tokenize
    import io
    src = """
from foo import bar
from foo.bar import baz
from foo.bar.baz import xxx
from foo.bar.baz import yyy
from baz.foo import bar
from baz.foo.bar import baz
from baz.foo.bar.baz import xxx
from baz.foo.bar.baz import yyy
"""