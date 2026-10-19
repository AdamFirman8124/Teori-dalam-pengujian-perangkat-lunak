

# Generated at 2022-06-14 06:00:08.201587
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """IllegalUseOfScopeReplacer.__unicode__() -> unicode

    IllegalUseOfScopeReplacer unicode should be the same as str
    """
    e = IllegalUseOfScopeReplacer('foo', 'bar')
    u = unicode(e)
    s = str(e)
    assert type(u) is unicode
    assert type(s) is str
    assert u == s



# Generated at 2022-06-14 06:00:09.213943
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    pass

# Generated at 2022-06-14 06:00:22.069781
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    # test IllegalUseOfScopeReplacer._format()
    from bzrlib.lazy_import import IllegalUseOfScopeReplacer

    # String format exception.
    e = IllegalUseOfScopeReplacer('name', 'msg')
    u = e._format() # raises exception
    # Unicode format exception.
    e = IllegalUseOfScopeReplacer(u'name', 'msg')
    u = e._format() # raises exception
    # Bad format string.
    e = IllegalUseOfScopeReplacer('name', 'msg')
    e._fmt = ''
    u = e._format() # raises exception
    # Good format string.
    e = IllegalUseOfScopeReplacer('name', 'msg')
    e._fmt = 'name: %(name)s'
    u = e._format()
    # Preformatted string.


# Generated at 2022-06-14 06:00:29.058129
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """__str__ should return str object."""
    x = IllegalUseOfScopeReplacer('foo', 'bar')
    # __str__ should return str object
    result = str(x)
    expected = "foo was used incorrectly: bar"
    assert result == expected
test_IllegalUseOfScopeReplacer___str__.todo = None



# Generated at 2022-06-14 06:00:34.256971
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """Method __str__ of class IllegalUseOfScopeReplacer must return
    a str.
    """
    e = IllegalUseOfScopeReplacer('bugzilla', 'unimplemented yet',
                                  extra='commit message')
    assert isinstance(str(e), str)



# Generated at 2022-06-14 06:00:41.062237
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    from bzrlib.i18n import gettext
    e = IllegalUseOfScopeReplacer("foo", "bar")
    eq = gettext("ScopeReplacer object %(name)r was used incorrectly:"
                 " %(msg)s%(extra)s")
    eq = eq % dict(name="foo", msg="bar", extra="")
    u = unicode(e)
    assert u == eq
    # check that __str__ works too
    assert str(e) == eq



# Generated at 2022-06-14 06:00:53.709521
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """IlllegalUseOfScopeReplacer.__unicode__"""
    exc = IllegalUseOfScopeReplacer("name", "msg", extra=None)
    assert isinstance(exc.__unicode__(), unicode) # py2.5: no unicode
    assert exc.__unicode__() == "ScopeReplacer object 'name' was used incorrectly: msg"
    exc.extra = "more"
    assert isinstance(exc.__unicode__(), unicode) # py2.5: no unicode
    assert exc.__unicode__() == "ScopeReplacer object 'name' was used incorrectly: msg: more"
    exc._preformatted_string = "a non-string"
    assert not isinstance(exc.__unicode__(), str) # py2.5: no unicode

# Generated at 2022-06-14 06:00:59.884502
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    # test_ScopeReplacer___setattr__()
    
    
    
    class ScopeReplacerSubclass(ScopeReplacer):
    
        def __init__(self):
            self.foo = None
    
    obj = ScopeReplacerSubclass()
    obj.foo = 'bar'
    assert obj.foo == 'bar'



# Generated at 2022-06-14 06:01:05.407928
# Unit test for method __setattr__ of class ScopeReplacer

# Generated at 2022-06-14 06:01:08.958729
# Unit test for method __getattribute__ of class ScopeReplacer
def test_ScopeReplacer___getattribute__():
    # Method __getattribute__ of class ScopeReplacer

    # TODO: write a unit test for method __getattribute__ of class ScopeReplacer
    pass

# Generated at 2022-06-14 06:01:35.432607
# Unit test for method __getattribute__ of class ScopeReplacer
def test_ScopeReplacer___getattribute__():
    from bzrlib.tests import TestCase
    class Test_ScopeReplacer(TestCase):
        def test_ScopeReplacer(self):
            from bzrlib.lazy_import import IllegalUseOfScopeReplacer
            from bzrlib.lazy_import import ScopeReplacer
            class ExpectedException(Exception):
                pass
            class Testee:
                def __init__(self, name):
                    self.name = name
                def _resolve(self):
                    return self
                def __getattribute__(self, attr):
                    if attr == '_resolve':
                        raise ExpectedException()
                    else:
                        return getattr(self, attr)
            testee = Testee('testee')

# Generated at 2022-06-14 06:01:39.472004
# Unit test for method __getattribute__ of class ScopeReplacer
def test_ScopeReplacer___getattribute__():
    """Unit test for method __getattribute__ of class ScopeReplacer"""
    import sys
    # import modules required
    import bzrlib
    import bzrlib.lazy_import
    # initialize the test suite
    import TestSuite
    suite = TestSuite.TestSuite()
    # TODO: add tests
    # return the test suite
    return suite

# Generated at 2022-06-14 06:01:51.600963
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """Test the __str__ method of IllegalUseOfScopeReplacer.

    This is a little involved because the implementation of __str__ uses the
    _get_format_string method, which will return __fmt, which is supposed to
    be an ascii string.
    """
    import bzrlib.i18n
    bzrlib.i18n.set_output_encoding('ascii')
    # This is a little like a unit test for i18n, because it ensures that the
    # default encoding is actually ascii, and that strings in __fmt can
    # actually be encoded.
    # This should raise an adoption error because the IllegalUseOfScopeReplacer
    # class is not subclassed.
    e = IllegalUseOfScopeReplacer('name', 'msg', 'extra')
    # Since the _fmt class

# Generated at 2022-06-14 06:01:52.895809
# Unit test for method __getattribute__ of class ScopeReplacer
def test_ScopeReplacer___getattribute__():
    """Test method __getattribute__ of class ScopeReplacer"""
    global scope_replacer_test_object
    scope_replacer_test_object = ScopeReplacer_test_object(1, 2, 3)

# Generated at 2022-06-14 06:01:58.478347
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    """__setattr__ should pass the attribute to the real object"""
    class TestClass(object):
        def __init__(self):
            self.x = 'hi'
    t = TestClass()
    s = ScopeReplacer(None, lambda o,s,n:t, 'x')
    s.x = 'ho'
    assert t.x == 'ho'


# Generated at 2022-06-14 06:02:03.292667
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    """Create test cases for the method ScopeReplacer.__setattr__.

    Yields tuples of (method, inputs, expected_result)
    """
    # TODO: Create tests
    # yield ('ScopeReplacer.__setattr__', ('attr', 'value'), '')
    raise tests.TestNotApplicable('method __setattr__ of class ScopeReplacer is not implemented')



# Generated at 2022-06-14 06:02:16.121337
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    import sys
    import sys
    import tempfile

    # This tests a call to a bound method - see also
    # test_lazy_import.py: test_method_calls
    test_ScopeReplacer___call__.func = lambda self: None
    globals()['test_ScopeReplacer___call__.func'] = (
        test_ScopeReplacer___call__.func)
    def test():
        globals()['test_ScopeReplacer___call__.func'] = (
            test_ScopeReplacer___call__.func)
        (test_ScopeReplacer___call__.func).not_here()
    class Tester(object):
        def test(self):
            test()
    def test_suite():
        from unittest import TestSuite, TestLoader

# Generated at 2022-06-14 06:02:27.783238
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    from bzrlib.tests.lazy_import_test import Mock
    from bzrlib.tests import TestCase
    from bzrlib._lazy_import import ScopeReplacer

    class TestScopeReplacer___call__(TestCase):

        def test_ScopeReplacer___call__(self):
            # The object must be replaced by the time it is called, because
            # functions may not be called on the lazy_import object.
            def factory(scope_replacer, scope, name):
                # The module that is being loaded.
                return [1, 2]
            scope = {}
            name = 'myobj'
            scope[name] = ScopeReplacer(scope, factory, name)
            rs = scope[name]
            self.assertEqual([1, 2], rs(6, 7))
            # Check that it's

# Generated at 2022-06-14 06:02:38.239267
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    from bzrlib.tests import TestCase
    from bzrlib.lazy_import import ScopeReplacer, IllegalUseOfScopeReplacer
    class TestObj(object):
        def __setattr__(self, attr, value):
            object.__setattr__(self, attr, value)
            if attr == 'replaced':
                raise IllegalUseOfScopeReplacer(
                    'test', msg="Object tried to replace itself")

    scope = {}
    key = 'test'
    scope[key] = TestObj()
    replacer = ScopeReplacer(scope, None, key)
    replacer.test_attr = 'success'
    TestCase().assertEqual('success', scope['test'].test_attr)



# Generated at 2022-06-14 06:02:51.387418
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    # test setting attribute on a ScopeReplacer
    # test setting attribute on a function which replaces a ScopeReplacer
    # test setting attribute on a class which replaces a ScopeReplacer
    # throw an exception if the attribute already replaced

    # test setting attribute on a ScopeReplacer
    # TODO: static methods and class methods?
    # Foo should have a public 'bar' attribute (bar is public)
    class Foo(object):
        def __init__(self):
            self.bar = 'bar'
    for name in ['obj', 'func', 'class']:
        def factory(obj, scope, name):
            return factory.obj

        factory.obj = getattr(Foo, name)
        scope = {}
        replacer = ScopeReplacer(scope, factory, name)
        replacer.bar = 'replacer.bar'

# Generated at 2022-06-14 06:03:12.196526
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """Unit test for method __str__ of class IllegalUseOfScopeReplacer.

    This method is complicated by its use of gettext.
    """
    # Test '_preformatted_string' attribute
    msg = "This is a test message"
    e = IllegalUseOfScopeReplacer(None, None, None)
    e._preformatted_string = msg
    assert str(e) == msg
    assert unicode(e) == unicode(msg)
    # Test '_format()' method
    e = IllegalUseOfScopeReplacer('my_name', 'my message', 'my extra')
    assert str(e) == 'ScopeReplacer object \'my_name\'' \
        ' was used incorrectly: my message: my extra'
    assert unicode(e) == u'ScopeReplacer object \'my_name\'' \
       

# Generated at 2022-06-14 06:03:26.010884
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    def _make_replacer():
        global replacer
        replacer = ScopeReplacer(globals(),
                                 lambda s, scope, name: object(),
                                 'replacer')
    # Test that using __setattr__ on an as-yet-unresolved placeholder fails.
    _make_replacer()
    replacer.foo = 'bar'
    # Test that using __setattr__ on a resolved placeholder fails unless
    # proxying is enabled.
    replacer._should_proxy = False
    try:
        replacer.foo = 'bar'
    except IllegalUseOfScopeReplacer:
        pass
    else:
        raise AssertionError('expected IllegalUseOfScopeReplacer')
    # Test that __setattr__ works when proxying is enabled.
    replacer._should_proxy = True

# Generated at 2022-06-14 06:03:30.748361
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    e = IllegalUseOfScopeReplacer('foo_module', 'foo thing', extra='abc')
    s = str(e)
    if isinstance(s, unicode):
        s = s.encode('utf8')
    assert s.startswith('foo_module was used incorrectly: foo thing')
    assert s.endswith(': abc')



# Generated at 2022-06-14 06:03:34.423316
# Unit test for method __getattribute__ of class ScopeReplacer
def test_ScopeReplacer___getattribute__():
    import doctest
    import bzrlib.lazy_import
    return doctest.DocTestSuite(bzrlib.lazy_import)



# Generated at 2022-06-14 06:03:39.013260
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    obj = ScopeReplacer.__new__(ScopeReplacer)
    try:
        ScopeReplacer.__init__(obj, TypeError, "", "")
    except TypeError: pass
    try:
        obj("")
    except TypeError: pass

# Generated at 2022-06-14 06:03:49.038028
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    replacer = ScopeReplacer({}, lambda x,y,z:y[z], "")
    assert replacer(1,2,3) == (1,2,3)

    class Foo(object):
        def __call__(self, a,b):
            return (a,b)
    foo = Foo()
    replacer = ScopeReplacer({}, lambda x,y,z:y[z], "")
    assert replacer(1,2) == (1,2)
    replacer._real_obj = foo
    assert replacer(1,2) == (1,2)



# Generated at 2022-06-14 06:04:01.968132
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    import weakref
    global ScopeReplacer__setattr___called
    ScopeReplacer__setattr___called = 0
    def ScopeReplacer__setattr__(self, attr, value):
        global ScopeReplacer__setattr___called
        ScopeReplacer__setattr___called += 1
        return original_ScopeReplacer__setattr__(self, attr, value)


    original_ScopeReplacer__setattr__ =\
            ScopeReplacer.__setattr__
    ScopeReplacer.__setattr__ = ScopeReplacer__setattr__

    class ScopeReplacer_setattr__tested(object):
        def __init__(self):
            self.expected_attribute = None
            self.expected_value = None
            self.expected_return_value = None


# Generated at 2022-06-14 06:04:11.125478
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    # Make sure that setting an attribute on a ScopeReplacer results in the
    # attribute getting set on the underlying object.
    module = {'sp':ScopeReplacer(scope=module,
        factory=scope_replacer_factory, name='sp')}
    sp = module['sp']
    sp.attr1="attr1"
    sp.attr2="attr2"
    assert_equal(sp.attr1, "attr1")
    assert_equal(sp.attr2, "attr2")
    # Once the underlying object has been created, it shouldn't be possible
    # to set additional attributes - we need to keep the object manageable in
    # a debugger, and this also ensures correct thread safety.
    sp2 = module['sp']
    assert_equal(sp, sp2)

# Generated at 2022-06-14 06:04:21.684107
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    l = [0]
    def f(s):
        l[0] += s
    class A:
        def __init__(self, f):
            self.f = f
        def __call__(self, s):
            return self.f(s)
    a = A(f)
    g = ScopeReplacer({}, lambda r, s, n: a, "g")
    g(1)
    assert l == [1]


from bzrlib import (
    config,
    debug,
    errors,
    osutils,
    trace,
    )


# TODO: Rob: resolve this in the future; it's currently needed for
#       bzr_remove and symlink - it's just a compatibility hack.
#       Note that this doesn't have to be a lazy-load, because nothing
#

# Generated at 2022-06-14 06:04:24.991252
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    a = ScopeReplacer(None, None, "a")
    a(1,2)


# Generated at 2022-06-14 06:04:42.919625
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    class Foo(object):
        def __init__(self):
            self.bar = 'this is bar'
        def __call__(self, param, **kwargs):
            return param + self.bar, kwargs
    scope = {}
    def lazy_factory(self, scope, name):
        return Foo()
    foo = ScopeReplacer(scope, lazy_factory, 'foo')
    assert foo.bar == 'this is bar'
    assert foo('x') == ('xthis is bar', {})
    assert foo('y', a='A', b='B') == ('ythis is bar', {'a': 'A', 'b': 'B'})


# Generated at 2022-06-14 06:04:51.233670
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    from bzrlib.lazy_import import lazy_import
    def factory(self, scope, name):
        return getattr(bzrlib.branch, name)
    scope = {}
    name = 'Branch'
    lazy_import(scope, '''
    from bzrlib import branch
    ''', name, factory)
    scope[name].__setattr__('foobar', 456)
    scope[name].foobar
    return

# Generated at 2022-06-14 06:05:05.262243
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    # Tests that __call__ delegates to real object once available.
    class _TestClass(object):
        _CALL_COUNT = 0
        def called(self, *args, **kwargs):
            _TestClass._CALL_COUNT += 1
        def other(self):
            return 42
    _TestClass._CALL_COUNT = 0
    scope = {}
    name = 'foo'
    scope[name] = None
    lazy = ScopeReplacer(scope, _TestClass, name)
    # We can't explicitly call __call__ as it will delegate to _resolve,
    # which will create a real object. Instead, we need to call the object
    # directly and hope it is replaced.
    lazy.called()
    # Check that the real object was called, not just the ScopeReplacer.
    self.assertEqual

# Generated at 2022-06-14 06:05:10.441494
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """IllegalUseOfScopeReplacer.__str__()"""
    fmt = "some message: %(extra)s"
    msg = "deal with this"

    class MyException(IllegalUseOfScopeReplacer):
        _fmt = fmt

    exc = MyException('foo', msg)
    e1 = str(exc)
    e2 = fmt % {'extra':msg}
    assert (e1 == e2), "formatting error in __str__ %r %r" % (e1,e2)


# Generated at 2022-06-14 06:05:17.966329
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    e = IllegalUseOfScopeReplacer('_str_', '_str_')
    s = u'Unprintable exception IllegalUseOfScopeReplacer'\
        ': dict=%r, fmt=%r, error=%r' % (e.__dict__, '%s', None)

    # check that getting the str and repr of the exception doesn't raise
    str(e)
    repr(e)



# Generated at 2022-06-14 06:05:27.171296
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """__str__() should return a ascii string."""
    # This test will check that the IllegalUseOfScopeReplacer class
    # behaves as expected when its __str__ method is called.
    # XXX: This test should be rewritten to be more generic.
    # http://bugs.python.org/issue162126
    name = 'name'
    msg = 'msg'
    umsg = unicode(msg)
    extra = 'new extra'
    uextra = unicode(extra)
    from bzrlib.lazy_import import IllegalUseOfScopeReplacer
    obj = IllegalUseOfScopeReplacer(name, msg)
    from bzrlib import (
        errors,
        osutils,
        branch,
        )
    # Create a lazy_import object to test with.
    import bzrlib.branch

# Generated at 2022-06-14 06:05:29.997708
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    """Method __setattr__ of class ScopeReplacer must :
    """
    # Testing if object is working as expected
    s = ScopeReplacer({}, lambda self, scope, name: self, 'name')
    s.a = 42
    s.a == 42
    s.b = 42
    s.b == 42



# Generated at 2022-06-14 06:05:37.901986
# Unit test for method __getattribute__ of class ScopeReplacer
def test_ScopeReplacer___getattribute__():
    """__getattribute__ should return the real object's attribute,
    after resolving the real object.

    """
    class MyObj(object):
        def __init__(self):
            self.foo = 42

    scope = {}
    factory = lambda obj, s, n: MyObj()
    name = "my_var"
    obj = ScopeReplacer(scope, factory, name)
    assert 'my_var' in scope # sanity check
    assert obj == scope[name] # sanity check
    assert obj.foo == 42
    assert obj.foo == scope[name].foo



# Generated at 2022-06-14 06:05:42.411621
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__()"""
    e = IllegalUseOfScopeReplacer('name', 'message', 'extra')
    s = unicode(e)
    assert u'name' in s
    assert u'message' in s
    assert u'extra' in s



# Generated at 2022-06-14 06:05:48.637094
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """__str__ of IllegalUseOfScopeReplacer"""
    e = IllegalUseOfScopeReplacer('name', 'msg', 'extra')
    from bzrlib.i18n import gettext
    assert str(e) == gettext(
        "ScopeReplacer object 'name' was used incorrectly: msg: extra")


# Generated at 2022-06-14 06:06:11.319422
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    from bzrlib.tests import TestCase
    class StubObject(object):
        def __init__(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs

    stub = StubObject()

    # set initial state
    test_obj = ScopeReplacer({}, lambda x,y,z:stub, 'name')
    # invoke on object
    returned = test_obj('a', b='c')
    # check correct return value
    assert returned is stub
    # check correct state - args
    assert test_obj.args == ('a',)
    # check correct state - kwargs
    assert test_obj.kwargs == {'b':'c'}




# Generated at 2022-06-14 06:06:17.131459
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    import bzrlib.tests
    def fake_factory(self, scope, name):
        return 1
    scope = locals()
    name = 'a_name'
    obj = ScopeReplacer(scope, fake_factory, name)
    bzrlib.tests.assertEqual(1, obj())

# Generated at 2022-06-14 06:06:27.757160
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """Method __str__ of class IllegalUseOfScopeReplacer

    """
    try:
        raise IllegalUseOfScopeReplacer('s', 'm')
    except IllegalUseOfScopeReplacer as no:
        assert str(no) == "ScopeReplacer object 's' was used incorrectly: m"
    try:
        raise IllegalUseOfScopeReplacer('s', 'm', 'e')
    except IllegalUseOfScopeReplacer as no:
        assert str(no) == "ScopeReplacer object 's' was used incorrectly: " \
                        "m: e"

# Generated at 2022-06-14 06:06:34.741267
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    s = "dummyMsg"
    f = IllegalUseOfScopeReplacer("dummyName", s)
    assert(isinstance(f.__str__(), str))
    assert(f.__str__() == s)
    f = IllegalUseOfScopeReplacer(None, None)
    assert(isinstance(f.__str__(), str))

# Generated at 2022-06-14 06:06:46.975208
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    global test_ScopeReplacer___setattr__
    def test_ScopeReplacer___setattr__():
        global AttributeError, IllegalUseOfScopeReplacer
        class A(object):
            def __init__(self):
                self.x = True
        a = A()
        target = ScopeReplacer({}, lambda s,s2,n2: a, 'target')
        target.__setattr__('x', False)
        if a.x:
            raise AssertionError(a.x)
        def raiser(e):
            raise e
        ScopeReplacer._should_proxy = False

# Generated at 2022-06-14 06:06:57.167026
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__ should return an ascii string"""
    e = IllegalUseOfScopeReplacer('test', '', None)
    s = unicode(e)
    if isinstance(s, str):
        # note that this check can be false when using Python 3
        raise AssertionError("__unicode__ should return unicode, "
                             "not str: %r" % (s,))
    # Note that this check can be true when using Python 3
    if isinstance(s, str):
        raise AssertionError("__unicode__ should be ascii, "
                             "not utf-8: %r" % (s,))



# Generated at 2022-06-14 06:07:07.629223
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    """Method __call__ of class ScopeReplacer

    This method tests that calling a ScopeReplacer calls the callable
    it's replacing.
    """
    # Setup
    import copy
    original_args = (4, 5, 7)
    original_kwargs = {'foo': 'bar', 'spam': 'eggs'}
    original_self = 9
    calls = []
    def func(*args, **kwargs):
        calls.append((args, kwargs))
        return 999

    # Test
    global l
    l = ScopeReplacer(locals(), func, 'l')
    result = l(*original_args, **original_kwargs)

    # Verify
    assert result == 999
    assert len(calls) == 1
    assert calls[0][0][0] is original_self

# Generated at 2022-06-14 06:07:13.729218
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """Test that the __unicode__ method of IllegalUseOfScopeReplacer returns a
    unicode object.
    """
    e = IllegalUseOfScopeReplacer('my', 'operation', 'myvar')
    u = unicode(e)
    _test_unicode_normalization(u, 'my', 'operation', 'myvar')


# Generated at 2022-06-14 06:07:20.290920
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    class _Sample(object):
        __slots__ = ('__args', '__kwargs')
        def __init__(self, *args, **kwargs):
            self.__args = args
            self.__kwargs = kwargs
        def __call__(self, *args, **kwargs):
            return [self.__args, self.__kwargs, args, kwargs]

    sample_obj = _Sample(1, 2, 3, four=4, five=5)
    def factory(scope_replacer, scope, name):
        return sample_obj
    scope = {}
    name = 'sample_obj'
    scope_replacer = ScopeReplacer(scope=scope, factory=factory, name=name)

# Generated at 2022-06-14 06:07:23.633977
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__(self: bzrlib.lazy_import.IllegalUseOfScopeReplacer) -> unicode"""


# Generated at 2022-06-14 06:07:49.015454
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    ScopeReplacer = lazy_import.ScopeReplacer
    class Dummy(object):
        def __call__(self, *args, **kwargs):
            return (args, kwargs)
    scope = {'x': None}
    def factory(self, scope, name):
        return Dummy()
    scope['x'] = ScopeReplacer(scope, factory, 'x')
    assert scope['x'](1, 2, 3) == ((1, 2, 3), {}), scope['x'](1, 2, 3)
    assert scope['x'](a=1) == ((), {'a':1}), scope['x'](a=1)
    assert scope['x'](1, a=1) == ((1,), {'a':1}), scope['x'](1, a=1)

# Generated at 2022-06-14 06:07:52.212281
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    pass  # TODO: implement this

    # TODO: test the functionality of decorators.
    # They should work by using the returned value to replace the ScopeReplacer
    # and be able to pass in various arguments



# Generated at 2022-06-14 06:08:06.703423
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    from bzrlib.tests import TestCase

    class TestIllegalUseOfScopeReplacer(TestCase):

        def setUp(self, *args, **kwargs):
            super(TestIllegalUseOfScopeReplacer, self).setUp(*args, **kwargs)
            self.exception = IllegalUseOfScopeReplacer('some_name', 'some_msg')

        def test___unicode___with_str_return_value(self):
            self.exception._preformatted_string = 'some message'
            self.assertEqual('some message', unicode(self.exception))

        def test___unicode___with_non_unicode_return_value(self):
            self.exception._preformatted_string = 42
            self.assertEqual(u'42', unicode(self.exception))

       

# Generated at 2022-06-14 06:08:18.100143
# Unit test for method __call__ of class ScopeReplacer

# Generated at 2022-06-14 06:08:24.608893
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """Testing IllegalUseOfScopeReplacer.__str__()"""
    sr = IllegalUseOfScopeReplacer('foo', 'hi there')
    e = str(sr)
    import re
    pattern = """^ScopeReplacer .* was used incorrectly: .*$"""
    assert re.match(pattern, e), '%r does not match %r' % (e, pattern)



# Generated at 2022-06-14 06:08:33.165157
# Unit test for method __getattribute__ of class ScopeReplacer
def test_ScopeReplacer___getattribute__():
    # TODO: currently it is only possible to test whether the
    #       ScopeReplacer is able to proxy getattr calls.
    #       it is not easy to write a unit test that actually
    #       checks whether a second thread has replaced the
    #       ScopeReplacer with a real object before it is
    #       too late.
    import json
    import bzrlib.lazy_import
    globals()['json'] = bzrlib.lazy_import.ScopeReplacer(globals(),
        factory=lambda sr, scope, name: json, name='json')
    json.__name__ == 'json'

    bzrlib.lazy_import.ScopeReplacer._should_proxy = False

# Generated at 2022-06-14 06:08:35.744369
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    import random
    random = ScopeReplacer(globals(), lambda self, x, y: random, 'random')
    """Test __call__."""
    random()

# Generated at 2022-06-14 06:08:42.285695
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    from bzrlib.tests import TestCase
    class Test(TestCase):
        def test_simple(self):
            def f(s):
                return s
            scope = {}
            scope_replacer = ScopeReplacer(scope, f, 'f')
            self.assertEqual("Hello", scope_replacer("Hello"))
            self.assertEqual("Hello", scope['f']("Hello"))
    Test('test_simple').run()



# Generated at 2022-06-14 06:08:46.956777
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    import __builtin__
    exc = IllegalUseOfScopeReplacer('revno', 'clearing', 'foo')
    u = unicode(exc)
    __builtin__.__dict__['u'] = u



# Generated at 2022-06-14 06:08:49.492267
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    import bzrlib
    b = bzrlib.branch.Branch()
    f = b.get_bound_location

# Generated at 2022-06-14 06:09:20.817137
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    import sys
    v = ScopeReplacer(locals(), lambda self, s, n: sys, 'v')
    assert v._should_proxy
    sys._should_proxy = False
    try:
        v('exit')
    except IllegalUseOfScopeReplacer as e:
        assert e.name == 'v'
        assert 'Object already replaced' in str(e)
    else:
        assert False, "Expected IllegalUseOfScopeReplacer but no exception"
    finally:
        sys._should_proxy = True
        del sys._should_proxy



# Generated at 2022-06-14 06:09:25.401587
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """Unit test for method __unicode__ of class IllegalUseOfScopeReplacer

    This test is not run automatically. To run it::

        $ bzrlib/tests/test_lazy_import.py
    """
    import doctest
    return doctest.testmod()



# Generated at 2022-06-14 06:09:34.514415
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """__str__ must return a str and never a unicode object."""
    from bzrlib.lazy_import import IllegalUseOfScopeReplacer
    e = IllegalUseOfScopeReplacer('name', 'msg', extra='extra')
    s = e.__str__()
    assert isinstance(s, str)
    assert not isinstance(s, unicode)
    # now try to make one with non-ascii data.
    e = IllegalUseOfScopeReplacer('name', 'msg\xe3', extra='extra\xe3')
    s = e.__str__()
    assert isinstance(s, str)
    assert not isinstance(s, unicode)

