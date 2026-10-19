

# Generated at 2022-06-14 05:59:53.379863
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """__str__ should return a str object, not a unicode object."""
    inst = IllegalUseOfScopeReplacer('name', 'msg')
    assert isinstance(inst.__str__(), str)

# Generated at 2022-06-14 06:00:05.437459
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """Empty IllegalUseOfScopeReplacer object has the same __unicode__ as the
    IllegalUseOfScopeReplacer message"""
    class MyIllegalUseOfScopeReplacer(IllegalUseOfScopeReplacer):
        _fmt = "A %(item)s!"
    illegal = MyIllegalUseOfScopeReplacer('foo', 'Missing', extra=None)
    expected = "A foo!"
    actual = unicode(illegal)
    try:
        actual = unicode(actual)
    except UnicodeDecodeError:
        pass # just bind to 'e' for formatting below
    else:
        e = None

# Generated at 2022-06-14 06:00:17.059691
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    # Test that __setattr__ calls the wrapped objects __setattr__ method
    # correctly

    class Dummy:
        def __setattr__(self, attr, value):
            self.__dict__[attr] = value

    scope = {}
    lazy = ScopeReplacer(scope, lambda x, y, z: Dummy(), 'dummy')
    lazy.test_attr = 'test'
    assert scope['dummy'].test_attr == 'test', 'attribute not set on object'
    assert scope['dummy'].__dict__['test_attr'] == 'test', (
        'attribute not set in __dict__ of object')



# Generated at 2022-06-14 06:00:22.658294
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    if (
        ScopeReplacer.__setattr__.im_func is not object.__setattr__
    ):
        raise AssertionError


__all__ = [
    'IllegalUseOfScopeReplacer',
    'ScopeReplacer',
    'lazy_import',
    'test_ScopeReplacer___setattr__',
    ]



# Generated at 2022-06-14 06:00:36.850450
# Unit test for method __eq__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___eq__():
    """__eq__ should be equal for equal instances."""
    from bzrlib.tests.blackbox import TestCaseWithTransport
    TestCaseWithTransport.TestCase.longMessage = True
    class Test(TestCaseWithTransport.TestCase):
        def test(self):
            e1 = IllegalUseOfScopeReplacer("name","msg")
            e2 = IllegalUseOfScopeReplacer("name","msg")
            self.assertEqual(e1, e2, 
                             "e1 and e2 should be equal instances")
            e3 = IllegalUseOfScopeReplacer("name","msg",extra="test")
            e4 = IllegalUseOfScopeReplacer("name","msg",extra="test")
            self.assertEqual(e3, e4, 
                             "e3 and e4 should be equal instances")
   

# Generated at 2022-06-14 06:00:43.430407
# Unit test for method __eq__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___eq__():
    """IllegalUseOfScopeReplacer.__eq__ should compare instance dictionaries"""
    ex1 = IllegalUseOfScopeReplacer('name1', 'msg1')
    ex2 = IllegalUseOfScopeReplacer('name1', 'msg1')
    ex1.extra = 'extra1'
    ex2.extra = 'extra1'
    assert ex1 == ex2, (ex1, ex2)
    ex2.extra = 'extra2'
    assert ex1 != ex2, (ex1, ex2)
    ex2 = 1
    assert ex1 != ex2, (ex1, ex2)



# Generated at 2022-06-14 06:00:52.056231
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """IllegalUseOfScopeReplacer must inherit from Exception, and therefore
    from object.
    If the class hierarchy was:
    BaseException
    +-- Exception
    |   +-- IllegalUseOfScopeReplacer

    then this test would fail because str() does not call __str__.
    """
    e = IllegalUseOfScopeReplacer("name", "msg")
    s = str(e)
    assert isinstance(s, str)
    assert e._format() == s
    assert e._get_format_string() == s


# Generated at 2022-06-14 06:00:55.866633
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """IllegalUseOfScopeReplacer.__str__() should return a str object."""
    import bzrlib.errors as errors
    try:
        raise errors.IllegalUseOfScopeReplacer('foo', 'bar')
    except errors.IllegalUseOfScopeReplacer as e:
        assert isinstance(e.__str__(), str)



# Generated at 2022-06-14 06:01:00.637185
# Unit test for method __getattribute__ of class ScopeReplacer
def test_ScopeReplacer___getattribute__():
    """Test method __getattribute__ of class ScopeReplacer."""
    from bzrlib.lazy_import import ScopeReplacer
    class X(object):
        x = 1
        def __init__(self):
            self.y = 2
    def f(self, scope, name):
        return X()
    scope = {'x': None}
    x = ScopeReplacer(scope, f, 'x')
    assert x.x == 1
    assert x.y == 2
    assert x.__class__.__name__ == 'X'
    assert x.__class__ == X
    assert x._resolve() == X()
# End test_ScopeReplacer___getattribute__

# Generated at 2022-06-14 06:01:06.583324
# Unit test for method __eq__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___eq__():
    def check(a, b, want):
        actual = (a == b)
        if (actual != want):
            raise AssertionError('A=%s, B=%s, Want=%s, Got=%s'
                % (repr(a), repr(b), want, actual))
    err = IllegalUseOfScopeReplacer('name', 'msg', 'extra')
    check(err, err, True)
    err_other_1 = IllegalUseOfScopeReplacer('name', 'msg', 'extra')
    check(err, err_other_1, True)
    err_other_2 = IllegalUseOfScopeReplacer('name', 'msg', 'extra-other')
    check(err, err_other_2, False)

# Generated at 2022-06-14 06:01:23.170295
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """IllegalUseOfScopeReplacer.__str__ should always return str"""
    e = IllegalUseOfScopeReplacer('foo', '%(name)s', '"bar"')
    u = unicode(e)
    if not isinstance(u, unicode):
        raise AssertionError('IllegalUseOfScopeReplacer.__str__() should '
            'always return a str, not %s' % type(u))
    return u


# Generated at 2022-06-14 06:01:33.521367
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    import bzrlib.lazy_import
    bzrlib.lazy_import.ScopeReplacer._should_proxy = False
    import bzrlib.tests.test_lazy_import
    replacer = bzrlib.tests.test_lazy_import.MockScopeReplacer()
    try:
        replacer.foo = 'bar'
    except bzrlib.lazy_import.IllegalUseOfScopeReplacer as e:
        assert str(e).startswith('Object tried to replace itself')
    else:
        raise AssertionError('Should have raised exception')



# Generated at 2022-06-14 06:01:41.388554
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """test_IllegalUseOfScopeReplacer___unicode__

    Ensure that IllegalUseOfScopeReplacer objects implement a __unicode__
    method and that it behaves as expected.
    """
    from bzrlib.lazy_import import IllegalUseOfScopeReplacer
    def assertUnicodeEqual(expected, got):
        """Helper for assertEqual that only compares the 'unicode' representation
        of the object.
        """
        from bzrlib.tests import TestCase
        TestCase().assertEqualUnicode(expected, got)

    # Make sure that the exception is raised and that it has an useful message
    # in it.

# Generated at 2022-06-14 06:01:53.159909
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    """Testing method __setattr__ of class ScopeReplacer."""
    import bzrlib.lazy_import
    bzrlib.lazy_import.ScopeReplacer._should_proxy = False
    import inspect
    import sys
    frame = inspect.currentframe()
    def lazy_import_factory(self, scope, name):
        import bzrlib.lazy_import
        bzrlib.lazy_import.ScopeReplacer._should_proxy = True
        import bzrlib
        return bzrlib
    obj = bzrlib.lazy_import.ScopeReplacer(sys.modules, lazy_import_factory, 'bzrlib')
    obj2 = obj
    obj3 = obj
    # Test __setattr__ raises IllegalUseOfScopeReplacer

# Generated at 2022-06-14 06:02:03.081790
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    def _check_exception_type_and_content(exc, type, content):
        if not isinstance(exc, type):
            raise AssertionError("Unexpected exception %r, wanted %r"
                                 % (exc, type))
        if content not in str(exc):
            raise AssertionError("Exception %r did not contain expected"
                                 " string %r" % (exc, content))

    # Disable proxy to test detection of abuse.
    old_should_proxy = ScopeReplacer._should_proxy

# Generated at 2022-06-14 06:02:05.894664
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """Method __unicode__ returns a unicode object"""
    iu = IllegalUseOfScopeReplacer('name', 'msg')
    assert isinstance(unicode(iu), unicode)

# Generated at 2022-06-14 06:02:16.550335
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """__str__ should return a str in the default encoding.

    """
    e = IllegalUseOfScopeReplacer('foo', 'bar', 'extra')
    s = str(e)
    # assertIsInstance does not exist in python 2.4.
    assert isinstance(s, str), "__str__ should return a 'str' object"
    # but assertIsInstance does make it into python 2.5, so use it there.
    # (this test case will not work in python 2.4)
    assert isinstance(s, str), "__str__ should return a 'str' object"

# Generated at 2022-06-14 06:02:28.583514
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    """__setattr__ works as expected."""
    # __setattr__ only proxies to an underlying object if it uses an
    # attribute that exist on that object. We construct a test that try to
    # mutate an object via __setattr__, but for a attribute that is not on
    # the underlying object.
    #
    # We also need to handle the case that the underlying object is a proxy
    # itself. We test with a scope replacer that is, and one that is not.
    _real_obj_with_foo = type('_', (), dict(foo=1))()
    _real_obj_without_foo = type('_', (), dict(foo=1))()

    class _DummyScopeReplacer(ScopeReplacer):
        """''Replacer'' that always just return the real object."""

# Generated at 2022-06-14 06:02:36.624458
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    """__call__(self: bzrlib.lazy_import.ScopeReplacer, *args, **kwargs) -> object
    """

    def _test(obj, *args, **kwargs):
        return obj

    class _test(object):

        def __call__(self, *args, **kwargs):
            return self

    scope = {'_test': _test()}
    lazy_import(scope, '_test')
    assert scope['_test'] is scope['_test'](1, 2, 3)



# Generated at 2022-06-14 06:02:37.682606
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    raise NotImplementedError()


# Generated at 2022-06-14 06:03:10.157378
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """
    An assertionError is raised when the __unicode__ method of 
    IllegalUseOfScopeReplacer is called.
    """
    from bzrlib import lazy_import
    try:
        lazy_import.lazy_import(locals(), '''
        from bzrlib import subprocess
        ''')
        subprocess.getoutput(['ThisCommandDoesNotExist']).decode('utf-8')
    except lazy_import.IllegalUseOfScopeReplacer as e:
        assert unicode(e) != ''
        # The next two tests are valid because this is the only known usage
        # of IllegalUseOfScopeReplacer, and so __unicode__ is valid.
        assert e.name == 'subprocess'
        assert e.msg == "You can't use a ScopeReplacer object in a scope"
   

# Generated at 2022-06-14 06:03:15.653806
# Unit test for method __getattribute__ of class ScopeReplacer
def test_ScopeReplacer___getattribute__():
    from bzrlib import _lazy_import
    from bzrlib.tests.per_lazy_import import TestCase
    class ScopeReplacerGetattrTest(TestCase):
        def test(self):
            x = _lazy_import.scope_replace(
                globals(), 'X', 'bzrlib.tests.per_lazy_import.ClassWithOneAttr')
            self.assertEqual(x.one, 'ONE')
            self.assertEqual(x.two, 'TWO')
            self.assertRaises(
                AttributeError, lambda: __getattr__(x, 'three'))
    return ScopeReplacerGetattrTest



# Generated at 2022-06-14 06:03:17.630718
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    """__call__(self, *args, **kwargs)"""

# Generated at 2022-06-14 06:03:28.873093
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """This method tests IllegalUseOfScopeReplacer.__str__()"""
    # This method uses 'exec' and cannot be tested by pychecker
    import sys
    import threading

    class MyClass(object):
        def __str__(self):
            return "MyClass instance"

    class MyThread(threading.Thread):
        """This thread raises an exception"""
        def run(self):
            """Run method of thread"""
            raise IllegalUseOfScopeReplacer("name",
                                            "<exception msg>",
                                            "<more info>")


# Generated at 2022-06-14 06:03:33.606884
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """Unit test for method __unicode__ of class IllegalUseOfScopeReplacer"""
    e = IllegalUseOfScopeReplacer('name', 'msg')
    assert isinstance(unicode(e), unicode), "IllegalUseOfScopeReplacer.__unicode__ didn't return a unicode object."


# Generated at 2022-06-14 06:03:34.787338
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__(): pass # test_module_import


# Generated at 2022-06-14 06:03:41.502005
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """Method __str__() of class IllegalUseOfScopeReplacer should work."""
    e1 = IllegalUseOfScopeReplacer(name='foo', msg='bar')
    e1.__str__()
    e1._fmt = '%(msg)s'
    e1.__str__()
    e1._preformatted_string = 'baz'
    e1.__str__()


# Generated at 2022-06-14 06:03:44.218352
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    return 2*3 == 6
# End of unit test for method __call__ of class ScopeReplacer


# Generated at 2022-06-14 06:03:58.338467
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    """This test demonstrates the use of ScopeReplacer.

    To run this test:

    bzr selftest --subunit bzrlib.tests.test_lazy_import.test_ScopeReplacer___setattr__

    """
    from bzrlib.tests import TestCase
    from bzrlib.tests.matchers import ContainsNoVfsCalls
    from bzrlib.lazy_import import ScopeReplacer
    from bzrlib.lazy_import import lazy_import
    import functools, sys
    # This test is fragile and we only want to test ScopeReplacer, not any
    # other part of bzrlib, so we come up with a minimal example that uses
    # ScopeReplacer.
    #
    # The module under test is a function that uses ScopeReplacer to
    # construct a

# Generated at 2022-06-14 06:04:06.204301
# Unit test for method __getattribute__ of class ScopeReplacer
def test_ScopeReplacer___getattribute__():
    # Note that we actually never call this function in the tests, but having
    # it marked as a test means there can be no dead code on it.
    from bzrlib.lazy_import import lazy_import
    global get_module_file_id
    get_module_file_id = None

    def do_lazy_import(scope, modulename, _name_id=None):
        # This is a simplified version of lazy_import
        modulename = modulename.strip()
        _name_id = _name_id or modulename.replace('.', '_')
        scope[_name_id] = ScopeReplacer(scope, get_module, _name_id)
        return _name_id


# Generated at 2022-06-14 06:04:20.212536
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    return ScopeReplacer.__call__



# Generated at 2022-06-14 06:04:25.562681
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """__str__ must return a str, not a unicode object."""
    e = IllegalUseOfScopeReplacer(name='c', msg='msg')
    s = str(e)
    assert isinstance(s, str)



# Generated at 2022-06-14 06:04:28.578674
# Unit test for method __getattribute__ of class ScopeReplacer
def test_ScopeReplacer___getattribute__():
    # __getattribute__ -> <method '__getattribute__' of 'object' objects>
    assert ScopeReplacer.__getattribute__ is not None

# Generated at 2022-06-14 06:04:40.114280
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """test__unicode__ of IllegalUseOfScopeReplacer"""
    # We should be able to get a unicode repr of the object, even if the
    # Exception class has a constructor that takes non-string arguments
    class UnicodeException(Exception):
        def __init__(self, name, msg, extra=0):
            super(UnicodeException, self).__init__(name, msg)
            self.extra = extra
    class ExcParent(IllegalUseOfScopeReplacer):
        _fmt = '%(msg)s'
    class ExcChild(IllegalUseOfScopeReplacer):
        _fmt = '%(msg)s'
    class BadEncodingException(IllegalUseOfScopeReplacer):
        _fmt = '%(msg)s'

# Generated at 2022-06-14 06:04:44.215765
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """__str__ should return a string, not unicode"""
    exc = IllegalUseOfScopeReplacer(name='foo', msg='bar')
    s = str(exc)
    assert isinstance(s, str)



# Generated at 2022-06-14 06:04:53.936114
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    from bzrlib.tests import TestCase
    from bzrlib import lazy_import
    import sys

    class TestLazyImport(TestCase):

        def test_lazy_import_does_not_override_existing_names(self):
            # In some locations, a name might already exist in the namespace.
            # This is unlikely but not impossible.
            # We should not override those names.
            class MyException(Exception):
                pass
            def my_function():
                raise MyException()
            scope = {'MyException':MyException, 'my_function':my_function}
            # ScopeReplacer will use MyException to raise an exception
            # if it tries to override 'MyException'
            # it will try to call my_function() if it tries to override
            # 'my_function'.
            lazy_import.l

# Generated at 2022-06-14 06:05:06.187298
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
  from unittest import TestCase
  from bzrlib.lazy_import import ScopeReplacer
  from tempfile import mkdtemp
  from shutil import rmtree
  from bzrlib import errors
  import os
  import sys
  import gc
  class TestCaseWithTransport(TestCase):
    def setUp(self):
      self.prefix = mkdtemp()
    def tearDown(self):
      rmtree(self.prefix)
  class TestCase1(TestCaseWithTransport):
    def test_ScopeReplacer___setattr__(self):
      sep = ScopeReplacer(globals(),
                          ScopeReplacer._factory_import,
                          'sep')

# Generated at 2022-06-14 06:05:10.353859
# Unit test for method __call__ of class ScopeReplacer
def test_ScopeReplacer___call__():
    class Foo(object):
        def __call__(self):
            return 1
    def factory(sr, scope, name):
        return Foo()

    # Test the obj is called.
    scope = {}
    name = 'obj'
    replacer = ScopeReplacer(scope, factory, name)
    assert replacer() == 1



# Generated at 2022-06-14 06:05:23.411306
# Unit test for method __getattribute__ of class ScopeReplacer
def test_ScopeReplacer___getattribute__():
    """Checks __getattribute__ of ScopeReplacer class.

    """
    # test for the case when attr is not equal "_resolve" and "_real_obj"
    def run():
        import random
        class Foo:
            pass
        #Generate random value for attributes of 'Foo' class.
        attrs={}
        for i in range(10):
            k,v=random.randrange(100),random.random()
            attrs[k]=v
        Foo.__dict__.update(attrs)
        globals()['Foo']=Foo
        #Generate random value for 'name' and 'attr'
        name=random.randrange(100)
        attr=random.randrange(100)
        scope = {}
        # Create object 'obj' of 'ScopeReplacer' class.
       

# Generated at 2022-06-14 06:05:28.995746
# Unit test for method __getattribute__ of class ScopeReplacer
def test_ScopeReplacer___getattribute__():
    real_obj = object()
    def factory(self, scope, name):
        return real_obj
    sr = ScopeReplacer({}, factory, name='factory')
    assert sr == real_obj
    assert sr.__getattribute__('__class__') == real_obj


# Generated at 2022-06-14 06:05:59.217962
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    import tempfile
    # Test case to ensure the method does not allow setting of the
    # attribute _should_proxy after the first call of _resolve has been
    # made.

    class A(ScopeReplacer):
        """A specialized ScopeReplacer that prints a message if _should_proxy
        is set"""

        def _resolve(self):
            print("Resolving object %s" % self._name)
            return super(A, self)._resolve()

    fd, tmpfile = tempfile.mkstemp()

# Generated at 2022-06-14 06:06:10.711941
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    ScopeReplacer._should_proxy = True

    class Obj(object):
        def __init__(self):
            self._a = None

        def get_a(self):
            return self._a

        def set_a(self, value):
            self._a = value

    scope = {}
    def factory(self, scope, name):
        return Obj()
    replacer = ScopeReplacer(scope, factory, name='obj')
    replacer.set_a(5)
    replacer.a = 6
    try:
        replacer.a = 7
        assert False, '__setattr__ of ScopeReplacer should not work when '\
            'ScopeReplacer._should_proxy is set to False'
    except IllegalUseOfScopeReplacer:
        pass



# Generated at 2022-06-14 06:06:16.844271
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """Test for method __str__ of class IllegalUseOfScopeReplacer"""
    e = IllegalUseOfScopeReplacer('one', 'two', 'three')
    r = repr(e)
    assert isinstance(r, str)
    assert r == "IllegalUseOfScopeReplacer('one', 'two', 'three')"

# Generated at 2022-06-14 06:06:30.436545
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__ of IllegalUseOfScopeReplacer should work in all situations.

    It should work with a simple string message, a unicode message, and a
    message which cannot be decoded to a unicode string.
    """
    # str
    x = IllegalUseOfScopeReplacer('s', 'simple')
    assert isinstance(x.__unicode__(), unicode)
    # unicode
    x = IllegalUseOfScopeReplacer('u', u'simple')
    assert isinstance(x.__unicode__(), unicode)
    # undecodeable
    class Binary(object):
        def __str__(self):
            return '\xaa'
    x = IllegalUseOfScopeReplacer('b', Binary())
    assert isinstance(x.__unicode__(), unicode)



# Generated at 2022-06-14 06:06:38.952627
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """A test for method __str__ of class IllegalUseOfScopeReplacer
    """
    from bzrlib.lazy_import import IllegalUseOfScopeReplacer
    test_obj = IllegalUseOfScopeReplacer('name', 'msg', 'extra')
    # __str__() should always return a 'str' object, never a 'unicode' object
    assert isinstance(str(test_obj), str)
test_IllegalUseOfScopeReplacer___str__.unittest = ['test', 'lazy_import']



# Generated at 2022-06-14 06:06:49.032679
# Unit test for method __getattribute__ of class ScopeReplacer
def test_ScopeReplacer___getattribute__():
    """ __getattribute__()

        This method is complicated by the presence of a scope. It needs to
        be able to handle the case where a variable is referenced before
        it is actually assigned to.
    """
    scope = {'foo': 'bar'}
    lazy = ScopeReplacer(scope, None, 'foo')
    # Until the real object is available, we should get whatever was in the
    # scope originally.
    e = None
    try:
        lazy.replace()
    except IllegalUseOfScopeReplacer as e:
        pass
    else:
        raise AssertionError('ScopeReplacer.replace() should have raised an'
            ' exception.')
    assert e.msg == 'Object tried to replace itself, check it\'s not using'\
        ' its own scope.'
    assert e.name == 'foo'

# Generated at 2022-06-14 06:06:55.350062
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """__unicode__ should return a unicode object"""
    e = IllegalUseOfScopeReplacer('name', 'message')
    u = e.__unicode__()
    assert isinstance(u, unicode), \
        'IllegalUseOfScopeReplacer.__unicode__ did not return unicode'



# Generated at 2022-06-14 06:06:57.058147
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    import doctest
    doctest.DocTestSuite('bzrlib.lazy_import')



# Generated at 2022-06-14 06:07:06.493791
# Unit test for method __getattribute__ of class ScopeReplacer
def test_ScopeReplacer___getattribute__():
    """Test method ScopeReplacer.__getattribute__()"""
    import unittest
    class TestScopeReplacer(unittest.TestCase):
        def test___getattribute__(self):
            import sys
            from bzrlib.lazy_import import (
                ScopeReplacer,
                IllegalUseOfScopeReplacer,
                )
            def factory(self, scope, name):
                scope[name] = scope[name]
                return scope[name]
            scope = sys._getframe(1).f_locals
            original_scope_replacer = scope['ScopeReplacer']

# Generated at 2022-06-14 06:07:11.467877
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """IllegalUseOfScopeReplacer.__unicode__() should return unicode object"""
    e = IllegalUseOfScopeReplacer('name', 'msg')
    u = unicode(e)
    assert isinstance(u, unicode)
    return u


# Generated at 2022-06-14 06:07:51.903833
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    """Unit test for method __setattr__ of class ScopeReplacer"""
    #__setattr__ method of class ScopeReplacer

    class A(object):
        def __setattr__(self, attr, value):
            raise ValueError('set %r to %r' % (attr, value))
    a = A()

# Generated at 2022-06-14 06:07:59.816929
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    # Method __unicode__ of class IllegalUseOfScopeReplacer must return
    # a unicode object.
    e = IllegalUseOfScopeReplacer('foo', 'got a %s', 'bar')
    u = unicode(e)
    assert(isinstance(u, unicode))
    assert(u == "ScopeReplacer object 'foo' was used incorrectly: got a bar")

# Generated at 2022-06-14 06:08:10.414975
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    """Let's test the __setattr__ method of class ScopeReplacer"""
    import sys
    import sys
    from bzrlib.lazy_import import lazy_import, ScopeReplacer
    from bzrlib.lazy_import import IllegalUseOfScopeReplacer


    # We create a blank ScopeReplacer object
    obj = ScopeReplacer(scope=None, factory=None, name=None)
    attr='_resolve'
    # We set the attribute '_resolve' to obj
    object.__setattr__(obj, attr, object.__getattribute__(obj, '_resolve'))
    # We expect:
    #
    # obj._resolve() == obj
    assert (obj._resolve() == obj)
    #
    # to be:
    #
    # False

# Generated at 2022-06-14 06:08:23.254347
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    # Check that __setattr__ properly processes
    # IllegalUseOfScopeReplacer exceptions
    from bzrlib.lazy_import import ScopeReplacer
    from bzrlib.lazy_import import IllegalUseOfScopeReplacer
    from bzrlib.lazy_import import lazy_import
    import sys

    # Generate error, check it looks sane
    # This is not a complete test of the error, but it is better than no test.
    # test_lazy_import_module.test_lazy_import() has a complete test.
    saved_should = ScopeReplacer._should_proxy

# Generated at 2022-06-14 06:08:26.237144
# Unit test for method __getattribute__ of class ScopeReplacer
def test_ScopeReplacer___getattribute__():
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS, verbose=True)
test_ScopeReplacer___getattribute__()



# Generated at 2022-06-14 06:08:31.504772
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    import bzrlib.tests
    bzrlib.tests.TestCaseWithMemoryTransport.tearDown(None)
    bzrlib.tests.TestCaseWithMemoryTransport.setUp(None)
    return

# Generated at 2022-06-14 06:08:42.929282
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    import bzrlib.tests
    import sys
    import types
    import unittest

    class Dummy(object):
        """A class with special meaning for the tests"""
        pass

    class TestScopeReplacer(unittest.TestCase):

        def setUp(self):
            self.bzrlib.tests.blackbox.TestCaseWithTransport.setUp(self)
            self.default_scope = sys._getframe(0).f_globals
            self.obj_name = 'test_obj'
            self.obj = Dummy()
            self.scope_replacer = None


# Generated at 2022-06-14 06:08:45.531164
# Unit test for method __unicode__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___unicode__():
    """Unit test for method __unicode__ of class IllegalUseOfScopeReplacer"""
    import doctest
    try:
        doctest.testmod()
    except Exception as e:
        raise e




# Generated at 2022-06-14 06:08:53.878629
# Unit test for method __setattr__ of class ScopeReplacer
def test_ScopeReplacer___setattr__():
    """Test method __setattr__ of class ScopeReplacer.

    If method __setattr__ of class ScopeReplacer is broken, then e.g.
    property bzrlib.inter.Inter.show_errors will be always set to the
    value contained in the __init__ method of class
    bzrlib.inter.Inter.

    To run the unit tests, please call this method from the command
    line::

    bzr selftest bzrlib.lazy_import.test_ScopeReplacer___setattr__

    """
    from bzrlib.tests.blackbox import ExternalBase
    from bzrlib.tests.script import (
        ScriptRunner,
        )


# Generated at 2022-06-14 06:08:56.764632
# Unit test for method __str__ of class IllegalUseOfScopeReplacer
def test_IllegalUseOfScopeReplacer___str__():
    """__str__ of IllegalUseOfScopeReplacer class."""
    scope_err = IllegalUseOfScopeReplacer('name', 'msg', extra=None)
    expected = "ScopeReplacer object 'name' was used incorrectly: msg"
    assert str(scope_err) == expected


_modules_not_loaded = {}