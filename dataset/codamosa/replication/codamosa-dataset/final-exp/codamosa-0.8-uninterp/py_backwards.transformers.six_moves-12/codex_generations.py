

# Generated at 2022-06-14 02:06:12.005080
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    attr = MovedAttribute("name", "old_mod", "new_mod", "old_attr", "new_attr")
    assert(attr.name == "name")
    assert(attr.new_mod == "new_mod")
    assert(attr.new_attr == "new_attr")

    attr = MovedAttribute("name", "old_mod", "new_mod", "old_attr", None)
    assert(attr.name == "name")
    assert(attr.new_mod == "new_mod")
    assert(attr.new_attr == "old_attr")

    attr = MovedAttribute("name", "old_mod", "new_mod", None, "new_attr")
    assert(attr.name == "name")
    assert(attr.new_mod == "new_mod")

# Generated at 2022-06-14 02:06:16.030179
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    csa = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert csa.name == "cStringIO"
    assert csa.new_mod == "io"
    assert csa.new_attr == "StringIO"

# Generated at 2022-06-14 02:06:26.621053
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    moved_attribute = MovedAttribute('name', 'old_mod', 'new_mod', 'old_attr', 'new_attr')
    assert moved_attribute.name == 'name'
    assert moved_attribute.new_mod == 'new_mod'
    assert moved_attribute.new_attr == 'new_attr'
    assert MovedAttribute('name', 'old_mod', 'new_mod', 'old_attr').new_attr == 'old_attr'
    assert MovedAttribute('name', 'old_mod', 'new_mod').new_attr == 'name'
    assert MovedAttribute('name', 'old_mod', 'new_mod', 'old_attr', None).new_attr == 'old_attr'

# Generated at 2022-06-14 02:06:30.842559
# Unit test for constructor of class MovedModule
def test_MovedModule():
    assert MovedModule("builtins", "__builtin__").new == MovedModule("builtins", "__builtin__").name

# Generated at 2022-06-14 02:06:39.127152
# Unit test for constructor of class MovedModule
def test_MovedModule():
    test_moved_module = MovedModule("configparser", "ConfigParser")
    assert test_moved_module.name == "configparser"
    assert test_moved_module.old == "ConfigParser"
    assert test_moved_module.new == "configparser"
    test_moved_module = MovedModule("configparser", "ConfigParser", "configparser")
    assert test_moved_module.name == "configparser"
    assert test_moved_module.old == "ConfigParser"
    assert test_moved_module.new == "configparser"
    test_moved_module = MovedModule("configparser", "ConfigParser", "lala")
    assert test_moved_module.name == "configparser"
    assert test_moved_module.old == "ConfigParser"
    assert test

# Generated at 2022-06-14 02:06:40.864599
# Unit test for constructor of class MovedModule
def test_MovedModule():
    assert MovedModule("string", "oldString") is not None

# Generated at 2022-06-14 02:06:42.105721
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    x = SixMovesTransformer()
    assert x.rewrites == _get_rewrites()


# Generated at 2022-06-14 02:06:44.043997
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    with pytest.raises(TypeError):
        _ = MovedAttribute("cStringIO")

# Generated at 2022-06-14 02:06:45.857870
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert SixMovesTransformer().rewrites == _get_rewrites()

# Generated at 2022-06-14 02:06:47.950063
# Unit test for constructor of class MovedModule
def test_MovedModule():
    with pytest.raises(AssertionError):
        MovedModule(1, None)


# Generated at 2022-06-14 02:06:52.370048
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert MovedAttribute("name", "old_mod", "new_mod", "old_attr", "new_attr").name == "name"


# Generated at 2022-06-14 02:07:06.214825
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    from .base import get_imports
    from six import moves
    import six.moves.urllib.parse as urllib_parse
    SixMovesTransformer()
    assert urllib_parse.urlsplit('http://www.python.org') == (
        'http', 'www.python.org', '', '', '',
    )
    assert moves.urllib_parse.urlsplit('http://www.python.org') == (
        'http', 'www.python.org', '', '', '',
    )
    assert get_imports('import six.moves') == 'import six.moves'
    assert get_imports('import six.moves.urllib.error') == '''import six.moves
import six.moves.urllib.error'''
    assert get_

# Generated at 2022-06-14 02:07:20.399108
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    d = SixMovesTransformer._get_rewrites()
    d = dict(d)
    assert 'builtins.input' in d
    assert d['builtins.input'] == 'six.moves.input'

    d = dict(_urllib_request_moved_attributes)
    assert 'urllib.request.HTTPCookieProcessor' in d
    assert d['urllib.request.HTTPCookieProcessor'] \
        == 'six.moves.urllib.request.HTTPCookieProcessor'

    d = dict(_urllib_response_moved_attributes)
    assert 'urllib.response.addbase' in d
    assert d['urllib.response.addbase'] == 'six.moves.urllib.response.addbase'

# Generated at 2022-06-14 02:07:24.695019
# Unit test for constructor of class MovedModule
def test_MovedModule():
    movedModule = MovedModule("name", "old")
    assert movedModule.name == "name"
    assert movedModule.old == "old"
    assert movedModule.new == "name"


# Generated at 2022-06-14 02:07:37.777713
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    # Case 1: Provide all arguments
    ma = MovedAttribute("old_name", "old_mod", "new_mod", "old_attr", "new_attr")
    assert ma.name == "old_name"
    assert ma.old_mod == "old_mod"
    assert ma.new_mod == "new_mod"
    assert ma.old_attr == "old_attr"
    assert ma.new_attr == "new_attr"

    # Case 2: Provide no argument for old_attr and new_attr
    ma = MovedAttribute("old_name", "old_mod", "new_mod")
    assert ma.name == "old_name"
    assert ma.old_mod == "old_mod"
    assert ma.new_mod == "new_mod"

# Generated at 2022-06-14 02:07:43.703374
# Unit test for constructor of class MovedModule
def test_MovedModule():
    move1 = MovedModule('foo', 'bar')
    assert move1.name == 'foo'
    assert move1.old == 'bar'
    assert move1.new == 'foo'

    move2 = MovedModule('foo', 'bar', 'baz')
    assert move2.name == 'foo'
    assert move2.old == 'bar'
    assert move2.new == 'baz'

# Generated at 2022-06-14 02:07:45.987188
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    import_rewrite = SixMovesTransformer.load()
    assert import_rewrite


# Generated at 2022-06-14 02:07:49.450348
# Unit test for constructor of class MovedModule
def test_MovedModule():
    move = MovedModule('name', 'old', None)
    assert move.name == 'name'
    assert move.new == 'name'

    move = MovedModule('name', 'old', 'new')
    assert move.new == 'new'

# Generated at 2022-06-14 02:07:59.097233
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert MovedAttribute("cStringIO", "cStringIO", "io", "StringIO").name == "cStringIO"
    assert MovedAttribute("cStringIO", "cStringIO", "io", "StringIO").old_attr == "StringIO"
    assert MovedAttribute("cStringIO", "cStringIO", "io", "StringIO").new_mod == "io"
    assert MovedAttribute("cStringIO", "cStringIO", "io").new_attr == "cStringIO"
    assert MovedAttribute("cStringIO", "cStringIO", "io").new_attr == "cStringIO"
    assert MovedAttribute("cStringIO", "cStringIO", None).new_mod == "cStringIO"

# Generated at 2022-06-14 02:08:08.510182
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    with wrap_process_import_error():
        from .. import transforms
        from ..utils.helpers import eager

        _get_rewrites = eager(lazy=lambda: transforms.SixMovesTransformer.rewrites)
        rewrites = _get_rewrites()
        assert 'os.getcwd' in rewrites
        assert 'sched.scheduler' in rewrites
        assert 'builtins.zip' in rewrites
        assert 'builtins.filter' in rewrites
        assert 'builtins.reduce' in rewrites
        assert 'urllib.parse.parse_qs' in rewrites
        assert 'urllib.parse.quote_plus' in rewrites
        assert 'urllib.request.urlopen' in rewrites

# Generated at 2022-06-14 02:08:13.455731
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    print(SixMovesTransformer())

if __name__ == '__main__':
    test_SixMovesTransformer()

# Generated at 2022-06-14 02:08:27.577655
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert MovedAttribute("cStringIO", "cStringIO", "io", "StringIO").new_attr == "StringIO"
    assert MovedAttribute("cStringIO", "cStringIO", "io", new_attr='StringIO').new_attr == "StringIO"
    assert MovedAttribute("cStringIO", "cStringIO", "io", old_attr='StringIO').new_attr == "StringIO"
    assert MovedAttribute("cStringIO", "cStringIO", "io", old_attr='StringIO', new_attr='StringIO').new_attr == "StringIO"
    assert MovedAttribute("cStringIO", "cStringIO", "io", old_attr='something').new_attr == "cStringIO"

# Generated at 2022-06-14 02:08:38.117698
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    # test __init__
    x = MovedAttribute('cStringIO', 'cStringIO', 'io', 'StringIO')
    # test __eq__
    assert x == MovedAttribute('cStringIO', 'cStringIO', 'io', 'StringIO')
    # test __ne__
    assert x != MovedAttribute('cStringIO', 'cStringIO', 'io', 'StringIO2')
    assert x != MovedAttribute('cStringIO', 'cStringIO', 'io2', 'StringIO')
    assert x != MovedAttribute('cStringIO', 'cStringIO2', 'io', 'StringIO')
    assert x != MovedAttribute('cStringIO2', 'cStringIO', 'io', 'StringIO')

# Generated at 2022-06-14 02:08:39.394594
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert SixMovesTransformer.rewrites == _get_rewrites()

# Generated at 2022-06-14 02:08:46.089125
# Unit test for constructor of class MovedModule
def test_MovedModule():
    test_module = MovedModule("test", "test1")
    assert test_module.name == "test"
    assert test_module.new == "test"

    test_module2 = MovedModule("test2", "test3", "test4")
    assert test_module2.name == "test2"
    assert test_module2.new == "test4"


# Generated at 2022-06-14 02:08:49.273160
# Unit test for constructor of class MovedModule
def test_MovedModule():
    mm = MovedModule("foo","bar")
    assert mm.name=="foo"
    assert mm.new=="bar"

# Generated at 2022-06-14 02:09:02.217067
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    ma = MovedAttribute('name', 'old_mod', 'new_mod')
    assert ma.name == 'name'
    assert ma.new_mod == 'new_mod'
    assert ma.new_attr == 'name'
    ma2 = MovedAttribute('name', 'old_mod', 'new_mod', 'old_attr', 'new_attr')
    assert ma2.name == 'name'
    assert ma2.new_mod == 'new_mod'
    assert ma2.new_attr == 'new_attr'
    ma3 = MovedAttribute('name', 'old_mod', 'new_mod', 'old_attr', None)
    assert ma3.name == 'name'
    assert ma3.new_mod == 'new_mod'
    assert ma3.new_attr == 'old_attr'

#

# Generated at 2022-06-14 02:09:12.684559
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    from libcst._six import PY36
    import ast
    import os
    import shutil
    import sys
    from libcst.metadata.wrapper import ModuleWrapper
    from libcst.testing.utils import UnitTest, data_provider


# Generated at 2022-06-14 02:09:16.562242
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    s = MovedAttribute("name", "old_mod", "new_mod", "old_attr", "new_attr")
    assert s.name == "name"
    assert s.new_mod == "new_mod"
    assert s.new_attr == "new_attr"


# Generated at 2022-06-14 02:09:19.332502
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    move = MovedAttribute('test', 'test1', 'test2')
    assert move.name == 'test'
    assert move.new_mod == 'test2'
    assert move.new_attr == 'test'



# Generated at 2022-06-14 02:09:27.392612
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert MovedAttribute("test", "test", "test", "test", "test")
    assert MovedAttribute("test", "test", "test")
    assert MovedAttribute("test", "test", "test", "test")
    assert MovedAttribute("test", "test")
    assert MovedAttribute("test")


# Generated at 2022-06-14 02:09:38.583040
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    ma = MovedAttribute('cStringIO', 'cStringIO', 'io', 'StringIO')
    assert ma.name == 'cStringIO'
    assert ma.new_mod == 'io'
    assert ma.new_attr == 'StringIO'

    ma = MovedAttribute('cStringIO', 'cStringIO', 'io')
    assert ma.name == 'cStringIO'
    assert ma.new_mod == 'io'
    assert ma.new_attr == 'cStringIO'

    ma = MovedAttribute('cStringIO', 'cStringIO')
    assert ma.name == 'cStringIO'
    assert ma.new_mod == 'cStringIO'
    assert ma.new_attr == 'cStringIO'


# Generated at 2022-06-14 02:09:44.228775
# Unit test for constructor of class MovedModule
def test_MovedModule():

    move_module = MovedModule("myfrom","myto")
    assert move_module.name == 'myfrom'
    assert move_module.new == 'myto'

    move_module = MovedModule("myfrom")
    assert move_module.name == 'myfrom'
    assert move_module.new == 'myfrom' 


# Generated at 2022-06-14 02:09:57.428493
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    ma = MovedAttribute("test_ma", "test_MA_old_mod", "test_MA_new_mod", "test_MA_old_attr", "test_MA_new_attr")
    assert ma.name == "test_ma"
    assert ma.new_mod == "test_MA_new_mod"
    assert ma.new_attr == "test_MA_new_attr"
    ma = MovedAttribute("test_ma", "test_MA_old_mod", "test_MA_new_mod", "test_MA_old_attr")
    assert ma.name == "test_ma"
    assert ma.new_mod == "test_MA_new_mod"
    assert ma.new_attr ==  "test_MA_old_attr"

# Generated at 2022-06-14 02:10:01.804745
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    # The goal of this test is to check that the constructor of SixMovesTransformer works.
    # Note that SixMovesTransformer is a BaseImportRewrite subclass.
    moves = SixMovesTransformer()

# Generated at 2022-06-14 02:10:12.814918
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    # Test the constructor with 3 parameters
    move = MovedAttribute("cStringIO", "cStringIO", "io")
    assert move.name == "cStringIO"
    assert move.new_mod == "io"
    assert move.new_attr == "cStringIO"
    # Test the constructor with 4 parameters
    move = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert move.name == "cStringIO"
    assert move.new_mod == "io"
    assert move.new_attr == "StringIO"
    # Test the constructor with 5 parameters
    move = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO", "Input")
    assert move.name == "cStringIO"
    assert move.new_mod == "io"

# Generated at 2022-06-14 02:10:25.171378
# Unit test for constructor of class SixMovesTransformer

# Generated at 2022-06-14 02:10:28.843506
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    transformer = SixMovesTransformer()
    assert transformer.target == (2, 7)
    assert len(transformer.rewrites) == 31

# Generated at 2022-06-14 02:10:30.886094
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    pass


# Unit test at module level

# Generated at 2022-06-14 02:10:38.736637
# Unit test for constructor of class MovedModule
def test_MovedModule():
    mv_mod = MovedModule("name", "old")
    assert mv_mod.name == "name"
    assert mv_mod.old == "old"
    assert mv_mod.new == "name"

    mv_mod = MovedModule("name", "old", "new")
    assert mv_mod.name == "name"
    assert mv_mod.old == "old"
    assert mv_mod.new == "new"

# Generated at 2022-06-14 02:10:48.203583
# Unit test for constructor of class MovedModule
def test_MovedModule():
    with pytest.raises(TypeError) as excinfo:
        MovedModule()
    assert '__init__()' in str(excinfo.value)


# Generated at 2022-06-14 02:10:50.399626
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert not _get_rewrites()
    assert SixMovesTransformer.rewrites is not _get_rewrites()
    assert not _get_rewrites()

# Generated at 2022-06-14 02:11:00.014872
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    ma = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert ma.new_mod == "io"
    assert ma.new_attr == "StringIO"
    assert ma.name == "cStringIO"

    ma = MovedAttribute("filter", "itertools", "builtins", "ifilter", "filter")
    assert ma.new_mod == "builtins"
    assert ma.new_attr == "filter"
    assert ma.name == "filter"


# Generated at 2022-06-14 02:11:04.383752
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    a = MovedAttribute('foo', 'old.mod', 'new.mod', 'old.attr', 'new.attr')
    assert a.name == 'foo'
    assert a.new_mod == 'new.mod'
    assert a.new_attr == 'new.attr'



# Generated at 2022-06-14 02:11:06.944760
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert SixMovesTransformer(None)



# Generated at 2022-06-14 02:11:13.249806
# Unit test for constructor of class MovedModule
def test_MovedModule():
    mm = MovedModule("name", "old")
    assert mm.name == "name"
    assert mm.old == "old"
    assert mm.new == "name"

    mm = MovedModule("name", "old", "new")
    assert mm.name == "name"
    assert mm.old == "old"
    assert mm.new == "new"

# Generated at 2022-06-14 02:11:16.955997
# Unit test for constructor of class MovedModule
def test_MovedModule():
    mm = MovedModule("name", "old", "new")
    assert mm.name == "name"
    assert mm.old == "old"
    assert mm.new == "new"


# Generated at 2022-06-14 02:11:18.438114
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    t = SixMovesTransformer()
    assert t is not None

# Generated at 2022-06-14 02:11:26.157459
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    m = MovedAttribute('name', 'old_mod', 'new_mod', 'old_attr', 'new_attr')
    assert m.name == 'name'
    assert m.new_mod == 'new_mod'
    assert m.new_attr == 'new_attr'
    # Constructor should accept both old_attr and new_attr as None
    m = MovedAttribute('name', 'old_mod', 'new_mod')
    assert m.name == 'name'
    assert m.new_mod == 'new_mod'
    assert m.new_attr == 'name'
    # Without new_attr, new_attr should be old_attr
    m = MovedAttribute('name', 'old_mod', 'new_mod', 'old_attr')
    assert m.name == 'name'
    assert m.new_mod

# Generated at 2022-06-14 02:11:38.199678
# Unit test for constructor of class MovedModule
def test_MovedModule():
    import six.moves.configparser
    import six.moves.copyreg
    import six.moves.dbm_gnu
    import six.moves._dummy_thread
    import six.moves.http_cookiejar
    import six.moves.http_cookies
    import six.moves.html_entities
    import six.moves.html_parser
    import six.moves.http_client
    import six.moves.BaseHTTPServer
    import six.moves.CGIHTTPServer
    import six.moves.SimpleHTTPServer
    import six.moves.cPickle
    import six.moves.queue
    import six.moves.reprlib
    import six.moves.socketserver
    import six.moves._thread
    import six.moves.winreg

# Generated at 2022-06-14 02:11:56.626931
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    transformer = SixMovesTransformer('six.moves.urllib')
    assert transformer.rewrites == [('urllib.parse', 'six.moves.urllib_parse'), ('urllib.error', 'six.moves.urllib_error'), ('urllib.request', 'six.moves.urllib_request'), ('urllib.response', 'six.moves.urllib_response'), ('urllib.robotparser', 'six.moves.urllib_robotparser')]

# Generated at 2022-06-14 02:11:58.969850
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    """Test that SixMovesTransformer doesn't crash on initialization."""
    SixMovesTransformer()

# Generated at 2022-06-14 02:12:02.363583
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    cls = SixMovesTransformer
    assert len(cls.dependencies) == 1
    assert cls.dependencies[0] == 'six'
    assert len(cls.rewrites) == 56

# Generated at 2022-06-14 02:12:06.114676
# Unit test for constructor of class MovedModule
def test_MovedModule():
    actual = MovedModule('module', 'old').__dict__
    expected = {'name': 'module', 'new': 'module', 'old': 'old'}
    assert actual == expected


# Generated at 2022-06-14 02:12:13.967499
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    a = MovedAttribute("name", "old_mod", "new_mod")
    assert a.name == "name"
    assert a.new_mod == "new_mod"
    assert a.new_attr == "name"
    b = MovedAttribute("name", "old_mod", "new_mod", "old_attr")
    assert b.new_attr == "old_attr"
    c = MovedAttribute("name", "old_mod", "new_mod", "old_attr", "new_attr")
    assert c.new_attr == "new_attr"



# Generated at 2022-06-14 02:12:17.045108
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    with pytest.raises(TypeError):
        MovedAttribute("cStringIO", "cStringIO")


# Generated at 2022-06-14 02:12:26.935160
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    move = MovedAttribute("name", "old_mod", "new_mod", "old_attr", "new_attr")
    assert move.name == "name"
    assert move.new_mod == "new_mod"
    assert move.new_attr == "new_attr"
    assert str(move) == "name"
    move = MovedAttribute("name", "old_mod", "new_mod", "old_attr")
    assert move.name == "name"
    assert move.new_mod == "new_mod"
    assert move.new_attr == "old_attr"
    assert str(move) == "name"
    move = MovedAttribute("name", "old_mod", "new_mod")
    assert move.name == "name"
    assert move.new_mod == "new_mod"

# Generated at 2022-06-14 02:12:36.304243
# Unit test for constructor of class MovedModule
def test_MovedModule():
    assert MovedModule("name", "old").new == "name"
    assert MovedModule("name", "old").name == "name"
    assert MovedModule("name", "old").old == "old"
    assert MovedModule("name", "old", "new").new == "new"
    assert MovedModule("name", "old", "new").name == "name"
    assert MovedModule("name", "old", "new").old == "old"
    assert MovedModule("name", "old", "new").new == "new"



# Generated at 2022-06-14 02:12:39.899945
# Unit test for constructor of class MovedModule
def test_MovedModule():
        testMovedModule = MovedModule('module', 'old')
        assert testMovedModule.name == 'module'
        assert testMovedModule.new == 'module'

# Unit test 2 for constructor of class MovedModule

# Generated at 2022-06-14 02:12:44.722624
# Unit test for constructor of class MovedModule
def test_MovedModule():
    mod = MovedModule('name', 'old')
    assert mod.name == 'name'
    assert mod.old == 'old'
    assert mod.new == 'name'
    mod = MovedModule('name', 'old', 'new')
    assert mod.name == 'name'
    assert mod.old == 'old'
    assert mod.new == 'new'

# Generated at 2022-06-14 02:13:17.983367
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    name = "name"
    new_mod = "new_mod"
    new_attr = "new_attr"
    old_attr = "old_attr"
    old_mod = "old_mod"
    moved_attribute = MovedAttribute(name, old_mod, new_mod, old_attr,
                                     new_attr)
    assert moved_attribute.name == "name"
    assert moved_attribute.old_mod == "old_mod"
    assert moved_attribute.new_mod == "new_mod"
    assert moved_attribute.old_attr == "old_attr"
    assert moved_attribute.new_attr == "new_attr"


# Generated at 2022-06-14 02:13:26.242072
# Unit test for constructor of class MovedModule
def test_MovedModule():
    import sys
    moves = SixMovesTransformer.rewrites()
    for move in moves:
        try:
            __import__(move[1])
        except ImportError:
            print(move[1], ' Import Error')  # pragma: no cover
        print(move[0], " -> ", move[1])
        fix_module = '{} = {}'.format(move[0], move[1])
        exec(fix_module, sys.modules)
    test_module = __import__('requests.compat')
    assert test_module.queue.Queue is not None

# Generated at 2022-06-14 02:13:34.075487
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    move = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert move.name == "cStringIO"
    assert move.new_mod == "io"
    assert move.new_attr == "StringIO"

    move = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO", "StringIO2")
    assert move.name == "cStringIO"
    assert move.new_mod == "io"
    assert move.new_attr == "StringIO2"

    move = MovedAttribute("filter", "itertools", "builtins", "ifilter", "filter")
    assert move.name == "filter"
    assert move.new_mod == "builtins"
    assert move.new_attr == "filter"


# Generated at 2022-06-14 02:13:44.500783
# Unit test for constructor of class MovedModule
def test_MovedModule():
    class_ = MovedModule('name', 'old')
    assert class_.name == 'name'
    assert class_.old == 'old'
    assert class_.new == 'name'
    class_ = MovedModule('name', 'old', 'new')
    assert class_.name == 'name'
    assert class_.old == 'old'
    assert class_.new == 'new'
    # Calling with wrong number of arguments
    with pytest.raises(TypeError):
        class_ = MovedModule('name')
    with pytest.raises(TypeError):
        class_ = MovedModule('name', 'old', 'new', 'additional')

# Unit tests for constructor of class MovedAttribute

# Generated at 2022-06-14 02:13:47.212087
# Unit test for constructor of class MovedModule
def test_MovedModule():
    moved = MovedModule('module', 'old')
    assert moved.name == 'module'
    assert moved.new == 'module'
    assert moved.old == 'old'

# Generated at 2022-06-14 02:13:50.945790
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    ma = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert ma.name == "cStringIO"
    assert ma.new_attr == "StringIO"

# Generated at 2022-06-14 02:13:59.370764
# Unit test for constructor of class MovedModule
def test_MovedModule():
    test_value = MovedModule("builtins", "__builtin__")
    assert test_value.name == "builtins" and test_value.old == "__builtin__"
    assert test_value.new == "builtins"
    test_value = MovedModule("urllib", __name__ + ".moves.urllib")
    assert test_value.name == "urllib" and test_value.old == __name__ + ".moves.urllib"
    assert test_value.new == __name__ + ".moves.urllib"

# Generated at 2022-06-14 02:14:03.406058
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    ma = MovedAttribute(name='cStringIO', old_mod='cStringIO', new_mod='io', old_attr='StringIO')
    assert ma.name == 'cStringIO'
    assert ma.new_mod == 'io'
    assert ma.new_attr == 'StringIO'


# Generated at 2022-06-14 02:14:12.250362
# Unit test for constructor of class MovedModule
def test_MovedModule():
    moved_module = MovedModule(name='tkinter', old='Tkinter', new='tkinter')
    assert moved_module.name == 'tkinter'
    assert moved_module.old == 'Tkinter'
    assert moved_module.new == 'tkinter'

    moved_module = MovedModule(name='tkinter', old='Tkinter')
    assert moved_module.name == 'tkinter'
    assert moved_module.old == 'Tkinter'
    assert moved_module.new == 'tkinter'

# Generated at 2022-06-14 02:14:19.805140
# Unit test for constructor of class MovedModule
def test_MovedModule():
    mm=MovedModule('hello','world','hi')
    assert mm.name == 'hello'
    assert mm.new == 'hi'
    mm=MovedModule('hello','world')
    assert mm.name == 'hello'
    assert mm.new == 'hello'
    mm=MovedModule('hello',None,'hi')
    assert mm.name == 'hello'
    assert mm.new == 'hi'

# Generated at 2022-06-14 02:15:18.169506
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    """
    Tests the auto-generated constructor of MovedAttribute
    """
    ma = MovedAttribute("name", "old_mod", "new_mod", "old_attr", "new_attr")
    assert ma.name == "name"
    assert ma.new_mod == "new_mod"
    assert ma.new_attr == "new_attr"



# Generated at 2022-06-14 02:15:26.761546
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    attr = MovedAttribute("getcwd", "os", "os", "getcwdu", "getcwd")
    assert attr.name == "getcwd"
    assert attr.new_mod == "os"
    assert attr.old_attr is None
    assert attr.new_attr == "getcwd"

    attr = MovedAttribute("getcwd", "os", "os", "getcwdu")
    assert attr.name == "getcwd"
    assert attr.new_mod == "os"
    assert attr.old_attr == "getcwdu"
    assert attr.new_attr is None

    # Check the special case where new_attr is None, old_attr is None
    attr = MovedAttribute("StringIO", "StringIO", "io")
   

# Generated at 2022-06-14 02:15:38.887238
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    for prefix, moves in prefixed_moves:
        for move in moves:
            if isinstance(move, MovedAttribute):
                path = '{}.{}'.format(move.new_mod, move.new_attr)
                import_line = 'from six.moves{} import {}'.format(prefix, move.name)
                if '(' in import_line:
                    import_line = 'import six\n' + import_line
                cst = parse_module(import_line)
                SixMovesTransformer().visit_Module(cst)
                final_module = cst.code
                if '(' in import_line:
                    final_module = ''.join(final_module.split('\n')[1:])
                assert final_module == import_line

# Generated at 2022-06-14 02:15:44.204657
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    transformer = SixMovesTransformer()
    assert transformer.rewrites[0] == ('io.StringIO', 'six.moves.cStringIO')
    assert transformer.rewrites[-1] == ('urllib.robotparser.RobotFileParser', 'six.moves.urllib_robotparser.RobotFileParser')

# Generated at 2022-06-14 02:15:46.480325
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert len(SixMovesTransformer.rewrites) == len(set(SixMovesTransformer.rewrites))

# Generated at 2022-06-14 02:15:52.881670
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert MovedAttribute('cStringIO', 'cStringIO', 'io', 'StringIO')
    assert MovedAttribute('cStringIO', 'cStringIO', 'io')
    assert MovedAttribute('cStringIO', 'cStringIO', 'io', 'StringIO', 'cStringIO')
    assert MovedAttribute('cStringIO', 'cStringIO', None, 'StringIO', 'cStringIO')

# Generated at 2022-06-14 02:16:08.369195
# Unit test for constructor of class SixMovesTransformer