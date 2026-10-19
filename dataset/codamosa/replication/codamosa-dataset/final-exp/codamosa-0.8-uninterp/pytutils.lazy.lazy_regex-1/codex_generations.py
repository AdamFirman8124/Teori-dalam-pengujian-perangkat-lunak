

# Generated at 2022-06-14 06:14:54.125119
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    from bzrlib.errors import InternalBzrError
    try:
        raise InvalidPattern('error message')
    except InvalidPattern as e:
        assert str(e) == "Invalid pattern(s) found. error message"
        assert unicode(e) == u"Invalid pattern(s) found. error message"
        e = e.__class__('\xc3\xa9rror message')
        assert unicode(e) == u"Invalid pattern(s) found. érror message"
    try:
        raise InternalBzrError('message')
    except InternalBzrError as e:
        assert str(e) == 'message'
        assert unicode(e) == 'message'

# Generated at 2022-06-14 06:15:00.102430
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    u = InvalidPattern(u'foo')
    # unicode() can raise a UnicodeError
    try:
        unicode(u)
    except UnicodeError:
        pass
    else:
        raise AssertionError('unicode(InvalidPattern(%r)) should raise a UnicodeError' % (u,))


# Generated at 2022-06-14 06:15:10.539710
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    import sys
    import traceback
    def _check_str(exp, msg):
        e = InvalidPattern(msg)
        obs = str(e)
        if sys.version_info[0] < 3:
            obs = unicode(e)
        try:
            if obs == exp:
                return
        except:
            pass
        traceback.print_exc()
        print('expect: %s' % exp)
        print('actual: %s' % obs)
        raise AssertionError('strings do not match')

# Generated at 2022-06-14 06:15:22.165440
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """InvalidPattern has str() and unicode() implementations.

    This test is to check that InvalidPattern has __str__() and __unicode__()
    implementations (at least in python 2.x).
    """
    import sys
    if sys.version_info[0] < 3:
        class MyInvalidPattern(InvalidPattern):
            message = str('a message')
            def _get_format_string(self):
                return self.message
        assert str(MyInvalidPattern('a message')) == 'a message'
        assert unicode(MyInvalidPattern('a message')) == unicode('a message')
    else:
        # Running this test in python 3.x will not work.
        pass

# Generated at 2022-06-14 06:15:26.501690
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """Method __str__ should return a str object"""
    e = InvalidPattern('msg')
    assert isinstance(str(e), str)
test_InvalidPattern___str__.todo = 'This fails because re.error is unicode'


# Generated at 2022-06-14 06:15:31.414564
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """__str__ must return a str.  The str may be a multibyte string if
    the default encoding is not ASCII.
    """
    str_object = InvalidPattern('test').__str__()
    assert isinstance(str_object, str)



# Generated at 2022-06-14 06:15:43.179606
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """Test for method __str__ of class InvalidPattern"""
    # The first test is used to check that converting to a str object will
    # succeed. The second test is used to check that the content of the str
    # object is equal to the expected string.
    test_cases = [(InvalidPattern(u'foo'),
                   "Unprintable exception InvalidPattern: dict={'msg': 'foo'}, fmt=None, error=None"),
                  (InvalidPattern(u'bar'),
                   "Unprintable exception InvalidPattern: dict={'msg': 'bar'}, fmt=None, error=None")]
    for test_case in test_cases:
        # The __str__ method must return a str object.
        value = str(test_case[0])
        assert isinstance(value, str)
        assert value == test_case[1]

# Generated at 2022-06-14 06:15:56.138959
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Test for method __unicode__ of class InvalidPattern."""
    from bzrlib.i18n import gettext
    from bzrlib.i18n import install_gettext_translations
    try:
        install_gettext_translations(domain='bzr', localedir=None, codeset='utf-8')
        fmt1 = 'Invalid pattern(s) found. %(msg)s'
        e = InvalidPattern('hello')
        e._preformatted_string = 'preformatted message'
        m = e.__unicode__()
        if not isinstance(m, unicode):
            raise AssertionError('__unicode__ must return a unicode object; '
                                 'got %s.' % m)
    finally:
        from bzrlib.i18n import unregister_get

# Generated at 2022-06-14 06:16:03.337667
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    from bzrlib.i18n import _i18n_exceptions

    _i18n_exceptions.install()
    try:
        raise InvalidPattern('%(num)s %(foo)s')
    except InvalidPattern as e:
        e.foo = 'bar'
        e.num = 1
        assert unicode(e) == u'Invalid pattern(s) found. 1 bar'
    _i18n_exceptions.uninstall()

# Generated at 2022-06-14 06:16:11.265502
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Test method __unicode__ of class InvalidPattern

    This test is here to help guarantee proper __unicode__ handling
    for InvalidPattern. """
    exceptions = [InvalidPattern('test')]

# Generated at 2022-06-14 06:16:27.591283
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    from bzrlib.tests import TestCase
    class Test(TestCase):
        def __str__(self):
            raise AssertionError("Tried to convert unicode to str")

    class FailingGettext(object):
        def __init__(self, fails_on):
            self.fails_on = fails_on

        def __call__(self, s):
            if s == self.fails_on:
                raise Test(u'Did not expect translation to be performed.')
            return s
    test = FailingGettext('a')
    try:
        InvalidPattern('abc', _fmt='a %(b)s c')
        InvalidPattern('hello', _fmt='a %(b)s c')
    except Test:
        self.fail("_get_format_string should have failed")

   

# Generated at 2022-06-14 06:16:40.192536
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """test for method __unicode__"""
    from bzrlib.i18n import gettext
    class Emptyfmt(Exception):
        """An exception without _fmt parameter"""
        pass
    e = InvalidPattern("test message")
    assert e.__unicode__() == u"test message"
    s = gettext("test message")
    e = InvalidPattern(s)
    assert isinstance(e.__unicode__(), unicode)
    assert e.__unicode__() == s
    e._preformatted_string = u"test message"
    assert e.__unicode__() == u"test message"
    e = InvalidPattern(u"test message")
    assert e.__unicode__() == u"test message"
    e = InvalidPattern("test message")

# Generated at 2022-06-14 06:16:49.057546
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    from bzrlib.i18n import ugettext
    from bzrlib import i18n
    from bzrlib.config import GlobalStack

    environ = {'LC_ALL': 'C', 'LANGUAGE': 'C'}
    config_stack = GlobalStack()
    # We fake bzrlib.i18n._translations.
    try:
        i18n._translations = LazyRegex(
            # This function is used as re._translations, see comment in
            # LazyRegex.__init__.
            lambda: ugettext)
        unicode(InvalidPattern('blah'))
    finally:
        i18n._translations = _real_re_compile

    # Russian translation
    environ['LANGUAGE'] = 'ru'
    config_stack.set

# Generated at 2022-06-14 06:16:50.502637
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    import doctest
    doctest.testmod(verbose=False)

# Generated at 2022-06-14 06:17:00.616288
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """__str__() should return a 'str' object."""
    from bzrlib.i18n import gettext
    from bzrlib.pyutils import _mod_re
    from bzrlib.tests import TestCase

    class TestInvalidPattern(InvalidPattern):

        _fmt = 'Invalid pattern(s) found. %(msg)s'

    def check_str_returns_a_str(e):
        """__str__() should return a 'str' object."""
        s = str(e)
        self.assertIsInstance(s, str)
        return s

    def check_unicode_returns_a_unicode(e):
        """__unicode__ should return a 'unicode' object."""
        u = unicode(e)
        self.assertIsInstance(u, unicode)

# Generated at 2022-06-14 06:17:13.452176
# Unit test for method __setstate__ of class LazyRegex
def test_LazyRegex___setstate__():
    import pickle
    import cStringIO

    args = ("abc", 0)
    kwargs = {}
    l1 = LazyRegex(args, kwargs)
    l1._compile_and_collapse()
    state = l1.__getstate__()
    f = cStringIO.StringIO()
    pickle.dump(state, f)
    f.seek(0)
    state = pickle.load(f)
    l2 = LazyRegex((), {})
    l2.__setstate__(state)
    for attr in LazyRegex._regex_attributes_to_copy:
        if getattr(l1, attr) != getattr(l2, attr):
            return False
    return True

# Generated at 2022-06-14 06:17:24.281561
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Test that __unicode__ works for an ascii and a unicode message"""
    from bzrlib.i18n import gettext
    fmt = gettext('%(msg)s')
    # Check an ascii message
    exc = InvalidPattern('Invalid regex')
    expected_msg = u'Invalid regex'
    check_msg = exc.__unicode__()
    if check_msg != expected_msg:
        raise AssertionError(
            '__unicode__ with an ascii message returned '
            '"%(actual)s" expected "%(expected)s"' %
            {'actual':check_msg, 'expected':expected_msg})
    # Check a unicode message
    exc = InvalidPattern('\u2620 invalid')
    expected_msg = u'\u2620 invalid'
    check_msg

# Generated at 2022-06-14 06:17:30.149769
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Method __unicode__() of class InvalidPattern must return unicode"""
    class TestInvalidPattern(InvalidPattern):
        def __init__(self, msg, nonascii_msg):
            InvalidPattern.__init__(self, msg)
            self.nonascii_msg = nonascii_msg
        def _get_format_string(self):
            return self._fmt + ' %(nonascii_msg)s'
    e = TestInvalidPattern('hello', 'world')
    if isinstance(unicode(e), str):
        raise AssertionError(
            "InvalidPattern.__unicode__ must return unicode not ascii")
    if not isinstance(unicode(e), unicode):
        raise AssertionError(
            "InvalidPattern.__unicode__ must return unicode")


# Generated at 2022-06-14 06:17:36.264791
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """Test method __str__ in class InvalidPattern.

    Make sure UnicodeDecodeError will not occur, when
    method __str__ of class InvalidPattern is called.
    """
    class TestInvalidPattern(InvalidPattern):
        _fmt = "hello world"
    exception = TestInvalidPattern()

# Generated at 2022-06-14 06:17:38.140311
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    exc = InvalidPattern('Invalid pattern')
    str(exc)

# Generated at 2022-06-14 06:17:49.670074
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """Test method __str__ of class InvalidPattern"""
    # Test for an unicode string
    e = InvalidPattern(unicode('a unicode string'))
    assert isinstance(str(e), str)
    assert isinstance(unicode(e), unicode)
    assert str(e) == 'a unicode string'

    # Test for a str containing an ascii string
    e = InvalidPattern('a str (ascii)')
    assert isinstance(str(e), str)
    assert isinstance(unicode(e), unicode)
    assert str(e) == 'a str (ascii)'

    # Test for a str containing a unicode object
    e = InvalidPattern(unicode('a str with a unicode object'))
    e._preformatted_string = str(e)

# Generated at 2022-06-14 06:18:03.577382
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    msg = 'utf8 encoded message'
    e = InvalidPattern(msg)
    assert isinstance(e.msg, str)

    s = e._format()
    assert isinstance(s, str)

    u = unicode(e)
    assert isinstance(u, unicode)

    # e.msg is utf8 encoded, and the default encoding is not utf8
    try:
        s = str(e)
        assert False, 'Expected UnicodeEncodeError'
    except UnicodeEncodeError:
        pass

    e = InvalidPattern(u'unicode message')
    assert isinstance(e.msg, unicode)

    s = e._format()
    assert isinstance(s, unicode)

    s = str(e)
    assert isinstance(s, str)


# Generated at 2022-06-14 06:18:08.453336
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """Check that calling str() on an InvalidPattern instance works properly.

    It checks that the result is a str (respectively a unicode on Python 2.6+)
    and that the unicode(str(instance)) gives back the original str.
    """
    utf8_text = '\xe9\xf6\xe7\xe0\xe9'
    if str is not unicode:
        # Unicode was not introduced in Python 2.6 yet, this can't happen.
        utf8_text = utf8_text.decode('utf8')
    exc = InvalidPattern("foo %s bar" % utf8_text)
    exc._preformatted_string = '123' + utf8_text + '456'
    format_string = exc._get_format_string()

# Generated at 2022-06-14 06:18:15.360103
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """Test case of method __str__ of class InvalidPattern

    The method __str__ returns a string representation of the exception.
    It is used by str() and print to convert the exception to a string.
    """
    assert str(InvalidPattern('')) == "Invalid pattern(s) found. "
    assert str(InvalidPattern('msg')) == "Invalid pattern(s) found. msg"



# Generated at 2022-06-14 06:18:26.790424
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """Test method __str__ of class InvalidPattern."""
    import unittest
    from bzrlib.tests import TestCaseInTempDir

    class TestInvalidPattern(TestCaseInTempDir):
        """Test exceptions handling."""

        def test_InvalidPattern___str__(self):
            """Test method __str__ of class InvalidPattern."""
            msg = 'Invalid pattern(s): abc'
            e = InvalidPattern(msg)
            self.assertEqual(str(e), msg)

    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestInvalidPattern)
    module_suite = unittest.TestSuite([test_suite])
    unittest.TextTestRunner(verbosity=2).run(module_suite)

# Generated at 2022-06-14 06:18:28.506314
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    raise InvalidPattern('somemessage')


# Generated at 2022-06-14 06:18:36.092332
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """InvalidPattern.__unicode__() should return a unicode string"""
    msg = 'foo bar'
    e = InvalidPattern('foo bar')
    # e should return a unicode object, not a str.
    u = e.__unicode__()
    assert isinstance(u, unicode)
    # Check that the message is really the one we passed
    assert u == msg, u



# Generated at 2022-06-14 06:18:47.377288
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """__str__() of InvalidPattern"""
    # This is the list of tests.

# Generated at 2022-06-14 06:18:52.566251
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """InvalidPattern.__unicode__

    Unicode string is returned.
    """
    ip = InvalidPattern('foo')
    ip._preformatted_string = u'unicode'
    actual = unicode(ip)
    expected = u'unicode'
    assert actual == expected



# Generated at 2022-06-14 06:19:04.525355
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """This test ensures that method __unicode__ of class InvalidPattern
    works properly.
    """
    from bzrlib.i18n import gettext

    class DummyException(InvalidPattern):
        _fmt = 'Unknown error: %(msg)s'

    msg = 'Break all the things'
    e = DummyException(msg)
    expected = gettext('Unknown error: %s') % msg
    # If a unicode object is returned, that's OK
    assert isinstance(e.__unicode__(), unicode)
    assert e.__unicode__() == expected
    # If a str object is returned, that's OK
    assert isinstance(e.__str__(), str)
    assert e.__str__() == expected
    # If a str containing unicode-escaped utf8 is returned, that's OK

# Generated at 2022-06-14 06:19:18.246634
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    e = InvalidPattern("foobar")
    str(e)
    repr(e)



# Generated at 2022-06-14 06:19:21.954591
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    try:
        raise InvalidPattern('"foo" ')
    except InvalidPattern as e:
        assert str(e) == 'Invalid pattern(s) found. "foo" '
        assert unicode(e) == u'Invalid pattern(s) found. "foo" '


if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 06:19:25.375390
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """__str__ should return str object"""
    try:
        raise InvalidPattern('foo')
    except InvalidPattern as e:
        assert type(str(e)) == str

# Generated at 2022-06-14 06:19:33.328815
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Test for InvalidPattern.__unicode__().

    There was a problem that __unicode__() didn't work if the format string
    in _fmt was unicode and the _fmt parameter was not.

    This test shows that the problem is fixed now.
    """
    ex = InvalidPattern("")
    ex._fmt = "test %(msg)s"
    str(ex)
    ex._fmt = u"test %(msg)s"
    str(ex)



# Generated at 2022-06-14 06:19:39.788196
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """__unicode__ must return a unicode object."""
    err = InvalidPattern('message')
    # the result is a unicode object
    assert isinstance(unicode(err), unicode)
    # the result contains the expected message
    assert str(err) == 'message'
    # the result can be decoded using the default encoding
    assert unicode(err).decode('utf8') == 'message'


# Generated at 2022-06-14 06:19:49.069014
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """Test method __str__ in class InvalidPattern

    Method __str__ is overridden so that any type of object can be used in the
    format string. We test this by using a dict object as the format string.
    """
    msg = dict()
    msg['pattern'] = '*'
    msg['msg'] = 'You must escape wildcard characters'
    err = InvalidPattern(msg)
    str_err = str(err)
    # we can't use unicode here because that would depend on Bazaar's
    # translation setup, which may not be available in other tests
    expected_str = ("Invalid pattern(s) found. You must escape wildcard "
                    "characters")
    assert str_err == expected_str, "%r != %r" % (str_err, expected_str)

# test_InvalidPattern___str__()

# Generated at 2022-06-14 06:19:55.856978
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """Test method __str__ of class InvalidPattern.

    This tests for bug #420185.
    """
    from bzrlib.i18n import gettext

    message = gettext('the %(message)s')
    try:
        raise InvalidPattern(message % { 'message': 'message'})
    except InvalidPattern as e:
        assert str(e) == 'the message'

# Generated at 2022-06-14 06:20:06.111634
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """Unit test for method __str__ of class InvalidPattern"""
    # There is no way to test the result of __str__ since it depends on
    # the locale, so we only check for any exception raised by this method
    import bzrlib.tests.test_i18n as test_i18n
    from bzrlib.i18n import gettext
    test_i18n.install_gettext_augmented_unicode()

# Generated at 2022-06-14 06:20:16.918291
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    from bzrlib.i18n import gettext
    f = InvalidPattern._fmt
    gettext(f)
    InvalidPattern._preformatted_string = 'test'
    assert str(InvalidPattern('test')) == 'test'
    InvalidPattern._preformatted_string = None

    s = 'test'
    u = unicode(s)
    assert unicode(InvalidPattern(s)) == u
    assert str(InvalidPattern(s)) == s.encode('utf8')

    assert str(InvalidPattern(u)) == u.encode('utf8')
    assert unicode(InvalidPattern(u)) == u

# Generated at 2022-06-14 06:20:30.204177
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    import re

    def _test_InvalidPattern___str__(s):
        """Assert that the string will be printed as s"""
        msg = 'Invalid pattern: "%s": unbalanced parenthesis' % (s,)
        error = InvalidPattern(msg)
        error._fmt = 'Invalid pattern(s) found. %(msg)s'

# Generated at 2022-06-14 06:20:55.421022
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """__str__ should produce a 'str' object"""
    e = InvalidPattern('test')
    assert str(e) == unicode(e)
    assert isinstance(str(e), str)



# Generated at 2022-06-14 06:21:09.272340
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    from cStringIO import StringIO
    from bzrlib.i18n import gettext
    try:
        gettext('%s')
    except TypeError:
        # This is the case where gettext doesn't take a variable argument
        # list. We don't care about it here, as we test it already elsewhere
        pass
    else:
        # We have to intercept stdout and stderr to check that the output of
        # the exception is right.
        saved_stdout = sys.stdout
        saved_stderr = sys.stderr

# Generated at 2022-06-14 06:21:15.603946
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Test for (Totally Broken) method __unicode__ of class InvalidPattern"""
    # constructor args
    msg = 'a'
    ip = InvalidPattern(msg)
    assert(ip.msg == msg)
    # test __unicode__
    ip._preformatted_string = 'b'
    assert(unicode(ip) == 'b')
    del ip._preformatted_string
    assert(unicode(ip) == 'Unprintable exception InvalidPattern: dict={}, fmt=%(msg)s, error=None')

# Generated at 2022-06-14 06:21:25.168900
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Test that InvalidPattern allows unicode characters in arguments."""
    # This is not a complete test, but it covers the most commonly
    # used arguments.
    s = unicode(u'\N{CYRILLIC CAPITAL LETTER A}')
    e = InvalidPattern('%s')
    e._preformatted_string = s
    s_actual = unicode(e)
    s_expected = u'\N{CYRILLIC CAPITAL LETTER A}'
    assert s_actual == s_expected, (s_actual, s_expected)

# Generated at 2022-06-14 06:21:33.334496
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    from breezy.tests import (
        TestCase,
        )

    class TestInvalidPattern(TestCase):

        def test__unicode__inherited(self):
            e = InvalidPattern('test_InvalidPattern___str__')
            self.assertEqual('test_InvalidPattern___str__', str(e))
            from bzrlib.i18n import gettext
            self.assertEqual(
                gettext('test_InvalidPattern___str__'), unicode(e))

    TestInvalidPattern.__name__ = 'TestInvalidPattern'
    return TestInvalidPattern

# Generated at 2022-06-14 06:21:42.185271
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Test for InvalidPattern.__unicode__

    InvalidPattern should translate messages used in constructor.
    """
    # Translation is not used in testing so we need to mock
    # gettext() function to emulate it.
    def gettext(message):
        if message == 'foo':
            return 'bar'
        else:
            return message
    import sys
    import locale
    import bzrlib
    sys.modules['bzrlib.i18n'] = bzrlib.i18n

    import bzrlib.i18n
    old_gettext = bzrlib.i18n.gettext
    old_current_translation = bzrlib.i18n.current_translation
    old_locale_code = locale.getlocale(locale.LC_MESSAGES)
    bzrlib

# Generated at 2022-06-14 06:21:47.574821
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """__str__ must return a valid str object.
    """
    ip = InvalidPattern(msg='test')
    # We add a random attribute which must be ignored by __str__.
    ip.random = 'test'
    # __str__ must not fail
    str(ip)
    # __str__ must return a valid str object
    str(ip) == "Invalid pattern(s) found. test"

# Generated at 2022-06-14 06:21:57.420326
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """__unicode__ of InvalidPattern should return a unicode object.

    If it gives a UnicodeDecodeError, it means that Unicode conversion has
    failed, and it should not.
    """
    msg = u"G\u00f6del"
    e = InvalidPattern(msg)
    try:
        str(e)
        ustr(e)
        repr(e)
    except UnicodeDecodeError:
        raise TestSkipped('UnicodeDecodeError: Unable to convert Unicode '
                          'string to given encoding')


# Generated at 2022-06-14 06:22:03.369137
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """InvalidPattern must return a unicode object"""
    err = InvalidPattern("test")
    u = u"test"
    assert err.__unicode__() == u, repr(err.__unicode__())
    assert isinstance(err.__unicode__(), unicode)


# Generated at 2022-06-14 06:22:16.716173
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """Test method __str__ of class InvalidPattern."""
    from bzrlib.i18n import gettext

    err = InvalidPattern('Sre_Pattern_Exception')
    str(err)
    # The following fails, for example, in french:
    #   >>> err = InvalidPattern('Sre_Pattern_Exception')
    #   >>> str(err)
    #   'Invalid pattern(s) found. Sre_Pattern_Exception'
    #   >>> gettext('Invalid pattern(s) found. %(msg)s')
    #   u'Pattern invalide ou invalides. %(msg)s'
    #   >>> err = InvalidPattern('Sre_Pattern_Exception')
    #   >>> str(err)
    #   'Invalid pattern(s) found. Sre_Pattern_Exception'

    del err

# Generated at 2022-06-14 06:22:48.327637
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    try:
        e = InvalidPattern(msg='foo')
        raise e
    except InvalidPattern as e:
        # __str__ must return a str.
        assert isinstance(str(e), str)

    try:
        e = InvalidPattern(msg='foo')
        raise e
    except InvalidPattern as e:
        # __unicode__ must return a unicode.
        assert isinstance(unicode(e), unicode)

# If you want to run unit tests:
# import bzrlib.regexs
# bzrlib.regexs.test_InvalidPattern___str__()

# Generated at 2022-06-14 06:22:55.334946
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    # No message
    exc = InvalidPattern(None)
    assert repr(exc) == 'InvalidPattern(None)'
    assert str(exc) == 'None'
    assert unicode(exc) == u'None'
    # A message that doesn't need encoding
    msg = 'this is a message'
    exc = InvalidPattern(msg)
    assert repr(exc) == 'InvalidPattern(%r)' % msg
    assert str(exc) == msg
    assert unicode(exc) == msg.decode('utf8')
    # A message that does need encoding
    msg = '\xc3\xa8\xc3\xa9'
    exc = InvalidPattern(msg)
    assert repr(exc) == 'InvalidPattern(%r)' % msg
    assert str(exc) == msg.decode('utf8').encode('utf8')


# Generated at 2022-06-14 06:23:05.950267
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Formatting unicode reasons"""
    exc = InvalidPattern('oh noes')
    exc._preformatted_string = 'oh noes'
    unicode(exc)
    exc._preformatted_string = 'oh noes in %(language)s'
    exc.language = 'python'
    exc.__unicode__()
    exc._fmt = 'oh noes in %(language)s'
    unicode(exc)
    exc.language = u'n\N{LATIN SMALL LETTER N WITH TILDE}'
    unicode(exc)
    exc._preformatted_string = u'oh noes in %(language)s'
    unicode(exc)

# Generated at 2022-06-14 06:23:08.663483
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """This tests that we have a valid unicode representation of the class
    InvalidPattern. This is important because we want the exception to be
    well formated in case it is raised at the command line in bzr.
    """
    e = InvalidPattern('message')
    unicode(e)

test_suite = [
    "test_InvalidPattern___unicode__",
]


# Generated at 2022-06-14 06:23:19.260195
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Unit test for method __unicode__ of class InvalidPattern."""
    # If we try to format a unicode error message, we should get a unicode
    # object that contains the unformatted message.
    error1 = InvalidPattern(u'foo')
    # We should get a unicode object that contains the unformatted
    # message.
    error1_unicode = unicode(error1)
    msg = u'Unknown exception InvalidPattern: dict=%s, fmt=%s, error=%s' \
        % (repr(error1.__dict__), error1._fmt, None)
    assert_equal(error1_unicode, msg)
    # If we try to format a unicode error message, we should get a unicode
    # object that contains the formatted message.

# Generated at 2022-06-14 06:23:31.126640
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """InvalidPattern.__str__ should always return a 'str' object.

    This unit test checks that __str__ returns a 'str' object and never
    a 'unicode' object, as was previously the case.
    """
    import sys
    RealInvalidPattern = InvalidPattern

    class InvalidPattern(RealInvalidPattern):

        def __init__(self, msg):
            RealInvalidPattern.__init__(self, msg)
            self._preformatted_string = unicode(msg)

    try:
        e = InvalidPattern("A message")
        assert isinstance(str(e), str)
        assert type(str(e)) == type("")
        if sys.version_info[0] == 2:
            assert type(unicode(e)) == type(u"")
    finally:
        InvalidPattern = RealInvalidPattern

# Generated at 2022-06-14 06:23:32.909902
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    e = InvalidPattern('msg')
    unicode(e)
    e._preformatted_string = 'abc'
    unicode(e)

# Generated at 2022-06-14 06:23:42.228745
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """__str__ should never return a unicode object"""
    from bzrlib.i18n import gettext
    err1 = InvalidPattern(gettext('foo'))
    assert isinstance(err1.__str__(), str)
    assert not isinstance(err1.__str__(), unicode)
    err2 = InvalidPattern('bar')
    assert isinstance(err2.__str__(), str)
    assert not isinstance(err2.__str__(), unicode)

# Generated at 2022-06-14 06:23:44.597777
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """InvalidPattern.__unicode__: returns a unicode object"""
    error = InvalidPattern("msg")
    assert isinstance(error.__unicode__(), unicode)
    error = InvalidPattern("msg")
    error._fmt = 'fmt'
    assert isinstance(error.__unicode__(), unicode)

# Generated at 2022-06-14 06:23:58.320314
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    e = InvalidPattern('message')
    assert unicode(e) == 'message'
    assert str(e) == 'message'
    assert e.__str__() == 'message'
    assert e._format() == 'message'
    e = InvalidPattern('%(foo)s')
    assert unicode(e) == '%(foo)s'
    assert str(e) == '%(foo)s'
    assert e.__str__() == '%(foo)s'
    assert e._format() == '%(foo)s'
    e = InvalidPattern('%(foo)s')
    e.foo = 'hello'
    assert repr(e) == "InvalidPattern('hello')"
    assert unicode(e) == 'hello'
    assert str(e) == 'hello'
    assert e.__str__