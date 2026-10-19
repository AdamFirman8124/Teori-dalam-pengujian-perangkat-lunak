

# Generated at 2022-06-14 06:00:11.257732
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    class x:
        pass
    o = x()
    o.x = 1
    a = ScopeReplacer({}, lambda s, x, y: o, 'o')
    a.x = 1
    if o.x != 2:
        raise AssertionError()


# Generated at 2022-06-14 06:00:23.196895
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    """Testing the operation of ScopeReplacer.__setattr__(attr, value)"""
    def my_factory(self, scope, name):
        """A simple factory"""
        return self
    from bzrlib.lazy_import import _py_compile
    from StringIO import StringIO
    from bzrlib import symbol_versioning
    my_scope = {}
    my_name = "my_name"
    # Create the ScopeReplacer object
    my_sr = ScopeReplacer(my_scope, my_factory, my_name)
    # Nothing should have happened yet
    assert my_scope[my_name] is my_sr
    # Allowing proxying should permit setting an attribute

# Generated at 2022-06-14 06:00:36.490378
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    from bzrlib.tests import TestCase
    class _MyScopeReplacer(ScopeReplacer):
        def __init__(self):
            super(_MyScopeReplacer, self).__init__(None, None, None)
        def _resolve(self):
            return self
        def __call__(self, *args, **kwargs):
            return super(_MyScopeReplacer, self).__call__(*args, **kwargs)
    rep = _MyScopeReplacer()
    r = rep('hello', 'world', important=True)
    TestCase.assertEqual(('hello', 'world',), r[:-1])
    TestCase.assertEqual({'important': True}, r[-1])
# /Unit test for method __call__ of class ScopeReplacer



# Generated at 2022-06-14 06:00:44.516628
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
  import bzrlib.lazy_import
  import bzrlib.branch

# Generated at 2022-06-14 06:00:50.294645
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__ of IllegalUseOfScopeReplacer must return a unicode object"""
    # Arrange
    e = IllegalUseOfScopeReplacer('foo', 'Some string')
    # Act
    u = unicode(e)
    # Assert
    assert u.__class__ is unicode
    # Clean-up




# Generated at 2022-06-14 06:00:58.202662
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    from bzrlib.lazy_import import lazy_import
    from bzrlib import tests
    bzrlib_module = tests.module_to_mod_dict('bzrlib')
    bzrlib_module['other_module'] = tests.module_to_mod_dict('other_module')
    import bzrlib.lazy_import
    old_eager_import = bzrlib.lazy_import.eager_import
    bzrlib.lazy_import.eager_import = lambda module: bzrlib_module[str(module)]

# Generated at 2022-06-14 06:01:11.620856
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """The string representation of IllegalUseOfScopeReplacer is useful"""
    msg = "foo %bar %baz"
    ex = IllegalUseOfScopeReplacer('abc', msg)
    ex.__dict__['x'] = 'y'
    actual = str(ex)
    assert "'baz'" in actual, repr(actual)
    assert "'bar'" in actual, repr(actual)
    assert repr(ex.__dict__) in actual, repr(actual)
    ex.__dict__['bar'] = 'z'
    ex.__dict__['baz'] = 'zz'
    actual = str(ex)
    assert "ScopeReplacer object 'abc'" in actual, repr(actual)
    assert "foo 'z' 'zz'" in actual, repr(actual)



# Generated at 2022-06-14 06:01:21.907458
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    from bzrlib.tests import TestCase
    # Test for normal functioning
    class Test_getattribute_ScopeReplacer(object):
        def __init__(self, original_object, scope, name):
            object.__setattr__(self, 'original_object', original_object)
            object.__setattr__(self, 'scope', scope)
            object.__setattr__(self, 'name', name)
        def _resolve(self):
            return object.__getattribute__(self, 'original_object')
        def __getattribute__(self, attr):
            obj = object.__getattribute__(self, '_resolve')()
            return getattr(obj, attr)

# Generated at 2022-06-14 06:01:25.684715
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    from bzrlib.lazy_import import ScopeReplacer
    s = ScopeReplacer
    # FIXME: test method __setattr__ of class ScopeReplacer in module lazy_import

# Generated at 2022-06-14 06:01:36.558837
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    from bzrlib.tests.per_lazy_import import TestCase
    from bzrlib.lazy_import import lazy_import, ScopeReplacer

    def factory(self, scope, name):
        return 42

    class TestScopeReplacer(TestCase):

        def test_call_instantiated(self):
            import sys
            scope = sys._getframe(0).f_globals
            name = 'foo'
            scope[name] = ScopeReplacer(scope, factory, name)
            self.assertEqual(42, scope[name]())

    # Run the tests
    import bzrlib.tests.test_per_lazy_import
    bzrlib.tests.test_per_lazy_import.testmod()


# Generated at 2022-06-14 06:02:02.952742
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """__str__ should not raise UnicodeDecodeError."""
    try:
        raise IllegalUseOfScopeReplacer('somename', 'some message')
    except IllegalUseOfScopeReplacer as e:
        def _raise(*args, **kwargs):
            raise
        e._get_format_string = _raise
        str(e)



# Generated at 2022-06-14 06:02:06.343712
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    import doctest
    doctest.run_docstring_examples(ScopeReplacer.__call__,
                                   globals(),
                                   name="ScopeReplacer.__call__",
                                   optionflags=doctest.ELLIPSIS)

# Generated at 2022-06-14 06:02:16.374023
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """Method __str__ of class IllegalUseOfScopeReplacer

    It should be possible to call __str__() on the exception
    and get a string back.
    """

    e = IllegalUseOfScopeReplacer(name='foo', msg='bar')
    s = str(e)
    if not isinstance(s, str):
        raise AssertionError('__str__ must return a str.')

    # __str__ must return a str.
    if isinstance(s, unicode):
        raise AssertionError('__str__ must return a str.')


# Generated at 2022-06-14 06:02:23.866709
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """Unit test for method __str__ of class IllegalUseOfScopeReplacer"""
    try:
        raise IllegalUseOfScopeReplacer('foo', 'bar')
    except IllegalUseOfScopeReplacer as e:
        pass
    else:
        # ValueError should be raised
        raise AssertionError("IllegalUseOfScopeReplacer should have been raised")
    str(e) # Should not raise an exception - just make sure it doesn't



# Generated at 2022-06-14 06:02:36.863950
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    from bzrlib import _i18n_strings
    _i18n_strings.set_up()
    try:
        raise IllegalUseOfScopeReplacer('x', "message", {'a':1, 'b':2})
    except Exception as e:
        s = str(e)
        assert isinstance(s, str)
        assert s.startswith('IllegalUseOfScopeReplacer(')
        assert "message" in s
        u = unicode(e)
        assert isinstance(u, unicode)
        assert u.startswith(u'IllegalUseOfScopeReplacer(')
        assert u"message" in u
        unicode(e)
        # Test format strings, which should normally be ascii

# Generated at 2022-06-14 06:02:45.923664
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """Method __unicode__ of class IllegalUseOfScopeReplacer

    This class defines two string attributes: _fmt and extra.
    The _fmt attribute is a message string and can contain
    substitution values. The extra attribute is an optional
    additional message string.

    Substitution values are contained in a dict and are either
    in the dict of the object (self.__dict__) or in the object
    itself (self.name etc.).

    The __unicode__ method formats the message based on _fmt and
    extra. _fmt is optional, extra is not.
    """
    import bzrlib.errors
    from bzrlib.lazy_import import limit_args_to_kw_args

    class K(bzrlib.errors.BzrError):
        _fmt = "K(%(key)s)"

# Generated at 2022-06-14 06:02:55.525675
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """__str__ should always return a str object, never a unicode object."""
    # We must check whether the result of __str__ is a str or unicode object.
    # If str and unicode have the same type (the Python 2.x byte string type),
    # then it always returns str. If they have different types (Python 3.x),
    # it should return the unicode object.

    if str == unicode:
        # Python 2.x
        x = IllegalUseOfScopeReplacer('name', 'msg')
        __str__ = x.__str__()
        assert type(__str__) is str, "__str__ should return a str object"
    else:
        # Python 3.x
        x = IllegalUseOfScopeReplacer('name', 'msg')
        __str__ = x.__str__()
       

# Generated at 2022-06-14 06:03:02.899356
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """Unit test for method __str__ of class IllegalUseOfScopeReplacer"""
    from bzrlib.tests import TestCase
    from StringIO import StringIO
    class TestException(IllegalUseOfScopeReplacer):
        def _get_format_string(self):
            return '%(name)s'
    # Note: we check __str__() and __unicode__() in test_exception_formatting
    tb = StringIO()
    try:
        raise TestException('foo', 'bar')
    except TestException as e:
        import traceback
        traceback.print_exc(file=tb)
    tc = TestCase()

# Generated at 2022-06-14 06:03:13.440814
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    from bzrlib.lazy_import import ScopeReplacer
    from bzrlib.lazy_import import IllegalUseOfScopeReplacer
    import sys
    # 
    # Using an empty scope
    scope = {}
    # 
    # We want it to be replaced by a ModifiedCallable
    class ModifiedCallable(object):
        def __init__(self):
            self.attr = 'value'
    def create_replacement():
        return ModifiedCallable()
    # 
    # Create the replacer object.
    replacer = ScopeReplacer(scope, create_replacement, 'name')
    # 
    # Using the replacer like the actual object is permitted,
    # But the object is not created until it is used.
    # 
    # The replacer defines 'attr', but the replacement does not.


# Generated at 2022-06-14 06:03:27.521038
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    from pprint import pformat

# Generated at 2022-06-14 06:03:54.437316
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__ must return a unicode object, not a str object.

    This allows downstream code to do some more processing on it.
    """
    from bzrlib.lazy_import import IllegalUseOfScopeReplacer
    e = IllegalUseOfScopeReplacer("the_name", "the_msg")
    # We cannot really assert this, because other code might set the
    # _preformatted_string argument of the exception.
    if '_preformatted_string' in e.__dict__:
        # __unicode__ must return a unicode object, not a str object.
        assert isinstance(e.__unicode__(), unicode)
        return
    # If it is not set, then __unicode__ must use str and the default encoding
    assert isinstance(e.__unicode__(), unicode)

#

# Generated at 2022-06-14 06:03:58.865951
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    from bzrlib import lazy_import
    def f(a):
        return a
    b = lazy_import.ScopeReplacer(locals(), f, 'f')
    b.test = 1
    f.test = 1
    b.test = 3
    f.test = 3



# Generated at 2022-06-14 06:04:04.051138
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """
    >>> e = IllegalUseOfScopeReplacer('a', 'b', 'c')
    >>> str(e)
    'IllegalUseOfScopeReplacer object \'a\' was used incorrectly: b: c'
    >>> e = IllegalUseOfScopeReplacer('a', 'b')
    >>> str(e)
    'IllegalUseOfScopeReplacer object \'a\' was used incorrectly: b'
    """

_sentinel = object()



# Generated at 2022-06-14 06:04:12.489097
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """Testing IllegalUseOfScopeReplacer.__str__"""
    from bzrlib import lazy_import
    import bzrlib
    from bzrlib.tests import TestCase
    from bzrlib.lazy_import import AttributeMapping

    scope = {}
    scope.update(bzrlib.__dict__)
    scope.update(lazy_import.__dict__)
    lazy_import.lazy_import(scope, '''
    from bzrlib import (
        errors,
        osutils,
        branch,
        )
    import bzrlib.branch
    ''')
    mapping = AttributeMapping(scope)
    mapping._update_location()

    self = TestCase('__init__')
    sr = scope['errors']
    e = lazy_import.Illegal

# Generated at 2022-06-14 06:04:22.611090
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    import unittest
    import itertools
    from bzrlib.tests import TestCase
    from bzrlib.lazy_import import lazy_import, ScopeReplacer

    def my_factory(sr, scope, name):
        def f(arg1, arg2):
            return name, arg1, arg2
        return f

    class TestScopeReplacer(TestCase):

        def test_callable_factory(self):
            globs = {}
            lazy_import(
                globs,
                '''
                import bzrlib.lazy_import
                my_callable = bzrlib.lazy_import.ScopeReplacer(
                    globals(), my_factory, 'my_callable')
                ''')

# Generated at 2022-06-14 06:04:34.678450
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """__str__ of IllegalUseOfScopeReplacer"""
    o = IllegalUseOfScopeReplacer(name=u'some-name', msg=u'x')
    # The object is a str object
    __str__ = o.__str__()
    # The object is a unicode object
    __unicode__ = o.__unicode__()
    # Check that the encoded unicode object is the same as the str object
    assert __str__ == __unicode__.encode('utf8'), "%r != %r" % (__str__, __unicode__)
    assert isinstance(__str__, str), "%r is not a str" % (__str__,)
    # Check that the unicode object is the same as the str object

# Generated at 2022-06-14 06:04:48.441985
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    import sys
    import bzrlib.lazy_import
    bzrlib.lazy_import.lazy_import(globals(), """
    import bzrlib.tests.blackbox
    """)
    ScopeReplacer_class = bzrlib.lazy_import.ScopeReplacer

    class FakeModule:
        pass

    class FakeScope:
        pass

    fake_module = FakeModule()

    def _factory(self, scope, name):
        # Confirm that _resolve() is being called, not __resolve__
        assert self.name != '_resolve'
        assert self.name != '_real_obj'
        assert self.name == name
        assert self.scope is scope
        if name == 'a':
            return 10
        else:
            return 20


# Generated at 2022-06-14 06:04:51.353430
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    r = IllegalUseOfScopeReplacer('x', 'y')
    assert isinstance(unicode(r), unicode)


# Generated at 2022-06-14 06:05:00.861998
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    from bzrlib.tests.blackbox import ExternalBase

    class TestCase(ExternalBase):

        def test_ScopeReplacer___setattr__(self):
            # ScopeReplacer should disallow setting attributes on replaced
            # objects.
            out, err = self.run_bzr('selftest --load-list'
                                    ' bzrlib.tests.blackbox.test_ScopeReplacer___setattr__'
                                    )
            self.assertEqual('', err)
            self.assertContainsRe(out, '.*Failed:.*')

    return TestCase

# Generated at 2022-06-14 06:05:09.785653
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """IllegalUseOfScopeReplacer.__unicode__"""
    # This tests that IllegalUseOfScopeReplacer.__unicode__ gracefully
    # handles exceptions in IllegalUseOfScopeReplacer._format. This can
    # happen when the format string is invalid (e.g. %(frob)s where frob is
    # not a parameter).
    import traceback
    class BadException(Exception):
        _fmt = "Bad exception %(charge_num)s"
    e = BadException()
    traceback.extract_tb()
    # If _format raises an exception, we want to fallback gracefully
    # without crashing.
    unicode(e)


# Generated at 2022-06-14 06:05:25.787831
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    # TODO: Test not implemented
    pass



# Generated at 2022-06-14 06:05:29.258605
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """This test case ensures that the __str__()
    method of class IllegalUseOfScopeReplacer works properly.
    """
    _lazy_import()


# Generated at 2022-06-14 06:05:41.946827
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """The __unicode__ method of IllegalUseOfScopeReplacer should always return
    a unicode object.  It should also gracefully handle format strings that
    are not unicode objects as long as they can be converted to unicode using
    the ascii codec."""
    from bzrlib import lazy_import
    obj = lazy_import.IllegalUseOfScopeReplacer('name', 'msg', 'extra')
    obj._preformatted_string = 'value'
    u = obj.__unicode__()
    if not isinstance(u, unicode):
        raise AssertionError('__unicode__() should have returned a unicode'
                             'object')
    obj._preformatted_string = '\xbd' # invalid utf8

# Generated at 2022-06-14 06:05:48.398990
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    from bzrlib import lazy_import

    # Create a ScopeReplacer object, then call its __setattr__ method with a
    # attribute name and a value.

    x = lazy_import._ScopeReplacer(None,None,'name')
    x.__setattr__('name','value')



# Generated at 2022-06-14 06:05:49.555635
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    pass # nothing to test

# Generated at 2022-06-14 06:05:55.750361
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """Unit test for method __unicode__ of class IllegalUseOfScopeReplacer"""
    obj = IllegalUseOfScopeReplacer('name', 'msg', 'extra')
    obj.__dict__['_preformatted_string'] = 'This is a %s exception.'
    if not isinstance(obj.__unicode__(), unicode):
        raise AssertionError



# Generated at 2022-06-14 06:06:04.017705
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    from bzrlib import lazy_import
    import bzrlib.smart.repository
    old_should_proxy = ScopeReplacer._should_proxy

# Generated at 2022-06-14 06:06:17.802095
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    from bzrlib.lazy_import import lazy_import
    from bzrlib.errors import get_error_from_name
    from bzrlib.errors import BzrError
    from bzrlib.errors import BzrCommandError as _BzrCommandError
    test_mod = '''
    from bzrlib.errors import (
        BzrError,
        BzrCommandError,
        )
    '''
    ScopeReplacer._should_proxy = True

# Generated at 2022-06-14 06:06:24.752383
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
  import test_pychecker_scope_replacer_1
  # Check that ScopeReplacer has no attribute '___setattr__'.
  try:
    test_pychecker_scope_replacer_1.ScopeReplacer.__setattr__
  except AttributeError:
    pass
  else:
    raise AssertionError



# Generated at 2022-06-14 06:06:33.452489
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    from bzrlib import lazy_import
    import gc
    # test_ScopeReplacer___call__ {{{1
    # Ensure an exception is raised when the object is called before it
    # has been loaded.
    globals()["test_ScopeReplacer___call___proxy_factory_scope"] = locals()
    globals()["test_ScopeReplacer___call___proxy_name"] = "test_ScopeReplacer___call___proxy"
    ScopeReplacer(
        globals()["test_ScopeReplacer___call___proxy_factory_scope"],
        lambda self, scope, name: scope[name],
        globals()["test_ScopeReplacer___call___proxy_name"])
    del globals()["test_ScopeReplacer___call___proxy_factory_scope"]

# Generated at 2022-06-14 06:07:05.426406
# Unit test for method __getattribute__ of class ScopeReplacer
def test_ScopeReplacer___getattribute__():
    """Test __getattribute__ in ScopeReplacer"""
    import doctest
    from bzrlib.tests import TestCase
    globs = globals()
    globs.update({
        'test_ScopeReplacer___getattribute__':test_ScopeReplacer___getattribute__,
        })
    doctest.testmod(globs=globs,
                    optionflags=doctest.NORMALIZE_WHITESPACE+doctest.ELLIPSIS)



# Generated at 2022-06-14 06:07:19.572015
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    """__setattr__ should set the attribute of the lazy object

    When the lazy object is first used, it resolves itself and
    executes its __setattr__ method"""
    class Foo(object):

        def __init__(self, value):
            self.value = value

    class Bar(object):

        def __init__(self):
            self.foo = None

    b = Bar()
    f = Foo(b)
    s = ScopeReplacer({}, lambda _, __, ___: f, 'f')
    # Initially the lazy object proxies all calls to f
    f.value.foo = 1
    s.value.foo = 2
    # After the first operation through the lazy object, it
    # resolves itself and its __setattr__ method is executed
    s.value.foo = 3
    # So the correct value is set in f


# Generated at 2022-06-14 06:07:21.942683
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    e = IllegalUseOfScopeReplacer('xyz', 'abc')
    assert isinstance(e.__unicode__(), unicode)


# Generated at 2022-06-14 06:07:25.728315
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """
    Ensure that IllegalUseOfScopeReplacer's __str__ returns a string.
    """
    e = IllegalUseOfScopeReplacer('foo', 'bar')
    assert isinstance(str(e), str)



# Generated at 2022-06-14 06:07:29.276507
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """IllegalUseOfScopeReplacer._format works"""
    u = IllegalUseOfScopeReplacer('name', 'msg', 'extra')
    s = unicode(u)



# Generated at 2022-06-14 06:07:35.919756
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """Unit test for method __str__ of class IllegalUseOfScopeReplacer"""
    e = IllegalUseOfScopeReplacer(
        'name',
        'msg',
        extra='extra')
    expected = 'name: msg: extra'
    got = '%s' % e
    assert(got == expected)
test_IllegalUseOfScopeReplacer___str__()



# Generated at 2022-06-14 06:07:41.347673
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """IllegalUseOfScopeReplacer.__unicode__ returns str based on _fmt"""
    e = IllegalUseOfScopeReplacer('foo', 'spam', 'foo')
    assert e.__unicode__() == (u"foo was used incorrectly: spam: foo")


# Generated at 2022-06-14 06:07:52.391860
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    def _fun_1():
        attr = '_real_obj'
        value = None
        obj = ScopeReplacer()
        return setattr(obj, attr, value)
    def _fun_2():
        attr = '_real_obj'
        value = None
        obj = ScopeReplacer()
        return setattr(obj, attr, value)
    def _fun_3():
        attr = '_real_obj'
        value = None
        obj = ScopeReplacer()
        return setattr(obj, attr, value)
    assert _fun_1() is None
    assert _fun_2() is None
    assert _fun_3() is None


# Generated at 2022-06-14 06:08:06.822158
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """IllegalUseOfScopeReplacer.__unicode__() should return a unicode object

    It should return a unicode object even if _fmt was given a str object
    (bug #112238).
    """
    from bzrlib.i18n import gettext
    import bzrlib._pyutils as _pyutils

    # gettext() returns a unicode.
    # if _fmt is a unicode, we should return a unicode.
    class UnicodeFmtScopeReplacer(IllegalUseOfScopeReplacer):
        _fmt = gettext(u"blah")
    e = UnicodeFmtScopeReplacer("name", "msg")
    _pyutils.UNICODE_STRINGS = True
    u = e.__unicode__()
    _pyutils.UNICODE_STRINGS = False

# Generated at 2022-06-14 06:08:18.293419
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """IllegalUseOfScopeReplacer.__unicode__ should return unicode

    This is a regression test for bug #106415
    """
    e = IllegalUseOfScopeReplacer('name', 'msg')
    # __unicode__ should return unicode
    u = unicode(e)
    # u should be decodable as ascii
    if not isinstance(u, unicode):
        raise AssertionError('__unicode__ returned non-unicode: %r' % (u,))
    s = u.encode('ascii')
    # u should contain the word 'IllegalUseOfScopeReplacer'
    if s.find('IllegalUseOfScopeReplacer') == -1:
        raise AssertionError('output of __unicode__ is wrong: %r' % (u,))

    # u

# Generated at 2022-06-14 06:09:38.857578
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__ must return a unicode object."""
    x = IllegalUseOfScopeReplacer(u'foo'.encode('utf8'), 'bar')
    assert isinstance(x.__unicode__(), unicode)
    x = IllegalUseOfScopeReplacer(u'foo', 'bar')
    assert isinstance(x.__unicode__(), unicode)

