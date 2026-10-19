

# Generated at 2022-06-14 02:06:08.432436
# Unit test for constructor of class MovedModule
def test_MovedModule():
    obj = MovedModule("name", "old", "new")
    assert obj.name == "name"
    assert obj.old == "old"
    assert obj.new == "new"
    obj = MovedModule("name", "old")
    assert obj.name == "name"
    assert obj.old == obj.new == "name"
    obj = MovedModule("name", None, "new")
    assert obj.name == "name"
    assert obj.new == "new"
    assert obj.old is None

# Generated at 2022-06-14 02:06:12.701870
# Unit test for constructor of class MovedModule
def test_MovedModule():
    mm = MovedModule('name', 'old', 'new')
    assert mm.name == 'name'
    assert mm.old == 'old'
    assert mm.new == 'new'

    mm = MovedModule('name', 'old')
    assert mm.name == 'name'
    assert mm.old == 'old'
    assert mm.new == 'name'



# Generated at 2022-06-14 02:06:23.695301
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    class FakeRewriter(object):
        def __init__(self):
            self.imports = []
            self.new_imports = []

        def add_dynamic_import(self, module_name):
            self.imports.append(module_name)

        def add_new_dynamic_import(self, module_name):
            self.new_imports.append(module_name)

    rewriter = FakeRewriter()
    rewriter_with_six = SixMovesTransformer(rewriter)

    assert rewriter_with_six.rewriters[0].imports == ['six']
    assert rewriter_with_six.rewriters[0].new_imports == []

    rewriter_with_six.rewrite_imports('six.moves')


# Generated at 2022-06-14 02:06:32.575481
# Unit test for constructor of class SixMovesTransformer

# Generated at 2022-06-14 02:06:33.510938
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    # type: () -> None
    pass

# Generated at 2022-06-14 02:06:37.647407
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    x = SixMovesTransformer()
    assert x.target == (2, 7)
    assert len(x.rewrites) == len(_moved_attributes + prefixed_moves)
    assert x.dependencies == ['six']


if __name__ == '__main__':
    x = SixMovesTransformer()
    print(x.rewrites)

# Generated at 2022-06-14 02:06:45.911875
# Unit test for constructor of class MovedModule
def test_MovedModule():
    assert MovedModule("tkinter", "Tkinter") == MovedModule("tkinter", "Tkinter")
    assert MovedModule("tkinter", "Tkinter", "tkinter") == MovedModule("tkinter", "Tkinter", "tkinter"
                                                               )
    assert MovedModule("tkinter_tix", "Tix", "tkinter.tix") == MovedModule("tkinter_tix", "Tix",
                                                                   "tkinter.tix")



# Generated at 2022-06-14 02:06:54.496010
# Unit test for constructor of class MovedModule
def test_MovedModule():
    # Correct object
    assert MovedModule("abc", "abc", "abc")
    # Name has to be a string
    with pytest.raises(TypeError):
        MovedModule(["abc"], "abc", "abc")
    # Old has to be a string
    with pytest.raises(TypeError):
        MovedModule("abc", ["abc"], "abc")
    # New has to be a string if given
    with pytest.raises(TypeError):
        MovedModule("abc", "abc", ["abc"])


# Generated at 2022-06-14 02:06:58.524759
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    moveattr = MovedAttribute("new_attr", "old_mod", "new_mod", "old_attr")
    assert moveattr.name == "new_attr"
    assert moveattr.new_mod == "new_mod"
    assert moveattr.new_attr == "old_attr"

# Generated at 2022-06-14 02:06:59.503803
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    MovedAttribute("test", "old", "new")

# Generated at 2022-06-14 02:07:03.280852
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    """Test constructor of class SixMovesTransformer"""
    SixMovesTransformer().transformer_init()
    assert True

# Generated at 2022-06-14 02:07:09.826935
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    attribs = []
    attribs.append(MovedAttribute('move1', 'old1', 'new1', 'oldattr1'))
    attribs.append(MovedAttribute('move2', 'old2', 'new2', 'oldattr2', 'newattr2'))
    attribs.append(MovedAttribute('move3', 'old3', None, 'oldattr3', 'newattr3'))
    attribs.append(MovedAttribute('move4', 'old4', 'new4', None, 'newattr4'))
    attribs.append(MovedAttribute('move5', 'old5', None, None, 'newattr5'))
    attribs.append(MovedAttribute('move6', 'old6', 'new6', None))

# Generated at 2022-06-14 02:07:12.847947
# Unit test for constructor of class MovedModule
def test_MovedModule():
    modules = MovedModule('foo', 'foo', 'bar')
    assert modules.name == 'foo'
    assert modules.new == 'bar'



# Generated at 2022-06-14 02:07:28.742819
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    transformer = SixMovesTransformer()

# Generated at 2022-06-14 02:07:41.614086
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    # this should always succeed
    MovedAttribute("name", "old_mod", "new_mod", "old_attr", "new_attr")
    MovedAttribute("name", "old_mod", "new_mod", "old_attr", None)
    MovedAttribute("name", "old_mod", "new_mod", None, "new_attr")
    MovedAttribute("name", "old_mod", "new_mod", None, None)
    MovedAttribute("name", "old_mod", None, "old_attr", "new_attr")
    MovedAttribute("name", "old_mod", None, "old_attr", None)
    MovedAttribute("name", "old_mod", None, None, "new_attr")
    MovedAttribute("name", "old_mod", None, None, None)
    MovedAttribute

# Generated at 2022-06-14 02:07:48.404465
# Unit test for constructor of class MovedModule
def test_MovedModule():
    mod = MovedModule('urllib', '_urllib')
    assert mod.name == 'urllib'
    assert mod.new == 'urllib'

    mod = MovedModule('urllib', '_urllib', 'six.moves.urllib')
    assert mod.new == 'six.moves.urllib'



# Generated at 2022-06-14 02:07:58.669067
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    import six
    import six.moves.urllib.parse as urlparse
    assert SixMovesTransformer.rewrites[0] == \
        ('urllib.parse.ParseResult', 'six.moves.urllib_parse.ParseResult')
    assert SixMovesTransformer.rewrites[-1] == \
        ('urllib.robotparser.RobotFileParser', 'six.moves.urllib_robotparser.RobotFileParser')
    assert SixMovesTransformer.rewrites[1] == \
        ('urllib.parse.SplitResult', 'six.moves.urllib_parse.SplitResult')

# Generated at 2022-06-14 02:08:08.168557
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    m1 = MovedAttribute('cStringIO', 'cStringIO', None)
    assert m1.new_mod == 'cStringIO'
    assert m1.new_attr == 'cStringIO'
    assert m1.name == 'cStringIO'

    m2 = MovedAttribute('StringIO', 'cStringIO', None, 'StringIO', None)
    assert m2.new_mod == 'cStringIO'
    assert m2.new_attr == 'StringIO'
    assert m2.name == 'StringIO'

    m3 = MovedAttribute('StringIO', 'cStringIO', None, 'StringIO', 'StringIO')
    assert m3.new_mod == 'cStringIO'
    assert m3.new_attr == 'StringIO'
    assert m3.name == 'StringIO'

    m

# Generated at 2022-06-14 02:08:10.479199
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    with pytest.raises(TypeError):
        MovedAttribute()
        MovedAttribute(1)
        MovedAttribute(1,2)



# Generated at 2022-06-14 02:08:16.593511
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert (MovedAttribute('StringIO', 'cStringIO', 'io', 'StringIO') ==
        MovedAttribute('StringIO', 'cStringIO', 'io', 'StringIO'))
    assert MovedAttribute('StringIO', 'cStringIO', 'io',
                          'StringIO') is not MovedAttribute('StringIO', 'cStringIO', 'io', 'StringIO')  # noqa
    assert MovedAttribute('StringIO', 'cStringIO', 'io',
                          'StringIO') is not MovedAttribute('StringIO', 'cStringIO', 'io', 'String')  # noqa
    assert MovedAttribute('StringIO', 'cStringIO', 'io',
                          'StringIO') is not MovedAttribute('String', 'cStringIO', 'io', 'StringIO')  # noqa
    assert MovedAttribute

# Generated at 2022-06-14 02:08:31.569898
# Unit test for constructor of class MovedAttribute

# Generated at 2022-06-14 02:08:40.219702
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    moved_attribute = MovedAttribute('name', 'old', 'new')
    assert moved_attribute.name == 'name'
    assert moved_attribute.new_mod == 'new'
    assert moved_attribute.new_attr == 'name'
    assert moved_attribute.old_name == 'name'
    moved_attribute = MovedAttribute('name', 'old', 'new', 'old_attr', 'new_attr')
    assert moved_attribute.name == 'name'
    assert moved_attribute.new_mod == 'new'
    assert moved_attribute.new_attr == 'new_attr'
    assert moved_attribute.old_name == 'old_attr'



# Generated at 2022-06-14 02:08:41.922956
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    SixMovesTransformer()

# Generated at 2022-06-14 02:08:55.044766
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    move = MovedAttribute("name", "old_mod", "new_mod", "old_attr", "new_attr")
    assert move.name == "name"
    assert move.new_mod == "new_mod"
    assert move.new_attr == "new_attr"
    move = MovedAttribute("name", "old_mod", "new_mod")
    assert move.name == "name"
    assert move.new_mod == "name"
    assert move.new_attr == "name"
    move = MovedAttribute("name", "old_mod", "new_mod", "old_attr", None)
    assert move.name == "name"
    assert move.new_mod == "new_mod"
    assert move.new_attr == "old_attr"

# Generated at 2022-06-14 02:09:05.041136
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    attr = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert attr.name == "cStringIO"
    assert attr.new_mod == "io"
    assert attr.new_attr == "StringIO"

    attr = MovedAttribute("cStringIO", "cStringIO", "io")
    assert attr.name == "cStringIO"
    assert attr.new_mod == "io"
    assert attr.new_attr == "cStringIO"

    attr = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO", "StringIO2")
    assert attr.name == "cStringIO"
    assert attr.new_mod == "io"
    assert attr.new_attr == "StringIO2"

# Generated at 2022-06-14 02:09:08.147703
# Unit test for constructor of class MovedModule
def test_MovedModule():
    obj = MovedModule('name', 'old')
    assert obj.name == 'name'
    assert obj.new == 'name'

# Generated at 2022-06-14 02:09:14.750263
# Unit test for constructor of class MovedModule
def test_MovedModule():
    MM = MovedModule("mod", "old", "new")
    assert MM.name == "mod"
    assert MM.old == "old"
    assert MM.new == "new"
    MM = MovedModule("mod", "old")
    assert MM.name == "mod"
    assert MM.old == "old"
    assert MM.new == "mod"



# Generated at 2022-06-14 02:09:19.124698
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    """Test function for constructor of class SixMovesTransformer"""
    addback_rewrites = list(SixMovesTransformer.rewrites)
    SixMovesTransformer.rewrites = []
    with pytest.raises(NotImplementedError):
        SixMovesTransformer()
    SixMovesTransformer.rewrites = addback_rewrites

# Generated at 2022-06-14 02:09:25.682609
# Unit test for constructor of class MovedModule
def test_MovedModule():
    """
    Test the constructor of class MovedModule
    """

    moved_module_test = MovedModule("test", "old", "new")
    assert moved_module_test.name == "test"
    assert moved_module_test.old == "old"
    assert moved_module_test.new == "new"

# Generated at 2022-06-14 02:09:29.745735
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    move=MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")

    assert move.name=='cStringIO'
    assert move.new_mod=='cStringIO'
    assert move.new_attr=='StringIO'

# Generated at 2022-06-14 02:09:49.240196
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    transformer = SixMovesTransformer()

# Generated at 2022-06-14 02:09:56.813879
# Unit test for constructor of class MovedModule
def test_MovedModule():
  assert MovedModule("name", "old").name == "name"
  assert MovedModule("name", "old").old == "old"
  assert MovedModule("name", "old").new == "name"
  assert MovedModule("name", "old", "new").name == "name"
  assert MovedModule("name", "old", "new").old == "old"
  assert MovedModule("name", "old", "new").new == "new"
  

# Generated at 2022-06-14 02:10:03.629172
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():

    assert MovedAttribute('cStringIO', 'cStringIO', 'io', 'StringIO').new_attr == 'StringIO'
    assert MovedAttribute('cStringIO', 'cStringIO', 'io', old_attr='StringIO').new_attr == 'StringIO'
    assert MovedAttribute('cStringIO', 'cStringIO', 'io').new_attr == 'cStringIO'


# Generated at 2022-06-14 02:10:06.377039
# Unit test for constructor of class MovedModule
def test_MovedModule():
    mod = MovedModule("test", "test")
    assert mod.name == 'test'
    assert mod.new == 'test'

# Generated at 2022-06-14 02:10:09.783863
# Unit test for constructor of class MovedModule
def test_MovedModule():
    test_obj = MovedModule("name", "old", "new")
    assert test_obj.name == "name"
    assert test_obj.old == "old"
    assert test_obj.new == "new"

# Generated at 2022-06-14 02:10:15.236228
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    ma = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert ma.name == "cStringIO"
    assert ma.new_mod == "io"
    assert ma.new_attr == "StringIO"

    assert ma.new_attr == "StringIO"

# Generated at 2022-06-14 02:10:25.124728
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    print(SixMovesTransformer.rewrites)
    test_input = "print(six.moves.urllib.parse.urlparse)"
    transformer = SixMovesTransformer()
    assert transformer.test(test_input)
    output = transformer.transform(test_input)
    assert output == "print(urllib.parse.urlparse)"

    test_input = "import six.moves.urllib.parse"
    transformer = SixMovesTransformer()
    assert transformer.test(test_input)
    output = transformer.transform(test_input)
    assert output == "import urllib.parse"

#

# Generated at 2022-06-14 02:10:35.245050
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    t = SixMovesTransformer()

# Generated at 2022-06-14 02:10:46.322687
# Unit test for constructor of class SixMovesTransformer

# Generated at 2022-06-14 02:10:53.028482
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    """Test for constructor of class SixMovesTransformer"""
    assert SixMovesTransformer.target == (2, 7)
    assert isinstance(SixMovesTransformer.dependencies, list)
    assert all([isinstance(x, str) for x in SixMovesTransformer.dependencies])
    assert SixMovesTransformer.rewrites == _get_rewrites()

# Generated at 2022-06-14 02:11:18.628367
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    """Special class for handling six moves: MovedAttribute."""
    m1 = MovedAttribute("Attribute1", "Module", "NewModule",
                        "Attribute", "NewAttribute")
    m2 = MovedAttribute("Attribute2", "Module", "NewModule")
    m3 = MovedAttribute("Attribute3", "Module")
    assert m1.name == "Attribute1"
    assert m1.new_mod == "NewModule"
    assert m1.new_attr == "NewAttribute"
    assert m2.name == "Attribute2"
    assert m2.new_mod == "NewModule"
    assert m2.new_attr == "Attribute2"
    assert m3.name == "Attribute3"
    assert m3.new_mod == "Attribute3"
    assert m3.new_attr == "Attribute3"

#

# Generated at 2022-06-14 02:11:26.267557
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert MovedAttribute('old', 'old_mod', 'new_mod', 'old_attr', 'new_attr').name == 'old'
    assert MovedAttribute('old', 'old_mod', 'new_mod', 'old_attr', 'new_attr').new_mod == 'new_mod'
    assert MovedAttribute('old', 'old_mod', 'new_mod', 'old_attr', 'new_attr').new_attr == 'new_attr'
    assert MovedAttribute('old', 'old_mod', 'new_mod', 'old_attr', None).new_attr == 'old_attr'
    assert MovedAttribute('old', 'old_mod', 'new_mod', None, None).new_attr == 'old'
    assert MovedAttribute('old', 'old_mod', None).new_mod == 'old'
   

# Generated at 2022-06-14 02:11:38.273220
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    a = MovedAttribute("test1", "test2", "test3", "test4", "test5")
    b = MovedAttribute("test1", "test2", "test3", "test4", None)
    c = MovedAttribute("test1", "test2", "test3", None, "test5")
    d = MovedAttribute("test1", "test2", "test3", None, None)
    e = MovedAttribute("test1", "test2", None)
    expected = ('test1', 'test2', 'test3', 'test4', 'test5')
    assert a == expected
    expected = ('test1', 'test2', 'test3', 'test4', 'test4')
    assert b == expected

# Generated at 2022-06-14 02:11:51.747816
# Unit test for constructor of class SixMovesTransformer

# Generated at 2022-06-14 02:11:55.701926
# Unit test for constructor of class MovedModule
def test_MovedModule():
    try:
        x = MovedModule("builtins", "__builtin__")
        if x.name != "builtins" or x.old != "__builtin__" or x.new != "builtins":
            raise RuntimeError("MovedModule failure")
        print("Success!")
    except:
        raise RuntimeError("MovedModule failure")


# Generated at 2022-06-14 02:12:03.624455
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    moved_attribute = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert moved_attribute.name == "cStringIO"
    assert moved_attribute.new_mod == "io"
    assert moved_attribute.new_attr == "StringIO"


if __name__ == '__main__':  # pragma: no cover
    import pytest  # type: ignore
    pytest.main(args=['-s', __file__])

# Generated at 2022-06-14 02:12:08.831673
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    moved_attribute = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert moved_attribute.name == "cStringIO"
    assert moved_attribute.new_mod == "io"
    assert moved_attribute.new_attr == "StringIO"


# Generated at 2022-06-14 02:12:19.252691
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    import re

    def check():
        return True

    def check_regex(expected, actual):
        return re.match(expected, actual) is not None

    def check_exact(expected, actual):
        return expected == actual

    def check_output(test_name, expected, actual, checker):
        if checker(expected, actual):
            print('Passed {}: {}'.format(test_name, actual))
        else:
            print('Failed {}: expected {}, got {}'.format(test_name, expected, actual))

    transformer = SixMovesTransformer()
    test_result = 'six.moves'
    assert check_regex(test_result, transformer.get_import_prefix())

# Generated at 2022-06-14 02:12:22.861327
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    transformer = SixMovesTransformer({})
    assert transformer.dependencies == ['six']
    assert len(transformer.rewrites) > 0
    assert transformer.target == (2, 7)
    assert transformer.comment == 'py2 -> py3 (SixMovesTransformer)'

# Generated at 2022-06-14 02:12:24.500782
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():  # pylint: disable=missing-docstring
    # Just make sure it won't fail.
    SixMovesTransformer()

# Generated at 2022-06-14 02:12:59.055787
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

    move = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO", "StringIO")
    assert move.name == "cStringIO"
    assert move.new_mod == "io"
    assert move.new_attr == "StringIO"


# Generated at 2022-06-14 02:13:05.056463
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    attr = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert attr.name == "cStringIO"
    assert attr.new_mod == "io"
    assert attr.new_attr == "StringIO"

    attr = MovedAttribute("cStringIO", "cStringIO", "io")
    assert attr.name == "cStringIO"
    assert attr.new_mod == "io"
    assert attr.new_attr == "cStringIO"

    attr = MovedAttribute("cStringIO", "cStringIO", None)
    assert attr.name == "cStringIO"
    assert attr.new_mod == "cStringIO"
    assert attr.new_attr == "cStringIO"


# Generated at 2022-06-14 02:13:09.407823
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    t = SixMovesTransformer()
    assert t.target == SixMovesTransformer.target
    assert t.rewrites == SixMovesTransformer.rewrites
    assert t.dependencies == SixMovesTransformer.dependencies


# Generated at 2022-06-14 02:13:11.873113
# Unit test for constructor of class MovedModule
def test_MovedModule():
    assert MovedModule("foo", "bar").name == "foo"
    assert MovedModule("foo", "bar").new == "foo"

# Generated at 2022-06-14 02:13:16.753044
# Unit test for constructor of class MovedModule
def test_MovedModule():
    # GIVEN
    testMovedModule = MovedModule("testName", "testOldName")
    # THEN
    assert testMovedModule.name == "testName"
    assert testMovedModule.old == "testOldName"
    assert testMovedModule.new == "testName"


# Generated at 2022-06-14 02:13:19.499124
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    """This function tests the constructor of the class SixMovesTransformer."""
    trans = SixMovesTransformer()


# Generated at 2022-06-14 02:13:22.365892
# Unit test for constructor of class MovedModule
def test_MovedModule():
    mm = MovedModule("math","basicmath")
    assert mm.name == "math"
    assert mm.new == "math"


# Generated at 2022-06-14 02:13:27.261367
# Unit test for constructor of class MovedModule
def test_MovedModule():
    """ Make sure that, when MovedModule is called with a single argument, the
    new attribute will take the name of the argument.
    """
    m = MovedModule('something')
    assert m.name == 'something'
    assert m.new == 'something'


# Generated at 2022-06-14 02:13:29.412986
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    for path, target in SixMovesTransformer._rewrites:
        assert_equal(SixMovesTransformer._get_import_name(path), target)

# Generated at 2022-06-14 02:13:31.875322
# Unit test for constructor of class MovedModule
def test_MovedModule():
    moved_module = MovedModule("name", "old", "new")
    assert moved_module.name == "name"
    assert moved_module.old == "old"
    assert moved_module.new == "new"


# Generated at 2022-06-14 02:14:33.987771
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert MovedAttribute('name', 'old_mod', 'new_mod').__class__.__name__ == 'MovedAttribute'



# Generated at 2022-06-14 02:14:37.639869
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    """Test SixMovesTransformer constructor."""
    assert SixMovesTransformer.target == (2, 7)
    assert len(SixMovesTransformer.rewrites) == 142
    assert len(SixMovesTransformer.dependencies) == 1


# Generated at 2022-06-14 02:14:47.701452
# Unit test for constructor of class SixMovesTransformer

# Generated at 2022-06-14 02:15:01.230284
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    m = MovedAttribute('name', 'old_mod', 'new_mod')
    assert m.name == 'name'
    assert m.new_mod == 'new_mod'
    assert m.new_attr == 'name'
    m = MovedAttribute('name', 'old_mod', 'new_mod', 'old_attr', 'new_attr')
    assert m.name == 'name'
    assert m.new_mod == 'new_mod'
    assert m.new_attr == 'new_attr'
    m = MovedAttribute('name', 'old_mod', 'new_mod', 'old_attr')
    assert m.name == 'name'
    assert m.new_mod == 'new_mod'
    assert m.new_attr == 'old_attr'


# Generated at 2022-06-14 02:15:07.951539
# Unit test for constructor of class MovedModule
def test_MovedModule():
    m = MovedModule('name', 'old')
    assert m.name == 'name'
    assert m.old == 'old'
    assert m.new == 'name'
    m = MovedModule('name', 'old', 'new')
    assert m.name == 'name'
    assert m.old == 'old'
    assert m.new == 'new'


# Generated at 2022-06-14 02:15:12.168924
# Unit test for constructor of class MovedModule
def test_MovedModule():
    module = MovedModule("winreg", "_winreg")
    assert module.name == "winreg"
    assert module.new == "winreg"


# Generated at 2022-06-14 02:15:16.774285
# Unit test for constructor of class MovedModule
def test_MovedModule():
    mm = MovedModule('foo', 'bar')
    assert mm.name == 'foo'
    assert mm.new == 'bar'

    mm = MovedModule('foo', 'bar', 'baz')
    assert mm.name == 'foo'
    assert mm.new == 'baz'

# Generated at 2022-06-14 02:15:26.142721
# Unit test for constructor of class SixMovesTransformer

# Generated at 2022-06-14 02:15:28.225025
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert SixMovesTransformer.rewrites != set()

# Generated at 2022-06-14 02:15:33.423036
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    moved_attribute = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert moved_attribute.name == "cStringIO"
    assert moved_attribute.new_mod == "io"

# Unit tests for constructor of class MovedModule