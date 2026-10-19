

# Generated at 2022-06-14 06:14:47.883067
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    from bzrlib.i18n import gettext
    msg = 'This is a test'
    e = InvalidPattern('%s' % msg)
    # ensure the exception is localed
    gettext(msg)
    assert str(e) == msg
    assert unicode(e) == msg

# Install the real re.compile function in the global scope so that it is
# available to tests.
__all__ = ['lazy_compile', '_real_re_compile']

# Generated at 2022-06-14 06:14:53.130756
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    import doctest
    from bzrlib import tests
    doctest.testmod(tests, optionflags=doctest.NORMALIZE_WHITESPACE)



# Generated at 2022-06-14 06:15:06.414705
# Unit test for method __setstate__ of class LazyRegex
def test_LazyRegex___setstate__():
    # Create a LazyRegex object
    lz = LazyRegex(('^a$', 0, None))
    # It is not yet compiled
    assert lz._real_regex is None
    assert lz._regex_args == ('^a$', 0, None)
    assert lz._regex_kwargs == {}
    # Compile it
    lz._compile_and_collapse()
    # It is now compiled
    assert lz._real_regex is not None
    # Save its state
    state = lz.__getstate__()
    # Create a new LazyRegex object
    lz = LazyRegex(('^b$', 0, None))
    assert lz._real_regex is None

# Generated at 2022-06-14 06:15:15.535981
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Test method __unicode__ of class InvalidPattern"""
    unicode_string = "a unicode string"
    latin_string = unicode_string.encode("latin1")
    unicode_object = InvalidPattern(unicode_string)
    # test for unicode string
    assert unicode_object == InvalidPattern(unicode(unicode_string))
    # test for latin1 encoded string (converted to unicode)
    assert unicode_object == InvalidPattern(latin_string)

# Generated at 2022-06-14 06:15:26.879105
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Test for InvalidPattern.__unicode__

    This uses an InvalidPattern object that does not contain a format string
    (it contains only a raw string)
    """
    from bzrlib.win32utils import get_user_encoding
    from bzrlib.i18n import u

    s = u'invalid message'
    ip = InvalidPattern(s)
    # This call must not raise an exception
    ustr = unicode(ip)
    assert isinstance(ustr, unicode)
    # We expect that the unicode string contains the raw string
    assert s in ustr
    # If the encoding is not UTF-8, we expect that the str string contains
    # the unicode string encoded in UTF-8

# Generated at 2022-06-14 06:15:35.619155
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    from cStringIO import StringIO
    import sys

    # unicode string message
    err = InvalidPattern(u'\u0B85\u0BB5')
    old_out = sys.stdout
    sys.stdout = StringIO()
    try:
        print(err)
    finally:
        sys.stdout = old_out
    # unicode characters should be printed properly.
    assert(sys.stdout.getvalue() == 'Unprintable exception InvalidPattern: '
                                    'dict={}, fmt=None, error=None\n'.decode('utf8'))

# Generated at 2022-06-14 06:15:44.844346
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """Unit test for method __str__ of class InvalidPattern"""
    def _encoder(obj):
        """An encoder that will return a safe representation of an object."""
        if isinstance(obj, str):
            try:
                return repr(obj).lstrip('u')
            except UnicodeEncodeError:
                return repr(unicode(obj)).lstrip('u')
        elif isinstance(obj, unicode):
            return repr(obj)
        else:
            return repr(obj)
    test_dict = {'msg':'error message...'}
    test_instance = InvalidPattern('error message...')
    test_instance.__dict__ = test_dict
    # Test the property of method __str__
    expected_result = "{'msg':'error message...'}"

# Generated at 2022-06-14 06:15:56.658461
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    import bzrlib.tests
    import gettext
    class Foo(InvalidPattern):
        _fmt = 'There is a %(animal)s in my %(place)s.'
    gettext.install(bzrlib._format._domain, unicode=True)
    foo = Foo('This is a message.')
    foo._preformatted_string = '<preformatted>'
    foo.animal = u'black cat'
    foo.place = u'backyard'
    en_us = gettext.translation(bzrlib._format._domain, 'locale',
                                codeset='UTF-8', fallback=True)

# Generated at 2022-06-14 06:16:03.392281
# Unit test for method __setstate__ of class LazyRegex
def test_LazyRegex___setstate__():
    """__setstate__ restores the LazyRegex"""
    state = {"args": (r'\d$',), "kwargs": {}}
    regex = LazyRegex()
    regex.__setstate__(state)
    regex._compile_and_collapse()
    if regex._real_regex.pattern != state['args'][0]:
        raise AssertionError('restored LazyRegex not correct')

# Generated at 2022-06-14 06:16:14.403225
# Unit test for method __getattr__ of class LazyRegex
def test_LazyRegex___getattr__():
    from bzrlib.tests import TestCase

    class TestClass(TestCase):

        def setUp(self):
            TestCase.setUp(self)
            self.lazy_regex = LazyRegex(args=("b+ ",))

        def test_lazy_regex_returns_compiled_regex(self):
            compiled_regex_pattern = self.lazy_regex._real_re_compile(
                "b+ ").pattern
            self.assertEqual("b+ ", compiled_regex_pattern)

        def test_getattr_returns_compiled_regex_pattern(self):
            compiled_regex_pattern = self.lazy_regex._real_re_compile(
                "b+ ").pattern

# Generated at 2022-06-14 06:16:24.321221
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    assert str(InvalidPattern('test')) == "Invalid pattern(s) found. test"


# FIXME: Move this to a better place. This can't be in the selftest because
# it will break some tests.
_modules_to_fix_compile = ['subvertpy',
    'bzrlib.tests.test_regex', 'bzrlib.osutils']


# Generated at 2022-06-14 06:16:26.068674
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)

# Generated at 2022-06-14 06:16:39.608710
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """Test __str__() method of InvalidPattern class."""
    from bzrlib.i18n import gettext
    original_gettext = bzrlib.i18n.gettext
    bzrlib.i18n.gettext = lambda x: unicode(x)
    try:
        raise InvalidPattern('message')
    except InvalidPattern as e:
        # initial object is of unicode type
        assert isinstance(e, unicode)
        # convert object to str type
        s = str(e)
        assert isinstance(s, str)
        # has to be utf8, not a latin1
        assert s.decode('utf8') == s.decode('latin1')
    finally:
        bzrlib.i18n.gettext = original_gettext

# Generated at 2022-06-14 06:16:46.070156
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """InvalidPattern.__str__ returns a unicode object.

    When __str__(self) is called self._format() must return a unicode object
    else self.msg is unicode.
    """
    # bug 834759
    msg = "Invalid pattern(s) found. 'bar'\n" \
        "Did you forget to escape \\ or to quote it ?"
    e = InvalidPattern(msg)
    assert isinstance(unicode(e), unicode)

# Generated at 2022-06-14 06:16:58.898278
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """Test if InvalidPattern.__str__ returns an expected string.

    This method tests if the InvalidPattern.__str__ returns a string as
    expected. First, it tests the case that the string is set as a
    preformatted string and then it tests the case that the string has to be
    computed before returning it.
    """
    class TestInvalidPattern(InvalidPattern):
        """Class to test __str__ method of InvalidPattern."""

        def __init__(self):
            self._preformatted_string = 'A preformatted string'

    ip = TestInvalidPattern()
    ip1 = InvalidPattern('I am a test')
    assert str(ip) == 'A preformatted string'
    assert str(ip1) == 'Invalid pattern(s) found. I am a test'

# Generated at 2022-06-14 06:17:03.499833
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """Test for method __str__ of class InvalidPattern"""
    import doctest
    doctest.testmod(name="test_InvalidPattern___str__", optionflags=doctest.ELLIPSIS)

# Generated at 2022-06-14 06:17:11.112590
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """InvalidPattern.__unicode__ should succeed when it receives any
    characters.
    """
    error = InvalidPattern('foo')
    unicode(error)
    error = InvalidPattern(u'\xe9')
    unicode(error)
    error = InvalidPattern('\xe9')
    unicode(error)
    error = InvalidPattern(u'\xe9'.encode('utf8'))
    unicode(error)

# Generated at 2022-06-14 06:17:18.556387
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    import sys
    if sys.version_info[0] < 3:
        from StringIO import StringIO
    else:
        from io import StringIO
    import bzrlib.trace

    # We need to capture stderr because this error is reported to it
    stderr = StringIO()
    bzrlib.trace.stderr_writer = stderr

    # Test unicode() under py2
    if sys.version_info[0] < 3:
        try:
            raise InvalidPattern('pattern')
        except InvalidPattern:
            error = sys.exc_info()[1]
        # Test that unicode() is called
        if isinstance(error, str):
            raise AssertionError(
                'unicode() is not called by the code or by the exception')
        # Test that the error message is send

# Generated at 2022-06-14 06:17:25.062791
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """InvalidPatern.__unicode__() returns a unicode object"""
    e = InvalidPattern('Error message')
    s = unicode(e)
    if not isinstance(s, unicode):
        raise TypeError("InvalidPattern.__unicode__() does not return a "
                        "unicode object")


# Generated at 2022-06-14 06:17:28.613305
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    from bzrlib.i18n import gettext
    s = 'Invalid regular expression: unknown property name after \\\\. - \\\\%'
    gettext(s)

# Generated at 2022-06-14 06:17:39.503725
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Test that InvalidPattern can be converted into unicode."""

    # Create an instance of InvalidPattern without specifying a 'msg'
    # attribute.
    i = InvalidPattern(msg=None)

    # Convert it into a unicode object.
    u = unicode(i)

    # Test that the attribute 'msg' is None.
    assert ('msg' in u and u['msg'] is None) is False

# Generated at 2022-06-14 06:17:42.596139
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """A method __unicode__ of class InvalidPattern should return an unicode
    object"""
    err = InvalidPattern("Invalid regex 'foo'")
    obj = unicode(err)
    assert isinstance(obj, unicode)



# Generated at 2022-06-14 06:17:49.282797
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """Unit test for method __str__ of class InvalidPattern.

    This test ensures that InvalidPattern message is decoded
    to unicode and encoded to string when the message contains
    non-ascii characters.
    """
    inst = InvalidPattern(unicode('foo \xc3\xa2\xc2\x80\xc2\x99 bar', 'utf8'))
    try:
        str(inst)
    except UnicodeDecodeError:
        # No exception raised
        pass
    else:
        raise AssertionError('Expected UnicodeDecodeError')
    try:
        unicode(inst)
    except UnicodeDecodeError:
        raise AssertionError('Expected no UnicodeDecodeError')

# Generated at 2022-06-14 06:17:54.662491
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """Test the method __str__ of class InvalidPattern."""
    exc = InvalidPattern(u"This is an error message")
    # __str__ must return a str
    assert isinstance(str(exc), str)
    assert str(exc) == "Invalid pattern(s) found. This is an error message"

# Generated at 2022-06-14 06:17:59.708363
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    # InvalidPattern should return a unicode object
    err = InvalidPattern(u"This is an error message")
    assert(isinstance(err.__unicode__(), unicode))
    assert(isinstance(unicode(err), unicode))
    assert(isinstance(err.__str__(), str))
    assert(isinstance(str(err), str))
    # FIXME: More tests need to be added to test InputPattern in more examples.


# Generated at 2022-06-14 06:18:08.530044
# Unit test for method __getattr__ of class LazyRegex
def test_LazyRegex___getattr__():
    """Test __getattr__ of class LazyRegex

    __getattr__ should compile the real regex, which has the method
    requested, then return the method from the real regex.
    """
    lr = LazyRegex()
    # Get a method which is not present on the proxy object
    # In the case of a real regex, this is usually a method on the
    # _sre.SRE_Pattern object.
    sce = lr.search
    # This should actually be the same object as returned by
    # the real compiled object
    assert str(sce) == str(_real_re_compile('(a)').search('abcdef'))

# Generated at 2022-06-14 06:18:13.971269
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    e = InvalidPattern('This is my message')
    assert type(unicode(e)) is unicode
    e._preformatted_string = u'Test\u1234'
    assert type(unicode(e)) is unicode
    e._preformatted_string = 'Test\xc2\xa2'
    assert type(unicode(e)) is unicode

# Generated at 2022-06-14 06:18:19.636856
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    msg = u"abc \u1234 def"
    e = InvalidPattern(msg)
    assert msg == unicode(e)
    s = str(e)
    assert isinstance(s, str)
    # Check that we can convert the str back to unicode.
    assert msg == s.decode('utf-8')

# Generated at 2022-06-14 06:18:28.792094
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Test InvalidPattern.__unicode__"""
    # Test 1: check that if format string exists, it is used.
    # fmt is a usual string and not a unicode string.
    #
    # Here we use a string with a character with codepoint > 127
    # (U+00C0). This tests that the string is converted to a unicode
    # string first.
    class MyException(InvalidPattern):
        _fmt = "Test1: foo bar." + chr(0x00C0)
    e = MyException('message 1')
    u = unicode(e)
    if not (type(u) is unicode and u.__class__ is unicode):
        raise AssertionError(
            "__unicode__ does not return a 'unicode' object")

# Generated at 2022-06-14 06:18:33.862279
# Unit test for method __getattr__ of class LazyRegex
def test_LazyRegex___getattr__():
    """__getattr__() must use __getattr__ from compiled regex."""
    s = "abc"
    p = LazyRegex((s, 0))
    assert (p.pattern == s)
    assert (p.match(s).group(0) == s)

# Generated at 2022-06-14 06:18:41.497345
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """Make sure the __str__ returns a str object, not unicode.

    This avoids that the caller has to decode it.
    """
    assert isinstance(InvalidPattern('a'), str)

# Generated at 2022-06-14 06:18:45.479503
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """__str__ method of InvalidPattern should return a str"""

    error = InvalidPattern('Test')
    s = str(error)
    assert isinstance(s, str)


# Generated at 2022-06-14 06:18:57.187487
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Ensure that the InvalidPattern can be converted to unicode.
    """
    from bzrlib import errors
    from bzrlib.i18n import gettext
    # Gettext is imported via the branch module, so we need to ensure that the
    # module is imported to ensure that the gettext metadata is registered.
    # TODO: Fix the circular import.
    import bzrlib.branch
    class TestInvalidPattern(errors.InvalidPattern):

        _fmt = 'Test invalid pattern (%%(msg)s)'

    msg = 'This is a message'
    exc = TestInvalidPattern(msg)
    s = unicode(exc)
    expected = 'Test invalid pattern (%s)' % (msg,)
    assert s == gettext(expected), (s, gettext(expected))

# Generated at 2022-06-14 06:19:10.783367
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """Testing method __str__ of class InvalidPattern"""
    from bzrlib.i18n import gettext
    # Make sure gettext does not translate by default
    e = InvalidPattern('foobar')
    # __str__ should always return a 'str' object
    # never a 'unicode' object.
    eq = __builtins__['eq']
    eq(str(e), 'Unprintable exception InvalidPattern: dict={}, fmt=None, error=None')

    # Test with a pre-formatted message
    e._preformatted_string = 'foobar'
    eq(str(e), 'foobar')

    # Test with a _fmt attribute
    e._preformatted_string = None
    e._fmt = 'foobar'
    eq(str(e), 'foobar')

    # Test with gettext

# Generated at 2022-06-14 06:19:12.321172
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    e = InvalidPattern('foo')
    assert str(e) == 'Invalid pattern(s) found. foo'

# Generated at 2022-06-14 06:19:21.384060
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """Checks __str__ method of class InvalidPattern
    
    The method must return 'unicode' object.
    """
    from bzrlib import errors
    import locale
    locale.setlocale(locale.LC_ALL, "C") # To have ascii output in tests
    exc = errors.InvalidPattern("Test")
    assert isinstance(exc.__str__(), unicode), \
        "Method __str__ returns '%s' instead of 'unicode'" % str(type(exc.__str__()))

# Generated at 2022-06-14 06:19:31.100762
# Unit test for method __getattr__ of class LazyRegex
def test_LazyRegex___getattr__():
    """__getattr__ should return the attribute from the real regex object.

    As the real regex object is created at first by the __getattr__ method
    after the real regex object is created, attributes should be returned
    directly without creating the real regex object again.
    """
    import re

    pattern = "^[0-9]+$"
    p = LazyRegex(args=(pattern,))
    if re.compile(pattern).findall('123') != p.findall('123'):
        raise AssertionError('findall is not equal')



# Generated at 2022-06-14 06:19:35.474419
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    from bzrlib.i18n import gettext
    def _mocked_gettext(s):
        return s
    old_gettext = gettext
    try:
        gettext = _mocked_gettext
        exc = InvalidPattern('msg')
        str_exc = 'Invalid pattern(s) found. msg'
        assert(str(exc) == str_exc)
        assert(exc.msg == 'msg')
        assert(unicode(exc) == str_exc)
        exc.msg = 'second message'
        assert(str(exc) == 'Invalid pattern(s) found. second message')
        assert(exc.msg == 'second message')
        assert(unicode(exc) == 'Invalid pattern(s) found. second message')
    finally:
        gettext = old_gettext

# Generated at 2022-06-14 06:19:43.530822
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """Test method __str__ of class InvalidPattern

    If a string passed to method InvalidPattern constructor can't be
    decoded using the default encoding or is not a unicode object then we
    must still be able to format the exception and we must return a str
    object from method __str__ of the exception.
    """
    def d():
        invalid_pattern = InvalidPattern(
            'abc\xedn'.decode('utf-8').encode('utf-16'))
        return str(invalid_pattern)
    d()

# Generated at 2022-06-14 06:19:52.367579
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    from bzrlib.i18n import gettext
    from bzrlib.i18n import set_default_encoding
    set_default_encoding('ascii')

# Generated at 2022-06-14 06:20:02.129904
# Unit test for method __getattr__ of class LazyRegex
def test_LazyRegex___getattr__():
    """Calling a method on LazyRegex should trigger a real regex compilation"""
    def test():
        regex = LazyRegex((r'\bpatch\b', re.I))
        # we should not be compiled yet
        regex.match('patch')
    test.__name__ = 'LazyRegex___getattr__'
    return test



# Generated at 2022-06-14 06:20:10.600286
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    from bzrlib.tests import TestCase
    from bzrlib.i18n import gettext

    class TestCase(TestCase):

        def test_InvalidPattern___str__(self):
            # Test the method __str__ of class InvalidPattern
            # It should return the same result when the method is called
            # with an unicode value or with a str value.
            msg = 'some valid utf8 message'
            unicode_msg = msg.decode('utf8')
            error1 = InvalidPattern(msg)
            error2 = InvalidPattern(unicode_msg)
            self.assertEqual(gettext(msg), error1.__str__())
            self.assertEqual(gettext(msg), error2.__str__())

# Generated at 2022-06-14 06:20:21.345843
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """__unicode__ and __str__ should return a unicode object and a str object 
    respectively.

    __unicode__ and __str__ should return a unicode and a str object 
    respectively, even in the case where the string contains unicode 
    characters.
    """
    # A 'str' object created from a bytestring shouldn't be unicode-hashable.
    # (don't know why this is so, but it is.)
    text = u'This is a unicode string: \u2603'
    unicode_text = unicode(text, 'utf-8')
    error = InvalidPattern(text)
    # __unicode__ should return a unicode object.
    assert isinstance(unicode(error), unicode)
    assert unicode(error) == unicode_text
    # __str__ should return

# Generated at 2022-06-14 06:20:34.720312
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Test method _InvalidPattern.__unicode__.

    Some variables used in this test:
        u - unicode object
        s - string object
    """
    class IP(InvalidPattern):
        _fmt = u"unicode object %(x)s %(y)s"

    # x and y are unicode objects
    x = u'x'
    y = u'y'
    ip = IP(x=x, y=y)
    u = unicode(ip)
    # u should be a unicode object
    assert isinstance(u, unicode)
    # u should be
    # u"unicode object x y"
    assert u == u"unicode object x y"

    # x and y are string objects
    x = 'x'
    y = 'y'

# Generated at 2022-06-14 06:20:41.667315
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    from bzrlib import _i18n_pyx
    from bzrlib.trace import mutter
    from bzrlib import trace
    from bzrlib.tests import TestCase
    from bzrlib.lazy_regex import InvalidPattern

    # None, str, unicode
    for s in [None, u"a", "a"]:
        assert isinstance(InvalidPattern(s).__unicode__(), unicode)

    # mixed list
    assert isinstance(InvalidPattern([u"a", "b"]).__unicode__(), unicode)

    # mixed tuple
    assert isinstance(InvalidPattern((u"a", "b")).__unicode__(), unicode)

    # mixed dict

# Generated at 2022-06-14 06:20:49.233702
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    import locale
    import sys
    try:
        # tests python using ascii as default encoding
        string = str(InvalidPattern('msg'))
    except UnicodeDecodeError:
        # but some python implementations use utf-8 as default encoding
        string = str(InvalidPattern(u'msg'))
    assert string == 'Invalid pattern(s) found. msg'



# Generated at 2022-06-14 06:20:55.656227
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Test method __unicode__ of class InvalidPattern"""
    from testresources import OptimisingTestSuite
    from bzrlib.tests import TestCase
    from bzrlib.tests.per_interversion import TestCaseWithInterVersions
    # test to check the method returns unicode (utf-8)
    t = TestInvalidPattern___unicode__()
    suite = OptimisingTestSuite()
    suite.addTest(t)
    res = suite.run('')
    if not res.wasSuccessful():
        raise AssertionError("%s failed:\n%s" % (t, res))



# Generated at 2022-06-14 06:21:09.500238
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    class TestException(InvalidPattern):
        _fmt = u'Invalid argument(s): %(msg)s'
    e = TestException(u'unicode string, \u1234\u5678')
    try:
        raise e
    except TestException as e:
        assert str(e) == 'Invalid argument(s): unicode string, ???\u5678'
        assert unicode(e) == u'Invalid argument(s): unicode string, \u1234\u5678'
        assert unicode(e) == u'Invalid argument(s): unicode string, \u1234\u5678'
    e = TestException('ascii string')
    try:
        raise e
    except TestException as e:
        assert str(e) == 'Invalid argument(s): ascii string'
        assert unicode

# Generated at 2022-06-14 06:21:20.662940
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """Ensure that InvalidPattern objects can be converted to a string safely.

    This test makes sure that when e.__str__() is called, it will
    not raise an exception.
    """
    import sys
    if sys.version_info[0] == 2:
        # In Python 2, str and unicode may be the same object
        unicode = unicode
        str = str
    else:
        # In Python 3, __str__() should return a 'str' object and __unicode__()
        # should return a 'unicode' object.
        unicode = str
        str = bytes
    # No format string, so lets put some unicode in the values
    e = InvalidPattern({u'hello': u'world'})
    type(e)._fmt = None
    e._preformatted_string = None

# Generated at 2022-06-14 06:21:32.498958
# Unit test for method __getattr__ of class LazyRegex
def test_LazyRegex___getattr__():

    # Bug #212612: Calling __getattr__ on an uninitialized LazyRegex
    #              raises an AttributeError which is not documented
    #              in the docstrings of LazyRegex.
    #
    #              This test case tries to ensure that the exception is
    #              raised as documented.
    class LazyRegexTestException(Exception):
        pass

    class LazyRegexTest(LazyRegex):
        def _real_re_compile(self, *args, **kwargs):
            raise LazyRegexTestException()

    lazy = LazyRegexTest("../data/README.txt")

# Generated at 2022-06-14 06:21:48.887441
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Testing method __unicode__ of class InvalidPattern.

    Result must be a unicode string.
    """
    unicode_msg = u"a unicode message"
    e = InvalidPattern(unicode_msg)
    uni_msg = e.__unicode__()
    if not isinstance(uni_msg, unicode):
        raise AssertionError(
            "%r is not a unicode string!" % uni_msg)
    if uni_msg != unicode_msg:
        raise AssertionError(
            "unicode msg is not the same as the source: %r != %r" % (
                unicode_msg, uni_msg))


# Generated at 2022-06-14 06:21:58.482055
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """InvalidPattern.__unicode__ should return a unicode object."""
    from bzrlib.i18n import gettext
    gettext("Unprintable exception %s: dict=%r, fmt=%r, error=%r")
    s = unicode('example')
    p = InvalidPattern(s)
    u = p.__unicode__()
    msg = ("__unicode__ of InvalidPattern must return a unicode object,"
           " but it returns a %s object") % type(u)
    assert isinstance(u, unicode), msg



# Generated at 2022-06-14 06:22:09.535908
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    from bzrlib.tests import TestCase
    import sys
    # test ascii only
    class DummyException(Exception):
        __str__ = InvalidPattern._get_format_string
        _fmt = u'DummyException: %(msg)s'

    def p(x):
        """Unicode-safe print function"""
        try:
            return x.encode('ascii')
        except UnicodeError:
            return '<invalid encoding>'

    class TestInvalidPattern(TestCase):

        def test___str__(self):
            """InvalidPattern.__str__ should return a str"""
            s = str(DummyException('ascii'))
            self.assertContainsRe(s, '^DummyException: ascii$')

# Generated at 2022-06-14 06:22:12.548026
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """__unicode__ of InvalidPattern returns string"""
    p = InvalidPattern('foo')
    assert p.__unicode__() == u'foo'



# Generated at 2022-06-14 06:22:16.958097
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """__str__ should return the message in case of unicode error in __unicode__"""
    class UnicodeTest(InvalidPattern):
        def __init__(self):
            self.msg = u'\xac'
    ex = UnicodeTest()
    assert str(ex) == ex._format()

# Generated at 2022-06-14 06:22:21.860680
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    # The functions str and unicode must return a value
    msg = 'Invalid pattern found'
    invalid_pattern = InvalidPattern(msg)
    s = str(invalid_pattern)
    assert isinstance(s, str)
    u = unicode(invalid_pattern)
    assert isinstance(u, unicode)

# Generated at 2022-06-14 06:22:32.131453
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """This test verifies that InvalidPattern is properly formatted.

    There are 3 cases where InvalidPattern is used.

    case 1: msg is a str
    case 2: msg is a unicode object
    case 3: msg has not been specified.

    """
    # Case 1: msg is a str
    pattern = InvalidPattern('Invalid pattern')
    s = unicode(pattern)
    expected = u'Invalid pattern(s) found. Invalid pattern'
    assert s == expected, (s, expected)

    # Case 2: msg is a unicode. No encoding should be done.
    unicode_msg = u'Invalid pattern'
    pattern = InvalidPattern(unicode_msg)
    s = unicode(pattern)
    expected = u'Invalid pattern(s) found. Invalid pattern'
    assert s == expected, (s, expected)

    # Case

# Generated at 2022-06-14 06:22:41.274006
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """Ensure that method InvalidPattern.__str__() works as expected. """
    def check(s):
        """Return True if s is a valid string which meets the requirements
        from the docstring of method InvalidPattern.__str__().
        """

# Generated at 2022-06-14 06:22:54.646515
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """The method __unicode__ for `InvalidPattern` class should return unicode
    object."""
    class DummyInvalidPattern(InvalidPattern):
        _fmt = u'%(msg)s'

    m = _mod_re.match

# Generated at 2022-06-14 06:23:01.265272
# Unit test for method __getattr__ of class LazyRegex
def test_LazyRegex___getattr__():
    """Ensure that the __getattr__ method of the LazyRegex class works as expected.
    """
    from bzrlib.tests import TestCase

    class TestLazyRegexGetAttr(TestCase):

        def test_unknown_attribute(self):
            lazy_regex = LazyRegex()
            self.assertRaises(AttributeError, getattr, lazy_regex, 'unknown')

# Generated at 2022-06-14 06:23:11.299265
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    # bug #532346
    import locale
    import sys
    class Error(Exception):
        pass
    class UnicodeError(UnicodeError, Error):
        pass
    def t(s):
        try:
            u = unicode(s, 'ascii')
        except UnicodeError:
            raise Error
        return u
    try:
        s = '\xc3' # Not UTF-8
        unicode(s, 'utf-8')
    except UnicodeError:
        pass
    else:
        raise AssertionError("Expected UnicodeError")
    err_locale_format = locale.Error
    locale.Error = Error
    err_sys_format = sys.getfilesystemencoding
    sys.getfilesystemencoding = lambda: 'ascii'
    # on some non-ascii platforms we

# Generated at 2022-06-14 06:23:18.569402
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Testing method __unicode__ of class InvalidPattern"""
    m = InvalidPattern('')
    s = unicode(m)
    expected = 'Unprintable exception InvalidPattern: dict={}, ' \
        'fmt=None, error=None'

# Generated at 2022-06-14 06:23:30.514261
# Unit test for method __getattr__ of class LazyRegex
def test_LazyRegex___getattr__():
    """Testing method LazyRegex.__getattr__"""
    # create a new object
    lr = LazyRegex()
    # check if real regex is not None
    if lr._real_regex is not None:
        raise AssertionError('_real_regex should be None')
    # try to get a regex attribute that does not exist, will raise error
    # if regex is not None
    lr.search('')
    # now real regex should be compiled
    if lr._real_regex is None:
        raise AssertionError('_real_regex should not be None, it should' \
            ' have been compiled')
    # try to access a member that we know exists

# Generated at 2022-06-14 06:23:37.841075
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    import sys
    if sys.version_info[0] < 3:
        from bzrlib.tests.indep_bytes import as_bytes_if_unicode
    else:
        from bzrlib.tests.indep_bytes import as_unicode_if_py3
    from bzrlib.tests.blackbox import ExternalBase

    class TestInvalidPattern(ExternalBase):

        def test_simple(self):
            e = InvalidPattern('msg')
            self.assertEqual('Invalid pattern(s) found. msg', str(e))

        def test_format(self):
            e = InvalidPattern(_fmt='msg %(msg)s')
            self.assertEqual('msg msg', str(e))


# Generated at 2022-06-14 06:23:49.990405
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    from bzrlib.i18n import gettext
    from bzrlib.i18n import lazy_gettext
    from bzrlib.i18n import ugettext
    from bzrlib.lazy_regex import InvalidPattern

    class TestInvalidPattern(InvalidPattern):
        _fmt = 'test gettext message'
    _test_msg = 'test'
    _test_exception = TestInvalidPattern(_test_msg)
    assert str(_test_exception) == _test_msg

    _test_exception._preformatted_string = 'test preformatted message'
    assert str(_test_exception) == 'test preformatted message'

    _test_exception._fmt = _test_msg
    assert str(_test_exception) == _test_msg

    _test_exception

# Generated at 2022-06-14 06:23:59.575097
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """__unicode__() must return unicode"""
    from bzrlib.i18n import gettext
    from bzrlib.i18n import set_default_encoding

    set_default_encoding('utf-8')
    invalid_pattern = InvalidPattern(u'\u0401')
    if gettext is not None:
        # Using gettext(), __unicode__() will return unicode.
        assert isinstance(invalid_pattern.__unicode__(), unicode)
    else:
        # Without gettext(), __unicode__() returns a str.
        assert isinstance(invalid_pattern.__unicode__(), str)

# Generated at 2022-06-14 06:24:09.260627
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """__str__ should always return str object."""
    ip = InvalidPattern("test message")
    # __str__ should always return str, even non-ascii message
    assert isinstance(ip.__str__(), str)
    # gettext marker
    ip = InvalidPattern("_(" + repr("test message") + ")")
    # Should be able to convert to unicode and back
    str(ip)
    # __str__ should always return str, even non-ascii message
    assert isinstance(ip.__str__(), str)

# Generated at 2022-06-14 06:24:12.468869
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    msg = 'Pattern has a bad escape'
    e = InvalidPattern(msg)
    assert str(e) == msg
    assert unicode(e) == msg



# Generated at 2022-06-14 06:24:23.103255
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    error = InvalidPattern('Invalid regex: the string "foo" is not a regex')
    try:
        import TestSuite  # noqa: F401
    except ImportError: # happens in bzr-builder
        # If the test suite is not loaded, we don't have messages to extract
        # and we can't display the error message in another language.
        expected = "Invalid pattern(s) found. 'Invalid regex: the string " \
            "\"foo\" is not a regex'"
        assert str(error) == expected
    else:
        from bzrlib.i18n import gettext
        expected = gettext("Invalid pattern(s) found. "
                           "'Invalid regex: the string \"foo\" is not a regex'")
        assert str(error) == expected

# Generated at 2022-06-14 06:24:31.486455
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Test the __unicode__ method of class InvalidPattern.

    Unicode or encoded string should be returned depending on the
    context.
    """
    msg = 'Unprintable exception InvalidPattern: dict=%r, fmt=%r, error=%r'
    e = InvalidPattern('Invalid pattern(s) found. foo')
    u = unicode(e)
    s = str(e)
    assert str(e) == msg % {'msg': 'foo'}