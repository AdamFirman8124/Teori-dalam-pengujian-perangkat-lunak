

# Generated at 2022-06-14 05:59:56.204706
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    e = IllegalUseOfScopeReplacer('foo', 'No, no, no', '\nbar')
    u = unicode(e)
    assert isinstance(u, unicode)

# Generated at 2022-06-14 06:00:02.848053
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    import bzrlib.tests
    output = bzrlib.tests.run_doctest(bzrlib.lazy_import)
    if output.find("Failed doctest test for bzrlib.lazy_import.ScopeReplacer.__call__") != -1:
        raise Exception("Method __call__ of class ScopeReplacer in module lazy_import failed")


# Generated at 2022-06-14 06:00:14.096463
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    import __future__
    import bzrlib
    import bzrlib.branch
    import bzrlib.errors
    import bzrlib.osutils
    real_import = __builtin__.__import__
    __builtin__.__import__ = type(__builtin__.__import__)(
            __future__.absolute_import.__name__,
            __future__.absolute_import.__doc__,
            __future__.absolute_import.__dict__)
    __builtin__.__import__.__code__ = (
            __future__.absolute_import.__code__)
    scope = {
        'bzrlib': ScopeReplacer(scope, lambda s, scope, name: scope, 'bzrlib'),
    }
    scope['bzrlib']._resolve

# Generated at 2022-06-14 06:00:24.799696
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """__str__ should always return a 'str' object, never a 'unicode' object.
    __str__ should always return a valid str, even if _get_format_string
    returns a broken string.
    """
    # Test 1, __getitem__ in _get_format_string
    class TestIllegalUseOfScopeReplacer(IllegalUseOfScopeReplacer):
        _fmt = "%(foo)[1]"
    e = TestIllegalUseOfScopeReplacer('foo', 'bar', 'extra')
    # __str__ should return a valid str
    assert e.__str__() == "Unprintable exception TestIllegalUseOfScopeReplacer: dict=%r, fmt=%r, error=%r" % (e.__dict__, e._fmt, None)

    # Test 2, returns unicode
    e

# Generated at 2022-06-14 06:00:38.040713
# Unit test for method __getattribute__ of class ScopeReplacer
def test_ScopeReplacer___getattribute__():
    """test for method __getattribute__ of class ScopeReplacer"""
    import __builtin__
    try:
        __builtin__.__dict__.pop('__getattribute__', None)
        global getattr
        getattr = object.__getattribute__
        import bzrlib.lazy_import as lazy_import_module
        from bzrlib.lazy_import import ScopeReplacer
        from bzrlib.lazy_import import IllegalUseOfScopeReplacer
    except:
        del __builtin__.__dict__['__getattribute__']
        raise
    # test for AttributeError:
    # scope = __builtin__.__dict__ # scope of this function
    scope = {}
    scope["__name__"] = "__main__"
    scope["__doc__"] = None

# Generated at 2022-06-14 06:00:40.860552
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    from bzrlib.tests.test_lazy_import import Case
    # Method __call__ of ScopeReplacer
    raise NotImplementedError(Case.id())


# Generated at 2022-06-14 06:00:53.668354
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """Method __unicode__ of class IllegalUseOfScopeReplacer"""
    class FooError(IllegalUseOfScopeReplacer):
        _fmt = "Foo: %(msg)s"
    foo = FooError('baz', 'msg')
    unicode(foo)

# Generated at 2022-06-14 06:00:56.390327
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """IllegalUseOfScopeReplacer.__str__() should return a str object"""
    e = IllegalUseOfScopeReplacer('name', 'message', 'extra')
    assert isinstance(e.__str__(), str)



# Generated at 2022-06-14 06:00:59.596014
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    test_result = True
    try:
        #
        # __setattr__ can't be called directly
        #
        pass
    except:
        traceback_passed = False
    else:
        traceback_passed = True
    test_result = (test_result and traceback_passed)
    #
    # __setattr__ can't be called directly
    #
    return test_result


# Generated at 2022-06-14 06:01:01.377909
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    obj = ScopeReplacer({}, None, "")
    # no exception raised
    obj.__setattr__("", 1)


# Generated at 2022-06-14 06:01:17.596795
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    from bzrlib.tests import TestCase
    from bzrlib.lazy_import import ScopeReplacer

    class TestScopeReplacer(TestCase):

        def assert_scope_replacer(self, scope_replacer, name):
            self.assertIsInstance(scope_replacer, ScopeReplacer)
            self.assertEqual(scope_replacer._name, name)
            self.assertIsNone(scope_replacer._real_obj)

    def test_dummy(self):
        # Just to cover everything.
        return

    def test_ScopeReplacer_uses_scope_and_factory():
        # ScopeReplacer() instantiates with a scope, factory and name.
        scope = {}
        def factory(self, scope, name):
            return object()
        name = 'name'

# Generated at 2022-06-14 06:01:23.101282
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    import sys
    import bzrlib
    __pychecker__ = 'no-classattr'
    class Foo(object):
        pass
    class Bar(object):
        pass
    foo = Foo()
    bar = Bar()
    baz = ScopeReplacer(sys.modules, lambda placeholder, scope, name: foo,
                        'bzrlib.foo')
    baz.attribute1 = bar
    assert foo.attribute1 is bar

# Generated at 2022-06-14 06:01:26.650187
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    from bzrlib import osutils
    assert osutils.file_kind('/') == 'directory' # sanity

# Generated at 2022-06-14 06:01:37.612487
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    from inspect import getargspec
    from testtools import TestCase
    from testtools.matchers import Equals, HasLength
    from bzrlib.tests import TestSkipped
    argspec = getargspec(ScopeReplacer.__setattr__)
    if argspec.args is None or argspec.varargs is not None:
        raise TestSkipped('%s.%s method has a variable number of arguments.'
                          % (ScopeReplacer.__class__.__name__,
                             '__setattr__'))
    if argspec.keywords is not None:
        raise TestSkipped('%s.%s method has a variable number of keyword'
                          ' arguments.' % (ScopeReplacer.__class__.__name__,
                                           '__setattr__'))

# Generated at 2022-06-14 06:01:48.563458
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """__str__() should convert a UnicodeEncodeError to an ascii string

    It should also convert a UnicodeEncodeError within a UnicodeEncodeError
    to an ascii string.
    """
    # this test is a bit hard to understand because we need to raise
    # a UnicodeEncodeError *in* the method __str__ of the exception
    try:
        raise IllegalUseOfScopeReplacer('x', 'is unknown', '%5d' % 0x80)
    except IllegalUseOfScopeReplacer as e:
        s = e.__str__()
        assert not isinstance(s, unicode)
        assert 'Unprintable exception IllegalUseOfScopeReplacer' in s



# Generated at 2022-06-14 06:02:02.755759
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    from bzrlib.tests import TestCase

    # Create a scope for the lazy import
    scope = {}

    # Define the lazy import
    lazy_import(scope, '''
    from bzrlib import (
        errors,
        osutils,
        branch,
        lazy_import,
        )
    ''')

    class MyTestCase(TestCase):

        def test_scope_replacer(self):
            # Prove that access to the module's errors object works
            self.assertTrue(hasattr(errors, 'BzrError'))

            # Prove that assignment works
            errors.Foo = "bar"
            self.assertEqual("bar", errors.Foo)

    # Create the test object and run the tests
    import doctest
    doctest.testmod()



# Generated at 2022-06-14 06:02:07.714397
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__ should produce a unicode string"""
    e = IllegalUseOfScopeReplacer('unittest', 'Testing', [1,2,3,4])
    u = e.__unicode__()
    if not isinstance(u, unicode):
        raise AssertionError('__unicode__ did not produce a unicode')



# Generated at 2022-06-14 06:02:20.524702
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    from unittest import TestCase
    from unittest import makeSuite


    class _MockScope(dict):

        def __init__(self):
            dict.__init__(self)
            self.passed_args = []

        def _factory(self, proxy, scopedict, name):
            self.passed_args.append((proxy, scopedict, name))
            return proxy

    class _TestCase(TestCase):

        def test_set_attribute_in_scope(self):
            from bzrlib.lazy_import import ScopeReplacer
            scope = _MockScope()
            sr = ScopeReplacer(scope, scope._factory, 'some_obj')
            self.assertEqual([], scope.passed_args)
            sr.some_attr = 'new_value'
           

# Generated at 2022-06-14 06:02:27.651606
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    from bzrlib.lazy_import import lazy_import
    from bzrlib import errors
    from bzrlib import osutils
    from bzrlib import branch
    import bzrlib.branch
    ScopeReplacer._should_proxy = True
    bzrlib.branch.ScopeReplacer._should_proxy = True

    # tests error raised if object has already been replaced
    ScopeReplacer._should_proxy = False
    bzrlib.branch.ScopeReplacer._should_proxy = False

# Generated at 2022-06-14 06:02:38.636126
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    # method __call__ of class ScopeReplacer
    # called with arguments: ()
    # called with arguments: (1,)
    # called with arguments: (1, 2)
    # called with arguments: (1, 2, 3)
    # called with arguments: (1, 2, 3, a=4)
    # called with arguments: (1, 2, 3, a=4, b=5)
    # called with arguments: (1, a=4, b=5, c=6)
    # called with arguments: (1, 2, a=4, b=5, c=6)
    # called with arguments: (a=4, b=5, c=6)
    global calls
    calls += 1
    return True
calls = 0

# Generated at 2022-06-14 06:02:51.920925
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """Test that __unicode__ can handle an object like IllegalUseOfScopeReplacer."""
    obj = IllegalUseOfScopeReplacer("name", "msg")
    _ = unicode(obj)



# Generated at 2022-06-14 06:02:57.786692
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    # prepare test data
    import bzrlib
    from bzrlib.trace import mutter, note
    from bzrlib.tests import TestCase
    import osutils

    class bzrlib_Error(Exception):
        """Non-fatal problem that should be reported to the user."""

    class bzrlib_OSUtils_PathTooLong(bzrlib_Error):
        _fmt = "Path too long: %(path)r"
        def __init__(self, path):
            super(bzrlib_Error, self).__init__(path)

    class bzrlib_tests_TestCase(TestCase):
        def assertFails(self, func, *args, **kwargs):
            self.assertRaises(AssertionError, func, *args, **kwargs)



# Generated at 2022-06-14 06:03:02.556012
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    """tests that the case of an object not calling the _factory callable
    happens without raising errors, and that it works as expected if
    it calls it.
    """
    scope = {}
    class C(object):
        def __init__(self):
            pass
    def factory(self, scope, name):
        # return without constructing a new object
        return self
    sr = ScopeReplacer(scope, factory, 'name')
    assert scope['name'] is sr
    assert scope['name'].__class__ is C
    assert scope['name'] is sr


# Generated at 2022-06-14 06:03:12.196772
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """__str__ should always work, even if _format fails badly"""
    x = IllegalUseOfScopeReplacer('test_name', 'test_msg')
    x._get_format_string = lambda: None
    x._format = lambda: ''[1:]
    x.__str__()
    # The following should fail, but not raise an exception to prevent
    # the unit test suite from failing. (It should be fixed when the
    # unit test is run in a debugger).
    # x._fmt = None
    # x._get_format_string = lambda: None
    # x._format = lambda: ''[1:]
    # x.__str__()
    # del x._fmt



# Generated at 2022-06-14 06:03:26.012080
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    from bzrlib.tests import TestCase
    from bzrlib.lazy_import import (
        ScopeReplacer,
        IllegalUseOfScopeReplacer,
        )

    class TestObj(object):
        _foo = None
        def __init__(self, foo=None):
            self._foo = foo
        def __setattr__(self, attr, value):
            if attr == '_foo':
                self.__dict__['_foo'] = value
            else:
                raise IllegalUseOfScopeReplacer(
                    attr, msg="Cannot set attributes other than _foo",
                    extra=dir(self))


# Generated at 2022-06-14 06:03:36.398760
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    from weakref import ref
    from bzrlib.tests import TestCase
    from bzrlib.lazy_import import ScopeReplacer
    class ScopeReplacerTest(TestCase):

        def test___setattr__(self):
            # __setattr__ sets attributes on the object which it is replacing.
            class X(object):
                pass

            def factory(replacer, scope, name):
                # We create an object, and replace ourselves with it
                # and return it.
                x = X()
                object.__setattr__(replacer, '_real_obj', x)
                # We need to explicitly put it in the scope, because if we
                # return self we will be left containing a copy of it
                # which is unnecessary.
                scope[name] = x
                return x


# Generated at 2022-06-14 06:03:39.247725
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """IllegalUseOfScopeReplacer.__str__()"""
    e = IllegalUseOfScopeReplacer('x', "hi!")
    str(e)
    unicode(e)



# Generated at 2022-06-14 06:03:49.644401
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    import bzrlib.lazy_import
    bzrlib.lazy_import.ScopeReplacer._should_proxy = False
    try:
        import os
        a = bzrlib.lazy_import.ScopeReplacer.__new__(
            bzrlib.lazy_import.ScopeReplacer)
        a._scope = {'os': a}
        a._name = 'os'
        a._real_obj = None
        os.path.expanduser('~')
    finally:
        bzrlib.lazy_import.ScopeReplacer._should_proxy = True



# Generated at 2022-06-14 06:04:02.285655
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    """ScopeReplacer.__setattr__"""
    from bzrlib.lazy_import import lazy_import
    from bzrlib.ui.text import TextUI
    def _add_import(scope, name, module, *args):
        lazy_import(scope, 'from %s import %s' % (module, ', '.join(args)))
    globals()['_add_import'] = _add_import
    lazy_import(globals(), '''
    import bzrlib
    from bzrlib.option import Option
    ''')
    # this should not raise an exception with the current proxy behavior
    ui_options = [(Option('test', '', type=int, help='test'), _add_import),]

# Generated at 2022-06-14 06:04:05.751514
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """__str__ must return a str"""
    e = IllegalUseOfScopeReplacer(1,'a')
    # if __str__ returns a unicode object, an exception is raised
    str(e)



# Generated at 2022-06-14 06:04:32.207739
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    # test_ScopeReplacer___setattr__()
    
    # __call__()
    # __getattribute__()
    # __init__()
    # __setattr__()
    # _resolve()
    # _should_proxy
    
    
    r = ScopeReplacer({}, lambda x, y, z: x, 'x')
    # simple setattr
    r.l = 'l'
    (r.l, r.l) == ('l', 'l')
    # via __dict__
    r.__dict__['l'] = 'l'
    (r.l, r.l) == ('l', 'l')
    # dict setitem
    r.__dict__['l'] = 'l'
    (r.l, r.l) == ('l', 'l')
    # object.__

# Generated at 2022-06-14 06:04:39.404285
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    class O(object):
        def __init__(self, x):
            object.__setattr__(self, '_x', x)
        def __getattribute__(self, attr):
            if attr == '_x':
                return object.__getattribute__(self, '_x')
            raise AttributeError(attr)
        def __setattr__(self, attr, value):
            if attr == '_x':
                object.__setattr__(self, '_x', value)
            else:
                raise AttributeError(attr)
        def __call__(self, *args, **kwargs):
            return self._x + 1

    x = ScopeReplacer({}, lambda sr, s, n: O(100), 'x')
    eq(x._x, 100)

# Generated at 2022-06-14 06:04:51.844037
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """IllegalUseOfScopeReplacer.__unicode__()

    returns a unicode object.
    """
    import sys

    # The standard Error classes have __str__ and __repr__ methods, which
    # return a str object by default. In future it is expected that the
    # standard Error classes will have a __unicode__ method and that the
    # __str__ and __repr__ methods will return a unicode object by default.
    # Until that happens, this test checks that the __unicode__ method of
    # IllegalUseOfScopeReplacer returns a unicode object by default.

    # We have to check for Python version 'cause the format for the message
    # changed in Python 2.6.

# Generated at 2022-06-14 06:05:05.485769
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    """__setattr__ must throw an error when trying to set members after
    it has been resolved"""
    def make_foo():
        class foo(object):
            pass
        return foo
    from bzrlib.lazy_import import ScopeReplacer
    name = 'foo'
    fake_scope = {name:ScopeReplacer(fake_scope, make_foo, name)}
    obj = fake_scope[name]
    obj.x = 'contents'
    import sys
    if sys.version_info[:2] >= (2, 5):
        e = IllegalUseOfScopeReplacer(name, msg="Object already replaced, did"
            " you assign it to another variable?", extra=obj.x)

# Generated at 2022-06-14 06:05:11.943165
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    from bzrlib.tests import TestCaseWithMemoryTransport
    import bzrlib.branch

    class TestScopeReplacer(TestCaseWithMemoryTransport):

        def test_ScopeReplacer___setattr___after_resolution(self):
            # __setattr__ raises IllegalUseOfScopeReplacer if _should_proxy is
            # False and the object has already been resolved.
            ScopeReplacer._should_proxy = False
            # restore bzrlib.branch.Branch.open behavior
            scope = locals()
            scope["bzrlib"] = bzrlib
            factory = bzrlib_branch_open
            name = "bzrlib_branch_open"
            replacer = ScopeReplacer(scope, factory, name)

# Generated at 2022-06-14 06:05:16.617643
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """IllegalUseOfScopeReplacer.__unicode__ works"""
    e = IllegalUseOfScopeReplacer('name', 'msg', 1)
    s = unicode(e)
    assert isinstance(s, unicode)

# Generated at 2022-06-14 06:05:26.574150
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    # See http://bugs.python.org/issue1340
    # This test is to ensure that the ScopeReplacer does not fail with this
    # bug when the real object has an __setattr__ method (since it has to
    # ensure that its own cases are still handled correctly -- see also
    # ScopeReplacer.__setattr__).
    class C(object):
        def __init__(self):
            self.foo = dict()
            self.bar = dict()
        def __setattr__(self, attr, value):
            if attr in ('foo', 'bar'):
                object.__setattr__(self, attr, value)
    scope = dict()
    lazy_proxy = ScopeReplacer(scope, lambda x,y,z: C(), 'obj')
    lazy_proxy.foo['baz'] = 10


# Generated at 2022-06-14 06:05:33.713319
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """Test __str__ method of class IllegalUseOfScopeReplacer."""
    obj = IllegalUseOfScopeReplacer('me', 'hi')
    if not isinstance(obj.__str__(), str):
        raise TestNotApplicable(
            "__str__ of IllegalUseOfScopeReplacer did not return a string")
test_IllegalUseOfScopeReplacer___str__.unittest = ['.errors']



# Generated at 2022-06-14 06:05:44.836820
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    from bzrlib.tests import TestCase
    from bzrlib.lazy_import import ScopeReplacer

    class Foo(object):
        pass
    foo = Foo()
    from cStringIO import StringIO
    out = StringIO()
    foo.stdout = out
    class Bar(ScopeReplacer):
        pass
    bar = Bar(locals(), lambda s, scope, name: foo, 'bar')
    bar.stdout.write('Hello world\n')
    TestCase().assertEqual('Hello world\n', out.getvalue())
    # Intentionally use the real object, so that the proxy object
    # is not used
    foo.stdout.write('Hello again\n')
    import sys
    TestCase().assertEqual('Hello world\nHello again\n', out.getvalue())



# Generated at 2022-06-14 06:05:49.066201
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    e = IllegalUseOfScopeReplacer('name', 'msg')
    assert unicode(e) == 'ScopeReplacer object \'name\': msg'

# Generated at 2022-06-14 06:06:05.767181
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """__str__ of IllegalUseOfScopeReplacer"""
    e = IllegalUseOfScopeReplacer('self.name', 'self.msg', 'self.extra')
    assert str(e) == "ScopeReplacer object 'self.name' was used incorrectly:"\
        " self.msg: self.extra"
    assert unicode(e) == u"ScopeReplacer object 'self.name' was used incorrectly:"\
        u" self.msg: self.extra"

# Generated at 2022-06-14 06:06:19.048833
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    from bzrlib._lazy_import_behaviour_helper import _set_method_to_dict
    _set_method_to_dict()
    class Dummy:
        def __getattr__(self, name):
            """Get an attribute, returning a description of the attribute."""
            return "<%s>" % name
    obj = Dummy()
    test = IllegalUseOfScopeReplacer('foo', 'bad')
    test.bad_obj = obj
    expected = '<IllegalUseOfScopeReplacer> object <foo> was used incorrectly: <bad>'
    if str(test) != expected:
        raise AssertionError(
            'str(test) != expected\n'
            'got: %r\n'
            'expected: %r' % (str(test), expected))

# Generated at 2022-06-14 06:06:28.193494
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """test method __str__ of class IllegalUseOfScopeReplacer"""
    e = IllegalUseOfScopeReplacer('name', 'msg', 'extra')
    e._fmt = "This %(name)r is %(msg)r."
    r = repr(e)
    assert r.endswith(", name='name', msg='msg', extra='extra')")
    assert unicode(e) == u"This 'name' is 'msg'."
    assert str(e) == "This 'name' is 'msg'."

# Generated at 2022-06-14 06:06:41.855981
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    from doctest import testmod
    if testmod()[0] == 0:
        import unittest
        import __builtin__

        class TestScopeReplacer(unittest.TestCase):
            def tearDown(self):
                super(TestScopeReplacer, self).tearDown()
                self.s = None

            def test___call__(self):
                import bzrlib
                # quick check that we can call the real method.
                __builtin__.__dict__['sys'] = None

                def make_real_obj(replacer, scope, name):
                    # If a module is already loaded, don't fail.
                    if 'sys' in scope and scope['sys'] is not None:
                        return scope['sys']
                    return __import__('sys')


# Generated at 2022-06-14 06:06:54.249994
# Unit test for method __getattribute__ of class ScopeReplacer
def test_ScopeReplacer___getattribute__():
    from bzrlib.tests import TestCase
    from bzrlib.lazy_import import ScopeReplacer

    class Dummy(object):
        pass

    class TestScopeReplacer(TestCase):

        def setUp(self):
            super(TestScopeReplacer, self).setUp()
            class Dummy(object):
                pass
            self.dummy = Dummy()

        def _make_replacer(self):
            return ScopeReplacer({}, lambda obj, scope, name: self.dummy,
                'dummy')

        def test__getattribute__(self):
            dummy = self.dummy
            dummy.foo = 'foo'
            repl = self._make_replacer()
            self.assertEquals('foo', repl.foo)


# Generated at 2022-06-14 06:07:05.537153
# Unit test for method __setattr__ of class ScopeReplacer

# Generated at 2022-06-14 06:07:08.423686
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    u = unicode(IllegalUseOfScopeReplacer('foo', 'bar'))
    if isinstance(u, str):
        u.decode('ascii')
    else:
        u.encode('ascii')


# Generated at 2022-06-14 06:07:13.524454
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__() should return a unicode object with the expected value."""
    foo = IllegalUseOfScopeReplacer('bar', 'baz', 'qux')
    foo_unicode = unicode(foo)
    assert isinstance(foo_unicode, unicode)



# Generated at 2022-06-14 06:07:24.162457
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """When __str__ is called on an IllegalUseOfScopeReplacer object, it must
    return a str.
    """
    import bzrlib
    old_locale = bzrlib._get_default_encoding() or 'C'
    bzrlib.set_user_encoding('utf8')
    e = IllegalUseOfScopeReplacer(u'name', u'foo')
    try:
        s = str(e)
    finally:
        bzrlib.set_user_encoding(old_locale)
    assert isinstance(s, str)
test_IllegalUseOfScopeReplacer___str__.__doc__ = \
    str(test_IllegalUseOfScopeReplacer___str__.__doc__)



# Generated at 2022-06-14 06:07:33.069941
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    """Unit test for method __setattr__ of class ScopeReplacer

    This test is designed to be run from the bzrlib.tests.test_lazy_import
    suite.
    """
    from bzrlib.tests.blackbox import ExternalBase
    from bzrlib.lazy_import import ScopeReplacer
    class Test(object):
        def __init__(self, a, b):
            self.a = a
            self.b = b
    class TestCase(ExternalBase):
        def setUp(self):
            ExternalBase.setUp(self)
            self.scope = {}
            self.factory = lambda o, s, n: Test(42, None)
            self.name = 'top_level'
    s = TestCase()
    s.setUp()

# Generated at 2022-06-14 06:07:46.049187
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    import doctest
    import bzrlib.tests.blackbox.test_lazy_import
    return doctest.DocTestSuite(bzrlib.tests.blackbox.test_lazy_import)

# Generated at 2022-06-14 06:07:53.071401
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """convert to str('str')"""
    self = IllegalUseOfScopeReplacer('', '')
    self.__dict__['foo'] = 'bar'
    self.__dict__['who'] = 'who'
    self.__dict__['_fmt'] = "%(who)s is a %(foo)s"
    self.__dict__['_preformatted_string'] = None
    s = str(self)
    assert s == 'who is a bar'



# Generated at 2022-06-14 06:08:04.712012
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    class _Object(object):
        __slots__ = ('_attr',)

        def __init__(self):
            self._attr = None

    def _factory(replacer, scope, name):
        return _Object()

    scope = {}
    replacer = ScopeReplacer(scope, _factory, 'my_obj')

    replacer._should_proxy = False
    replacer.attr = 1
    assert replacer._real_obj is not None

    replacer._should_proxy = True
    replacer.attr = 2
    assert replacer._real_obj is not None

# Generated at 2022-06-14 06:08:09.746997
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """Test method __str__ of class IllegalUseOfScopeReplacer"""
    from bzrlib.lazy_import import IllegalUseOfScopeReplacer
    s = IllegalUseOfScopeReplacer('foo', 'msg', 'extra')
    assert str(s) == 'msg extra'



# Generated at 2022-06-14 06:08:15.247127
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__ should return a unicode string"""
    obj = IllegalUseOfScopeReplacer('name', 'msg', 'extra')
    u = unicode(obj)
    if not isinstance(u, unicode):
        raise AssertionError('Returned value of unicode is not a unicode object')


# Generated at 2022-06-14 06:08:23.665480
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """Unit test for method __unicode__ of class IllegalUseOfScopeReplacer"""
    import bzrlib.tests
    e = IllegalUseOfScopeReplacer("a", "b", "c")
    bzrlib.tests.TestCase.assertContainsRe(e, "name='a'")
    bzrlib.tests.TestCase.assertContainsRe(e, "msg='b'")
    bzrlib.tests.TestCase.assertContainsRe(e, "extra=': c'")



# Generated at 2022-06-14 06:08:31.928015
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__ preserves unicode message and parameters"""
    # __unicode__ should always return a unicode object,
    # not a str object.  It should also preserve unicode strings
    # and convert str objects to unicode objects (if possible).
    message = u'This is a test'
    param = u'Param'
    e = IllegalUseOfScopeReplacer('name', message, param)
    u = unicode(e)
    # u should be a unicode string
    assert isinstance(u, unicode), u
    # u should contain the unicode message
    assert u.find(message) != -1, u
    # u should contain the unicode parameter
    assert u.find(param) != -1, u



# Generated at 2022-06-14 06:08:36.301516
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__() should always return a unicode object"""
    try:
        raise IllegalUseOfScopeReplacer('foo', 'bar')
    except IllegalUseOfScopeReplacer as e:
        u = unicode(e)


# Generated at 2022-06-14 06:08:40.548145
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """test IllegalUseOfScopeReplacer.__str__ method."""
    e = IllegalUseOfScopeReplacer('foo','bar','baz')
    assert str(e) == 'foo bar: baz'
    assert repr(e) == 'IllegalUseOfScopeReplacer(foo bar: baz)'



# Generated at 2022-06-14 06:08:51.674504
# Unit test for method __getattribute__ of class ScopeReplacer
def test_ScopeReplacer___getattribute__():
    """__getattribute__ should act as a proxy to a real object

    When __getattribute__ is called it will:
    - return the '_resolve' method when called for that attribute
    - call the '_resolve' method to get the real object, getting
      the real object from the cache first if possible
    - return the attribute from the real object.
    """
    scope = {}
    class FakeModule(object):
        x = 0
        y = 1
        z = 2
    scope["module"] = FakeModule()

    def factory(self, scope, name):
        return scope['module']

    replacer = ScopeReplacer(scope, factory, "module")

    # '_resolve' is the special attribute to get the
    # special '_resolve' method.

# Generated at 2022-06-14 06:09:08.539910
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    # __call__ is a special method, so a test isn't generated automatically
    obj = ScopeReplacer({}, lambda x, y, z: x, 'name')
    # can I call it?
    obj()
    # can I pass arguments?
    obj(1, 2, 3, a=4)
    # does it have a __name__ member?
    obj.__name__

# Generated at 2022-06-14 06:09:17.109035
# Unit test for method __getattribute__ of class ScopeReplacer
def test_ScopeReplacer___getattribute__():
    globals = {}
    lazy_import(globals, '''
    import bzrlib
    ''')
    class Foo(object):
        def __init__(self):
            pass
        def foo(self):
            return 'foo'
    globals['Foo'] = Foo()
    return globals['Foo'].foo() == 'foo'
assert test_ScopeReplacer___getattribute__()



# Generated at 2022-06-14 06:09:21.567355
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__ should return a unicode object"""
    i = IllegalUseOfScopeReplacer('foo', 'bar')
    u = unicode(i)
    assert(isinstance(u, unicode))



# Generated at 2022-06-14 06:09:31.897383
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """Test __unicode__ method of IllegalUseOfScopeReplacer

    This is just a simple test to establish 100% coverage of the method.
    """
    from bzrlib.trace import mutter
    mutter('Test of __unicode__ for IllegalUseOfScopeReplacer')
    e = IllegalUseOfScopeReplacer('name', 'msg')
    mutter(u'e.__unicode__() returned: %r', e.__unicode__())


# TODO: RBC 20060625 there may be a better way to implement this:
# - use a real decorator
# - use a dummy object to represent the import, providing __getattr__ to do
#   the load.

# Generated at 2022-06-14 06:09:42.922678
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """IllegalUseOfScopeReplacer.__unicode__() works as expected."""
    # This is a little strange: the VariableNotFound exception is used as
    # a test.
    e = IllegalUseOfScopeReplacer(name='foo', msg='something went wrong')
    # This test will fail if the exception provides a value for the 'name'
    # member.
    try:
        unicode(e)
    except AttributeError:
        pass
    else:
        raise AssertionError("IllegalUseOfScopeReplacer.__unicode__() loaded"
                             " the 'name' member, which is forbidden.")

