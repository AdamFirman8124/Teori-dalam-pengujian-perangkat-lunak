

# Generated at 2022-06-14 06:00:06.474893
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    obj = ScopeReplacer({}, lambda s, sc, n: n, 'test')
    try:
        result = obj()
    except:
        raise AssertionError("__call__ raised an exception")
    assert result == 'test', (result, 'test')
test_ScopeReplacer___call__()

# Generated at 2022-06-14 06:00:20.012874
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    from bzrlib import lazy_import
    import sys
    lazy_import(sys.modules[__name__],
        '''
        from bzrlib import tests
        '''.split(),
        globals())
    from bzrlib import tests
    # Call of __call__ of class ScopeReplacer with parameter args=() and parameter kwargs={}
    # No exception should be thrown
    assert tests.selftest_suite() is not None

    # Call of __call__ of class ScopeReplacer with parameter args=() and parameter kwargs={}
    # No exception should be thrown
    assert tests.selftest_suite() is not None

    # Call of __call__ of class ScopeReplacer with parameter args=() and parameter kwargs={}
    # No exception should be thrown
    assert tests.selftest_

# Generated at 2022-06-14 06:00:24.450064
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    assert ScopeReplacer.__call__.im_func is object.__call__.im_func
try:
    from bzrlib._lazy_imports import builtin
except ImportError:
    builtin = None
builtin = ScopeReplacer(locals(), lambda r,s,n: builtin or __import__('builtins'), 'builtin')



# Generated at 2022-06-14 06:00:34.114193
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    import sys
    import __builtin__
    global_vars = __builtin__.__dict__
    sr = ScopeReplacer(dict(global_vars), lambda sr, scope, name: 0, "foo")

# Generated at 2022-06-14 06:00:43.251445
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    from bzrlib.tests import TestCase
    class DummyClass(object):
        def dummy_method(self, *args, **kwargs):
            self.called = (args, kwargs)
            return (args, kwargs)
    def dummy_factory(self, scope, name):
        return DummyClass()
    class ScopeReplacerTestCase(TestCase):
        def setUp(self):
            super(ScopeReplacerTestCase, self).setUp()
            self.scope = locals()
            self.obj = ScopeReplacer(self.scope, dummy_factory, 'obj')
        def test_calling_method(self):
            args = (1, 2, 3)
            kwargs = {'a': 'b'}

# Generated at 2022-06-14 06:00:53.127490
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    from bzrlib import tests as _mod_tests
    def _test_it():
        import sys as __mod_sys
        myvalue = __mod_sys.modules['bzrlib.tests'].myvalue
        myvalue = __mod_sys.modules['bzrlib.tests'].myvalue
        return myvalue
    _mod_tests.myvalue = 'bar'
    # this test is supposed to succeed, but ScopeReplacer._should_proxy should
    # be protected.
    # self.assertRaises(IllegalUseOfScopeReplacer, _test_it)
    __mod_sys = _mod_tests = None



# Generated at 2022-06-14 06:00:59.669677
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """IllegalUseOfScopeReplacer.__unicode__()

    The __unicode__ should return the same as the __str__. This is because
    the __unicode__ should return unicode object and the __str__ should
    return a str object.
    """
    str_obj = 'some unicode string \N{COPYRIGHT SIGN} \N{CENT SIGN}'
    str_unicode = unicode(str_obj)
    try:
        str_unicode.decode('ascii')
    except UnicodeDecodeError:
        have_non_ascii_characters = True
    else:
        have_non_ascii_characters = False
    e = IllegalUseOfScopeReplacer('name', 'msg',
                                  extra=str_unicode)

# Generated at 2022-06-14 06:01:05.984063
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """IllegalUseOfScopeReplacer.__unicode__() returns a unicode object."""
    e = IllegalUseOfScopeReplacer('foo', 'bar')
    u = unicode(e)
    if isinstance(u, str):
        raise TypeError('Expected unicode object, got byte string')
    else:
        # Test passed.
        pass



# Generated at 2022-06-14 06:01:07.883239
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    """__setattr__ should replace the object when accessed"""



# Generated at 2022-06-14 06:01:18.386473
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    import sys
    class A(object):
        def __init__(self):
            self.i = 1
            self.j = 2
        def f(self, a, b=1, c=2):
            return (a, b, c)
    old_real_obj = A()
    o = ScopeReplacer(sys.modules, lambda self, scope, name: old_real_obj, 'A')
    assert (1, 2) == o(1)
    assert (1, 1, 2) == o(1, b=1)
    assert (1, 1, 2) == o.f(1, b=1)
    assert (1, 1, 2) == o.f(1, c=2)
    assert (1, 1, 2) == o.f(1, b=1, c=2)




# Generated at 2022-06-14 06:01:32.611084
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """IllegalUseOfScopeReplacer.__str__() should not crash"""
    def method(self):
        return 'dummy scope replacer'
    scope_replacer = type('ScopeReplacer', (object,), dict(
        __str__=method))()
    try:
        scope_replacer()
    except IllegalUseOfScopeReplacer:
        pass



# Generated at 2022-06-14 06:01:39.565575
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    from bzrlib.tests import TestCase
    from bzrlib.lazy_import import (
        ScopeReplacer,
        )
    
    class TestScopeReplacer___call__(TestCase):
        
        def test__call(self):
            context = {}
            name = 'name'
            def factory(self2, scope, name2):
                return lambda a: a*2
            scope_replacer = ScopeReplacer(context, factory, name)
            self.assertEqual('abab', scope_replacer('ab'))
    
    TestCase.run_suite(__name__)



# Generated at 2022-06-14 06:01:51.707530
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    from bzrlib.tests import TestCase
    import types
    class TestClass(object):
        pass
    class TestCall(object):
        def __call__(self, *args, **kwargs):
            return (args, kwargs)
        def __getattr__(self, attr):
            return attr
    test_cases = (
        # (obj, args, kwargs, expected_result)
        (TestClass, (1,2), {'abc':3}, (1,2)),
        (TestCall(), (1,2), {'abc':3}, ((1,2), {'abc':3})),
        )
    for obj, args, kwargs, expected_result in test_cases:
        scope = {}
        scope_name = obj.__class__.__name__
        scope_repl

# Generated at 2022-06-14 06:02:00.742079
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """IllegalUseOfScopeReplacer.__str__ should return a str object."""
    from bzrlib.lazy_import import IllegalUseOfScopeReplacer
    msg = 'This is a message'
    extra = 'This is extra text'
    exception = IllegalUseOfScopeReplacer('foo', msg, extra)
    s = str(exception)
    assert isinstance(s, str)
    assert unicode(s) == unicode(exception)
    assert s.startswith('IllegalUseOfScopeReplacer(')
    assert 'foo' in s
    assert msg in s
    assert extra in s
    assert s.endswith(')')

# Generated at 2022-06-14 06:02:03.495865
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__ of IllegalUseOfScopeReplacer returns a unicode object."""
    e = IllegalUseOfScopeReplacer('name', 'msg', 'extra')
    u = unicode(e)
    assert isinstance(u, unicode)



# Generated at 2022-06-14 06:02:16.422255
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    from bzrlib.lazy_import import lazy_import
    lazy_import(globals(), '''
    from bzrlib import (
        errors
        )
    ''', force=True)
    class MyObject(object):
        def __call__(self, *args, **kwargs):
            return ('called', args, kwargs)
    scope = {}
    factory = lambda self, scope, name: MyObject()
    scopeReplacer = ScopeReplacer(scope, factory, 'target')
    # Call of: scopeReplacer(a, b, c=None)
    expected = ('called', (1, 2), {'c':None})
    actual = scopeReplacer(1, 2, c=None)

# Generated at 2022-06-14 06:02:27.197763
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    class SomeClass(object):
        def __call__(self, *args, **kwargs):
            return args, kwargs
    class SomeOtherClass(object):
        pass

    class MiscTests(object):
        def test_function_call(self):
            # check that we can call ScopeReplacer instances that wrap
            # callable objects
            a = SomeClass()
            b = ScopeReplacer(MiscTests.__dict__, lambda self, scope, name: a,
                'a')
            self.assertEqual(((), {}), b())
            self.assertEqual(((1,), {}), b(1))
            self.assertEqual(((1, 2), {}), b(1, 2))
            self.assertEqual(((), {'one': 1}), b(one=1))

# Generated at 2022-06-14 06:02:37.957879
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    from bzrlib.lazy_import import lazy_import, lazy_import_submodules
    def my_method(*args, **kwargs):
        assert args == (43, )
        assert kwargs == {'x': 44}
        return

    lazy_import(globals(), '''
    import bzrlib.timestamp
    ''')
    bzrlib.timestamp.my_method = my_method
    # FIXME: RBC 20060131 What is the purpose of this test?
    # The code being tested is not called: 'bzrlib.timestamp.my_method' will
    # already have been created.
    bzrlib.timestamp.my_method(43, x=44)



# Generated at 2022-06-14 06:02:45.870811
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """IllegalUseOfScopeReplacer.__unicode__()

    Tries to reproduce a bug in Python 2.3.
    """
    e = IllegalUseOfScopeReplacer('foo', "message")
    assert isinstance(unicode(e), unicode)
    assert unicode(e) == 'message', unicode(e)
test_IllegalUseOfScopeReplacer___unicode__.unittest = ['errors']



# Generated at 2022-06-14 06:02:55.501681
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """Test method __str__ of class IllegalUseOfScopeReplacer"""
    import sys
    if sys.getdefaultencoding() != 'ascii':
        # This test can only be run if the default encoding is 'ascii',
        # because the exception message contains non-ascii characters.
        # This test should be run before the default encoding is changed by
        # bzrlib.i18n.install_gettext_translations
        return
    e = IllegalUseOfScopeReplacer('foo', 'some error')
    s = e.__str__()
    # The message must be a str object, not a unicode object
    assert isinstance(s, str)
    # The message must not contain non-ascii characters
    assert '\xb5' not in s
    assert '\xa3' not in s



# Generated at 2022-06-14 06:03:11.026565
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    class foo:
        pass
    
    obj = foo()
    
    x = ScopeReplacer(globals(), lambda *args, **kw: obj, 'obj')
    assert x('hello') is obj
    assert x('hello', x='world') is obj
    assert x() is obj
test_ScopeReplacer___call__.unittest = ['.lazy_import']



# Generated at 2022-06-14 06:03:22.794046
# Unit test for method __getattribute__ of class ScopeReplacer
def test_ScopeReplacer___getattribute__():
    import os
    import sys
    import unittest

    class TestScopeReplacer(unittest.TestCase):

        def test_getattribute(self):
            import __main__
            old = __main__.__dict__.get('__builtins__', None)
            try:
                del __main__.__dict__['__builtins__']
                # Can still use globals() after deletion
                globals()
                # but __builtins__ is readonly
                self.assertRaises(TypeError,
                    ScopeReplacer, globals(), lambda *a: 17, '__builtins__')
            finally:
                if old is not None:
                    __main__.__dict__['__builtins__'] = old

    from bzrlib.tests.test_lazy_import import TestCaseWithLazyImport
    test

# Generated at 2022-06-14 06:03:29.679334
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    import bzrlib.tests

    class Dummy:
        def __init__(self, s):
            self.s = s

        def __call__(self, *args, **kwargs):
            return (self.s, args, kwargs)

    d = Dummy('test')
    sd = ScopeReplacer({}, lambda self, scope, name: d, name='d')
    bzrlib.tests.TestSkipped('Hookup test')


# Generated at 2022-06-14 06:03:42.592764
# Unit test for method __getattribute__ of class ScopeReplacer
def test_ScopeReplacer___getattribute__():
    class Mock:
        def __init__(self, attr):
            self.attr = attr
        def __getattribute__(self, attr):
            return object.__getattribute__(self, attr)

    # None
    class Test1(Mock, ScopeReplacer):
        def _resolve(self):
            return None
        def __init__(self):
            self.attr = 0

    test1 = Test1()
    test1.attr # None
    test1.attr = "ABC" # should not error out

    # Regular object
    class Test2(Mock, ScopeReplacer):
        def _resolve(self):
            return self
        def __init__(self):
            self.attr = 1

    test2 = Test2()
    test2.attr # 1

# Generated at 2022-06-14 06:03:45.134916
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    from bzrlib.tests import TestSkipped
    raise TestSkipped("no unit test exists for this method")



# Generated at 2022-06-14 06:03:48.829374
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """Test method __str__ of class IllegalUseOfScopeReplacer."""
    e = IllegalUseOfScopeReplacer('name', 'msg', 'extra')
    str(e)



# Generated at 2022-06-14 06:04:01.901188
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    class Foo(object):
        __slots__ = ('_bar',)
        def __getattribute__(self, name):
            if name == '_resolve':
                return object.__getattribute__(self, name)
            if name == 'bar':
                return object.__getattribute__(self, '_bar')
            if name == '__dict__':
                return object.__getattribute__(self, name)
            raise AttributeError('no attribute %r' % name)
        def __setattr__(self, name, value):
            if name == '_bar':
                object.__setattr__(self, name, value)
                return
            if name == '__dict__':
                object.__setattr__(self, name, value)
                return

# Generated at 2022-06-14 06:04:03.192866
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    pass


# Generated at 2022-06-14 06:04:04.289731
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    """__call__(self, *args, **kwargs)"""


# Generated at 2022-06-14 06:04:11.838435
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """test_IllegalUseOfScopeReplacer___str__
    Unit test for method __str__ of class IllegalUseOfScopeReplacer.
    """
    e = IllegalUseOfScopeReplacer('name', 'msg', 'extra')
    str_e = str(e)
    if isinstance(str_e, unicode):
        str_e = str_e.encode('utf8')
    # should start "ScopeReplacer object 'name'"
    # and contain "msg" and "extra"
    assert str_e.startswith("ScopeReplacer object 'name'")
    assert "'msg'" in str_e
    assert "'extra'" in str_e


# Generated at 2022-06-14 06:04:29.216579
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """Unit test for method __str__ of class IllegalUseOfScopeReplacer"""
    # Testcase 1.
    exc = IllegalUseOfScopeReplacer(
        'foo', 'bar', 'baz')
    assert str(exc) == ('foo: bar: %s: baz'
                        % _('IllegalUseOfScopeReplacer.__init__'))
    assert repr(exc) == 'IllegalUseOfScopeReplacer(%r)' % str(exc)


# Generated at 2022-06-14 06:04:35.701360
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """Unit test for method __unicode__ of class IllegalUseOfScopeReplacer"""
    import sys
    if sys.getdefaultencoding() in ('ascii', 'ANSI_X3.4-1968'):
        raise TestSkipped('%r is ASCII, but that may fail this test'
                          % sys.getdefaultencoding())
    err = IllegalUseOfScopeReplacer('foo', 'an error')
    err.test_attr = 'test_attr'
    check_string = (u'ScopeReplacer object \'foo\' was used incorrectly:'
                    u' an error')
    # This is simply a hack to get around the fact that the test harness
    # depends on __str__ being available when setting up the test suite.
    # The 'bytes' object should be of type 'unicode'
    ui = err.__unicode__

# Generated at 2022-06-14 06:04:40.328819
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """__str__ should return a str object"""
    import six
    s = IllegalUseOfScopeReplacer('name', 'msg').__str__()
    assert isinstance(s, str)
    assert not isinstance(s, six.text_type)



# Generated at 2022-06-14 06:04:51.693975
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    from bzrlib.lazy_import import lazy_import
    from bzrlib.lazy_import import ScopeReplacer
    scope = {}
    lazy_import(scope, 'import bzrlib.revision as _mod_revision')
    _obj_revision = scope['_mod_revision']
    _obj_revision('a', 'b')
    _obj_revision.Revision('a', 'b')
    _obj_revision.Revision.NULL_REVISION('a', 'b')
    _obj_revision.Revision.NULL_REVISION.timestamp('a', 'b')

# Generated at 2022-06-14 06:05:03.966123
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    try:
        x = IllegalUseOfScopeReplacer('hello', 'there')
        raise AssertionError('should have raised')
    except IllegalUseOfScopeReplacer as e:
        # 'e' is an instance of IllegalUseOfScopeReplacer
        e_repr = repr(e)
        u = unicode(e)
        u_repr = repr(u)
        assert isinstance(u, unicode)

# Generated at 2022-06-14 06:05:07.991757
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    foo = ScopeReplacer(globals(), lambda *args: object(), 'foo')
    bar = ScopeReplacer(globals(), lambda *args: object(), 'bar')
    foo.a = bar
    return foo.a == bar

# Generated at 2022-06-14 06:05:21.784224
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    class FakeBzrDir(object):
        """A fake bzrdir to use in tests"""

    class FakeBzrDirFormat(object):
        """A fake bzrdir format to use in tests"""

        def __init__(self):
            """Constructor"""
            self.__bzrdirs = []

        @property
        def bzrdirs(self):
            """Return the bzrdirs that have been constructed"""
            return self.__bzrdirs

        def open(self, transport):
            """Open the bzrdir"""
            self.__bzrdirs.append(FakeBzrDir())
            return self.__bzrdirs[-1]

    scope = {}

# Generated at 2022-06-14 06:05:29.144151
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    # works for None extra
    e = IllegalUseOfScopeReplacer('foo', 'bar')
    u = unicode(e)
    assert isinstance(u, unicode)
    assert u == 'ScopeReplacer object \'foo\' was used incorrectly: bar'
    # works for non-None extra
    e = IllegalUseOfScopeReplacer('foo', 'bar', 'baz')
    u = unicode(e)
    assert isinstance(u, unicode)
    assert u == 'ScopeReplacer object \'foo\' was used incorrectly: bar: baz'
    # works if str(extra) is non-ascii
    e = IllegalUseOfScopeReplacer('foo', 'bar', u'\u03b1')
    u = unicode(e)
    assert isinstance(u, unicode)

# Generated at 2022-06-14 06:05:34.778400
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    # The __unicode__ method is not normally touched.
    # Testing it would require stubbing out a gettext implementation.
    # Instead we check that it returns a unicode object,
    # which is what is required.
    e = IllegalUseOfScopeReplacer("name", "msg")
    u = e.__unicode__()
    if not isinstance(u, unicode):
        raise AssertionError("__unicode__ did not return a unicode object.")



# Generated at 2022-06-14 06:05:44.250746
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """Method __str__ of class IllegalUseOfScopeReplacer produces a string
    representation of the exception."""
    from bzrlib.tests import TestCase

    class Checker(TestCase):

        def check(self, e):
            self.assertEqual(
                '%s(%s)'
                % (IllegalUseOfScopeReplacer.__name__, e.__str__()),
                '%s' % e)


# Generated at 2022-06-14 06:06:04.808745
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """IllegalUseOfScopeReplacer.__unicode__()

    __unicode__() must return unicode object
    """
    exc = IllegalUseOfScopeReplacer('foo', 'bar')
    assert isinstance(unicode(exc), unicode)
    assert unicode(exc) == u'bar'



# Generated at 2022-06-14 06:06:18.317429
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__ of IllegalUseOfScopeReplacer"""
    import re
    test_cases = [
        (IllegalUseOfScopeReplacer("name", "msg", "extra"),
         u"ScopeReplacer object 'name' was used incorrectly: msg: extra"),
        (IllegalUseOfScopeReplacer("name", "msg", None),
         u"ScopeReplacer object 'name' was used incorrectly: msg"),
        (IllegalUseOfScopeReplacer("name", "msg", 1),
         u"ScopeReplacer object 'name' was used incorrectly: msg: 1"),
        (IllegalUseOfScopeReplacer("name", "1 \u01fb 2", "extra"),
         u"ScopeReplacer object 'name' was used incorrectly: 1 \u01fb 2: extra"),
        ]

# Generated at 2022-06-14 06:06:26.017837
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """Method __str__ of class IllegalUseOfScopeReplacer"""
    inst1 = IllegalUseOfScopeReplacer("foo", "bar")
    inst2 = IllegalUseOfScopeReplacer("foo", "bar")
    assert inst1 == inst2
    # We use repr() to account for repr() differences on unicode strings
    # between Python 2 and Python 3.
    assert repr(inst1) == repr(inst2)



# Generated at 2022-06-14 06:06:34.220256
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    # This test is a bit of a kludge, but without it the unit test for
    # lazy_import.py fails. There is probably a better way to do this.
    import bzrlib.lazy_import
    orig_method = bzrlib.lazy_import.ScopeReplacer.__setattr__
    def method_test(test_case, method, *args, **kwargs):
        # This is NOT a method of this class, so is not called with
        # 'self' as the first argument.
        method(test_case, *args, **kwargs)
    def test_method(test_case):
        def factory(replacer, scope, name):
            return 'foo'
        ScopeReplacer(scope, factory, name)

# Generated at 2022-06-14 06:06:39.590265
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    """__call__ should call the real object"""
    def factory(self, scope, name):
        def meth(*args, **kwargs):
            return (args, kwargs)
        return meth
    scope = {}
    scope_replacer = ScopeReplacer(scope, factory, 'obj')
    args = (1, 2)
    kwargs = {'kwargs': 'kwargs'}
    ret = scope_replacer(*args, **kwargs)
    assert (ret == (args, kwargs))
    assert (scope['obj'] == scope_replacer)
    assert (scope['obj']._real_obj == ret)

# Generated at 2022-06-14 06:06:45.221799
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__ should return unicode"""
    try:
        from bzrlib.tests import TestCase
    except ImportError:
        from unittest import TestCase
    try:
        err = IllegalUseOfScopeReplacer('name', 'message', 'extra')
        err.__unicode__()
    except UnicodeDecodeError:
        raise AssertionError("IllegalUseOfScopeReplacer.__unicode__ did not"
                             " return a unicode object")



# Generated at 2022-06-14 06:06:50.852591
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    obj = ScopeReplacer(None, None, 'scopereplacer')
    # Set obj.foo to 1
    obj.foo = 1
    # Check if obj.foo == 1
    if obj.foo != 1:
        raise AssertionError('obj.foo != 1')


# Generated at 2022-06-14 06:07:03.906737
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """IllegalUseOfScopeReplacer.__unicode__() is idempotent"""
    import bzrlib.tests.blackbox
    e = IllegalUseOfScopeReplacer('a', 'b', 'c')
    # make sure that e.__unicode__() returns a unicode object
    for i in range(5):
        s = e.__unicode__()
        # We can't compare the output to a known value because it depends on the
        # default encoding. Make sure it is at least a unicode object with a
        # non-zero length and looks like the original string.
        bzrlib.tests.blackbox.TestCase.assertIsInstance(s, unicode)
        bzrlib.tests.blackbox.TestCase.assertNotEqual(len(s), 0)

# Generated at 2022-06-14 06:07:12.524719
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    from bzrlib import (
        lazy_import,
        )
    from bzrlib.tests import (
        TestCase,
        )

    def make_scope_replacer(name):
        def factory(replacer, scope, name):
            scope[name] = scope[name] + 1
            return scope[name]
        scope = {name:0}
        lazy_import.ScopeReplacer(scope, factory, name)
        return scope

    class TestScopeReplacer(TestCase):

        def test___setattr__(self):
            scope = make_scope_replacer('scope')
            scope['scope'] = 100
            self.assertEqual(scope['scope'], 100)

    from bzrlib.tests import test_suite
    return test_suite()

# Generated at 2022-06-14 06:07:19.571965
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    from mock import Mock
    scope = {}
    scope_a = scope
    scope_b = {}
    def factory(orig_obj, scope, name):
        assert scope is scope_b
        assert name == 'name_b'
        return object()
    obj = ScopeReplacer(scope, factory, 'name')
    setattr(obj, 'a', 'b')
    try:
        setattr(obj, 'a', 'b')
        raise AssertionError("setattr happened twice on scope replacer")
    except IllegalUseOfScopeReplacer as e:
        assert str(e) == "ScopeReplacer object 'name' was used incorrectly:" \
            " Object already replaced, did you assign it to another variable?"



# Generated at 2022-06-14 06:07:46.338305
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__() should return a unicode object"""
    a = IllegalUseOfScopeReplacer(name='foo', msg='bar')
    u = unicode(a)
    assert isinstance(u, unicode)


# Generated at 2022-06-14 06:07:56.580793
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """IllegalUseOfScopeReplacer.__str__()

    [It] must return a str.
    """
    class UnicodeObj(unicode):
        pass
    class NonUnicodeObj(object):
        def __str__(self):
            return self
    obj = UnicodeObj(u'foo')
    obj2 = NonUnicodeObj()
    obj3 = 'foo'
    def test_str(obj):
        try:
            str(obj)
        except UnicodeEncodeError:
            pass
        else:
            raise AssertionError('IllegalUseOfScopeReplacer.__str__() must return a str, not a unicode object')
    test_str(IllegalUseOfScopeReplacer('name', 'msg', obj))

# Generated at 2022-06-14 06:08:07.988945
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    from bzrlib.tests import TestCase
    scope = {}
    class TestClass(object):
        foo = 'bar'
        def __call__(self, a, b):
            return a, b
    def factory(replacer, scope, name):
        return TestClass()
    sr = ScopeReplacer(scope, factory, 'testobj')
    self.assertEqual(('a', 'b'), sr('a', 'b'))

    # Using __call__ directly on self._resolve should work
    # This failed in the past, see bug #334815
    self.assertEqual(('a', 'b'), scope['testobj']._resolve()('a', 'b'))



# Generated at 2022-06-14 06:08:19.976764
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """Method __unicode__ of class IllegalUseOfScopeReplacer

    Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
    """
    import sys
    sys.stdout.write('\n')
    exc = IllegalUseOfScopeReplacer(
        'scope', 'foo', extra='extra')
    if isinstance(exc, Exception):
        result = unicode(exc)
        reference = u'ScopeReplacer object \'scope\' was used incorrectly:' \
            u' foo: extra'
        sys.stdout.write('\n')
        if reference == result:
            sys.stdout.write('ok\n')
        else:
            sys.stdout.write('not ok\n')
        sys.stdout.write('\n')
    else:
        sys.stdout.write('\n')


# Generated at 2022-06-14 06:08:22.744251
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__ should return a unicode string."""
    "XXX TODO"



# Generated at 2022-06-14 06:08:26.283592
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__ must return a unicode object.

    This is tested using cmp().
    """
    e = IllegalUseOfScopeReplacer("name", "msg")
    cmp(u'IllegalUseOfScopeReplacer("name", "msg")', unicode(e))



# Generated at 2022-06-14 06:08:40.017705
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__() of IllegalUseOfScopeReplacer"""
    import sys
    # by default, raise an AttributeError
    e = IllegalUseOfScopeReplacer('__unicode__', '__unicode__')
    try:
        unicode(e)
    except AttributeError:
        pass
    else:
        # On Python 3, the str() function returns unicode, so the
        # AttributeError is not propagated.
        if sys.version_info < (3, 0):
            raise AssertionError()
    # with a format string, it should work
    def _get_format_string_fake(self):
        return "abc"
    e._get_format_string = _get_format_string_fake
    assert unicode(e) == u"abc"
    e._message = u"abc"

# Generated at 2022-06-14 06:08:41.475755
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    """__call__(self, *args, **kwargs)"""


# Generated at 2022-06-14 06:08:45.000373
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """Unit test for method __unicode__ of class IllegalUseOfScopeReplacer"""
    e = IllegalUseOfScopeReplacer('test', 'testing')
    assert unicode(e) == 'testing'
    assert e._get_format_string() == 'testing'

# Generated at 2022-06-14 06:08:53.042104
# Unit test for method __getattribute__ of class ScopeReplacer
def test_ScopeReplacer___getattribute__():
    import inspect

    class Object():
        def __init__(self, name):
            self.name = name

        def method1(self):
            return self.name

        def __repr__(self):
            return 'Object(%r)' % self.name

    class FakeScope():
        def __init__(self):
            self.obj = None

        def __setitem__(self, key, value):
            self.obj = value

        def __getitem__(self, key):
            return self.obj

    def _scope_replacer_factory(scope_replacer, scope, key):
        fake_obj = Object(key)
        # ScopeReplacer should proxy to obj, so this will return the 1st
        # argument.
        return lambda x: x

    name = 'object_name'
    scope = Fake

# Generated at 2022-06-14 06:09:14.991733
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__ works according to the documentation in IllegalUseOfScopeReplacer"""
    # __unicode__ must return a unicode object.

    # Try a str.
    exc = IllegalUseOfScopeReplacer('name', 'message')
    u = unicode(exc)
    # It should be a unicode object now.
    assert(isinstance(u, unicode))
    # It should contain the message.
    assert('message' in str(u))

    # Try a unicode.
    exc = IllegalUseOfScopeReplacer('name', u'message')
    u = unicode(exc)
    # It should be a unicode object.
    assert(isinstance(u, unicode))
    # It should contain the message.
    assert('message' in str(u))

    # Try a tuple of str and unicode.


# Generated at 2022-06-14 06:09:28.014131
# Unit test for method __str__ of class IllegalUseOfScopeReplacer

# Generated at 2022-06-14 06:09:32.718501
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """IllegalUseOfScopeReplacer.__unicode__"""

    f = IllegalUseOfScopeReplacer('name', 'msg', extra='extra')
    # ensure that __str__ uses the same string as __unicode__
    assert f.__unicode__() == f.__str__()

