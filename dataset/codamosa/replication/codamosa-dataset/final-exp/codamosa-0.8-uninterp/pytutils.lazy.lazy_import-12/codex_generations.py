

# Generated at 2022-06-14 06:00:07.753337
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__ is the same as __str__"""
    import bzrlib.lazy_import
    bzrlib.lazy_import.lazy_import(globals(), """
        from bzrlib.lazy_import import IllegalUseOfScopeReplacer
        """)

    # test that __unicode__ is the same as __str__
    e = IllegalUseOfScopeReplacer('foo', 'bar')
    assert e.__unicode__() == e.__str__()
    assert isinstance(e.__unicode__(), unicode)
    assert isinstance(e.__str__(), str)
    assert str(e) == 'bar'
    assert isinstance(repr(e), str)

# Generated at 2022-06-14 06:00:11.855955
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__ should return a unicode object"""
    e = IllegalUseOfScopeReplacer('x', 'msg')
    u = unicode(e)
    assert isinstance(u, unicode)



# Generated at 2022-06-14 06:00:21.676346
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    # Make sure that ScopeReplacer really calls its real object
    class TestModule(object):
        @staticmethod
        def real_func(arg):
            return arg
    sr = ScopeReplacer({}, lambda self,scope,name: TestModule, 'real_func')

    assert 'real_func' in globals()
    assert isinstance(real_func, ScopeReplacer)

    assert real_func('foo') == 'foo'

    # Now make sure that the real function is back
    assert isinstance(real_func, type(TestModule.real_func))
    assert real_func('bar') == 'bar'



# Generated at 2022-06-14 06:00:28.126787
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """__str__ of IllegalUseOfScopeReplacer is correct."""

    obj = IllegalUseOfScopeReplacer(name='name',
                                    msg='msg',
                                    extra='extra')
    expected = ("ScopeReplacer object 'name' was used incorrectly:"
                " 'msg': 'extra'")
    result = str(obj)
    assert result == expected, "%r != %r" % (result, expected)



# Generated at 2022-06-14 06:00:32.411931
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """IllegalUseOfScopeReplacer.__str__()"""
    e = IllegalUseOfScopeReplacer("a", "b")
    str(e)
    e.extra = "c"
    str(e)



# Generated at 2022-06-14 06:00:37.982644
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """test method __str__ of class IllegalUseOfScopeReplacer."""
    e = IllegalUseOfScopeReplacer('foo', 'bar')
    s = str(e)
    assert isinstance(s, str)
    assert e.__dict__['name'] == 'foo'
    assert 'foo' in s



# Generated at 2022-06-14 06:00:43.402468
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    import bzrlib.lazy_import
    scope = {}
    scope["a"] = bzrlib.lazy_import.ScopeReplacer(scope,
        lambda self,x,y:x[y] + 5, "a")
    scope["a"](5)
    scope["a"] = bzrlib.lazy_import.ScopeReplacer(scope, lambda self,x,y:x[y]
        + 5, "a")
    scope["a"](10)
    scope["a"](15)



# Generated at 2022-06-14 06:00:53.657704
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """Testing method __str__ of class IllegalUseOfScopeReplacer"""
    import re
    testtext = '''Unprintable exception IllegalUseOfScopeReplacer: dict={'name': 'foo', 'msg': 'bar', 'extra': ''}, fmt=%(name)r was used incorrectly: %(msg)s%(extra)s, error='''
    e = IllegalUseOfScopeReplacer('foo', 'bar')
    res = str(e)
    m = re.match(r'^' + testtext + r'$', res)
    assert m is not None, 'Not matched: %r' % (res,)
test_IllegalUseOfScopeReplacer___str__()

# Generated at 2022-06-14 06:01:01.698038
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    # test_ScopeReplacer___setattr__ is generated automatically by
    # pydoc testtools.TestCase.__test_ScopeReplacer___setattr__
    # from testtools/testcase.py test_ScopeReplacer___setattr__
    from unittest import TestCase
    class test_ScopeReplacer___setattr__(TestCase):
        def test_ScopeReplacer___setattr__(self):
            self.fail("unimplemented test case")
    return test_ScopeReplacer___setattr__



# Generated at 2022-06-14 06:01:09.463338
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """IllegalUseOfScopeReplacer.__unicode__ is tested elsewhere."""
    i = IllegalUseOfScopeReplacer("name", "msg")
    assert isinstance(i, str)
    assert isinstance(i, unicode)
    import bzrlib.tests
    bzrlib.tests.per_interpreter_deferred(
        test_IllegalUseOfScopeReplacer___unicode__)



# Generated at 2022-06-14 06:01:23.881471
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """IllegalUseOfScopeReplacer.__str__ should return a str object.

    This method is called by the traceback module when formatting an
    exception.
    """
    ex = IllegalUseOfScopeReplacer('foo', 'bar')
    str(ex)
    repr(ex)
    str(ex)



# Generated at 2022-06-14 06:01:33.568987
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    """test ScopeReplacer.__call__"""
    # the below import must be done in this module to ensure that
    # tests.per_module_imports.TestModuleImports still fails.
    import unittest
    import bzrlib.lazy_import

    class _SampleClass(unittest.TestCase):
        def __call__(self):
            pass

    _replacer = bzrlib.lazy_import.ScopeReplacer({}, lambda s,
        scope, name:_SampleClass, 'name')
    _replacer()


# Generated at 2022-06-14 06:01:41.412470
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    class Foo(object):
        def __init__(self):
            self.x = 0
        def increment_x(self):
            self.x = self.x + 1
        def get_x(self):
            return self.x
    class Bar(object):
        def __init__(self):
            self.x = 0
        def set_x(self, x):
            self.x = x
    s = {'Foo':None}
    ScopeReplacer(s, lambda self, scope, name: Foo(), 'Foo')
    foo = s['Foo']
    foo.increment_x()
    bar = Bar()
    bar.set_x(foo.get_x())
    assert bar.x == 1

    s = {'Bar':None}

# Generated at 2022-06-14 06:01:53.147487
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """__str__: return a string object

    This is not a test of the semantic correctness of the results, just whether
    the API is correctly implemented.

    It will call the function __format__() with an empty format String.

    """
    for s in ['', ' ', '\n', u'', u' ', u'\n']:
        # This forces the _get_format_string to return a string instead of the
        # unicode object we use for translation purposes.
        t = IllegalUseOfScopeReplacer(s, s, extra=s)
        t._fmt = t._get_format_string()
        s_str = str(t)
        assert isinstance(s_str, str)
        assert not isinstance(s_str, unicode)
        assert str(t) == s_str



# Generated at 2022-06-14 06:01:55.266931
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    import bzrlib.tests
    bzrlib.tests.TestSkipped("Not implemented")
    pass

# Generated at 2022-06-14 06:02:05.617844
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    """This test is needed to avoid future regressions in this method.

    In particular, it has to verify the correctness of the attribute
    replacement in the case where the attribute is '__class__'. In this
    particular case, the method __setattr__ can't be used on the object
    since that method is defined by the class type, raising a TypeError
   (read-only attribute).
    """
    import bzrlib.tests
    bzrlib.tests.load_tests.load_test_by_name(
        b'bzrlib.tests.lazy_import.test_ScopeReplacer')


# Generated at 2022-06-14 06:02:15.254427
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    from bzrlib.tests import TestCase
    class SimpleMod(object):
        def func(self):
            return "func"
    def create_obj(replacer, scope, name):
        return SimpleMod()
    scope = {}
    replacer = ScopeReplacer(scope, create_obj, "mod")
    self.assertRaises(IllegalUseOfScopeReplacer, replacer.func)
    self.assertEqual("func", scope["mod"].func())
    self.assertEqual("func", replacer.func())



# Generated at 2022-06-14 06:02:24.036123
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    import bzrlib.lazy_import

    def factory(self, scope, name):
        class MyObject(object):
            def __call__(self, *args, **kwargs):
                return '%s %s %s %s' % (name, scope, args, kwargs)

        self._real_obj = MyObject()
        scope[name] = self._real_obj
        return self._real_obj

    scope = {}
    bzrlib.lazy_import.ScopeReplacer(scope, factory, 'MyObject')
    assert scope['MyObject']() == 'MyObject {} () {}'
    assert scope['MyObject'](1) == 'MyObject {} (1,) {}'
    assert scope['MyObject'](1, 2, 3) == 'MyObject {} (1, 2, 3) {}'


# Generated at 2022-06-14 06:02:35.935701
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    from bzrlib._lazy_import_test_module import LazyClass, LazyFunc, LazyModule
    class DummyScope(object):
        def __init__(self, name, value):
            self.name = name
            self.value = value
            self.seen = False
        def __setitem__(self, name, value):
            self.name = name
            self.value = value
            self.seen = True
        def __getitem__(self, name):
            self.name = name
            return self.value

    def dummy_factory(this, scope, name):
        if name == 'LazyClass':
            return LazyClass()
        if name == 'LazyFunc':
            return LazyFunc()
        if name == 'LazyModule':
            return LazyModule()


# Generated at 2022-06-14 06:02:40.369503
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__ should return the formatted message, even if that message
    contains non-ascii characters."""
    e = IllegalUseOfScopeReplacer("foo", "\xc3\xa9")
    # __unicode__ should always return a unicode
    # object, not a str object.
    msg = unicode(e)
    # The message should contain the funky, non-ascii character because the
    # constructor told the exception to.
    assert msg.find("\xc3\xa9") != -1


# Generated at 2022-06-14 06:02:56.188102
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """Unit Test for IllegalUseOfScopeReplacer.__unicode__()."""
    from bzrlib import tests
    from bzrlib.tests.test_lazy_import import (
        IllegalUseOfScopeReplacer,
        )
    x = IllegalUseOfScopeReplacer('foo', 'weird')
    tests.TestCase.assertIsInstance(x, Exception)
    tests.TestCase.assertIsInstance(x, IllegalUseOfScopeReplacer)
    tests.TestCase.assertIsInstance(x._format(), str)
    tests.TestCase.assertIsInstance(x.__str__(), str)
    tests.TestCase.assertIsInstance(x.__unicode__(), unicode)
    tests.TestCase.assertIsInstance(x.__repr__(), str)

# Generated at 2022-06-14 06:02:59.568951
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__ should be reversible"""
    err = IllegalUseOfScopeReplacer('name', 'msg', 'extra')
    assert isinstance(err.__unicode__(), unicode)
    assert unicode(err) == err.__unicode__()

# Generated at 2022-06-14 06:03:09.163034
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """Method __str__ must return a non-unicode string."""
    # Verify that the method always returns a non-unicode string.
    e = IllegalUseOfScopeReplacer('foo', 'bar')
    # If this call raises a UnicodeEncodeError then the method is broken.
    str(e)


# The ScopeReplacer class is used by the lazy_import utility to ensure that
# the modules that it imports are available under the correct name in the
# calling scope.
#
# It is not considered part of the public API and should never be used
# directly.

# Generated at 2022-06-14 06:03:15.316297
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__ should always return a unicode object,
    even when called in a non-unicode context."""
    e = IllegalUseOfScopeReplacer('foo', 'bar')
    s = str(e)
    assert s.startswith('Unprintable exception')
    assert isinstance(s, str)
    u = unicode(e)
    assert u.startswith(u'Unprintable exception')
    assert isinstance(u, unicode)
    # And just in case:
    u = unicode(e)
    assert u.startswith(u'Unprintable exception')
    assert isinstance(u, unicode)



# Generated at 2022-06-14 06:03:27.848470
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    from bzrlib.lazy_import import lazy_import
    lazy_import(globals(), '''
    from bzrlib.lazy_import import ScopeReplacer
    ''')
    class A(object):
        def __call__(self, i):
            return i + 1
    a = A()
    # Assign to a preprocessed variable
    b = lazy_import(globals(), '''
    from bzrlib.lazy_import import ScopeReplacer
    ''')
    b._resolve()
    assert b.ScopeReplacer is ScopeReplacer
    assert not isinstance(a, ScopeReplacer)
    assert isinstance(b.ScopeReplacer, ScopeReplacer)
    assert b.ScopeReplacer(a, a, 'a') is a

# Generated at 2022-06-14 06:03:29.865306
# Unit test for method __getattribute__ of class ScopeReplacer
def test_ScopeReplacer___getattribute__():
    obj = ScopeReplacer()
    pass



# Generated at 2022-06-14 06:03:37.045261
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    from bzrlib.tests.test_lazy_import import TestScopeReplacer
    from bzrlib.tests.test_lazy_import import Foo
    scope = {}
    def factory(replacer, scope, name):
        return Foo()
    name = 'foo'
    foo = ScopeReplacer(scope, factory, name)
    TestScopeReplacer.assertIsInstance(foo, Foo)

# Generated at 2022-06-14 06:03:40.633852
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    e = IllegalUseOfScopeReplacer('foo', 'bar', 'a message')
    u = u'foo bar: a message'
    return e.__unicode__() == u

# Generated at 2022-06-14 06:03:46.920423
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """Unit test for method __unicode__ of class IllegalUseOfScopeReplacer"""
    import bzrlib.lazy_import
    bzrlib.lazy_import._ = lambda x: unicode(x)
    e = bzrlib.lazy_import.IllegalUseOfScopeReplacer(u'name', u'message')
    bzrlib.lazy_import._ = lambda x: x
    assert not isinstance(e.__unicode__(), unicode)
    assert not isinstance(e.__str__(), unicode)
    assert not isinstance(e.__str__(), str)



# Generated at 2022-06-14 06:03:55.692972
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    from StringIO import StringIO
    e = IllegalUseOfScopeReplacer("name1", "msg1")
    expected = "[IllegalUseOfScopeReplacer('name1')] msg1"
    out = StringIO()
    out.write("[%s] " % str(e))
    out.write(str(e))
    result = out.getvalue()
    assert expected == result, \
        "actual: %r\n  expected: %r\n" % (result, expected)



# Generated at 2022-06-14 06:04:08.913949
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """Ensure __str__ of IllegalUseOfScopeReplacer works"""
    m = "The giraffe with purple spots slipped on the banana"
    ex = IllegalUseOfScopeReplacer("object name", m)
    s = str(ex)
    u = unicode(ex)
    assert s == u.encode('ascii')


# Generated at 2022-06-14 06:04:15.943662
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    from bzrlib.lazy_import import lazy_import
    import bzrlib
    def f(x,y):
        return x+y
    bzrlib.f = f
    lazy_import(locals(), '''
    from bzrlib import f
    ''')
    assert f(1,2) == 3

# Generated at 2022-06-14 06:04:22.593604
# Unit test for method __getattribute__ of class ScopeReplacer
def test_ScopeReplacer___getattribute__():
    import bzrlib
    e = bzrlib.errors
    bzrlib.errors = lambda x : x
    l = ScopeReplacer(locals(), lambda self, scope, name : None, 'e')
    try:
        try:
            # Testing with a function
            assert e.__getattribute__('__call__') == l.__getattribute__('__call__')
        except AttributeError:
            pass
        try:
            # Testing with a class
            assert e.__getattribute__('CleanupError').__name__ == 'CleanupError'
        except AttributeError:
            pass
        try:
            # Testing with a module
            assert e.__getattribute__('errors') is e.errors
        except AttributeError:
            pass
    finally:
        bzrlib.errors = e



# Generated at 2022-06-14 06:04:26.991958
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    # call
    obj = ScopeReplacer({}, lambda me, scope, name: name, 'abc')
    # call
    obj()
    expected = 'abc'
    actual = obj()
    assert actual == expected, '%r != %r' % (actual, expected)

# Generated at 2022-06-14 06:04:38.789058
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """IllegalUseOfScopeReplacer.__str__ should return a str object

    This is a str() object, whose value is the result of the unicode
    conversion.
    """
    e = IllegalUseOfScopeReplacer('test', 'foo')
    assert type(e.__str__()) is str
    assert type(str(e)) is str
    assert type(unicode(e)) is unicode
    assert type(e) is not str
    assert type(u'abc') is unicode
    assert type(u'abc'.encode('utf8')) is str

from bzrlib.trace import mutter
from bzrlib.symbol_versioning import (
    deprecated_function,
    deprecated_in,
    )
from bzrlib.transport import (
    get_transport,
    )


# Generated at 2022-06-14 06:04:45.431550
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """String representation should be nicely formatted."""
    e = IllegalUseOfScopeReplacer("name", "msg", "extra")
    assert str(e) == "ScopeReplacer object 'name' was used incorrectly:" \
        " msg: extra"
    e._fmt = "%(msg)s"
    assert str(e) == "msg"



# Generated at 2022-06-14 06:04:55.172950
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    from cStringIO import StringIO
    from bzrlib.lazy_import import ScopeReplacer
    from bzrlib import (
        errors,
        osutils,
        branch,
        )

    def factory(self, scope, name):
        _scope = object.__getattribute__(self, '_scope')
        _name = object.__getattribute__(self, '_name')
        if name != _name:
            raise IllegalUseOfScopeReplacer(_name, "Wrong name passed")
        if _scope is not scope:
            raise IllegalUseOfScopeReplacer(_name, "Wrong scope passed")
        return False
    ScopeReplacer({}, factory, 'a')
    a = ScopeReplacer({}, factory, 'a')
    assert not a
    assert a is False and ScopeReplacer._should_proxy


# Generated at 2022-06-14 06:05:08.093793
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    import bzrlib.tests as tests
    tests.TestCaseWithMemoryTransport.feature_flags.add('lazy_import')
    class test_ScopeReplacer___setattr__(tests.TestCaseWithMemoryTransport):
        def test_ScopeReplacer___setattr__(self):
            import bzrlib.lazy_import
            bzrlib.lazy_import._should_proxy = False
            import bzrlib.tests as tests
            from bzrlib.lazy_import import ScopeReplacer
            import bzrlib.tests.blackbox

            tests.blackbox = ScopeReplacer({}, bzrlib.tests.blackbox._resolve,
                'blackbox')
            tests.blackbox2 = {}
            tests.blackbox2 = tests.blackbox

# Generated at 2022-06-14 06:05:21.842819
# Unit test for method __getattribute__ of class ScopeReplacer
def test_ScopeReplacer___getattribute__():
    """Unit test for method __getattribute__ of class ScopeReplacer"""
    import bzrlib.tests.blackbox as tests

    # XXX: Skip the tests when we are running the selftest command.
    if tests.blackbox_selftest:
        return

    def _factory(self, scope, name):
        return 'baz'

    scope = {}
    _ = ScopeReplacer(scope, _factory, 'foo')
    # Check the object 'foo' resolves correctly
    try:
        assert isinstance(scope['foo'], ScopeReplacer)
        assert scope['foo']._resolve() == 'baz'
    # Ensure we can't assign the ScopeReplacer to other variable names
    except IllegalUseOfScopeReplacer:
        pass

# Generated at 2022-06-14 06:05:33.126965
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """Unit test for method __unicode__ of class IllegalUseOfScopeReplacer"""
    import sys
    # _get_format_string and _fmt
    exc = IllegalUseOfScopeReplacer("...", "...")
    exc2 = IllegalUseOfScopeReplacer("...", "...")
    exc2._fmt = exc._fmt
    if not exc == exc2:
        raise AssertionError("equality failed")
    exc3 = IllegalUseOfScopeReplacer("...", "...")
    exc3._fmt = "not the same"
    if exc == exc3:
        raise AssertionError("inequality failed")
    # __str__
    f = sys.exc_info()[2] # current frame

# Generated at 2022-06-14 06:05:45.785847
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """IllegalUseOfScopeReplacer.__str__ should get the right result"""
    e = IllegalUseOfScopeReplacer('foo', 'bar', 'baz')
    assert e._format() == "ScopeReplacer object 'foo' was used incorrectly: bar: baz"
    assert str(e) == "ScopeReplacer object 'foo' was used incorrectly: bar: baz"
    assert repr(e) == "IllegalUseOfScopeReplacer('ScopeReplacer object 'foo' was used incorrectly: bar: baz')"



# Generated at 2022-06-14 06:05:52.934107
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    _skip_if_py3k_warnings_filtered()
    # simple use, just confirm it works
    f = lambda : 'result'
    l = ScopeReplacer(locals(), lambda obj, scope, name: f, 'f')
    eq = object.__getattribute__(l, '__eq__')
    assert eq(l, f)
    assert f() == 'result'

# Generated at 2022-06-14 06:05:59.908670
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    u = IllegalUseOfScopeReplacer('name', 'message', {'key': 'value'})
    import six
    if six.PY2:
        assert isinstance(u.__unicode__(), unicode)
    else:
        assert isinstance(u.__unicode__(), str)
    s = u.__unicode__()
    assert s.endswith('dict={\'extra\': \': {\'key\': \'value\'}\', \'name\': \'name\', \'msg\': \'message\'}')


# Generated at 2022-06-14 06:06:11.274505
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    from bzrlib import (
        lazy_import,
        )
    lazy_import(globals(), '''
from bzrlib import tests
''')
    replacer1 = ScopeReplacer('scope', 'factory', 'name')
    replacer2 = ScopeReplacer('scope', 'factory', 'name')
    replacer = replacer1
    # Note that this assertion can fail if the scope contains a real
    # object before calling replace_lazy_object.
    tests.TestCase.assertEqual(replacer1, replacer)

    replacer = ScopeReplacer('scope', 'factory', 'name')

    # Note that this assertion can fail if the scope contains a real
    # object before calling replace_lazy_object.
    tests.TestCase.assertEqual(replacer1, replacer)

    #

# Generated at 2022-06-14 06:06:23.144845
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    from bzrlib.tests import TestCase
    from bzrlib.tests.lazy_import_helper import make_a_module
    from bzrlib.lazy_import import ScopeReplacer, lazy_import
    from bzrlib import (
        errors,
        osutils,
        branch,
        )


    class LazyImportTestCase(TestCase):
        def setUp(self):
            super(LazyImportTestCase, self).setUp()
            self.globals = dict(globals())
            self.module_name = make_a_module()

        def tearDown(self):
            # Make sure we restore the globals
            globals().clear()
            globals().update(self.globals)



# Generated at 2022-06-14 06:06:30.766838
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    from cStringIO import StringIO
    from bzrlib.lazy_import import IllegalUseOfScopeReplacer
    # test unicode() output
    save_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        ex = IllegalUseOfScopeReplacer('foo', 'msg')
        ex._fmt = '%(name)r %(msg)s'
        try:
            unicode(ex)
        except UnicodeError:
            raise TestSkipped('babel is not present')
    finally:
        sys.stdout = save_stdout


# Generated at 2022-06-14 06:06:43.400050
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """Unit test for method IllegalUseOfScopeReplacer.__unicode__

    This method is used in the traceback module (for instance) to
    display an error message.
    """
    e = IllegalUseOfScopeReplacer(
        'myname',
        'mymsg',
        'myextra')
    expected = u'myname: mymsg: myextra'
    if unicode(e) != expected:
        raise AssertionError('%r != %r' % (unicode(e), expected))
    # now with a preformatted string
    e._preformatted_string = u'mypreformatted'
    if unicode(e) != u'mypreformatted':
        raise AssertionError('%r != %r' % (unicode(e), expected))
    # now with a 8 bit string
    e

# Generated at 2022-06-14 06:06:49.674673
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__() should return str to unicode conversion."""
    illegal_use_exception = IllegalUseOfScopeReplacer('foo', 'bar')
    unicode_string = unicode(illegal_use_exception)
    # IllegalUseOfScopeReplacer should return a unicode object.
    assert isinstance(unicode_string, unicode)
    # Verify unicode conversion.
    assert unicode_string == "ScopeReplacer object 'foo' was used incorrectly: bar"
    # Verify that another unicode conversion does not fail with an UnicodeDecodeError.
    assert unicode(unicode_string) == unicode_string


# Generated at 2022-06-14 06:06:58.819562
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """IllegalUseOfScopeReplacer.__unicode__() should return a unicode string"""
    # Calling __unicode__() must return a unicode object.
    e = IllegalUseOfScopeReplacer('name', 'msg', 'extra')
    u = unicode(e)
    # Note that in Python 2.6, str and unicode are the same type.
    if type(str('str')) is not type(unicode('unicode')):
        assert type(u) is unicode



# Generated at 2022-06-14 06:07:03.274129
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """__str__ should return a str object (not bytestring)"""
    e = IllegalUseOfScopeReplacer('name', 'message')
    x = str(e)
    assert isinstance(x, str)
    assert not isinstance(x, unicode)


# Generated at 2022-06-14 06:07:11.996596
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    # FIXME: RBC 20060127 no test exists, but code coverage is 100%
    pass

# Generated at 2022-06-14 06:07:19.571769
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    if na:
        eq = ne = undefined
    raise TestSkipped('Test disabled because it is broken.')
    return
    import bzrlib.tests
    x = ScopeReplacer(bzrlib.tests.__dict__, undefined, undefined)
    return



# Generated at 2022-06-14 06:07:28.400296
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    # Method __call__ of ScopeReplacer can be called.
    class MyClass(object):
        def __call__(self):
            return self
    my_class = MyClass()
    my_scope = {}
    my_factory = lambda s, sc, n: my_class
    my_name = "my_name"
    sr = ScopeReplacer(my_scope, my_factory, my_name)
    sr()

# Generated at 2022-06-14 06:07:32.062487
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """Unit test for method __unicode__ of class IllegalUseOfScopeReplacer"""
    # The method is tested in the module test_lazy_import.py
    pass



# Generated at 2022-06-14 06:07:39.682934
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__ -> unicode object"""
    exc = IllegalUseOfScopeReplacer('name', 'msg', 'extra')
    s = exc.__unicode__()
    assert isinstance(s, unicode), "not a unicode object: %r" % (s,)
    # check result
    assert s == u"ScopeReplacer object 'name' was used incorrectly: msg: extra"
    # more test with format string in unicode
    exc._fmt = u"%(name)s => %(msg)s"
    s = exc.__unicode__()
    assert isinstance(s, unicode), "not a unicode object: %r" % (s,)
    # check result
    assert s == u"name => msg"


# Generated at 2022-06-14 06:07:52.925799
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    import __builtin__
    __builtin__.__dict__['_s'] = None
    def f(scope, name):
        def _f():
            return 'my_scope'
        return _f
    def g(self, scope, name):
        global _s
        _s = self
        return self
    sr = ScopeReplacer(__builtin__.__dict__, g, 'sr')
    assert __builtin__.__dict__['_s'] is sr
    # __builtin__.__dict__['sr'] == sr
    assert __builtin__.__dict__['_s']() == 'my_scope'
    # __builtin__.__dict__['sr']() == 'my_scope'
    del __builtin__.__dict__['_s']

# Generated at 2022-06-14 06:08:07.323105
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    from bzrlib.tests import TestCase
    from bzrlib.tests.features import UnicodeFilenameFeature

    class UnicodeFilenameTest(TestCase):

        _test_needs_features = [UnicodeFilenameFeature]

        def test_IllegalUseOfScopeReplacer___str__(self):
            """__str__ of IllegalUseOfScopeReplacer must return an ascii str.

            It should not fallback to the 'ascii' encoding, because it doesn't
            know anything about the locale of the user.
            """
            e = IllegalUseOfScopeReplacer('x', "excuse me", extra="extra")
            # Make the encoding of the error message different from
            # the default encoding (which is used for non-unicode strings).
            self.overrideEnv('LANG', 'fr_FR.UTF-8')
           

# Generated at 2022-06-14 06:08:11.227916
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """This test checks that __unicode__ returns unicodes and not strs"""
    e = IllegalUseOfScopeReplacer('name', 'msg')
    u = unicode(e)
    assert isinstance(u, unicode)
    assert u == u'name: msg'

# Generated at 2022-06-14 06:08:25.178538
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    sl = ScopeReplacer(globals(), lambda x, y, z: x, 'sl')
    def testfunc(x):
        return x
    sl.testfunc = testfunc
    assert sl(1) == 1
    assert sl(1, 2, 3) == 1, sl(1, 2, 3)
    assert sl(1, 2, z=3) == 1, sl(1, 2, z=3)
    assert sl('abc') == 'abc', repr(sl('abc'))

    def testkw(x, y=2):
        return x, y
    sl.testkw = testkw
    assert sl(1) == 1, sl(1)
    assert sl(1, 2, 3) == 1, sl(1, 2, 3)
    assert sl(1, 2, z=3) == 1, sl

# Generated at 2022-06-14 06:08:39.315849
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """IllegalUseOfScopeReplacer.__unicode__() should return unicode

    Note: This is a unit test for the method
    IllegalUseOfScopeReplacer.__unicode__(). It is here rather than in
    test_errors.py because it needs to import this module to construct
    the object under test.
    """
    from . import lazy_import
    import sys
    import types
    if sys.version_info[0] == 2:
        # Make sure the method returns unicode
        _myunicode = unicode
    else:
        # make sure the method returns str
        _myunicode = str

    test_one = IllegalUseOfScopeReplacer('abc', 'ex1')
    test_one.extra = 'ex2'

    # test 'ascii' format string

# Generated at 2022-06-14 06:08:57.986546
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    import bzrlib.tests
    bounds = bzrlib.tests.TestCaseWithMemoryTransport.make_bounds
    import bzrlib
    bounds('bzrlib')
    import bzrlib.tests
    import bzrlib.lazy_import
    bounds('bzrlib.lazy_import')
    import bzrlib.tests.TestCaseWithMemoryTransport
    bounds('bzrlib.tests.TestCaseWithMemoryTransport')
    import bzrlib.tests.per_workingtree as per_workingtree
    bounds('bzrlib.tests.per_workingtree')
    import bzrlib
    bounds('bzrlib')
    import bzrlib.tests
    bounds('bzrlib.tests')
    import bzrlib.lazy_import


# Generated at 2022-06-14 06:09:11.302771
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__ must return a unicode object"""
    # we have to override it to call the non-unicode version and check
    # the type of the result.
    class TestIllegalUseOfScopeReplacer(IllegalUseOfScopeReplacer):
        def __unicode__(self):
            u = IllegalUseOfScopeReplacer.__str__(self)
            assert isinstance(u, unicode), type(u)
            # and for good measure, check we can actually convert it
            uni = unicode(u)
            assert isinstance(uni, unicode)
            return u

# Generated at 2022-06-14 06:09:14.822777
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """IllegalUseOfScopeReplacer.__unicode__() is tested by test_string_conversions()."""
    raise ExceptionNotImplemented()

# Generated at 2022-06-14 06:09:27.777059
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """__str__() of IllegalUseOfScopeReplacer"""
    # Test that the message is encoded in utf8
    import __builtin__
    # Build the message in unicode
    msg = u'\u00e9'
    e = IllegalUseOfScopeReplacer('name', msg)
    s = str(e)
    assert isinstance(s, str)
    assert isinstance(s, __builtin__.str)
    # Test that the exception is decoded in unicode
    assert isinstance(e, unicode)
    assert isinstance(e, __builtin__.unicode)
    assert e == s, '%r should be equal to %r' % (e, s)
    # Test that __str__() returns the same string, no matter if the message is
    # a str or unicode.

# Generated at 2022-06-14 06:09:33.182064
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """IllegalUseOfScopeReplacer.__unicode__() works"""
    try:
        raise IllegalUseOfScopeReplacer('foo', 'bar', 'baz')
    except IllegalUseOfScopeReplacer as e:
        u = unicode(e) # runs __unicode__()
    assert isinstance(u, unicode), "__unicode__ did not return unicode"

