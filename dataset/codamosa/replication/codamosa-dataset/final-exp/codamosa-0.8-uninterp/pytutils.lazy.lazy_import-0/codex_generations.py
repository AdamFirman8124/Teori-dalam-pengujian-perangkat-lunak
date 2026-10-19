

# Generated at 2022-06-14 05:59:53.378176
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """Test method __str__ of class IllegalUseOfScopeReplacer."""
    e = IllegalUseOfScopeReplacer(name='foo', msg='bar')
    assert str(e) == 'foo: bar'



# Generated at 2022-06-14 06:00:00.412371
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    from bzrlib.tests import TestCase
    import bzrlib.lazy_import as _mod_lazy_import
    class TestScopeReplacer(TestCase):
        def test___setattr__(self):
            _mod_lazy_import._should_proxy = True
            def _factory(self, scope, name):
                return 'VALUE'
            scope = {}
            obj = _mod_lazy_import.ScopeReplacer(scope, _factory, 'obj')
            self.assertEqual('VALUE', obj())
            self.assertEqual('VALUE', scope['obj'])
            return
    return

# Generated at 2022-06-14 06:00:09.459381
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """Assert that IllegalUseOfScopeReplacer.__str__() returns a str object.

    The __str__() method should always return a str object, never a unicode
    object.
    """
    e = IllegalUseOfScopeReplacer('name', 'msg', 'extra')
    from bzrlib.i18n import gettext
    e._fmt = '%(msg)s'
    s = e.__str__()
    if isinstance(s, unicode):
        raise AssertionError('%r.__str__() should return a str object, not '
                             'a unicode object.' % e)
    assert s == gettext('msg')



# Generated at 2022-06-14 06:00:13.358118
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """The method __str__ of class IllegalUseOfScopeReplacer returns a string"""
    instance = IllegalUseOfScopeReplacer('name', 'msg')
    assert isinstance(instance.__str__(), str)



# Generated at 2022-06-14 06:00:24.451600
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    """Unit test for method __setattr__ of class ScopeReplacer."""
    import unittest

    class TestCase(unittest.TestCase):

        def test_ScopeReplacer___setattr__(self):
            from bzrlib.lazy_import import lazy_import, ScopeReplacer
            ScopeReplacer._should_proxy = False
            global_scope = {}
            lazy_import(global_scope, '''
            from bzrlib.lazy_import import NotImplemented
            ''')
            global_scope["NotImplemented"] = "Original value for NotImplemented"
            self.assertEqual("Original value for NotImplemented",
                             global_scope["NotImplemented"])

# Generated at 2022-06-14 06:00:27.360189
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    """Tests for method ScopeReplacer.__call__"""
    raise UnitTestSkipped('Not Yet Implemented')


# Generated at 2022-06-14 06:00:36.113726
# Unit test for method __getattribute__ of class ScopeReplacer
def test_ScopeReplacer___getattribute__():
    # test getattr
    def factory(a, b, c):
        return a, b, c
    import sys
    a = ScopeReplacer(sys.modules, factory, 'bzrlib')
    res = a.__getattribute__('_factory')
    assert res == factory, 'bad object'
    # test getattr
    res = a.bzrlib
    assert res == ('bzrlib', sys.modules, 'bzrlib'), 'bad object'



# Generated at 2022-06-14 06:00:44.171616
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """Unit test for method __str__ of class IllegalUseOfScopeReplacer.

    This test is in lazy_import because IllegalUseOfScopeReplacer is used
    by a bunch of imports.
    """
    import bzrlib.trace
    bzrlib.trace.enable_default_logging()
    bzrlib.trace.mutter("this is a mutter")

# Generated at 2022-06-14 06:00:55.568944
# Unit test for method __getattribute__ of class ScopeReplacer
def test_ScopeReplacer___getattribute__():
    import bzrlib.lazy_import
    bzrlib.lazy_import._should_proxy = False
    import bzrlib.trace
    try:
        bzrlib.trace._bzr_trace_logger._bzr_log_file
    except IllegalUseOfScopeReplacer:
        pass
    else:
        raise AssertionError
    import bzrlib.trace
    from bzrlib.trace import _bzr_trace_logger
    try:
        _bzr_trace_logger._bzr_log_file
    except IllegalUseOfScopeReplacer:
        pass
    else:
        raise AssertionError
    bzrlib.lazy_import._should_proxy = True
test_ScopeReplacer___getattribute__()



# Generated at 2022-06-14 06:01:06.781915
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    # XXX: tests for translations would be great
    # IllegalUseOfScopeReplacer is a subclass of Exception.
    # __str__ must return a str.
    # __unicode__ must return a unicode object.
    # It is not possible to write a test that catches the case when __str__
    # or __unicode__ return something which is not a str or a unicode object.
    s = str(IllegalUseOfScopeReplacer('foo', 'bar'))
    u = unicode(IllegalUseOfScopeReplacer('foo', 'bar'))
    raise TestNotApplicable('Not testable as there is no exception in a '
                            'string comparison.')



# Generated at 2022-06-14 06:01:20.972847
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    """__call__() -> None"""
    import unittest
    import traceback
    s = unittest.TestSuite()
    try:
        import bzrlib.tests as tests
        s.addTest(tests.test_suite())
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()
    unittest.TextTestRunner().run(s)

# Generated at 2022-06-14 06:01:32.321670
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """IllegalUseOfScopeReplacer.__str__() should return a str
    
    It uses a format string if it exists, or else calls the method 
    _get_format_string, or else it returns a default
    message. In all cases, the returned value is expected to be a str.
    
    This test fails when unicode is returned.
    """
    import sys
    class MyException(IllegalUseOfScopeReplacer):
        _fmt = "foo %(name)s"
    e = MyException('bar', 'msg')
    assert isinstance(str(e), str)
    assert isinstance(str(e), unicode)

    class MyException2(IllegalUseOfScopeReplacer):
        def _get_format_string(self):
            return 'foo'
    e = MyException2('bar')


# Generated at 2022-06-14 06:01:40.829259
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    # list of (input, output) pairs.
    # empty input list stands for instance creation
    test_data = [
        ([('foo', (1, 2, 3))], # input
         [1, 2, 3]),           # output
        ([('foo', ((1, 2, 3),))], # input
         [1, 2, 3]),           # output
        ]
    for (args_list, want_result) in test_data:
        obj = ScopeReplacer({}, lambda *a:a[0], 'mysr')
        got_result = obj(*args_list)

# Generated at 2022-06-14 06:01:48.613361
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__ should return a unicode of the original message"""
    e = IllegalUseOfScopeReplacer(name='name', msg='msg', extra='extra')
    u = unicode(e)
    assert isinstance(u, unicode), "%r is not unicode" % u
    assert u == 'ScopeReplacer object \'name\'' \
                ' was used incorrectly:' \
                ' msg: extra'



# Generated at 2022-06-14 06:02:02.820900
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    import sys
    from bzrlib.tests import TestCase
    from bzrlib.lazy_import import lazy_import
    from bzrlib.lazy_import import ScopeReplacer

    class TestScopedReplace(TestCase):
        def test_set_attribute(self):
            # calling ScopeReplacer.__setattr__() should replace the object
            # with a ScopeReplacer instance
            global mod_a
            class mod_a:
                x = 'mod_a.x'
            lazy_import(sys.modules[__name__], 'mod_a')
            self.assertIsInstance(mod_a, ScopeReplacer)
            mod_a.x = 'mod_a.x'
            self.assertEqual('mod_a.x', mod_a.x)

# Generated at 2022-06-14 06:02:14.884285
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    from bzrlib._simple_set import _simple_set

    # test_no_proxying
    o = ScopeReplacer(dict(), _simple_set, 'foo')
    o.foo = 'bar'
    try:
        o.foo = 'baz'
    except TypeError:
        pass
    else:
        raise AssertionError

    # test_proxied_obj
    ScopeReplacer._should_proxy = True
    o = ScopeReplacer(dict(), _simple_set, 'foo')
    o.foo = 'bar'
    o.foo = 'baz'
    if o.foo != 'baz':
        raise AssertionError
    if o.__dict__.keys() != ['foo']:
        raise AssertionError



# Generated at 2022-06-14 06:02:21.748007
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    # __call__: (...) -> Any.  Call this object as a function.

    # Note that this is a *method* so requires an instance as the first arg
    # (self).
    instance = ScopeReplacer(scope={}, factory=lambda _, scope, name: scope,
                             name='')
    result = instance.__call__()
    # A function call should return a value
    assert result is not None
test_ScopeReplacer___call__()



# Generated at 2022-06-14 06:02:30.376256
# Unit test for method __getattribute__ of class ScopeReplacer
def test_ScopeReplacer___getattribute__():
    global _result
    _result = None
    class A(ScopeReplacer):
        def a(self):
            global _result
            _result = ("inside A.a")
    a = A({}, lambda self,scope,name:self, "a")
    a.a()
    assert(_result == "inside A.a")
    try:
        a.b()
        assert(False)
    except Exception as e:
        assert(str(e) == "has no attribute 'b'")

# Generated at 2022-06-14 06:02:36.183549
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__ must return a unicode object."""
    from bzrlib import lazy_import
    error = lazy_import._IllegalUseOfScopeReplacer('test', 'msg')
    result = error.__unicode__()
    if not isinstance(result, unicode):
        raise AssertionError("__unicode__ must return a unicode object.")



# Generated at 2022-06-14 06:02:41.398098
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """Unit test for method __str__ of class IllegalUseOfScopeReplacer"""
    # __str__ should return a str() object.
    e = IllegalUseOfScopeReplacer('foo', 'bar', 'the extra')
    result = str(e)
    if not isinstance(result, str):
        raise AssertionError('result is not of str type %r' % (result,))


# Generated at 2022-06-14 06:02:49.510526
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    raise NotImplementedError


# Generated at 2022-06-14 06:02:57.018487
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """IllegalUseOfScopeReplacer.__str__ should produce a str object"""
    exc = IllegalUseOfScopeReplacer('name', 'msg', 'extra')
    r = exc.__str__()
    assert isinstance(r, str), "IllegalUseOfScopeReplacer.__str__ should" \
        " produce a str object, %s was returned instead" % (type(r),)

# Generated at 2022-06-14 06:03:10.973966
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """Unit test for method __str__ of class IllegalUseOfScopeReplacer"""

    class MyIllegalUseOfScopeReplacer(IllegalUseOfScopeReplacer):
        """Test class"""

    def check(lazy_obj, obj):
        """Check that a lazy object matches the expected object"""
        # The object should have the expected attributes
        for attr in dir(obj):
            if not attr.startswith('__'):
                # Check the attribute's value
                obj_value = getattr(obj, attr)
                lazy_obj_value = getattr(lazy_obj, attr)

# Generated at 2022-06-14 06:03:22.693901
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    # ScopeReplacer.__call__() -> <object>.__call__(*args, **kwargs)
    # __call__ is called for all functions, so delegate to the actual
    # function object.
    def factory(self, scope, name):
        def myfn():
            return name
        return myfn
    scope = {}
    # Assign object to name 's'
    s = ScopeReplacer(scope, factory, 's')
    e = 's'
    a = s()
    assertEquals(a, e)
    # Check assignment happened in scope
    e = myfn = factory(None, None, None)
    a = s._real_obj
    assertEquals(a, e)
    a = s._scope['s']
    assertEquals(a, e)

    # Check that existing objects are returned


# Generated at 2022-06-14 06:03:26.278008
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """__str__ is overridden, so just call it"""
    e = IllegalUseOfScopeReplacer('foo', 'bar')
    str(e)



# Generated at 2022-06-14 06:03:40.099745
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    import bzrlib.lazy_import
    import bzrlib.trace
    l = {}
    class b(object):
        def __init__(self):
            self.a = None
    class c(object):
        trace = None
    bzrlib.lazy_import.lazy_import(l, '''
    import bzrlib.trace
    ''')
    assert l['trace']._real_obj is None
    assert l['trace']._should_proxy
    l['trace'] = bzrlib.trace.Note()
    assert l['trace']._real_obj is None
    assert not l['trace']._should_proxy
    del l['trace']
    assert 'trace' not in l
    l['trace'] = bzrlib.trace.Note()

# Generated at 2022-06-14 06:03:51.762780
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    from bzrlib.tests import TestCase
    from bzrlib.lazy_import import lazy_import, ScopeReplacer
    import sys
    import os

# Generated at 2022-06-14 06:04:03.164941
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    import bzrlib.lazy_import
    reload(bzrlib.lazy_import)
    from bzrlib.lazy_import import lazy_import, ScopeReplacer
    ScopeReplacer._should_proxy = True
    def get_diagnostic():
        # Setup
        scope = {}
        factory = lambda self, scope, name: None
        lazy_import(scope, 'root = bzrlib.lazy_import.ScopeReplacer(scope, factory, "root")')
        # Exercise
        try:
            root.root = None # doctest: +ELLIPSIS
        except AttributeError as e:
            # Verify
            msg = str(e)
            return msg
    expected_result = 'root'

# Generated at 2022-06-14 06:04:16.606536
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    # Test the __unicode__ method of the IllegalUseOfScopeReplacer class
    def check(string):
        """Check if the string gives the expected kind of exception."""
        obj = IllegalUseOfScopeReplacer('some_name', string)
        unicode(obj)

    check('Some error')

    # Test the correct handling of the exception when _fmt is not defined.
    class TestException(Exception):
        def _get_format_string(self):
            return None
    check(TestException('Some other exception'))

    # Test the correct handling of the exception when _get_format_string()
    # returns None.
    class TestException2(Exception):
        def _get_format_string(self):
            return None
    check(TestException2('Some other exception'))



# Generated at 2022-06-14 06:04:24.250638
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    import bzrlib.lazy_import
    bzrlib.lazy_import.lazy_import(globals(), '''
        import bzrlib.testament
    ''')
    # Using a callable that returns a different result each time
    def _factory():
        ret = _factory.calls
        _factory.calls += 1
        return ret
    testament = bzrlib.testament
    _factory.calls = 0
    bzrlib.lazy_import.ScopeReplacer({}, _factory, 'testament')
    assert testament() == 0
    assert testament() == 1
    assert testament() == 2
    # Calling this after it's been resolved returns the same value

# Generated at 2022-06-14 06:04:38.653677
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """Unit test for method __unicode__ of class IllegalUseOfScopeReplacer"""
    # Test that if the class contains an str attribute _preformatted_string, it
    # is returned as a unicode object
    e = IllegalUseOfScopeReplacer('name', 'msg')
    # This can't be tested since we don't know the encoding here, but at least
    # this works for ascii strings
    e._preformatted_string = 'str'
    assert(isinstance(e.__unicode__(), unicode))

    # Test that when _preformatted_string is not an str, it is converted to an
    # str and then to a unicode object
    e = IllegalUseOfScopeReplacer('name', 'msg')
    e._preformatted_string = 1.0

# Generated at 2022-06-14 06:04:44.588205
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """Unit test for method __unicode__ of class IllegalUseOfScopeReplacer"""
    sr = IllegalUseOfScopeReplacer('foo', 'bar')
    # TODO: this test is weak
    self.assertEndsWith(unicode(sr), 'ScopeReplacer object \'foo\' was '
                                 'used incorrectly: bar')



# Generated at 2022-06-14 06:04:48.573451
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """__str__ must return a str instance"""
    exception = IllegalUseOfScopeReplacer(name='name', msg='msg')
    assert isinstance(str(exception), str)


# Generated at 2022-06-14 06:04:56.521158
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    import tempfile
    import os
    import shutil

    old_dir = os.getcwd()
    curr_dir = tempfile.mkdtemp()
    def cleanup():
        os.chdir(old_dir)
        shutil.rmtree(curr_dir)

    os.chdir(curr_dir)

    from bzrlib.tests import TestCase, KnownFailure
    try:
        import bzrlib.workingtree
    except ImportError:
        raise KnownFailure('bzrlib.workingtree not built')

    from bzrlib.branch import Branch

    def factory(self, scope, name):
        from bzrlib import (
            workingtree,
            )
        # The test will try to call self.branch, which will call this
        # method, so set the value

# Generated at 2022-06-14 06:05:04.661806
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    """__setattr__ creates a real object if needed"""
    class FakeScope(dict):
        def __setitem__(self, key, value):
            self.key = key
            self.value = value

    class FakeObject(object):
        def __setattr__(self, key, value):
            self.key = key
            self.value = value

    def factory(self, scope, name):
        return FakeObject()

    scope = FakeScope()
    replacer = ScopeReplacer(scope, factory, 'name')
    replacer.attr = 'value'
    assert scope.key == 'name'
    assert scope.value.key == 'attr'
    assert scope.value.value == 'value'



# Generated at 2022-06-14 06:05:15.571668
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    import sys
    import tempfile
    sys.path.append(tempfile.gettempdir())
    class test_class(object):
        pass
    tc_instance = test_class()
    sr_instance = ScopeReplacer(sys.modules, (lambda self, scope, name: tc_instance), 'fake_class')
    for i in range(4):
        try:
            sr_instance.fake_attr = 'abc'
        except IllegalUseOfScopeReplacer:
            pass
        else:
            break
        if i == 0:
            # First call will succeed as this object hasn't been resolved yet
            pass
        elif i == 1:
            ScopeReplacer._should_proxy = False
            # Second call will always fail as proxying is disabled
        elif i == 2:
            ScopeReplacer._should_proxy = True


# Generated at 2022-06-14 06:05:21.808441
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """Method test_IllegalUseOfScopeReplacer___unicode__ of class IllegalUseOfScopeReplacer."""
    obj = IllegalUseOfScopeReplacer(None, None)
    s = unicode(obj)
    # The string is a string, not a unicode object.
    # On py3k, this might change; we don't have a __bytes__ method
    # for the exception.
    assert isinstance(s, str), repr(s)



# Generated at 2022-06-14 06:05:24.312697
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    if not hasattr(ScopeReplacer, '__call__'):
        yield skipped("class ScopeReplacer has no method __call__")
    obj = ScopeReplacer.__call__
    yield "Not implemented"

# Generated at 2022-06-14 06:05:38.029857
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """Unit test for IllegalUseOfScopeReplacer.__unicode__"""
    # The following makes more sense when read backwards.
    # List of pairs (object to format, expected string)

# Generated at 2022-06-14 06:05:43.208406
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """__str__ returns a str object not a unicode object"""
    e = IllegalUseOfScopeReplacer("lazy_import", "foo")
    s = str(e)
    import types
    assert isinstance(s, types.StringType), \
        '__str__ must return a str object got a %s' % type(s)



# Generated at 2022-06-14 06:06:18.971509
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    """Unit test for method __setattr__ of class ScopeReplacer"""

    import bzrlib
    import os

    mod_name = "bzrlib.tests.test_lazy_import"
    class Bar:
        pass
    b = Bar()
    def factory(self, scope, name):
        old_obj = self._scope[name]
        assert isinstance(old_obj, ScopeReplacer)
        assert old_obj._scope is scope
        assert old_obj._name == name
        assert old_obj._factory is factory
        try:
            return os.tmpnam
        except NameError:
            return b
    globals_vars = {}
    globals_vars["lazy_import"] = lazy_import

# Generated at 2022-06-14 06:06:26.074421
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """Method __unicode__ of class IllegalUseOfScopeReplacer must return
    a unicode object.
    """
    e = IllegalUseOfScopeReplacer('name', 'msg')
    u = e.__unicode__()
    assert isinstance(u, unicode), ("Must return a unicode object, but got: %r"
                                    % (u,))


# Generated at 2022-06-14 06:06:27.455198
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """This method is not tested, should it ?"""



# Generated at 2022-06-14 06:06:36.973321
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """Unit test for method '__str__' of class 'IllegalUseOfScopeReplacer'"""
    i = IllegalUseOfScopeReplacer("bad thing", "it exploded")
    str(i)
    i = IllegalUseOfScopeReplacer("bad thing", "it exploded", {'a':1})
    str(i)
    i = IllegalUseOfScopeReplacer("bad thing", "it exploded", ['a',1])
    i.__str__()
# end of test for method __str__ of class IllegalUseOfScopeReplacer



# Generated at 2022-06-14 06:06:45.137321
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """__str__() should always return the same thing as unicode(self)"""
    try:
        # Can we encode the unicode string as US-ASCII?
        (IllegalUseOfScopeReplacer('name', 'msg').__str__().
            encode('ascii'))
        s = '%r.__str__() is a str, not unicode'
    except UnicodeEncodeError:
        # No - __str__() does not return the same thing as unicode(self)
        s = '%r.__str__() is unicode, not a str'
    assert False, s % IllegalUseOfScopeReplacer



# Generated at 2022-06-14 06:06:57.355590
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """Return format string for this exception or None"""
    # Tests for method __str__ of class IllegalUseOfScopeReplacer
    # See http://bugs.python.org/issue1469 for more details
    from cStringIO import StringIO # pyflakes.ignore
    from bzrlib.i18n import gettext
    from bzrlib.lazy_import import IllegalUseOfScopeReplacer
    import sys
    import traceback
    # Set a default encoding, because it may have been set to
    # bzrlib.user_encoding during the test run, and then the
    # str() repr will have to use that encoding and fail
    # because the default encoding is always ascii
    import locale
    locale.setlocale(locale.LC_ALL, 'C')

# Generated at 2022-06-14 06:07:06.851174
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """This method is being tested implicitly by calling
    str() on the object.
    """
    scope_replacer = IllegalUseOfScopeReplacer('name', 'msg', extra='extra')
    str(scope_replacer)
    scope_replacer._fmt = "fmt %(name)s"
    str(scope_replacer)
    scope_replacer._fmt = "fmt %(msg)s"
    str(scope_replacer)
    scope_replacer._fmt = "fmt %(extra)s"
    str(scope_replacer)
    scope_replacer._fmt = "fmt %(something_not_present)s"
    str(scope_replacer)

# Generated at 2022-06-14 06:07:13.386116
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    """__call__ should return the result of calling the original object.

    >>> scope = {}
    >>> name = 'name'
    >>> def factory(self, scope, name):
    ...     return "my object"
    >>> s = ScopeReplacer(scope, factory, name)
    >>> s('foo', bar='baz')
    'my object'
    """

    pass



# Generated at 2022-06-14 06:07:24.550330
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    from testtools.matchers import Equals
    from bzrlib.tests import TestCase

    class TestScopeReplacer(TestCase):

        def test_ScopeReplacer_set_attribute(self):
            class TestClass(object):
                def __init__(self):
                    self._attr = None

                def set_attr(self, value):
                    self._attr = value

            scope = {}

            def factory(self, scope, name):
                obj = TestClass()
                return obj

            sr = ScopeReplacer(scope, factory, 'obj')
            attr_name = '_attr'
            value = 'value'
            sr.set_attr(value)
            matcher = Equals(value)
            self.assertThat(sr._attr, matcher)
            self.assertIs(scope['obj'], sr)


# Generated at 2022-06-14 06:07:33.975708
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    from sys import getdefaultencoding, setdefaultencoding, stdout
    defaultencoding = getdefaultencoding()
    for enc in ['ascii', 'latin1']:
        setdefaultencoding(enc)
        obj = IllegalUseOfScopeReplacer('name', 'msg', 'extra')
        try:
            obj.__unicode__()
        except UnicodeDecodeError:
            print >>stdout, \
                "Shouldn't be a UnicodeDecodeError in %s encoding" % enc

    setdefaultencoding(defaultencoding)



# Generated at 2022-06-14 06:07:57.534688
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    from bzrlib.tests import TestCase

    class ModuleProxy(ScopeReplacer):
        def __init__(self, modname):
            self.modname = modname
            super(ModuleProxy, self).__init__(globals(),
                    module_factory, modname)

        def _resolve(self):
            if self.modname not in sys.modules:
                __import__(self.modname)
            return sys.modules[self.modname]

    def module_factory(modname, scope, name):
        return ModuleProxy(modname)

    class TestCallReplacer(TestCase):

        def test_simple(self):
            foo = ModuleProxy('bzrlib.lazy_import')
            self.assertEqual('lazy_import', foo.__name__)

    TestCallRepl

# Generated at 2022-06-14 06:08:09.194019
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    def _factory(self, scope, name):
        return self
    from bzrlib.tests import (
        SyntheticTestCase,
        )
    from bzrlib import lazy_import
    lazy_import.ScopeReplacer._should_proxy = True
    self = SyntheticTestCase
    scope = {}
    name = 'blah'
    self.assertRaises(lazy_import.IllegalUseOfScopeReplacer,
                      lazy_import.ScopeReplacer,
                      scope, _factory, name)
    lazy_import.ScopeReplacer._should_proxy = False
    self.assertRaises(lazy_import.IllegalUseOfScopeReplacer,
                      lazy_import.ScopeReplacer,
                      scope, _factory, name)



# Generated at 2022-06-14 06:08:16.046220
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """Check that __str__() is returning a str object and not a unicode
    object.
    """
    e = IllegalUseOfScopeReplacer('foo', 'bar')
    if isinstance(e.__str__(), unicode):
        raise AssertionError("__str__() should not return a unicode object.")


try:
    import cStringIO as StringIO
except ImportError:
    import StringIO  # pyflakes.ignore



# Generated at 2022-06-14 06:08:21.072058
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """
    Test __str__() and __unicode__() methods of IllegalUseOfScopeReplacer.
    """
    import doctest
    from bzrlib.lazy_import import IllegalUseOfScopeReplacer
    doctest.testmod(IllegalUseOfScopeReplacer)



# Generated at 2022-06-14 06:08:30.851832
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    f = lambda a: lambda b: a+b
    g = f(1)
    def get_attr(*args, **kwargs):
        obj = object.__getattribute__(self, '_resolve')()
        return getattr(obj, attr)
    attr = '_resolve'
    scope = {}
    name = 'f'
    scope[name] = ScopeReplacer(scope, get_attr, name)
    assert scope[name](3) == 4
    return
test_ScopeReplacer___call__()


# Generated at 2022-06-14 06:08:35.785682
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """IllegalUseOfScopeReplacer.__unicode__"""
    msg = 'error message'
    name = 'replacer name'
    error = IllegalUseOfScopeReplacer(name, msg)
    assert unicode(error) == u'error message'

# Generated at 2022-06-14 06:08:47.092303
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    if not hasattr(ScopeReplacer, '_should_proxy'):
        raise AssertionError("ScopeReplacer._should_proxy not found.")
    # call __setattr__ on the class.
    # it should have the same effect as on an instance.
    obj = object()
    class ScopeReplacerSubclass(ScopeReplacer): pass
    def factory(self, scope, name): return obj
    scope = {}
    name = 'name'
    replacer = ScopeReplacerSubclass(scope, factory, name)
    def do_setattr(replacer):
        replacer.attr = 1
    do_setattr(replacer)
    replacer = scope[name]

# Generated at 2022-06-14 06:08:58.316649
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """__str__(self) of IllegalUseOfScopeReplacer should return a str

    This test will only pass if the dict used in IllegalUseOfScopeReplacer
    contains byte strings. Note that IllegalUseOfScopeReplacer does not
    subclass UnicodeError so we do not need unicode aware keys in this
    class's dict.
    """
    obj = IllegalUseOfScopeReplacer('name', 'msg')
    if isinstance(obj.__str__(), unicode):
        raise AssertionError("__str__ should return a str, got %s" % obj.__str__())

# Generated at 2022-06-14 06:09:02.729104
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """str(IllegalUseOfScopeReplacer('x', 'y')) -> 'y'"""
    e = IllegalUseOfScopeReplacer('x', 'y')
    str(e) == 'y'



# Generated at 2022-06-14 06:09:14.558190
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    from bzrlib import lazy_import
    import bzrlib
    old_items = lazy_import._scope_cache.items()
    lazy_import._scope_cache = {}