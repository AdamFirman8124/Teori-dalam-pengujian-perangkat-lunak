

# Generated at 2022-06-14 05:59:58.883048
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    import bzrlib
    new_bzrlib = bzrlib.lazy.make_scope_replacer(
        'bzrlib', lambda: 'new bzrlib')

# Generated at 2022-06-14 06:00:09.692860
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """Test __str__ method of class IllegalUseOfScopeReplacer"""
    x = IllegalUseOfScopeReplacer('x', 'y')
    y = IllegalUseOfScopeReplacer(u'x', u'y')
    z = IllegalUseOfScopeReplacer(u'x', u'y')

    assert x == y
    assert y == x
    assert x != z
    assert y != z
    assert str(x) == str(y)
    assert str(y) == str(x)
    assert str(x) != str(z)
    assert str(y) != str(z)
    assert unicode(x) == unicode(y)
    assert unicode(y) == unicode(x)
    assert unicode(x) != unicode(z)
    assert unicode(y) != unicode(z)



# Generated at 2022-06-14 06:00:16.733508
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """Unit test for method __unicode__ of class IllegalUseOfScopeReplacer"""
    # __unicode__ should return a unicode string, not a utf-8 encoded str
    exc = IllegalUseOfScopeReplacer('name', 'message')
    s = exc.__unicode__()
    if isinstance(s, str):
        raise AssertionError("__unicode__ returned a str")


# Generated at 2022-06-14 06:00:21.301980
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """IllegalUseOfScopeReplacer___str__ returns a string."""
    f = IllegalUseOfScopeReplacer('foo', 'Bar!')
    s = str(f)
    assert isinstance(s, str), "__str__() did not return a string."


# Generated at 2022-06-14 06:00:23.523453
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    l = IllegalUseOfScopeReplacer('name', 'msg', 'extra')
    unicode(l)



# Generated at 2022-06-14 06:00:37.084890
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    def test_func(a, b=3, c=4, d=5):
        return a, b, c, d
    scope = {}
    lazy_import(scope, '''
    from bzrlib.tests import test_lazy_import
    ''')
    factory = scope['test_func']
    name = 'test_func'
    obj = ScopeReplacer(scope, factory, name)
    # Test correct call
    result = obj(1)
    assert result == (1, 3, 4, 5)
    result = obj(1, 2)
    assert result == (1, 2, 4, 5)
    result = obj(1, 2, 3)
    assert result == (1, 2, 3, 5)
    result = obj(1, 2, 3, 4)

# Generated at 2022-06-14 06:00:42.396352
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    from bzrlib import lazy_import
    lazy_import(globals(), '''
    from bzrlib import (
        bzrdir,
        )
    ''')

    # XXX: The following test is not py3k compat, because bzrdir.BzrDir
    # is no longer a new style class.
    # test calling the class
    assert bzrdir.BzrDir() is not None



# Generated at 2022-06-14 06:00:54.453360
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():

    def test_calling_setattr_on_attribute_of_already_replaced_object_causes_error():
        from bzrlib.lazy_import import lazy_import
        # set a known value
        class_setattr_called = []
        class ClassToImplement(object):
            def __setattr__(self, attr, value):
                class_setattr_called.append(attr)
        obj = ClassToImplement()
        # ScopeReplacer _resolve() should return obj, not self
        def factory(self, scope, name):
            return obj
        globals = {}
        name = 'lazy_import_test_obj'
        new_obj = ScopeReplacer(globals, factory, name)
        obj.attr_to_set = 'value_to_set'
        exception_raised

# Generated at 2022-06-14 06:01:03.693367
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    """Check if static property _should_proxy is honoured.
    """
    class Foo(object): pass
    foo = Foo()
    foo.attr = 42
    class ScopeReplacer1(ScopeReplacer):
        _should_proxy = True
    foo.ScopeReplacer = ScopeReplacer1
    foo.ScopeReplacer('foo', lambda self, scope, name: Foo(), 'foo_scope')
    foo_scope = foo.foo_scope
    try:
        foo_scope.attr = 43
    except IllegalUseOfScopeReplacer:
        e = sys.exc_info()[1]
        if str(e).find('Object already replaced') == -1:
            raise
    else:
        raise AssertionError(
            "ScopeReplacer did not reject set upon fq name using _should_proxy")

# Generated at 2022-06-14 06:01:13.530391
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    from bzrlib.tests.test_lazy_import import TestCase
    def check(msg, name, value):
        exc = IllegalUseOfScopeReplacer(msg, name, value)
        expected = "IllegalUseOfScopeReplacer('%s', '%s', '%s')" \
            % (msg, name, value)
        got = str(exc)

# Generated at 2022-06-14 06:01:28.355720
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """IllegalUseOfScopeReplacer.__str__() should be reentrant.

    We test this by creating an exception instance and
    then calling .__str__ on the .__str__ result.
    """
    try:
        raise IllegalUseOfScopeReplacer('my name', 'my message')
    except IllegalUseOfScopeReplacer:
        s = str(sys.exc_info()[1])
        str(s)

# Generated at 2022-06-14 06:01:33.044229
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """Test method __str__ of class IllegalUseOfScopeReplacer."""
    o = IllegalUseOfScopeReplacer('name', 'msg')
    s = str(o)
    assert s == "ScopeReplacer object 'name' was used incorrectly: msg", s



# Generated at 2022-06-14 06:01:41.182102
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """Test method __unicode__ of class IllegalUseOfScopeReplacer

    This method tests the method __unicode__ of class IllegalUseOfScopeReplacer
    which is capable of converting the exception object into a unicode
    string.
    """
    import sys
    if sys.version_info < (3, 0):
        _error_class = UnicodeError
    else:
        _error_class = UnicodeEncodeError
    e = IllegalUseOfScopeReplacer('test name', 'test msg')
    u = e.__unicode__()
    # 'u' must be a unicode string
    # will fail if '__unicode__' does not return a unicode string

# Generated at 2022-06-14 06:01:47.920228
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    u = unicode(IllegalUseOfScopeReplacer('foo', 'bar'))
    assert isinstance(u, unicode)
    u = unicode(IllegalUseOfScopeReplacer('foo', 'bar: %s %s', (1, 2)))
    assert isinstance(u, unicode)

# Generated at 2022-06-14 06:01:58.637983
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """__str__ of IllegalUseOfScopeReplacer should return a str, and not raise
    any exceptions.
    """
    # This test is here because the above method can raise
    # non-printable exceptions (like OverflowError) and we want to
    # ensure they don't do that. This method is pure, so it can be in
    # the class definition.
    e = IllegalUseOfScopeReplacer('test', 'foo')
    if isinstance(e.__str__(), unicode):
        raise AssertionError("__str__ of IllegalUseOfScopeReplacer returned "
                             "unicode")



# Generated at 2022-06-14 06:02:02.161134
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """__str__ method of IllegalUseOfScopeReplacer"""
    e = IllegalUseOfScopeReplacer('foo', 'msg', extra=None)
    str(e)



# Generated at 2022-06-14 06:02:07.021611
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    from bzrlib.lazy_import import lazy_import
    lazy_import(locals(), '''
    from bzrlib import osutils
    import sys
    ''')
    scope = locals()
    factory = lambda self, scope, name: scope[name]
    name = 'osutils'
    sr = ScopeReplacer(scope, factory, name)
    sr()



# Generated at 2022-06-14 06:02:11.822728
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """IllegalUseOfScopeReplacer.__unicode__() should return a unicode string."""
    err = IllegalUseOfScopeReplacer('name', 'msg')
    result = unicode(err)
    assert isinstance(result, unicode)



# Generated at 2022-06-14 06:02:18.596459
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    class TestableScopeReplacer(ScopeReplacer):
        def _resolve(self):
            return TestableScopeReplacer._resolve

    sr = TestableScopeReplacer(None, None, '')
    try:
        sr(1, 2, 3)
    except TestableScopeReplacer._resolve:
        pass
    else:
        raise AssertionError('Test failed')


# Generated at 2022-06-14 06:02:28.074268
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    # Test that _resolve() is only called on the first access to
    # _real_obj.
    from bzrlib.trace import mutter
    class test_instance(ScopeReplacer):
        pass
    
    
    
    
    
    
    
    
    
    def test_factory(self, scope, name):
        return self
    
    
    
    
    
    
    t = test_instance({}, test_factory, 'foo')
    # Mutter is called when ScopeReplacer is created
    mutter("%d mutters", 1)
    # Once per access to _real_obj
    mutter("%d mutters", 2)
    # Once per access to _real_obj
    mutter("%d mutters", 3)
    mutter("%d mutters", 4)


# Generated at 2022-06-14 06:02:45.182151
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    from bzrlib import lazy_import

    def factory(sr, scope, name):
        def my_method(arg):
            if arg == 'hello':
                return 'hello world'
            else:
                return 'unexpected'
        return my_method

    lazy_import.lazy_import(globals(), '''
    import bzrlib.lazy_import
    ''')

    bzrlib.lazy_import.lazy_import(globals(), '''
    my_method = bzrlib.lazy_import.ScopeReplacer(locals(), factory,
                                                 'my_method')
    ''')
    # This will have the effect of replacing my_method with the result of
    # the factory function.
    func = my_method
    #my_method is now callable

# Generated at 2022-06-14 06:02:55.204348
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    class TestScopeReplacer(ScopeReplacer):
        """A subclass of ScopeReplacer with a testable __setattr__ method."""
        def __init__(self, *args, **kwargs):
            ScopeReplacer.__init__(self, *args, **kwargs)
            self._calls = []

        def _resolve(self):
            self._calls.append('_resolve')
            obj = ScopeReplacer._resolve(self)
            obj._calls = self._calls
            return obj

        def __setattr__(self, attr, value):
            if attr == '_resolve':
                raise ValueError('_resolve cannot be set in a subclass.')
            self._calls.append('__setattr__(%r, %r)' % (attr, value))

# Generated at 2022-06-14 06:02:59.744162
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    # XXX: Should this raise an error about the __call__ method not existing?
    raise NotImplementedError(
        "Test case for method not implemented")

    # XXX: Implement test case for method __call__ of class ScopeReplacer



# Generated at 2022-06-14 06:03:08.866298
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    from bzrlib.lazy_import import ScopeReplacer

    scope = {}
    obj = ScopeReplacer(scope, lambda x, scope, name: scope, 'var')
    scope['var'] = obj
    def inner():
        scope = {}
        obj = ScopeReplacer(scope, lambda x, scope, name: scope, 'var')
        scope['var'] = obj
        def inner_inner():
            obj.attr = 2
        inner_inner()

    inner()
    obj.attr = 1




# Generated at 2022-06-14 06:03:16.224609
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """IllegalUseOfScopeReplacer.__unicode__"""
    import bzrlib.lazy_import
    er = bzrlib.lazy_import.IllegalUseOfScopeReplacer(
        'name', 'message', 'extra')
    expected_format = "ScopeReplacer object 'name' was used incorrectly:" \
                      " message: extra"
    er.__unicode__().should_be_like(expected_format)
    # Now try again when the locals already contain a format
    er._fmt = "Already here"
    er.__unicode__().should_be_like(expected_format)



# Generated at 2022-06-14 06:03:26.341172
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    class DummyScope(object):
        pass

    def factory(replacer, scope, name):
        class FakeThing(object):
            pass
        return FakeThing()

    class DummySysModule(object):
        """Made to look like the sys module.

        This dummy cannot actually be imported, but we only use it as a
        backing store here.
        """

        modules = {}

        @staticmethod
        def modules_get(module_name, default=None):
            return DummySysModule.modules.get(module_name, default)

        @staticmethod
        def modules_set(module_name, module):
            DummySysModule.modules[module_name] = module


# Generated at 2022-06-14 06:03:31.447445
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """Check that IllegalUseOfScopeReplacer.__str__() raises no uncaught exceptions
    """
    exc = IllegalUseOfScopeReplacer('s', 'm')
    # Check that the method does not raise an Exception
    str(exc)



# Generated at 2022-06-14 06:03:40.727327
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    class Foo(object):
        __slots__ = ["a", "b"]
    foo = Foo()
    foo.a = "a"
    foo.b = "b"
    exception = IllegalUseOfScopeReplacer("name", "msg", foo)
    reference = ("ScopeReplacer object 'name' was used incorrectly: msg: "
        "{'a': 'a', 'b': 'b'}")
    actual = exception.__str__()
    if actual != reference:
        raise AssertionError('Actual %r != Reference %r'
            % (actual, reference))



# Generated at 2022-06-14 06:03:49.836420
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    from bzrlib.tests import TestCase
    from bzrlib.lazy_import import lazy_import, ScopeReplacer
    import sys
    def _factory(self, scope, name):
        return self
    globals()['foo'] = ScopeReplacer(globals(), _factory, 'foo')
    test_case = TestCase()
    test_case.assertTrue(globals()['foo'] is foo())
test_ScopeReplacer___call__.unittest = ['.functest']



# Generated at 2022-06-14 06:04:00.663997
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    import bzrlib.tests
    e = IllegalUseOfScopeReplacer('replacer', 'msg', 'extra')
    bzrlib.tests.TestCaseWithTransport.assertEqualIgnoreLeadingWhitespace(
        'IllegalUseOfScopeReplacer(replacer, \'\'\'\n    msg: extra\n    \'\'\')',
        repr(e)
        )
    bzrlib.tests.TestCaseWithTransport.assertEqualIgnoreLeadingWhitespace(
        'IllegalUseOfScopeReplacer(replacer, \'\'\'\n    msg: extra\n    \'\'\')',
        unicode(e)
        )



# Generated at 2022-06-14 06:04:19.358593
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """IllegalUseOfScopeReplacer.__str__() should be fixed in Python 3"""
    # Check that in Python 3 the __str__ method of this Exception
    # returns a unicode string, but that in Python 2 it returns a str
    # containing encoded bytes.
    e = IllegalUseOfScopeReplacer('objname', 'msg')
    s = str(e)
    if isinstance(s, str):
        # expected for Python 2
        pass
    elif isinstance(s, unicode):
        raise AssertionError('%s.str() is unicode, expected str: %r'
                             % (e.__class__.__name__, s))

# Generated at 2022-06-14 06:04:25.562925
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """__str__ of IllegalUseOfScopeReplacer"""
    r = IllegalUseOfScopeReplacer("obj-name", "message", "extra")
    if str(r) != "message: extra":
        raise AssertionError("Wrong message")
test_IllegalUseOfScopeReplacer___str__()


# Generated at 2022-06-14 06:04:29.448181
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """__str__() should return str"""
    e = IllegalUseOfScopeReplacer(1, 2, 3)
    s = str(e)
    assert isinstance(s, str)

# Generated at 2022-06-14 06:04:32.005887
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """IllegalUseOfScopeReplacer.__unicode__() returns unicode strings"""
    e = IllegalUseOfScopeReplacer('FOO', 'BAR')
    u = unicode(e)
    assert isinstance(u, unicode)



# Generated at 2022-06-14 06:04:37.624484
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__ should return a unicode string"""
    # The exception's message should be a unicode object
    ex = IllegalUseOfScopeReplacer('ex1', 'message1')
    u = unicode(ex)
    if not isinstance(u, unicode):
        raise AssertionError('not a unicode object: %r' % (u,))
    # The object should support __str__
    s = str(ex)
    if not isinstance(s, str):
        raise AssertionError('not a str object: %r' % (s,))

# Generated at 2022-06-14 06:04:51.324950
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    try:
        from bzrlib.lazy_import import lazy_import, ScopeReplacer
    except ImportError:
        # Python 2.4 does not support "except ImportError, e:"
        import sys
        e = sys.exc_info()[1]
        raise ImportError("%s - required for testing" % (e,))
    import bzrlib.tests
    lazy_import(globals(), '''
    import bzrlib.tests
    ''')
    import doctest
    doctest.DocTestSuite(bzrlib.tests,
        globs={
            'lazy_import':lazy_import,
            'ScopeReplacer':ScopeReplacer,
            },
        checker=None,
        optionflags=doctest.NORMALIZE_WHITESPACE
        )



# Generated at 2022-06-14 06:05:03.796319
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """The string representation of an IllegalUseOfScopeReplacer must be
    fully informative.
    """
    import re
    e = IllegalUseOfScopeReplacer(
        'spam', 'The object cannot be found in the given scope.',
        '<KeyError: \'spam\'>')
    # check the main information is present
    assert re.match(
        'The object cannot be found in the given scope.: '
        '<KeyError: \'spam\'>', str(e))
    assert re.match(
        'The object cannot be found in the given scope.: '
        '<KeyError: \'spam\'>', repr(e))
    # but that it doesn't just go on a dump everything
    assert 'locals' not in repr(e)
    assert 'globals' not in repr(e)

# Generated at 2022-06-14 06:05:10.582869
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """__str__(IllegalUseOfScopeReplacer()) produces a valid str object

    In some places where we need a str, we cannot be sure that the
    str will not contain non-ascii characters.
    """
    from bzrlib import lazy_import
    import bzrlib.lazy_import
    lazy_import.lazy_import(locals(), '''
        from bzrlib import (
            errors,
            osutils,
            branch,
            )
        import bzrlib.branch
        ''')
    # no exceptions should be raised after this point

# Generated at 2022-06-14 06:05:22.753281
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """__str__ should support str as well as unicode input"""
    #__doc__ = IllegalUseOfScopeReplacer.__str__.__doc__

    from bzrlib import (
        errors,
        osutils,
        branch,
        )
    import bzrlib.branch
    _fmt = "ScopeReplacer object %(name)r was used incorrectly: %(msg)s%(extra)s"
    obj = errors.IllegalUseOfScopeReplacer('fred', 'msg')
    _expected = "fred: msg"
    _actual = str(obj)
    assert _actual == _expected, "_actual != _expected:\n_actual=%r\n_expected=%r" % (_actual, _expected)



# Generated at 2022-06-14 06:05:24.768538
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    import doctest
    doctest.run_docstring_examples(ScopeReplacer.__call__, globals())

# Generated at 2022-06-14 06:05:35.482930
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    from bzrlib import lazy_import
    import sys
    # set up scope
    lazy_import._scope_stack.append({})
    sys.modules['m'] = ScopeReplacer(
        scope=lazy_import._scope_stack[-1], factory=None, name='m')
    # do test
    import m
    m.__name__ = 'foo'
    m.__name__


# Generated at 2022-06-14 06:05:42.221057
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """__str__ must return a non unicode string"""
    e = IllegalUseOfScopeReplacer('foo', 'bar')
    foo = e.__str__()
    # __str__ must return a non unicode string.
    assert isinstance(foo, str), "__str__ must return a non unicode string."

# Generated at 2022-06-14 06:05:55.093543
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    import sys
    from bzrlib import lazy_import
    mod1 = sys.modules['bzrlib.lazy_import']
    del sys.modules['bzrlib.lazy_import']
    try:
        class mock:
            def __init__(self):
                self.called = False
            def __call__(self, *args, **kwargs):
                self.called = True
        scope = {}
        mock_obj = mock()
        lazy_import.lazy_import(scope, """
        x = mock_obj
        """)
        scope['x']()
        assert mock_obj.called
    finally:
        sys.modules['bzrlib.lazy_import'] = mod1



# Generated at 2022-06-14 06:06:00.848507
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__ converts arguments to str

    This is a regression test for https://bugs.launchpad.net/bzr/+bug/276228
    """
    e = IllegalUseOfScopeReplacer('name', 'msg', extra=u'\u1234')
    u = unicode(e)
    from bzrlib.tests import TestCase
    TestCase.assertEqual('ScopeReplacer object u"name" was used incorrectly: msg: \xe1\x88\xb4', u)


# Generated at 2022-06-14 06:06:10.615735
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    class ScopeReplacerSubclass(ScopeReplacer):
        def __call__(self, *args, **kwargs):
            obj = object.__getattribute__(self, '_resolve')()
            return obj(*args, **kwargs)
    my_dict = dict()
    my_name = "test_ScopeReplacer___call__"
    my_obj = ScopeReplacerSubclass(my_dict, lambda x, y, z: None, my_name)
    assert my_dict[my_name] is my_obj
    try:
        my_obj()
    except TypeError:
        assert False, "__call__ should raise an exception"



# Generated at 2022-06-14 06:06:15.170095
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    # Test calling a module as a function; that should be legal.
    import sys
    assert sys.argv == __call__.func_defaults[0].argv



# Generated at 2022-06-14 06:06:22.964692
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    from bzrlib.tests import TestCase
    from bzrlib.lazy_import import ScopeReplacer

    class TestLazyObject(object):

        def __init__(self):
            self.attr = 'blah'

        def __call__(self):
            return 'called'

    class TestCaseWithScopeReplacer(TestCase):

        def setUp(self):
            super(TestCaseWithScopeReplacer, self).setUp()
            self.replacer = ScopeReplacer(self.__dict__,
                                          lambda scope, name: scope[name+'_obj'],
                                          'lazy')
            self.lazy_obj = TestLazyObject()


# Generated at 2022-06-14 06:06:32.383108
# Unit test for method __setattr__ of class ScopeReplacer

# Generated at 2022-06-14 06:06:44.248829
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """Using Unicode literals in IllegalUseOfScopeReplacer"""
    # This is a simple test to use unicode literals in IllegalUseOfScopeReplacer.
    # It may be used to do a more complex test later.
    try:
        raise IllegalUseOfScopeReplacer(
            'lazy_import',
            '''It is not safe to use this object for "import",
            "exec", "compile" or "eval", because the string to use
            is not known until the function is called.''')
    except IllegalUseOfScopeReplacer as e:
        assert isinstance(e.name, unicode)
        assert isinstance(e.msg, unicode)



# Generated at 2022-06-14 06:06:56.752848
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    __tracebackhide__ = True
    import sys

    class Foo(object):
        def __init__(self, a, b, c=None):
            self.a = a
            self.b = b
            self.c = c
        def bar(self, d, e):
            return self.a, self.b, self.c, d, e

    # Plain old module
    scope = {}
    foo = ScopeReplacer(scope, module_import_factory, 'foo')
    sys.modules["foo"] = foo
    try:
        foo("bar", a=1, b=2, c=3)
        raise AssertionError("Non-lazy import did not fail.")
    except ImportError:
        pass
    assert len(scope) == 1
    assert scope["foo"] is foo
    scope["foo"]

# Generated at 2022-06-14 06:07:11.881677
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    """Test method __setattr__ of class ScopeReplacer.

    Unit test for method __setattr__ of class ScopeReplacer.
    """
    pass # TODO



# Generated at 2022-06-14 06:07:23.485142
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    obj = ScopeReplacer(None, None, None)

    # Method called without params/returns.
    obj.__setattr__()
    # Method called with incorrect param types.
    raises(TypeError, obj.__setattr__, *[1])
    raises(TypeError, obj.__setattr__, *[1.1])
    raises(TypeError, obj.__setattr__, *[None])
    raises(TypeError, obj.__setattr__, *[[]], **{})
    raises(TypeError, obj.__setattr__, *[{}], **{})
    # Method called with unexpected keyword param.
    raises(TypeError, obj.__setattr__, *[], **{'attr': 1})

# Generated at 2022-06-14 06:07:36.689442
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    import doctest
    from bzrlib.tests import TestCase
    from bzrlib.lazy_import import (
        IllegalUseOfScopeReplacer,
        )



# Generated at 2022-06-14 06:07:42.438991
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    global _bzrlib
    _bzrlib = ScopeReplacer(globals(), lambda self, scope, name: scope[name],
        '_bzrlib')
    def _f():
        global _bzrlib
        _bzrlib = ''
    _f()


# Generated at 2022-06-14 06:07:48.352954
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__ should return unicode"""
    s = "hello"
    e = IllegalUseOfScopeReplacer("name", "msg", s)
    try:
        unicode(e) + " world"
    except UnicodeDecodeError:
        raise AssertionError("IllegalUseOfScopeReplacer failed to return "
                             "unicode from __unicode__")



# Generated at 2022-06-14 06:07:57.260442
# Unit test for method __getattribute__ of class ScopeReplacer
def test_ScopeReplacer___getattribute__():
    from bzrlib import lazy_import as _LI
    _LI._testing_verify_real_import = True
    old_should_proxy = _LI.ScopeReplacer._should_proxy
    _LI.ScopeReplacer._should_proxy = True

# Generated at 2022-06-14 06:08:09.368088
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """Test __unicode__ method of IllegalUseOfScopeReplacer class"""

    import sys
    import tempfile
    tmpdir = tempfile.mkdtemp()
    filename = '%s/bzrlib/lazy_import.py' % tmpdir
    # Set up a file with a localizable string in it
    with open(filename, 'w') as f:
        f.write('''from bzrlib.i18n import (
    lazy_gettext,
    )
lazy_string = lazy_gettext("a localizable string")
''')
    message = 'blah blah blah'
    exc = IllegalUseOfScopeReplacer('LazyModuleName', message)
    # add a localized string to the exception object
    exc.lazy_string = 'a translated string'
    # Save previous sys.path, and

# Generated at 2022-06-14 06:08:22.235987
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    from bzrlib import (
        lazy_import,
        )
    lazy_import(globals(), '''
    import bzrlib.tests
    ''')
    global test_ScopeReplacer___setattr__
    scope = {}
    def importer(replacer, scope, name):
        scope[name] = bzrlib.tests.ModuleForTests
        return scope[name]
    replacer = lazy_import.ScopeReplacer(scope, importer, 'testmod')
    assert replacer._should_proxy
    global test_ScopeReplacer___setattr__
    replacer.test_ScopeReplacer___setattr__ = test_ScopeReplacer___setattr__
    assert scope[test_ScopeReplacer___setattr__.func_name] is test_ScopeReplacer___setattr__

# Generated at 2022-06-14 06:08:31.283371
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """Tests that IllegalUseOfScopeReplacer.__unicode__ returns the expected
    string for a given exception."""
    class DummyClass(object):
        pass
    class DummyException(IllegalUseOfScopeReplacer):
        pass

    s = DummyClass()
    # should look like this:
    # "DummyException(DummyClass object at 0xdeadbeef): dict={}, fmt=None,
    #                                                    error=None"
    expected_msg = 'DummyException(%r): dict={}, fmt=None, error=None' \
        % s
    exc = DummyException(s, '')
    actual_msg = str(exc)

# Generated at 2022-06-14 06:08:42.823267
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    from bzrlib import (
        errors,
        osutils,
        branch,
        )
    import bzrlib.branch

    def _wrap_ScopeReplacer(cls, *args):
        return cls(*args)
    _wrap_ScopeReplacer.__name__ = 'ScopeReplacer'

    import __builtin__
    _real_object = __builtin__.object
    __builtin__.object = _wrap_ScopeReplacer(ScopeReplacer, globals(),
                                             lambda *args: _real_object(),
                                             '_real_object')

    my_branch = branch.Branch()
    assert(isinstance(my_branch, branch.Branch))
    my_branch.__class__ == branch.Branch
    __builtin__.object = _real_object

# Generated at 2022-06-14 06:09:18.496508
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer

# Generated at 2022-06-14 06:09:24.512864
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    # Test __call__ method of class ScopeReplacer
    def self_test(scope, factory, name):
        # Test self_test method of class ScopeReplacer
        return 10
    scope = {'self_test': ScopeReplacer(scope, self_test, 'self_test')}
    scope['self_test']()



# Generated at 2022-06-14 06:09:32.735220
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    global _test_ScopeReplacer___setattr___done
    _test_ScopeReplacer___setattr___done = True

    import sys
    # Note that this tests only the behavior of __setattr__ in
    # a single thread.
    # This class is supposed to be used in a multithreaded context,
    # so a test for the multithreaded case would be nice...
    class MyScope:
        def __init__(self):
            self.value = None
        def __setitem__(self, key, value):
            self.value = value
    value = [1]
    scope = MyScope()
    name = 'lazy'
    ScopeReplacer._should_proxy = True
    new_object = ScopeReplacer(scope, lambda x, scope, name: scope.value, name)
    assert new_object