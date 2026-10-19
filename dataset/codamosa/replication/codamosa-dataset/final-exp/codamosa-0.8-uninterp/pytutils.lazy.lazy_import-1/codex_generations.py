

# Generated at 2022-06-14 05:59:58.833296
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    # self is the class, so new should be called.
    from bzrlib.lazy_import import ScopeReplacer

    class Foo(object):
        pass

    foo = Foo()
    foo.x = 1
    assert foo.x == 1
    # but only if there is a field named 'x'
    foo2 = Foo()
    try:
        foo2.y = 2
    except AttributeError:
        pass
    else:
        raise AssertionError("should have raised AttributeError")



# Generated at 2022-06-14 06:00:08.498835
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    from bzrlib.tests import TestSkipped
    try:
        from importlib import import_module
    except ImportError:
        raise TestSkipped('Needs importlib')
    from bzrlib.lazy_import import ScopeReplacer, IllegalUseOfScopeReplacer
    def foo():
        pass
    ScopeReplacer({}, foo, 'bar')

# Generated at 2022-06-14 06:00:21.449040
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    from bzrlib.lazy_import import lazy_import
    def factory(self, scope, name):
        return 42
    # Create a new ScopeReplacer in the global scope.
    lazy_import(locals(), '''
    from bzrlib import (
        errors,
        osutils,
        branch,
        )
    import bzrlib.branch
    ''')
    # This should replace the module with 42.
    osutils.path.join(osutils.curdir(), 'foo')
    # Verify that it was replaced.
    try:
        object.__getattribute__(osutils, '_resolve')
    except AttributeError:
        pass
    except:
        raise AssertionError
    else:
        raise AssertionError

# Generated at 2022-06-14 06:00:29.674158
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    from bzrlib.lazy_import import ScopeReplacer

    class MyClass(object):
        def __init__(self, a, b, c=None):
            self.a = a
            self.b = b
            self.c = c

    def factory(self, scope, name):
        self.a = 'alpha'
        self.b = 'beta'
        return self

    my_instance = MyClass(None, None)
    scope = {}
    replacer = ScopeReplacer(scope, factory, 'my_instance')

    # replacement will happen
    assert my_instance.a == 'alpha'
    assert my_instance.b == 'beta'
    # there was no replacement
    assert my_instance.a is None
    assert my_instance.b is None

    replacer('carl', None)
   

# Generated at 2022-06-14 06:00:38.912954
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    # Basic setup
    _factory = object()
    _name = object()
    _real_obj = object()
    _scope = dict()
    obj = ScopeReplacer(_scope, _factory, _name)
    obj._ScopeReplacer__setattr__('_real_obj', _real_obj)

    # Call the tested method
    obj._ScopeReplacer__setattr__('_factory', _factory)

    # Check the results
    assert obj._ScopeReplacer__getattribute__('_factory') == _factory


# Generated at 2022-06-14 06:00:41.134265
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    from bzrlib.tests.test_lazy_import import test_ScopeReplacer___setattr__
    return test_ScopeReplacer___setattr__()

# Generated at 2022-06-14 06:00:53.709505
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """Method __str__ should return printable strings.

    For instance in doctest, the __str__ method should return a str with
    non-unicode characters.

    >>> raise IllegalUseOfScopeReplacer('foo', 'bar')
    Traceback (most recent call last):
      ...
    IllegalUseOfScopeReplacer: ScopeReplacer object 'foo' was used incorrectly: bar

    :returns: True if all tests succeed, False if any fails.
    """
    from bzrlib.tests import TestCase
    class TestCaseWithNastyEncoding(TestCase):
        """Subclass TestCase to be sure that doctest's stderr is utf-8"""
        _encoding = 'utf-8'

    from doctest import DocTestCase
    from bzrlib import lazy_import

# Generated at 2022-06-14 06:00:56.418710
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """IllegalUseOfScopeReplacer.__unicode__ must return a unicode object"""
    m = IllegalUseOfScopeReplacer('x', 'y')
    u = unicode(m)
    assert isinstance(u, unicode)

# Generated at 2022-06-14 06:01:01.450392
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """__str__ should return a str, not unicode"""
    e = IllegalUseOfScopeReplacer('name', 'msg')
    s = str(e)
    assert isinstance(s, str), "instance of %s is not a str: %r" % (
        e.__class__.__name__, s)



# Generated at 2022-06-14 06:01:06.885390
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """__str__ should return a str, not unicode"""
    e = IllegalUseOfScopeReplacer('foo', 'bar')
    s = str(e)
    if isinstance(s, unicode):
        raise AssertionError('Expected a str, got a unicode')


# Generated at 2022-06-14 06:01:28.752796
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """Unit test for method __unicode__ of class IllegalUseOfScopeReplacer"""
    e = IllegalUseOfScopeReplacer('replacer', 'not ready!')
    assert isinstance(unicode(e), unicode)
    # 'IllegalUseOfScopeReplacer' should be present in the message
    assert unicode(e).find('IllegalUseOfScopeReplacer') >= 0


# TODO: We probably need to have a better way of specifying the list of
# modules. It is a bit too easy to make typos. Eg rp was missing the 'b'
# Maybe this should be a string of some sort (json/yaml) that we parse in
# here. Or maybe it should be a list of (name, modpath) pairs.

# Generated at 2022-06-14 06:01:36.860098
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """IllegalUseOfScopeReplacer.__str__() should raise is self._fmt is not set"""
    class Foo(IllegalUseOfScopeReplacer):
        pass
    foo = Foo("name")
    e = assert_raises(AttributeError, getattr, foo, '_fmt')
    assert e.args[0] == "_fmt"
    # __str__() should always return a 'str' object, never a 'unicode' object.
    assert isinstance(str(foo), str)
    assert not isinstance(str(foo), unicode)


# Generated at 2022-06-14 06:01:48.758784
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__ of IllegalUseOfScopeReplacer"""
    import os
    import tempfile

    # unicode error object
    e = IllegalUseOfScopeReplacer('fake_name',
                                  'fake_message',
                                  'fake_extra')

    # unicode message
    e._preformatted_string = u'fake_message'
    assert e.__unicode__() == u'fake_message'

    # non unicode message
    e._preformatted_string = u'\xdd' # invalid UTF-8

# Generated at 2022-06-14 06:02:03.016439
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    from bzrlib.tests import TestCaseWithMemoryTransport

    class TestScopeReplacer(TestCaseWithMemoryTransport):

        def test___call__(self):
            # regression test for http://pad.lv/521151.
            from bzrlib.lazy_import import lazy_import, ScopeReplacer
            import bzrlib.tests
            lazy_import(locals(), """
            import bzrlib.tests
            """)
            test_code = "self.assertFalse(True)"
            # use a scope replacer to delay the import
            def _lazy_import_bzrlib__tests(replacer, scope, name):
                from bzrlib import (
                    tests,
                    )
                return tests

# Generated at 2022-06-14 06:02:05.781248
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """__str__ should work as expected"""
    exc = IllegalUseOfScopeReplacer('foo', 'bar')
    assert exc.__str__() == 'Illegal use of foo: bar'


# Generated at 2022-06-14 06:02:18.264183
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    from bzrlib.tests.lazy_import_implementation import import_module_to_scope
    from bzrlib.tests.lazy_import_implementation import Call_class
    # Simple test
    class A(Call_class):
        def __call__(self, *args, **kwargs):
            return 'A'
    scope = {}
    factory = lambda self, scope, name: A()
    name = 'a'
    obj = ScopeReplacer(scope, factory, name)
    # Test that __call__ works before self._resolve is run, and
    # that it works after
    import_module_to_scope(scope, 'A')
    assert obj() == 'A'
    assert obj() == 'A'



# Generated at 2022-06-14 06:02:25.690825
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    i = IllegalUseOfScopeReplacer('foo', 'bar', 'baz')
    s = unicode(i)
    # The format string
    assert '%(name)s' in unicode(IllegalUseOfScopeReplacer._fmt)
    # The format string with the name substituted
    assert unicode(IllegalUseOfScopeReplacer._fmt) % dict(name='foo') in s
    assert 'foo' in s
    assert 'bar' in s
    assert 'baz' in s



# Generated at 2022-06-14 06:02:37.923131
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    from bzrlib.lazy_import import lazy_import
    import bzrlib.errors as errors
    # Copy the dict for testing
    g = dict(globals())
    # We don't want sycoca_path to be set in the test environment
    del g['sycoca_path']
    lazy_import(g, '''
    from bzrlib import (
        errors,
        )
    ''')
    # Make sure that the import did not happen
    cur_errors = errors.UnsupportedOperation
    try:
        g['errors'] = None
        errors.UnsupportedOperation
    except AttributeError:
        pass
    else:
        raise AssertionError(
            "AttributeError not raised, importing already happened.")
    # Check that 'sycoca_path' is not in the scope of '

# Generated at 2022-06-14 06:02:45.374555
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    from bzrlib.lazy_import import lazy_import
    globals()['__builtins__'] = __builtins__
    lazy_import(globals(), '''
    from bzrlib import (
        osutils,
        )
    ''')
    # call osutils.open_zip_exclusive
    osutils.open_zip_exclusive(None, None)



# Generated at 2022-06-14 06:02:52.159960
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__ must return a unicode object"""
    e = IllegalUseOfScopeReplacer(None, None)
    u = unicode(e)
    assert isinstance(u, unicode), (
        "%s was not returned from __unicode__" % (type(u).__name__,))
test_IllegalUseOfScopeReplacer___unicode__.skip = True



# Generated at 2022-06-14 06:03:10.238197
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    # call __call__ of ScopeReplacer
    from bzrlib.lazy_import import lazy_import
    scope = {'original': object()}
    lazy_import(scope, 'x = original')
    scope['x']('a', b='b')



# Generated at 2022-06-14 06:03:15.881597
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    e = IllegalUseOfScopeReplacer('foo', 'bar', extra='baz')
    u = unicode(e)
    str(u)
    repr(u)
    # TODO: assert something about the string.
    # like that it starts with 'foo' or that it has the form
    # 'foo: bar: baz'?
    return u



# Generated at 2022-06-14 06:03:21.384015
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """__str__(IllegalUseOfScopeReplacer(name='x', msg='a', extra='b'))
    -> 'x: a: b'"""
    e = IllegalUseOfScopeReplacer('x', 'a', extra='b')
    assert str(e) == 'x: a: b'



# Generated at 2022-06-14 06:03:30.929081
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """Unit test for method __str__ of class IllegalUseOfScopeReplacer

    If a lossy conversion is attempted, a warning will be generated.
    See e.g. http://bzr.arbash-meinel.com/plugins/view_log_hook/index.html
    """
    import warnings
    warnings.simplefilter('ignore')
    # This test was generated because of
    # bzrlib.tests.blackbox.test_pull.TestPull.test_pull_and_commit_to_missing
    x = IllegalUseOfScopeReplacer(
        "foo",
        "execute_root",
        "'_execute' returned non-None")
    try:
        x.__str__()
    except UnicodeEncodeError:
        raise AssertionError("Lossy conversion attempted.")


# Generated at 2022-06-14 06:03:32.440485
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    pass # TODO



# Generated at 2022-06-14 06:03:40.215596
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """IllegalUseOfScopeReplacer.__str__()

    Test that __str__() works on IllegalUseOfScopeReplacer.
    """
    e = IllegalUseOfScopeReplacer('foo', 'msg')
    s = str(e)
    # str(e) must return a 'str', not a 'unicode'
    assert type(s) == type('')
    assert s == "IllegalUseOfScopeReplacer(u'foo', u'msg')"



# Generated at 2022-06-14 06:03:51.763276
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    from bzrlib.tests import TestCase
    import bzrlib
    # 1. Test that __call__ passes all args through
    def factory(self, scope, name):
        return lambda *args: args
    old_should_proxy = ScopeReplacer._should_proxy
    ScopeReplacer._should_proxy = True
    v = ScopeReplacer(globals(), factory, 'test_call_proxy')
    self.assertEqual((1,2), v(1,2))
    v = bzrlib.test_call_proxy
    self.assertEqual((3,4), v(3,4))
    ScopeReplacer._should_proxy = old_should_proxy
    # 2. Test that __call__ works if proxying is disabled
    def factory(self, scope, name):
        return lambda *args: args


# Generated at 2022-06-14 06:04:00.363111
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    from bzrlib.tests.test_lazy_import import _AssertCalled
    import bzrlib.tests.test_lazy_import
    called = _AssertCalled()
    def factory(self, scope, name):
        object.__setattr__(self, '_real_obj', called)
        return called
    scope = {}
    name = 'test'
    replacer = ScopeReplacer(scope, factory, name)
    obj = replacer()
    assert (called.called_with is None)
    assert (obj._called_with is None)



# Generated at 2022-06-14 06:04:11.956857
# Unit test for method __getattribute__ of class ScopeReplacer
def test_ScopeReplacer___getattribute__():
    """__getattribute__ calls on a ScopeReplacer should be forwarded to its attr if the object is resolved"""
    class Foo(object):
        def __init__(self, value=0):
            self.value = value
        def bar(self):
            return 1
        def __getattr__(self, factor):
            return self.value * factor
    def factory(repl, scope, name):
        return Foo(value=2)
    scope = {}
    name = 'foo'
    scope[name] = ScopeReplacer(scope, factory, name)
    assert scope[name].bar() == 1
    assert scope[name].spam == 4


# Generated at 2022-06-14 06:04:22.243718
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    # __setattr__ is implemented as __getattribute__ and then setattr,
    # only the second of which is accessible to test. Since it is
    # implemented in Python, we can access it directly to see what it
    # does.
    #
    # One important case is that __setattr__ should not be called when
    # the object is still initializing fields.
    from bzrlib.tests.test_lazy_import import (
        NoSelfAttributeError,
        )
    # We need to make a subclass for this to work.
    class SubScopeReplacer(ScopeReplacer):

        def __init__(self, scope, factory, name):
            # Note that _name is not initialised
            object.__setattr__(self, '_scope', scope)

# Generated at 2022-06-14 06:04:53.312330
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    class ScopeReplacerMock(ScopeReplacer):
        def __setattr__(self, attr, value):
            return ScopeReplacer.__setattr__(self, attr, value)
    ScopeReplacerMock._should_proxy = False
    name = '_name'
    attr = '_attr'
    value = '_value'
    real_obj = Mock()
    real_obj.__setattr__ = Mock()
    real_obj.__setattr__.return_value = value
    scope = {name: real_obj}
    def factory(self, scope, name):
        return real_obj
    srm = ScopeReplacerMock(scope, factory, name)
    srm.__setattr__(attr, value)

# Generated at 2022-06-14 06:04:56.143961
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)



# Generated at 2022-06-14 06:05:03.289955
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    # ScopeReplacer.__setattr__ is not a function, it is a method.
    # This test will check method __setattr__ of class ScopeReplacer
    # but it is not possible to call it like a function.
    # Call test_ScopeReplacer___setattr__ instead of
    # test_ScopeReplacer___setattr_.
    test_ScopeReplacer___setattr_(None)


# Generated at 2022-06-14 06:05:11.305427
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    import unittest

    import bzrlib.tests

    class TestCase(bzrlib.tests.TestCaseWithMemoryTransport):

        def test_empty_function(self):
            """Function that doesn't return anything."""
            def factory(self, scope, name):
                def empty_function():
                    pass
                return empty_function

            scope = {}
            name = 'empty_function'
            ScopeReplacer(scope, factory, name)
            self.assertRaises(TypeError, scope[name])

        def test_function(self):
            """Function that takes one argument"""
            def factory(self, scope, name):
                def empty_function(arg):
                    return 'I was called with: %r' % (arg,)
                return empty_function

            scope = {}
            name = 'empty_function'


# Generated at 2022-06-14 06:05:24.139468
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    def get_str(replacer):
        """Get str of a replacer. Used to avoid UnboundLocalError
        in the unit test."""
        return str(replacer)
    def get_repr(replacer):
        return repr(replacer)
    r = IllegalUseOfScopeReplacer('r', 'something went wrong')
    if get_repr(r) != "IllegalUseOfScopeReplacer(r)":
        raise AssertionError()
    if get_str(r) != "r: something went wrong":
        raise AssertionError()
    try:
        raise IllegalUseOfScopeReplacer(None, 'something went wrong')
    except Exception as e:
        if get_repr(e) != "IllegalUseOfScopeReplacer(None)":
            raise AssertionError()

# Generated at 2022-06-14 06:05:34.818198
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    # Note: This function is called within a try block to catch
    # anything that might be raised.  Return 'True' if you do not
    # want the exception (if any) to be trapped.
    #scope = {'__name__': 'foo'}
    #lazy_import(scope, '''
    #def foo():
    #    print "foo"
    #':        # <-- note the colon!
    #    pass
    #''')
    foo = scope['foo']
    foo.__setattr__('bar', 'baz')
    foo.bar == 'baz'
    del scope

# Generated at 2022-06-14 06:05:45.642590
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """This tests that IllegalUseOfScopeReplacer.__unicode__() can
    handle unicode and str values in self.__dict__.
    """
    from bzrlib import trace
    trace.mutter("Try to break IllegalUseOfScopeReplacer.__unicode__()")
    def check(**kwargs):
        e = IllegalUseOfScopeReplacer('foo', 'bar', kwargs)
        assert unicode(e)
    check(msg='\xa3')
    check(msg=u'\xa3')
    check(name='\xa3')
    check(name=u'\xa3')
    check(extra='\xa3')
    check(extra=u'\xa3')
    # check that it works if __init__() is passed strings or unicodes

# Generated at 2022-06-14 06:05:49.951408
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """IllegalUseOfScopeReplacer.__str__ should return the message"""
    e = IllegalUseOfScopeReplacer('foo', 'bar', 'baz')
    assert str(e) == 'bar: baz'

# Generated at 2022-06-14 06:06:01.276613
# Unit test for method __getattribute__ of class ScopeReplacer
def test_ScopeReplacer___getattribute__():
    import inspect
    import bzrlib.lazy_import
    from bzrlib.lazy_import import IllegalUseOfScopeReplacer

    # build fake test object
    s = ScopeReplacer({},'','')
    # check for functions
    for i in dir(ScopeReplacer):
        f = getattr(ScopeReplacer, i)
        if inspect.isfunction(f):
            # test function
            if i == 'test_ScopeReplacer___getattribute__':
                # skip recursive calls
                continue
            if i == '_resolve':
                # skip this one because it has side effects
                continue
            if i == '__getattribute__':
                # check __getattribute__()
                g = f(s, '_resolve')

# Generated at 2022-06-14 06:06:11.677916
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    """Unit test for method __setattr__ of class ScopeReplacer"""
    def __test_ScopeReplacer___setattr__():
        class C(object):
            pass
        import bzrlib
        old_should_proxy = ScopeReplacer._should_proxy

# Generated at 2022-06-14 06:06:41.477100
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """IllegalUseOfScopeReplacer.__str__() should return a string."""
    IE = IllegalUseOfScopeReplacer('name', 'msg')
    result = str(IE)
    # Check that the result is a str object, not a unicode object.
    if not isinstance(result, str):
        raise AssertionError('IllegalUseOfScopeReplacer.__str__() expected to'
                             ' return a str, got %r' % (result,))

# Generated at 2022-06-14 06:06:45.804689
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__ must return a unicode string."""
    e = IllegalUseOfScopeReplacer('name', 'msg', 'extra')
    u = e.__unicode__()
    assert isinstance(u, unicode)
    assert u == u'ScopeReplacer object \'name\': msg: extra'


# Generated at 2022-06-14 06:06:57.943989
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """str(X) should return ascii and never raise UnicodeError"""
    # Check that str() can always be applied.
    # This is a regression test for http://bugs.launchpad.net/bzr/+bug/553580
    # The test is needed because _fmt is an ascii string but the object may
    # get unicode string attributes.
    import sys
    class unicodeattribs(object):
        # __unicode__() is missing, so calling str() will raise UnicodeError.
        def __init__(self):
            # Emulate unicode string attributes.
            self.unicode = u'a'
    inst = unicodeattribs()

# Generated at 2022-06-14 06:07:02.994448
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__ of IllegalUseOfScopeReplacer"""
    e = IllegalUseOfScopeReplacer('name', 'message')
    # Note: unicode(e) works too
    u = e.__unicode__()
    assert isinstance(u, unicode)
    assert unicode(e) == u

# Generated at 2022-06-14 06:07:10.155013
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__ should return a unicode object

    Any kind of object is passed to the __unicode__ method, but it must
    return a unicode object.
    """
    msg = 'test message'
    obj = IllegalUseOfScopeReplacer('name', msg)
    result = unicode(obj)
    if not isinstance(result, unicode):
        raise AssertionError('__unicode__ did not return a unicode object')



# Generated at 2022-06-14 06:07:19.571856
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    class Test(ScopeReplacer):
        def __init__(self, *a, **kw):
            ScopeReplacer.__init__(self, *a, **kw)
    from bzrlib import osutils
    test_dict = dict()
    test_obj = Test(test_dict, osutils, 'test_obj')
    test_obj.new_attribute = '1'
    try:
        raise test_dict['test_obj']
    except OSError:
        pass


# Generated at 2022-06-14 06:07:28.880996
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    import imp
    def isopen(name):
        try:
            file = open(name)
        except IOError:
            return False
        else:
            file.close()
            return True
    # Local test to ensure ScopeReplacer can be given module name and 
    # import of module is done when created, not before.
    mod_name = 'bzrlib.lazy_import'
    scope = {}
    def factory(replacer, scope, name):
        return imp.load_module(name, *imp.find_module(name))
    # remove any module that may have been loaded in previous tests.
    if mod_name in sys.modules:
        del sys.modules[mod_name]
    # verify no .pyc file exists.
    mod_name_pyc = mod_name.replace('.', '/')

# Generated at 2022-06-14 06:07:39.065632
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    def func(arg1, arg2, kwarg1=None, kwarg2=None):
        return (arg1, arg2, kwarg1, kwarg2)

    def factory(obj, scope, name):
        return func

    scope = {'__name__': 'test', '__file__': 'test.py'}
    obj = ScopeReplacer(scope, factory, name='func')
    try:
        e = str(func)
    except TypeError:
        # In Python 3 str() doesn't accept default arguments.
        expected = "('x', 'y', None, None)"
    else:
        expected = "('x', 'y', None, 'z')"
    r = obj('x', 'y', kwarg2='z')
    s = str(r)

# Generated at 2022-06-14 06:07:42.863994
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """Unit test for IllegalUseOfScopeReplacer.__unicode__()"""
    exc = IllegalUseOfScopeReplacer('foo', 'bar')
    assert str(exc) == "foo was used incorrectly: bar"


# Generated at 2022-06-14 06:07:47.423430
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """__str__ should return a str."""
    x = IllegalUseOfScopeReplacer('name', 'msg')
    s = type(str())
    assert isinstance(str(x), s)
# TODO: Add unit test for __unicode__.

# Generated at 2022-06-14 06:08:20.040088
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    import bzrlib, bzrlib.errors
    import sys

    def run_test(scope, factory, name, attr, value):
        replacer = bzrlib.lazy_import.ScopeReplacer(scope, factory, name)
        if type(value) == str:
            exc = None
        elif type(value) == Exception:
            exc = value
            value = None
        # must raise TypeError when value is not string
        if type(attr) != str:
            replacer.__setattr__(attr, value)
        # must raise IllegalUseOfScopeReplacer when attr is '_resolve'
        replacer.__setattr__('_resolve', value)
        # must raise IllegalUseOfScopeReplacer when ScopeReplacer._should_proxy is False
        bzrlib.lazy_

# Generated at 2022-06-14 06:08:30.514927
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
 
    
    import sys
    def test_stderr(msg):
        sys.stderr.write(msg)
    test_stderr("""test_ScopeReplacer___call__:         1/12""")
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    module = lazy_import_module(name='bzrlib.tests.blackbox', debug_text='bzrlib.tests.blackbox', filepath='/home/vila/dev/bzrlib/bzrlib/tests/blackbox.py')
    
    
    
    
    
    

    
    
    
    
    skip_unless_Alive = module.skip_unless_Alive
    
    
    
    import bzrlib



# Generated at 2022-06-14 06:08:42.520966
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    def check(name, msg, extra=None):
        err = IllegalUseOfScopeReplacer(name, msg, extra)
        if extra:
            u = u"ScopeReplacer object '%s' was used incorrectly: %s: %s" \
                % (name, msg, extra)
        else:
            u = u"ScopeReplacer object '%s' was used incorrectly: %s" \
                % (name, msg)
        if u != err.__unicode__():
            raise AssertionError("Should have returned '%s' but got '%s'" \
                % (u, err.__unicode__()))
    check(u'test_name', u'test_msg', u'test_extra')
    check(u'test_name_2', u'test_msg')

# Generated at 2022-06-14 06:08:48.591846
# Unit test for method __getattribute__ of class ScopeReplacer
def test_ScopeReplacer___getattribute__():
    class Xyz(object):
        pass
    x = Xyz()
    x.foo = 'bar'
    y = ScopeReplacer(None, None, 'x')
    z = y._resolve()
    z.foo = 'baz'
    eq(x.foo, 'baz')


# Generated at 2022-06-14 06:09:00.173228
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """__str__() of IllegalUseOfScopeReplacer"""
    class Foo(IllegalUseOfScopeReplacer):
        _fmt = '_fmt %(msg)s%(extra)s'
    m = Foo('name_of_foo', 'message_of_foo')
    assert_equal("_fmt message_of_foo", str(m))
    m = Foo('name_of_foo', 'message_of_foo', 'extra_of_foo')
    assert_equal("_fmt message_of_foorextra_of_foo", str(m))
    m = Foo('name_of_foo', 'message_of_foo', 'extra_of_foo')
    m.__dict__['_fmt'] = '_fmt %(msg)s%(extra)s + %(abc)s'


# Generated at 2022-06-14 06:09:13.045137
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    import sys
    import traceback
    from bzrlib.lazy_import import (
        IllegalUseOfScopeReplacer,
        )
    if sys.version_info[0] == 3:
        e = lambda x: bytes(x, 'utf-8')
    else:
        e = lambda x: x
    try:
        raise IllegalUseOfScopeReplacer('foo', 'test1')
    except IllegalUseOfScopeReplacer as ex:
        tb = traceback.extract_exception(ex.__class__, ex, None)
        # This string is transcoded from utf-8 to local encoding

# Generated at 2022-06-14 06:09:22.193299
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    import bzrlib.lazy_import
    bzrlib.lazy_import._extra_scope = {}

# Generated at 2022-06-14 06:09:31.098537
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    from bzrlib.tests.blackbox import ExternalBase
    from bzrlib.lazy_import import lazy_import
    def _factory(self, scope, name):
        scope.pop(name, None)
        scope[name] = ExternalBase()
        return scope[name]
    globs = {}
    lazy_import(globs, """
    from bzrlib.tests.blackbox import ExternalBase
    test_instance = None
    """)
    test_instance = ScopeReplacer(globs, _factory, 'test_instance')
    test_instance.run_bzr(['--no-plugins', 'help'])
