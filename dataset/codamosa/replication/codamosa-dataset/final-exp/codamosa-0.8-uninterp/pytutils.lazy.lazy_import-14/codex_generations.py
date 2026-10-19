

# Generated at 2022-06-14 06:00:11.418825
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    e = IllegalUseOfScopeReplacer('name', 'msg', 'extra')
    assert str(e) == ("ScopeReplacer object 'name' was used incorrectly:"
                      " msg: extra")

    # Check that changing the instance doesn't change the message
    e.msg = 'other'
    assert str(e) == ("ScopeReplacer object 'name' was used incorrectly:"
                      " msg: extra")

    # Check that we can mark exceptions as having preformatted messages and
    # it is used instead of the format string.
    e._preformatted_string = "This should be used instead"
    assert str(e) == "This should be used instead"

    # Check that we can mark exceptions as having no format string and
    # checking for it doesn't raise
    del e._preformatted_string
    e._fmt = None

# Generated at 2022-06-14 06:00:19.425065
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """Ensure that the class IllegalUseOfScopeReplacer returns a str object
    and not a unicode object.

    We don't want a unicode object as that would cause problems on
    systems that use an encoding other than utf8.
    """
    err = IllegalUseOfScopeReplacer("test", "msg")
    assert isinstance(str(err), str)
    assert not isinstance(str(err), unicode)
    assert not isinstance(str(err), bytes)



# Generated at 2022-06-14 06:00:27.898104
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    import unittest
    class DummyScope(object):
        def __init__(self):
            self.name = None
            self.obj = None
        def __setitem__(self, key, obj):
            self.name = key
            self.obj = obj
    class DummyClass(object):
        def __call__(self, a, b, c=None):
            return a+b+c
    class TestCase(unittest.TestCase):
        def test_ScopeReplacer___call__(self):
            d = DummyScope()
            def factory(obj, scope, name):
                return DummyClass()
            sr = ScopeReplacer(d, factory, 'x')
            self.assertEqual(sr(5, 6, c=7), 5+6+7)

# Generated at 2022-06-14 06:00:33.967106
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    r"""IllegalUseOfScopeReplacer.__str__()

    This method is called when str(exception) is evaluated.

    >>> str(IllegalUseOfScopeReplacer('name', 'msg', 'extra'))
    'IllegalUseOfScopeReplacer: ScopeReplacer object 'name' was used incorrectly: msg: extra'
    """



# Generated at 2022-06-14 06:00:36.369214
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """IllegalUseOfScopeReplacer.__unicode__ is tested in test_errors."""
    pass



# Generated at 2022-06-14 06:00:42.175277
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """Unit test for method __unicode__ of class IllegalUseOfScopeReplacer"""
    # Since this method relies on __str__, the test is just a sanity check.
    e = IllegalUseOfScopeReplacer('name', 'msg')
    u = unicode(e)
    s = str(e)
    assert u == s
    assert isinstance(u, unicode)
    assert isinstance(s, str)
test_IllegalUseOfScopeReplacer___unicode__()



# Generated at 2022-06-14 06:00:49.072099
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """IllegalUseOfScopeReplacer.__unicode__() returns a unicode object."""

    e = IllegalUseOfScopeReplacer(name='some name', msg='some message')
    u = e.__unicode__()
    assert isinstance(u, unicode)

test_IllegalUseOfScopeReplacer___unicode__._test_needs_i18n = True


# Generated at 2022-06-14 06:00:57.546628
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    import unittest as _mod_unittest
    import sys as _mod_sys
    class _mod_TestCase(_mod_unittest.TestCase):
        def _run_test(self, test, name, doc=None, sys_exc=None):
            test_globals = {'test': test}
            if sys_exc is not None:
                test_globals['__builtins__'] = {'SystemExit': sys_exc}
            if doc is None:
                doc = name
            new_globals = {}

# Generated at 2022-06-14 06:01:00.774794
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__ must return a unicode object."""
    e = IllegalUseOfScopeReplacer('e', 'msg')
    u = unicode(e)
    assert isinstance(u, unicode)

# Generated at 2022-06-14 06:01:13.415504
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """Test __unicode__ method of IllegalUseOfScopeReplacer.

    Unfortunately this function can't raise IllegalUseOfScopeReplacer
    itself, because it's a builtin exception, but it can test the
    method.
    """
    import StringIO
    # We have to patch StringIO.StringIO.__str__ to avoid
    # testing it's use of __unicode__
    old_StringIO__str__ = StringIO.StringIO.__str__
    def raise_exception(self, encoding=None):
        if encoding is not None:
            raise TypeError("__str__ doesn't take an 'encoding' argument")
        raise Exception("%s.__str__ was called" % type(self))
    StringIO.StringIO.__str__ = raise_exception


# Generated at 2022-06-14 06:01:26.639198
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    # __setattr__ defined in class ScopeReplacer
    # __setattr__ is a wrapper around the __setattr__ method
    # __setattr__ of class object
    # Calling __setattr__(self, attr, value)
    raise NotImplementedError()



# Generated at 2022-06-14 06:01:37.612052
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__ of IllegalUseOfScopeReplacer

    IllegalUseOfScopeReplacer is a subclass of Exception, but it overrides
    __unicode__ to restrict the output to a format and dict.  If the format
    string is unicode, the output should be unicode.  If the format string is
    ascii, the output should be utf8.
    """
    name = u'name'
    msg = u'msg'
    extra = u'extra'
    _fmt = u'name: %(name)s, msg: %(msg)s%(extra)s'

    x = IllegalUseOfScopeReplacer(name, msg, extra)
    x._fmt = _fmt
    assert isinstance(x.__unicode__(), unicode)


# Generated at 2022-06-14 06:01:38.506787
# Unit test for method __getattribute__ of class ScopeReplacer
def test_ScopeReplacer___getattribute__():
    assert True


# Generated at 2022-06-14 06:01:49.561736
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """IllegalUseOfScopeReplacer.__unicode__()

    __unicode__() must return a unicode object.
    """
    from bzrlib import (
        lazy_import,
        )
    lazy_import(globals(), """
from bzrlib import (
    errors,
    )
""")
    s = 'unicode string'
    e = errors.IllegalUseOfScopeReplacer('name', s)
    u = unicode(e)
    if s != u:
        raise AssertionError(u'test_IllegalUseOfScopeReplacer___unicode__:'
                             ' unicode(e) != s, got %r' % (u,))

# Generated at 2022-06-14 06:02:03.779480
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    from bzrlib.tests import TestCase
    from bzrlib.lazy_import import ScopeReplacer
    import __builtin__
    class Test(TestCase):
        def __call__(self):
            pass
    sr = ScopeReplacer(__builtin__.__dict__,
        lambda self, scope, name: Test(), 'Test')
    test = Test()
    result = test()
    self.assertEqual(None, result)
    result = test.__call__()
    self.assertEqual(None, result)
    result = sr()
    self.assertEqual(test, result)
    result = sr.__call__()
    self.assertEqual(test, result)
    result = sr.__call__().__call__()
    self.assertEqual(test, result)
   

# Generated at 2022-06-14 06:02:16.777390
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """This test ensures that IllegalUseOfScopeReplacer.__unicode__ works.

    IllegalUseOfScopeReplacer.__unicode__ is a variant of
    Exception.__unicode__ that tries to decode the result of Exception.__str__
    to unicode using the default encoding.

    Note that the test ensures that IllegalUseOfScopeReplacer.__unicode__
    can be called. However, it doesn't test that IllegalUseOfScopeReplacer
    actually is a good base class for other exceptions.
    """
    class X(IllegalUseOfScopeReplacer):
        _fmt = 'X %(name)r %(msg)r %(extra)r'
    x = X('a', 'b', 'c')
    u = unicode(x)
    assert isinstance(u, unicode)



# Generated at 2022-06-14 06:02:26.663623
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """__str__ should return str instance."""
    x = IllegalUseOfScopeReplacer(1, 2)
    s = str(x)
    assert isinstance(s, str)
    # It should be unicode
    y = IllegalUseOfScopeReplacer(1, u'a\u1234', u'c\u1234')
    s = str(y)
    assert isinstance(s, str)
    assert s == 'Unprintable exception IllegalUseOfScopeReplacer: dict={\'name\': 1, \'msg\': u\'a\\u1234\', \'extra\': u\'c\\u1234\'}, fmt=None, error=None'

# Generated at 2022-06-14 06:02:38.211182
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    d = {}
    def factory(self, scope, name):
        return []
    obj = ScopeReplacer(d, factory, 'foo')
    obj.append(1)
    obj.__setattr__('foo', 2)
    obj.append(3)
    obj.__setattr__('bar', 4)
    assert len(obj) == 2
    assert d['foo'] == [1, 3]
    try:
        obj.__getattr__('foo')
    except IllegalUseOfScopeReplacer:
        pass
    else:
        raise AssertionError("__getattr__ is not proxied")
    try:
        obj.__setattr__('foo', 2)
    except IllegalUseOfScopeReplacer:
        pass
    else:
        raise AssertionError("__setattr__ is not proxied")


# Generated at 2022-06-14 06:02:50.904260
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """IllegalUseOfScopeReplacer.__str__()

    This test checks that IllegalUseOfScopeReplacer correctly formats
    IllegalUseOfScopeReplacer exceptions.
    """
    # IllegalUseOfScopeReplacer.__init__() with all fields defined
    # intentionally not translated to check that format string is correct
    e = IllegalUseOfScopeReplacer('foo', 'bar', 'baz')
    assert str(e) == 'ScopeReplacer object \'foo\' was used incorrectly:' \
        ' bar: baz'
    # IllegalUseOfScopeReplacer.__init__() with translated format string
    e = IllegalUseOfScopeReplacer('x', 'y')
    assert str(e) == u'ScopeReplacer object \'x\' was used incorrectly:' \
        u' y'


# Generated at 2022-06-14 06:02:57.724425
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__ should convert to unicode if it starts as str"""
    my_ex = IllegalUseOfScopeReplacer('my_ex', 'msg', extra='extra')
    my_ex._fmt = 'a %(name)s msg %(msg)s'
    assert isinstance(my_ex, Exception)
    assert isinstance(unicode(my_ex), unicode)

# Generated at 2022-06-14 06:03:14.923490
# Unit test for method __getattribute__ of class ScopeReplacer
def test_ScopeReplacer___getattribute__():
    from unittest import TestCase
    import sys

    class _Foo(object):
        pass

    def factory(self, scope, name):
        obj = _Foo()
        return obj

    old_should_proxy = ScopeReplacer._should_proxy
    try:
        # Test that attribute access in the 'resolve' method works
        # correctly.
        ScopeReplacer._should_proxy = True
        ScopeReplacer(sys.modules, factory, '_ScopeReplacer')
        ScopeReplacer._ScopeReplacer._resolve()
    finally:
        ScopeReplacer._should_proxy = old_should_proxy

    # Test that the ScopeReplacer replaces itself in the scope
    # when accessed via __getattribute__. Note that the unit test
    # rules require __getattribute__ to be called getattr.

# Generated at 2022-06-14 06:03:23.745843
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """Unit test for IllegalUseOfScopeReplacer.__str__"""
    e = IllegalUseOfScopeReplacer('name',
            'message',
            'extra')
    e_repr = repr(e)
    s = str(e)
    assert isinstance(s, str), '__str__ did not return a str'
    # Make sure the description, message and extra are found in __str__
    assert 'name' in s
    assert 'message' in s
    assert 'extra' in s


# Generated at 2022-06-14 06:03:32.983156
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    import bzrlib.tests
    ScopeReplacer._should_proxy = False
    try:
        # Try to recreate the error caused by bug #95866
        from bzrlib.tests import (
            # This next line should cause an error, which is the point of the
            # test, so don't move it out of this test function.
            features,
            )
    except IllegalUseOfScopeReplacer:
        # All ok, this is what was expected.
        pass
    else:
        bzrlib.tests.TestCase.fail("expected IllegalUseOfScopeReplacer to be "
            "raised, but none was")


# Generated at 2022-06-14 06:03:44.457574
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """All scope replacers should be printable"""
    # This test is unusual in that it tests a base class method.
    import sys
    if '--force-unicode' in sys.argv:
        # We have been specifically requested to test unicode paths
        # (rather than the default of testing str paths.)
        # This can be done by passing '--force-unicode' as an argument.
        import unicodedata
        # Create a string that is two characters,
        # one being a combining character.
        # The first is an ASCII character, so that unicode()
        # will return a unicode object.
        name = unicodedata.lookup('LATIN SMALL LETTER A WITH ACUTE')
        name = name + unicodedata.lookup('COMBINING TILDE')
        # The unicode() function below would work

# Generated at 2022-06-14 06:03:52.991610
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """Test method __unicode__ of class IllegalUseOfScopeReplacer"""
    o = IllegalUseOfScopeReplacer(u'abc', u'msg', u'extra')
    assert isinstance(o, IllegalUseOfScopeReplacer)
    assert isinstance(o, Exception)
    u = str(o)
    assert isinstance(u, unicode)
    assert u == u'ScopeReplacer object u\'abc\' was used incorrectly: msg: extra'

# Generated at 2022-06-14 06:04:03.339926
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """IllegalUseOfScopeReplacer.__str__()

    The following cases are checked:
    - exception message is ascii
    - exception message contains a unicode character
    """
    import sys
    error = IllegalUseOfScopeReplacer('name', 'msg')
    # The correct encoding is detected by the modification to
    # the PYTHONPATH
    assert str(error) == "IllegalUseOfScopeReplacer object 'name' was used incorrectly: msg"
    error = IllegalUseOfScopeReplacer('n\xe5me', 'm\xe9sg')
    # The correct encoding is detected by the modification to
    # the PYTHONPATH
    assert str(error) == "IllegalUseOfScopeReplacer object 'n\xc3\xa5me' was used incorrectly: m\xc3\xa9sg"



# Generated at 2022-06-14 06:04:07.375701
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__ should return a unicode object"""
    e = IllegalUseOfScopeReplacer('foo', 'msg', 'extra')
    assert isinstance(unicode(e), unicode)



# Generated at 2022-06-14 06:04:11.313225
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """__str__ must return a str"""
    e = IllegalUseOfScopeReplacer('fake exception', 'some message')
    s = str(e)
    assert isinstance(s, str)



# Generated at 2022-06-14 06:04:16.869889
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__() should return a unicode object (not a str)"""
    from bzrlib.lazy_import import IllegalUseOfScopeReplacer
    s = IllegalUseOfScopeReplacer("f", "m")
    u = unicode(s)
    assert isinstance(u, unicode)


# Generated at 2022-06-14 06:04:24.414029
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    import bzrlib.lazy_import
    from bzrlib.errors import BzrError
    from bzrlib import (
        _simple_set,
        )
    from testtools import TestCase
    from testtools.matchers import (
        Equals,
        MatchesException,
        )
    #E Preserve source-code line-numbering

# Generated at 2022-06-14 06:04:35.588602
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """IllegalUseOfScopeReplacer.__unicode__"""
    err = IllegalUseOfScopeReplacer('name', 'msg')
    expected = u'ScopeReplacer object \'name\' was used incorrectly: msg'
    actual = unicode(err)
    assert expected == actual



# Generated at 2022-06-14 06:04:40.211367
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """test_IllegalUseOfScopeReplacer___unicode__ - tests __unicode__ method"""
    e = IllegalUseOfScopeReplacer('foo', 'bar')
    assert type(e.__unicode__()) is unicode
    assert str(e) == 'bar'



# Generated at 2022-06-14 06:04:47.652680
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """__str__() should return a str"""
    class AnIllegalUseOfScopeReplacer(IllegalUseOfScopeReplacer):
        pass
    exception = AnIllegalUseOfScopeReplacer(
        'fake name', 'fake message', 'fake extra')
    s = str(exception)
    from bzrlib.tests import TestCase
    TestCase().assertIsInstance(s, str)



# Generated at 2022-06-14 06:04:51.179907
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    e = IllegalUseOfScopeReplacer('name', 'msg')
    u = e.__unicode__()
    assert isinstance(u, unicode)
    assert u == unicode(str(e))


# Generated at 2022-06-14 06:04:59.439399
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """IllegalUseOfScopeReplacer.__unicode__() -> unicode"""
    o = IllegalUseOfScopeReplacer('name-value', 'msg-value', extra='')
    expected = u"name-value was used incorrectly: msg-value"
    actual = unicode(o)
    # __unicode__ should return a unicode object
    assert(isinstance(actual, unicode))
    assert(actual == expected)


# Generated at 2022-06-14 06:05:10.150676
# Unit test for method __getattribute__ of class ScopeReplacer
def test_ScopeReplacer___getattribute__():
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    def test_ScopeReplacer___getattribute__():
        import sys
        def test_ScopeReplacer___getattribute__():
            import sys
            def test_ScopeReplacer___getattribute__():
                import sys
                def test_ScopeReplacer___getattribute__():
                    import sys
                    def test_ScopeReplacer___getattribute__():
                        import sys
                        class ScopeReplacer(object):
                            def test_ScopeReplacer___getattribute__():
                                import sys
                                def test_ScopeReplacer___getattribute__():
                                    import sys
                                    def test_ScopeReplacer___getattribute__():
                                        import sys

# Generated at 2022-06-14 06:05:16.618254
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """IllegalUseOfScopeReplacer -- str"""
    from bzrlib.lazy_import import IllegalUseOfScopeReplacer
    e = IllegalUseOfScopeReplacer('foo', 'msg', 'extra')
    s = str(e)
    assert 'foo' in s
    assert 'msg' in s
    assert 'extra' in s



# Generated at 2022-06-14 06:05:20.394531
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """Unit test for method __unicode__ of class IllegalUseOfScopeReplacer"""
    # Make sure that (a) __unicode__ returns a unicode object, and
    # (b) the UnicodeDecodeError raised in the default __unicode__
    # implementation is caught in __unicode__.
    e = IllegalUseOfScopeReplacer('foo name', 'foo message')
    e._fmt = 'foo fmt'
    u = e.__unicode__()
    # py3k compat: __unicode__ is called __str__, and the result is
    # already a unicode object.
    if not isinstance(u, unicode):
        u = unicode(u)
    assert u.__class__ is unicode


# Generated at 2022-06-14 06:05:28.477721
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """Test of method __unicode__ of class IllegalUseOfScopeReplacer"""
    from bzrlib._lazy_import_pyx import ScopeReplacer
    e = IllegalUseOfScopeReplacer(
        'name', 'msg', 'extra')
    u = unicode(e)
    assert u == 'ScopeReplacer object \'name\' was used incorrectly: msg: extra', \
        'Unicode representation of exception should be as expected.'
    assert isinstance(u, unicode), \
        'Unicode representation should be a unicode object'
    # The following lines should not be translated by xgettext whatsoever.
    assert str(e) == 'ScopeReplacer object \'name\' was used incorrectly: msg: extra', \
        'String representation of exception should be as expected.'

# Generated at 2022-06-14 06:05:37.124223
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    import collections
    class A:
        def __init__(self):
            self.args = []
        def __call__(self, *args, **kwargs):
            self.args.append((args, kwargs))
    a = A()
    b = ScopeReplacer(locals(), lambda x, y, z: a, 'a')
    assert b(1, a=2) is a
    assert a.args == [( (1,), {'a': 2} )]

# Generated at 2022-06-14 06:05:57.553817
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    from bzrlib import lazy_import
    from bzrlib.tests import TestCase
    from bzrlib.tests.test_lazy_import import Module, get_importer

    class TestScopeReplacer(TestCase):

        def setUp(self):
            TestCase.setUp(self)
            self.addCleanup(ScopeReplacer._replace_globals,
                            lazy_import._globals)

        def _fake_module(self):
            """Return a fake module.

            :returns: A fake module object with a counter variable that can be
                incremented.
            """
            return Module({'counter': 0}, 'test_fake_module',
                          get_importer())


# Generated at 2022-06-14 06:06:09.947785
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """Unit test for method __unicode__ of class IllegalUseOfScopeReplacer"""
    import bzrlib.tests
    # Note that all check_* methods take unicode strings, strictly.
    # These tests check the behaviour when a string str is passed or when
    # a unicode with non-ascii characters is passed.
    # Also the unicode formatting should work with the default encoding.
    # There is no need to make the tests pass with both the default encoding
    # and with a non-ascii-compatible encoding: it is enough to test that
    # the encoding is used at all.

    # If there is an error while formatting the exception,
    # str(IllegalUseOfScopeReplacer()) should not raise an exception.
    # It should just return a string describing the problem and the exception.
    # See lp:848601 to

# Generated at 2022-06-14 06:06:15.124698
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    import bzrlib._lazy_import_tests
    obj, _scope = bzrlib._lazy_import_tests._make_scope_replacer_obj()
    d = {}
    obj.__setattr__("__dict__", d)
    return d

# Generated at 2022-06-14 06:06:20.555436
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    # Simple instantiation and test of return value
    s = ScopeReplacer({}, lambda self, scope, name: self, '')
    s.__class__.__call__ = None
    assert_raises(TypeError, s)
    assert_raises(TypeError, s, 2)
    assert_raises(TypeError, s, x=3)



# Generated at 2022-06-14 06:06:27.151465
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    import sys
    # Test that IllegalUseOfScopeReplacer(name, msg) can be stringified
    e = IllegalUseOfScopeReplacer('foo', 'bar')
    msg = str(e)
    if sys.version_info[0] < 3:
        e = IllegalUseOfScopeReplacer('foo', u'bar')
        msg = str(e)



# Generated at 2022-06-14 06:06:31.958613
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    # test return value
    # TODO: make sure that the return value is a function
    assert True

    # test attribute access
    # TODO: make sure that we can access the attributes of the return value
    # (i.e. a function)
    assert True

    # test calling
    # TODO: make sure that we can call the return value (i.e. a function)
    assert True



# Generated at 2022-06-14 06:06:45.537586
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    from random import normalvariate as n
    from math import hypot
    from math import pi as PI
    class Point:
        def __init__(self, x, y):
            self.x, self.y = x, y
        def __hash__(self):
            return hash((self.x, self.y))
        def __add__(self, other):
            return Point(self.x + other.x, self.y + other.y)
        def __repr__(self):
            return 'Point(%s, %s)' % (self.x, self.y)
        def distance(self, other):
            dx, dy = self.x - other.x, self.y - other.y
            return hypot(dx, dy)

# Generated at 2022-06-14 06:06:57.628384
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    #__call__(self, *args, **kwargs) -> value
    import bzrlib.lazy_import
    bzrlib.lazy_import._test_ScopeReplacer___call__ = False
    def f(self, *args, **kwargs):
        return (args, kwargs)
    bzrlib.lazy_import._test_ScopeReplacer___call__ = False
    sr = bzrlib.lazy_import.ScopeReplacer(
        bzrlib.lazy_import.__dict__, f, '_test_ScopeReplacer___call__')
    args = (1, 2, 3)
    kwargs = {'a':5, 'b':'c'}
    value = sr(*args, **kwargs)
    return (value == (args, kwargs))

# Generated at 2022-06-14 06:07:01.323268
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    s = IllegalUseOfScopeReplacer('foo', 'bar')
    assert isinstance(s, Exception)
    assert str(s) == "ScopeReplacer object 'foo' was used incorrectly: bar"


# Generated at 2022-06-14 06:07:14.540224
# Unit test for method __setattr__ of class ScopeReplacer

# Generated at 2022-06-14 06:07:39.860773
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    import sys
    import subprocess
    # There is no support for unicode in python on win32
    # TODO: Jam 20060420 This should be handled by lazy_import, which
    # should not need to be tested that way anyway, but it is not.
    if sys.platform == 'win32':
        return
    # Check for unicode support
    try:
        # python >= 2.4
        subprocess.Popen(['true'], universal_newlines=True)
    except (AttributeError, ValueError):
        # python < 2.4
        raise TestSkipped("module subprocess doesn't support universal_newlines")

    e = IllegalUseOfScopeReplacer('foo', 'bar', extra='baz')

# Generated at 2022-06-14 06:07:52.067712
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """IllegalUseOfScopeReplacer.__str__() works like we expect."""
    # Test for normal formatting
    e = IllegalUseOfScopeReplacer(name='foo', msg='it blew up')
    assert str(e) == 'foo: it blew up'
    # Test for normal formatting with extra details
    e = IllegalUseOfScopeReplacer(name='foo', msg='it blew up', extra=42)
    assert str(e) == 'foo: it blew up: 42'
    # Test for error in formatting
    e = IllegalUseOfScopeReplacer(name='foo', msg='it blew up', extra=None)
    del e.extra
    assert str(e).startswith('Unprintable exception IllegalUseOfScopeReplacer')



# Generated at 2022-06-14 06:07:59.021684
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__ should produce sensible output"""
    e = IllegalUseOfScopeReplacer("foo", "bar")
    expected = u"IllegalUseOfScopeReplacer object 'foo' was used incorrectly: bar"
    raise AssertionError("%r\n!=\n%r" % (e, expected))



# Generated at 2022-06-14 06:08:10.082615
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    from bzrlib import errors
    import bzrlib.lazy_import
    def check_str(obj, str):
        assert (str(obj) == str or
                obj.__class__.__name__ + '(' + str + ')' == str(obj))
    def check_exception_str(exc_name, fmt, args, str):
        exc = exceptions[exc_name](fmt, *args)
        check_str(exc, str)
    def check_exception_repr(exc_name, fmt, args, str):
        exc = exceptions[exc_name](fmt, *args)
        assert repr(exc) == '%s(%s)' % (exc_name, str)
    exc_fmt = bzrlib.lazy_import.IllegalUseOfScopeReplacer._fmt

# Generated at 2022-06-14 06:08:16.405484
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    x = ScopeReplacer('scope', 'factory', 'x')
    x = ScopeReplacer('scope', 'factory', 'y')
    x.r = x
    x.s = x
    x.t = x
    x.u = x
    x.v = x
    x.w = x
    x.x = x # this should be reported as a IllegalUseOfScopeReplacer


# Generated at 2022-06-14 06:08:22.688711
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
    """
    # Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
    e = IllegalUseOfScopeReplacer('foo', 'bar', 'baz')
    assert unicode(e) == u'foo was used incorrectly: bar: baz'



# Generated at 2022-06-14 06:08:31.927147
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """Some easy cases"""
    from breezy.tests import TestCase
    from breezy.tests.per_interactor import TestCaseWithInteractor

    class IllegalUseOfScopeReplacerTests(TestCase):

        def test_good_fmt(self):
            e = IllegalUseOfScopeReplacer('name', 'msg')
            self.assertEqual('name', e.name)
            self.assertEqual('msg', e.msg)
            self.assertEqual('', e.extra)
            self.assertEqual(
                "ScopeReplacer object 'name' was used incorrectly: msg",
                str(e))

        def test_bad_fmt(self):
            e = IllegalUseOfScopeReplacer(None, None)

# Generated at 2022-06-14 06:08:37.858404
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """IllegalUseOfScopeReplacer.__unicode__()

    __unicode__() should return a unicode object.
    """
    e = IllegalUseOfScopeReplacer('a', 'b')
    r = repr(e)
    e1 = IllegalUseOfScopeReplacer('a', 'b')
    r1 = repr(e1)
    u = unicode(e)
    u1 = unicode(e1)
    return



# Generated at 2022-06-14 06:08:48.318061
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__ should return a unicode object."""
    u = IllegalUseOfScopeReplacer('foo', 'bar')
    # Testing object 'eq'
    msg = u'IllegalUseOfScopeReplacer(foo, bar)'
    expected = msg
    result = unicode(u)
    assert expected == result, "%r != %r" % (expected, result)
    # Testing object 'ne'
    msg = u'IllegalUseOfScopeReplacer(bar, foo)'
    expected = msg
    result = unicode(u)
    assert expected != result, "%r == %r" % (expected, result)
    # Testing object 'lt'
    msg = u'IllegalUseOfScopeReplacer(bar, baz)'
    expected = msg
    result = unicode(u)

# Generated at 2022-06-14 06:08:50.970547
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """Unit test for method IllegalUseOfScopeReplacer.__unicode__"""
    import bzrlib.errors   # required to test the load_module code

    def _make_scope():
        d = locals()

# Generated at 2022-06-14 06:09:24.776725
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """Test method __unicode__ of class IllegalUseOfScopeReplacer"""
    s = IllegalUseOfScopeReplacer('name', 'msg', 'extra')
    assert_equal(unicode(s), u"name was used incorrectly: msg: extra")
    assert_equal(str(s), "name was used incorrectly: msg: extra")
    assert_equal(repr(s), "IllegalUseOfScopeReplacer('name was used incorrectly: msg: extra')")



# Generated at 2022-06-14 06:09:32.843957
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    # verify that we correctly raise IllegalUseOfScopeReplacer when it's used
    # after it's been replaced.
    scope = {}
    def replace(scope_replacer, scope, name):
        # This factory simply returns the scope_replacer as the replacement.
        return scope_replacer
    from bzrlib import lazy_import
    lazy_import.ScopeReplacer._should_proxy = False
    sr = lazy_import.ScopeReplacer(scope, replace, 'foo')
    # Now that one has replaced itself, no more setting on it should be allowed
    def set_again():
        sr.bar = 'baz'
    e = lazy_import.IllegalUseOfScopeReplacer

# Generated at 2022-06-14 06:09:45.659573
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    import sys
    import bzrlib
    # Testing attribute _should_proxy of class ScopeReplacer
    # Testing override of method _resolve of class ScopeReplacer
    # Testing override of method __setattr__ of class ScopeReplacer
    # Testing override of method __getattribute__ of class ScopeReplacer
    # Testing override of method __call__ of class ScopeReplacer
    from bzrlib.lazy_import import lazy_import
    import bzrlib.transport.memory
    if 'bzrlib.transport' in sys.modules:
        del sys.modules['bzrlib.transport']
    if 'bzrlib.transport.memory' in sys.modules:
        del sys.modules['bzrlib.transport.memory']