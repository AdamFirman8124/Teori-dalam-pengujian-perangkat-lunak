

# Generated at 2022-06-14 06:00:03.748390
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """__str__ returns value of _format"""
    class TestableIllegalUseOfScopeReplacer(IllegalUseOfScopeReplacer):

        def _format(self):
            return 'preformatted message'
    e = TestableIllegalUseOfScopeReplacer('name', 'msg')
    assert str(e) == 'preformatted message'

# Generated at 2022-06-14 06:00:14.488386
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    import sys
    import unicodedata
    from bzrlib.tests.blackbox import ExternalBase


# Generated at 2022-06-14 06:00:20.888242
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__(self): must return a unicode object"""
    x = IllegalUseOfScopeReplacer('name', 'msg')
    result = x.__unicode__()
    # Test explicitly against unicode, not '__builtin__.unicode' which
    # is a python 2.x specific alias.
    assert isinstance(result, unicode)


# Generated at 2022-06-14 06:00:29.588602
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    """
    Unit test for method __setattr__ of class ScopeReplacer
    """
    replacer = ScopeReplacer(object_class_name='ScopeReplacer',
                             suite_name='lazy_import',
                             module_relative_path='__init__.py')
    # Default value of attribute attr
    assert replacer.attr == None
    # Setting attribute attr
    replacer.attr = "lazy import"
    # Value of attribute attr
    assert replacer.attr == "lazy import"

# Generated at 2022-06-14 06:00:41.764251
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():# This is a bug in the original code.
    from testtools import TestCase, TestResult
    from testtools.testresult import ExtendedToOriginalDecorator
    from testtools.testsuite import MultipleExceptions, iterate_tests
    from testtools.testsuite.iterator import TestSuiteIterator
    from testtools.testsuite.multiplex import _CollectingTestResult
    from testtools.testsuite.runtest import RunTest
    from testtools.testsuite.run import _extract_result
    from testtools.testsuite.stb import (
        DebugResult,
        DebugResultDecorator,
        SkippedResult,
        )
    import os
    import sys
    import unittest
    import testtools
    if sys.version_info[0] == 3:
        import io
        StringIO = io

# Generated at 2022-06-14 06:00:53.964134
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """IllegalUseOfScopeReplacer.__unicode__() should give something like
    IllegalUseOfScopeReplacer(u'foo', u'bar', u'baz')"""
    sre = IllegalUseOfScopeReplacer(u'foo', u'bar', u'baz')
    # There is no easy way to test this precisely.
    # The %s operator of unicode in Python 2.x doesn't always work
    # properly with Unicode strings, but does work properly with
    # UTF8-encoded strings.  We can't test the __str__ method, but the
    # __unicode__ method should give the right results.  Since the
    # results should be the same, we can just check that it has the
    # right number of %-signs in it!

# Generated at 2022-06-14 06:00:57.255206
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """Unit test for method __str__ of class IllegalUseOfScopeReplacer"""
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS)



# Generated at 2022-06-14 06:01:04.641649
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    # testing the IllegalUseOfScopeReplacer class
    import sys
    import tempfile
    def make_exception(name):
        return IllegalUseOfScopeReplacer(name, 'test message')
    e = make_exception('e1')
    # str(e) should return a 'str' object
    assert isinstance(str(e), str), "str(e) should be a str object"
    # str(e) should not raise an exception
    str(e)
    # the output should be split over two lines.
    assert str(e).count('\n') == 1
    # check unicode conversion of this exception

# Generated at 2022-06-14 06:01:12.722556
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """Unit tests for IllegalUseOfScopeReplacer.__str__

    If you see this test fail in a PQM run, it means that the output of an
    exception has changed. The easiest way to get the tests to pass again
    is to simply update the expected output string.
    """
    e = IllegalUseOfScopeReplacer("foo", "error")
    assert str(e) == "foo was used incorrectly: error"



# Generated at 2022-06-14 06:01:16.298113
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__ converts to unicode"""
    e = IllegalUseOfScopeReplacer('foo', 'bar')
    u = e.__unicode__()
    if not isinstance(u, unicode):
        raise AssertionError('%r is not unicode' % u)


# Generated at 2022-06-14 06:01:33.285130
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__()"""
    # Test of method '__unicode__' from class 'IllegalUseOfScopeReplacer'
    class _Dummy(IllegalUseOfScopeReplacer):
        _fmt = "foo %(msg)s"
    assert unicode(_Dummy("foo_name", "bar_msg")) == 'foo bar_msg'
    # Test of method '__unicode__' from class 'IllegalUseOfScopeReplacer'
    class _Dummy(IllegalUseOfScopeReplacer):
        _fmt = "%s %s"
    assert unicode(_Dummy("foo_name", "bar_msg")) == 'foo_name bar_msg'
    # Test of method '__unicode__' from class 'IllegalUseOfScopeReplacer'

# Generated at 2022-06-14 06:01:41.262214
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    def factory(self, scope, name):
        return lambda *args, **kwargs: (name, scope[name], args, kwargs)
    scope = {}
    name = 'foo'
    scope[name] = ScopeReplacer(scope, factory, name)
    obj = scope[name]
    test_args = [1, 2, 3]
    test_kwargs = {'a':1, 'b':2}
    expected_args = test_args
    expected_kwargs = test_kwargs
    result = obj(*test_args, **test_kwargs)
    # resolver will have replaced the ScopeReplacer instance
    expected_obj = factory(None, scope, name)
    expected = (name, expected_obj, expected_args, expected_kwargs)
    assert result == expected

    name = 'bar'


# Generated at 2022-06-14 06:01:46.610784
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """Using IllegalUseOfScopeReplacer(..).__unicode__() should work."""
    e = IllegalUseOfScopeReplacer('x', 'y')
    unicode(e)
    str(e)


# Generated at 2022-06-14 06:01:50.492619
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """Test for IllegalUseOfScopeReplacer.__str__"""
    e = IllegalUseOfScopeReplacer('foo', 'bar', 'baz')
    assert str(e) == 'ScopeReplacer object \'foo\' was used incorrectly: bar: baz'

# Generated at 2022-06-14 06:02:00.347294
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """IllegalUseOfScopeReplacer.__unicode__ should return a unicode object"""
    e = IllegalUseOfScopeReplacer('scope_replacer_object_name', "Error message")
    result = unicode(e)
    # We can't really test anything about the contents, because that depends
    # on the current locale.  At least make sure it's a unicode string.
    if not isinstance(result, unicode):
        raise AssertionError('result should be unicode, but it is %r'
                             % (result,))



# Generated at 2022-06-14 06:02:02.767309
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__() should return a unicode object."""
    e = IllegalUseOfScopeReplacer('name', 'msg', 'extra')
    assert isinstance(unicode(e), unicode)



# Generated at 2022-06-14 06:02:07.005166
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__(): # TODO py3k

    """__str__() should always return a str object, not a unicode object"""

    from bzrlib.lazy_import import IllegalUseOfScopeReplacer
    e = IllegalUseOfScopeReplacer(
        'name', 'msg', 'extra')
    assert isinstance(str(e), str)



# Generated at 2022-06-14 06:02:18.823840
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    def test_method():
        pass
    fake_object = ScopeReplacer({}, lambda x, y, z: test_method, 'name')
    assert fake_object() == test_method()

    def test_set_val(val):
        return val
    fake_object = ScopeReplacer({}, lambda x, y, z: test_set_val, 'name')
    assert fake_object(1) == 1

    def test_kwargs(**kwargs):
        return kwargs
    fake_object = ScopeReplacer({}, lambda x, y, z: test_kwargs, 'name')
    assert fake_object(a=1, b=2) == {'a': 1, 'b': 2}



# Generated at 2022-06-14 06:02:30.871522
# Unit test for method __getattribute__ of class ScopeReplacer
def test_ScopeReplacer___getattribute__():
    # Create an object to test
    from bzrlib.tests import TestCase
    from bzrlib.tests.test_lazy_import import TestLazyImport
    from bzrlib.lazy_import import ScopeReplacer
    from bzrlib.i18n import gettext
    import bzrlib
    obj = ScopeReplacer({},
        lambda _lazy_object, scope, name: TestLazyImport(name, scope),
        'bzrlib')
    obj.__getattribute__('_name')
    obj.__getattribute__('_real_obj')
    obj.__getattribute__('_resolve')
    obj.__getattribute__('bzrlib')
    ScopeReplacer._should_proxy = False
    obj.__getattribute__('bzrlib')
    ScopeReplacer

# Generated at 2022-06-14 06:02:42.636998
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    import sys
    bzrlib = sys.modules['bzrlib']
    _factory = lambda self, scope, name: bzrlib
    _name = 'bzrlib'
    repl = ScopeReplacer(globals(), _factory, _name)
    ScopeReplacer._should_proxy = False

    # this is actually the first time the module is loaded
    assert repl.__setattr__('_should_proxy', False)
    # and this won't work when we repeat it
    try:
        repl.__setattr__('_should_proxy', False)
    except IllegalUseOfScopeReplacer as e:
        assert str(e).startswith(
            'ScopeReplacer object \'bzrlib\' was used incorrectly:'
            ' Illegal attribute access.')

# Generated at 2022-06-14 06:02:58.904153
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    assert repr(IllegalUseOfScopeReplacer('name', 'msg')) == \
        'IllegalUseOfScopeReplacer(name)'
    exc = IllegalUseOfScopeReplacer('name', 'msg', extra='extra')
    assert repr(exc) == \
        "IllegalUseOfScopeReplacer('name', 'msg', extra='extra')"
    assert str(exc) == "name was used incorrectly: msg: extra"



# Generated at 2022-06-14 06:03:11.734896
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    from bzrlib.lazy_import import lazy_import, ScopeReplacer
    from bzrlib import (
        errors,
        osutils,
        branch,
        )
    import bzrlib.branch

    class ModuleObject(object):
        def __init__(self, val):
            self.val = val

        def __call__(self, *args, **kwargs):
            return self.val

    test_globals = {}
    lazy_import(test_globals, '''
    from bzrlib import (
        errors,
        osutils,
        branch,
        )
    import bzrlib.branch
    ''')
    test_globals['errors'] = ModuleObject(10)
    test_globals['osutils'] = ModuleObject(20)


# Generated at 2022-06-14 06:03:16.187944
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    from bzrlib import lazy_import
    def a_factory(self, scope, name): return 1
    lazy_import.lazy_import(globals(), '''
    a = None
    ''')
    assert a() == 1

# Generated at 2022-06-14 06:03:20.662494
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__ must return a unicode object"""
    e = IllegalUseOfScopeReplacer('name', 'msg', 'extra')
    res = unicode(e)
    assert isinstance(res, unicode)



# Generated at 2022-06-14 06:03:30.685017
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """IllegalUseOfScopeReplacer.__unicode__() returns a unicode object"""
    try:
        raise IllegalUseOfScopeReplacer('foo', 'bar')
    except IllegalUseOfScopeReplacer as e:
        error = e
    u = unicode(error)
    if not isinstance(u, unicode):
        raise AssertionError('IllegalUseOfScopeReplacer.__unicode__() did'
                             ' not return a unicode object: %r %r'
                             % (type(u), u))
    s = str(error)
    if not isinstance(s, str):
        raise AssertionError('IllegalUseOfScopeReplacer.__str__() did'
                             ' not return a str object: %r %r'
                             % (type(s), s))



# Generated at 2022-06-14 06:03:43.174482
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    # Set to False to raise IllegalUseOfScopeReplacer if methods called on
    # object after it has been replaced.
    ScopeReplacer._should_proxy = False
    x = object()
    scope = {}
    def create_obj(_unused, scope, name):
        scope[name] = x
        return x
    name = 'foo'
    from bzrlib.lazy_import import ScopeReplacer
    obj = ScopeReplacer(scope, create_obj, name)

# Generated at 2022-06-14 06:03:50.161711
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    import bzrlib
    __tracebackhide__ = True
    def test_method(self, scope, name):
        return 10
    def test_function(x, y):
        return x + y
    obj = ScopeReplacer(bzrlib.__dict__, test_method, "add")
    assert obj(1, 2) == 3
    obj = ScopeReplacer(bzrlib.__dict__, test_function, "add")
    assert obj(1, 2) == 10



# Generated at 2022-06-14 06:04:01.837946
# Unit test for method __getattribute__ of class ScopeReplacer
def test_ScopeReplacer___getattribute__():
    class _FakeScope(dict):
        _called = []
        def __getitem__(self, key):
            self._called.append(('__getitem__', key))
            return super(_FakeScope, self).__getitem__(key)

    def _factory(replacer, scope, name):
        scope._called.append(('_factory', name))
        return 'fake object'

    scope = _FakeScope()
    replacer = ScopeReplacer(scope, _factory, 'foo')
    scope._called = []

    # Get the fake object itself
    assert replacer._resolve() == 'fake object'
    assert scope._called == [('_factory', 'foo')]
    scope._called = []

    # Fetch an attribute from the fake object
    assert replacer.bar == 'fake object'
   

# Generated at 2022-06-14 06:04:11.257375
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__ should return unicode, either a str or a unicode object"""
    from bzrlib.tests import TestCase
    from bzrlib.lazy_import import IllegalUseOfScopeReplacer

    # The type of IllegalUseOfScopeReplacer._fmt is str
    msg = 'foo'
    e = IllegalUseOfScopeReplacer('name', msg)
    u = unicode(e)
    TestCase.assertEquals(str, type(u))
    TestCase.assertTrue(isinstance(u, unicode))

    # The type of IllegalUseOfScopeReplacer._fmt is unicode
    msg = u'foo'
    e = IllegalUseOfScopeReplacer('name', msg)
    u = unicode(e)
    TestCase.assertEquals(unicode, type(u))
    Test

# Generated at 2022-06-14 06:04:19.458897
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """__str__(IllegalUseOfScopeReplacer) == format(IllegalUseOfScopeReplacer)"""
    obj = IllegalUseOfScopeReplacer('', '')
    assert str(obj) == obj.__str__()
    obj._fmt = '%(msg)r %(name)r'
    obj.name = 'a'
    obj.msg = 'b'
    expected = 'b a'
    assert str(obj) == expected
    assert repr(obj) == 'IllegalUseOfScopeReplacer("b a")'

# Generated at 2022-06-14 06:04:35.359348
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    """Unit test for method __setattr__ of class ScopeReplacer"""
    from bzrlib.tests import TestCase
    from bzrlib.lazy_import import ScopeReplacer

    class test_ScopeReplacer___setattr__TestCase(TestCase):
        """Test case for testing method __setattr__ of class ScopeReplacer"""

        def test_setattr_fails(self):
            """Setattr fails"""
            scope = {}
            def factory():
                """Create factory"""
                return 'testing'
            ScopeReplacer(scope, factory, 'test')
            scope['test'].foo = 'bar'
            self.assertEquals(scope['test'].foo, 'bar')

    return test_ScopeReplacer___setattr__TestCase



# Generated at 2022-06-14 06:04:49.408351
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
  import bzrlib.tests
  bzrlib.tests.features.require_features(['threading'])
  import bzrlib.lazy_import
  import copy
  import threading
  import time
  o = bzrlib.lazy_import.ScopeReplacer({}, lambda a, b, c: None, 'foo')
  orig = copy.deepcopy(o)
  o.foo = 'bar'
  time.sleep(1.0)
  if orig is not o._real_obj:
    raise AssertionError
  try:
    bzrlib.lazy_import.ScopeReplacer._should_proxy = False
    o.foo = 'bar'
    raise AssertionError
  except bzrlib.lazy_import.IllegalUseOfScopeReplacer:
    pass


# Generated at 2022-06-14 06:04:56.546412
# Unit test for method __getattribute__ of class ScopeReplacer
def test_ScopeReplacer___getattribute__():
    import unittest
    class Dummy():
        def __init__(self):
            pass
        def call(self):
            return "this is a return value"
    class ScopeReplacerTester(unittest.TestCase):
        def test_ScopeReplacer___getattribute__(self):
            scope = {}
            def factory(self2, scope, name):
                return Dummy()
            scope_replacer = ScopeReplacer(scope, factory, 'dummy')
            self.assertEqual(scope_replacer.call(), "this is a return value")
    suite = unittest.TestLoader().loadTestsFromTestCase(ScopeReplacerTester)
    unittest.TextTestRunner(verbosity=2).run(suite)
# end unit test

# Generated at 2022-06-14 06:05:03.594361
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """Unit test for method __str__ of class IllegalUseOfScopeReplacer"""
    # derived classes have valid _fmt attribute
    class Derived(IllegalUseOfScopeReplacer):
        _fmt = 'a %(name)s %(msg)s %(extra)s'
    msg = Derived('foo', 'bar', 'extra')
    eq = str(msg)
    assert eq == 'a foo bar extra'


# Generated at 2022-06-14 06:05:06.337456
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """IllegalUseOfScopeReplacer.__str__() must return a str object.

    Not a unicode object nor something else.
    """
    err = IllegalUseOfScopeReplacer('name', 'msg')
    str(err)



# Generated at 2022-06-14 06:05:12.483704
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    """ScopeReplacer.__setattr__ raises on use of scope replacer."""
    scope = {}
    name = 'test'
    foo = ScopeReplacer(scope, lambda self, scope, name: None, name)
    assert scope[name] is foo
    try:
        foo.baz = 'baz'
        assert False, ("Expected exception IllegalUseOfScopeReplacer"
            " was not raised.")
    except IllegalUseOfScopeReplacer:
        pass



# Generated at 2022-06-14 06:05:17.206516
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """Tests that IllegalUseOfScopeReplacer.__unicode__() returns a unicode object"""
    e = IllegalUseOfScopeReplacer('a', 'b')
    assert isinstance(e.__unicode__(), unicode)


# Generated at 2022-06-14 06:05:23.080227
# Unit test for method __getattribute__ of class ScopeReplacer
def test_ScopeReplacer___getattribute__():
    """test method __getattribute__ of class ScopeReplacer"""
    def my_factory(self, scope, name):
        return 42
    vars = {} # XXX this should probably use a string.StringIO() instance
    _replace_scope(vars, 'foo', my_factory)
    a = vars["foo"]
    assert a._resolve() == 42

# Generated at 2022-06-14 06:05:36.746620
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """Test case for IllegalUseOfScopeReplacer.__unicode__"""
    from bzrlib.tests import TestCase
    from bzrlib.lazy_import import (
        IllegalUseOfScopeReplacer,
        )
    class SampleException(Exception):
        def __init__(self, value):
            super(SampleException, self).__init__(value)
    s = 'abc'
    u1 = unicode(u'\N{LATIN SMALL LETTER A WITH ACUTE}')
    class FailedToConvertStringToUnicode(SampleException):
        def __str__(self):
            return s
    # The unicode object is correct.
    e = IllegalUseOfScopeReplacer('hello', 'it is not loaded.')

# Generated at 2022-06-14 06:05:46.272902
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__ should return a unicode string"""
    obj = IllegalUseOfScopeReplacer('fake', 'spam')
    expected = u'Unprintable exception IllegalUseOfScopeReplacer: ' \
        u'dict={\'msg\': \'spam\', \'name\': \'fake\', \'extra\': \'\'}, ' \
        u'fmt=%(name)r was used incorrectly: %(msg)s%(extra)s, ' \
        u'error=None'
    assert isinstance(obj.__unicode__(), unicode)
    assert obj.__unicode__() == expected
    # Check __str__ returns a str, not a unicode.
    assert isinstance(obj.__str__(), str)
    assert obj.__str__() == expected.encode('utf8')



# Generated at 2022-06-14 06:06:08.712794
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    """__setattr__ of ScopeReplacer"""
    # __setattr__ of ScopeReplacer # pylint: disable=W0212
    scope = {'a':1}
    replacer = ScopeReplacer(scope, lambda self, scope, name: scope[name],
                             'a')
    assert scope['a'] is replacer

# Generated at 2022-06-14 06:06:10.521275
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """IllegalUseOfScopeReplacer.__str__"""
    e = IllegalUseOfScopeReplacer('name', 'message')
    assert str(e) == "ScopeReplacer object 'name' was used incorrectly:" \
        " message"



# Generated at 2022-06-14 06:06:20.931144
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """Method __str__ of class IllegalUseOfScopeReplacer"""
    for classname, extra in [('IllegalUseOfScopeReplacer', 'bad'),
                             (IllegalUseOfScopeReplacer, 'bad')]:
        e = IllegalUseOfScopeReplacer('test', "string %s", extra)
        want = "IllegalUseOfScopeReplacer(test, string %s: bad)" % extra
        if classname == 'IllegalUseOfScopeReplacer':
            want = 'bzrlib.lazy_import.IllegalUseOfScopeReplacer' + want[22:]
        got = str(e)
        if got != want:
            raise AssertionError("__str__(%r) returned %r, wanted %r"
                                 % (e, got, want))



# Generated at 2022-06-14 06:06:26.773708
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    obj = ScopeReplacer({}, object, 'attr')
    try:
        obj.__setattr__('attr', 'value')
    except Exception as e:
        assert type(e) is IllegalUseOfScopeReplacer
        assert e.name == 'attr'
        assert e.msg.startswith('Object already replaced, ')
    else:
        assert False, 'did not raise'


# Generated at 2022-06-14 06:06:39.703207
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """IllegalUseOfScopeReplacer.__unicode__ must decode the text to unicode"""
    from bzrlib.lazy_import import IllegalUseOfScopeReplacer
    utf8_str = u'test \u20ac'
    utf8_str = utf8_str.encode('utf8')
    e = IllegalUseOfScopeReplacer('scope replacer', 'message',
                                  extra=utf8_str)
    # __unicode__ should return a unicode object
    assert isinstance(unicode(e), unicode)
    assert unicode(e).encode('utf8') == (
        "ScopeReplacer object 'scope replacer' was used incorrectly:"
        " message: 'test \xe2\x82\xac'")



# Generated at 2022-06-14 06:06:46.923264
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """This tests IllegalUseOfScopeReplacer.__str__()."""

    # Make an IllegalUseOfScopeReplacer object. It's defined in
    # bzrlib.lazy_import
    from bzrlib.lazy_import import ScopeReplacer
    s = ScopeReplacer(bzrlib, 'bzrlib', 'from bzrlib.lazy_import import bzrlib')
    # Make sure the __str__ method works.
    # If it fails then this test will fail, because __str__() is used in
    # the formatting of an exception.
    s.__str__()
    # Unicode and str should work as well.
    s.__unicode__()
    s.__str__()

# Generated at 2022-06-14 06:06:58.778647
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """Unit test for method __unicode__ of class IllegalUseOfScopeReplacer."""
    # Start off with the simplest case.
    e = IllegalUseOfScopeReplacer('pippo', 'pluto')
    # then make sure the message is a string
    assert isinstance(e.__unicode__(), unicode)
    # and that it is the same as str(e)
    assert e.__unicode__() == str(e)

test_IllegalUseOfScopeReplacer___unicode__.todo = (
    'The __unicode__ method needs to be tested on python versions prior'
    ' to 2.6 for the following:\n'
    ' - it returns the message as a unicode object;\n'
    ' - the message is the same as str(e).')


# Generated at 2022-06-14 06:07:04.564019
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    def test_factory(self, scope, name):
        scope[name] = 'test_string'
        return scope[name]
    scope = {}
    test_obj = ScopeReplacer(scope, test_factory, 'test_obj')
    assert test_obj() == 'test_string'
# End of test for method __call__ of class ScopeReplacer

# Generated at 2022-06-14 06:07:19.573133
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    try:
        from bzrlib.tests import TestCase
        import __builtin__
        import sys
    except ImportError:
        pass
    else:
        # __call__ is a method
        # _resolve is a method
        # _real_obj is an instance attribute
        # _scope is a data descriptor
        # _factory is a data descriptor
        # _name is a data descriptor
        try:
            testcase = TestCase.TestCase()
        except AttributeError:
            pass
        else:
            obj = ScopeReplacer({"temp_dictionary_var": "temp"}, __builtin__.str, "temp_dictionary_var")

# Generated at 2022-06-14 06:07:26.617752
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """Unit test for method __str__ of class IllegalUseOfScopeReplacer"""
    try:
        raise IllegalUseOfScopeReplacer('name', 'msg', 'extra')
    except IllegalUseOfScopeReplacer as e:
        assert(isinstance(str(e), str))
        assert(isinstance(repr(e), str))



# Generated at 2022-06-14 06:07:54.362579
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """Check the IllegalUseOfScopeReplacer's str"""
    e = IllegalUseOfScopeReplacer('foo', 'frob')
    msg = 'foo: frob'
    if e.__str__() != msg:
        raise AssertionError('expected:\n%s\nbut got:\n%s\n' %
            (msg, e.__str__()))



# Generated at 2022-06-14 06:08:01.465198
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """__str__ of IllegalUseOfScopeReplacer"""
    s = str(IllegalUseOfScopeReplacer('foo', 'a %(value)s', {'value': 'bar'}))
    if s != "ScopeReplacer object 'foo' was used incorrectly: a bar":
        raise AssertionError(s)

# Generated at 2022-06-14 06:08:10.873513
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    class A:
        pass
    def f(self, scope, name):
        return A()
    scope = {}
    obj = ScopeReplacer(scope, f, 'foo')
    assert 'foo' not in dir(obj)
    obj.bar = 'baz'
    assert 'bar' in dir(obj)
    assert obj.bar == 'baz'
    assert 'bar' in dir(A())
    assert A().bar == 'baz'
    assert dir(scope['foo']) == dir(A())
    assert scope['foo'].bar == 'baz'

# Generated at 2022-06-14 06:08:25.069656
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """Construct a IllegalUseOfScopeReplacer exception, serialize it
    to unicode and make sure it is correctly encoded.

    Test for http://pad.lv/779169, see that bug report for details.
    """
    # This exception message is intentionally not translated because
    # we want to test the default (english) case.
    exc = IllegalUseOfScopeReplacer('name', u'This is a unicode message')
    unicode(exc)
    return


# TODO: HP-UX does not have an implementation of getattr().
#   This is a temporary workaround that is similar to the one in osutils
#   (see bug #304909).
#   This can be removed once getattr() is implemented on HP-UX.

# Generated at 2022-06-14 06:08:36.758554
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """This test method was generated by testtools.

    If you want to add tests to this test case, add them to the test
    module, using the testtools syntax.
    """
    e = IllegalUseOfScopeReplacer('name', 'msg', extra='extra')
    result = unicode(e)
    # Ensure __unicode__() returns a unicode object
    assert isinstance(result, unicode)
    # Ensure __unicode__() returns a string containing some of the class
    # attributes
    assert result.find('name') >= 0
    assert result.find('msg') >= 0
    assert result.find('extra') >= 0

# Generated at 2022-06-14 06:08:43.136771
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """This method must return a str object, not a unicode object.
    """
    e = IllegalUseOfScopeReplacer('a', 'b', 'c')
    result = str(e)
    assert isinstance(result, str)
    assert not isinstance(result, unicode)



# Generated at 2022-06-14 06:08:51.236839
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    from .. import selftest
    from . import lazy_import
    test_obj = lazy_import.lazy_import(globals(), '''
        class TestScopeReplacer(object):
            def __init__(self, value):
                self.value = value
            def plus_one(self):
                return self.value + 1
        ''').TestScopeReplacer
    assert len(sys.modules) == selftest.prev_sys_modules_len + 1
    with lazy_import.ScopeReplacer(globals(), test_obj, 'test_obj') as obj:
        assert obj.value == 0
        assert obj.plus_one() == 1
    assert obj.value == 0
    assert obj.plus_one() == 1



# Generated at 2022-06-14 06:09:01.308380
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__ should return a unicode object.

    This is important because it will often be used to construct
    other unicode objects, e.g. in tracebacks.

    Also, for a newly created exception the content of the exception
    should be visible without having to decode the message.
    """
    e = IllegalUseOfScopeReplacer(name=u'e', msg=u'm')
    u = e.__unicode__()
    if not isinstance(u, unicode):
        raise AssertionError('must return unicode, not %r' %
                             (type(u),))
    # __unicode__() should always return a 'unicode' object
    # never a 'str' object.

# Generated at 2022-06-14 06:09:06.303902
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    import sys
    def myfactory(replacer, scope, name):
        return lambda: 'goodbye'
    scope = {}
    scope['scr'] = ScopeReplacer(scope, myfactory, 'scr')
    scope['scr']()

# Generated at 2022-06-14 06:09:15.991190
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    from bzrlib import lazy_import
    import gc
    # 2:Set a member of a ScopeReplacer object, checking that it
    # is proxied, and that the lazy object is replaced in the global scope.
    self.globs['lazy_import'] = lazy_import
    self.globs['gc'] = gc
    code = """\
    import sys
    scope = globals()
    name = '_ScopeReplacerObject'
    scope[name] = lazy_import.ScopeReplacer(
        scope, lambda s, sc, n: object(), name)
    object = scope[name]
    object.foo = 42
    gc.collect()
    """
    self.assertGlobalsEqual(self.globals_before, code)