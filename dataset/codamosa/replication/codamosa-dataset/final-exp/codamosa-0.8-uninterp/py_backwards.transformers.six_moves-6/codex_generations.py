

# Generated at 2022-06-14 02:06:09.641424
# Unit test for constructor of class MovedModule
def test_MovedModule():
    assert MovedModule('name', 'old') == MovedModule('name', 'old')
    assert MovedModule('name', 'old') != MovedModule('name', 'old', 'new')
    assert MovedModule('name', 'old') != MovedModule('name', '0ld')
    assert MovedModule('name', 'old') != MovedModule('Name', 'old')
    assert MovedModule('name', 'old') != MovedModule('name', 'old', 'new')

# Generated at 2022-06-14 02:06:14.719034
# Unit test for constructor of class MovedModule
def test_MovedModule():
    assert MovedModule("name", "old").name == "name"
    assert MovedModule("name", "old").old == "old"
    assert MovedModule("name", "old").new == "name"
    assert MovedModule("name", "old", "new").name == "name"
    assert MovedModule("name", "old", "new").old == "old"
    assert MovedModule("name", "old", "new").new == "new"

# Generated at 2022-06-14 02:06:25.490936
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    s = string.Template("""from __future__ import absolute_import
import six
""")
    t = astroid.scoped_nodes.Module(None)
    t.name = 'test'
    x = SixMovesTransformer()
    for line in s.substitute(None).split('\n'):
        t.body.append(astroid.parse(line))
    print(unparse(astroid.parse('from six.moves import range, filter')))
    print(unparse(astroid.parse('from six.moves.urllib.parse import urlparse')))
    print(unparse(astroid.parse('from six.moves.urllib import urlparse')))
    print(unparse(astroid.parse('from six.moves.urllib.parse import urlparse')))
   

# Generated at 2022-06-14 02:06:35.025790
# Unit test for constructor of class MovedModule
def test_MovedModule():
    module1 = MovedModule("module1", "old_module1")
    assert(module1.name == "module1")
    assert(module1.new == "module1")
    assert(module1.old == "old_module1")

    module2 = MovedModule("module2", "old_module2", "new_module2")
    assert(module2.name == "module2")
    assert(module2.new == "new_module2")
    assert(module2.old == "old_module2")


# Generated at 2022-06-14 02:06:37.571697
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    SixMovesTransformer([])


if __name__ == '__main__':
    print(SixMovesTransformer.get_test_cases())

# Generated at 2022-06-14 02:06:48.714822
# Unit test for constructor of class SixMovesTransformer

# Generated at 2022-06-14 02:06:55.377949
# Unit test for constructor of class MovedModule
def test_MovedModule():
    def noclass():
        MovedModule(None, None)

    with pytest.raises(TypeError):
        noclass()
    assert MovedModule('name', 'old', 'new').name == 'name'
    with pytest.raises(TypeError):
        MovedModule('name', 'old', None)
    with pytest.raises(TypeError):
        MovedModule('name', 'old', None)

# Generated at 2022-06-14 02:07:06.646613
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert MovedAttribute('name', 'old_mod', 'new_mod', 'old_attr', 'new_attr').name == 'name'
    assert MovedAttribute('name', 'old_mod', 'new_mod', 'old_attr', 'new_attr').old_mod == 'old_mod'
    assert MovedAttribute('name', 'old_mod', 'new_mod', 'old_attr', 'new_attr').new_mod == 'new_mod'
    assert MovedAttribute('name', 'old_mod', 'new_mod', 'old_attr', 'new_attr').old_attr == 'old_attr'
    assert MovedAttribute('name', 'old_mod', 'new_mod', 'old_attr', 'new_attr').new_attr == 'new_attr'

# Generated at 2022-06-14 02:07:10.952219
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert len(_get_rewrites()) == len(SixMovesTransformer.rewrites)
    assert isinstance(_get_rewrites().__wrapped__(), tuple)

# Generated at 2022-06-14 02:07:16.804787
# Unit test for constructor of class MovedModule
def test_MovedModule():
    assert MovedModule('foo', 'bar').name == 'foo'
    assert MovedModule('foo', 'bar').new == 'foo'
    assert MovedModule('foo', 'bar', 'baz').new == 'baz'
    assert MovedModule('foo', 'bar', 'baz').name == 'foo'


# Generated at 2022-06-14 02:07:26.864574
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    import ast
    import difflib
    import sys
    from textwrap import dedent

    # Test code snippet
    test_snippet = dedent("""
    import collections
    import inspect
    import itertools
    import os
    import sys
    import threading
    import time
    import urllib
    import urllib2
    import urlparse

    import foo.bar.baz
    import a.b.c as x
    import a.b.c.d as y, a.b.c.e as z
    from foo.bar.baz import spam

    from a.b.c import spam, eggs as spam2

    from a.b.c import spam as spam3, eggs as spam4

    """)
    node = ast.parse(test_snippet)
    transformer = SixMovesTransformer

# Generated at 2022-06-14 02:07:31.279586
# Unit test for constructor of class MovedModule
def test_MovedModule():
    module = MovedModule("queue", "Queue")
    assert module.name == "queue" and module.new == "queue"
    module = MovedModule("queue", "_Queue", "Queue")
    assert module.name == "queue" and module.new == "Queue"

# Generated at 2022-06-14 02:07:42.370588
# Unit test for constructor of class SixMovesTransformer

# Generated at 2022-06-14 02:07:43.699096
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    SixMovesTransformer()

# Generated at 2022-06-14 02:07:53.004929
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert ('six.moves.urllib.parse', 'six.moves') in SixMovesTransformer.rewrites
    assert ('six.moves.urllib.error', 'six.moves') in SixMovesTransformer.rewrites
    assert ('six.moves.urllib.request', 'six.moves') in SixMovesTransformer.rewrites
    assert ('six.moves.urllib.response', 'six.moves') in SixMovesTransformer.rewrites
    assert ('six.moves.urllib.robotparser', 'six.moves') in SixMovesTransformer.rewrites

# Generated at 2022-06-14 02:08:01.723026
# Unit test for constructor of class MovedModule
def test_MovedModule():
    mod1 = MovedModule("builtins", "__builtin__")
    mod2 = MovedModule("urllib", __name__ + ".moves.urllib",
                       __name__ + ".moves.urllib")
    assert mod1.name == "builtins"
    assert mod1.old == "__builtin__"
    assert mod1.new == "builtins"
    assert mod2.name == "urllib"
    assert mod2.old == __name__ + ".moves.urllib"
    assert mod2.new == __name__ + ".moves.urllib"

# Generated at 2022-06-14 02:08:04.683980
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    # The following test will fail if a constructor of SixMovesTransformer class
    # is not properly defined.
    assert SixMovesTransformer is not None

# Generated at 2022-06-14 02:08:12.507042
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    try:
        from six.moves import urllib
    except ImportError:
        warnings.warn('Failed to import six.moves.urllib. Using dummy.')
        class urllib:
            class error:
                URLError = None
                HTTPError = None
                ContentTooShortError = None
    else:
        assert urllib.error.URLError is not None
        assert urllib.error.HTTPError is not None
        assert urllib.error.ContentTooShortError is not None

# Generated at 2022-06-14 02:08:13.229186
# Unit test for constructor of class MovedModule
def test_MovedModule():
    pass

# Generated at 2022-06-14 02:08:19.790516
# Unit test for constructor of class MovedModule
def test_MovedModule():
    mm = MovedModule("Queue", "Queue")
    assert mm.name == 'Queue'
    assert mm.new == 'Queue'
    mm = MovedModule("Queue", "Queue", "NewQueue")
    assert mm.name == 'Queue'
    assert mm.new == 'NewQueue'


# Generated at 2022-06-14 02:08:24.318795
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    SixMovesTransformer()

# Generated at 2022-06-14 02:08:35.921022
# Unit test for constructor of class SixMovesTransformer

# Generated at 2022-06-14 02:08:40.683983
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert len(_get_rewrites()) == len(_moved_attributes)+len(_urllib_parse_moved_attributes)+len(_urllib_error_moved_attributes)+len(_urllib_request_moved_attributes)+len(_urllib_response_moved_attributes)+len(_urllib_robotparser_moved_attributes)

# Generated at 2022-06-14 02:08:54.545231
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    assert len(SixMovesTransformer.rewrites) == 59
    assert SixMovesTransformer.rewrites[0][0] == 'io.StringIO'
    assert SixMovesTransformer.rewrites[0][1] == 'six.moves.cStringIO'
    assert SixMovesTransformer.rewrites[1][0] == 'builtins.filter'
    assert SixMovesTransformer.rewrites[1][1] == 'six.moves.filter'
    assert SixMovesTransformer.rewrites[2][0] == 'itertools.filterfalse'
    assert SixMovesTransformer.rewrites[2][1] == 'six.moves.filterfalse'
    assert SixMovesTransformer.rewrites[3][0] == 'builtins.input'

# Generated at 2022-06-14 02:08:57.908679
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    a = MovedAttribute("str", "__builtin__", "builtins")
    assert a.new_attr == "str"
    assert a.name == "str"
    assert a.new_mod == "builtins"

# Generated at 2022-06-14 02:09:06.871248
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert MovedAttribute("cStringIO", "cStringIO", "io", "StringIO").name == 'cStringIO'
    assert MovedAttribute("filter", "itertools", "builtins", "ifilter", "filter").new_mod == 'builtins'
    assert MovedAttribute("filterfalse", "itertools", "itertools", "ifilterfalse", "filterfalse").new_attr == 'filterfalse'
    assert MovedAttribute("input", "__builtin__", "builtins", "raw_input", "input").name == 'input'
    assert MovedAttribute("intern", "__builtin__", "sys").new_attr == 'intern'
    assert MovedAttribute("map", "itertools", "builtins", "imap", "map").new_attr == 'map'

# Generated at 2022-06-14 02:09:16.477464
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    class Foo:
        def __init__(self, x = 2, y = 3):
            self.x = x
            self.y = y


# Generated at 2022-06-14 02:09:27.060270
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    transformer = SixMovesTransformer(('2','7'))

    assert transformer.rewrites[('io.StringIO', 'six.moves.cStringIO.StringIO')] == True
    assert transformer.rewrites[('itertools.filterfalse', 'six.moves.filterfalse')] == True
    assert transformer.rewrites[('builtins.range', 'six.moves.range')] == True
    assert transformer.rewrites[('__builtin__.zip', 'six.moves.zip')] == True
    assert transformer.rewrites[('ConfigParser', 'six.moves.configparser')] == True
    assert transformer.rewrites[('Queue', 'six.moves.queue')] == True

# Generated at 2022-06-14 02:09:29.758926
# Unit test for constructor of class MovedModule
def test_MovedModule():
    mm = MovedModule("name", "old")
    assert mm.name == "name"
    assert mm.old == "old"
    assert mm.new == "name"

# Generated at 2022-06-14 02:09:35.746173
# Unit test for constructor of class MovedModule
def test_MovedModule():
    '''
    This unit test tests the constructor of class MovedModule
    '''
    modul = MovedModule("builtins", "__builtin__")
    assert modul.name == "builtins"
    assert modul.old == "__builtin__"
    assert modul.new == "builtins"


# Generated at 2022-06-14 02:09:48.581031
# Unit test for constructor of class MovedModule
def test_MovedModule():
    MM = MovedModule('name', 'old', 'new')
    assert MM.name == 'name'
    assert MM.old == 'old'
    assert MM.new == 'new'

    MM = MovedModule('name', 'old')
    assert MM.name == 'name'
    assert MM.old == 'old'
    assert MM.new == 'name'

# Generated at 2022-06-14 02:09:53.938272
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    actual = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert actual.name == "cStringIO"
    assert actual.new_mod == "io"
    assert actual.new_attr == "StringIO"


# Generated at 2022-06-14 02:09:58.323397
# Unit test for constructor of class MovedModule
def test_MovedModule():
    mod = MovedModule("testmod", "testlib.module")
    assert mod.name == "testmod"
    assert mod.new == "testmod"


# Generated at 2022-06-14 02:10:02.118859
# Unit test for constructor of class MovedModule
def test_MovedModule():
    with pytest.raises(TypeError) as excinfo:
        test = MovedModule()
    excinfo.match(r"__init__\(\) missing 1 required positional argument: 'name'")

# Generated at 2022-06-14 02:10:08.539109
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    data = ('name' , 'old_mod', 'new_mod', 'old_attr', 'new_attr')
    test_moves = [MovedAttribute(*move) for move in data]
    for move in test_moves:
        assert move.name == 'name'
        assert move.new_mod == 'new_mod'
        assert move.new_attr == 'new_attr'

# Generated at 2022-06-14 02:10:21.508647
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    m1 = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO", "StringIO")
    assert m1.name == "cStringIO"
    assert m1.new_mod == "io"
    assert m1.new_attr == "StringIO"
    m2 = MovedAttribute("cStringIO", "cStringIO", "io")
    assert m2.name == "cStringIO"
    assert m2.new_mod == "io"
    assert m2.new_attr == "cStringIO"
    m3 = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert m3.name == "cStringIO"
    assert m3.new_mod == "io"
    assert m3.new_attr == "StringIO"
    m4

# Generated at 2022-06-14 02:10:23.785094
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    t = SixMovesTransformer()
    assert t.rewrites == list(_get_rewrites())

# Generated at 2022-06-14 02:10:29.927240
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    class_moved_attribute = MovedAttribute(
        "name",
        "old_mod",
        "new_mod",
        "old_attr",
        "new_attr")
    assert class_moved_attribute.name == "name"
    assert class_moved_attribute.new_mod == "new_mod"
    assert class_moved_attribute.new_attr == "new_attr"



# Generated at 2022-06-14 02:10:34.225897
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    ma = MovedAttribute('hello', 'world', 'hello')
    assert ma.name == 'hello'
    assert ma.new_mod == 'hello'
    assert ma.new_attr == 'hello'


# Generated at 2022-06-14 02:10:38.176140
# Unit test for constructor of class MovedModule
def test_MovedModule():
    moved_module = MovedModule("name", "old", "new")
    assert moved_module.name == "name"
    assert moved_module.old == "old"
    assert moved_module.new == "new"


# Generated at 2022-06-14 02:10:54.026022
# Unit test for constructor of class MovedModule
def test_MovedModule():
    obj = MovedModule("os", "os", "new")
    assert obj.name == "os"
    assert obj.new == "new"

    obj = MovedModule("os", "os")
    assert obj.new == "os"

# Generated at 2022-06-14 02:10:59.955501
# Unit test for constructor of class MovedModule
def test_MovedModule():
    m1 = MovedModule("name", "old", "new")
    assert m1.name == "name"
    assert m1.old == "old"
    assert m1.new == "new"
    m2 = MovedModule("name", "old")
    assert m2.name == "name"
    assert m2.old == "old"
    assert m2.new == "name"

# Generated at 2022-06-14 02:11:04.010974
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    ma = MovedAttribute('some_name', 'old_mod', 'new_mod', 'old_attr', 'new_attr')
    assert ma.name == 'some_name'
    assert ma.new_mod == 'new_mod'
    assert ma.new_attr == 'new_attr'


# Generated at 2022-06-14 02:11:18.091583
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    moves = _get_rewrites()

    # check that each has been found

# Generated at 2022-06-14 02:11:20.887327
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    from .. import jedi_api
    # This should not throw any errors
    script = jedi_api.Script("from six.moves import configparser", 2, 7, '')
    script.completions()

# Generated at 2022-06-14 02:11:31.686914
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    a = MovedAttribute('cStringIO', 'cStringIO', 'io', 'StringIO')
    assert a.name == 'cStringIO'
    assert a.new_mod == 'io'
    assert a.new_attr == 'StringIO'
    b = MovedAttribute('intern', '__builtin__', 'sys')
    assert b.name == 'intern'
    assert b.new_mod == 'sys'
    assert b.new_attr == 'intern'

test_data = '''\
import cStringIO
from cStringIO import StringIO
import sys
from __builtin__ import intern
'''



# Generated at 2022-06-14 02:11:37.091521
# Unit test for constructor of class MovedModule
def test_MovedModule():
    obj = MovedModule(name = 'aaa', old = 'aaa_old', new = 'aaa_new')
    assert obj.name == 'aaa'
    assert obj.new == 'aaa_new'
    obj = MovedModule(name = 'aaa', old = 'aaa_old')
    assert obj.name == 'aaa'
    assert obj.new == 'aaa'

# Generated at 2022-06-14 02:11:51.236224
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    # type: () -> None
    MovedAttribute('cStringIO', 'cStringIO', 'io', 'StringIO')
    MovedAttribute('filter', 'itertools', 'builtins', 'ifilter', 'filter')
    MovedAttribute('filterfalse', 'itertools', 'itertools', 'ifilterfalse', 'filterfalse')
    MovedAttribute('input', '__builtin__', 'builtins', 'raw_input', 'input')
    MovedAttribute('intern', '__builtin__', 'sys')
    MovedAttribute('map', 'itertools', 'builtins', 'imap', 'map')
    MovedAttribute('getcwd', 'os', 'os', 'getcwdu', 'getcwd')

# Generated at 2022-06-14 02:11:54.403095
# Unit test for constructor of class MovedModule
def test_MovedModule():
    m = MovedModule("name", "old", "new")
    assert m.name == "name"
    assert m.old == "old"
    assert m.new == "new"

# Generated at 2022-06-14 02:12:03.766989
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    for prefix, moves in prefixed_moves:
        for move in moves:
            if isinstance(move, MovedAttribute):
                path = '{}.{}'.format(move.new_mod, move.new_attr)
                assert (path, 'six.moves{}.{}'.format(prefix, move.name)) in SixMovesTransformer.rewrites
            elif isinstance(move, MovedModule):
                assert (move.new, 'six.moves{}.{}'.format(prefix, move.name)) in SixMovesTransformer.rewrites

# Generated at 2022-06-14 02:12:37.933630
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    if sys.version_info[:2] >= (3, 5):
        attribute = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
        assert attribute.name == "cStringIO"
        assert attribute.new_attr == "StringIO"
        assert attribute.new_mod == "io"
    else:
        attribute = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
        assert attribute.name == "cStringIO"
        assert attribute.new_attr == "cStringIO"
        assert attribute.new_mod == "io"

# Generated at 2022-06-14 02:12:48.307119
# Unit test for constructor of class MovedModule
def test_MovedModule():
    t1 = MovedModule("builtins", "__builtin__", "builtins")
    t2 = MovedModule("configparser", "ConfigParser", "configparser")
    t3 = MovedModule("copyreg", "copy_reg", "copyreg")
    assert t1.name == "builtins"
    assert t1.old == "__builtin__"
    assert t1.new == "builtins"
    assert t2.name == "configparser"
    assert t2.old == "ConfigParser"
    assert t2.new == "configparser"
    assert t3.name == "copyreg"
    assert t3.old == "copy_reg"
    assert t3.new == "copyreg"


# Unit test to check if the attribute list _moved_attributes
# is constant and in accordance with the

# Generated at 2022-06-14 02:12:57.327087
# Unit test for constructor of class MovedModule
def test_MovedModule():
    assert MovedModule("builtins", "_builtin__").name == "builtins"
    assert MovedModule("builtins", "_builtin__").new == "builtins"
    assert MovedModule("builtins", "_builtin__").old == "_builtin__"

    assert MovedModule("builtins", "_builtin__", "__builtin__").name == "builtins"
    assert MovedModule("builtins", "_builtin__", "__builtin__").new == "__builtin__"
    assert MovedModule("builtins", "_builtin__", "__builtin__").old == "_builtin__"


# Generated at 2022-06-14 02:13:11.002421
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    move1 = MovedAttribute("map", "builtins", "itertools", "imap", "map")
    assert move1.name == "map"
    assert move1.new_mod == "itertools"
    assert move1.new_attr == "imap"
    move2 = MovedAttribute("map", "builtins", "itertools", old_attr="imap")
    assert move2.name == "map"
    assert move2.new_mod == "itertools"
    assert move2.new_attr == "imap"
    move3 = MovedAttribute("map", "builtins", "itertools")
    assert move3.name == "map"
    assert move3.new_mod == "itertools"
    assert move3.new_attr == "map"
    move4 = Moved

# Generated at 2022-06-14 02:13:14.070894
# Unit test for constructor of class MovedModule
def test_MovedModule():
    old = 'servicenow'
    new = 'snow'
    mm = MovedModule(old, old, new)
    assert mm.name == old
    assert mm.new == new

# Generated at 2022-06-14 02:13:24.813876
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    transformer = SixMovesTransformer()
    assert transformer.target == (2, 7)
    assert transformer.dependencies == ['six']

# Generated at 2022-06-14 02:13:28.473063
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    moved_attribute = MovedAttribute("cStringIO", "cStringIO", "io", "StringIO")
    assert moved_attribute.name == "cStringIO"
    assert moved_attribute.new_mod == "io"
    assert moved_attribute.new_attr == "StringIO"

# Generated at 2022-06-14 02:13:35.132344
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    m_attr = MovedAttribute('cStringIO', 'cStringIO', 'io', 'StringIO')
    assert m_attr.name == 'cStringIO'
    assert m_attr.new_mod == 'io'
    assert m_attr.new_attr == 'StringIO'
    m_attr = MovedAttribute('cStringIO', 'cStringIO', 'io')
    assert m_attr.name == 'cStringIO'
    assert m_attr.new_mod == 'io'
    assert m_attr.new_attr == 'cStringIO'
    m_attr = MovedAttribute('cStringIO', 'cStringIO')
    assert m_attr.name == 'cStringIO'
    assert m_attr.new_mod == 'cStringIO'
    assert m_attr.new_attr == 'cStringIO'

# Generated at 2022-06-14 02:13:43.063128
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():
    from .base import check_transform
    from .six import SixImportRewrite
    code = """
        from six.moves import filter
        from six.moves import map
        from six.moves import range
        from six.moves.urllib.parse import urlencode
    """
    output = """
        import six
        import builtins
        import functools
        import six
        import builtins
        import six
        import builtins
        import six
        import six.moves.urllib.parse
        filter = six.moves.filter
        map = six.moves.map
        range = six.moves.range
        urlencode = six.moves.urllib.parse.urlencode
    """.strip()
    check_transform(SixImportRewrite(), code, output)

# Generated at 2022-06-14 02:13:48.567349
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    # type: () -> None
    move = MovedAttribute("name", "old_mod", "new_mod", "old_attr", "new_attr")
    assert move.name == "name"
    assert move.new_mod == "new_mod"
    assert move.new_attr == "new_attr"
    move = MovedAttribute("name", "old_mod", "new_mod", "old_attr")
    assert move.name == "name"
    assert move.new_mod == "new_mod"
    assert move.new_attr == "old_attr"
    move = MovedAttribute("name", "old_mod", "new_mod")
    assert move.name == "name"
    assert move.new_mod == "new_mod"
    assert move.new_attr == "name"
    move = M

# Generated at 2022-06-14 02:14:55.920303
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

    move = MovedAttribute("name", "old_mod", "new_mod", "old_attr")
    assert move.name == "name"
    assert move.new_mod == "new_mod"
    assert move.new_attr == "old_attr"

# Generated at 2022-06-14 02:14:57.672699
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    assert MovedAttribute('cStringIO', 'cStringIO', 'io', 'StringIO')

# Generated at 2022-06-14 02:15:07.849205
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    a1 = MovedAttribute("quote", "urllib", "urllib.parse", "quote", "quote")
    assert a1.name == "quote"
    assert a1.new_mod == "urllib.parse"
    assert a1.new_attr == "quote"
    a2 = MovedAttribute("quote", "urllib", "urllib.parse")
    assert a2.name == "quote"
    assert a2.new_mod == "urllib.parse"
    assert a2.new_attr == "quote"
    a3 = MovedAttribute("quote", "urllib", "urllib.parse", "quote")
    assert a3.name == "quote"
    assert a3.new_mod == "urllib.parse"

# Generated at 2022-06-14 02:15:12.054405
# Unit test for constructor of class MovedModule
def test_MovedModule():
    obj = MovedModule("name","old")
    assert obj.name == "name"
    assert obj.old == "old"
    assert obj.new == "name"


# Generated at 2022-06-14 02:15:16.774449
# Unit test for constructor of class MovedModule
def test_MovedModule():
    m = MovedModule('name', 'old')
    assert m.name == 'name'
    assert m.new == 'name'
    m = MovedModule('name', 'old', 'new')
    assert m.name == 'name'
    assert m.new == 'new'

# Generated at 2022-06-14 02:15:27.776348
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    test_object = MovedAttribute('test_name', 'test_old_mod', 'test_new_mod')
    assert test_object.name == 'test_name'
    assert test_object.new_mod == 'test_new_mod'
    assert test_object.new_attr == 'test_name'

    test_object_2 = MovedAttribute('test_name_2', 'test_old_mod_2', 'test_new_mod_2', 'test_old_attr_2', 'test_new_attr_2')
    assert test_object_2.name == 'test_name_2'
    assert test_object_2.new_mod == 'test_new_mod_2'
    assert test_object_2.new_attr == 'test_new_attr_2'



# Generated at 2022-06-14 02:15:34.732147
# Unit test for constructor of class MovedModule
def test_MovedModule():
    new_module = MovedModule('new_name', 'old_name')
    assert new_module.name == 'new_name'
    assert new_module.new == 'new_name'

    new_module = MovedModule('new_name', 'old_name', 'moved_name')
    assert new_module.name == 'new_name'
    assert new_module.new == 'moved_name'

# Generated at 2022-06-14 02:15:39.381625
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():
    obj=MovedAttribute('cStringIO', 'cStringIO', 'io', 'StringIO')
    assert obj.name == 'cStringIO'
    assert obj.new_mod == 'io'
    assert obj.new_attr == 'StringIO'


# Generated at 2022-06-14 02:15:41.736434
# Unit test for constructor of class MovedModule
def test_MovedModule():
    assert MovedModule("builtins", "__builtin__") == MovedModule("builtins", "__builtin__")

# Generated at 2022-06-14 02:15:46.572359
# Unit test for constructor of class MovedModule
def test_MovedModule():
    assert MovedModule('n1', 'n1')
    assert MovedModule('n1', 'n1', 'n1')
    assert MovedModule('n1', 'n2')
    assert MovedModule('n1', 'n2', 'n1')
    assert MovedModule('n1', 'n2', 'n3')
