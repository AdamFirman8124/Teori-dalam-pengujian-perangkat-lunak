

# Generated at 2022-06-14 06:14:41.628162
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """Test for method __str__ of class InvalidPattern"""
    # See https://bugs.launchpad.net/bzr/+bug/363881/comments/5
    s = InvalidPattern("").__str__()
    if not isinstance(s, str):
        raise AssertionError("Test failed: method __str__ of class InvalidPattern "\
                             "should return a str")

# Generated at 2022-06-14 06:14:47.873810
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Test __unicode__ of class InvalidPattern."""
    from bzrlib.lazy_regex import InvalidPattern
    result = InvalidPattern('msg').__unicode__()
    # gettext.gettext always returns unicode. Here we expect a string
    # that should contain 'msg'.
    expected = u'Invalid pattern(s) found. msg'
    assert result == expected


# Generated at 2022-06-14 06:14:53.938561
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """Test that InvalidPattern.__str__ works with unicode strings.

    InvalidPattern.__str__ should always return a 'str' object.
    """
    invalid_pattern = InvalidPattern(u"invalid-pattern")
    str(invalid_pattern)

# Generated at 2022-06-14 06:14:57.721146
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    invalid_pattern = InvalidPattern(msg='foo')
    unicode_object = invalid_pattern.__unicode__()
    assert isinstance(unicode_object, unicode)

# Generated at 2022-06-14 06:15:01.109459
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    # Test a simple message string
    e = InvalidPattern(u'hi there')
    assert str(e) == 'hi there'
    assert unicode(e) == 'hi there'

# Generated at 2022-06-14 06:15:05.726405
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    e = InvalidPattern("msg")
    u = unicode(e)
    assert isinstance(u, unicode)
    assert u == "msg"
    e._preformatted_string = "msg2"
    u = unicode(e)
    assert u == "msg2"

# Generated at 2022-06-14 06:15:08.516011
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    msg = 'message'
    e = InvalidPattern(msg)
    assert e.__unicode__() == msg

# Generated at 2022-06-14 06:15:18.868661
# Unit test for function finditer_public
def test_finditer_public():
    """Unit test for function finditer_public.

    Unicode is used to test that finditer_public works
    with unicode strings.
    """
    # Test with string
    result = re.finditer("a", "abba")
    assert(isinstance(result, re.SRE_Match))
    # Test with unicode
    u = u"\xe9\xe9"
    result = re.finditer(u"a", u)
    assert(isinstance(result, re.SRE_Match))
    # Test with LazyRegex
    assert(isinstance(re.finditer(LazyRegex(), u), re.SRE_Match))

# Generated at 2022-06-14 06:15:21.791143
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    error = InvalidPattern('message')
    result = str(error)
    expected = 'Invalid pattern(s) found. message'
    assert result == expected, '%r != %r' % (result, expected)

# Generated at 2022-06-14 06:15:25.605355
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Test for method __unicode__ of class InvalidPattern"""
    invalid_pattern = InvalidPattern('msg')
    assert invalid_pattern.__unicode__() == u'Invalid pattern(s) found. msg'

# Generated at 2022-06-14 06:15:43.144708
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """Test for method __str__ of class InvalidPattern"""
    from bzrlib import tests
    import re
    class TestCase(tests.TestCase):
        def test___str__(self):
            k = InvalidPattern('t')
            self.assertEqual('Invalid pattern(s) found. t', k.__str__())
            self.assertEqual(k.__str__(), str(k))
            self.assertEqual('Invalid pattern(s) found. t', unicode(k))

            def fun(value):
                regex = re.compile(value)

            self.assertRaises(InvalidPattern, fun, '(')
    return TestCase



# Generated at 2022-06-14 06:15:53.480595
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    msg = 'lazy_compile_test'
    f = InvalidPattern(msg)
    try:
        raise f
    except InvalidPattern as e:
        l = e.__unicode__()
        assert isinstance(l, unicode)
        assert msg in l
        # Test that the printed message is different from the message
        # provided to the InvalidPattern constructor
        assert(l != msg)
        #test that .__str__() == .__unicode__().encode('utf8')
        assert e.__str__() == l.encode('utf8')


# TODO: Test the proxy behaviour on _all_ of the attributes and methods on
# the _sre.SRE_Pattern class when we have the apis.

# Generated at 2022-06-14 06:16:00.383194
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    from bzrlib import i18n
    i18n.install()
    try:
        msg = "Not a valid pattern, not a valid pattern."
        invalid = InvalidPattern(msg)
        # Check expected output is equal to message passed
        assert str(invalid) == msg
        # Check output is a string
        assert isinstance(str(invalid), str)
    finally:
        i18n.uninstall()

# Generated at 2022-06-14 06:16:05.802399
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    from bzrlib.i18n import gettext
    gettext.install('bzrlib')
    try:
        e = InvalidPattern(_fmt='%(msg)s')
        e.msg = 'hello'
        assert unicode(e) == u'hello'
    finally:
        gettext.uninstall()



# Generated at 2022-06-14 06:16:15.824560
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Test for method __unicode__ of class InvalidPattern

    Here is the test plan:
    - Do one test for each exception string formating cases supported by
      bzrlib.errors.BzrError.
      - string is for ascii charcters
      - string is for non-ascii characters
      - string has a '%(attr)s' formating argument
      - string has multiple '%(attr)s' formating arguments
      - string has '%(attr)s' and '%' formatting arguments
      - string has unicode string as formating argument
    - Do one test for each supported type of error string.
      - error string is a normal string
      - error string is a unicode string
      - error string is a gettext response
    - Test that the result is always a unicode string
    """

    import b

# Generated at 2022-06-14 06:16:23.075537
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Ensure that InvalidPattern.__unicode__ does not raise an exception"""
    msg = 'something is wrong'
    e = InvalidPattern(msg)
    u = unicode(e)
    if not isinstance(u, unicode):
        raise AssertionError("Expected unicode object but got: %r" % (u,))
    if u == '':
        raise AssertionError("unicode object is empty")

# Generated at 2022-06-14 06:16:31.010825
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Unit test for method __unicode__ of class InvalidPattern"""

    class InvalidPattern_with_unicode(InvalidPattern):
        _fmt = u'Invalid pattern(s) found. %(msg)s'
    e = InvalidPattern_with_unicode('foo')
    if not isinstance(unicode(e), unicode):
        raise AssertionError('bzrlib.lazy_regex.InvalidPattern.__unicode__ must return a unicode object')

    e = InvalidPattern('foo')
    if not isinstance(str(e), str):
        raise AssertionError('bzrlib.lazy_regex.InvalidPattern.__str__ must return a str object')

# Generated at 2022-06-14 06:16:41.951141
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """Unit test for method __str__ of class InvalidPattern
    """
    # no preformatted string, no _fmt, no __dict__
    class InvalidPattern2(InvalidPattern):
        pass
    e = InvalidPattern2('')
    s = u'Unprintable exception InvalidPattern2: dict=None, fmt=None, error=None'
    assert str(e) == s
    assert unicode(e) == s

    # preformatted string
    class InvalidPattern3(InvalidPattern):
        _preformatted_string = '_preformatted_string'
    e = InvalidPattern3('')
    s = u'_preformatted_string'
    assert unicode(e) == s
    assert str(e) == s

    # preformatted string, _fmt

# Generated at 2022-06-14 06:16:45.319300
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    from bzrlib.i18n import gettext
    error = InvalidPattern('Error message')
    assert str(error) == gettext(error._fmt) % error.__dict__

# Generated at 2022-06-14 06:16:52.464308
# Unit test for method __getattr__ of class LazyRegex
def test_LazyRegex___getattr__():
    """Unit test for method __getattr__ of class LazyRegex

    >>> a = LazyRegex(('a',))
    >>> a._real_regex
    >>> a.match('a')
    <_sre.SRE_Match object at 0x...>
    >>> a._real_regex
    <_sre.SRE_Pattern object at 0x...>
    """


# Generated at 2022-06-14 06:17:00.545681
# Unit test for method __setstate__ of class LazyRegex
def test_LazyRegex___setstate__():
    lr = LazyRegex(['foo'])
    lr.__setstate__({'args': ['bar'], 'kwargs': {}})
    if lr._regex_args != ('bar',):
        raise AssertionError('__setstate__ failed')

# Generated at 2022-06-14 06:17:05.686875
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    # InvalidPattern.__unicode__() should work on python 2.4.
    # See https://bugs.launchpad.net/bzr/+bug/434736
    e = InvalidPattern('msg')
    str(e)

# Generated at 2022-06-14 06:17:15.861557
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    from bzrlib import _i18n

    # Test the method __unicode__
    class TestException(Exception):

        _fmt = '%(msg)s'

    def test_exception_msg(exception, msg):
        """Test a message of an exception"""
        u = gettext(unicode(msg))
        exception.msg = u
        str(exception)
        a = gettext(unicode(msg))
        exception.msg = a
        str(exception)
        b = gettext(unicode(msg))
        if a != b:
            # The message must be different for each gettext call
            raise AssertionError("The message '%s' is not different for each" \
                    "gettext call" % msg)

    # We need to switch from the default encoding to 'utf8'


# Generated at 2022-06-14 06:17:19.562943
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """InvalidPattern.__str__ is correct"""
    msg = "Parsing a pattern failed"
    err = InvalidPattern(msg)
    assert msg in str(err)

# Generated at 2022-06-14 06:17:32.361959
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """testing for method __unicode__ of class InvalidPattern."""
    # see http://zope3.pov.lt/trac/browser/sandbox/povilas/misc/misc/test.py
    # for zope3-style tests.
    #
    # Let's try to create an instance of InvalidPattern
    msg = "Invalid UTF-8 byte found"
    exc = InvalidPattern(msg)
    # No, this should not raise an exception.
    unicode(exc)
    # Let's check it's contents.
    unicode_result = unicode(exc)
    assert unicode_result.startswith(unicode(msg))
    assert unicode_result.find('dict=') != -1
    assert unicode_result.find(', fmt=') != -1

# Generated at 2022-06-14 06:17:41.581277
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """Test for method __str__ of class InvalidPattern"""
    import sys
    try:
        raise InvalidPattern("A message")
    except InvalidPattern as e:
        w = sys.exc_info()[1]
    else:
        raise AssertionError("Should have raised an exception")
    s = str(w)
    assert s == "A message"
    assert isinstance(s, str)
    u = unicode(w)
    assert u == "A message"
    assert isinstance(u, unicode)

# Generated at 2022-06-14 06:17:44.325487
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """__str__ should return a bytestring"""
    try:
        raise InvalidPattern('testing invalid pattern')
    except InvalidPattern as e:
        # __str__ must return a str.
        assert isinstance(str(e), str)


# Generated at 2022-06-14 06:17:49.922763
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """InvalidPattern.__str__ must return a string."""
    # set the preformatted string to a unicode string
    ip = InvalidPattern("message")
    ip._preformatted_string = u"unicode message\u1234"

    assert isinstance(ip.__str__(), str)

# Generated at 2022-06-14 06:17:52.746258
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    s = str(InvalidPattern('an error'))
    assert s == 'Invalid pattern(s) found. an error', s


# Generated at 2022-06-14 06:17:59.112010
# Unit test for method __setstate__ of class LazyRegex
def test_LazyRegex___setstate__():
    lazy_regex = LazyRegex(('<.*>',), {'re.UNICODE':True})
    dict = lazy_regex.__getstate__()
    setstate = LazyRegex.__setstate__
    setstate(lazy_regex, dict)
    assert lazy_regex._regex_args == dict['args']
    assert lazy_regex._regex_kwargs == dict['kwargs']

# Generated at 2022-06-14 06:18:06.416237
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """Test InvalidPattern.__str__."""
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS)

# Generated at 2022-06-14 06:18:13.652394
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    from bzrlib import (
        errors,
    )
    from bzrlib.tests import (
        TestCase,
        )
    error = errors.BzrError(errors.BzrError.INVALID_PREFIX)

# Generated at 2022-06-14 06:18:26.044381
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():

    from bzrlib.tests import TestCase

    class TestCaseInvalidPattern___str__(TestCase):

        def test_string_without_formatter(self):
            ex = InvalidPattern('test')
            self.assertEquals('test', str(ex))
            self.assertEquals('test', unicode(ex))

        def test_unicode_string_without_formatter(self):
            ex = InvalidPattern(u'test')
            self.assertEquals('test', str(ex))
            self.assertEquals(u'test', unicode(ex))

        def test_string_with_formatter(self):
            ex = InvalidPattern('%s test')
            self.assertEquals('%s test', str(ex))
            self.assertEquals(u'%s test', unicode(ex))


# Generated at 2022-06-14 06:18:39.571496
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """This tests the method __unicode__ of class InvalidPattern

    InvalidPattern.__unicode__() should return a unicode string.
    """
    e = InvalidPattern('something went wrong')
    assert e.__unicode__() == u'something went wrong'
    e._preformatted_string = 'something went wrong'
    e.msg = 'error'
    assert e.__unicode__() == u'something went wrong'
    assert e._format() == u'something went wrong'
    assert e.__str__() == u'something went wrong'
    e.msg = u'error'
    assert e.__unicode__() == u'error'
    assert e._format() == u'error'
    assert e.__str__() == u'error'

# Generated at 2022-06-14 06:18:46.338313
# Unit test for method __getattr__ of class LazyRegex
def test_LazyRegex___getattr__():
    """Now we use slot, the following test is no longer needed.

    test for invalid pattern
        - before compiling, no exception is thrown
        - after compiling, exception is thrown

    r = LazyRegex(('(?P<foo]'), {})

    r.__getattr__('match')
    r.match('test string')
    => re.error
    """
    pass

# Generated at 2022-06-14 06:18:52.565050
# Unit test for method __getattr__ of class LazyRegex
def test_LazyRegex___getattr__():
    """Tests that LazyRegex.__getattr__ returns the right value"""
    lazy = LazyRegex(('foo.*',))
    regex = re.compile('foo.*')
    for attr in LazyRegex._regex_attributes_to_copy:
        assert getattr(lazy, attr) == getattr(regex, attr)

# Generated at 2022-06-14 06:19:00.277540
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """InvalidPattern.__str__ formatted and unformatted exception message.

    __str__ should always return an encoded str, and not a unicode object.
    """
    s = InvalidPattern('bar')
    s._fmt = 'foo'
    # __str__ should always return a 'str' object
    # never a 'unicode' object.
    assert isinstance(s.__str__(), str)
    assert s.__str__() == 'foo'
    del s._fmt
    assert isinstance(s.__str__(), str)
    assert s.__str__().startswith('Unprintable exception InvalidPattern')



# Generated at 2022-06-14 06:19:07.021901
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Test for method InvalidPattern.__unicode__"""

    class InvalidPatternSubclass(InvalidPattern):
        pass

    class InvalidPatternSubclassWithFormat(InvalidPattern):
        _fmt = u"Test"

    class InvalidPatternSubclassWithFormatOverride(InvalidPattern):
        _fmt = u"Test"

        def _get_format_string(self):
            return "Overriden"

    def test(expected_result, cls):
        exc = cls("msg")
        exc_unicode = unicode(exc)
        if not hasattr(exc, '_get_format_string'):
            # Force the _format method to be called, otherwise we won't
            # know if the fallback logic has been triggered
            unicode(exc)
        assert exc_unicode == expected_result


# Generated at 2022-06-14 06:19:17.997454
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    from bzrlib.tests import TestUtil

    def check_invalid_pattern(expected, msg):
        # utf-8: '\xe4\xbd\xa0\xe5\xa5\xbd\xe4\xb8\x96\xe7\x95\x8c' means 'hello world' in chinese
        e = InvalidPattern(msg)
        TestUtil.assertEqualDiff(expected, str(e))

# Generated at 2022-06-14 06:19:31.345428
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """InvalidPattern.__unicode__ should return correct unicode objects."""

    # Test None for msg.
    err = InvalidPattern(None)
    expected = u"Unprintable exception InvalidPattern:" \
               + u" dict={}, fmt=None, error=None"
    # Test equality of __unicode__ result.
    assert(err.__unicode__() == expected)

    # Test empty string for msg.
    err = InvalidPattern('')
    expected = u"Unprintable exception InvalidPattern:" \
               + u" dict={}, fmt=None, error=None"
    # Test equality of __unicode__ result.
    assert(err.__unicode__() == expected)

    # Test some string for msg.
    err = InvalidPattern('x')

# Generated at 2022-06-14 06:19:46.723166
# Unit test for method __getattr__ of class LazyRegex
def test_LazyRegex___getattr__():
    """Test that LazyRegex.__getattr__() proxies properly"""
    # build a simple regex
    r = lazy_compile('foo')
    h = hash(r)
    # verify it is a proxy.
    if getattr(r, '_real_regex') is not None:
        raise AssertionError("_real_regex is not None")
    # verify the proxy works
    if not r.match('foo'):
        raise AssertionError("match failed")
    # test that we can call it a second time
    if not r.match('foo'):
        raise AssertionError("match failed")
    # also test that it has collapsed properly and produces the same hash
    if hash(r) != h:
        raise AssertionError("hash %s != %s" % (hash(r), h))

# Generated at 2022-06-14 06:20:00.257875
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    from bzrlib import (
        osutils,
        )

    # If a string is given as the msg to the constructor,
    # the string may contain '%' characters, which are not escaped.
    # The string may be unicode.
    # The string may be not well-formed utf-8, e.g. containing
    # bytes in the range 128 - 255.
    pat = u'hello\n'
    pat += unichr(0x0281)
    pat += unichr(0x10FFFF)
    # It is utf-8 encoded.
    pat_utf8 = pat.encode('utf-8')
    # It is utf-8 encoded, but '0xe2' is replaced by '0xc2'.

# Generated at 2022-06-14 06:20:06.425003
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    import bzrlib
    e = InvalidPattern('msg')
    if (bzrlib.__dict__['__version__'][0] < '2'):
        # version < 2.0
        assert str(e) == 'Invalid pattern(s) found. msg'
        # in version < 2.0, InvalidPattern._fmt was unicode
        assert unicode(e) == u'Invalid pattern(s) found. msg'
    else:
        # version >= 2.0
        assert str(e) == 'Invalid pattern(s) found. ' + e.msg
        assert unicode(e) == u'Invalid pattern(s) found. ' + e.msg

# Generated at 2022-06-14 06:20:19.529794
# Unit test for method __getattr__ of class LazyRegex
def test_LazyRegex___getattr__():
    """Method __getattr__ of class LazyRegex must return attribute of _real_regex.

    If the regex hasn't been compiled yet, compile it.
    In case of exception raise it.
    """
    import sys

    class _RegexProxy(object):
        def __init__(self):
            # Proxy uses this variable to test if it has been compiled
            self._real_regex = None
            # Other attributes, copied from _real_regex
            self.findall = 'findall'
            self.finditer = 'finditer'
            self.match = 'match'
            self.scanner = 'scanner'
            self.search = 'search'
            self.split = 'split'
            self.sub = 'sub'
            self.subn = 'subn'


# Generated at 2022-06-14 06:20:22.219281
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """__str__ of InvalidPattern should return a str

    The method __str__ of class InvalidPattern should always return a
    str, never a unicode object.
    """
    ip = InvalidPattern('foo')
    assert isinstance(str(ip), str)


# Generated at 2022-06-14 06:20:35.409221
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    from bzrlib.i18n import gettext
    from bzrlib.i18n import set_output_encoding
    import sys
    e = InvalidPattern('Pattern is not found.')
    # First test with the default encoding.
    set_output_encoding(sys.getdefaultencoding())
    # The default encoding is not utf8, so decoding by this encoding fails.
    try:
        e.__unicode__()
    except UnicodeDecodeError:
        pass
    else:
        raise AssertionError("Decode should fail "
                             "because output encoding is not utf8.")
    # Now test with utf8 encoding.
    set_output_encoding('utf8')
    # In utf8 encoding, the string can be decoded without any error.
    _ = e.__unicode__

# Generated at 2022-06-14 06:20:42.679441
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    from bzrlib.lazy_regex import InvalidPattern
    from bzrlib.i18n import gettext

    gettext('Invalid pattern(s) found. %(msg)s')
    ip = InvalidPattern('msg')
    try:
        raise ip
    except InvalidPattern as e:
        if str(e) != 'Invalid pattern(s) found. msg':
            raise AssertionError('InvalidPattern.__str__() returned an wrong string.')

# Generated at 2022-06-14 06:20:46.555308
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    from bzrlib.i18n import gettext
    s = gettext(u'plop')
    # this should not raise UnicodeDecodeError
    assert isinstance(str(InvalidPattern(s)), str)

# Generated at 2022-06-14 06:20:52.950952
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    from bzrlib.tests import TestCaseWithTransport
    class Test(TestCaseWithTransport):

        def test_InvalidPattern___str__(self):
            # 'InvalidPattern._format' must always return a 'str' object
            # never a 'unicode' object.
            e = InvalidPattern('foo')
            self.assertIsInstance(str(e), str)

    Test('test_InvalidPattern___str__').run()

# Generated at 2022-06-14 06:21:03.889783
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """Test method __str__ of class InvalidPattern"""

    # Make a InvalidPattern object and test that calling __str__
    # returns something else than 'None' and that the returned
    # value is of type 'str'
    base_exception = InvalidPattern('Invalid pattern(s) found. %(msg)s')
    s = str(base_exception)
    assert s is not None and isinstance(s, str)

    # Unicode invalid pattern message
    invalid_pattern = InvalidPattern(u'Uh-oh invalid pattern')
    assert 'Uh-oh invalid pattern' in str(invalid_pattern)

    # Unicode invalid pattern message with added double quote
    invalid_pattern_with_quote = InvalidPattern(u'"Uh-oh invalid pattern')
    assert '"Uh-oh invalid pattern' in str(invalid_pattern_with_quote)

   

# Generated at 2022-06-14 06:21:17.195118
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """__str__ should return a 'str' object, not a unicode object."""
    # Class InvalidPattern is tested in test_regex.py.
    # This test is here because of the intricate relation between its
    # __unicode__() and __str__() methods.
    assert isinstance(InvalidPattern('hello').__str__(), str)
    assert not isinstance(InvalidPattern('hello').__str__(), unicode)
    assert isinstance(InvalidPattern('abc').__unicode__(), unicode)
    assert not isinstance(InvalidPattern('abc').__unicode__(), str)

# Generated at 2022-06-14 06:21:28.732746
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    import bzrlib.i18n # for set_user_option to work
    bzrlib.i18n.set_user_option('show_structured_error', True)

# Generated at 2022-06-14 06:21:37.325667
# Unit test for method __getattr__ of class LazyRegex
def test_LazyRegex___getattr__():
    """Unit test for method __getattr__ of class LazyRegex"""
    # regex has not been compiled yet
    regex = LazyRegex(['(?P<foo>bar)'])
    assert regex.__getattr__('match') is None
    assert regex.match is None

    # regex has been compiled now
    res = regex.findall('a barbarian')
    assert res == ['bar']
    assert regex.findall is not None
    assert res == ['bar']

# Generated at 2022-06-14 06:21:50.853123
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    # XXX: Aaron Bentley 2009-10-17 bug=424148:
    # This test is a bit fragile, because it assumes we get a particular
    # error.
    from bzrlib._builtin_i18n import _i18n_preferences
    _i18n_preferences()
    # This should not raise an exception
    try:
        raise InvalidPattern(None)
    except InvalidPattern as e:
        assert str(e) == 'Unprintable exception InvalidPattern:' \
            ' dict={}, fmt=None, error=None'
        assert unicode(e) == 'Unprintable exception InvalidPattern:' \
            ' dict={}, fmt=None, error=None'

# Generated at 2022-06-14 06:22:01.064576
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """Check that str()::InvalidPattern() works.

    This test is more specific than the one in tests/i18n_tests.py.
    """
    # This test is more specific than the one in tests/i18n_tests.py.
    import doctest
    import bzrlib.i18n
    enUS = getattr(bzrlib.i18n.translation_to_enUS, 'enUS')
    msg = enUS._fmt % enUS.__dict__
    assert msg == "foo", (enUS._fmt, enUS.__dict__, msg)
    return doctest.testmod(bzrlib.i18n)

# Generated at 2022-06-14 06:22:10.931192
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    class FakeTranslation(object):
        def ugettext(self, text):
            return text
    test = InvalidPattern('test_message')
    test._preformatted_string = 'test_string_%(msg)s'
    test.__class__._fmt = 'test_format'
    inst = test.__class__
    inst._get_format_string = lambda x: 'test_format_%(msg)s'
    inst._no_translation = True
    result1 = unicode(test)
    assert result1 == 'test_string_test_message'
    _real_gettext = inst._gettext
    inst._gettext = FakeTranslation().ugettext
    try:
        result2 = unicode(test)
        assert result2 == 'test_format_test_message'
    finally:
        inst._

# Generated at 2022-06-14 06:22:15.120694
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    import sys
    e = InvalidPattern('msg')
    assert e.__str__() == 'msg'
    if sys.version_info[0] >= 3:
        # Python 3 uses unicode for custom exception messages, so we need
        # to make sure that __str__ returns a valid utf8 string.
        e = InvalidPattern('\xe4\xe9\xec\xf3\xf9')
        assert e.__str__() == '\xc3\xa4\xc3\xa9\xc3\xac\xc3\xb3\xc3\xb9'



# Generated at 2022-06-14 06:22:25.051316
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    from bzrlib.i18n import gettext
    from bzrlib import errors

    try:
        errors.InvalidPattern('"%s",%d' % (u'a', 1))
    except ValueError as e:
        # the ValueError should be caught and the string
        # should be decoded by __unicode__.
        assert(isinstance(e, errors.InvalidPattern)), \
            "InvalidPattern must catch ValueError"

    formated_str = gettext(
        "Invalid pattern(s) found. "
        "The patterns must be a string.")
    pattern = errors.InvalidPattern('"%s", %d' % (u'a', 1))
    assert(pattern.__unicode__() == formated_str), \
        "__unicode__ must return u" + formated_str

# Generated at 2022-06-14 06:22:37.017120
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Test method __unicode__ of class InvalidPattern."""
    from bzrlib.i18n import (
        gettext,
        set_output_encoding,
        )
    set_output_encoding("utf-8")
    msg = "This is a test to verify that *only* the format string is translated"
    ip = InvalidPattern(msg)
    # call the _get_format_string method to verify that it produces the
    # translated message
    assert ip._get_format_string() == gettext(u"Invalid pattern(s) found. %(msg)s")
    u = unicode(ip)
    assert u == gettext(u"Invalid pattern(s) found. ") + msg
    s = str(ip)
    assert s == gettext(u"Invalid pattern(s) found. ") + msg

# Generated at 2022-06-14 06:22:44.794394
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    # Verify that InvalidPattern.__str__() and
    # InvalidPattern.__unicode__() return exactly the same string
    # object. In the case of python 2.x, this happens to be a str,
    # whereas in the case of python 3.x it happens to be a unicode object.
    v = InvalidPattern("foo")
    str_v = str(v)
    unicode_v = unicode(v)
    # Check that __str__ and __unicode__ return the same string object.

# Generated at 2022-06-14 06:22:58.955607
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Test method __unicode__ of class InvalidPattern

    If no '_fmt' is defined, it should return a sensible default message"""
    msg = 'This is a pattern error'
    pattern_error = InvalidPattern(msg)

    expected_msg = 'Unprintable exception InvalidPattern: ' \
                    'dict={\'msg\': \'This is a pattern error\'}, ' \
                    'fmt=None, error=None'
    assert pattern_error._format() == expected_msg



# Generated at 2022-06-14 06:23:03.737872
# Unit test for method __getattr__ of class LazyRegex
def test_LazyRegex___getattr__():
    """Test for <class 'LazyRegex'>."""
    a = LazyRegex(('a', 'b'))
    try:
        a.group()
    except AttributeError:
        return
    raise Exception('LazyRegex should not have a .group attribute')


# Generated at 2022-06-14 06:23:15.121274
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """InvalidPattern.__str__ should produce a valid str

    On Python 2, should produce utf-8 bytes that can be decoded into unicode.
    On Python 3, should produce a unicode string.
    """
    e = InvalidPattern('föö')
    s = str(e)
    try:
        unicode(s)
    except UnicodeDecodeError:
        print("FAIL: Can't convert %r back to unicode" % (s,))
    except TypeError:
        # On Python 3, s is already a unicode string
        pass
    else:
        # On Python 2, s is a utf-8 string
        print("PASS: %r is valid utf-8" % (s,))


# Install the lazy compile functionality, by default
install_lazy_compile()

# Generated at 2022-06-14 06:23:18.384636
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Test for __unicode__ method invocation."""
    e = InvalidPattern(_fmt='Wrong pattern.')
    assert unicode(e) == u'Wrong pattern.'



# Generated at 2022-06-14 06:23:26.512349
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Test method __unicode__ of class InvalidPattern

    This test is separated from the test_errors.py because it must be run
    without a branch since it installs lazy_compile in re.compile.
    """
    install_lazy_compile()
    try:
        re.compile(r'(*')
    except InvalidPattern as e:
        # InvalidPattern is a subclass of ValueError.
        s = unicode(e)
    else:
        raise AssertionError('InvalidPattern should have been raised')
    reset_compile()

# Generated at 2022-06-14 06:23:33.024403
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    from bzrlib.i18n import gettext
    txt = gettext('Invalid pattern(s) found. %(msg)s')
    msg = 'bad pattern'
    e = InvalidPattern(msg)
    unicode_e = unicode(e)
    expected = txt % {'msg': msg}
    if unicode_e != expected:
        raise AssertionError('InvalidPattern.__unicode__() is broken, got "%s" '
                             'instead of "%s"' %(unicode_e, expected))

# Generated at 2022-06-14 06:23:38.554422
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    from bzrlib import (
        trace,
        )
    try:
        raise InvalidPattern('error message')
    except InvalidPattern as e:
        assert trace.user_exc_str(e) == "error message"



# Generated at 2022-06-14 06:23:48.581564
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    from bzrlib import (
        errors,
        )
    # __str__ must return a str.
    e = errors.InvalidPattern('xyz')
    s = str(e)
    if isinstance(s, unicode):
        raise AssertionError('__str__() should return a str')
    # __str__ must return a str even when _format() returns a unicode.
    e._preformatted_string = u'xyz'
    s = str(e)
    if isinstance(s, unicode):
        raise AssertionError('__str__() should return a str')

# Generated at 2022-06-14 06:23:57.609107
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Test __unicode__ method of InvalidPattern.

    This test ensures that the exception raises doesn't have the
    preformatted string but the usual formated string.
    """
    try:
        raise InvalidPattern('foo')
    except InvalidPattern:
        exc = str(sys.exc_info()[1])
        print(exc)
        expected = 'Unprintable exception InvalidPattern: dict={"msg": "foo"}'
        if exc != expected:
            raise AssertionError('exc != "%s"' % expected)



# Generated at 2022-06-14 06:24:07.309015
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    from bzrlib.trace import mutter
    msg_ascii = 'msg_ascii'
    msg_unicode = u'msg_unicode'
    e = InvalidPattern(msg_ascii)
    # msg_ascii is a plain ascii string
    mutter('e.__str__(): %r, type: %s', e.__str__(), type(e.__str__()))
    e = InvalidPattern(msg_unicode)
    # msg_unicode is a unicode string
    mutter('e.__str__(): %r, type: %s', e.__str__(), type(e.__str__()))

# Generated at 2022-06-14 06:24:23.359017
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    import sys
    if sys.version_info.major == 2:
        from . import tests
        # We need to create the fake encoding environment.
        # Note that we need to be careful of not to test any real
        # environment, hence the use of tests.Environ and the
        # tests.system_encoding variable.
        # In Python2, we also need to cleanup the default
        # environment to be sure there is no encoding set.
        # In Python3, we need to keep the PYTHONIOENCODING
        # variable, but set it to None, to prevent Python3 to
        # use it.
        tests.Environ.unset('PYTHONIOENCODING',
                            writer=tests.Environ.system_writer)
    elif sys.version_info.major == 3:
        import os

# Generated at 2022-06-14 06:24:27.979169
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    import doctest
    return doctest.DocTestSuite(doctest=True)

if __name__ == '__main__':
    import unittest
    unittest.main(defaultTest='test_InvalidPattern___unicode__')

# Generated at 2022-06-14 06:24:41.151620
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """Unit test for method __str__ of class InvalidPattern"""
    from bzrlib.tests import TestCase

    class InvalidPatternTestCase(TestCase):

        def test_no_format_string_or_unicode_attribute(self):
            exc = InvalidPattern('Test exception')
            self.assertEqual(
                'Invalid pattern(s) found. Test exception',
                str(exc))

        def test_format_string_no_unicode_attribute(self):
            exc = InvalidPattern('Test exception')
            exc._fmt = 'An exception happened: %(msg)s'
            self.assertEqual(
                'An exception happened: Test exception',
                str(exc))

        def test_unicode_attribute(self):
            exc = InvalidPattern(u'Test exception')
            exc._preformatted_string = u