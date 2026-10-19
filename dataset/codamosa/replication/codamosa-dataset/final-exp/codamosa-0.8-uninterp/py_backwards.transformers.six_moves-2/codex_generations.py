

# Generated at 2022-06-14 02:06:09.550410
# Unit test for constructor of class SixMovesTransformer

# Generated at 2022-06-14 02:06:12.336095
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    t = SixMovesTransformer()
    assert t.target == (2, 7)
    assert len(t.rewrites) == len(_get_rewrites()) == 147

# Generated at 2022-06-14 02:06:23.320839
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    move = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    expected = 'MovedAttribute(name=\'cStringIO\',' \
               ' old_mod=\'cStringIO\',' \
               ' new_mod=\'io\',' \
               ' old_attr=\'StringIO\',' \
               ' new_attr=\'cStringIO\')'
    assert expected == repr(move)
    move = MovedAttribute("cStringIO", "cStringIO", "io")
    expected = 'MovedAttribute(name=\'cStringIO\',' \
               ' old_mod=\'cStringIO\',' \
               ' new_mod=\'io\',' \
               ' old_attr=None,' \
               ' new_attr=\'cStringIO\')'

# Generated at 2022-06-14 02:06:26.948505
# Unit test for constructor of class MovedModule
def test_MovedModule():
    moved_module = MovedModule("builtins", "__builtin__")
    assert moved_module.name == "builtins"
    assert moved_module.new == "builtins"
    assert moved_module.old == "__builtin__"



# Generated at 2022-06-14 02:06:30.361052
# Unit test for constructor of class MovedModule
def test_MovedModule():
    assert MovedModule('name', 'old') == MovedModule('name', 'old')



# Generated at 2022-06-14 02:06:31.710285
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    x = SixMovesTransformer()
    assert isinstance(x, BaseImportRewrite)

# Generated at 2022-06-14 02:06:37.119672
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert len(SixMovesTransformer.rewrites) == len(_urllib_robotparser_moved_attributes) + \
        len(_urllib_parse_moved_attributes) + \
        len(_urllib_error_moved_attributes) + \
        len(_urllib_request_moved_attributes) + \
        len(_urllib_response_moved_attributes) + \
        len(_moved_attributes)

# Generated at 2022-06-14 02:06:39.980829
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    xformer = SixMovesTransformer()
    assert str(xformer).endswith('SixMovesTransformer')

# Generated at 2022-06-14 02:06:49.913529
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    att = MovedAttribute("name", "old_mod", "new_mod", "old_attr", "new_attr")
    assert att.name == "name"
    assert att.new_mod == "new_mod"
    assert att.new_attr == "new_attr"

    att = MovedAttribute("name", "old_mod", None, "old_attr", None)
    assert att.name == "name"
    assert att.new_mod == "name"
    assert att.new_attr == "name"

    att = MovedAttribute("name", "old_mod", "new_mod")
    assert att.name == "name"
    assert att.new_mod == "new_mod"
    assert att.new_attr == "name"

    att = MovedAttribute("name", "old_mod", None)


# Generated at 2022-06-14 02:06:51.000865
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    SixMovesTransformer()

# Generated at 2022-06-14 02:06:59.331699
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    m = MovedAttribute('a', 'b', 'c')
    assert (m.name, m.new_mod, m.new_attr) == ('a', 'c', 'a')
    m = MovedAttribute('a', 'b', None, 'old', 'new')
    assert (m.name, m.new_mod, m.new_attr) == ('a', 'a', 'new')
    assert (m.old_attr, m.old_mod) == ('old', 'b')

# Generated at 2022-06-14 02:07:03.199457
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    m1 = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert m1.name == "cStringIO"
    assert m1.new_mod == "cStringIO"
    assert m1.new_attr == "StringIO"

# Generated at 2022-06-14 02:07:11.702976
# Unit test for constructor of class MovedModule
def test_MovedModule():
    a = MovedModule("http_cookiejar", "cookielib", "http.cookiejar")
    assert a.name == "http_cookiejar"
    assert a.new == "http.cookiejar"
    b = MovedModule("email_mime_base", "email.MIMEBase", "email.mime.base")
    assert b.name == "email_mime_base"
    assert b.new == "email.mime.base"
    # Should be false
    c = MovedModule("email_mime_base", "email.MIMEBase", "email.mime.base")
    assert not c.name == "email_mime_base"
    assert not c.new == "cookielib"
    d = MovedModule("http_cookiejar", "cookielib", "http.cookiejar")


# Generated at 2022-06-14 02:07:20.088639
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    attr = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert attr.name == "cStringIO"
    assert attr.new_mod == "cStringIO"
    assert attr.new_attr == "StringIO"
    attr = MovedAttribute("cStringIO", "cStringIO", "io")
    assert attr.new_attr == "cStringIO"

# Generated at 2022-06-14 02:07:23.733493
# Unit test for constructor of class MovedModule
def test_MovedModule():
    for prefix, moves in prefixed_moves:
        for move in moves:
            if isinstance(move, MovedAttribute):
                path = '{}.{}'.format(move.new_mod, move.new_attr)
                assert path != '{}.{}'.format(move.new_mod, move.name)

            elif isinstance(move, MovedModule):
                assert move.new != move.name

# Generated at 2022-06-14 02:07:26.348799
# Unit test for constructor of class MovedModule
def test_MovedModule():
    assert MovedModule('builtins', '__builtin__') == MovedModule('builtins', '__builtin__')


# Generated at 2022-06-14 02:07:29.883083
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert MovedAttribute("cStringIO", "cStringIO", "io", "StringIO").__dict__ == \
        {"name": "cStringIO", "new_mod": "io", "new_attr": "StringIO"}

# Generated at 2022-06-14 02:07:39.172301
# Unit test for constructor of class MovedModule
def test_MovedModule():
    m1 = MovedModule('a', 'b', 'c')
    assert (m1.name, m1.old, m1.new) == ('a', 'b', 'c')

    m2 = MovedModule('a', 'b')
    assert (m2.name, m2.old, m2.new) == ('a', 'b', 'a')

    m3 = MovedModule('a')
    assert (m3.name, m3.old, m3.new) == ('a', 'a', 'a')



# Generated at 2022-06-14 02:07:42.196481
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert SixMovesTransformer.rewrites != _get_rewrites()  # In the SixMovesTransformer module the eagerness is off.

# Generated at 2022-06-14 02:07:55.470540
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    """Unit test for constructor of class SixMovesTransformer"""
    rewrites = set(SixMovesTransformer.rewrites)

# Generated at 2022-06-14 02:08:02.023783
# Unit test for constructor of class MovedModule
def test_MovedModule():
    moved_module = MovedModule('name', 'old', 'new')
    assert moved_module.name == 'name'
    assert moved_module.old == 'old'
    assert moved_module.new == 'new'


# Generated at 2022-06-14 02:08:06.517417
# Unit test for constructor of class MovedModule
def test_MovedModule():
    moved_module = MovedModule("example", "example.old", "example.new")
    assert moved_module.name == "example"
    assert moved_module.new == "example.new"
    assert moved_module.old == "example.old"

# Generated at 2022-06-14 02:08:07.445804
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert SixMovesTransformer.rewrites

# Generated at 2022-06-14 02:08:10.439768
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    for rewrite in SixMovesTransformer.rewrites: 
        assert len(rewrite) == 2
        assert isinstance(rewrite, tuple)
        assert isinstance(rewrite[0], str)
        assert isinstance(rewrite[1], str)
        assert re.search("six\\.moves", rewrite[1])

# Generated at 2022-06-14 02:08:13.371833
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    attr = MovedAttribute("filter", "itertools", "builtins")
    assert attr.name == 'filter'
    assert attr.new_mod == 'builtins'
    assert attr.new_attr == 'filter'



# Generated at 2022-06-14 02:08:18.404330
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    obj = MovedAttribute('X', 'Y', 'Z')
    assert obj.name == 'X'
    assert obj.new_attr == 'X'
    assert obj.new_mod == 'Z'

# Generated at 2022-06-14 02:08:30.571346
# Unit test for constructor of class MovedModule
def test_MovedModule():
    assert MovedModule("name", "old") == MovedModule("name", "old")
    assert MovedModule("name", "old", "new") == MovedModule("name", "old", "new")
    assert MovedModule("name", "old") != MovedModule("name_other", "old")
    assert MovedModule("name", "old") != MovedModule("name", "old_other")
    assert MovedModule("name", "old", "new") != MovedModule("name", "old")
    assert MovedModule("name", "old", "new") != MovedModule("name_other", "old", "new")
    assert MovedModule("name", "old", "new") != MovedModule("name", "old_other", "new")
    assert MovedModule("name", "old", "new_other")

# Generated at 2022-06-14 02:08:37.534363
# Unit test for constructor of class MovedModule
def test_MovedModule():
    assert MovedModule(name="hello", old="old", new="new").name == "hello"
    assert MovedModule(name="hello", old="old", new="new").old == "old"
    assert MovedModule(name="hello", old="old", new="new").new == "new"
    assert MovedModule(name="hello", old="old").old == "old"
    assert MovedModule(name="hello", old="old").new == "hello"

# Generated at 2022-06-14 02:08:45.988060
# Unit test for constructor of class SixMovesTransformer

# Generated at 2022-06-14 02:08:59.810030
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    a = MovedAttribute("name", "old_mod", "new_mod", "old_attr", "new_attr")
    assert a.name == "name"
    assert a.new_mod == "new_mod"
    assert a.new_attr == "new_attr"
    a = MovedAttribute("name", "old_mod", "new_mod", "old_attr")
    assert a.name == "name"
    assert a.new_mod == "new_mod"
    assert a.new_attr == "old_attr"
    a = MovedAttribute("name", "old_mod", "new_mod")
    assert a.name == "name"
    assert a.new_mod == "new_mod"
    assert a.new_attr == "name"

# Generated at 2022-06-14 02:09:03.737925
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    t = SixMovesTransformer()
    assert list(t.rewrites) == _get_rewrites()

# Generated at 2022-06-14 02:09:05.691371
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert list(SixMovesTransformer.rewrites)

# Generated at 2022-06-14 02:09:18.803304
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    
    moved_attr = MovedAttribute("moved_attr", "old_mod", "new_mod", "old_attr", "new_attr")
    assert moved_attr.name == "moved_attr"
    assert moved_attr.new_mod == "new_mod"
    assert moved_attr.new_attr == "new_attr"
    
    moved_attr = MovedAttribute("moved_attr", "old_mod", "new_mod", "old_attr")
    assert moved_attr.name == "moved_attr"
    assert moved_attr.new_mod == "new_mod"
    assert moved_attr.new_attr == "old_attr"
    
    moved_attr = MovedAttribute("moved_attr", "old_mod", "new_mod")

# Generated at 2022-06-14 02:09:26.211801
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    """
    This method is a unit test for constructor of class SixMovesTransformer
    """
    target = (2, 7)
    rewrites = _get_rewrites()
    dependencies = ['six']
    test = SixMovesTransformer()
    assert test.target == target
    assert test.rewrites == rewrites
    assert test.dependencies == dependencies

# Generated at 2022-06-14 02:09:29.802050
# Unit test for constructor of class MovedModule
def test_MovedModule():
    m = MovedModule("name", "old")
    assert m.name == "name"
    assert m.old == "old"
    assert m.new == "name"


# Generated at 2022-06-14 02:09:34.178832
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    move = MovedAttribute('foo', 'old', 'new', 'old_attr')
    assert move.name == 'foo'
    assert move.new_mod == 'new'
    assert move.new_attr == 'old_attr'


# Generated at 2022-06-14 02:09:35.666937
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert SixMovesTransformer() is not None

# Generated at 2022-06-14 02:09:39.189685
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert 'six.moves' in SixMovesTransformer.dependencies

    # Check __init__()
    assert len(SixMovesTransformer.rewrites) == len(_get_rewrites())



# Generated at 2022-06-14 02:09:42.831070
# Unit test for constructor of class MovedModule
def test_MovedModule():
    move = MovedModule("name", "old", "new")
    assert move.name == "name"
    assert move.old == "old"
    assert move.new == "new"



# Generated at 2022-06-14 02:09:47.437675
# Unit test for constructor of class MovedModule
def test_MovedModule():
    mod = MovedModule("execfile", "execfile", "six.moves.execfile")
    assert mod.name == "execfile"
    assert mod.new == "six.moves.execfile"


# Generated at 2022-06-14 02:09:56.557945
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    attr = MovedAttribute("foo", "bar", "baz", "sniggle", "snaggle")
    assert attr.name == attr.new_attr == "snaggle"
    assert attr.new_mod == "baz"
    attr = MovedAttribute("foo", "bar", "baz", "sniggle")
    assert attr.name == attr.new_attr == "sniggle"
    assert attr.new_mod == "baz"
    attr = MovedAttribute("foo", "bar", "baz")
    assert attr.name == attr.new_mod == attr.new_attr == "foo"
    attr = MovedAttribute("foo", "bar", None, "sniggle", "snaggle")

# Generated at 2022-06-14 02:10:09.494768
# Unit test for constructor of class MovedModule
def test_MovedModule():
    mv = MovedModule("builtins", "__builtin__")
    assert mv.name == "builtins"
    assert mv.old == "__builtin__"
    assert mv.new == "builtins"

    mv = MovedModule("builtins", "__builtin__", "builtins")
    assert mv.name == "builtins"
    assert mv.old == "__builtin__"
    assert mv.new == "builtins"

    mv = MovedModule("builtins", "__builtin__", "__builtin__")
    assert mv.name == "builtins"
    assert mv.old == "__builtin__"
    assert mv.new == "builtins"

    mv = MovedModule("builtins", "__builtin__", None)
   

# Generated at 2022-06-14 02:10:14.501130
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    move = MovedAttribute('name', 'old_mod', 'new_mod', 'old_attr', 'new_attr')
    assert move.name == 'name'
    assert move.new_mod == 'new_mod'
    assert move.new_attr == 'new_attr'

# Generated at 2022-06-14 02:10:16.114163
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    from .. import futures
    assert futures.SixMovesTransformer.rewrites is not None

# Generated at 2022-06-14 02:10:23.511460
# Unit test for constructor of class MovedModule
def test_MovedModule():
    # Tests
    assert MovedModule('name', 'old', 'new').name == 'name'
    assert MovedModule('name', 'old', 'new').new == 'new'
    assert MovedModule('name', 'old').name == 'name'
    assert MovedModule('name', 'old').new == 'name'
    assert MovedModule('name').name == 'name'
    assert MovedModule('name').new == 'name'


# Generated at 2022-06-14 02:10:25.400403
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    print(SixMovesTransformer.rewrite_paths)

# Generated at 2022-06-14 02:10:31.525552
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    item = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert item.name == "cStringIO"
    assert item.new_mod == "io"
    assert item.new_attr == "cStringIO"
    item = MovedAttribute("test", "old", "new")
    assert item.name == "test"
    assert item.new_mod == "new"
    assert item.new_attr == "test"

# Generated at 2022-06-14 02:10:43.879601
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    move = MovedAttribute("foo", "mod1", "mod2")
    assert move.name == "foo"
    assert move.new_attr == "foo"
    assert move.new_mod == "mod2"

    move = MovedAttribute("foo", "mod1", "mod2", "foo", "bar")
    assert move.name == "foo"
    assert move.new_attr == "bar"
    assert move.new_mod == "mod2"

    move = MovedAttribute("foo", "mod1", "mod2", None, "bar")
    assert move.name == "foo"
    assert move.new_attr == "bar"
    assert move.new_mod == "mod2"

    move = MovedAttribute("foo", "mod1", "mod2", "bar")

# Generated at 2022-06-14 02:10:51.165406
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert MovedAttribute("cStringIO", "cStringIO", "io", "StringIO").name == "cStringIO"
    assert MovedAttribute("cStringIO", "cStringIO", "io", "StringIO").new_mod == "io"
    assert MovedAttribute("cStringIO", "cStringIO", "io", "StringIO").new_attr == "StringIO"



# Generated at 2022-06-14 02:10:54.772990
# Unit test for constructor of class MovedModule
def test_MovedModule():
    movedmodule = MovedModule("builtins", "__builtin__")
    assert movedmodule.name == "builtins"
    assert movedmodule.new == "builtins"

# Generated at 2022-06-14 02:11:09.250821
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert MovedAttribute("cStringIO", "cStringIO", "io", "StringIO").name == "cStringIO"
    assert MovedAttribute("cStringIO", "cStringIO", "io", "StringIO").new_mod == "io"
    assert MovedAttribute("cStringIO", "cStringIO", "io", "StringIO").new_attr == "StringIO"
    assert MovedAttribute("filter", "itertools", "builtins", "ifilter", "filter").name == "filter"
    assert MovedAttribute("filter", "itertools", "builtins", "ifilter", "filter").new_attr == "filter"
    assert MovedAttribute("getcwd", "os", "os", "getcwdu", "getcwd").name == "getcwd"

# Generated at 2022-06-14 02:11:11.469941
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert len([x for (x, y) in _get_rewrites()]) == 67 + 5 + 20 + 26 + 10

# Generated at 2022-06-14 02:11:21.872526
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    moved_attribute = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    moved_attribute = MovedAttribute("cStringIO", "cStringIO", "io")
    with pytest.raises(TypeError):
        moved_attribute = MovedAttribute(1, "cStringIO", "io")
    with pytest.raises(TypeError):
        moved_attribute = MovedAttribute("cStringIO", 1, "io")
    with pytest.raises(TypeError):
        moved_attribute = MovedAttribute("cStringIO", "cStringIO", 1)
    with pytest.raises(TypeError):
        moved_attribute = MovedAttribute("cStringIO", "cStringIO", "io", 1)



# Generated at 2022-06-14 02:11:35.095103
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    m = MovedAttribute("name1","old_mod1","new_mod1","old_attr1","new_attr1")
    assert m.name == "name1"
    assert m.new_mod == "new_mod1"
    assert m.new_attr == "new_attr1"

    m = MovedAttribute("name2","old_mod2","new_mod2","old_attr2")
    assert m.name == "name2"
    assert m.new_mod == "new_mod2"
    assert m.new_attr == "old_attr2"

    m = MovedAttribute("name3","old_mod3","new_mod3")
    assert m.name == "name3"
    assert m.new_mod == "new_mod3"
    assert m.new_attr == "name3"


# Generated at 2022-06-14 02:11:45.269289
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    moved_attrib = MovedAttribute('name', 'old_mod', 'new_mod')
    moved_mod = MovedModule('name', 'old', 'new')
    test = SixMovesTransformer()
    assert test.rewrites
    assert test.rewrites[0] == ('builtins.filter', 'six.moves.filter')
    assert test.rewrites[1] == ('builtins.cStringIO', 'six.moves.cStringIO')
    assert test.rewrites[2] == ('builtins.input', 'six.moves.input')
    assert test.rewrites[3] == ('sys.intern', 'six.moves.intern')
    assert test.rewrites[4] == ('builtins.map', 'six.moves.map')

# Generated at 2022-06-14 02:11:48.846113
# Unit test for constructor of class MovedModule
def test_MovedModule():
    import pytest
    module = MovedModule('name', 'old', 'new')
    assert module.name == 'name'
    assert module.new == 'new'
    # Ensure that MovedModule instance has expected attributes.
    # https://docs.pytest.org/en/latest/reference.html#_pytest.python.Class
    assert 'name' in dir(module)
    assert 'new' in dir(module)

# Generated at 2022-06-14 02:11:49.993369
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    transformer = SixMovesTransformer()
    assert transformer


# Generated at 2022-06-14 02:11:56.449580
# Unit test for constructor of class MovedModule
def test_MovedModule():
    test_obj1 = MovedModule('module_1', 'old_module_1', 'new_module_1')
    test_obj2 = MovedModule('module_2', 'old_module_2')
    assert (test_obj1.name == 'module_1')
    assert (test_obj1.old == 'old_module_1')
    assert (test_obj1.new == 'new_module_1')
    assert (test_obj2.new == 'module_2')


# Generated at 2022-06-14 02:11:58.479027
# Unit test for constructor of class MovedModule
def test_MovedModule():
    # see six/moves.py
    assert str(MovedModule("builtins", "__builtin__")) == "MovedModule(name='builtins', old='__builtin__', new='builtins')"


# Generated at 2022-06-14 02:12:06.792378
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    """test_SixMovesTransformer.py

    This test verifies that the SixMovesTransformer generates the expected
    mappings. Make sure that your changes are compatible with the list of
    items in the `moves` list.
    """
    path_map = dict(SixMovesTransformer.rewrites)
    assert path_map['shlex.quote'] == 'six.moves.shlex_quote'
    assert path_map['io.StringIO'] == 'six.moves.cStringIO.StringIO'

# Generated at 2022-06-14 02:12:20.033628
# Unit test for constructor of class MovedModule
def test_MovedModule():
    assert _moved_attributes[-6] == MovedModule("builtins", "__builtin__")

# Generated at 2022-06-14 02:12:27.154785
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    mv = MovedAttribute("a", "b", "c")
    assert mv.name == "a"
    assert mv.new_mod == "c"
    assert mv.new_attr == "a"
    mv = MovedAttribute("a", "b", "c", "d", "e")
    assert mv.new_attr == "e"
    mv = MovedAttribute("a", "b", "c", "d")
    assert mv.new_attr == "d"
    mv = MovedAttribute("a", "b", "c", new_attr="e")
    assert mv.new_attr == "e"

# Generated at 2022-06-14 02:12:40.082189
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    attribute1 = MovedAttribute('cStringIO', 'cStringIO', 'io', 'StringIO')
    attribute2 = MovedAttribute('cStringIO', 'cStringIO', 'io', new_attr='StringIO')
    attribute3 = MovedAttribute('cStringIO', 'cStringIO', 'io', old_attr='StringIO')
    attribute4 = MovedAttribute('cStringIO', 'cStringIO', 'io')
    assert attribute1.name == attribute2.name == attribute3.name == attribute4.name == 'cStringIO'
    assert attribute1.new_mod == attribute2.new_mod == attribute3.new_mod == attribute4.new_mod == 'io'
    assert attribute1.old_attr == attribute2.old_attr == attribute3.old_attr == attribute4.old_attr == 'StringIO'


# Generated at 2022-06-14 02:12:51.352296
# Unit test for constructor of class SixMovesTransformer

# Generated at 2022-06-14 02:12:58.626260
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


# Generated at 2022-06-14 02:13:07.363632
# Unit test for constructor of class MovedModule
def test_MovedModule():
    # passing name, old
    m = MovedModule('name', 'old')
    assert m.name == 'name'
    assert m.old == 'old'
    assert m.new == 'name'

    # passing name, old, new
    m = MovedModule('name', 'old', 'new')
    assert m.name == 'name'
    assert m.old == 'old'
    assert m.new == 'new'



# Generated at 2022-06-14 02:13:11.409859
# Unit test for constructor of class MovedModule
def test_MovedModule():
    assert MovedModule("name", "old", "new") == \
        MovedModule("name", "old", "new")
    assert MovedModule("name", "old") == MovedModule("name", "old", "name")

# Generated at 2022-06-14 02:13:14.287029
# Unit test for constructor of class MovedModule
def test_MovedModule():
    module = MovedModule("foo", "bar")
    assert module.name == "foo"
    assert module.old == "bar"
    assert module.new == "foo"

# Generated at 2022-06-14 02:13:27.203491
# Unit test for constructor of class SixMovesTransformer

# Generated at 2022-06-14 02:13:33.475184
# Unit test for constructor of class MovedModule
def test_MovedModule():
    res = MovedModule("foo", "bar", "baz")
    assert res.name == "foo"
    assert res.old == "bar"
    assert res.new == "baz"

    res = MovedModule("foo")
    assert res.name == "foo"
    assert res.old == "foo"
    assert res.new == "foo"

    res = MovedModule("foo", "bar")
    assert res.name == "foo"
    assert res.old == "bar"
    assert res.new == "foo"

# Generated at 2022-06-14 02:14:04.294855
# Unit test for constructor of class MovedModule
def test_MovedModule():
    mm = MovedModule("name", "old", "new")
    assert mm.name == "name"
    assert mm.old == "old"
    assert mm.new == "new"
    mm = MovedModule("name", "old")
    assert mm.name == "name"
    assert mm.old == "old"
    assert mm.new == "name"

# Generated at 2022-06-14 02:14:06.895639
# Unit test for constructor of class MovedModule
def test_MovedModule():
    mm = MovedModule("name", "old", "new")
    assert mm.name == "name"
    assert mm.new == "new"
    mm2 = MovedModule("newname")
    assert mm2.name == "newname"
    assert mm2.new == "newname"

# unit test for constructor of class MovedAttribute

# Generated at 2022-06-14 02:14:09.291724
# Unit test for constructor of class MovedModule
def test_MovedModule():
    MovedModule("foo", "foo")
    MovedModule("foo", "foo", "bar")



# Generated at 2022-06-14 02:14:19.554306
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert MovedAttribute("cStringIO", "cStringIO", "io", "StringIO").name == "cStringIO"
    assert MovedAttribute("cStringIO", "cStringIO", "io", "StringIO").old_attr is None
    assert MovedAttribute("cStringIO", "cStringIO", "io", "StringIO").new_attr == "StringIO"
    assert MovedAttribute("cStringIO", "cStringIO", "io", "StringIO").old_mod == "cStringIO"
    assert MovedAttribute("cStringIO", "cStringIO", "io", "StringIO").new_mod == "io"
    assert MovedAttribute("cStringIO", "cStringIO", "io").name == "cStringIO"

# Generated at 2022-06-14 02:14:32.457913
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    a1 = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert a1.name == "cStringIO"
    assert a1.new_mod == "io"
    assert a1.new_attr == "StringIO"
    a2 = MovedAttribute("cStringIO", "cStringIO", "io")
    assert a2.name == "cStringIO"
    assert a2.new_mod == "io"
    assert a2.new_attr == "cStringIO"
    a3 = MovedAttribute("cStringIO", None, None)
    assert a3.name == "cStringIO"
    assert a3.new_mod == "cStringIO"
    assert a3.new_attr == "cStringIO"



# Generated at 2022-06-14 02:14:36.651810
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    with ExpectedException(TypeError, '__init__() takes at least 2 arguments (1 given)'):
        MovedAttribute('cStringIO')
    with ExpectedException(TypeError, '__init__() takes at most 5 arguments (6 given)'):
        MovedAttribute('cStringIO', 'cStringIO', 'io', 'StringIO', 'new_attr', "unexpected_arg")

# Generated at 2022-06-14 02:14:41.128825
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    move = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert move.name == 'cStringIO'
    assert move.new_mod == 'io'
    assert move.new_attr == 'StringIO'

# Generated at 2022-06-14 02:14:47.677572
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    testcase = MovedAttribute("name", "old_mod", "new_mod", "old_attr", "new_attr")
    assert testcase.name == "name"
    assert testcase.new_mod == "new_mod"
    assert testcase.new_attr == "new_attr"


# Generated at 2022-06-14 02:14:55.123367
# Unit test for constructor of class MovedModule
def test_MovedModule():
    assert MovedModule('argparse','optparse').name == 'argparse'
    assert MovedModule('argparse','optparse').new == 'argparse'
    assert MovedModule('argparse','optparse','optparse').name == 'argparse'
    assert MovedModule('argparse','optparse','optparse').new == 'optparse'

# Generated at 2022-06-14 02:14:59.461941
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    c1 = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    if c1.name == "cStringIO":
        return True
    else:
        return False


# Generated at 2022-06-14 02:15:52.255528
# Unit test for constructor of class MovedModule
def test_MovedModule():
    MovedModule('dbm_gnu', 'gdbm', 'dbm.gnu')

# Generated at 2022-06-14 02:15:57.276924
# Unit test for constructor of class MovedModule
def test_MovedModule():
    old_module = "os.path"
    new_module = "pathlib"
    m = MovedModule(old_module, new_module)
    assert m.name == old_module
    assert m.new == new_module