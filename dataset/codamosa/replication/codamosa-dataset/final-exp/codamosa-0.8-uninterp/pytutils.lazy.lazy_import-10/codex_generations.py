

# Generated at 2022-06-14 06:00:12.147330
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    import sys

    global __name__
    global __doc__

    def func():
        assert __name__ == '__main__'
        assert __doc__ is None
        global __name__
        global __doc__
        __name__ = 'foo'
        __doc__ = 'bar'
    scope = locals()
    scope_replacer = ScopeReplacer(locals(),
        None, '__name__') # test func access to local variables
    scope_replacer = ScopeReplacer(locals(),
        None, '__doc__') # test func access to local variables
    func()
    assert __name__ == 'foo'
    assert __doc__ == 'bar'



# Generated at 2022-06-14 06:00:19.203726
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    instance = IllegalUseOfScopeReplacer('lazy_import', 'Illegal')
    instance.x = 1
    instance.y = 2

# Generated at 2022-06-14 06:00:27.746938
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    """__setattr__() sets attributes on the real object when it exists

    This method is here because setting attributes on a ScopeReplacer
    object should be rare, and wouldn't be possible once the object has
    been replaced. In that case, the attribute should be set on the
    target object.
    """

    class RealObj(object):
        """A simple target object"""
        def __init__(self, name):
            self.name = name
    # RealObj

    class Scope(dict):
        """A simple scope"""
        pass
    # Scope

    scope = Scope()
    replacer = ScopeReplacer(scope, lambda a, b, c: RealObj(c), "real_obj_name")
    scope['real_obj_name'].foo = 'bar'

# Generated at 2022-06-14 06:00:33.258724
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """IllegalUseOfScopeReplacer.__unicode__() should format into a unicode."""
    e = IllegalUseOfScopeReplacer('name', 'msg')
    u = unicode(e)
    # the default encoding is utf8.
    assert not isinstance(u, str)



# Generated at 2022-06-14 06:00:43.496027
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    class Bar(object):
        def __call__(self, *args, **kwargs):
            return 'bar %s %s'% (args, kwargs)
    def make_bar(repl, scope, name):
        return Bar()
    scope = {'bar' : None}
    bar_replacer = ScopeReplacer(scope, make_bar, 'bar')
    # unraced
    assert scope['bar'] is bar_replacer
    assert bar_replacer('one', two=3) == 'bar (\'one\',) {\'two\': 3}'
    assert scope['bar'] is not bar_replacer
    # raced
    import threading
    event = threading.Event()
    def racing_thread():
        event.wait()
        assert scope['bar'] is not bar_replacer

# Generated at 2022-06-14 06:00:55.303254
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    class DummyClass(object):
        def __call__(self, *args, **kwargs):
            return self.__class__.__name__, args, kwargs
    scope = {}
    lazy_import(scope, '''
    class DummyClass(object):
        def __call__(self, *args, **kwargs):
            return self.__class__.__name__, args, kwargs
    ''')
    assert scope['DummyClass']().__class__.__name__ == 'DummyClass'
    assert scope['DummyClass'](1, one=1).__class__.__name__ == 'DummyClass'
    scope['real'] = DummyClass()
    assert scope['real']().__class__.__name__ == 'tuple'

# Generated at 2022-06-14 06:01:00.838030
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    # test check for races on _resolve
    import bzrlib
    from bzrlib.lazy_import import (
        lazy_import,
        lazy_import_later,
        )
    lazy_import(globals(), """
    from bzrlib import (
        config,
        )
    """)
    # need to ensure that bzrlib.config has not been loaded yet
    # so we disable the loading of the module and then re-enable it
    # so that the unittest loading of bzrlib.config will fail (if it's needed)
    _orig_enabled = ScopeReplacer._should_proxy
    try:
        ScopeReplacer._should_proxy = False
        obj = bzrlib.config
    finally:
        ScopeReplacer._should_proxy = _orig_enabled
    #

# Generated at 2022-06-14 06:01:02.401548
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    obj = ScopeReplacer({}, lambda o,s,n: o, '')
    obj.__setattr__('a', 3)
    return



# Generated at 2022-06-14 06:01:14.354140
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    # Probably the only test there is not a test of import
    real = [0]
    def factory(self, scope, name):
        real[0] += 1
        return self
    scope = {}
    name = 'test_name'
    lazy = ScopeReplacer(scope, factory, name)
    assert real == [0], "Should not have called factory yet"
    assert lazy is lazy(), "Should be equal to itself"
    assert real == [1], "Should have called factory once"
    assert lazy is lazy(), "Should still be equal to itself"
    assert real == [1], "Should not have called factory again"
    # Allow using lazy variable as a function - should not be allowed once
    # replaced.
    ScopeReplacer._should_proxy = False
    original_should_proxy = ScopeReplacer._should_proxy

# Generated at 2022-06-14 06:01:24.332858
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    """__setattr__ calls setattr(self._resolve(), attr, value)"""
    import sys
    import bzrlib
    obj = ScopeReplacer(sys.modules, lambda _: bzrlib, 'bzrlib')
    obj.__setattr__('attr1', 'value1')
    # _resolve() has been called
    # NOTE: This test is too strict, it should check if bzrlib.attr1 ==
    # value1, but this is not achieved.
    assert_equal('value1', bzrlib.attr1)

# Generated at 2022-06-14 06:01:45.099355
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """IllegalUseOfScopeReplacer.__unicode__()

    Smoketest for basic UI message handling.
    """
    inst = IllegalUseOfScopeReplacer('name', 'msg', extra='data')
    inst.__unicode__()
    inst.__str__()
    expected = ('Unprintable exception IllegalUseOfScopeReplacer:'
        ' dict={"name": "name", "msg": "msg", "extra": ": data"}, fmt=None,'
        ' error=None')
    inst.__repr__() == expected

# Generated at 2022-06-14 06:01:50.713496
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    f = lambda: 'dummy'
    class MockScopeReplacer(ScopeReplacer):
        def _resolve(self):
            return self._factory(self, self._scope, self._name)
    r = MockScopeReplacer({}, f, 'foo')
    def call_self():
        return r()
    # no exception
    call_self()




# Generated at 2022-06-14 06:01:54.188252
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """IllegalUseOfScopeReplacer.__unicode__ should behave like __str__"""
    e = IllegalUseOfScopeReplacer('name', 'msg', 'extra')
    s = unicode(e)
    assert 'name' in s
    assert 'msg' in s
    assert 'extra' in s
    assert 'Unprintable exception' not in s



# Generated at 2022-06-14 06:02:01.081826
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """
    str(IllegalUseOfScopeReplacer('name', 'msg', 'extra')) should
    return 'IllegalUseOfScopeReplacer object name used incorrectly: msg: extra'.
    """
    e = IllegalUseOfScopeReplacer('name', 'msg', 'extra')
    assert str(e) == 'IllegalUseOfScopeReplacer object name used incorrectly: msg: extra'



# Generated at 2022-06-14 06:02:09.174088
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """IllegalUseOfScopeReplacer.__str__()

    Test that IllegalUseOfScopeReplacer.__str__() works.
    """
    # Test that IllegalUseOfScopeReplacer.__str__() works with a preformatted
    # string.
    s = u"IllegalUseOfScopeReplacer.__str__() works"
    obj = IllegalUseOfScopeReplacer('name', 'msg', extra=s)
    obj._preformatted_string = s
    s2 = str(obj)
    assert s == s2
    # Test that IllegalUseOfScopeReplacer.__str__() works with a non-ascii
    # string, with a non-ascii encoding.
    s = u"IllegalUseOfScopeReplacer.__str__() \xe8 works"
    obj = IllegalUseOfScopeReplacer

# Generated at 2022-06-14 06:02:21.689479
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    # ScopeReplacer.__call__() -> None
    # Test __call__ method of ScopeReplacer
    import re
    import bzrlib.tests.blackbox
    import bzrlib.tests.blackbox.cmd_selftest
    _pattern = ', '.join(repr(e) for e in re.split('(,\s*)', r'\t+?# '))
    _regex = re.compile(_pattern, re.VERBOSE)
    _code = """\tdef __call__(self, *args, **kwargs):
\t\tobj = object.__getattribute__(self, '_resolve')()
\t\treturn obj(*args, **kwargs)"""
    _source = _regex.sub('', _code)
    _globals = globals().copy()

# Generated at 2022-06-14 06:02:29.274896
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    from bzrlib.tests import TestCase

    class Test(TestCase):

        def test_scope_replacer_get_called(self):
            class TestObj(object):
                called = False
                def __call__(self, *args, **kwargs):
                    self.called = True

            called = False
            def factory(self, scope, name):
                self.called = True
                return TestObj()

            scope = {}
            name = 'name'
            replacer = ScopeReplacer(scope, factory, name)
            self.assertFalse(replacer.called)
            self.assertFalse(replacer._real_obj.called)
            replacer()
            self.assertTrue(replacer.called)
            self.assertTrue(replacer._real_obj.called)
            ScopeReplacer._should_proxy = False

# Generated at 2022-06-14 06:02:35.155768
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__ must return a unicode object"""
    e = IllegalUseOfScopeReplacer('foo', u'bar', u'baz')
    u = e.__unicode__()
    if not isinstance(u, unicode):
        raise AssertionError('__unicode__ must return a unicode object, not %r'
                             % (u,))

# Generated at 2022-06-14 06:02:45.320959
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    from bzrlib.tests import TestCase
    from bzrlib.lazy_import import (
        lazy_import,
        )
    from bzrlib.lazy_import import _StaticObject
    def func_to_replace(self, scope, name):
        raise NotImplementedError(self)
    global_dict = {'lazy_import_test': None}
    lazy_import(global_dict, 'lazy_import_test', func_to_replace)
    _StaticObject.scope_check_disabled = False

# Generated at 2022-06-14 06:02:48.398668
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    args = ()
    kwargs = {}
    assert ScopeReplacer(None, None, None).__call__(*args, **kwargs) is None


# Generated at 2022-06-14 06:03:12.652504
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """Unit test for IllegalUseOfScopeReplacer.__str__()"""
    # test a simple exception
    e = IllegalUseOfScopeReplacer(
        'name', 'message', 'extra')
    assert str(e) == "ScopeReplacer object 'name' was used incorrectly:"\
           " message: extra"
    # test a preformatted string
    e = IllegalUseOfScopeReplacer(
        'name', 'message', 'extra')
    e._preformatted_string = 'preformatted string'
    assert str(e) == "preformatted string"
    # test the formatting
    e = IllegalUseOfScopeReplacer(
        'name', 'message', 'extra')

# Generated at 2022-06-14 06:03:26.416994
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    import bzrlib.tests.test__lazy_import as fakemodule
    from bzrlib.lazy_import import (
        lazy_import,
        ScopeReplacer,
        IllegalUseOfScopeReplacer,
        )
    g = globals()
    # Clear the global namespace
    g.clear()
    lazy_import(g, "fakemodule.fake_class")
    fake_class = g['fake_class']
    fake_object = fake_class()
    f = fake_class()
    g['f'] = f
    sr = ScopeReplacer(g, ScopeReplacer._resolve, 'f')
    # To keep things simple, we must only have one replacement object,
    # 'f' in the test case.

# Generated at 2022-06-14 06:03:32.317490
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """IllegalUseOfScopeReplacer.__unicode__() should return a unicode object."""
    e = IllegalUseOfScopeReplacer("name", "msg")
    u = unicode(e)
    assert isinstance(u, unicode)

# Generated at 2022-06-14 06:03:35.204587
# Unit test for method __getattribute__ of class ScopeReplacer
def test_ScopeReplacer___getattribute__():
    """test for method __getattribute__ of class ScopeReplacer"""
    # FIXME: implement this test
    pass

# Generated at 2022-06-14 06:03:45.059268
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """__str__ should return a str object, not a unicode object"""
    # Because of the way __str__ is defined in
    # bzrlib.errors.BzrError, it can return a unicode object.
    # This test ensures that this does not happen.
    from bzrlib.errors import BzrError
    from bzrlib.lazy_import import IllegalUseOfScopeReplacer
    exc = IllegalUseOfScopeReplacer("name", "msg")
    assert exc.__class__ is IllegalUseOfScopeReplacer
    isinstance(exc, BzrError) # This should not raise
    assert isinstance(str(exc), str)
    assert not isinstance(str(exc), unicode)


# Generated at 2022-06-14 06:03:50.433595
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__ of IllegalUseOfScopeReplacer should return unicode"""
    obj = IllegalUseOfScopeReplacer('my_name', 'my_msg', 'my_extra')
    assert isinstance(obj.__unicode__(), unicode)


# Generated at 2022-06-14 06:04:01.878548
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    # This is indirect testing of the function _resolve() and is mainly to
    # ensure that __call__ does the right thing.
    class RealThing(object):
        def __init__(self, args=None):
            self.args = args
    scope = {}
    replacer = ScopeReplacer(scope, factory=lambda self, scope, name: RealThing(), name='obj')
    obj = replacer(['hello'])
    if obj.args is not ['hello']:
        raise AssertionError('obj.args is not ["hello"]')


_import_lock = None
"""Lock object used to ensure that multiple threads create modules safely

This lock is used to ensure that only one thread attempts to create a module
at a time.
"""


# Some variables are stored in the lazily-imported modules.  If we are
#

# Generated at 2022-06-14 06:04:03.736240
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    """Method __call__ of class ScopeReplacer"""
    pass # tested by test__lazy_import



# Generated at 2022-06-14 06:04:12.296712
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    from unittest import TestCase
    import weakref

    class Test(TestCase):
        class Module(object):
            pass

        def setUp(self):
            import gc
            self.gc_collector = gc.collect
            self.scope = weakref.WeakKeyDictionary()
            self.lazy_import = ScopeReplacer(
                self.scope, self._make_module, 'lazy_import')

        def tearDown(self):
            self.gc_collector()

        def _make_module(self, replacer, scope, name):
            return self.Module()

        # Unit test for __setattr__
        def test__setattr__(self):
            o = self.lazy_import
            o.foo = 'foo_value'

# Generated at 2022-06-14 06:04:18.161544
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    e = IllegalUseOfScopeReplacer('name', 'msg', 'extra')
    assert str(e) == 'IllegalUseOfScopeReplacer object "name" was used incorrectly: msg: extra'
    assert repr(e) == 'IllegalUseOfScopeReplacer(IllegalUseOfScopeReplacer object "name" was used incorrectly: msg: extra)'



# Generated at 2022-06-14 06:04:42.307316
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    # this will raise if try to replace self.
    scope = {}
    scope_replacer = ScopeReplacer(scope, lambda self, scope, name: None, 'foo')

    # Make sure that __setattr__ does raise if try to replace self.

# Generated at 2022-06-14 06:04:48.508166
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """IllegalUseOfScopeReplacer.__unicode__ should return the exception
    message formatted"""
    e = IllegalUseOfScopeReplacer('name', 'message')
    result = unicode(e)
    expected = u'ScopeReplacer object \'name\' was used incorrectly: message'
    assert result == expected, (result, expected)



# Generated at 2022-06-14 06:04:55.249097
# Unit test for method __getattribute__ of class ScopeReplacer
def test_ScopeReplacer___getattribute__():
    name = 'foo'
    scope = {}
    def factory(self, scope, name):
        if name.startswith('_'):
            raise ValueError('Name %r should not start with _' % name)
        return object()
    repl = ScopeReplacer(scope, factory, name)
    obj = repl._resolve()
    assert repl is not obj
    assert repl._resolve() is obj
    assert repl._resolve().__class__ is obj.__class__
    assert repl.__getattr__('bar') is obj.__getattr__('bar')
    try:
        repl.__getattr__('__class__')
    except ValueError as e:
        assert str(e) == "Name '_foo' should not start with _"

# Generated at 2022-06-14 06:05:08.144720
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    import sys
    import unittest
    class TestScopeReplacer(unittest.TestCase):
        def test__resolve__setattr__(self):
            import sys
            globals_dict = sys._getframe().f_back.f_globals
            def factory_func(self, scope, name):
                return factory_func
            ScopeReplacer(globals_dict, factory_func, 'factory_func')
            class Foo(ScopeReplacer):
                def __init__(self):
                    ScopeReplacer.__init__(self, globals_dict,
                                           self._factory, 'self')
                def _factory(self, scope, name):
                    return name
            foo = Foo()
            self.assertEqual(foo(), 'self')
    results = unittest.TestResult()


# Generated at 2022-06-14 06:05:19.151925
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """Method __unicode__ of IllegalUseOfScopeReplacer must return the
    unicode representation of the exception, if the format string given
    in the format string attribute _fmt is set; otherwise it is hard to
    unit test this method because it returns a string that is specific
    to the locale """
    class TestException(Exception):
        _fmt = "test exception with format string %(num)s"

    exception = TestException(num=42)
    from bzrlib.i18n import gettext
    assert exception.__unicode__() == gettext(u"test exception with format string 42")



# Generated at 2022-06-14 06:05:25.740785
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__ should work"""
    # _fmt is ascii
    class A(IllegalUseOfScopeReplacer):
        _fmt = "foo"
    # _fmt is unicode
    class B(IllegalUseOfScopeReplacer):
        _fmt = u"foo"
    class C(IllegalUseOfScopeReplacer):
        pass
    def get_unicode(obj):
        return unicode(obj)
    a = A('bar', 'baz')
    b = B('bar', u'baz')
    c = C('bar', 'baz')
    str(a) # make sure it works
    str(b) # make sure it works
    str(c) # make sure it works
    # These are secretly just calling __str__
    u = unicode(a)
   

# Generated at 2022-06-14 06:05:34.493057
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    import os
    import bzrlib.tests
    bzrlib.tests.init()
    def create_importable_object(self, scope, name):
        return os.path
    scope = {}
    replacer = ScopeReplacer(scope, create_importable_object, 'os')
    os = scope['os']
    assert isinstance(os, ScopeReplacer)
    assert os.getcwd() == replacer.getcwd()
    assert os.path == replacer.path



# Generated at 2022-06-14 06:05:42.948162
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__ should return a unicode object"""
    e = IllegalUseOfScopeReplacer(name='foo', msg='bar')
    # Check that it does not raise an exception.
    u = e.__unicode__()
    # Check that it returns a unicode object.
    assert isinstance(u, unicode)
    # Check that __unicode__ returns a non-empty string.
    assert u != ''
    # Check that it returns the same string as __str__.
    assert e.__unicode__() == e.__str__()



# Generated at 2022-06-14 06:05:51.919292
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """Tests the method '__unicode__' of class 'IllegalUseOfScopeReplacer'."""
    excp = IllegalUseOfScopeReplacer('name', 'msg', extra='extra')
    unicode_result = unicode(excp)
    assert unicode_result == u"ScopeReplacer object 'name' was used incorrectly: msg: extra"
    str_result = str(excp)
    assert str_result == "ScopeReplacer object 'name' was used incorrectly: msg: extra"



# Generated at 2022-06-14 06:05:57.293571
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """IllegalUseOfScopeReplacer does not lose information when converted to unicode."""
    exc = IllegalUseOfScopeReplacer('name', 'msg', 'extra')
    u = unicode(exc)

# Generated at 2022-06-14 06:06:43.971042
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """IllegalUseOfScopeReplacer.__unicode__()

    The __unicode__() method of an exception should return a unicode string.
    """
    s = UnicodeException.__unicode__(UnicodeException())
    assert isinstance(s, unicode)


# Generated at 2022-06-14 06:06:56.559328
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    import unittest
    import warnings

    class TestScopeReplacer(unittest.TestCase):
        def setUp(self):
            # We want to test the *proxy* class, as that's what is
            # used by real code; in particular, the module-replacing
            # code in lazy_import() does not use a direct instance of
            # ScopeReplacer, but the proxy type returned by its
            # create_scope_proxy() method.
            from bzrlib.lazy_import import (
                ScopeReplacer,
                create_scope_proxy,
                )
            # Create a scope used for testing.
            tscope = dict(((k,v) for k, v in globals().items()
                           if k.startswith('test_')))
            # Wrap it in a proxy.

# Generated at 2022-06-14 06:07:03.440753
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    import bzrlib
    ScopeReplacer._should_proxy = False
    bzrlib.errors = ScopeReplacer(locals(), lambda self, scope, name: object(), 'bzrlib.errors')
    try:
        bzrlib.errors = object()
    except IllegalUseOfScopeReplacer:
        pass
    else:
        raise AssertionError
    ScopeReplacer._should_proxy = True


# Generated at 2022-06-14 06:07:08.590447
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """Test that strings are returned as-is and unicode objects are encoded
    using UTF-8.
    """
    exc = IllegalUseOfScopeReplacer("foo", "This is an error")
    ustr = unicode("foo")
    exc._preformatted_string = ustr
    assert exc.__str__() == "foo"
    exc._preformatted_string = "bar"
    assert exc.__str__() == "bar"



# Generated at 2022-06-14 06:07:19.571822
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__ should stringify the exception."""
    from breezy.tests.per_errors import TestCaseWithTransport
    case = TestCaseWithTransport()
    exc = IllegalUseOfScopeReplacer('foo', 'bar')
    case.assertEqual('IllegalUseOfScopeReplacer(foo): bar', str(exc))
    case.assertEqual('IllegalUseOfScopeReplacer(foo): bar', unicode(exc))



# Generated at 2022-06-14 06:07:24.837705
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """test __str__"""
    e = IllegalUseOfScopeReplacer('foo', 'bar')
    # __str__ should return a string
    assert isinstance(e.__str__(), basestring)
    # __str__ should return the same string as __repr__, since format strings
    # and extra data is not used.
    assert e.__str__() == e.__repr__()



# Generated at 2022-06-14 06:07:29.393251
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    global __doc__

    scope = {}
    x = ScopeReplacer(scope, lambda self, scope, name: name, 'x')
    x.z = 1
    assert scope == {'x': 'x'}, scope



# Generated at 2022-06-14 06:07:38.060006
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """__str__ of IllegalUseOfScopeReplacer must return str."""
    # The third argument is the 'msg' argument, which is supposed to be a
    # message that is utf8 encoded.
    x = IllegalUseOfScopeReplacer('foo', 'blah \xe9', 'blah \xe9')
    s = str(x)
    if not isinstance(s, str):
        raise AssertionError("s is not str: %s" % (s,))
    if not isinstance(s, str):
        raise AssertionError("s is not str: %s" % (s,))



# Generated at 2022-06-14 06:07:44.215546
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """Unit test for method __unicode__ of class `IllegalUseOfScopeReplacer`."""
    import bzrlib.lazy_import
    bzrlib.lazy_import._test_IllegalUseOfScopeReplacer___unicode__()

# Generated at 2022-06-14 06:07:49.817205
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__() supports unicode objects"""
    # unicode is supported
    class MyIllegalUseOfScopeReplacer(IllegalUseOfScopeReplacer):
        pass
    e = MyIllegalUseOfScopeReplacer('a', u'b')
    # check that it returns a unicode object
    assert isinstance(e.__unicode__(), unicode)



# Generated at 2022-06-14 06:08:26.824739
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    from . import lazy_import

    def _factory(self, scope, name):
        return import_module(name)

    t = {}
    lazy_import.lazy_import(t, 'bzrlib.lazy_import')
    t['bzrlib'].lazy_import = ScopeReplacer(t, _factory, 'bzrlib.lazy_import')
    t['bzrlib.lazy_import'].lazy_import(t, 'bzrlib.lazy_import')
    assert t['bzrlib.lazy_import'] is not None
    assert t['bzrlib.lazy_import'].lazy_import is not None

# Generated at 2022-06-14 06:08:34.960943
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    """__setattr__ should set the attribute on the real object."""

    def check(should_proxy):
        ScopeReplacer._should_proxy = should_proxy
        scope = {}
        sentinel = object()
        repl = ScopeReplacer(scope, lambda obj, scope, name:sentinel,
                             'sentinel')
        repl.attr = 1
        assert sentinel.attr == 1

    yield check, True
    yield check, False



# Generated at 2022-06-14 06:08:45.257216
# Unit test for method __getattribute__ of class ScopeReplacer
def test_ScopeReplacer___getattribute__():
    from bzrlib._lazy_import_tests import test_module
    _reset_scope()
    global test_module
    # Create a ScopeReplacer called lazy_module
    lazy_import(_scope, '''
    import bzrlib._lazy_import_tests.test_module
    ''', name='lazy_module')
    # This should proxy to the ScopeReplacer object,
    # not yet to the replaced object
    test_module = lazy_module
    # Beginning of test_ScopeReplacer___getattribute__
    # The following should refer to the object imported by lazy_module
    # Even though test_module refers directly to lazy_module, __getattribute__
    # should be called to replace the object.
    assert test_module.test_module_constant == 42

# Generated at 2022-06-14 06:08:48.352799
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__() should return unicode when possible."""
    sr = IllegalUseOfScopeReplacer('foo', 'bar')
    # We don't test the contents because it might change with gettext
    assert type(sr.__unicode__()) is unicode



# Generated at 2022-06-14 06:08:58.578416
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """testing method IllegalUseOfScopeReplacer.__str__"""
    # IllegalUseOfScopeReplacer.__str__ takes no arguments
    obj = IllegalUseOfScopeReplacer('name', 'msg')
    # we expect these to succeed
    obj.__str__()
    str(obj)
    # we expect these to fail
    raises(TypeError, obj.__str__, 1)
    raises(TypeError, str, obj, 1)


try:
    from bzrlib._lazy_import import (
        ScopeReplacer,
        lazy_import,
        _lazy_import,
        _lazy_import_funcs,
        )
except ImportError as e:
    # We don't have pyrex, so python-only code will have to be used
    # instead
    ScopeReplacer = object


# Generated at 2022-06-14 06:09:11.836066
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    from bzrlib.lazy_import import lazy_import
    # Unit test for method __call__ of class ScopeReplacer
    """bare bound method accepts one argument"""
    def test_method(arg):
        return arg
    lazy_import(locals(), "from bzrlib.lazy_import import ScopeReplacer")
    method_proxy = ScopeReplacer(locals(), test_method, "method_proxy")
    assert method_proxy("arg") == "arg"
    # Unit test for method __call__ of class ScopeReplacer
    """bare bound method accepts two arguments"""
    def test_method(arg, arg2):
        return arg, arg2
    method_proxy = ScopeReplacer(locals(), test_method, "method_proxy")

# Generated at 2022-06-14 06:09:21.754926
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__ should return unicode"""
    exc = IllegalUseOfScopeReplacer('my_name', 'my_msg', 'my_extra')
    result = exc.__unicode__()
    from bzrlib.i18n import gettext
    expected = gettext('ScopeReplacer object %(name)r was used incorrectly'
        ': %(msg)s%(extra)s')
    expected = expected % dict(name='my_name', msg='my_msg', extra=': my_extra')
    if not isinstance(result, unicode):
        raise AssertionError("IllegalUseOfScopeReplacer.__unicode__ should"
            " return a unicode object, but returned a %r"
            % type(result))

# Generated at 2022-06-14 06:09:25.946232
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """IllegalUseOfScopeReplacer.__str__()

    >>> IllegalUseOfScopeReplacer('a', 'b').__str__()
    'IllegalUseOfScopeReplacer object a was used incorrectly: b'
    """



# Generated at 2022-06-14 06:09:32.986284
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """IllegalUseOfScopeReplacer.__str__()

    IllegalUseOfScopeReplacer.__str__() should return either a str or
    unicode object, never anything else.
    """
    e = IllegalUseOfScopeReplacer('e1', 'exception message')
    assert not isinstance(e, unicode)
    assert isinstance(e, str)
    e2 = eval(repr(e))
    assert e == e2
