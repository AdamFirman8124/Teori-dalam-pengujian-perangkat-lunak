

# Generated at 2022-06-14 02:06:04.876454
# Unit test for constructor of class MovedModule
def test_MovedModule():
    m = MovedModule('name', 'old', 'new')
    assert m.name == 'name'
    assert m.new == 'new'

# Generated at 2022-06-14 02:06:06.063679
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    SixMovesTransformer()


# Generated at 2022-06-14 02:06:12.378551
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    moved_attribute = MovedAttribute('cStringIO', 'cStringIO', 'io', 'StringIO', 'StringIO')
    assert moved_attribute.name == 'cStringIO'
    assert moved_attribute.old_mod == 'cStringIO'
    assert moved_attribute.new_mod == 'io'
    assert moved_attribute.old_attr == 'StringIO'
    assert moved_attribute.new_attr == 'StringIO'



# Generated at 2022-06-14 02:06:14.170758
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    s = SixMovesTransformer(None)
    assert s._check_target(2, 7)



# Generated at 2022-06-14 02:06:18.414537
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    move = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert move.name == "cStringIO"
    assert move.new_mod == "io"
    assert move.new_attr == "StringIO"


# Generated at 2022-06-14 02:06:20.105830
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    st = SixMovesTransformer()
    assert len(st.rewrites) > 0

# Generated at 2022-06-14 02:06:30.066099
# Unit test for constructor of class SixMovesTransformer

# Generated at 2022-06-14 02:06:33.735900
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    ma = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert ma.name == "cStringIO"
    assert ma.new_mod == "io"
    assert ma.new_attr == "StringIO"


# Generated at 2022-06-14 02:06:40.959127
# Unit test for constructor of class MovedModule
def test_MovedModule():
    t11 = MovedModule("name", "old", "new")

    t12 = MovedModule("name", "old")
    t13 = MovedModule("name", "old", "name")

    t21 = MovedModule("name", "name")
    t22 = MovedModule("name", "name", "name")

    t3 = MovedModule("name", "name", "new")

    assert t11.name == 'name'
    assert t11.old == 'old'
    assert t11.new == 'new'

    assert t12.name == 'name'
    assert t12.old == 'old'
    assert t12.new == 'name'

    assert t13.name == 'name'
    assert t13.old == 'old'
    assert t13.new == 'name'

    assert t21

# Generated at 2022-06-14 02:06:43.797179
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    t = SixMovesTransformer()
    assert t.rewrites == _get_rewrites()
    assert t.target == (2, 7)
    assert t.dependencies == ['six']

# Generated at 2022-06-14 02:06:51.655233
# Unit test for constructor of class MovedModule
def test_MovedModule():
    assert MovedModule('hello', 'hello').name == 'hello'
    assert MovedModule('hello', 'hello').new == 'hello'
    assert MovedModule('hello', 'HELLO', 'hello').name == 'hello'
    assert MovedModule('hello', 'HELLO', 'hello').new == 'hello'

    assert MovedModule('hello', 'hello', 'Hello').name == 'hello'
    assert MovedModule('hello', 'hello', 'Hello').new == 'Hello'
    assert MovedModule('hello', 'HELLO', 'Hello').name == 'hello'
    assert MovedModule('hello', 'HELLO', 'Hello').new == 'Hello'



# Generated at 2022-06-14 02:06:56.868826
# Unit test for constructor of class MovedModule
def test_MovedModule():
    moved_module = MovedModule("os", "os", "os")
    assert moved_module.name == "os"
    assert moved_module.new == "os"
    moved_module = MovedModule("abc", "xyz", "cba")
    assert moved_module.name == "abc"
    assert moved_module.new == "cba"

# Generated at 2022-06-14 02:07:07.289227
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert MovedAttribute("name", "old_mod", "new_mod", "old_attr",
                          "new_attr").name == "name"
    assert MovedAttribute("name", "old_mod", "new_mod", "old_attr",
                          "new_attr").new_mod == "new_mod"
    assert MovedAttribute("name", "old_mod", "new_mod", "old_attr",
                          "new_attr").new_attr == "new_attr"
    assert MovedAttribute("name", "old_mod", "new_mod").name == "name"
    assert MovedAttribute("name", "old_mod", "new_mod").new_mod == "new_mod"
    assert MovedAttribute("name", "old_mod", "new_mod").new_attr == "name"

# Generated at 2022-06-14 02:07:10.830083
# Unit test for constructor of class MovedModule
def test_MovedModule():
    assert MovedModule("abc", "abc") == MovedModule("abc", "abc")
    assert MovedModule("abc", "def") != MovedModule("def", "ghi")
    assert MovedModule("abc", "def", "ghi") == MovedModule("abc", "def", "ghi")

# Generated at 2022-06-14 02:07:19.534143
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    a = MovedAttribute('name', 'old_mod', 'new_mod')
    assert a.name == 'name'
    assert a.new_mod == 'new_mod'
    assert a.new_attr == 'name'
    a = MovedAttribute('name', 'old_mod', 'new_mod', 'old_attr', 'new_attr')
    assert a.name == 'name'
    assert a.new_mod == 'new_mod'
    assert a.new_attr == 'new_attr'


# Generated at 2022-06-14 02:07:23.937983
# Unit test for constructor of class MovedModule
def test_MovedModule():
    mod = MovedModule("x", "y", "a")
    assert mod.name == "x"
    assert mod.old == "y"
    assert mod.new == "a"
    mod = MovedModule("x", "y")
    assert mod.name == "x"
    assert mod.old == "y"
    assert mod.new == "x"

# Generated at 2022-06-14 02:07:36.778769
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    a = MovedAttribute("name0", "old_mod0", "new_mod0", "old_attr0", "new_attr0")
    assert a.name == "name0"
    assert a.new_mod == "new_mod0"
    assert a.new_attr == "new_attr0"
    a = MovedAttribute("name1", "old_mod1", "new_mod1", "old_attr1")
    assert a.name == "name1"
    assert a.new_mod == "new_mod1"
    assert a.new_attr == "old_attr1"
    a = MovedAttribute("name2", "old_mod2", "new_mod2", new_attr="new_attr2")
    assert a.name == "name2"

# Generated at 2022-06-14 02:07:42.994115
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    a = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert a.name == "cStringIO"
    assert a.new_mod == "io"
    assert a.new_attr == "StringIO"

    b = MovedAttribute("cStringIO", "cStringIO", "io")
    assert b.new_attr == "cStringIO"


# Generated at 2022-06-14 02:07:54.854542
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert MovedAttribute("cStringIO", "cStringIO", "io", "StringIO").name == "cStringIO"
    assert MovedAttribute("cStringIO", "cStringIO", "io", "StringIO").old_attr == "StringIO"
    assert MovedAttribute("cStringIO", "cStringIO", "io", "StringIO").new_attr == "StringIO"

    assert MovedAttribute("cStringIO", "cStringIO", "io", "StringIO", "StringIO").old_attr == "StringIO"
    assert MovedAttribute("cStringIO", "cStringIO", "io", "StringIO", "StringIO").new_attr == "StringIO"

    assert MovedAttribute("cStringIO", "cStringIO", "io", "StringIO", "StringIO1").old_attr == "StringIO"
   

# Generated at 2022-06-14 02:08:03.269282
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    res = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert res.name == "cStringIO"
    assert res.new_mod == "io"
    assert res.new_attr == "StringIO"
    res = MovedAttribute("cStringIO", "cStringIO", "io")
    assert res.new_attr == "cStringIO"
    res = MovedAttribute("cStringIO", "cStringIO", None)
    assert res.new_mod == "cStringIO"
    res = MovedAttribute("cStringIO", None, None)
    assert res.new_mod == "cStringIO"



# Generated at 2022-06-14 02:08:10.309657
# Unit test for constructor of class MovedModule
def test_MovedModule():
    mod = MovedModule("builtins", "__builtin__")
    assert mod.name == "builtins"
    assert mod.new == "builtins"

    mod = MovedModule("configparser", "ConfigParser")
    assert mod.name == "configparser"
    assert mod.new == "configparser"


# Generated at 2022-06-14 02:08:12.947955
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert MovedAttribute('cStringIO', 'cStringIO', 'io', 'StringIO') == \
        MovedAttribute('cStringIO', 'cStringIO', 'io', 'StringIO')



# Generated at 2022-06-14 02:08:26.872488
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert MovedAttribute("cStringIO", "cStringIO", "io", "StringIO").name == "cStringIO"
    assert MovedAttribute("cStringIO", "cStringIO", "io", "StringIO").old_attr == "StringIO"
    assert MovedAttribute("cStringIO", "cStringIO", "io", "StringIO").new_mod == \
        "io"
    assert MovedAttribute("cStringIO", "cStringIO", "io", "StringIO").new_attr == \
        "StringIO"
    # Test for default new_mod
    assert MovedAttribute("cStringIO", "cStringIO", None, "StringIO").new_mod == \
        "cStringIO"
    # Test for default new_attr

# Generated at 2022-06-14 02:08:30.161683
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    t = SixMovesTransformer()
    assert t.target == (2, 7)
    assert len(t.rewrites) == len(_get_rewrites())

# Generated at 2022-06-14 02:08:37.200921
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    # Verify that the rewrites are sorted on the full name
    # and that they don't contain duplicates:
    previous_rewrite = ''
    for rewrite in _get_rewrites():
        if rewrite[0] == previous_rewrite[0]:
            pytest.fail('duplicate key in rewrites: {}'.format(rewrite[0]))
        if rewrite[0] < previous_rewrite[0]:
            pytest.fail('rewrites not sorted')

# Generated at 2022-06-14 02:08:46.630366
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert str(MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")) == "cStringIO(cStringIO, io, StringIO, None)"

    assert str(MovedAttribute("cStringIO", "cStringIO", "io")) == "cStringIO(cStringIO, io, cStringIO, None)"

    assert str(MovedAttribute("cStringIO", "cStringIO", "io", "cStringIO", "cStringIO")) == "cStringIO(cStringIO, io, cStringIO, cStringIO)"



# Generated at 2022-06-14 02:08:51.153148
# Unit test for constructor of class MovedModule
def test_MovedModule():
    moved_module = MovedModule('py_src', 'src', 'dst')
    assert moved_module.name == 'py_src'
    assert moved_module.new == 'src'


# Generated at 2022-06-14 02:08:54.106550
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    obj = SixMovesTransformer()
    assert obj.target == (2, 7)
    assert obj.dependencies == ['six']

# Generated at 2022-06-14 02:08:56.911707
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    import_rewrite_test_case = SixMovesTransformer()
    assert isinstance(import_rewrite_test_case, SixMovesTransformer)

# Generated at 2022-06-14 02:09:02.458716
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    # Set attr to None, it should be set to name
    move = MovedAttribute('name', 'old_mod', None)
    assert move.new_attr == 'name'
    # Set old_attr and new_attr, new_attr should not be overwritten
    move = MovedAttribute('name', 'old_mod', None, 'old_attr', 'new_attr')
    assert move.new_attr == 'new_attr'

# Generated at 2022-06-14 02:09:11.965788
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    """Test class SixMovesTransformer"""
    transformer = SixMovesTransformer('six.moves.urllib_parse', 'six.moves.urllib_parse')

# Generated at 2022-06-14 02:09:16.859824
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    transformer = SixMovesTransformer()

    assert transformer.rewrites[0] == ('urllib.parse.ParseResult',
                                       'six.moves.urllib_parse.ParseResult')
    assert transformer.rewrites[-1] == ('urllib.robotparser.RobotFileParser',
                                        'six.moves.urllib_robotparser.RobotFileParser')

# Generated at 2022-06-14 02:09:19.944321
# Unit test for constructor of class MovedModule
def test_MovedModule():
    move = MovedModule('module', 'oldmodule')
    assert move.name == 'module'
    assert move.new == 'oldmodule'

    move = MovedModule('module', 'oldmodule', 'newmodule')
    assert move.name == 'module'
    assert move.new == 'newmodule'

# Generated at 2022-06-14 02:09:30.744821
# Unit test for constructor of class MovedModule
def test_MovedModule():
    assert MovedModule('x', 'y') == MovedModule('x', 'y')
    assert MovedModule('x', 'y') != MovedModule('x', 'z')
    assert MovedModule('x', 'y') != MovedModule('z', 'y')
    assert MovedModule('x', 'y', 'z') == MovedModule('x', 'y', 'z')
    assert MovedModule('x', 'y') != MovedModule('x', 'y', 'z')
    assert MovedModule('x', 'y', 'z') != MovedModule('x', 'y', 'a')



# Generated at 2022-06-14 02:09:35.594406
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    ma = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert ma.name == "cStringIO"
    assert ma.new_mod == "io"
    assert ma.new_attr == "StringIO"



# Generated at 2022-06-14 02:09:37.750283
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")


# Generated at 2022-06-14 02:09:42.486790
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    move_attribute_obj = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert move_attribute_obj.name == "cStringIO"
    assert move_attribute_obj.new_mod == "io"
    assert move_attribute_obj.new_attr == "StringIO"

# Generated at 2022-06-14 02:09:46.299718
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    move = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert move.name == "cStringIO"
    assert move.new_mod == "io"
    assert move.new_attr == "StringIO"

# Generated at 2022-06-14 02:09:53.175009
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    # given
    move = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    # then
    assert move.name == "cStringIO"
    assert move.new_attr == "StringIO"
    assert move.new_mod == "io"


# Generated at 2022-06-14 02:10:01.619722
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

# Unit tests for constructor of class MovedAttribute

# Generated at 2022-06-14 02:10:25.444692
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert MovedAttribute('name', 'old_mod', 'new_mod').__dict__ == \
        {'name': 'name', 'new_mod': 'new_mod', 'new_attr': 'name'}
    assert MovedAttribute('name', 'old_mod', 'new_mod', 'old_attr', 'new_attr').__dict__ == \
        {'name': 'name', 'new_mod': 'new_mod', 'new_attr': 'new_attr'}
    assert MovedAttribute('name', 'old_mod', 'new_mod', old_attr='old_attr').__dict__ == \
        {'name': 'name', 'new_mod': 'new_mod', 'new_attr': 'old_attr'}

# Generated at 2022-06-14 02:10:34.433599
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    # assert that the first rewrite is ('.urllib.parse.urldefrag', 'six.moves.urllib_parse.urldefrag')
    assert SixMovesTransformer.rewrites[0] == ('.urllib.parse.urldefrag', 'six.moves.urllib_parse.urldefrag')
    # assert that the last rewrite is ('.urllib.robotparser.RobotFileParser', 'six.moves.urllib_robotparser.RobotFileParser')
    assert SixMovesTransformer.rewrites[-1] == ('.urllib.robotparser.RobotFileParser', 'six.moves.urllib_robotparser.RobotFileParser')

# Generated at 2022-06-14 02:10:46.177856
# Unit test for constructor of class MovedModule
def test_MovedModule():
    m_mod = MovedModule("configparser", "ConfigParser")
    assert m_mod.name == "configparser"
    assert m_mod.old == "ConfigParser"
    assert m_mod.new == "configparser"
    m_mod = MovedModule("configparser", "ConfigParser", "configparser")
    assert m_mod.old == "ConfigParser"
    assert m_mod.new == "configparser"
    m_mod = MovedModule("configparser", "ConfigParser", "configparser.configparser")
    assert m_mod.old == "ConfigParser"
    assert m_mod.new == "configparser.configparser"
    m_mod = MovedModule("configparser", "ConfigParser", new="configparser.configparser")
    assert m_mod.old == "ConfigParser"
    assert m_mod

# Generated at 2022-06-14 02:10:51.824862
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    # Assert that SixMovesTransformer contains all rewrites of six.moves
    # and is using the current six package.
    # This test needs to be updated whenever six changes.
    rewrites = list(_get_rewrites())
    assert rewrites == SixMovesTransformer.rewrites

# Generated at 2022-06-14 02:11:04.093621
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    # Test an attribute without new_attr
    attr = MovedAttribute("cStringIO", "cStringIO", "io")
    assert attr.name == "cStringIO"
    assert attr.new_mod == "io"
    assert attr.new_attr == "cStringIO"
    # Test an attribute without old_attr
    attr = MovedAttribute("cStringIO", "cStringIO", "io", new_attr="StringIO")
    assert attr.name == "cStringIO"
    assert attr.new_mod == "io"
    assert attr.new_attr == "StringIO"
    # Test an attribute with old_attr and new_attr
    attr = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO", "cStringIO")

# Generated at 2022-06-14 02:11:08.540171
# Unit test for constructor of class MovedModule
def test_MovedModule():
    module = MovedModule("tkinter_simpledialog", "SimpleDialog",
                         "tkinter.simpledialog")
    assert module.name == "tkinter_simpledialog"
    assert module.new == "tkinter.simpledialog"
    assert module.old == "SimpleDialog"



# Generated at 2022-06-14 02:11:14.847923
# Unit test for constructor of class MovedModule
def test_MovedModule():
    x = MovedModule('name', 'old', 'new')
    assert x.name == 'name'
    assert x.old == 'old'
    assert x.new == 'new'

    y = MovedModule('name', 'old')
    assert x.name == 'name'
    assert x.old == 'old'
    assert x.new == 'name'

# Generated at 2022-06-14 02:11:18.302991
# Unit test for constructor of class MovedModule
def test_MovedModule():
    m = MovedModule('a', 'b')
    assert m.name == 'a'
    assert m.new == 'b'



# Generated at 2022-06-14 02:11:25.218178
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    s = SixMovesTransformer({})
    assert s.target == (2, 7)
    assert len(s.rewrites) == len(set(s.rewrites))
    assert s.dependencies == ['six']

    assert ('six.moves.urllib.parse.urlparse', 'six.moves.urllib_parse.urlparse') in s.rewrites

    assert ('tkinter.tix', 'six.moves.tkinter_tix') in s.rewrites
    assert ('tkinter.tix', 'six.moves.tkinter_tix') in s.rewrites
    assert ('tkinter.tix', 'six.moves.tkinter_tix') in s.rewrites

# Generated at 2022-06-14 02:11:37.046185
# Unit test for constructor of class SixMovesTransformer

# Generated at 2022-06-14 02:11:56.892041
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert MovedAttribute('a', 'b', 'c').name == 'a'
    assert MovedAttribute('a', 'b', 'c').new_mod == 'c'
    assert MovedAttribute('a', 'b', 'c').new_attr == 'a'
    assert MovedAttribute('a', 'b', 'c', 'd', 'e').name == 'a'
    assert MovedAttribute('a', 'b', 'c', 'd', 'e').new_mod == 'c'
    assert MovedAttribute('a', 'b', 'c', 'd', 'e').new_attr == 'e'
    assert MovedAttribute('a', 'b', 'c', 'd').name == 'a'
    assert MovedAttribute('a', 'b', 'c', 'd').new_mod == 'c'
    assert MovedAttribute

# Generated at 2022-06-14 02:12:03.818298
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    test_moves_name = 'test_moves'
    test_moves_new_mod = 'test_new_mod'
    test_case = MovedAttribute(test_moves_name, 'old_mod', test_moves_new_mod)
    assert test_case.name == test_moves_name and test_case.new_mod == test_moves_new_mod and \
        test_case.new_attr == test_moves_name

# Generated at 2022-06-14 02:12:05.979517
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    test_moved_attribute = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert test_moved_attribute.name == 'cStringIO'
    assert test_moved_attribute.new_mod == 'io'
    assert test_moved_attribute.new_attr == 'StringIO'



# Generated at 2022-06-14 02:12:12.566894
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    with pytest.raises(TypeError):
        MovedAttribute()
    with pytest.raises(TypeError):
        MovedAttribute('name')
    with pytest.raises(TypeError):
        MovedAttribute('name','old_mod')
    with pytest.raises(TypeError):
        MovedAttribute('name','old_mod','new_mod','old_attr','new_attr','dummy_value')

# Generated at 2022-06-14 02:12:16.564179
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    move = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert move.name == "cStringIO"
    assert move.new_mod == "io"
    assert move.new_attr == "StringIO"

# Generated at 2022-06-14 02:12:22.507891
# Unit test for constructor of class MovedModule
def test_MovedModule():
    mm = MovedModule("a","b","c")
    assert mm.name == "a"
    assert mm.old == "b"
    assert mm.new == "c"
    mm = MovedModule("a","b")
    assert mm.name == "a"
    assert mm.old == "b"
    assert mm.new == "a"


# Generated at 2022-06-14 02:12:27.698411
# Unit test for constructor of class MovedModule
def test_MovedModule():
    move = MovedModule("wat", "here", "there")
    assert move.name == "wat"
    assert move.old == "here"
    assert move.new == "there"


# Generated at 2022-06-14 02:12:29.353600
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    t = SixMovesTransformer()
    assert t.rewrites


# Generated at 2022-06-14 02:12:34.075492
# Unit test for constructor of class MovedModule
def test_MovedModule():
    with pytest.raises(TypeError) as excinfo:
        MovedModule(name='module', old_module='old_module')
    assert 'too many positional arguments' in str(excinfo.value)

# Generated at 2022-06-14 02:12:38.899062
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    transformer = SixMovesTransformer()
    assert SixMovesTransformer.target == (2, 7)
    assert 'six' in SixMovesTransformer.dependencies
    assert len(SixMovesTransformer.rewrites) == 61

# Unit testing

# Generated at 2022-06-14 02:13:13.505052
# Unit test for constructor of class SixMovesTransformer

# Generated at 2022-06-14 02:13:14.698632
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    FiveMovesTransformer(None)

# Generated at 2022-06-14 02:13:27.569446
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    from .base import BaseImportRewrite
    import six

    assert SixMovesTransformer is not None
    assert BaseImportRewrite.__name__ in SixMovesTransformer.__bases__
    assert SixMovesTransformer.target == (2, 7)
    assert SixMovesTransformer.rewrites is not None
    assert SixMovesTransformer.dependencies == ['six']

    # make sure that the rewrites contains the correct items:
    assert (six.moves.urllib.parse.urlsplit,  # noqa: F821
            'six.moves.urllib.parse.urlsplit') in SixMovesTransformer.rewrites

# Generated at 2022-06-14 02:13:31.658261
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    m = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert m.name == "cStringIO"
    assert m.new_mod == "io"
    assert m.new_attr == "StringIO"

    m = MovedAttribute("cStringIO", "cStringIO", "io")
    assert m.new_attr == "cStringIO"

# Generated at 2022-06-14 02:13:33.697816
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert len(SixMovesTransformer.rewrites) == 217
    assert len(SixMovesTransformer.dependencies) == 1
    assert len(SixMovesTransformer.rewrites) == 217

# Generated at 2022-06-14 02:13:38.023451
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    CA = MovedAttribute("abc", "old", "new", "oldattr", "newattr")
    assert CA.name == "abc"
    assert CA.new_mod == "new"
    assert CA.new_attr == "newattr"


# Generated at 2022-06-14 02:13:39.614644
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert SixMovesTransformer.rewrites == _get_rewrites()

# Generated at 2022-06-14 02:13:43.342438
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert SixMovesTransformer(2, 7)


transformer = SixMovesTransformer.from_version(2, (2, 7))

# Generated at 2022-06-14 02:13:49.582405
# Unit test for constructor of class MovedModule
def test_MovedModule():
    mm1 = MovedModule("builtins", "__builtin__")
    assert mm1.name == "builtins"
    assert mm1.old == "__builtin__"
    assert mm1.new == "builtins"

    mm2 = MovedModule("winreg", "_winreg")
    assert mm2.name == "winreg"
    assert mm2.old == "_winreg"
    assert mm2.new == "winreg"



# Generated at 2022-06-14 02:13:54.095300
# Unit test for constructor of class MovedModule
def test_MovedModule():
    a = MovedModule('foo', 'foo')
    assert a.name == 'foo'
    assert a.new == 'foo'

    b = MovedModule('foo', 'foo', 'bar')
    assert b.name == 'foo'
    assert b.new == 'bar'

# Generated at 2022-06-14 02:14:49.602773
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    """Test that the constructor of class SixMovesTransformer works"""
    SixMovesTransformer.rewrites

# Generated at 2022-06-14 02:14:52.272488
# Unit test for constructor of class MovedModule
def test_MovedModule():
    assert MovedModule("tkinter", "Tkinter").new == "tkinter"
    assert MovedModule("tkinter", "Tkinter").name == "tkinter"


# Generated at 2022-06-14 02:14:58.238118
# Unit test for constructor of class MovedModule
def test_MovedModule():
    moved_module_tuple = ('name', 'old location', 'new location')
    moved_module = MovedModule(*moved_module_tuple)
    assert moved_module_tuple == (moved_module.name,
                                  moved_module.old,
                                  moved_module.new)

# Generated at 2022-06-14 02:15:09.648255
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert MovedAttribute("cStringIO", "cStringIO", "io", "StringIO").name == "cStringIO"
    assert MovedAttribute("cStringIO", "cStringIO", "io", "StringIO").new_mod == "io"
    assert MovedAttribute("cStringIO", "cStringIO", "io", "StringIO").new_attr == "StringIO"
    assert MovedAttribute("cStringIO", "cStringIO", "io").name == "cStringIO"
    assert MovedAttribute("cStringIO", "cStringIO", "io").new_mod == "io"
    assert MovedAttribute("cStringIO", "cStringIO", "io").new_attr == "cStringIO"
    assert MovedAttribute("cStringIO", "cStringIO", "io", "StringIO", "cStringIO").new

# Generated at 2022-06-14 02:15:22.082918
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    # This test requires `six` to be installed:
    try:
        import six
    except ImportError:
        return
    assert len(SixMovesTransformer.rewrites) == len(_moved_attributes) + len(_urllib_parse_moved_attributes) + len(_urllib_error_moved_attributes) + len(_urllib_request_moved_attributes) + len(_urllib_response_moved_attributes) + len(_urllib_robotparser_moved_attributes)
    assert SixMovesTransformer.rewrites[:3] == [
        ('cStringIO.StringIO', 'six.moves.cStringIO'),
        ('filter', 'six.moves.filter'),
        ('filterfalse', 'six.moves.filterfalse')
    ]
   

# Generated at 2022-06-14 02:15:31.318007
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    moved_attribute = MovedAttribute("module", "newmodule", None)

    assert moved_attribute.name == "module"
    assert moved_attribute.new_mod == "newmodule"
    assert moved_attribute.new_attr == "module"

    moved_attribute = MovedAttribute("module", "newmodule", "newmodule", "oldattribute")

    assert moved_attribute.name == "module"
    assert moved_attribute.new_mod == "newmodule"
    assert moved_attribute.new_attr == "oldattribute"

    moved_attribute = MovedAttribute("module", "newmodule", "newmodule", "oldattribute", "newattribute")

    assert moved_attribute.name == "module"
    assert moved_attribute.new_mod == "newmodule"
    assert moved_attribute.new_attr == "newattribute"


# Unit test

# Generated at 2022-06-14 02:15:35.640660
# Unit test for constructor of class MovedModule
def test_MovedModule():
    move = MovedModule('name', 'old', 'new')
    assert move.name == 'name'
    assert move.new == 'new'
    move = MovedModule('name', 'old')
    assert move.new == 'name'


# Generated at 2022-06-14 02:15:46.651028
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    code = """
import csv
import cStringIO
import ConfigParser
import copy_reg
import gdbm
import commands
import Cookie
import HTMLParser
import httplib
import imp
import importlib
import collections
import itertools
import robotparser
import shlex
import xmlrpclib
import urllib2
import urllib

from __future__ import absolute_import
import six
"""

# Generated at 2022-06-14 02:15:54.676488
# Unit test for constructor of class MovedModule
def test_MovedModule():
    try:
        import MovedModule
    except:
        import types
        MovedModule = types.ModuleType('MovedModule')
        sys.modules['MovedModule'] = MovedModule
    from py2to3.fixes.six.moves import MovedModule
    assert MovedModule.__module__ == 'py2to3.fixes.six.moves'
    assert MovedModule.name == 'MovedModule'
    assert MovedModule.new == 'MovedModule'


# Generated at 2022-06-14 02:15:56.137429
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")