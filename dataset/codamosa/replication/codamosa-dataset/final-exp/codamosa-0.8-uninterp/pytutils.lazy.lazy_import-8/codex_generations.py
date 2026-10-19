

# Generated at 2022-06-14 05:59:52.800067
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    import bzrlib.tests.test_lazy_import
    reload(bzrlib.tests.test_lazy_import)
    return bzrlib.tests.test_lazy_import.test_ScopeReplacer___call__()


# Generated at 2022-06-14 06:00:02.965221
# Unit test for method __eq__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___eq__():
    """__eq__ should return true when compare equal objects."""
    e1 = IllegalUseOfScopeReplacer(None, 'msg')
    e1.name = 'name'
    e2 = IllegalUseOfScopeReplacer(None, 'msg')
    e2.name = 'name'
    e3 = IllegalUseOfScopeReplacer(None, 'msg2')
    e3.name = 'name'
    e4 = IllegalUseOfScopeReplacer(None, 'msg')
    e4.name = 'name2'
    assert e1 == e2
    assert not e1 == e3
    assert not e1 == e4
test_IllegalUseOfScopeReplacer___eq__._default_test = True


# Generated at 2022-06-14 06:00:14.146025
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    from bzrlib.tests import TestCase
    from bzrlib.lazy_import import ScopeReplacer
    import sys
    import __builtin__
    class Foo: pass
    class TestScopeReplacer(TestCase):
        def setUp(self):
            TestCase.setUp(self)
            self.old_modules = dict(sys.modules)
            self.old_builtins = dict(__builtin__.__dict__)
            self.scope = {}
            self.replacer = ScopeReplacer(self.scope, self._factory, 'foo')
        def _factory(self, replacer, scope, name):
            return Foo()
        def test_instance_attribute(self):
            self.assertEqual(None, self.replacer.bar)
            self.replacer.bar = 10
            self

# Generated at 2022-06-14 06:00:21.405909
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    from bzrlib.lazy_import import IllegalUseOfScopeReplacer

    exc = IllegalUseOfScopeReplacer('scope_replacer_obj',
                                    'msg',
                                    'extra')
    # unicode() just calls __unicode__()
    s = unicode(exc)
    assert isinstance(s, unicode)
# /Unit test for method __unicode__ of class IllegalUseOfScopeReplacer


# Generated at 2022-06-14 06:00:27.849105
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """IllegalUseOfScopeReplacer.__unicode__() should leave unicode objects
    untouched.
    """
    e = IllegalUseOfScopeReplacer(u'Illegal use of "s"',
        u'This is a unicode object')
    s = unicode(e)
    assert isinstance(s, unicode), "__unicode__ returns a non-unicode object"



# Generated at 2022-06-14 06:00:40.642946
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    # This function tests method __setattr__ of class ScopeReplacer.
    # It is used by selftest.
    from bzrlib.tests.lazy_import_helper import FakeScope
    
    
    # Callable that generates a new object to replace the placeholder
    def create_real_object(self, scope, name):
        scope[name] = 'real_object'
        return scope[name]
    
    
    scope = FakeScope()
    scope['foo'] = 'placeholder'
    scope['foo']._factory = create_real_object
    scope['foo']._name = 'foo'
    scope['foo']._should_proxy = True
    scope['foo']._real_obj = None
    assert scope['foo'] == 'real_object'

# Generated at 2022-06-14 06:00:48.445218
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """Unit test for IllegalUseOfScopeReplacer"""
    from bzrlib.lazy_import import lazy_import
    lazy_import(globals(), """
    from bzrlib import (
        trace,
        )
    """)
    try:
        raise IllegalUseOfScopeReplacer('name', 'foo', 'bar')
    except IllegalUseOfScopeReplacer as e:
        trace.mutter(str(e))



# Generated at 2022-06-14 06:00:54.014995
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    import bzrlib.transform
    global bzrlib
    scope = {'bzrlib':bzrlib}
    scope['bzrlib.transform'] = ScopeReplacer(scope,
        lambda self, scope, name: scope[name], 'bzrlib.transform')
    scope['bzrlib.transform'].__call__()



# Generated at 2022-06-14 06:01:00.422016
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    from bzrlib import lazy_import
    a = {'foo': 'bar'}
    lazy_import.lazy_import(a, '_x = "y"')
    assert a._x == 'y'
    lazy_import.lazy_import(a, '_x2 = _x')
    assert a._x2 == 'y'



# Generated at 2022-06-14 06:01:04.665473
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    e = IllegalUseOfScopeReplacer('foo', 'bar', 'extra')
    expected = "IllegalUseOfScopeReplacer object 'foo' was used incorrectly:" \
               " bar: extra"
    assert str(e) == expected

# Generated at 2022-06-14 06:01:19.732624
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """This test checks that IllegalUseOfScopeReplacer.__unicode__() works.

    It also tests that IllegalUseOfScopeReplacer.__str__() works, because
    __unicode__() calls __str__().
    """
    o = IllegalUseOfScopeReplacer('o', 'msg', extra='extra')
    # We do not use assertRaises because it would eat the exception's
    # __unicode__() result.
    e = None
    try:
        unicode(o)
    except UnicodeDecodeError as e:
        pass
    if e is not None:
        raise AssertionError('Failed to decode unicode %r' % (unicode(o),))



# Generated at 2022-06-14 06:01:32.322294
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """__str__ of IllegalUseOfScopeReplacer"""
    # IllegalUseOfScopeReplacer is not supposed to be actually used, just
    # it's subclasses. This test is written in such a way that it will test
    # both the IllegalUseOfScopeReplacer and it's subclasses.
    e = IllegalUseOfScopeReplacer("foo", "msg", "extra")
    e_str = str(e)
    e_str = e_str.replace("u'", "'")
    # The above line is to make the test run under python 2.6 as well, as
    # python 2.6 puts u' in front of the strings. As IllegalUseOfScopeReplacer
    # should never be instantiated, this shouldn't cause any problems.


# Generated at 2022-06-14 06:01:33.868941
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    import doctest
    doctest.testmod()



# Generated at 2022-06-14 06:01:40.960233
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """Unit test for method __str__ of class IllegalUseOfScopeReplacer

    The method __str__ of class IllegalUseOfScopeReplacer must return a str.
    """
    e = IllegalUseOfScopeReplacer('module', 'message')
    msg = str(e)
    umsg = unicode(e)
    assert isinstance(msg, str), "%r is not an instance of str" % (msg,)
    assert msg.startswith('module was used incorrectly:'), \
        "Unexpected start of message %r" % (msg,)
    assert umsg.startswith(u'module was used incorrectly:'), \
        "Unexpected start of message %r" % (umsg,)


# Generated at 2022-06-14 06:01:52.734592
# Unit test for method __getattribute__ of class ScopeReplacer
def test_ScopeReplacer___getattribute__():
    class DummyClass(object):
        for attr in (name for name in ScopeReplacer.__slots__
                     if not name.startswith("_")):
            locals()[attr] = None
    # Add an extra attribute to check that it won't be returned
    DummyClass.extra = "extra"
    # Values for each attribute
    x = object() # _real_obj, should not be accessed at all
    y = object() # _scope
    z = object() # _factory
    a = object() # _name
    # Construct the instance
    dummy_object = DummyClass()
    # Add the instance to locals
    locals()["dummy_object"] = dummy_object
    # Set attribute values
    dummy_object._real_obj = x
    dummy_object._scope = y
    dummy_object._f

# Generated at 2022-06-14 06:02:02.887529
# Unit test for method __eq__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___eq__():
    """__eq__ should behave according to contract"""
    # check equal case, with and without extra info
    e = IllegalUseOfScopeReplacer('name', 'msg', 'extra')
    e2 = IllegalUseOfScopeReplacer('name', 'msg', 'extra')
    e3 = IllegalUseOfScopeReplacer('name', 'msg')
    assert e == e2 == e3
    # check unequal case, with and without extra info
    e4 = IllegalUseOfScopeReplacer('name4', 'msg', 'extra')
    e5 = IllegalUseOfScopeReplacer('name', 'msg2', 'extra')
    e6 = IllegalUseOfScopeReplacer('name', 'msg', 'extra2')
    assert e != e4 != e5 != e6
    # check based on class
    e7 = ValueError()
    assert e != e7

# Generated at 2022-06-14 06:02:10.310374
# Unit test for method __eq__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___eq__():
    r1 = IllegalUseOfScopeReplacer('name', 'msg', 'extra')
    r2 = IllegalUseOfScopeReplacer('name', 'msg', 'extra')
    r3 = IllegalUseOfScopeReplacer('name', 'msg', 'extra3')
    r4 = IllegalUseOfScopeReplacer('name', 'msg4', 'extra')
    r5 = IllegalUseOfScopeReplacer('name5', 'msg', 'extra')
    assert r1 == r2
    assert not r1 == r3
    assert not r1 == r4
    assert not r1 == r5
    # None isn't a valid error object
    assert r1 != None
    # OtherError is a valid error, but with no relation to
    # IllegalUseOfScopeReplacer
    assert r1 != Error()


# Generated at 2022-06-14 06:02:22.195869
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    from bzrlib import (
        lazy_import,
        tests,
        )
    lazy_import(globals(), """
import bzrlib.hsi
from bzrlib.tests import TestCase
""")

    class TestScopeReplacerCall(TestCase):

        def test_call(self):

            class Foo(object):

                def __init__(self, name):
                    self.name = name

                def __call__(self, *args, **kwargs):
                    return self.name, args, kwargs

            foo = Foo('bar')
            replacer = ScopeReplacer(globals(), lambda x,y,z: foo, 'foo')
            self.assertEqual(('bar', (1, 2), {'a': 3}), foo(1, 2, a=3))

# Generated at 2022-06-14 06:02:28.301491
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """IllegalUseOfScopeReplacer.__str__ returns the result of _format()
    as a string, which is the complete message.
    """
    e = IllegalUseOfScopeReplacer("name", "msg", "extra")
    assert str(e) == "ScopeReplacer object 'name' was used incorrectly:" \
                     " msg: extra"



# Generated at 2022-06-14 06:02:38.847260
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    from bzrlib.tests import TestCase
    from bzrlib.lazy_import import ScopeReplacer

    class Foo(object):
        _f = ''
        def __init__(self, value):
            self._f = value

    class Test(TestCase):
        def test_setattr(self):
            foo = Foo('')
            replacer = ScopeReplacer(None, Foo, 'foo')
            # This should do nothing as _should_proxy should be true.
            replacer.f = 'value'
            self.assertEqual('', foo._f)
            ScopeReplacer._should_proxy = False
            # Check that behaviour is correct when proxying is disabled.
            replacer.f = 'newvalue'

# Generated at 2022-06-14 06:02:47.244513
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    from bzrlib import (
        errors,
        osutils,
        branch,
        )


# Generated at 2022-06-14 06:02:54.074486
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """IllegalUseOfScopeReplacer.__unicode__() should raise an exception"""
    try:
        raise IllegalUseOfScopeReplacer(
            'name', 'msg', 'extra')
    except IllegalUseOfScopeReplacer as e:
        unicode(e)
    try:
        raise IllegalUseOfScopeReplacer(
            u'nam\xc3\xa9', 'msg', 'extra')
    except IllegalUseOfScopeReplacer as e:
        unicode(e)

# Generated at 2022-06-14 06:02:58.309092
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """__str__ should not raise an exception"""
    exc = IllegalUseOfScopeReplacer('name', 'msg', ValueError('extra'))
    # str must return bytes
    str(exc)

# Generated at 2022-06-14 06:03:07.244625
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    r"""test for method __setattr__ of class ScopeReplacer

        This test checks that assigning a value to an attribute of
        a ScopeReplacer instance behaves like assigning the same
        attribute to the ScopeReplacer's real object.
        """
    scope = locals()
    def factory(self, scope, name):
        return 'real object'
    scope['R'] = ScopeReplacer(scope, factory, 'R')
    scope['R'].attr = 'value'
    return scope['R'].attr == 'value'


# Generated at 2022-06-14 06:03:18.208856
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    from bzrlib.lazy_import import lazy_import
    scope = {'__name__': 'test_ScopeReplacer___setattr__'}
    def _factory(obj, scope, name):
        return scope[name]
    lazy_import(scope, 'from example import testmodule', _factory)
    if 'testmodule' in scope:
        raise ValueError('testmodule')
    scope['testmodule'] = 'testmodule'
    x = scope['testmodule']
    if x != 'testmodule':
        raise ValueError('%r != testmodule' % (x,))
    del scope['testmodule']
    try:
        scope['testmodule']
        raise ValueError('Unable to delete scope member')
    except KeyError:
        pass
# End of unit test for method __setattr__ of class ScopeRepl

# Generated at 2022-06-14 06:03:26.440296
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    from bzrlib import lazy_import
    lazy_import.lazy_import(globals(), '''
    from bzrlib import (
        errors,
        osutils,
        branch,
        )
    ''')
    # the lazy replacements should be callable

# Generated at 2022-06-14 06:03:37.464837
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """The __unicode__ method converts the instance attributes to a unicode
    string for debugging."""
    obj = IllegalUseOfScopeReplacer("a name", "a message", 'more info')
    expected = u"ScopeReplacer object 'a name' was used incorrectly: " \
               u"a message: more info"
    result = obj.__str__()
    # The test is not strict: we allow more space before the colon after
    # 'a message'
    assert result.find(expected) != -1, \
        "Expected %r, received %r" % (expected, result)


# Generated at 2022-06-14 06:03:42.517688
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    try:
        raise IllegalUseOfScopeReplacer('name', 'msg', 'extra')
    except IllegalUseOfScopeReplacer as e:
        assert 'name' in str(e)
        assert 'msg' in str(e)
        assert 'extra' in str(e)


# Generated at 2022-06-14 06:03:51.926036
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    __tracebackhide__ = True
    try:
        __ = ScopeReplacer(locals(), lambda x: x, '__')()(1,2,3)
    except IllegalUseOfScopeReplacer as e:
        # Test that exception is raised.
        assert 'bzrlib/tests/blackbox/test_lazy_import.py' in str(e)
        assert 'test_ScopeReplacer___call__' in str(e)
        assert 'ScopeReplacer object __ was used incorrectly: Object already replaced, did you assign it to another variable?' in str(e)
        # Ensure that we have got the line number where the exception was
        # raised
        assert ':133: ' in str(e)
        return
    else:
        raise AssertionError("IllegalUseOfScopeReplacer was not raised")

# Generated at 2022-06-14 06:04:03.199502
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    # This code raises an exception to indicate that the
    # tests failed. You may want to comment out that code if you want
    # to see the traceback.
    sr = ScopeReplacer
    assert False, "Unimplemented"

    # This code raises an exception to indicate that the
    # tests failed. You may want to comment out that code if you want
    # to see the traceback.
    assert False, "Unimplemented"

    # This code raises an exception to indicate that the
    # tests failed. You may want to comment out that code if you want
    # to see the traceback.
    assert False, "Unimplemented"

    # This code raises an exception to indicate that the
    # tests failed. You may want to comment out that code if you want
    # to see the traceback.

# Generated at 2022-06-14 06:04:14.907779
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """IllegalUseOfScopeReplacer.__unicode__() must return unicode()"""
    import traceback

# Generated at 2022-06-14 06:04:21.111753
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """__str__ must return a str object"""
    try:
        raise IllegalUseOfScopeReplacer('x', 'y')
    except IllegalUseOfScopeReplacer as e:
        s = str(e)
        # is s a str ?
        try:
            unicode(s)
        except UnicodeError:
            # s is a str, that's what we want
            return
        raise AssertionError('%s.__str__ must return a str object' %
                             e.__class__.__name__)



# Generated at 2022-06-14 06:04:26.936778
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():

    class TestScopeReplacer(ScopeReplacer):

        def __init__(self):
            self._resolve = lambda: 'Spam'
    obj = TestScopeReplacer()
    expected = 'Spam'
    actual = obj()
    assert(expected == actual)

# Generated at 2022-06-14 06:04:33.894439
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    def __init__(self, x):
        self.x = x
    globals()['MyClass'] = __init__
    globals()['foo'] = foo = ScopeReplacer(globals(), MyClass, 'foo')
    myobj = foo(x=12)
    assert myobj.x == 12
    assert myobj == foo
    assert foo is not None
    del globals()['foo']
    del globals()['MyClass']

# Generated at 2022-06-14 06:04:47.520857
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """IllegalUseOfScopeReplacer_unicode_

    This is a test for method __unicode__ of class IllegalUseOfScopeReplacer.
    """
    t1 = IllegalUseOfScopeReplacer(1, 2, 3)
    t2 = unicode(t1)
    t3 = str(t1)
    # XXX: The following two tests should pass but don't yet,
    #      because of the switch to the __str__ method in
    #      python 2.6 and 2.7.
    # t4 = t2 == u'IllegalUseOfScopeReplacer(1, 2, 3)'
    # t5 = t3 == 'IllegalUseOfScopeReplacer(1, 2, 3)'

# Generated at 2022-06-14 06:04:55.058582
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    import bzrlib.tests.test_lazy_import

    def _test_ScopeReplacer___setattr__():
        scope = {}
        name = 'test_object'

        # Create object and create real object.
        replacer = ScopeReplacer(scope, lambda self, scope, name: scope[name], name)
        scope[name] = "real"

        # Check the real object can be retrieved.
        replacer.other = 27
        try:
            if replacer.other != 27:
                bzrlib.tests.test_lazy_import.fail_func()
        except Exception:
            bzrlib.tests.test_lazy_import.fail_func()
        if scope[name].other != 27:
            bzrlib.tests.test_lazy_import.fail_func()
    _

# Generated at 2022-06-14 06:05:07.986685
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """Test the __str__ method of class IllegalUseOfScopeReplacer."""
    # Test exception with simple format string
    e = IllegalUseOfScopeReplacer('scope', 'msg', 'extra')
    got = str(e)
    expected = "ScopeReplacer object 'scope' was used incorrectly: msg: extra"
    assert got == expected, ('''got %r; expected %r''' % (got, expected))
    # Specify exception format in _fmt attribute directly
    e = IllegalUseOfScopeReplacer('scope', 'msg', 'extra')
    e._fmt = "Format string: %(name)s"
    got = str(e)
    expected = "Format string: scope"
    assert got == expected, ('''got %r; expected %r''' % (got, expected))
    # Test exception with a pre

# Generated at 2022-06-14 06:05:13.580586
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    import bzrlib.tests
    scope = bzrlib.tests.TestCase.__dict__
    brc = ScopeReplacer(scope,
                        lambda self, scope, name: scope[name],
                        'bzrlib')
    brc()



# Generated at 2022-06-14 06:05:20.207827
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    import bzrlib.tests
    bzrlib.tests.blackbox.ScopeReplacer___call__()

    def _test(self, scope, name):
        return name
    class _scope: pass
    s = _scope()
    r = ScopeReplacer(s, _test, 'foo')
    return r('bar', baz='bam') == 'foo'



# Generated at 2022-06-14 06:05:28.393378
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """__str__ of IllegalUseOfScopeReplacer"""
    import doctest
    doctest.ELLIPSIS
    doctest.NORMALIZE_WHITESPACE
    doctest.REPORT_NDIFF
    doctest.REPORT_ONLY_FIRST_FAILURE
    doctest.REPORT_UNABLE_TO_COMPARE
    doctest.REPORT_CDIFF
    doctest.REPORT_UDIFF
    doctest.REPORT_NDIFF
    doctest.REPORT_ONLY_FIRST_FAILURE
    doctest.REPORT_UNABLE_TO_COMPARE
    doctest.REPORT_CDIFF
    doctest.REPORT_UDIFF
    doctest.REPORT_NDIFF
    doctest.REPORT_ONLY_FIRST_FAILURE
    doctest

# Generated at 2022-06-14 06:05:44.923092
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """Method __unicode__ of class IllegalUseOfScopeReplacer must return unicode"""
    # illegal use of scope replacer (note the extra field)
    x = IllegalUseOfScopeReplacer('name', 'msg', extra='extra')
    # unicode object
    u = unicode(x)
    # unicode class
    s = type(u)
    # check that __unicode__() returns a unicode object
    assert isinstance(u, s), 'IllegalUseOfScopeReplacer.__unicode__() must return unicode object'
test_IllegalUseOfScopeReplacer___unicode__.error_level = 2


# Generated at 2022-06-14 06:05:56.988541
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    from bzrlib.lazy_import import lazy_import
    from bzrlib.tests import TestCase

    class Dummy:
        pass

    class TestScopeReplacer(TestCase):

        def test___setattr__(self):
            # Tests that a ScopeReplacer can be used in the place of a module.
            ScopeReplacer._should_proxy = False
            # The most common way to use ScopeReplacer is through the lazy_import
            # decorator.
            global_scope = globals()
            lazy_import(globals(), '''
            from bzrlib import tests
            ''')
            # Make a dummy module where tests.py will be replaced by.
            dummy = Dummy()
            dummy.test_foo = 42
            # replace tests with the dummy module
            global_scope['tests'] = dummy


# Generated at 2022-06-14 06:06:06.092744
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """__str__ of IllegalUseOfScopeReplacer"""
    # FIXME: Many many tests need to be written for this class.
    # (IanClatworthy)
    e = IllegalUseOfScopeReplacer('name', 'msg', 'extra')
    u = str(e)
    expected = "ScopeReplacer object 'name' was used incorrectly:" \
        " msg: extra"
    if u != expected:
        raise AssertionError('%s != %s' % (u, expected))



# Generated at 2022-06-14 06:06:12.755002
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """IllegalUseOfScopeReplacer.__str__ should output message"""
    e = IllegalUseOfScopeReplacer(
        'foo', 'hello world')
    s = str(e)
    assert s == 'ScopeReplacer object \'foo\' was used incorrectly: '\
        'hello world'


# Generated at 2022-06-14 06:06:21.392258
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    # __call__() (line 337)
    import bzrlib.lazy_import

    def _factory(obj, scope, name):
        def my_func(x):
            return x + x
        return my_func


    scope = {'ScopeReplacer':bzrlib.lazy_import.ScopeReplacer}
    ScopeReplacer = scope['ScopeReplacer']

    # call the method (line 339)
    scope['t'] = ScopeReplacer(scope, _factory, 't')
    t = scope['t']
    res = t(2)
    # line 340
    if res != 4: raise AssertionError
    return # exit function


# Generated at 2022-06-14 06:06:29.273175
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """Test method __unicode__ of class IllegalUseOfScopeReplacer"""

    e = IllegalUseOfScopeReplacer('foo', 'bar', 'baz')
    expected = 'ScopeReplacer object \'foo\' was used incorrectly: bar: baz'
    try:
        obtained = unicode(e)
    except UnicodeError:
        # This may fail, if e does not have a _unicode_ message
        obtained = str(e)
        expected = expected.encode('utf-8')
    assert obtained == expected, "%s != %s" % (obtained, expected)

# Generated at 2022-06-14 06:06:33.044691
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    import doctest
    return doctest.DocTestSuite(IllegalUseOfScopeReplacer)

__all__ = ['IllegalUseOfScopeReplacer', 'lazy_import']



# Generated at 2022-06-14 06:06:43.243103
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    e = IllegalUseOfScopeReplacer(name='foo', msg='something happened')
    u = unicode(e)
    # Unicode objects are always encoded using the default encoding.
    if not isinstance(u, unicode):
        raise AssertionError("Expected '%s' to be unicode" % u)

    # Non unicode objects are encoded using the default encoding.
    if not isinstance(u, unicode):
        raise AssertionError("Expected '%s' to be unicode" % u)

# Generated at 2022-06-14 06:06:48.942219
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__ of IllegalUseOfScopeReplacer should produce unicode"""
    # __unicode__ must return a unicode object.
    e = IllegalUseOfScopeReplacer('name', 'msg')
    assert isinstance(unicode(e), unicode)


# Generated at 2022-06-14 06:07:02.708749
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    import bzrlib.trace
    from bzrlib.tests import TestCase
    from bzrlib.tests import TestSkipped
    from bzrlib.trace import mutter

    try:
        bzrlib.trace.set_verbosity(1)
    except TestSkipped:
        raise TestSkipped('This test needs the test framework to be built with'
                          ' the VERBOSE configuration option.')

    # bzrlib.trace.set_verbosity(1)
    class MyScopeReplacer(ScopeReplacer):
        """A proxy that allows to set a member.
        """

        def __init__(self, scope, factory, name):
            super(MyScopeReplacer, self).__init__(scope, factory, name)
            object.__setattr__(self, '_something', None)

# Generated at 2022-06-14 06:07:19.572057
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    from bzrlib.tests import TestCaseWithTransport
    from bzrlib.lazy_import import lazy_import, ScopeReplacer
    import os
    import bzrlib
    class TestScopeReplacerMethods(TestCaseWithTransport):
        class SampleClass(object):
            pass
        def test_ScopeReplacer___setattr__(self):
            scope = {}
            def factory(self, scope, name):
                return TestScopeReplacerMethods.SampleClass()
            name = 'test'
            scope_replacer = ScopeReplacer(scope, factory, name)
            scope_replacer.test_attr = 'test_attr'
            self.assertEqual(bzrlib.SampleClass().test_attr, 'test_attr')

    test_ScopeReplacer___setattr__ = TestScopeReplacerMethods().test_

# Generated at 2022-06-14 06:07:23.483856
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__() must return a unicode object."""
    e = IllegalUseOfScopeReplacer('foo', 'bar')
    u = unicode(e)
    assert isinstance(u, unicode), "__unicode__() should return unicode"


# Generated at 2022-06-14 06:07:32.526414
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    import bzrlib.lazy_import as _mod_lazy_import
    self = _mod_lazy_import.ScopeReplacer.__new__(_mod_lazy_import.ScopeReplacer)
    self._scope = {'foo': 'already replaced'}
    self._factory = None
    self._name = 'foo'
    self._real_obj = 'already replaced'
    try:
        object.__setattr__(self, 'unknown attribute', 1)
    except Exception as e:
        if isinstance(e, AttributeError) and str(e) == "'ScopeReplacer' object has no attribute 'unknown attribute'":
            pass
        else:
            raise
    t = _mod_lazy_import.ScopeReplacer.__new__(_mod_lazy_import.ScopeReplacer)
   

# Generated at 2022-06-14 06:07:39.557485
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    class SomeClass(object):
        def __init__(self, n):
            self.n = n
        def do_something(self, m):
            return m + self.n
    some_obj = SomeClass(42)
    scopereplacer = ScopeReplacer(None, None, None)
    scopereplacer._real_obj = some_obj
    test_data = (
        ( (1,), 43),
        ( (17,), 59),
    )
    for args, expected_result in test_data:
        result = scopereplacer(*args)
        assert result == expected_result, "for %s, expected %s, got %s" % (
            args, expected_result, result)

# Generated at 2022-06-14 06:07:51.242083
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    """Check that ScopeReplacer doesn't leak memory when attributes are set on
    it.
    """
    def _factory(self, scope, name):
        scope[name] = 'something'
        return scope[name]
    scope = {}
    name = 'object'
    r = ScopeReplacer(scope, _factory, name)
    # Set attributes on the replacer, should not result in memory leaks due
    # to the use of setattr
    for i in range(10000):
        setattr(r, 'attribute_%d' % i, 'value_%d' % i)
    # Use the replacer, should not result in memory leaks due to the use of
    # getattr
    for i in range(10000):
        getattr(r, 'attribute_%d' % i)
    # Check that the object it created

# Generated at 2022-06-14 06:08:05.558761
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    class FakeModule(object):
        """Fake module object."""

        def __call__(self, *args, **kwargs):
            return (args, kwargs)

    scope = {'fake_module': 'old value'}
    factory = lambda placeholder, scope, name: 'new value'
    placeholder = ScopeReplacer(scope=scope, factory=factory, name='fake_module')
    # Call the object that is a placeholder
    result = placeholder()
    # Value should not be replaced yet
    eq((), result)
    # Decorator should not replace values, but accept the calls
    eq('new value', scope['fake_module'])

    # Now test with a real module (see if __call__ is called correctly)
    scope = {'fake_module': 'old value'}

# Generated at 2022-06-14 06:08:15.209317
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    msg = IllegalUseOfScopeReplacer('test', 'msg', 'extra info')
    msg.__class__.__unicode__ = msg.__class__.__str__
    # Test that the str value is returned as it should be.
    u = unicode(msg)
    assert isinstance(u, unicode), "__unicode__ should return a unicode."
    u = str(msg)
    assert isinstance(u, str), "__str__ should return a str."
    # Test that a message string can be provided to __unicode__.
    u = unicode(msg, 'utf-8')
    assert isinstance(u, unicode), "__unicode__ should return a unicode."



# Generated at 2022-06-14 06:08:19.664858
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """IllegalUseOfScopeReplacer.__str__ works"""
    e = IllegalUseOfScopeReplacer('name', 'msg', 'extra')
    str(e) # test __str__
    unicode(e) # test __unicode__



# Generated at 2022-06-14 06:08:30.316105
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    """__call__() should call object once it has been created"""


    # Scoped replacers can be called like a function, so we need to make a dummy
    # one to be able to call its _resolve() method.
    class _Dummy:
        def _resolve(self):
            return 10
    dr = _Dummy()

    # Create a scope with a replacer
    scope = {}
    class _DummyFactory:
        def __call__(self, obj, scope, name):
            # Return a new value for the scope
            return 11
    replacer = ScopeReplacer(scope, _DummyFactory(), 'dummy')
    replacer._resolve = dr._resolve

    # Check that the replacer is called as a function like the real object
    # would be.
    assert replacer() == 10



# Generated at 2022-06-14 06:08:42.434511
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    from bzrlib.tests import TestCase
    from bzrlib.lazy_import import lazy_import, ScopeReplacer
    lazy_import(locals(), '''
    from bzrlib.lazy_import import ScopeReplacer
    ''')
    # test that __call__ works on plain old functions
    def func(x):
        return x + 1
    class Test__call__(TestCase):
        def test__call__(self):
            self.assertEqual(1, ScopeReplacer(locals(),
                lambda replacer,scope,name:func, 'func')(0))
    # test that __call__ works on object methods
    class Object(object):
        def method(self, value):
            return value - 1

# Generated at 2022-06-14 06:09:05.151358
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """IllegalUseOfScopeReplacer.__unicode__()"""
    s = IllegalUseOfScopeReplacer('name', 'msg', 'extra')
    u = unicode(s)
    assert isinstance(u, unicode)
    assert u == u'ScopeReplacer object \'name\' was used incorrectly: msg: extra'



# Generated at 2022-06-14 06:09:07.661489
# Unit test for method __getattribute__ of class ScopeReplacer
def test_ScopeReplacer___getattribute__():
    """Test method ScopeReplacer.__getattribute__
    """
    import doctest
    d = {}

# Generated at 2022-06-14 06:09:20.324591
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    # This test is only for the method __unicode__ of
    # IllegalUseOfScopeReplacer, which has a wacky definition.  See
    # comments in that method.
    from bzrlib.i18n import gettext
    def my_gettext(unicode_string):
        s = str(unicode_string)
        if s == u"A warning: %(msg)s":
            return s
        if s == u"IllegalUseOfScopeReplacer object %(name)r was used incorrectly: %(msg)s%(extra)s":
            return s
        raise AssertionError("%r isn't a valid _fmt" % s)
    to_delete = []

# Generated at 2022-06-14 06:09:31.102977
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """This test checks method __str__ of class IllegalUseOfScopeReplacer"""
    from cStringIO import StringIO
    import sys
    old_stdout = sys.stdout