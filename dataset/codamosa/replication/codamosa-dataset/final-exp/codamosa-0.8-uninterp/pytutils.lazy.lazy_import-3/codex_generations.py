

# Generated at 2022-06-14 05:59:58.376367
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__ should return a unicode object."""
    e = IllegalUseOfScopeReplacer('foo', 'bar')
    result = unicode(e)
    expected = u'IllegalUseOfScopeReplacer(foo)'
    # The format of the unicode object is not important, but make sure that the
    # result is a unicode object.
    assert isinstance(result, unicode)
    assert result == expected


# Generated at 2022-06-14 06:00:09.278784
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    # This test is only needed when the exception does not implement a
    # format string for __str__ (or __unicode__).
    e = IllegalUseOfScopeReplacer('foo', 'not found')
    s = str(e)
    eq(s,
        "Unprintable exception IllegalUseOfScopeReplacer: dict={'extra': '', 'msg': 'not found', 'name': 'foo'}, fmt=None, error=None")
    # If a new format string is added to the class, it will be used to
    # format this instance.
    IllegalUseOfScopeReplacer._fmt = 'Message %(msg)s (for %(name)r)'
    s = str(e)
    eq(s, 'Message not found (for foo)')
    # This instance is not formatted by the format string for class
    # IllegalUse

# Generated at 2022-06-14 06:00:14.702813
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """Test method __str__ of class IllegalUseOfScopeReplacer.

    Unfortunately, we cannot write a unit test for method __str__ of class
    IllegalUseOfScopeReplacer. The reason is that that method has side
    effects which cannot get reversed: It installs a new text domain.
    """


# Generated at 2022-06-14 06:00:19.070745
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """__str__ should return a str object"""
    x = IllegalUseOfScopeReplacer('name', 'msg', 'extra')
    # must return an 8-bit-string
    assert isinstance(str(x), str)

# Generated at 2022-06-14 06:00:27.184892
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """IllegalUseOfScopeReplacer.__unicode__ does not raise on fake error

    This catches the same type of issues that occurred in the past with
    the following errors:

    * without errors: UnicodeEncodeError: 'ascii' codec can't encode
      character u'\\xf6' in position 5: ordinal not in range(128)
    * with errors: UnicodeEncodeError: 'ascii' codec can't encode
      character u'\\xf6' in position 5: ordinal not in range(128)
      (error occurs in _format of Exception class)
    """
    try:
        raise IllegalUseOfScopeReplacer('name', "msg", extra=u"\xf6")
    except IllegalUseOfScopeReplacer as e:
        unicode(e)



# Generated at 2022-06-14 06:00:40.170980
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """__str__ should return the same whether or not _fmt is defined.

    Additionally, it should not throw an exception.
    """
    class X1(IllegalUseOfScopeReplacer):
        pass
    x1 = X1('foo', 'bar')
    # Normal format strings from _fmt result in a str being returned
    assert isinstance(str(x1), str)
    # Calling str() before __init__ finishes results in a str being returned
    class X2(IllegalUseOfScopeReplacer):
        def __init__(self):
            self._fmt = "foo %(bar)s"
            self.bar = 'bar'
    x2 = X2()
    assert isinstance(str(x2), str)
    # If _fmt is not defined, then a str is returned

# Generated at 2022-06-14 06:00:50.950813
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    class SomeInstance(object):
        def __init__(self, value):
            self.value = value
        def __call__(self):
            return self.value
    value = 77
    def factory(self, scope, name):
        return SomeInstance(value)
    def check(self, scope, name, args, kwargs, expected):
        obj = ScopeReplacer(scope, factory, name)
        actual = obj(*args, **kwargs)
        assert expected == actual
    d = {}
    check(None, 'obj', d, (), 77)
    check(None, 'obj', d, (1, 2), 77)



# Generated at 2022-06-14 06:01:02.150505
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    from bzrlib import lazy_import
    from bzrlib.tests import TestCase
    class MyTestCase(TestCase):
        pass
    import bzrlib.tests
    lazy_import(locals(), '''
    from bzrlib.tests import (
        TestCase,
        )
    ''')
    s = ScopeReplacer(locals(), lazy_import.lazy_import_scope_replacer,
        'TestCase')

# Generated at 2022-06-14 06:01:09.607618
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """IllegalUseOfScopeReplacer.__unicode__ with default message"""
    ex = IllegalUseOfScopeReplacer('foo', 'nasty message')
    u = unicode(ex)
    assert isinstance(u, unicode)
    assert u.startswith('IllegalUseOfScopeReplacer(')
    assert u.endswith(')')


# Generated at 2022-06-14 06:01:18.760103
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    from bzrlib.tests import TestCase
    from bzrlib.lazy_import import ScopeReplacer
    class Callable(object):
        def __init__(self, value):
            self.value = value
        def __call__(self, *args, **kwargs):
            return self.value
    class Test(TestCase):
        """Unit test for method __call__ of class ScopeReplacer."""
        def test_it(self):
            value = "test"
            instance = Callable(value)
            ScopeReplacer(locals(), lambda self, scope, name: instance,
                          "instance")
            self.assertEquals(value, instance())
    test = Test()
    test.run()



# Generated at 2022-06-14 06:01:37.775924
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    from bzrlib.tests import TestCase
    from bzrlib.lazy_import import IllegalUseOfScopeReplacer
    e = IllegalUseOfScopeReplacer('foo', 'something bad happened', 1)
    TestCase().assertEqual("foo was used incorrectly: something bad happened: 1",
                           str(e))
    class LongString(IllegalUseOfScopeReplacer):
        _fmt = "a very long string..." * 1000

# Generated at 2022-06-14 06:01:49.848919
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """Unit test for method __unicode__ of class IllegalUseOfScopeReplacer"""
    import sys
    if sys.version_info[0] <= 2:
        # In python 2.x, __unicode__ should return a unicode object
        obj = IllegalUseOfScopeReplacer('name', 'msg', extra='extra')
        # Try to make a unicode object from it, because __unicode__ must
        # return a unicode object.
        u = unicode(obj)
        assert isinstance(u, unicode)
        assert u == u'name was used incorrectly: msg: extra'
    else:
        # In python 3.x, __unicode__ is actually __str__, so this is what is
        # tested.
        obj = IllegalUseOfScopeReplacer('name', 'msg', extra='extra')

# Generated at 2022-06-14 06:01:59.808514
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """IllegalUseOfScopeReplacer.__unicode__()

    __unicode__() should be defined for all exceptions, and should return
    a unicode object.
    """
    e = IllegalUseOfScopeReplacer('foo', 'bar')
    u = unicode(e)
    assert type(u) is unicode, \
        "Unexpected type of __unicode__() returned %s: expected: 'unicode'" \
        % type(u)
# Test for method __str__ of class IllegalUseOfScopeReplacer

# Generated at 2022-06-14 06:02:06.418688
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """__str__ should return a str object.

    This test is especially for the case where self._format() returns
    a unicode object.
    """
    # The case where self._format() returns a str object is checked
    # later in the test, so we don't need to test it here.
    e = IllegalUseOfScopeReplacer('name', 'msg')
    s = e.__str__()
    assert isinstance(s, str)

# Generated at 2022-06-14 06:02:17.800091
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    # this method is used by _do_import as a last resort, when an
    # import fails. This is in order to give the user a good chance
    # at seeing why an import failed, even if a plugin is keeping
    # tracebacks from being displayed.
    #
    # The output is currently an approximation of the behaviour of
    # AttributeError.
    #
    # It would be a better approximation if we could get python to
    # print the repr of the object, rather than the str.
    import doctest
    output = doctest.testmod(sys.modules[__name__])
    # if output[0] != 0:
    #     raise Exception(output)



# Generated at 2022-06-14 06:02:27.808794
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    """__setattr__ should raise an IllegalUseOfScopeReplacer exception
    if the ScopeReplacer's _real_obj is not None and ScopeReplacer._should_proxy
    is False.
    """
    scope = {}
    scope_replacer_obj = ScopeReplacer(scope, local_import, 'foo')
    scope['foo']._should_proxy = False
    scope['foo']._real_obj = object()

# Generated at 2022-06-14 06:02:38.268837
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    from bzrlib.tests.blackbox import ExternalBase
    test = ExternalBase()
    class test_existing(ExternalBase):
        def test_instance_of_scope_replacer(self):
            from bzrlib.lazy_import import lazy_import
            lazy_import(globals(), """
            from bzrlib import (
                )
            """)
            self.assertIsInstance(foo, ScopeReplacer)
            # Still lazy after first access:
            self.assertIsInstance(foo, ScopeReplacer)
            # Assignment already is disallowed:
            self.assertRaises(IllegalUseOfScopeReplacer, setattr, foo, 'bar', 1)
    test.run_tests(test_existing)

# Generated at 2022-06-14 06:02:47.447189
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """__str__ should decode all the non-ascii strings in the exception"""
    from bzrlib.i18n import gettext
    class UnicodeRaisingError(Exception):
        _fmt = gettext("An error with a unicode message: %(code)s")
        def __init__(self, code):
            self.code = code

# Generated at 2022-06-14 06:02:59.569366
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    from bzrlib.tests import TestCase, TestCaseWithTransport
    from bzrlib.lazy_import import lazy_import, lazy_class
# end TestCaseWithTransport

    test_cases = [
        ('bzrlib', 'Transport', TestCaseWithTransport),
        ('bzrlib.tests', 'TestCase', TestCase),
        ]

    for mod_name, name, cls in test_cases:
        _scope = {}
        lazy_import(_scope, 'from %s import %s' % (mod_name, name))
        # getattr(TestCaseWithTransport, 'assertRaises')
        assert getattr(_scope[name], 'assertRaises') is cls.assertRaises
        # TestCaseWithTransport.assertRaises

# Generated at 2022-06-14 06:03:12.518762
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    import random
    import unittest

    class Test(unittest.TestCase):

        def test_ScopeReplacer___setattr__(self):
            import bzrlib._scope_replacer
            bzrlib._scope_replacer._should_proxy = random.sample((False, True), 1)[0]
            _scope = { }
            _factory = random.sample((None, ), 1)[0]
            _name = random.sample((None, ), 1)[0]
            _real_obj = random.sample((None, ), 1)[0]
            x = bzrlib._scope_replacer.ScopeReplacer(_scope, _factory, _name)
            __getattribute__ = random.sample(((None, _factory), ), 1)[0]

# Generated at 2022-06-14 06:03:23.724108
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    import bzrlib
    _test_ScopeReplacer___setattr__(bzrlib.__dict__)
test_ScopeReplacer___setattr__.__test__ = False


# Generated at 2022-06-14 06:03:28.856386
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    from bzrlib.scope import ScopeReplacer
    def a_func():
        pass
    scope = locals()
    factory = lambda scope, name: scope[name]
    scopeReplacer = ScopeReplacer(scope, factory, 'a_func')
    scopeReplacer.__setattr__('a_func', 'a_value')


# Generated at 2022-06-14 06:03:42.477717
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    """__setattr__ of ScopeReplacer must not raise any exception"""
    # This test simply checks whether the method raises any exception
    # when called with valid arguments.
    # The only use of setattr on ScopeReplacer instances observed
    # in the code is in a selftest checking that they are not
    # overused. This test is therefore not expected to be
    # useful in practise.
    obj = ScopeReplacer(None, None, None)
    def test_with_valid_arguments(self):
        obj.__setattr__(self, None, None)
    try:
        test_with_valid_arguments(None)
    except Exception as e:
        raise AssertionError(
            "__setattr__ of ScopeReplacer should not have raised %s" \
            % (type(e),))

# Generated at 2022-06-14 06:03:52.275765
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """__str__(msg) -> str(msg)?"""
    # Test if the __str__ method returns a real str object or not
    def _test(msg):
        e = IllegalUseOfScopeReplacer('name', msg)
        s = str(e)
        ok = isinstance(s, str)
        if not ok:
            raise AssertionError(
                'str(%r) => %r, not str' % (e, s))
    _test('hello world')
    _test('abc'*1000)



# Generated at 2022-06-14 06:03:56.625908
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """IllegalUseOfScopeReplacer.__unicode__() => unicode object"""
    exc = IllegalUseOfScopeReplacer('foo', 'bar')
    assert isinstance(exc.__unicode__(), unicode)

# Generated at 2022-06-14 06:04:05.356246
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    """__setattr__ must work even after the object is resolved"""
    # Create an instance of ScopeReplacer
    import sys
    import tempfile
    from bzrlib.conflicts import ConflictList
    from bzrlib.trace import mutter
    from bzrlib.lazy_import import lazy_import
    lazy_import(globals(), """
from bzrlib import (
    conflicts,
    merge,
    osutils,
    )
""")
    class FakeObject(object):
        def __init__(self):
            self._attr = None
        def __setattr__(self, key, value):
            if key == '_attr':
                object.__setattr__(self, key, value)

# Generated at 2022-06-14 06:04:09.274881
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__ of IllegalUseOfScopeReplacer"""
    e = IllegalUseOfScopeReplacer('name', 'message', 'extra')
    expected = u'name was used incorrectly: message: extra'
    assert e.__unicode__() == expected
    assert unicode(e) == expected



# Generated at 2022-06-14 06:04:20.494785
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    class DummyScopeReplacer(object):
        def __init__(self, scope):
            self.scope = scope
        def __getattr__(self, attr):
            self.scope[attr] = object()
            return self.scope[attr]
    import UserDict
    import sys
    scope = UserDict.UserDict()
    scope['sys'] = sys
    scope['replacer'] = DummyScopeReplacer(scope)
    scope['replacer'].__getattr__('spam')
    scope['replacer'].__getattr__('baz')
    scope['replacer'].__getattr__('baz')
    scope['replacer'].__getattr__('eggs')
    scope['replacer'].__getattr__('eggs')
    scope['replacer'].__getattr__

# Generated at 2022-06-14 06:04:24.869233
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """__str__ should return a str"""
    i = IllegalUseOfScopeReplacer('name', 'msg', 'extra')
    assert isinstance(i.__str__(), str)



# Generated at 2022-06-14 06:04:35.322962
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """IllegalUseOfScopeReplacer" should be able to produce unicode strings."""
    def check(expect, _fmt=None, **kwargs):
        """Check that a message formatted with kwargs gives expect."""
        # TODO: jam 20051222 This is a nice generic method we could export
        if _fmt is not None:
            klass = IllegalUseOfScopeReplacer
            klass._fmt = _fmt
        try:
            e = IllegalUseOfScopeReplacer(**kwargs)
        except Exception:
            raise AssertionError('%s(%r) raised %s'
                                 % (IllegalUseOfScopeReplacer.__name__,
                                    kwargs, str(sys.exc_info()[1])))
        else:
            got = str(e)

# Generated at 2022-06-14 06:04:53.987364
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    import bzrlib.lazy_import
    import bzrlib.tests
    import bzrlib.tests.test_lazy_import
    import bzrlib.trace
    import bzrlib.tsort
    import bzrlib._dirstate_helpers
    import bzrlib.osutils
    import bzrlib.inter
    import bzrlib.branch
    import bzrlib.trace
    import bzrlib._dirstate_helpers
    import bzrlib.branch
    import bzrlib.trace
    import bzrlib._dirstate_helpers
    import bzrlib.branch
    import bzrlib.trace
    import bzrlib._dirstate_helpers
    import bzrlib.branch
   

# Generated at 2022-06-14 06:05:07.144159
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    """Test for method ScopeReplacer.__setattr__"""
    from bzrlib import lazy_import; from bzrlib import (lazy_import,)
    from bzrlib.tests import TestCase
    import unittest
    # Simulate a module that has been imported with the
    # lazy_import function
    def create_module():
        return ModuleMock()
    class ModuleMock(object): # Mock object, has attribute like a module
        # When called return self
        def __call__(self, *args, **kwargs):
            return self
        # Create an empty attribute with the given name
        def __getattribute__(self, attr):
            return self
        def __setattr__(self, attr, value):
            return self

# Generated at 2022-06-14 06:05:21.561441
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    import doctest
    # The doctest module is used to construct an object that also has
    # the imported module name (e.g. bzrlib.branch) in it's globals.
    # This is used to simulate a module that is importing a submodule.
    import_str = "import bzrlib.branch"
    module = doctest.DocTestParser().get_doctest(import_str, {}, "", "", None)
    scope = module.globs
    scope['bzrlib'] = ScopeReplacer(scope, lambda x, scope, name: x, "bzrlib")
    scope['bzrlib'].branch = ScopeReplacer(scope, lambda x, scope, name: x,
        "branch")

    import bzrlib.branch
    bzrlib.br

# Generated at 2022-06-14 06:05:32.472884
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    from time import time
    now = time()
    def constant(replacer):
        return now
    lazy_import(globals(), '''
    import time
    ''')
    time.sleep(0.1) # make sure "now" is different from real time
    # This should be a no-op, but it is not.
    # Pyrex gets it right, but python the creator object is not a
    # ScopeReplacer.
    # Test if the bug was fixed.
    now.__setattr__('foo', 'foo')
    now.__setattr__('bar', 'bar')
    assert now.foo == 'foo'
    assert now.bar == 'bar'
    # But regular use is fixed.
    assert time.time() != now


# Generated at 2022-06-14 06:05:36.059111
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """IllegalUseOfScopeReplacer.__str__ should return utf8 encoded str"""
    e = IllegalUseOfScopeReplacer('name', u'\u1234')
    s = str(e)
    if not isinstance(s, str):
        raise AssertionError('Expected str object, got %r' % s)
    if not all(ord(c) < 128 for c in s):
        raise AssertionError('Expected str, not unicode: %r' % s)
    if not s.decode('utf8').startswith(u'\u1234'):
        raise AssertionError('String %r does not start with utf8 string %r'
            % (s, u'\u1234'.encode('utf8')))


# Generated at 2022-06-14 06:05:43.390555
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__ should always return unicode"""
    c = IllegalUseOfScopeReplacer('name', 'msg', 'extra')
    r = unicode(c)
    assert isinstance(r, unicode)
    c = IllegalUseOfScopeReplacer(u'name', u'msg', u'extra')
    r = unicode(c)
    assert isinstance(r, unicode)



# Generated at 2022-06-14 06:05:51.860197
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """
    IllegalUseOfScopeReplacer.__str__ should return a str object.
    """
    er = IllegalUseOfScopeReplacer('name', 'msg')
    s = er.__str__()
    e = er.__unicode__()
    if not isinstance(s, str):
        raise AssertionError(s)
    for c in e:
        if ord(c) > 127:
            raise AssertionError(c)



# Generated at 2022-06-14 06:06:03.257041
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    """test method __call__ of class ScopeReplacer"""
    import random
    import math
    random.seed(a=1234567890)
    def tmp(self, scope, name):
        return math.exp(1)
    scope = {}
    name = 'e'
    scope_replacer = ScopeReplacer(scope=scope, factory=tmp, name=name)
    scope_replacer()
    scope_replacer._should_proxy = False
    scope['e'] = 'fooo'

# Generated at 2022-06-14 06:06:17.082629
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """__str__ of IllegalUseOfScopeReplacer"""
    # __str__ is not a public API and should not be changed without
    # providing super-compatible test coverage.
    # See https://bugs.launchpad.net/bzr/+bug/642356
    # See https://bugs.launchpad.net/bzr/+bug/716166
    # See PEP352

    # Let's bind the variables
    o = 'o'
    m = 'm'
    e = 'e'
    f = '_fmt'
    s = "_preformatted_string"
    # And unbind them
    del o
    del m
    del e
    del f
    del s

    # Now, let's see if we can replace the methods for IllegalUseOfScopeReplacer.
    # If we can't, an exception

# Generated at 2022-06-14 06:06:30.636447
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """__str__ of IllegalUseOfScopeReplacer"""
    # __str__ is only a proxy to the real method _format()

    # Part 1: _format() returns a str
    # The result of __str__ should be a str.
    def _format():
        return 'hello world'
    class TypeUnderTest(IllegalUseOfScopeReplacer):
        def __init__(self, name, msg, extra=None):
            super(TypeUnderTest, self).__init__(name, msg, extra)
    t = TypeUnderTest('name', 'msg')
    t._format = _format
    assert isinstance(t.__str__(), str)

    # Part 2: _format() returns an unicode
    # The result of __str__ should be a str.
    def _format():
        return u'hello world'
   

# Generated at 2022-06-14 06:06:49.160401
# Unit test for method __getattribute__ of class ScopeReplacer
def test_ScopeReplacer___getattribute__():

    def wrap(obj):
        def f(*args, **kwargs):
            return obj
        return f
    class S(object):
        def __init__(self, v):
            self.v = v
        def __getattribute__(self, attr):
            return wrap(getattr(object.__getattribute__(self, 'v'), '__getattribute__')(attr))
    class C(object):
        def __init__(self, v):
            self.v = v
        def __getattribute__(self, attr):
            return wrap(getattr(object.__getattribute__(self, 'v'), '__getattribute__')(attr))
    class I(object):
        def __init__(self, v):
            self.v = v

# Generated at 2022-06-14 06:06:52.875725
# Unit test for method __getattribute__ of class ScopeReplacer
def test_ScopeReplacer___getattribute__():
    class TestClass(ScopeReplacer):
        pass

    t = TestClass()

    t._fmt = '%(msg)s'

    t._fmt


# Generated at 2022-06-14 06:07:03.029485
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    import unittest
    class ScopeReplacerTest(unittest.TestCase):
        def test___call__(self):
            import sys
            def foo(self, scope, name):
                return 42
            def bar():
                return foo(None, None, None)
            scope = sys._getframe(0).f_locals

            scope['foo'] = ScopeReplacer(scope, foo, 'foo')
            scope['bar'] = ScopeReplacer(scope, bar, 'bar')
            self.assertEqual(bar(), 42)
    return unittest.makeSuite(ScopeReplacerTest)


# Generated at 2022-06-14 06:07:06.595832
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """__str__ should work."""
    # This is a very simple test, which basically checks that calling
    # __str__() doesn't cause an exception.
    e = IllegalUseOfScopeReplacer('scope', 'msg', None)
    e.__str__()



# Generated at 2022-06-14 06:07:19.573126
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """Test method __str__ of class IllegalUseOfScopeReplacer

    This is done in an un-localised environment to make sure that
    the format string gets used.
    """
    import bzrlib
    bzrlib._gettext_installed = False
    def translate_exc(exc):
        if isinstance(exc, Exception):
            return IllegalUseOfScopeReplacer(exc.__class__.__name__,
                'foo', 'bar')
        return exc

# Generated at 2022-06-14 06:07:27.102014
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """This checks that IllegalUseOfScopeReplacer correctly raises an
    exception when called.

    """

# Generated at 2022-06-14 06:07:38.059206
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """Method __str__ of class IllegalUseOfScopeReplacer"""
    # see test_errors.py for more tests
    e = IllegalUseOfScopeReplacer('foo', 'bar', 'extra')
    e.__dict__['_preformatted_string'] = 'preformatted'
    s = str(e)
    assert type(s) is str, s
    s = unicode(e)
    assert type(s) is unicode, type(s)
    e.__dict__['_fmt'] = '%(msg)s %(extra)s'
    s = str(e)
    assert type(s) is str, s
    s = unicode(e)
    assert type(s) is unicode, type(s)



# Generated at 2022-06-14 06:07:43.416562
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """__str__ of IllegalUseOfScopeReplacer
    """
    e = IllegalUseOfScopeReplacer('foo', 'msg', 'extra')
    assert str(e) == 'foo: msg: extra', "__str__(%r) != 'foo: msg: extra'" % (e,)


# Generated at 2022-06-14 06:07:52.700950
# Unit test for method __getattribute__ of class ScopeReplacer
def test_ScopeReplacer___getattribute__():
    class Foo(object):
        def __init__(self, x):
            self.x = x
        def __eq__(self, other):
            return self.x == other.x

    class Bar(object):
        __slots__ = ['_scope', '_factory', '_name', '_real_obj']
        def __init__(self, scope, factory, name):
            object.__setattr__(self, '_scope', scope)
            object.__setattr__(self, '_factory', factory)
            object.__setattr__(self, '_name', name)
            object.__setattr__(self, '_real_obj', None)
            scope[name] = self
        def _resolve(self):
            name = object.__getattribute__(self, '_name')


# Generated at 2022-06-14 06:08:07.101266
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    from bzrlib.lazy_import import lazy_import
    scope = {}
    lazy_import(scope, """
    from bzrlib import osutils
    from bzrlib.osutils import normpath
    """)
    assert scope['osutils'].normpath('/') == '/'
try:
    _ = test_ScopeReplacer___call__()
except NameError:
    pass

    def __delattr__(self, attr):
        obj = object.__getattribute__(self, '_resolve')()
        return delattr(obj, attr)

    def __getitem__(self, attr):
        obj = object.__getattribute__(self, '_resolve')()
        return obj.__getitem__(attr)


# Generated at 2022-06-14 06:08:31.141076
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    import sys
    import doctest
    from bzrlib.lazy_import import lazy_import, ScopeReplacer
    module_globals = sys.modules[__name__].__dict__

# Generated at 2022-06-14 06:08:40.642777
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    from StringIO import StringIO
    from bzrlib.tests import TestCase
    from bzrlib.lazy_import import ScopeReplacer
    class Foo(object):
        def bar(self, x):
            return x
    scope = {}
    replacer = ScopeReplacer(scope, lambda x, y, z: Foo(), 'foo')
    replacer.bar(1)
    scope['foo'].bar(2)
    scope2 = {'foo':Foo}
    scope2['foo'].bar(2)
    scope2['foo'] = replacer
    scope2['foo'].bar(2)
    scope2['foo'] = Foo
    scope2['foo'].bar(2)


# Generated at 2022-06-14 06:08:51.712142
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__ of IllegalUseOfScopeReplacer

    This test verifies that IllegalUseOfScopeReplacer.__unicode__ returns
    a unicode object and that it has the right value.
    """
    e = IllegalUseOfScopeReplacer(
        name='name',
        msg='message',
        extra='extra arg')
    import bzrlib.i18n
    bzrlib.i18n.setup_i18n()
    try:
        e_str = unicode(e)
    except Exception as e:
        raise AssertionError(e)
    if not isinstance(e_str, unicode):
        raise AssertionError('Return value is not unicode: %r' % (e_str,))

# Generated at 2022-06-14 06:08:57.567968
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__() should format messages properly."""
    try:
        raise IllegalUseOfScopeReplacer('var', 'was accessed', 1)
    except IllegalUseOfScopeReplacer as e:
        assert str(e) == 'var was accessed: 1'
        assert unicode(e) == u'var was accessed: 1'

# Generated at 2022-06-14 06:09:02.853218
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    e = IllegalUseOfScopeReplacer('name', 'msg', 'extra')
    s = str(e)
    assert 'ScopeReplacer object \'name\'' in s
    assert 'msg' in s
    assert 'extra' in s


# Generated at 2022-06-14 06:09:10.203409
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    class TestClass(ScopeReplacer):
        def __init__(self, scope, factory, name):
            super(TestClass, self).__init__(scope, factory, name)
    scope = {'r' : None}
    test_obj = TestClass(scope, scope.__setitem__, 'r')
    test_obj.__class__.__call__(test_obj, 'a')
    assert scope['r'] == 'a'



# Generated at 2022-06-14 06:09:21.288869
# Unit test for method __getattribute__ of class ScopeReplacer
def test_ScopeReplacer___getattribute__():
    # __getattribute__ -> _resolve -> _factory
    class DummyClass1(ScopeReplacer):
        def __init__(self, scope, factory, name):
            ScopeReplacer.__init__(self, scope, factory, name)
    # __getattribute__ -> _resolve -> _factory -> _scope
    class DummyClass2(ScopeReplacer):
        def __init__(self, scope, factory, name):
            ScopeReplacer.__init__(self, scope, factory, name)
            scope['DummyClass2'] = self
    # __getattribute__ -> _resolve -> _factory -> _scope -> getattr
    class DummyClass3(ScopeReplacer):
        def __init__(self, scope, factory, name):
            ScopeReplacer.__init__(self, scope, factory, name)

# Generated at 2022-06-14 06:09:23.944477
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    import doctest
    doctest.run_docstring_examples(IllegalUseOfScopeReplacer.__unicode__,
        globals())



# Generated at 2022-06-14 06:09:33.709457
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """__str__ should return a str object

    This is needed because the error is caught by bzrlib.trace, which
    expects a str, not a unicode object.
    """
    e = IllegalUseOfScopeReplacer('name', 'msg')
    s = str(e)
    assert isinstance(s, str)
    assert e.__str__() == s
    # Make sure that if the message is already a str, it is not converted to
    # unicode.
    e = IllegalUseOfScopeReplacer('name', 'msg', 'I am a str')
    s = str(e)
    assert isinstance(s, str)
    assert e.__str__() == s

