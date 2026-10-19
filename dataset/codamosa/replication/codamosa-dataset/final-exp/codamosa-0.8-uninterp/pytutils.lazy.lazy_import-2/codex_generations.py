

# Generated at 2022-06-14 06:00:01.658731
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    import bzrlib.tests
    from bzrlib.lazy_import import lazy_import
    def foo(): pass
    def func(foo):
        return foo()
    lazy_import(globals(), 'foo')
    func(foo)
    return


# Generated at 2022-06-14 06:00:04.012019
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    k = ScopeReplacer(None, None, None)
    assert k.__call__('x', 'y') == 'xy'


# Generated at 2022-06-14 06:00:09.504557
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__ called on IllegalUseOfScopeReplacer"""

    class MyException(IllegalUseOfScopeReplacer):

        _fmt = u"Exception %(name)r%(extra)s"

    e = MyException('name', 'msg', extra='extra')
    u = e.__unicode__()
    assert isinstance(u, unicode)
    assert u == u'Exception nameextra'

# Generated at 2022-06-14 06:00:10.816091
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    pass # not implemented


# Generated at 2022-06-14 06:00:18.870849
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """__str__ of IllegalUseOfScopeReplacer"""
    e1 = IllegalUseOfScopeReplacer('foo', 'bar')
    e2 = IllegalUseOfScopeReplacer('foo', 'bar')
    e3 = IllegalUseOfScopeReplacer('foo', 'baz')
    assert str(e1) == str(e2)
    assert e1 == e2
    assert e1 != e3
    assert e1 != None
    assert not e1 == None



# Generated at 2022-06-14 06:00:30.954165
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    from bzrlib.tests import TestCase
    from bzrlib.lazy_import import lazy_import
    from bzrlib.lazy_import import ScopeReplacer

    class __ScopeReplacer_TestCase(TestCase):
        def test_ScopeReplacer_should_proxy(self):
            # We need to be able to set/get _should_proxy, so lazy_import
            # ScopeReplacer.
            lazy_import(globals(), '''
            from bzrlib.lazy_import import ScopeReplacer
            ''')

            # Set the value of _should_proxy.
            ScopeReplacer._should_proxy = False

            # Try to access an attribute on a ScopeReplacer object.

# Generated at 2022-06-14 06:00:33.572411
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    # __call__(self, *args, **kwargs)
    raise Exception("Not implemented")

# Generated at 2022-06-14 06:00:43.625134
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    import sys
    import unittest

    def factory(lazy, scope, name):
        scope[name] = 'foo'
        return scope[name]

    scope = {}
    lazy = ScopeReplacer(scope, factory, 'test')
    assert scope['test'] == lazy

    lazy.__setattr__('test', 'bar')

    assert scope['test'] == 'bar'
    # check we can assign to a top-level var without restriction
    scope['bar'] = 'foo'
    assert scope['bar'] == 'foo'

    # Now make sure that if __setattr__ fails, it returns False
    # so we get an effective 'try/finally' scope.
    scope['test_attempt_copy'] = lazy

# Generated at 2022-06-14 06:00:53.443614
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """Unit test for method __str__ of class IllegalUseOfScopeReplacer"""
    class ExceptionSubclass(IllegalUseOfScopeReplacer):
        """Subclass of IllegalUseOfScopeReplacer
        """

    e = ExceptionSubclass("foo", "bar")
    # Note: Value (e.__class__) should be 'ExceptionSubclass', but the output
    # is 'IllegalUseOfScopeReplacer' because the class object is replaced
    # by its 'real' value before the __str__() method is called.
    assert str(e) == "IllegalUseOfScopeReplacer(foo): bar", e.__class__



# Generated at 2022-06-14 06:00:58.673168
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """Method __str__ of a class IllegalUseOfScopeReplacer may return a 
    unicode or str value.
    """
    # create an instance of IllegalUseOfScopeReplacer
    exception = IllegalUseOfScopeReplacer(
        'some_name', 'some_msg', 'some_extra')
    # call method __str__
    string = str(exception)
    # test the result
    if not isinstance(string, str):
        raise AssertionError(
            'Method __str__ of a class IllegalUseOfScopeReplacer '
            'should return a str value.')



# Generated at 2022-06-14 06:01:16.969309
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__calls _format and encodes to unicode with bzrlib.osutils.get_user_encoding. This test ensures that the get_user_encoding is called."""
    import bzrlib
    def test_encoding(s):
        return 'bzrlib.osutils.get_user_encoding was called'
    bzrlib.osutils.get_user_encoding = test_encoding
    from bzrlib import lazy_import
    lazy_import.IllegalUseOfScopeReplacer._fmt = 'dummy message'
    exc = lazy_import.IllegalUseOfScopeReplacer('obj', 'was used incorrectly')
    assert 'was used incorrectly' in unicode(exc)
    assert 'encoding' in unicode(exc)

# Generated at 2022-06-14 06:01:29.910236
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    """__call__(self, *args, **kwargs) *MUST* call the appropriate
    __call__ method on the real object, even if __call__ has been
    overridden by a subclass of the real object"""
    class CallableStub(object):
        called = False
        def __call__(self, *args, **kwargs):
            self.called = True
    scope = {}
    def factory(repl, scope, name):
        return CallableStub()
    my_repl = ScopeReplacer(scope, factory, 'my_obj')
    my_repl()
    assert scope['my_obj'].called, ("__call__ did not call the appropriate"
        " __call__ method on the real object")



# Generated at 2022-06-14 06:01:39.407385
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
  from bzrlib.lazy_import import ScopeReplacer
  from bzrlib.trace import mutter
  obj = ScopeReplacer({}, '',  '')
  mutter.mock_calls
  obj.__setattr__('_should_proxy', False)
  obj.__setattr__('_name', 'foo')
  obj.__setattr__('_real_obj', 'foo')
  obj.__setattr__('x', 'foo')
  obj.__setattr__('_name', 'foo')
  obj.__setattr__('_real_obj', 'foo')
  obj.__setattr__('_name', 'foo')
  obj.__setattr__('_real_obj', 'foo')
  obj.__setattr__('_name', 'foo')
  obj.__setattr

# Generated at 2022-06-14 06:01:41.937366
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """Testing method test_IllegalUseOfScopeReplacer___unicode__."""
    IllegalUseOfScopeReplacer('name', 'message', 'extra')


# Generated at 2022-06-14 06:01:52.932620
# Unit test for method __getattribute__ of class ScopeReplacer
def test_ScopeReplacer___getattribute__():
    """__getattribute__ gets attribute from real object"""
    class TestClass:
        def __init__(self, *args):
            self.args = args
        def id(self):
            return id(self)
        def func(self, *args):
            return self.args + args
    scope = {}
    name = 'test_instance'
    def factory(self, scope, name):
        return TestClass(id(scope), id(name))
    obj = ScopeReplacer(scope, factory, name)
    assert obj.args == (id(scope), id(name))
    assert obj.id() == id(obj)
    assert obj.func(1,2,3) == (id(scope), id(name), 1,2,3)


# Generated at 2022-06-14 06:02:03.017359
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    from bzrlib.tests import TestCase
    from bzrlib.lazy_import import scope_is_cleared

    class Dummy(object):
        pass

    class TestScopeReplacer(TestCase):

        def setUp(self):
            super(TestScopeReplacer, self).setUp()
            scope = {'abc':'abc'}
            def foo(self, scope, name):
                return 'bar'
            self.obj = ScopeReplacer(scope, foo, 'abc')

        def test_proxy(self):
            self.assertEqual('bar', self.obj)

        def test_proxy_failure(self):
            self.obj._resolve = self.fail
            val = Dummy()
            val.attr_name = 'attr_value'
            self.obj = val

# Generated at 2022-06-14 06:02:08.976564
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """IllegalUseOfScopeReplacer.__unicode__() should return
    str(self)"""
    # class A(Exception) is used for testing because _fmt is defined in
    # the class.
    class A(IllegalUseOfScopeReplacer):
        _fmt = "foo"
    e = A('a', 'b', 'c')
    assert unicode(e) == 'a: b: c'



# Generated at 2022-06-14 06:02:21.573686
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    import doctest
    from bzrlib.tests import SymlinkFeature
    from bzrlib.tests.features import ModuleAvailableFeature
    if not SymlinkFeature.available():
        raise TestSkipped('symlinks not available')
    if not ModuleAvailableFeature('foo').available():
        raise TestSkipped('test_module not available')
    import foo
    import bzrlib.lazy_import
    globs = {'__builtins__': None}
    globs['foo'] = bzrlib.lazy_import.scope_replacer(globs, 'foo',
        lambda _, scope, name: bzrlib.lazy_import._import_module(scope, name,
            'test_module'))

# Generated at 2022-06-14 06:02:29.275569
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    from inspect import getsourcefile, isclass
    from os.path import abspath
    import sys
    import unittest

    from bzrlib.lazy_import import (
        IllegalUseOfScopeReplacer,
        ScopeReplacer,
        )

    class TestCaseWithException(unittest.TestCase):
        """A TestCase which is able to raise bzrlib.errors.BzrError

        This allows to make unittests runnable by bzr selftest.
        """

        def assertRaises(self, exc_class, func, *args, **kwargs):
            try:
                func(*args, **kwargs)
            except exc_class:
                return
            raise self.failureException("Exception %s not raised" % exc_class)


# Generated at 2022-06-14 06:02:34.384796
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """__str__() must return a str, not a unicode"""
    try:
        raise IllegalUseOfScopeReplacer('test', 'this should be a str')
    except IllegalUseOfScopeReplacer as e:
        pass
    assert isinstance(str(e), str)


# Generated at 2022-06-14 06:02:52.744833
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    # verify the behavior of the __setattr__ method of the class ScopeReplacer.
    from bzrlib.lazy_import import scope_replace
    import bzrlib.osutils
    scope_replace(['bzrlib.osutils'])
    import unittest
    class test_ScopeReplacer___setattr__(unittest.TestCase):
        def test_setattr_custom_attribute(self):
            self.assertRaises(ScopeReplacer._IllegalUseOfScopeReplacer, lambda: 
                scope_replace(['bzrlib.osutils']).custom_attribute)
    unittest.main()


# Generated at 2022-06-14 06:03:00.431624
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """Test that the IllegalUseOfScopeReplacer (scope replacer) exception can
    be turned in a human readable string by __str__"""
    scope_replacer = IllegalUseOfScopeReplacer(
        'some_name',
        'some_msg',
        )
    expected = "Unprintable exception IllegalUseOfScopeReplacer: dict={'extra': '', 'name': 'some_name', 'msg': 'some_msg'}, fmt=None, error=None"
    got = str(scope_replacer)
    assert expected == got, "expected '%s', got '%s'" % (expected, got)



# Generated at 2022-06-14 06:03:03.987400
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """IllegalUseOfScopeReplacer.__str__() must be fast and return a str object
    """
    e = IllegalUseOfScopeReplacer('foo', 'bar')
    # We aim to be fast
    import time
    start_time = time.time()
    for i in range(100000):
        str(e)
    duration = time.time() - start_time
    # One second was deemed to be fast enough
    if duration > 1:
        raise AssertionError('IllegalUseOfScopeReplacer.__str__ is too slow'
                             ' (%fs)' % duration)



# Generated at 2022-06-14 06:03:14.287832
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    # Do not test this on windows, as we cannot use win32api.LoadLibrary
    import os, sys
    from bzrlib.lazy_import import lazy_import
    from bzrlib.tests import TestSkipped
    if sys.platform == 'win32':
        raise TestSkipped("Can't test on windows, win32api.LoadLibrary"
                          " is too expensive.")
    global mylib
    saved = dict(globals())

# Generated at 2022-06-14 06:03:19.569823
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """IllegalUseOfScopeReplacer.__unicode__() returns unicode string"""
    e = IllegalUseOfScopeReplacer("name", "msg")
    u = e.__unicode__()
    assert isinstance(u, unicode)



# Generated at 2022-06-14 06:03:26.111349
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """IllegalUseOfScopeReplacer.__unicode__ should roundtrip through str"""
    obj = IllegalUseOfScopeReplacer('foo', 'bar', 'extra')
    obj_u = unicode(obj)
    obj_s = str(obj)
    assert obj_s == obj_u.encode('utf8')
    assert obj_u == obj_s.decode('utf8')



# Generated at 2022-06-14 06:03:36.494799
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    class Foo(object):
        def __call__(self, *args, **kwargs):
            return (args,kwargs)
    foo = Foo()
    scope = {}
    name = 'foo'
    try:
        ScopeReplacer(scope, lambda _,x,y: foo, 'foo')
    except Exception as e:
        assert False, 'Unexpected exception raised: %r' % e
    try:
        assert scope[name](1, a=2) == ((1,),{'a':2}), "Unexpected result"
    except Exception as e:
        assert False, 'Unexpected exception raised: %r' % e
    assert not isinstance(scope[name], ScopeReplacer), \
        "Replacer not replaced by some kind of Foo object"


# _assert_no_scope_replacers does not test all

# Generated at 2022-06-14 06:03:41.961951
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    try:
        raise IllegalUseOfScopeReplacer('foo', 'bar', 'baz')
    except IllegalUseOfScopeReplacer as e:
        u = unicode(e)
        assert isinstance(u, unicode)
        assert 'foo' in u, u
        assert 'bar' in u, u
        assert 'baz' in u, u
test_IllegalUseOfScopeReplacer___unicode__.unittest = ['unicode']


# Generated at 2022-06-14 06:03:55.759475
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    """Test method __setattr__ of class ScopeReplacer.

    This tests for
      http://pad.lv/394564
    """
    # tests:
    # creates a ScopeReplacer object and gives it the attribute
    # '_should_proxy' with the value 'False'
    # then calls the __setattr__ method and verifies that an exception is
    # raised.
    # Then sets the value of _should_proxy to True and calls __setattr__
    # which should NOT raise an exception.
    global _should_proxy

    # test with _should_proxy being set to False
    _should_proxy = False
    obj = ScopeReplacer(None, None, None)
    try:
        obj.__setattr__('attr', 'value')
    except IllegalUseOfScopeReplacer as e:
        pass

# Generated at 2022-06-14 06:04:04.910735
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """Check that all methods of IllegalUseOfScopeReplacer are implemented"""
    import sys
    import locale
    def _test_IllegalUseOfScopeReplacer(use_unicode,
                                        use_custom_encoding,
                                        use_locale):
        if use_unicode:
            e = e_unicode = err = IllegalUseOfScopeReplacer(
                    'hello-name', 'foo/bar', extra='baz')
        else:
            e = e_unicode = err = IllegalUseOfScopeReplacer(
                    u'hello-name', u'foo/bar', extra=u'baz')
        if use_unicode:
            e_unicode = IllegalUseOfScopeReplacer(
                    'hello-name', 'foo/bar', extra='baz')
        else:
            e_unicode = IllegalUse

# Generated at 2022-06-14 06:04:20.717231
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__"""
    a = IllegalUseOfScopeReplacer("foo", "msg", "extra")
    b = eval(repr(a))
    eq = a.__eq__
    assert eq(b)
    assert eq(a)
    assert eq(b)
    e = IllegalUseOfScopeReplacer("bar", "message")
    neq = e.__ne__
    assert neq(e) # We can't do assert not eq(e), because cpython raises
                  # a TypeError.
    assert neq(a)
    assert neq(b)



# Generated at 2022-06-14 06:04:32.366091
# Unit test for method __getattribute__ of class ScopeReplacer
def test_ScopeReplacer___getattribute__():
    import bzrlib.lazy_import
    lazy_module = bzrlib.lazy_import
    obj = lazy_module.ScopeReplacer(None, lambda a,b,c:None, None)
    called = []
    def _resolve_calls_repr(self):
        called.append(1)
        return object.__getattribute__(self, '__repr__')()
    obj._resolve = _resolve_calls_repr
    obj.__repr__()
    if len(called) != 1:
        raise AssertionError('len(called) != 1, %r' % (called,))

# Generated at 2022-06-14 06:04:38.124664
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """Unit test for method __unicode__ of class IllegalUseOfScopeReplacer"""
    from bzrlib.tests import per_class

    get_mock_transport_from_url = per_class.get_mock_transport_from_url

    import bzrlib.tests.features
    if not bzrlib.tests.features.has_pyrex:
        # pyrex is not installed.
        return

    # Because IllegalUseOfScopeReplacer is of type ScopeReplacer the unit test
    # is done in the test__ScopeReplacer__unicode__() method defined below.



# Generated at 2022-06-14 06:04:39.250366
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    obj = ScopeReplacer(None, None, None)
    obj.__setattr__('attr', 'value')



# Generated at 2022-06-14 06:04:46.073224
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    import bzrlib.trace
    trace = bzrlib.trace

    def factory(self, scope, name):
        return 1

    r = ScopeReplacer(trace.__dict__, factory, 'a')
    try:
        r()
    except IllegalUseOfScopeReplacer:
        pass
    else:
        raise AssertionError()



# Generated at 2022-06-14 06:04:51.092480
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """__str__ of IllegalUseOfScopeReplacer"""

    e = IllegalUseOfScopeReplacer('test', 'msg', extra='extra')
    s = 'ScopeReplacer object test was used incorrectly: msg: extra'
    assert e.__str__() == s, (e.__str__(), s)



# Generated at 2022-06-14 06:05:05.261885
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    from bzrlib import lazy_import
    import bzrlib.builtins
    import bzrlib.tests
    # test_ScopeReplacer___call__ {{{
    _result = []
    def _wrapped_scope_replacer_factory(scope_replacer, scope, name):
        _result.append((scope_replacer, scope, name))
        return object()
    empty_scope = {}
    lazy_import.scope_replacer_factory(scope_replacer_factory=_wrapped_scope_replacer_factory, scope=empty_scope, name='extra-name')
    t = empty_scope['extra-name'](12, foo='bar')

# Generated at 2022-06-14 06:05:08.560300
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """testing __unicode__ of class IllegalUseOfScopeReplacer"""
    emsg = 'Something went wrong'
    ea = IllegalUseOfScopeReplacer('test', emsg)
    assert ea.__unicode__() == unicode(ea)



# Generated at 2022-06-14 06:05:22.230488
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    import sys
    from bzrlib.lazy_import import lazy_import, lazy_reload
    lazy_import(globals(), """
    from bzrlib import (
        debug,
        errors,
        osutils,
        )
    """)
    def call_me(arg):
        return arg
    def test_factory(replacer, scope, name):
        return call_me
    obj = ScopeReplacer(globals(), test_factory, 'call_me')
    if obj('foo') != 'foo': raise AssertionError()
    obj = ScopeReplacer(globals(), test_factory, 'call_me')
    if obj(42) != 42: raise AssertionError()
    obj = ScopeReplacer(globals(), test_factory, 'call_me')
   

# Generated at 2022-06-14 06:05:29.337441
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    from bzrlib.tests import TestCase

    class FakeException(Exception):
        pass

    e = FakeException()
    e.__name__ = 'FakeException'

    class FakeScopeReplacer(object):
        def __init__(self, name):
            self.name = name
        def __repr__(self):
            return '<scope replacer %r>' % (self.name,)
    class A(IllegalUseOfScopeReplacer):
        _fmt = 'This is a test with %(name)r %(msg)s'

# Generated at 2022-06-14 06:06:11.831995
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """Test __unicode__ of IllegalUseOfScopeReplacer"""
    ce = IllegalUseOfScopeReplacer('name', 'message', 'extra')
    ce_string = 'name: message: extra: (IllegalUseOfScopeReplacer)'
    assert unicode(ce) == ce_string
    assert str(ce) == ce_string



# Generated at 2022-06-14 06:06:21.656650
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    """__setattr__(self, attr, value) -> None

    This is to prevent assignment to the underlying object, which could
    cause the real object to be used before it is ready.
    """
    import bzrlib.lazy_import as lazy_import
    # A class that defines an attribute 'a'.
    class ScopeReplacerTest():
        def __init__(self):
            self.a = 10

    def test(s):
        """Test the assignment of the attibute 'a' to 's'
        """
        # Make the real object of the ScopeReplacer object 's'
        s._resolve()
        # Raise an error if the following is done, because the ScopeReplacer
        # object is already replaced
        s.a = 11

# Generated at 2022-06-14 06:06:31.707951
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    from bzrlib.lazy_import import lazy_import, ScopeReplacer
    from bzrlib import branch
    import bzrlib.branch
    global_dict = globals()
    lazy_import(global_dict, '''
    from bzrlib import branch
    import bzrlib.branch
    ''')
    branchReplacer = globals()['branch']
    bzrlib_branchReplacer = globals()['bzrlib_branch']
    assert isinstance(branchReplacer, ScopeReplacer), \
        "lazy_import should have created a ScopeReplacer object"
    assert isinstance(bzrlib_branchReplacer, ScopeReplacer), \
        "lazy_import should have created a ScopeReplacer object"
    # We can't write branch.* because

# Generated at 2022-06-14 06:06:43.815757
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """Unit test for method IllegalUseOfScopeReplacer.__unicode__."""
    import sys
    import bzrlib.lazy_import
    mod = bzrlib.lazy_import

    e = Exception()
    def run_test(args):
        # create an IllegalUseOfScopeReplacer instance and call __unicode__
        e = mod.IllegalUseOfScopeReplacer(*args)
        return e.__unicode__()
    # call with a unicode format string and a unicode exception
    unicode_msg = unicode("cannot use this object")
    u = run_test((u"my_name", unicode_msg, e))
    # should treat IllegalUseOfScopeReplacer.__unicode__ as a no-op
    # if exception has no _fmt attribute

# Generated at 2022-06-14 06:06:56.461275
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__ should return either a unicode object or a str"""
    # Make an IllegalUseOfScopeReplacer instance with a str and a unicode
    # attribute.
    s = 'abc'
    e = IllegalUseOfScopeReplacer('', '', s)
    u = u'abc'
    e.u = u
    e.__dict__[u] = u
    assert not isinstance(e.u, unicode)
    assert isinstance(e.name, unicode)
    assert isinstance(e.msg, unicode)
    assert isinstance(e.extra, unicode)
    assert isinstance(e.__dict__[u], unicode)
    assert isinstance(unicode(e.u), unicode)
    assert isinstance(unicode(e.name), unicode)

# Generated at 2022-06-14 06:07:05.483292
# Unit test for method __getattribute__ of class ScopeReplacer
def test_ScopeReplacer___getattribute__():
    # Calling object.__getattribute__ of ScopeReplacer is disallowed, so the
    # test suite can detect when the unit tests are insufficient.
    scope = {}
    replacer = ScopeReplacer(scope, lambda self, scope, name: scope, 'scope')

    class Foo(object):
        def __repr__(self):
            return 'Foo()'
    def factory(self, scope, name):
        return Foo()
    object.__setattr__(replacer, '_factory', factory)
    object.__setattr__(replacer, '_real_obj', Foo())
    replacer.__getattribute__('_resolve')()



# Generated at 2022-06-14 06:07:19.571815
# Unit test for method __getattribute__ of class ScopeReplacer
def test_ScopeReplacer___getattribute__():
    # This function doesn't test _should_proxy as it's a class attribute.
    def factory(self, scope, name):
        return name
    name = 'my_name'
    scope = {}
    obj = ScopeReplacer(scope, factory, name)
    # Check that ScopeReplacer.__getattribute__ correctly returns the
    # replacement name from the factory (my_name).
    assert obj.__getattribute__('upper') == name.upper()
    # Also check that replacing obj in the scope works correctly for
    # the next test.
    assert scope[name] == name
    # Check that replacing obj in the scope also changes the representation.
    assert obj == name
    # Check that the call method also works.
    assert obj() == name
    # Check that obj.__getattribute__ works for private members of ScopeReplacer
    assert obj

# Generated at 2022-06-14 06:07:26.053399
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """Test IllegalUseOfScopeReplacer.__unicode__ method"""
    import sys
    import traceback
    err1 = IllegalUseOfScopeReplacer('err1', 'some message')
    s = err1.__unicode__()
    err2 = eval(s)
    if err1 != err2:
        sys.stderr.write(traceback.format_exc())
        raise AssertionError("'%s' should equal '%s'" % (err1, err2))



# Generated at 2022-06-14 06:07:34.518218
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """Test method __str__ of IllegalUseOfScopeReplacer"""
    # Check that __str__ translates messages for '_fmt' keys
    # and formats them correctly. It should also return a str, not unicode.
    from bzrlib.i18n import gettext
    _fmt = "This is a test"
    class MyIllegalUseOfScopeReplacer(IllegalUseOfScopeReplacer):
        _fmt = _fmt
    exc = MyIllegalUseOfScopeReplacer('name', 'msg', 'extra')
    s = str(exc)
    # __str__ must return a str object, not unicode.
    assert isinstance(s, str)
    # Check exc._get_format_string()
    fmt = exc._get_format_string()
    assert isinstance(fmt, unicode)
   

# Generated at 2022-06-14 06:07:41.157451
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    from bzrlib import tests
    from bzrlib.lazy_import import lazy_import
    from bzrlib.lazy_import import ScopeReplacer

    class MyScopeReplacer(ScopeReplacer):
        def __init__(self, scope, factory, name):
            super(MyScopeReplacer, self).__init__(scope, factory, name)
        def _resolve(self):
            raise AssertionError('Shouldn\'t be called')

    scope = {}
    scope['scope_replacer'] = MyScopeReplacer(scope, lambda s, t, n: s, 'foo')
    scope['scope_replacer'].foo = 'foo'
    scope['scope_replacer'].bar = 'bar'
    scope['scope_replacer'].baz = 'baz'

# Generated at 2022-06-14 06:08:02.295052
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    class ScopeReplacer_sample:
        b = 2
        def __init__(self):
            pass
        def __setattr__(self, name, value):
            if name == 'a':
                if value != 2:
                    raise AssertionError
                return
            object.__setattr__(self, name, value)
            assert name == 'b'
            assert value == 4

    obj = ScopeReplacer_sample()
    obj.a = 2
    obj.b = 4
test_ScopeReplacer___setattr__()

# Generated at 2022-06-14 06:08:11.214796
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """This tests that IllegalUseOfScopeReplacer.__unicode__() works.

    Returns: None.
    """
    try:
        raise IllegalUseOfScopeReplacer('foo', 'badness')
    except Exception as e:
        assert str(e) == 'Unprintable exception IllegalUseOfScopeReplacer: ' \
            'dict={\'msg\': \'badness\', \'name\': \'foo\', \'extra\': \'\'}, ' \
            'fmt=None, error=None'
    assert UnicodeException() == UnicodeException()
    assert UnicodeException() != Exception()
    assert UnicodeException() != UnicodeException('foo')
    s = UnicodeException('foo')
    assert s == UnicodeException('foo')
    assert s != UnicodeException('bar')



# Generated at 2022-06-14 06:08:23.910726
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    e1 = IllegalUseOfScopeReplacer('name', 'message', 'extra')
    import sys
    from StringIO import StringIO
    saved_stderr = sys.stderr
    try:
        buf = StringIO()
        sys.stderr = buf
        str(e1)
    finally:
        sys.stderr = saved_stderr
    buf.seek(0)
    s = buf.read().splitlines()[-1]
    assert 'Unprintable exception IllegalUseOfScopeReplacer:' in s
    assert 'dict={' in s
    assert "msg=u'message'" in s
    assert "name=u'name'" in s
    assert "extra=u'extra'" in s
    assert '}, fmt=None, error=None' in s
test_IllegalUseOfScopeReplacer___

# Generated at 2022-06-14 06:08:26.879270
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__() returns unicode"""
    e = IllegalUseOfScopeReplacer('name', 'msg')
    assert type(e.__unicode__()) is unicode



# Generated at 2022-06-14 06:08:40.445149
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    global ScopeReplacer
    import bzrlib.lazy_import
    reload(bzrlib.lazy_import)
    ScopeReplacer = bzrlib.lazy_import.ScopeReplacer

    import bzrlib
    import bzrlib.trace
    bzrlib.trace.enable_default_logging()

    d = {}
    bzrlib.lazy_import.lazy_import(d, '''
from bzrlib import errors
from bzrlib.trace import mutter
''')
    ScopeReplacer._should_proxy = True
    e = d['errors']
    assert e.__class__.__name__ == 'ScopeReplacer'

# Generated at 2022-06-14 06:08:48.106258
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    from bzrlib.tests import TestCase
    from bzrlib.lazy_import import IllegalUseOfScopeReplacer
    class MyException(Exception):
        """Some exception - to override _fmt"""
        _fmt = ("blah")
    e = MyException('zzz', 'yyy')
    self = TestCase()
    self.assertEqual(repr(e), "MyException('zzz', 'yyy')")
    self.assertEqual(str(e), "zzz, yyy")
    self.assertEqual(e.__dict__, {'args': ('zzz', 'yyy'), '_fmt': 'blah'})



# Generated at 2022-06-14 06:08:51.306128
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """_format returns a string."""
    e = IllegalUseOfScopeReplacer('foo', 'bar')
    s = str(e)
    assert isinstance(s, str)



# Generated at 2022-06-14 06:08:54.747010
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """Testing method __str__ of class IllegalUseOfScopeReplacer."""
    # Testing whether IllegalUseOfScopeReplacer object's __str__ method
    # return a str object.
    err = IllegalUseOfScopeReplacer('name', 'msg', 'extra')
    err.__str__()



# Generated at 2022-06-14 06:09:05.684019
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    import bzrlib.tests
    class _TestScopeReplacer__setattr__(bzrlib.tests.TestCase):
        def assertSetattr(self, obj, attr, value):
            obj.__setattr__(attr, value)
            self.assertEqual(getattr(obj, attr), value)
        def test__ScopeReplacer___setattr(self):
            import bzrlib.tests.blackbox.test_do_cmd
            class Example(object):
                example_attr = 1
            namespace = {'Example':Example}
            bzrlib.lazy_import.lazy_import(namespace, 'Example')
            self.assertSetattr(namespace['Example'], 'example_attr', 2)
            self.assertSetattr(namespace['Example'], 'example_attr', 3)

# Generated at 2022-06-14 06:09:15.325570
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """IllegalUseOfScopeReplacer.__unicode__()

    If _preformatted_string is set then __unicode__ returns that else it takes
    self.__dict__,  self._fmt and the result of self._get_format_string()
    and formats them appropriately.

    :return: None.
    """
    class TestException(IllegalUseOfScopeReplacer):
        """Class for testing purpose"""

        _fmt = "Test exception message"

    exc = TestException('test', 'illegal call')
    assert exc._get_format_string() == "Test exception message"
    assert exc.__unicode__() == "Test exception message"
    assert exc.__str__() == "Test exception message"



# Generated at 2022-06-14 06:09:35.358859
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    __tracebackhide__ = True

    class Foo:
        # __call__ is missing
        pass
    foo = Foo()
    foo.called = False
    foo.args = []

    def _call_foo(my_self, my_scope, my_name):
        return foo

    foo_sl = ScopeReplacer(globals(), _call_foo, 'foo_sl')
    # Make sure we get a call through to the original foo
    foo_sl(1, 2, x=3, y=4, z=5)
    assert foo.called
    assert foo.args == [(1, 2), {'x': 3, 'y': 4, 'z': 5}]

    class Foo:
        # __call__ is defined

        def __call__(self, *args, **kwargs):
            self.args = []