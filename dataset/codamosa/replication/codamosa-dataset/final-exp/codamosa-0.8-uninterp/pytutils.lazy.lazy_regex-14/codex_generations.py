

# Generated at 2022-06-14 06:14:44.856841
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Test __unicode__ of class InvalidPattern.

    This is a tricky method to test because it is called when another
    exception is caught in __init__. That is, it is called when we
    want to raise a new exception to report that the user provided
    an invalid regex.
    """
    from bzrlib.i18n import gettext

    class MyException(Exception):
        pass

    class MyInvalidPattern(InvalidPattern):
        _fmt = 'Try harder: %(msg)s'

    # These tests check that the new exception can be properly
    # raised and caught, and that its content is what we expect
    # it to be.
    try:
        raise MyInvalidPattern('some error')
    except MyInvalidPattern as e:
        print(e)
        # Test that the new exception can be properly raised and caught
       

# Generated at 2022-06-14 06:14:51.263276
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """Method str raises UnicodeDecodeError if object contains invalid UTF8."""
    err = InvalidPattern(msg=u'foo\x80bar')
    try:
        str(err)
    except UnicodeDecodeError:
        pass # expected
    else:
        raise AssertionError('str(err) should raise UnicodeDecodeError')

# Generated at 2022-06-14 06:15:04.370627
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Unit test for method __unicode__ of class InvalidPattern.

    This tests that method prints an unicode object, and that it returns a
    unicode object when a 'str' object is passed.
    """
    import types
    import sys
    # Set up a unicode object in a Latin-1 environment.
    unicode_obj = unicode('a\u00C9cole')
    # unicode_obj.encode('utf-8') should fail.
    unicode_obj.encode('utf-8')
    # unicode_obj.encode('Latin-1') should succeed.
    unicode_obj.encode('Latin-1')
    # Set up an str object in a Latin-1 environment.
    str_obj = unicode_obj.encode('Latin-1')
    # str_obj.decode('

# Generated at 2022-06-14 06:15:11.260490
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Test that method __unicode__ of class InvalidPattern doesn't fail"""
    class TransportedInvalidPattern(InvalidPattern):
        """ Just a simple transport of InvalidPattern to be able to test the
        inherited method.
        """
        pass
    transport = TransportedInvalidPattern("message")
    # And call the method we want to test
    str(transport)

# Generated at 2022-06-14 06:15:24.769758
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Error message in unicode"""

    # Test with default formatting
    exc = InvalidPattern('Foo')
    assert isinstance(exc.__unicode__(), unicode)
    assert exc.__unicode__() == u'Invalid pattern(s) found. Foo'

    # Test with a preformatted message
    exc = InvalidPattern('Foo')
    exc._preformatted_string = u'I am sorry, Foo'
    assert isinstance(exc.__unicode__(), unicode)
    assert exc.__unicode__() == u'I am sorry, Foo'

    # Test with a non-string message
    exc = InvalidPattern(14)
    assert isinstance(exc.__unicode__(), unicode)

# Generated at 2022-06-14 06:15:29.476402
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    # __unicode__ should return an object of type unicode
    msg = u"foo"
    ip = InvalidPattern(msg)
    u = ip.__unicode__()
    assert isinstance(u, unicode)
    assert u == msg
    msg = "foo"
    ip = InvalidPattern(msg)
    u = ip.__unicode__()
    assert isinstance(u, unicode)
    assert u == msg.decode('utf8')

# Generated at 2022-06-14 06:15:42.162132
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """InvalidPattern.__unicode__ should return a unicode object.
    """
    from bzrlib.i18n import gettext
    from bzrlib.patiencediff import patiencediff
    from bzrlib.diff import unified_diff
    from bzrlib import urlutils
    class FakeLazyRegex(object):
        def __init__(self, pattern, flags=0):
            self.pattern = pattern
            self.flags = flags
        def finditer(self, string):
            return iter(())
        def __unicode__(self):
            return ''.join([u"u'",
                            self.pattern,
                            u"'"])
    class FakeUrlutils(object):
        def local_path_to_url(self, path):
            return path

# Generated at 2022-06-14 06:15:45.716884
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """InvalidPattern.__str__ must return a str."""
    exc = InvalidPattern(msg='msg')
    assert isinstance(str(exc), str)


# Generated at 2022-06-14 06:15:55.869682
# Unit test for method __setstate__ of class LazyRegex
def test_LazyRegex___setstate__():
    """__setstate__ should work with older version pickled data"""
    import pickle
    import sys
    lazy = LazyRegex()
    state = lazy.__getstate__()
    state.setdefault('args', ())
    pickle_state = pickle.dumps(state, 2)
    lazy2 = LazyRegex()
    lazy2.__setstate__(state)
    lazy2.__setstate__(pickle.loads(pickle_state))
    if sys.version_info[0] >= 3:
        # __getstate__ no longer returns a dict, so this fails
        lazy2.__setstate__(state.iteritems())



# Generated at 2022-06-14 06:15:58.097667
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """__str__(self)"""
    p = InvalidPattern('You must supply a pattern')
    # should not raise
    str(p)


# Generated at 2022-06-14 06:16:14.004648
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """__str__ must return an 8-bit string

    https://bugs.launchpad.net/bzr/+bug/595026
    """
    import sys
    if sys.version_info < (2, 5):
        raise TestSkipped('test for python versions >= 2.5.')
    # use re.compile to raise an InvalidPattern
    from bzrlib.trace import note
    try:
        re.compile(u'[\U0001f422]')
    except InvalidPattern as e:
        e.msg = u'unicode string'
        note(e)
        # __str__() must return an 8-bit string
        assert type(str(e)) is str

# Generated at 2022-06-14 06:16:24.901671
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    from bzrlib.i18n import gettext
    # Next test fails with WrongException
    from bzrlib._lazy_regex import InvalidPattern
    from bzrlib._lazy_regex import LazyRegex
    from bzrlib._lazy_regex import re
    from bzrlib._lazy_regex import lazy_compile
    # Next test fails with WrongException
    gettext('foo')
    # Next test fails with WrongException
    re
    # Next test fails with WrongException
    InvalidPattern
    # Next test fails with WrongException
    LazyRegex
    # Next test fails with WrongException
    lazy_compile
    # Next test fails with WrongException
    InvalidPattern._fmt
    # Next test fails with WrongException
    InvalidPattern.__module__
    # Next test fails

# Generated at 2022-06-14 06:16:38.338967
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    from bzrlib.i18n import gettext
    from bzrlib.i18n import fix_user_encoding
    from bzrlib.i18n import lazy_gettext
    from bzrlib.i18n import ugettext
    e = InvalidPattern("foo")
    e._preformatted_string = 'foo\n'
    assert str(e) == "foo\n"
    assert unicode(e) == u'foo\n'
    e = InvalidPattern("foo")
    e._fmt = 'foo'
    assert str(e) == "foo"
    assert unicode(e) == u'foo'
    e = InvalidPattern("foo")
    e._fmt = 'foo %(somevar)s'
    e.somevar = "bar"
    assert str(e)

# Generated at 2022-06-14 06:16:48.349278
# Unit test for method __getattr__ of class LazyRegex
def test_LazyRegex___getattr__():
    import random
    import string
    import re

    # Create a string containing random chars
    str = ''.join(random.choice(string.ascii_letters) for _ in range(10))

    # Create two LazyRegex proxies with different patterns and register
    # them as attributes of the object pattern
    pattern = LazyRegex(('abc',), {})
    allow_str = LazyRegex((str,), {})
    setattr(pattern, str, allow_str)

    # Try to access the second proxy from the first one by getting its
    # attribute with the name of the pattern of the second one
    assert pattern.__getattr__(str) is allow_str

    # Now try to access a non-existent attribute of the second proxy
    # through the first proxy
    def non_existent_attribute():
        pattern.__

# Generated at 2022-06-14 06:16:59.034233
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Test method __unicode__ of class InvalidPattern.

    This also test method __str__.
    """
    class TestInvalidPattern(InvalidPattern):
        _fmt = u'Test InvalidPattern %(foo)s'


# Generated at 2022-06-14 06:17:06.647063
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """__unicode__ of InvalidPattern should return a unicode object.

    This is used for printing messages to the user, for example when using
    the built-in help command.
    """
    e = InvalidPattern('Invalid pattern(s) found. No command supplied.')
    uh = unicode(e)
    assert isinstance(uh, unicode)
    assert not isinstance(uh, str)



# Generated at 2022-06-14 06:17:12.591471
# Unit test for method __getattr__ of class LazyRegex
def test_LazyRegex___getattr__():
    """__getattr__ of LazyRegex must compile the regex if it has not been done yet.
    """
    # compile is not called yet.
    l = LazyRegex(['^foo'])
    assert l._real_regex is None
    # compile is called when getattr.
    l.match('foo')
    assert l._real_regex is not None

# Generated at 2022-06-14 06:17:22.382327
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """InvalidPattern.__unicode__ must return a unicode object"""
    from bzrlib.i18n import gettext
    # Test with a str
    i = InvalidPattern(gettext('a str'))
    u = i.__unicode__()
    if not isinstance(u, unicode):
        raise AssertionError('%s is not a unicode object' % u)
    # Test with an unicode string
    i = InvalidPattern(gettext('a unicode'))
    u = i.__unicode__()
    if not isinstance(u, unicode):
        raise AssertionError('%s is not a unicode object' % u)


# Generated at 2022-06-14 06:17:26.787519
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    error = InvalidPattern(u'My Message 1')

# Generated at 2022-06-14 06:17:32.525593
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """Test that InvalidPattern.__str__() returns a str object, not a
    unicode object.
    """
    e = InvalidPattern('test')
    # __str__() should always return a str object, never a unicode object,
    # because the traceback module expects a str object, not a unicode object.
    assert isinstance(str(e), str)

# Generated at 2022-06-14 06:17:41.159634
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    pattern = InvalidPattern("Invalid pattern 123")
    assert str(pattern) == 'Invalid pattern(s) found. "Invalid pattern 123"'
    pattern = InvalidPattern("")
    assert str(pattern) == 'Invalid pattern(s) found. ""'
    # TODO: Add more tests

# Generated at 2022-06-14 06:17:52.500755
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """Test for method __str__ of class InvalidPattern"""
    inst = InvalidPattern('Invalid pattern(s) found. %(msg)s')
    assert inst.__str__() == 'Unprintable exception InvalidPattern: dict={}, fmt=%(msg)s, error=None'
    inst = InvalidPattern('Invalid pattern(s) found.')
    assert inst.__str__() == 'Unprintable exception InvalidPattern: dict={}, fmt=None, error=None'
    # TODO: re.error is not exported
    #try:
    #    inst = InvalidPattern('Invalid pattern(s) found. %(msg)s')
    #    inst._real_re_compile('\a')
    #except re.error as e:
    #    assert inst.__str__() == 'Invalid pattern(s) found. \a ' +

# Generated at 2022-06-14 06:18:02.830890
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """InvalidPattern.__unicode__() raises TypeError if __unicode__ is not
    implemented by subclass.
    """
    class InvalidPatternSubclass(InvalidPattern):
        def _get_format_string(self):
            return None
    e = InvalidPatternSubclass('abc')
    ex = TypeError('__str__ returned non-string (type NoneType)', object())

# Generated at 2022-06-14 06:18:11.685850
# Unit test for method __getattr__ of class LazyRegex
def test_LazyRegex___getattr__():
    """test LazyRegex.__getattr__()

    LazyRegex.__getattr__() returns the attribute named by 'attr' of the
    real regex. If the real regex has not been compiled yet, first
    compile it.
    """

    # Construct a real regex, (lazy regex does not compile regex, it just
    # constructs the object).
    r = _real_re_compile('^(.*)$')
    flags = r.flags

    # Construct a lazy regex.
    l = lazy_compile('^(.*)$', flags)

    # Lazy regex's attribute 'flags' will be the same as that of the real
    # regex.
    eq(r.flags, l.flags)

    # Lazy regex has not been compiled yet, so l.match() and r.match()
    # should return

# Generated at 2022-06-14 06:18:24.646138
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    from bzrlib.i18n import gettext
    e = InvalidPattern('foo')
    # XXX: This test seems a bit fragile.
    # Check that we are using the gettext.gettext
    # to create the string, by checking that the string is not
    # the one we just created.
    # Possibly we could check that the generated string
    # is the one returned by gettext.gettext
    # or simply check that _format returns a unicode object
    # which contains a string returned by _get_format_string
    # or a default string which doesn't contain _fmt
    # see also _get_format_string
    assert u'foo' != e.__unicode__()
    # Check that we are calling gettext with a unicode object
    gettext_mock = lambda x: x

# Generated at 2022-06-14 06:18:36.946900
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """Test what happens when InvalidPattern is cast to unicode or string"""
    # Create an InvalidPattern
    exc = InvalidPattern('foo')
    # __str__() should always return a 'str' object
    assert isinstance(str(exc), str)
    # __unicode__() should return a unicode object
    assert isinstance(unicode(exc), unicode)
    # Reimporting bzrlib updates logging to use gettext, which requires
    # localisation. In other words, our InvalidPattern '_fmt' must be a str.
    from bzrlib.i18n import (
        gettext,
        )
    # no _preformatted_string was passed, so it must use '_fmt'
    # this happens when the app is run without localisation

# Generated at 2022-06-14 06:18:46.398248
# Unit test for method __getattr__ of class LazyRegex
def test_LazyRegex___getattr__():
    """Test for exceptions in __getattr__"""
    # This test is only to check that we correctly get the exceptions
    # raised by the real object and not our proxy
    try:
        LazyRegex(args=("a+",)).match("ab")
    except Exception as e:
        # Make sure we get an exception of type re.error and not LazyRegex
        e_type = e.__class__.__name__
        if e_type == "LazyRegex":
            raise AssertionError("Exception raised is of type LazyRegex:"
                                 " %s" % e)

# Generated at 2022-06-14 06:18:58.055305
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Check InvalidPattern.__unicode__ exists and doesn't raise."""

# Generated at 2022-06-14 06:19:04.840647
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """__unicode__ and __str__ of InvalidPattern return str representation
    of the exception.
    """
    e = InvalidPattern('foo')
    u = u'Invalid pattern(s) found. foo'
    s = 'Invalid pattern(s) found. foo'
    assert e.__unicode__() == u
    assert e.__str__() == s



# Generated at 2022-06-14 06:19:12.241726
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """
    Test that the method __str__ of the class InvalidPattern
    returns a str object and not a unicode object.
    """
    # FIXME: This test fails, because the str object obtained
    # by calling __str__ returns a unicode object.
    # That is not a problem, because InvalidPattern
    # contains a __unicode__ method that does the conversion
    # to unicode.
    err = InvalidPattern(msg='foo')
    str_err = err.__str__()
    assert isinstance(str_err, str)

# Generated at 2022-06-14 06:19:22.573241
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """__unicode__ should always return a unicode object

    see bug #34846
    """
    u = InvalidPattern('a message').__unicode__()
    assert isinstance(u, unicode)



# Generated at 2022-06-14 06:19:34.815738
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """Test method __str__ of class InvalidPattern"""
    #Bind the message to the instance
    class MyException(InvalidPattern):
        _fmt = 'Message: %(msg)s'
    msg='my_error'
    my_exc = MyException(msg)
    # test the string representation of MyException
    assert '%s'%my_exc == 'Message: my_error'

    #Change the message and check if the new message is returned
    msg='new_error'
    my_exc.msg = msg
    assert '%s'%my_exc == 'Message: new_error'

    #Bind a preformatted message
    class MyException2(InvalidPattern): pass
    my_exc = MyException2('msg')
    my_exc._preformatted_string = 'Message: %(msg)s'

# Generated at 2022-06-14 06:19:46.573250
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """This is a test for the method __str__ of class InvalidPattern.

    Because it does not make a lot of sense to add a new unit test just for
    a single method, we add some other tests for other methods of the class
    InvalidPattern at the same time.
    """
    from bzrlib.tests import TestCase

    class TestInvalidPattern(TestCase):

        def test___str__(self):
            e = InvalidPattern('message')
            inv_argument = InvalidArgument('reason', details='details')
            e._preformatted_string = 'preformatted'
            # test __str__ with a unicode message
            unicode_message = unicode('unicode message')
            e.msg = unicode_message
            self.assertIsInstance(str(e), str)

# Generated at 2022-06-14 06:19:54.155785
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """InvalidPattern.__str__ should return a str object"""
    try:
        raise InvalidPattern('foo')
    except InvalidPattern as e:
        if isinstance(e.__str__(), str):
            # Test is successful
            return
        else:
            raise AssertionError('InvalidPattern.__str__ should return a str '
                                 'object')



# Generated at 2022-06-14 06:20:04.809536
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """Test of method __str__ of class InvalidPattern.

    Notes:
    - This test is not testing the implementation, but only the
      interface.
    - Method __str__ must return a str object (never a unicode object).
    """
    from bzrlib.i18n import gettext
    from bzrlib.i18n import gettext_for_locale

    def check_str_object(string):
        """Check that a given string is of type str.

        :param string: The string to check.
        :raise AssertionError: If the given string is not a str object.
        """
        if not isinstance(string, str):
            raise AssertionError("Expected a str object, got a %r object"
                                 % type(string))

    original_gettext = gettext
    original_

# Generated at 2022-06-14 06:20:10.816362
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """This test checks that InvalidPattern.__str__() returns a
    "unicode" object.
    """
    import sys
    if sys.version_info[0] > 2:
        assert isinstance(InvalidPattern('msg'), str)
    else:
        assert isinstance(InvalidPattern('msg'), unicode)

# Generated at 2022-06-14 06:20:15.664920
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """__unicode__ methods should return a unicode string"""
    error = InvalidPattern('The pattern is invalid')
    result = unicode(error)
    assert isinstance(result, unicode), \
        'Result should be a unicode string'


# Generated at 2022-06-14 06:20:20.694654
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """
    test_InvalidPattern___str__
    The method '__str__' convert an InvalidPattern object in a string.
    It is useful for print InvalidPattern object.
    """
    msg= 'Invalid patter'
    invalid_pattern_object= InvalidPattern(msg)
    assert msg in unicode(invalid_pattern_object)
    assert msg in str(invalid_pattern_object)

# Generated at 2022-06-14 06:20:30.530723
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    # test for a unicode object
    msg = u'unicode message'
    exc = InvalidPattern(msg)
    assert isinstance(exc.__unicode__(), unicode)
    # test for a str object
    msg = 'ascii message'
    exc = InvalidPattern(msg)
    assert isinstance(exc.__unicode__(), unicode)
    # test for a non standard object
    msg = ['strange', 'message']
    exc = InvalidPattern(msg)
    assert isinstance(exc.__unicode__(), unicode)

# Generated at 2022-06-14 06:20:40.195387
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """Test __str__ method of InvalidPattern class"""

    # Test case with a preformatted message
    exc = InvalidPattern('message')
    exc._preformatted_string = u'preformatted'
    assert exc.__str__() == 'preformatted'

    # Test that UnicodeEncodeErrors are handled correctly
    # (setting _fmt will cause InvalidPattern to use _get_format_string
    #  that will format the message using _fmt)
    exc = InvalidPattern(u'message')
    exc._fmt = u'%(msg)s'
    assert exc.__str__() == 'message'

    # Test that UnicodeEncodeErrors are handled correctly
    # (setting _fmt will cause InvalidPattern to use _get_format_string
    #  that will format the message using _fmt)
    exc

# Generated at 2022-06-14 06:20:51.219091
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    unicode_pattern = unicode('[\u0000-\uffff]+')
    # Simulate an InvalidRegex exception with a unicode pattern
    e = InvalidPattern(unicode_pattern)

    # str(e) must return a str object, not unicode
    assert isinstance(str(e), str), "__str__() must return a str not unicode"


# Generated at 2022-06-14 06:20:58.106295
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    from bzrlib.tests import TestCase
    class Test(TestCase):

        def test_InvalidPattern___unicode__(self):
            expected = u'Invalid pattern(s) found. "abc"[3:1]'
            t = InvalidPattern("\"abc\"[3:1]")
            self.assertEqual(expected, unicode(t))

    Test('test_InvalidPattern___unicode__').run()

# Generated at 2022-06-14 06:21:10.850583
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Some simple tests for InvalidPattern._format()."""
    from bzrlib.i18n import ugettext
    from bzrlib.i18n import set_translations_dir
    from bzrlib.i18n import push_translation
    from bzrlib.i18n import pop_translation

    # The error class has a _fmt string containing a single "%()s" string
    # format specifier so we can format the instance into a unicode string
    # containing the string 'Invalid pattern(s) found. %(msg)s'
    # (i.e. the string we see if the _fmt format string is missing).
    error = InvalidPattern('xxx')
    got = unicode(error)
    want = u'Invalid pattern(s) found. xxx'
    if want != got:
        raise

# Generated at 2022-06-14 06:21:14.950887
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """ Test method __unicode__ of class InvalidPattern """
    try:
        raise InvalidPattern("message")
    except InvalidPattern as e:
        print(e)
        print(str(e)) # should be the same as the next line
        print(e.__str__())

# Generated at 2022-06-14 06:21:28.109108
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """test method InvalidPattern.__unicode__()"""
    import re
    import StringIO

    dummy_regex = "dummy"
    valid_regex = "^[0-9a-zA-Z._'+-]+$"

    # Check that re.compile throws a InvalidPattern exception with a
    # valid (ascii only) message
    try:
        re.compile(dummy_regex)
    except InvalidPattern as e:
        # Check that __unicode__() returns a unicode object
        assert isinstance(unicode(e), unicode)

        # Check that __unicode__() returns a valid message
        assert "invalid" in unicode(e).lower()
        assert unicode(e)[0] == '"'
        assert unicode(e)[-1] == '"'

    #

# Generated at 2022-06-14 06:21:37.837066
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """Test method __str__ of class InvalidPattern"""
    pattern = InvalidPattern(msg='Invalid')
    pattern._preformatted_string = 'preformatted'
    # with _preformatted_string
    assert str(pattern) == 'preformatted'
    pattern._preformatted_string = 'preformatted with %(msg)s: %(msg)s'
    # with _preformatted_string with formatting
    assert str(pattern) == 'preformatted with Invalid: Invalid'
    del pattern._preformatted_string
    # without _preformatted_string
    assert str(pattern) == 'Invalid'
    # with fmt
    pattern._fmt = 'Invalid pattern(s) found. %(msg)s'
    assert str(pattern) == 'Invalid'
    # with unknown fmt

# Generated at 2022-06-14 06:21:47.764336
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """InvalidPattern.__unicode__

    The __unicode__ method is used by str(exception) and unicode(exception).
    """
    exception = InvalidPattern(u'A pattern error.')
    exception._fmt = u'Invalid pattern %(msg)s'
    expected = u'Invalid pattern A pattern error.'
    result = unicode(exception)
    assert result == expected, (result, expected)
    #
    # __unicode__() should always return a 'unicode' object.
    assert isinstance(result, unicode)

# Generated at 2022-06-14 06:22:01.117493
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    import unittest
    from bzrlib.tests import TestCase

    class Test__str__(TestCase):
        """Unit test for method __str__ of class InvalidPattern."""

        def test_unicode_str(self):
            try:
                raise InvalidPattern(u'u')
            except InvalidPattern as e:
                self.assertEqual(str(e), 'u')
                self.assertEqual(unicode(e), u'u')

        def test_str_str(self):
            try:
                raise InvalidPattern('u')
            except InvalidPattern as e:
                self.assertEqual(str(e), 'u')
                self.assertEqual(unicode(e), u'u')


# Generated at 2022-06-14 06:22:10.958729
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """InvalidPattern class must return a valid string"""
    from bzrlib.i18n import ustr
    from bzrlib.i18n import gettext

    original_string = "Some original value"
    e = InvalidPattern(original_string)
    # Case 1: class attribute '_fmt' is ascii
    e._fmt = 'Some %(msg)s value'
    assert str(e) == 'Some ' + original_string + ' value'
    assert unicode(e) == u'Some ' + ustr(original_string) + u' value'
    # Case 2: class attribute '_fmt' is unicode
    e._fmt = u'Some %(msg)s value'
    assert unicode(e) == u'Some ' + ustr(original_string) + u' value'


# Generated at 2022-06-14 06:22:21.926201
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    from bzrlib.i18n import gettext

    class IP(InvalidPattern):
        # We need a _fmt string to test the behaviour of method
        # __unicode__ of class InvalidPattern.
        _fmt = 'Don\'t %(msg)s'

    # Check that it returns a unicode object
    assert isinstance(IP(u'fear').__str__(), unicode)
    assert isinstance(IP('fear').__str__(), unicode)

    # Check the behaviour of the _get_format_string method
    ip = IP(u'fear')
    assert ip._get_format_string() == gettext(ip._fmt)

    # Check the behaviour of the _format method
    ip = IP(u'fear')

# Generated at 2022-06-14 06:22:39.704453
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    # __str__ must return a str.
    from bzrlib._key_value_pairs import KeyValuePairs
    from bzrlib.trace import mutter

    # Mutter to remove the warning about not being utf-8
    mutter("\xe2")
    e = InvalidPattern("\xe2")
    as_dict = KeyValuePairs(__class__=InvalidPattern,
                            _preformatted_string=None,
                            _fmt="%(msg)s",
                            msg=u"\xe2")
    assert str(e) == str(as_dict)



# Generated at 2022-06-14 06:22:53.439082
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """__str__ should never return unicode."""
    import os.path
    import sys

    # Test if __str__ returns unicode or not
    if sys.version_info[0] == 3:
        def is_string(s):
            return isinstance(s, str)
    else:
        def is_string(s):
            return isinstance(s, str) or isinstance(s, unicode)

    # Test basic case
    e = InvalidPattern('dummy')
    s = str(e)
    assert is_string(s)
    assert s == "Invalid pattern(s) found. dummy"

    # Test i18n case
    e = InvalidPattern('dummy')
    e._preformatted_string = 'A'
    s = str(e)
    assert is_string(s)

# Generated at 2022-06-14 06:23:05.153002
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """The method __unicode__ of class InvalidPattern must return a unicode
    object.
    """
    # preformatted message
    ip = InvalidPattern(msg=u'Test')
    ip._preformatted_string = u'preformatted message'
    assert unicode(ip) == u'preformatted message'
    # the message is not set for any reason
    ip = InvalidPattern(msg=None)
    assert unicode(ip).startswith(u'Unprintable exception InvalidPattern')
    # the message is set
    ip = InvalidPattern(msg='Test msg')
    assert unicode(ip) == u'Test msg'
    # the message is set
    ip = InvalidPattern(msg=u'Another \u0420\u043e\u0441\u0441\u0438\u044f')
   

# Generated at 2022-06-14 06:23:10.172636
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Test for method __unicode__ of class InvalidPattern."""
    from bzrlib.controldir import ControlDir
    try:
        ControlDir.find_repository()
    except Exception as e:
        if isinstance(InvalidPattern, e):
            unicode(e)
        else:
            raise

# Generated at 2022-06-14 06:23:21.104698
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Test method __unicode__ of class InvalidPattern.

    This will test the method __unicode__ which is used as a fallback when
    there is an error loading the translation of an exception.
    """
    # bind to a 'str' object
    s = unicode(u'foo')
    e = InvalidPattern(s)
    # __unicode__ must return a unicode object
    u = unicode(e)
    # u must be equal to s
    assert isinstance(u, unicode)
    # The previous test does not guarantee that u is equal to s
    # because u could be a different equivalent value
    assert u == s
    # Now bind to a 'unicode' object
    u = u'bar'
    e = InvalidPattern(u)
    # __unicode__ must return a unicode object
    u = unic

# Generated at 2022-06-14 06:23:28.336500
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    from bzrlib.tests import TestCase
    from bzrlib.i18n import gettext

    class TestCaseWithGettext(TestCase):
        def _get_format_string(self):
            return gettext('%(a)s')

    test_case = TestCaseWithGettext()
    test_case.a = u'some text'
    error = InvalidPattern(test_case)
    # __str__ should return an ascii string encoding an unicode one
    self.assertIsInstance(str(error), str)
    self.assertEqual('u\'some text\'', str(error))

# Generated at 2022-06-14 06:23:40.139216
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    import unittest

    class TestInvalidPattern(unittest.TestCase):

        def test_InvalidPattern___str__(self):
            import re

            # None of the patterns are valid so the patterns are all
            # 'invalid'
            patterns = [
                '',
                '*',
                ']',
                '[',
                '[',
                '[',
                '[',
                '[',
                '[',
                '[',
                '[',
                '[',
                '[',
                '[',
            ]
            for (i, p) in enumerate(patterns):
                try:
                    re.compile(p)
                except InvalidPattern as e:
                    i = e
                    self.assertIsInstance(i, InvalidPattern)
                    self.assertIsInstance(str(i), str)

# Generated at 2022-06-14 06:23:45.674157
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    from cStringIO import StringIO
    from bzrlib.trace import (
        MutableConfig,
        Config,
        mutter_callsite,
        mutter_stream,
        show_error,
        show_warning,
        show_exception,
        )
    errors_stream = StringIO()
    # Redefine show_error to write to errors_stream
    old_show_error = show_error
    def show_error(msg, *args, **kwargs):
        msg = msg % args
        errors_stream.write(msg + '\n')
        old_show_error(msg, *args, **kwargs)
    mutter_callsite = 'unit test for InvalidPattern.__unicode__'
    mutter_stream = StringIO()
    mutter_config = MutableConfig()


# Generated at 2022-06-14 06:23:59.121233
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():

    # all of these should work, because they don't access other attrs
    # (only _fmt and __dict__).
    class SimpleException(InvalidPattern):
        _fmt = 'Simple message with no attrs: %(msg)s'
    assert unicode(SimpleException('a')) == u"Simple message with no attrs: a"

    class SimpleException(InvalidPattern):
        _fmt = 'Simple message with no attrs: %(rmsg)s'
    assert unicode(SimpleException('a')) == u"Simple message with no attrs: a"

    class SimpleException(InvalidPattern):
        _fmt = 'Simple message with no attrs: %(ms)s'
    assert unicode(SimpleException('a')) == u"Simple message with no attrs: a"


# Generated at 2022-06-14 06:24:05.201499
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """__str__ should return an str object, not an unicode object
    """
    e = InvalidPattern("some message")
    s = str(e)
    assert isinstance(s, str)
    u = unicode(e)
    assert isinstance(u, unicode)

# Generated at 2022-06-14 06:24:26.250173
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """Unit test for method __str__ of class InvalidPattern.

    Called by:
    Test invalid pattern exceptions
    """
    msg = 'expected non-empty pattern'
    error = InvalidPattern(msg)
    # Test that an InvalidPattern can be converted to a string.
    # This is what happens when an InvalidPattern is passed to a trace function
    # and converted to a string.
    text = str(error)
    # Test that the message is present in the string.
    if not msg in text:
        raise AssertionError(
            "Expected message " + msg + " to be in " + text)

# Generated at 2022-06-14 06:24:34.018012
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Test method InvalidPattern.__unicode__()
    
    This is a test for a rather obscure situation: the _fmt attribute is a non
    ascii unicode string, and the current locale encoding is not utf8.

    It is not much of a problem in practice because non-ascii unicode strings
    are only used for translations, and the _fmt attribute is defined in this
    module, so the whole module is translated.
    """
    class AnInvalidPattern(InvalidPattern):
        _fmt = u"\xe9 pattern(s) found"

    ex = AnInvalidPattern(u"\xe9")
    utf8_encoding = "utf8"
    assert isinstance(ex._fmt, unicode)
    assert isinstance(ex._fmt, str)