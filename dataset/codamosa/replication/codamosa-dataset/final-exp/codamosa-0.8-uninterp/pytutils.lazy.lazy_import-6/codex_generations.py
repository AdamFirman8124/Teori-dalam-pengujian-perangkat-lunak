

# Generated at 2022-06-14 06:00:16.046330
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    # Called with no arg, 0 args.
    obj = ScopeReplacer({}, lambda x,y,z: x, 'test')
    # Called with 1 arg, 1 args.
    obj(5)
    # Called with 1 arg, 2 args.
    obj(5, 6)
    # Called with 1 arg, 3 args.
    obj(5, 6, 7)
    # Called with 1 arg, 4 args.
    obj(5, 6, 7, 8)



# Generated at 2022-06-14 06:00:23.750608
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    from bzrlib.lazy_import import ScopeReplacer
    from bzrlib.tests import TestCase

    class _CallableObject(TestCase):

        def __init__(self):
            TestCase.__init__(self)

        def __call__(self):
            return '_CallableObject.__call__'

    scope = {}
    def factory():
        return _CallableObject()

    scope_replacer = ScopeReplacer(scope, factory, 'name')
    self.assertEqual('_CallableObject.__call__', scope_replacer())



# Generated at 2022-06-14 06:00:31.098277
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    import doctest
    doctest.run_docstring_examples(
        IllegalUseOfScopeReplacer._format, {}, verbose=True)
    doctest.run_docstring_examples(
        IllegalUseOfScopeReplacer.__str__, {}, verbose=True)
    doctest.run_docstring_examples(IllegalUseOfScopeReplacer.__unicode__, {},
        verbose=True)



# Generated at 2022-06-14 06:00:37.359065
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """IllegalUseOfScopeReplacer.__unicode__() returns expected value."""
    e = IllegalUseOfScopeReplacer('name', 'msg', 'extra')
    s = unicode(e)
    if not isinstance(s, unicode):
        raise AssertionError('__unicode__() should return a unicode object')

# Generated at 2022-06-14 06:00:40.371828
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """IllegalUseOfScopeReplacer.__unicode__ should work"""
    e = IllegalUseOfScopeReplacer('name', 'message')
    e.__unicode__()



# Generated at 2022-06-14 06:00:53.127627
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    from breezy.tests import (
        TestNotApplicable,
        TestCase,
        )

    from bzrlib.lazy_import import RequiredFeatureMissing

    class TestRequiredFeatureMissing(TestCase):
        def setUp(self):
            TestCase.setUp(self)
            self.old_should_proxy = ScopeReplacer._should_proxy

        def tearDown(self):
            TestCase.tearDown(self)
            ScopeReplacer._should_proxy = self.old_should_proxy

    class TestScopeReplacer(TestCase):

        def setUp(self):
            TestCase.setUp(self)
            self.old_should_proxy = ScopeReplacer._should_proxy

        def tearDown(self):
            TestCase.tearDown(self)
            ScopeReplacer._should_proxy = self.old

# Generated at 2022-06-14 06:00:55.867817
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    lst = []
    def factory(self, scope, name):
        return lst
    r = ScopeReplacer(globals(), factory, 'lst')
    r.append(1)
    assert lst == [1]

# Generated at 2022-06-14 06:01:03.578228
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    """test__setattr__

    This test makes sure the __setattr__ method of ScopeReplacer
    is acting correctly, which is to call setattr on the object
    that will be replaced by the ScopeReplacer.
    """
    obj = object()
    sr = ScopeReplacer({}, lambda self, scope, name: obj, 'name')
    # Make a new method for the object
    def new_method(self):
        return "new"
    sr.__setattr__('new_method', new_method)
    # Make sure the attribute got set correctly
    assert obj.new_method() == "new"
    assert sr.new_method() == "new"


# Generated at 2022-06-14 06:01:10.200272
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """IllegalUseOfScopeReplacer.__unicode__()"""

    instance = IllegalUseOfScopeReplacer('name', 'msg')
    unicode_value = instance.__unicode__()
    type(unicode_value)
    unicode_value == u'ScopeReplacer object \'name\' was used incorrectly: msg'



# Generated at 2022-06-14 06:01:20.430719
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    """Unit test for method ScopeReplacer.__call__"""
    import unittest
    import six
    class TestScopeReplacer(unittest.TestCase):
        def test_basic(self):
            """Test basic calling of ScopeReplacer objects"""
            # Sadly, we can't test more than this without also loading the
            # underlying module, which is unsafe as the loading of that module
            # might use the object.
            class TestObject(object):
                def method_a(self, x):
                    return x
            class TestReplacer(ScopeReplacer):
                def __init__(self, scope, name):
                    super(TestReplacer, self).__init__(scope, lambda x,y,z:
                            TestObject(), name)
            # Create a replacer in the global scope

# Generated at 2022-06-14 06:01:32.234760
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """Unit test for method __unicode__ of class IllegalUseOfScopeReplacer"""
    assert unicode(IllegalUseOfScopeReplacer('foo', 'bar')) \
        == u'ScopeReplacer object \'foo\' was used incorrectly: bar'

# Generated at 2022-06-14 06:01:40.788967
# Unit test for method __getattribute__ of class ScopeReplacer
def test_ScopeReplacer___getattribute__():
    import unittest
    import types

    from bzrlib._lazy_import_py24 import _LazyImport_py24

    class Module(object):

        _Module__builtins = None

        def __init__(self, _):
            pass

        class _Module__builtins(object):

            class Exception(Exception):
                pass

    class LazyImportTest(unittest.TestCase):
        """A unittest.TestCase that provides a lazy_import method."""

        def __init__(self, *args, **kwargs):
            super(LazyImportTest, self).__init__(*args, **kwargs)
            self.addCleanup(self.cleanup_scope)

# Generated at 2022-06-14 06:01:50.081704
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """test_IllegalUseOfScopeReplacer___unicode__
    """
    s = IllegalUseOfScopeReplacer('foo', 'bar')
    assert isinstance(s.__unicode__(), unicode), repr(s.__unicode__())
    assert s._format() == unicode(s), repr(s._format())
    assert unicode(s) == u'foo was used incorrectly: bar', repr(unicode(s))
test_IllegalUseOfScopeReplacer___unicode__.unittest = ['.inter']



# Generated at 2022-06-14 06:02:00.013090
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    import bzrlib.lazy_import, __builtin__
    bzrlib.lazy_import.lazy_import(__builtin__, '''
    import bzrlib.split_repo
    ''')
    bzrlib.lazy_import.lazy_import(__builtin__, '''
    from bzrlib import errors
    ''')

    assert errors is bzrlib.errors
    assert bzrlib.split_repo(':memory:') is not None



# Generated at 2022-06-14 06:02:06.105453
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__ implemented"""
    import sys
    e = IllegalUseOfScopeReplacer(name='name',
            msg='This is an error message')
    u = unicode(e)
    if not isinstance(u, unicode):
        raise AssertionError('unicode(e) returned non-unicode: %r' % (u,))


# Generated at 2022-06-14 06:02:11.392245
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    import doctest
    from bzrlib.tests.test_lazy_import import LazyModule
    t = LazyModule('test', {}, {})
    doctest.run_docstring_examples(t.__setattr__, globals())



# Generated at 2022-06-14 06:02:22.578436
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    import doctest
    from bzrlib import lazy_import

# Generated at 2022-06-14 06:02:35.107211
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """IllegalUseOfScopeReplacer.__unicode__() should work"""
    # This test is for Issue #8211: __unicode__() method of bzrlib.errors
    # should always return an unicode object.
    from bzrlib.lazy_import import IllegalUseOfScopeReplacer

    # The following string should not cause an UnicodeDecodeError.
    # It should simply be decoded as 'ascii' and returned as an unicode
    # object.
    obj = IllegalUseOfScopeReplacer('name', 'msg')

# Generated at 2022-06-14 06:02:45.287580
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    import bzrlib.lazy_import
    bzrlib.lazy_import.lazy_import(globals(), """
import sys
""")

# Generated at 2022-06-14 06:02:51.600156
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    import os
    import bzrlib.tests

    def create_os(self, scope, name):
        return os

    lazy_os = ScopeReplacer(globals(), create_os, 'os')
    # check that an object that has replaced itself is callable
    os.close(bzrlib.tests.open_noatime(__file__, 'r'))

# Generated at 2022-06-14 06:03:09.259968
# Unit test for method __getattribute__ of class ScopeReplacer
def test_ScopeReplacer___getattribute__():
    import sys
    mod_name = "bzrlib.lazy_import"
    factory = "lazy_import"
    var_name = "bzrlib_factory"
    existing_obj = sys.modules[mod_name]
    scope = {var_name: existing_obj}
    scope_replacer = ScopeReplacer(scope, lambda self, scope, name: scope[name], var_name)
    assert scope_replacer.__getattribute__(factory) == existing_obj.__getattribute__(factory)



# Generated at 2022-06-14 06:03:15.703604
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    class FakeScope(object):
        pass
    scope = FakeScope()
    scope.var = 0
    def factory(replacer, scope, name):
        scope.var = 1
        return scope.var
    replacer = ScopeReplacer(scope, factory, 'var')
    scope.var = 2
    # ScopeReplacer allows to assign only before first accessing
    from bzrlib.tests.test_lazy_import import test_ScopeReplacer___setattr__
    try:
        replacer.__setattr__('var', 2)
    except IllegalUseOfScopeReplacer:
        pass
    else:
        raise AssertionError(
            'Assigning to a ScopeReplacer should not be allowed after'
            ' the first access')

# Generated at 2022-06-14 06:03:26.104564
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    # call
    # __call__
    # __call__ of class ScopeReplacer
    import bzrlib.lazy_import
    bzrlib.lazy_import.lazy_import(globals(), """
    import bzrlib.osutils
    """)
    bzrlib.osutils.split_lines('s')


    # Basic test of __call__
    class Foo(object):
        def __call__(self, a, b=4):
            return [a, b]
    foo = Foo()
    bzrlib.lazy_import.lazy_import(globals(), """
    import foo
    """)
    s = foo(1, 2)
    if not(isinstance(s, list)
           and s == [1,2]): raise AssertionError



# Generated at 2022-06-14 06:03:30.011181
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """This test exercises __unicode__ because the make_exception method
    in the bzrlib.trace module is the only other method that uses it.
    """
    e = IllegalUseOfScopeReplacer('a', 'b')
    assert isinstance(e.__unicode__(), unicode)

# Generated at 2022-06-14 06:03:37.646546
# Unit test for method __getattribute__ of class ScopeReplacer
def test_ScopeReplacer___getattribute__():
    """__getattribute__ should return the object's object attribute"""
    class Foo(ScopeReplacer):
        _factory = lambda s, scope, name: 'real_obj'
        _scope = {'foo': 'bar'}
        _name = 'obj'
    foo = Foo({}, '_factory', '_name')
    assert foo.__getattribute__('_factory') == '_factory'


# Generated at 2022-06-14 06:03:42.860227
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """__str__ should always return a str object, never a unicode object."""
    msg = 'test message'
    e = IllegalUseOfScopeReplacer('name', msg)
    assert isinstance(e.__str__(), str)

# Generated at 2022-06-14 06:03:52.064632
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__ of IllegalUseOfScopeReplacer must translate _fmt
    """
    from bzrlib.i18n import gettext
    # this is copied from breezy.tests.i18n_strings.gettext_testclass, it
    # is a little awkward to use this copy here but the test below already
    # exists, so it is better to use it than to create a new one.
    class TestClass(object):
        """A dummy class for testing interpolation"""
        _fmt = "A test for gettext interp %(a)s and %(b)s"
    e = IllegalUseOfScopeReplacer('an_example', 'A message: ')
    expected = gettext(TestClass._fmt) % {'a': 10, 'b': 20}
    e.__class__ = TestClass
   

# Generated at 2022-06-14 06:04:02.802374
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__ should return a unicode string."""
    err = IllegalUseOfScopeReplacer('foo', 'bar')
    u = unicode(err)
    # dir() should return a list of unicode strings.
    # We use list() here, to prevent __getitem__ from being called,
    # which would cause a lazy-loading.
    dir_u = list(dir(u))
    # __repr__ should return a str
    repr_u = repr(u)

    assert isinstance(u, unicode)
    assert isinstance(dir_u[0], unicode)
    assert isinstance(repr_u, str)



# Generated at 2022-06-14 06:04:05.718359
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__ should return a unicode object."""
    import bzrlib.lazy_import
    e1 = bzrlib.lazy_import.IllegalUseOfScopeReplacer('imported', 'blah')
    u = unicode(e1)
    assert isinstance(u, unicode)


# Generated at 2022-06-14 06:04:17.940102
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__() should return a unicode string.

    It should call the unicode() builtin on its internal string if it is
    a str, to try and convert it to unicode.
    """
    from bzrlib.lazy_import import IllegalUseOfScopeReplacer
    u = IllegalUseOfScopeReplacer(name='Foo', msg='Very bad')
    # This exception has a default encoding of 'utf8' which is not the default
    # encoding on python 2.6, so convert it to unicode using the default
    # encoding.
    u = unicode(u)
    # now check that it is indeed a unicode object.
    assert isinstance(u, unicode)


# Generated at 2022-06-14 06:04:33.948595
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    from bzrlib.tests import TestCaseWithTransport
    class TestScopeReplacer(TestCaseWithTransport):
        def test_basic(self):
            from bzrlib.lazy_import import ScopeReplacer
            self.assertRaises(IllegalUseOfScopeReplacer,
                ScopeReplacer, {'a': 1}, lambda:1, 'a')
            self.assertRaises(IllegalUseOfScopeReplacer,
                ScopeReplacer, {}, lambda x:x, 'a')

    import doctest
    doctest.testmod()

    # Test the unittest
    TestScopeReplacer('test_basic').run()

# Generated at 2022-06-14 06:04:47.523814
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    __tracebackhide__ = True
    from StringIO import StringIO
    old_stderr, sys.stderr = sys.stderr, StringIO()

# Generated at 2022-06-14 06:04:48.373473
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    pass

# Generated at 2022-06-14 06:04:55.347044
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """Tests the __str__ method of class IllegalUseOfScopeReplacer"""
    class TestIllegalUseOfScopeReplacerUnicode(Exception):
        _fmt = "Test %(name)s"
    class TestIllegalUseOfScopeReplacerStr(Exception):
        # No unicode here
        _fmt = "Test %(name)s"
    # Cases that should succeed
    expect_unicode = TestIllegalUseOfScopeReplacerUnicode('test_name')
    result_unicode = str(expect_unicode)
    expect_str = TestIllegalUseOfScopeReplacerStr('test_name')
    result_str = str(expect_str)
    # Check results
    assert result_unicode == 'Test test_name'
    assert result_str == 'Test test_name'




# Generated at 2022-06-14 06:05:08.194792
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    global __test_ScopeReplacer_obj
    global __test_ScopeReplacer_attr
    global __test_ScopeReplacer_value
    global __test_ScopeReplacer_result
    __test_ScopeReplacer_obj = ScopeReplacer({}, lambda scopeReplacer, scope, name: scopeReplacer, "name")

# Generated at 2022-06-14 06:05:14.352945
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    import bzrlib
    class SomeClass:
        _should_proxy = False
        _fmt = "TEST FMT"
        def some_method(self):
            """TEST DOCSTRING"""
    bzrlib.lazy_import.ScopeReplacer.__class__ = SomeClass


# Generated at 2022-06-14 06:05:19.922657
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """__str__ should return a str object."""
    import bzrlib.tests
    s = str(IllegalUseOfScopeReplacer('foo', 'bar'))
    bzrlib.tests.check_type(s, str)
    assert s == 'bar'


# Generated at 2022-06-14 06:05:28.896745
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    class MyException(Exception):
        pass
    class _TestSendSsh(object):
        def __call__(self):
            return MyException()
    def _create_object(self, scope, name):
        return _TestSendSsh()
    scope = {}
    class_obj = ScopeReplacer(scope, _create_object, '_ssh')
    try:
        class_obj()
    except MyException:
        pass
    else:
        raise AssertionError('ScopeReplacer.__call__ not calling')
# end unit test

# Generated at 2022-06-14 06:05:39.790193
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    import bzrlib.tests
    bzrlib.tests.TestCaseWithMemoryTransport.tearDown()

    import bzrlib.osutils
    reload(bzrlib.osutils)
    bzrlib.osutils.is_quiet = False
    import bzrlib
    reload(bzrlib)

    ScopeReplacer._should_proxy = False
    import bzrlib
    reload(bzrlib)
    bzrlib.lazy_import = ScopeReplacer(globals(), lazy_import_maker,
        'lazy_import')
    import bzrlib
    reload(bzrlib)
    import bzrlib.commands
    reload(bzrlib.commands)
    ScopeReplacer._should_proxy = True


# Generated at 2022-06-14 06:05:45.808286
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """__str__ must return a str"""
    import unicodedata
    s = 'a str'
    assert unicodedata.normalize('NFC', unicode(s)) == unicode(unicode(s))
    s = r'a str'
    assert unicodedata.normalize('NFC', unicode(s)) == unicode(unicode(s))
    s = u'a unicode'
    assert unicodedata.normalize('NFC', unicode(s)) == unicode(unicode(s))



# Generated at 2022-06-14 06:06:08.121414
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    class C(object):
        def __call__(self, *args, **kwargs):
            return (args, kwargs)
    c = C()
    s = ScopeReplacer(globals(), lambda self, d, name: c, 'c')
    r = c(12, 34, 56, a=1, b=2, c=3)
    e = s(12, 34, 56, a=1, b=2, c=3)
    assert r == e, (r, e)
    assert s == c


# Generated at 2022-06-14 06:06:18.324506
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """IllegalUseOfScopeReplacer.__str__() works correctly

    The return value of IllegalUseOfScopeReplacer.__str__() is a str,
    and should be the same as IllegalUseOfScopeReplacer.__unicode__()
    encoded with utf8.
    """
    from bzrlib.lazy_import import IllegalUseOfScopeReplacer
    msg = u"This is a unicode message."
    u = IllegalUseOfScopeReplacer('name', msg, extra=None)
    assert isinstance(u.__str__(), str)
    assert u.__unicode__().encode('utf8') == u.__str__()
    msg = "This is a str message."
    u = IllegalUseOfScopeReplacer('name', msg, extra=None)

# Generated at 2022-06-14 06:06:29.427543
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__ of IllegalUseOfScopeReplacer returns unicode"""
    old_failed_use_case = u'\xe4, \xf6, \xfc and \xdf'
    e = IllegalUseOfScopeReplacer('foo', old_failed_use_case)
    e_unicode = unicode(e)
    e_str = str(e)
    # Check that the unicode version is the same as the str version.
    # If these are different, we'll need to fix python2.4 to use
    # %z in _format(), and fix python2.5 to use %b in _format().
    assert e_unicode == e_str



# Generated at 2022-06-14 06:06:39.703459
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    def _test(name, msg, extra=''):
        inst = IllegalUseOfScopeReplacer(name, msg, extra)
        str(inst) # should not raise an exception

    _test('foo', 'bar')
    _test('foo', 'bar', 'baz')
    # this doesn't have all the data
    IllegalUseOfScopeReplacer._fmt = '%(name)s %(msg)s'
    _test('foo', 'bar')
    IllegalUseOfScopeReplacer._fmt = '%(name)s %(msg)s %(extra)s'
    _test('foo', 'bar', 'baz')




# Generated at 2022-06-14 06:06:45.706000
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    from bzrlib.tests import TestCase

    class TestScopeReplacer(TestCase):
        def setUp(self):
            super(TestScopeReplacer, self).setUp()
            self.scope = {}
            def factory():
                return 'test'
            self.test_obj = ScopeReplacer(self.scope, factory, 'test')
        def test___call__(self):
            self.assertEqual('test', self.test_obj())

    TestCase.run_suite(TestScopeReplacer)


# Generated at 2022-06-14 06:06:55.049599
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """IllegalUseOfScopeReplacer.__unicode__ must return a unicode"""
    from bzrlib.tests import TestCase
    from bzrlib.lazy_import import IllegalUseOfScopeReplacer
    class Test(IllegalUseOfScopeReplacer):
        pass
    a = Test('a', 'b')
    class Nasty(object):
        def __unicode__(self):
            return 'nasty unicode'
    a._preformatted_string = Nasty()
    self.assertIsInstance(unicode(a), unicode)



# Generated at 2022-06-14 06:07:01.138040
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    e = IllegalUseOfScopeReplacer('foo', 'msg', 'extra')
    # XXX do something with u ?
    u = unicode(e)
    # XXX do something with s ?
    s = str(e)
    # For coverage, call the preformatted version.
    e.__dict__['_preformatted_string'] = 'preformatted string'
    s = str(e)



# Generated at 2022-06-14 06:07:06.153600
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    from bzrlib.lazy_import import lazy_import
    from bzrlib import (
        errors,
        osutils,
        branch,
        )
    import bzrlib.branch
    raise NotImplementedError('')

# Generated at 2022-06-14 06:07:12.391472
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """Ensure IllegalUseOfScopeReplacer has __unicode__ method

    __unicode__ is supposed to return an unicode object.

    This test will fail if you rename the method __unicode__
    """
    e = IllegalUseOfScopeReplacer(u'foo', u'bar')
    # __unicode__() should always return a 'unicode' object
    # never a 'str' object.
    if type(e.__unicode__()) != unicode:
        raise AssertionError("IllegalUseOfScopeReplacer must have a "
                             "__unicode__() method")


# Generated at 2022-06-14 06:07:19.571752
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """__str__ of IllegalUseOfScopeReplacer should produce a valid str

    See http://bugs.python.org/issue6333 and
    http://bugs.python.org/issue6047

    This is not a complete test, but at least it check that we are
    generating a valid str object.
    """
    str(IllegalUseOfScopeReplacer('foo', 'bar'))



# Generated at 2022-06-14 06:07:56.610076
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """IllegalUseOfScopeReplacer.__str__ should render the error message into
    str

    This requires that the most recent traceback is stored.

    Calling str() on the error message object should render an unicode object
    into str, encoded in the default encoding (typically 'ascii').

    When the traceback is used in the error message, __str__ should work
    even when traceback.format_list is not available (i.e. not implemented
    in the current version of Python).
    """
    # It should display an UnicodeDecodeError when an encoding other than
    # str or unicode is given:
    # - it should decode the given bytes using the default encoding
    # - it should return the message as str encoded in the default encoding
    #   (ascii)
    message = 'message'
    plain_error = IllegalUseOf

# Generated at 2022-06-14 06:08:00.132659
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """IllegalUseOfScopeReplacer.__str__()"""
    import bzrlib.tests.test_errors
    return bzrlib.tests.test_errors.test___str__(IllegalUseOfScopeReplacer)

# Generated at 2022-06-14 06:08:10.550920
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    import os
    from . import lazy_import
    mod = os.path.abspath(lazy_import.__file__)
    try:
        reload(lazy_import)
    except NameError:
        import imp
        imp.load_source(lazy_import.__name__, mod)
    else:
        lazy_import.__loader__.load_module(lazy_import.__name__)
    test_case = globals()['test_ScopeReplacer___setattr__']
    if (hasattr(test_case, '__self__') and
        not isinstance(test_case.__self__, ScopeReplacer)):
        raise AssertionError(  # AssertionError if no AssertionError
            "ScopeReplacer.__setattr__() doesn't"
            " recognize self")


# Generated at 2022-06-14 06:08:13.779807
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    # Method __setattr__ of class ScopeReplacer
    # This method is used in many tests.
    # No actual test needed.
    pass


# Generated at 2022-06-14 06:08:26.665055
# Unit test for method __getattribute__ of class ScopeReplacer
def test_ScopeReplacer___getattribute__():
    from bzrlib.tests.per_lazy_import import TestCaseWithMemoryTransport

    class TestLazyImport(TestCaseWithMemoryTransport):

        def test_ScopeReplacer_proxy(self):
            scope = {}
            one = lazy_import(scope, 'from bzrlib import errors')

            # Ensure that the scope contains an iterable object
            self.failUnless(hasattr(scope, '__iter__'))
            # Ensure that the scope contains a 'errors' entry
            self.failUnless(one._name in scope)
            # Ensure that the scope entry points to a ScopeReplacer
            self.failUnless(isinstance(scope[one._name], ScopeReplacer))

            # Ensure that the ScopeReplacer can compile a re
            re = one.re

# Generated at 2022-06-14 06:08:28.381281
# Unit test for method __getattribute__ of class ScopeReplacer
def test_ScopeReplacer___getattribute__():
    assert False, "Test could not be implemented"



# Generated at 2022-06-14 06:08:39.034433
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """Testing IllegalUseOfScopeReplacer.__str__"""
    try:
        raise IllegalUseOfScopeReplacer(name='abc', msg='def')
    except IllegalUseOfScopeReplacer as e:
        assert str(e) == "IllegalUseOfScopeReplacer object 'abc' was used incorrectly: def"
    try:
        raise IllegalUseOfScopeReplacer(name='abc', msg='def', extra='ghi')
    except IllegalUseOfScopeReplacer as e:
        assert str(e) == "IllegalUseOfScopeReplacer object 'abc' was used incorrectly: def: ghi"



# Generated at 2022-06-14 06:08:46.298239
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """__str__ should return utf-8 encoded string"""
    from bzrlib.i18n import fix_user_encoding
    fix_user_encoding()
    try:
        b'foo'.decode('utf-8')
    except UnicodeDecodeError:
        raise TestSkipped("utf-8 support is not enabled")
    e = IllegalUseOfScopeReplacer("foo", "bar")
    assert isinstance(e.__str__(), str)
    assert e.__unicode__().encode('utf-8') == e.__str__()



# Generated at 2022-06-14 06:08:57.133858
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    # test the ability to call LazyObjects.
    # call_result is given a lazy_import'ed function with a return value
    # so that it can be called without fear of circular import errors.
    _f = lambda value: lambda: value
    call_result = _f("called!")
    def call_factory(o, s, n):
        return call_result
    l = ScopeReplacer({}, call_factory, 'l')
    eq = testtools.matchers.MatchesAll(
        testtools.matchers.Equals("called!"),
        testtools.matchers.StartsWith("called!"))
    assertThat(l(), eq)
# test_ScopeReplacer___call__()



# Generated at 2022-06-14 06:09:02.147067
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    # test that __call__ delegates to the real object
    from bzrlib import lazy_import
    class FuncObject(object):
        def __call__(self, arg):
            return arg + 5
    true_obj = FuncObject()
    def factory(me, scope, name):
        return true_obj
    scope = {}
    scope_replacer = lazy_import.ScopeReplacer(scope, factory, 'obj')
    assert scope['obj'] is scope_replacer
    assert scope_replacer(10) == 15
    assert scope['obj'] is true_obj

