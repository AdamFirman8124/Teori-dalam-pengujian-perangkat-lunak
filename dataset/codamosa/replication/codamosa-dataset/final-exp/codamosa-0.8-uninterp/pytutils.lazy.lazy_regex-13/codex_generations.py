

# Generated at 2022-06-14 06:14:51.268055
# Unit test for method __setstate__ of class LazyRegex
def test_LazyRegex___setstate__():
    from bzrlib import trace
    from cStringIO import StringIO

    def _check(old_stdout, proxy, expected_compiled_regex_str, expected_real_regex_str):
        """Test the proxy state"""
        proxy.search('')
        stdout = sys.stdout
        sys.stdout = old_stdout
        msg = trace.mutter_debug(str(proxy))
        sys.stdout = stdout
        compiled_regex_str = msg[:msg.find('\n')]
        real_regex_str = msg[msg.find('\n') + 1:]
        # Check if the proxy is in the expected state

# Generated at 2022-06-14 06:15:04.372967
# Unit test for method __getattr__ of class LazyRegex
def test_LazyRegex___getattr__():
    """__getattr__ should return a member from the proxied regex object."""
    from testtools.matchers import Contains
    from bzrlib import errors
    regex = LazyRegex([r'\s'])
    e = None
    try:
        regex.match('should raise an error')
    except errors.InvalidPattern as error:
        e = error
    e.__unicode__().decode('utf8')  # No UnicodeDecodeError.
    e.__str__().decode('utf8')  # No UnicodeDecodeError.
    e.__repr__().decode('utf8')  # No UnicodeDecodeError.
    e.__eq__(e).__str__().decode('utf8')  # No UnicodeDecodeError.
    str(e)
    msg = '%r' % e

# Generated at 2022-06-14 06:15:15.070000
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """Test method __str__ of class InvalidPattern.
    """
    msg = 'Failed to compile regex'
    e = InvalidPattern(msg)
    assert e.__str__() == ('Invalid pattern(s) found. Failed to compile regex')

    # Test a more complex message, that uses a format string
    msg = 'Failed to compile regex %s'
    e = InvalidPattern(msg % '(?<![A-Z])[A-Z]')
    assert e.__str__() == 'Invalid pattern(s) found. Failed to compile regex (?<![A-Z])[A-Z]'

# Generated at 2022-06-14 06:15:26.308296
# Unit test for method __getattr__ of class LazyRegex
def test_LazyRegex___getattr__():
    import re
    class MockRe(object):
        def __init__(self):
            self.called = False

        def __getattr__(self, attr):
            self.called = True
            return attr

    re.compile = lambda *args, **kwargs: MockRe()
    proxy = LazyRegex('test')
    class MockRaise_error(Exception):
        pass
    proxy._real_re_compile = lambda *args, **kwargs: MockRaise_error()
    try:
        proxy.match
        assert(False)
    except MockRaise_error:
        assert(True)
    try:
        proxy.search
        assert(False)
    except MockRaise_error:
        assert(True)

# Generated at 2022-06-14 06:15:36.961163
# Unit test for method __getattr__ of class LazyRegex
def test_LazyRegex___getattr__():
    """__getattr__ returns a member from the proxied regex object.

    If the regex hasn't been compiled yet, compile it
    """
    _real_re_compile = re.compile
    re.compile = _my_re_compile

    # If the regex hasn't been compiled yet, compile it with the given regex
    # before returning a member from the proxied regex object.
    # It should return the regex's groups without error.
    string = "Hello world!"
    pattern = re.compile('(?P<one>.+) (?P<two>.+)')
    proxy = LazyRegex(('(?P<one>.+) (?P<two>.+)',))
    to_match = proxy.pattern
    search = to_match.search(string)
    proxy_group_dict = search.groupdict()
   

# Generated at 2022-06-14 06:15:46.609906
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """Check __str__() method of InvalidPattern class.

    The method should return a string object."""
    try:
        raise InvalidPattern('This is a test message.')
    except InvalidPattern as e:
        s = str(e)
        if isinstance(s, unicode):
            # A unicode object is not good enough.
            raise Exception('__str__ returned unicode object')
        if not isinstance(s, str):
            raise Exception('__str__ returned an invalid type')

# Generated at 2022-06-14 06:15:57.966245
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Check that __unicode__ return a unicode object"""
    from bzrlib.tests import TestCase
    msg = 'test'

    class TestInvalidPattern(TestCase):
        def setUp(self):
            super(TestInvalidPattern, self).setUp()
            self.exc = InvalidPattern(unicode(msg))

    test_case = TestInvalidPattern('test_InvalidPattern___unicode__')
    test_case.setUp()
    exc = test_case.exc

    # unicode
    try:
        unicode(exc)
    except UnicodeDecodeError:
        test_case.fail('InvalidPattern._format() returned a not-unicode object'
                       ' when _format() returned a unicode object.')
    # str
    try:
        str(exc)
    except UnicodeDecodeError:
        test

# Generated at 2022-06-14 06:16:05.776985
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """InvalidPattern.__str__ should return a str object."""
    msg = 'This is just a simple test message.'
    v = InvalidPattern(msg)
    s = str(v)
    u = unicode(v)
    if isinstance(s, unicode) or isinstance(u, str):
        raise AssertionError(
            '__str__ or __unicode__ returned an unexpected object type.')
    if s != msg:
        raise AssertionError(
            '__str__ returned an unexpected string.')

# Generated at 2022-06-14 06:16:12.633936
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """__unicode__() should return a unicode object that has the default encoding."""
    msg = u"\u3042\u3044\u3046" # 3 charcaters in Japanese.
    e = InvalidPattern(msg)
    u = str(e)
    assert isinstance(u, unicode)
    # The default encoding is 'ascii' in this unit test.
    assert u.encode('ascii') == msg.encode('ascii')

# Generated at 2022-06-14 06:16:18.756817
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    # This is the test for __unicode__ of InvalidPattern class.
    # If a test fails or raises an exception, please let us know.
    import os

    # Set the locale to 'C'
    old_lang = os.environ.get('LANG')
    os.environ['LANG'] = 'C'

    # The param '_preformatted_string' is not specified.
    # The param '_fmt' is not specified.
    exc = InvalidPattern("test_InvalidPattern")
    str1 = exc._format()
    if str1 != 'Unprintable exception InvalidPattern: dict={}, fmt=None, error=None':
        raise AssertionError("1")

    # The param '_preformatted_string' is specified.
    exc = InvalidPattern("test_InvalidPattern")
    exc._preformatted

# Generated at 2022-06-14 06:16:32.719838
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Test InvalidPattern.__unicode__"""
    class InvalidPatternTester(InvalidPattern):

        _fmt = ('Invalid pattern(s) found. %(msg)s')

        def __init__(self, msg):
            self.msg = msg
    for s in ('simple', 'with space', 'with\ttab', 'with\nnewline'):
        e = InvalidPatternTester(s)
        try:
            unicode(e)
        except UnicodeDecodeError:
            assert False, ("unicode() of InvalidPattern should not fail"
                           " with string containing %s" % repr(s))
test_InvalidPattern___unicode__.todo = 'Bug #404047'

# vim: ft=python

# Generated at 2022-06-14 06:16:40.805122
# Unit test for method __getattr__ of class LazyRegex
def test_LazyRegex___getattr__():
    """Ensure that value returned by __getattr__ is the same than the value returned by
    the original __getattr__ method.
    """
    __getattr__ = LazyRegex.__getattr__
    r1 = __getattr__('(a+)b', 'ab')
    r2 = LazyRegex().__getattr__('(a+)b', 'ab')
    r3 = re.compile('(a+)b').__getattr__('(a+)b', 'ab')
    assert r1==r2==r3

# Generated at 2022-06-14 06:16:47.201107
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """InvalidPattern.__unicode__ as expected"""
    from bzrlib import errors
    e = errors.InvalidPattern(u"\xd0\x94\xd0\xb5\xd0\xbb\xd0\xb8\xd0\xbc")
    expected = u"\xd0\x94\xd0\xb5\xd0\xbb\xd0\xb8\xd0\xbc"
    assert e.__unicode__() == expected, \
        "Error message should be in unicode"

# Generated at 2022-06-14 06:16:51.702414
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    import doctest
    from bzrlib.tests.blackbox import ExternalBase
    return ExternalBase('bzrlib.lazy_regex').load_tests('',
        doctest.DocTestSuite(InvalidPattern), None, None, None)

# Generated at 2022-06-14 06:17:01.942427
# Unit test for method __getattr__ of class LazyRegex
def test_LazyRegex___getattr__():
    """Ensure that LazyRegex.__getattr__() works as expected."""
    # patch _real_re_compile() to be able to test whether it is called
    global _real_re_compile
    _real_re_compile_old = _real_re_compile
    _real_re_compile = lambda *args, **kwargs: None

# Generated at 2022-06-14 06:17:14.085372
# Unit test for method __getattr__ of class LazyRegex
def test_LazyRegex___getattr__():
    """The method __getattr__ must return a member from the proxied regex
    object. If the regex hasn't been compiled yet, compile it.
    """
    # The test function is a member of the real regex
    lazy_regex = LazyRegex(('',), {})
    assert 'test' in dir(lazy_regex._real_re_compile(''))
    assert lazy_regex.test is lazy_regex._real_regex.test
    # The test function is not a member of the LazyRegex object
    assert 'test' not in dir(lazy_regex)
    # The test function is a member of the proxied regex object
    assert lazy_regex.test is lazy_regex._real_regex.test

# Generated at 2022-06-14 06:17:16.853388
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    e = InvalidPattern('invalid pattern')
    assert str(e) == 'invalid pattern'
    assert unicode(e) == u'invalid pattern'

# Generated at 2022-06-14 06:17:26.113754
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Test method __unicode__ of class InvalidPattern."""
    # it's better to test with a unicode pattern
    pattern = b'\xc3\xa8\xc3\xa9'
    # and with a unicode string in the exception message
    from bzrlib.i18n import gettext
    str_in_the_exception_message = gettext('invalid pattern')
    try:
        re.compile(pattern)
    except InvalidPattern as e:
        # we should have a string object (a.k.a. str), not a unicode object
        assert isinstance(str(e), str)
        assert unicode(e) == str_in_the_exception_message

# Generated at 2022-06-14 06:17:36.917170
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """InvalidPattern.__unicode__ should return unicode"""
    from bzrlib.i18n import gettext
    from bzrlib.i18n import ugettext
    from bzrlib import translation
    from bzrlib.tests import TestCase
    from bzrlib.transport.http._urllib2_wrappers import HTTPSHandler

    class TestCaseWithTrans(TestCase):

        def test_httpshandler_authorization_failure(self):
            """HTTPSHandler should correctly handle authorization failures"""
            # https://bugs.launchpad.net/bzr/+bug/281441
            import urllib2
            import urllib
            import socket
            import httplib
            import os.path
            import sys

            # set up a handler with a spoofed BaseHTTPServer

# Generated at 2022-06-14 06:17:50.045216
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """InvalidPattern(msg='').__unicode__()

    The __unicode__() method must return a unicode object.
    """
    import bzrlib.tests
    # This test doesn't make sense when run in python 2.x or when the
    # system encoding is not able to decode the unicode string.
    if (bzrlib.tests.TestCase.python_version == 2) or \
       (bzrlib.tests.TestCase.system_encoding == 'unknown'):
        return
    error = InvalidPattern('')
    result = unicode(error)
    if isinstance(result, unicode) is False:
        raise AssertionError('InvalidPattern(msg=\'\').__unicode__() did not '
                             'return a unicode object')

# Generated at 2022-06-14 06:18:02.345392
# Unit test for method __getattr__ of class LazyRegex
def test_LazyRegex___getattr__():
    """Test __getattr__ of LazyRegex"""
    import re
    import pickle

    # Compile the regex and test it
    def test_regex_compile(regex_args, regex_kwargs):
        # Create the regex and test it
        def test_regex():
            regex = lazy_compile(*regex_args, **regex_kwargs)
            # None of the attributes should have been copied yet
            assert regex._real_regex == None
            # Test all of the attributes which will be copied
            for attr in regex._regex_attributes_to_copy:
                assert not hasattr(regex, attr)
                getattr(regex, attr)
                assert hasattr(regex, attr)
        # Pickle the regex and test it

# Generated at 2022-06-14 06:18:11.718142
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """InvalidPattern.__unicode__() should return a smart message when
    preformatted or not.
    """
    from bzrlib import i18n
    i18n.install_gettext()
    try:
        # Test an exception with a preformatted string
        fmt = 'Invalid pattern(s) found. %(msg)s'
        msg = 'this is a message'
        e = InvalidPattern(msg)
        e._fmt = fmt
        # Test an exception without a preformatted string
        e = InvalidPattern(msg)
        # Checking types
        assert(isinstance(e.__unicode__(), unicode))
        assert(isinstance(e.__str__(), str))
    finally:
        # We need to release gettext
        i18n.uninstall_gettext()
    return

# Generated at 2022-06-14 06:18:24.686171
# Unit test for method __setstate__ of class LazyRegex
def test_LazyRegex___setstate__():
    """__setstate__ for LazyRegex"""
    # Testing a method of LazyRegex requires to import LazyRegex
    # and have it installed
    from bzrlib.lazy_regex import LazyRegex
    from bzrlib.lazy_regex import install_lazy_compile
    regex = LazyRegex([])
    regex.__setstate__({'args': [], 'kwargs': {}})

    # Check the right method has been called
    install_lazy_compile()
    LazyRegex._real_regex = "original_regex"
    LazyRegex._real_re_compile = "compile_called"
    LazyRegex.__setstate__(regex, {'args': [], 'kwargs': {}})
    # compile_called

# Generated at 2022-06-14 06:18:27.667481
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """__str__ should return a string."""
    invalid = InvalidPattern('invalid')
    str(invalid)

# Generated at 2022-06-14 06:18:38.717591
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    from bzrlib.lazy_regex import InvalidPattern

    test_cases = (
        (InvalidPattern(u'foo'), u'Invalid pattern(s) found. foo'),
        (InvalidPattern(u'foo\\'), u'Invalid pattern(s) found. foo\\'),
        (InvalidPattern(u'foo\\u1234'),
         u'Invalid pattern(s) found. foo\u1234'),
        (InvalidPattern('foo\nbar'), 'Invalid pattern(s) found. foo\nbar'),
        )
    for e, expected in test_cases:
        result = str(e)
        assert result == expected, result



# Generated at 2022-06-14 06:18:51.701570
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    from bzrlib.trace import mutter
    mutter.set_verbosity(mutter._show_differing_environments_verbosity_level)

    inv_pat = InvalidPattern('foo')
    if not isinstance(inv_pat.__unicode__(), unicode):
        raise AssertionError('InvalidPattern.__unicode__ should return unicode but'
                             ' returns %s' % inv_pat.__unicode__().__class__)
    if not isinstance(inv_pat.__str__(), str):
        raise AssertionError('InvalidPattern.__str__ should return str but'
                             ' returns %s' % inv_pat.__str__().__class__)

# Generated at 2022-06-14 06:18:55.670741
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Test method __unicode__ of class InvalidPattern."""
    msg = 'test'
    error = InvalidPattern(msg)
    assert str(error) == unicode(error)==msg


# Generated at 2022-06-14 06:19:02.434933
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """The method __unicode__ should return a unicode object."""
    from bzrlib.i18n import gettext
    ipattern = InvalidPattern('test string')
    ipattern._preformatted_string = gettext(unicode(ipattern._fmt)) % \
        {'msg': 'test string'}
    assert isinstance(ipattern.__unicode__(), unicode)


# Generated at 2022-06-14 06:19:08.653383
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    try:
        raise InvalidPattern('Some message')
    except Exception as e:
        assert str(e) == 'Invalid pattern(s) found. Some message'
        assert unicode(e) == 'Invalid pattern(s) found. Some message'
        assert repr(e) == 'InvalidPattern(Invalid pattern(s) found. Some message)'

# Generated at 2022-06-14 06:19:12.574643
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """InvalidPattern.__unicode__() should return an unicode object."""
    ip = InvalidPattern('msg')
    assert(isinstance(ip.__unicode__(), unicode))

# Generated at 2022-06-14 06:19:22.029285
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    from bzrlib import (
        errors,
        )

    invalid_pattern = InvalidPattern('Invalid regex')
    errors.str_to_unicode(str(invalid_pattern)) # should not raise UnicodeDecodeError



# Generated at 2022-06-14 06:19:32.687079
# Unit test for method __getattr__ of class LazyRegex
def test_LazyRegex___getattr__():
    """Test accessing attributes on LazyRegex without triggering compiling"""
    lr = LazyRegex(args=("a",))
    lr._real_regex = False
    # check attr on LazyRegex class
    assert lr.__class__ is LazyRegex
    # check attr on LazyRegex instance
    assert lr._real_regex is False
    # check attr on proxied re.SRE_Pattern instance
    assert lr.findall("b") == ["a"]
    # check that _compile_and_collapse() worked
    assert lr.__class__ is not LazyRegex


# Generated at 2022-06-14 06:19:35.812906
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    import doctest
    from bzrlib import errors
    doctest.testmod(errors, optionflags=doctest.ELLIPSIS)

# Generated at 2022-06-14 06:19:45.084799
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """Assert that InvalidPattern can be converted to a string"""

    class InvalidPatternDerived(InvalidPattern):
        _fmt = 'Invalid pattern "%(pattern)s". %(msg)s\n%(filename)s:%(lineno)s'
    error = InvalidPatternDerived("'[a-z]'", {'pattern': 'regexp',
                                              'msg': 'Invalid regex',
                                              'filename': 'file.py',
                                              'lineno': 100})
    expected = 'Invalid pattern "regexp". Invalid regex\nfile.py:100'
    assert_equal(str(error), expected)

# Generated at 2022-06-14 06:19:58.634295
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """InvalidPattern class should return a str object in case of __str__."""
    # We test 2 cases: 1 with and 1 without format string
    # case 1: with format string
    ex = InvalidPattern("This is a test")
    result = str(ex)
    if isinstance(result, str):
        pass # ok
    else:
        raise AssertionError("__str__  of InvalidPattern should return a "
                             "str object, but returned a %r"
                             % result.__class__.__name__)
    
    # case 2: without format string
    ex = InvalidPattern('')
    result = str(ex)
    if isinstance(result, str):
        pass # ok

# Generated at 2022-06-14 06:20:09.430668
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """__unicode__ must always return a unicode object."""
    class Foo(InvalidPattern):
        def _get_format_string(self):
            return 'Something Bizarre Happened: %(bizarre_thing)s'
    # Create an InvalidPattern whose message is a unicode.
    f = Foo(unicode('something bizarre'))
    # The __unicode__() method must return a unicode object.
    assert isinstance(f.__unicode__(), unicode)

    # Create an InvalidPattern whose message is a str.
    f = Foo('something bizarre')
    # The __unicode__() method must return a unicode object.
    assert isinstance(f.__unicode__(), unicode)

    # Create an InvalidPattern whose message is not a str or unicode.

# Generated at 2022-06-14 06:20:17.848152
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """Test the method __str__ of class InvalidPattern

    This test is intended to check if the format of the error message is
    correct for the method __str__.
    """
    import re
    from StringIO import StringIO
    error_message = StringIO()

# Generated at 2022-06-14 06:20:30.840848
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """Tests for InvalidPattern.__str__()"""
    from bzrlib.i18n import gettext

    # Needed for being able to call setlocale() in
    # InvalidPattern._format().
    from bzrlib import osutils
    # Use a locale which will decode the format string below.
    osutils.setlocale(locale='fr_FR.UTF-8')

    # Initialize the _fmt attribute as 'Invalid pattern(s) found. %(msg)s'
    e = InvalidPattern('abc')

    # Check that the string is decoded properly.
    assert str(e) == 'Invalid pattern(s) found. abc'
    assert unicode(e) == u'Invalid pattern(s) found. abc'
    # And that it can be printed using non-ascii encoding.
   

# Generated at 2022-06-14 06:20:40.321701
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Test the method __unicode__ of class InvalidPattern"""
    def translate(s):
        return s

    err = InvalidPattern(10)
    err._format = (lambda : 10)
    # call __unicode__ with no translator for repr(err)
    err.__unicode__()
    # call __unicode__ with a translator for repr(err)
    err.__unicode__(translate)
    # call __unicode__ with a translator that raises an exception for
    # repr(err)
    def translate(s):
        raise TypeError
    err.__unicode__(translate)
    # call __unicode__ with a translator that raises an exception
    # for s and repr(err)
    def translate(s):
        err._preformatted_string = 10
        return s
    err.__unicode

# Generated at 2022-06-14 06:20:53.960961
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    from bzrlib.i18n import gettext

    if hasattr(gettext, '__unicode__'):
        gettext_u = gettext.__unicode__
    else:
        # Python 2.3
        gettext_u = gettext.__str__
    gettext_u.__doc__ = gettext.__doc__

    class Fmt(object):
        _fmt = 'Foo %(x)s'
        def __init__(self, x):
            self.x = x
        def __unicode__(self):
            return gettext_u('Foo %(x)s') % {'x':self.x}
    def __eq__(self, other):
        if self.__class__ is not other.__class__:
            return False
        return self.x == other

# Generated at 2022-06-14 06:21:11.601241
# Unit test for method __getattr__ of class LazyRegex
def test_LazyRegex___getattr__():
    """Test getattr of LazyRegex

    This test is a bit ugly to test the __getattr__ method.

    If a new method is added to re.RegexObject, we need to add a new test in
    this method.
    """
    class MyRegexObject(re.RegexObject):
        def new_method(self):
            """New method in RegexObject"""
            return "method"

    re_compile_old = re.compile
    re.compile = lambda pattern, flags=0: MyRegexObject(pattern, flags)


# Generated at 2022-06-14 06:21:20.711968
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    import traceback
    from bzrlib.tests.scenarios import load_tests_apply_scenarios
    from bzrlib.tests import TestCaseInTempDir

    class TestCase(TestCaseInTempDir):

        scenarios = [
            ('ascii', {'message': 'foobar'}),
            ('unicode', {'message': u'foobar'}),
            ('non_ascii', {'message': u'\xe9'}),
            ('non_ascii_and_unicode', {'message': u'\xe9f\xf6ba'}),
            ]

        def test_InvalidPattern__unicode__(self):
            class SpecialException(Exception):
                def __str__(self):
                    super(SpecialException, self).__str__()
                    # Simulate the case

# Generated at 2022-06-14 06:21:27.140258
# Unit test for method __getattr__ of class LazyRegex
def test_LazyRegex___getattr__():
    """LazyRegex.__getattr__ should correctly return attributes after compilation.
    """
    lazy_regex = LazyRegex([r'^foo$'])
    lazy_regex._compile_and_collapse()
    assert getattr(lazy_regex, 'match')('foo') is not None
    assert getattr(lazy_regex, 'match')('bar') is None

# Generated at 2022-06-14 06:21:37.361027
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """__str__ of InvalidPattern should return a str, not unicode."""
    # this test is important because bzrlib.errors.BzrError metaclass
    # (in bzrlib.trace) expects that when defining a new Exception
    # that subclasses a BzrError (such as InvalidPattern) that
    # self.__unicode__() returns a unicode object and self.__str__()
    # returns a str object. 
    e = InvalidPattern('msg')
    assert isinstance(str(e), str), "str(e) is %r, not str" % (type(str(e)))
    assert isinstance(unicode(e), unicode), \
           "unicode(e) is %r, not unicode" % (type(unicode(e)))



# Generated at 2022-06-14 06:21:50.904517
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    from cStringIO import StringIO
    stream = StringIO()
    e = InvalidPattern('foo')
    class MyException(Exception):
        def __str__(self):
            stream.write('str')
            return 'str'
        def __unicode__(self):
            stream.write('unicode')
            return u'unicode'
    e = InvalidPattern('foo')
    e.e = MyException()
    # the previous invalidpatterns went via __repr__ rather than __str__
    # and thus did not result in anything being printed
    str(e)
    stream.seek(0)

# Generated at 2022-06-14 06:21:57.149525
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    t = InvalidPattern('Oups!')
    e = t._format()
    assert isinstance(e, str), (e, type(e))
    e = unicode(t)
    assert isinstance(e, unicode), (e, type(e))
    e = str(t)
    assert isinstance(e, str), (e, type(e))

# Generated at 2022-06-14 06:22:08.848854
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Test __unicode__ of class InvalidPattern"""
    # The following test is translated from the docstring of
    # test_InvalidPattern___unicode__.
    # We run the test in a function because we don't want to change the
    # state of the exception module.
    class TestError(Exception):
        _fmt = """\
    You can't just say "Hey! What's wrong with saying %(something)s?"
    %(something)s is just what's wrong with America!
    """
        def __init__(self, msg, something=None):
            if something:
                self.something = 'It is insensitive.'
            else:
                self.something = 'You can\'t say that!'
            super(TestError, self).__init__(msg)
    e = TestError('')
    assert str(e)

# Generated at 2022-06-14 06:22:12.264977
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    try:
        raise InvalidPattern('test')
    except InvalidPattern as e:
        # Test __unicode__ return a unicode object.
        assert(isinstance(unicode(e), unicode))

# Generated at 2022-06-14 06:22:23.564894
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """InvalidPattern.__str__() should always return a 'str' object"""
    # A valid message, which returns a unicode object
    o1 = InvalidPattern('normal message')
    r1 = o1.__str__()
    # Another valid message, which returns a unicode object
    o2 = InvalidPattern(u'\u1112\u1161\u11ab normal message')
    r2 = o2.__str__()
    # A invalid message, which returns a unicode object
    o3 = InvalidPattern(u'\u1112\u1161\u11ab \u1112\u1161\u11ab')
    r3 = o3.__str__()
    # A invalid message, which returns a str object

# Generated at 2022-06-14 06:22:33.803506
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    # Normal scenario
    err = InvalidPattern('test')
    assert str(err) == 'Invalid pattern(s) found. test'

    # Unicode utf-8 message
    err = InvalidPattern(u'test')
    assert isinstance(str(err), str)
    assert str(err) == 'Invalid pattern(s) found. test'

    # Unicode with non-ascii characters in it.
    err = InvalidPattern(u'\xa3')
    assert isinstance(str(err), str)
    assert str(err) == 'Invalid pattern(s) found. \xc2\xa3'

# Generated at 2022-06-14 06:22:52.699518
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    from bzrlib.trace import mutter
    # InvalidPattern.__unicode__ must return a unicode object even if the
    # message to print was supplied in an ascii string.
    exc = InvalidPattern('some message')
    s = unicode(exc)
    mutter('unicode(exc) in test_LazyRegex.test_InvalidPattern___unicode__(): %r', s)
    # __unicode__ must return a unicode object.
    assert isinstance(s, unicode)
    # InvalidPattern.__unicode__ must return a unicode object even if the
    # message to print was supplied in a unicode string.
    exc = InvalidPattern(u'some message')
    s = unicode(exc)

# Generated at 2022-06-14 06:22:57.772952
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """ This is a regression test for bug #324452,
    InvalidPattern.__str__() must not raise UnicodeDecodeError.
    """

# Generated at 2022-06-14 06:23:05.803168
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Unit test for method __unicode__ of class InvalidPattern"""
    # Create the object to test
    i = InvalidPattern('msg')
    i.__str__ = lambda: 'str'
    # __str__ is expected to be returned as unicode
    s = i.__unicode__()
    if isinstance(s, unicode):
        return
    raise AssertionError(
        "expected unicode, but got %s" \
        % (repr(s)))


# Generated at 2022-06-14 06:23:17.760636
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """Test method __str__ of class InvalidPattern"""
    e = InvalidPattern("test exception")
    assert str(e) == 'test exception'
    e = InvalidPattern("test exception %(msg)s")
    assert str(e) == 'test exception test exception %(msg)s'
    e = InvalidPattern("test exception %(msg)s")
    e._preformatted_string = "preformatted"
    assert str(e) == 'preformatted'
    e = InvalidPattern("test exception %(msg)s")
    e._fmt = 'test exception %(msg)s'
    assert str(e).startswith("_("), str(e)
    e = InvalidPattern("test exception %(msg)s")
    e._fmt = 'test exception %(msg)s'
    e._get_format_

# Generated at 2022-06-14 06:23:25.962918
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Ensure InvalidPattern.__unicode__ works.

    This must work both with Python 2 and Python 3.
    """
    e = InvalidPattern('abc def')
    if sys.version_info[0] > 2:
        expected = str('abc def')
        actual = e.__unicode__()
        assert isinstance(actual, str)
        assert actual == expected
    else:
        expected = unicode('abc def')
        actual = e.__unicode__()
        assert isinstance(actual, unicode)
        assert actual == expected

# Generated at 2022-06-14 06:23:28.948447
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Tests that InvalidPattern.__unicode__() returns a unicode."""
    e = InvalidPattern("msg")
    assert isinstance(e.__unicode__(), unicode)

# Generated at 2022-06-14 06:23:31.368071
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    e = InvalidPattern('unicode')
    u = unicode(e)
    assert u.__class__ == unicode

# Generated at 2022-06-14 06:23:41.190492
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Ensure that InvalidPattern.__unicode__() returns a unicode object"""
    from bzrlib.i18n import ugettext
    try:
        original_ugettext = ugettext
        def mock_ugettext(s):
            return u'ugettext: ' + s
        ugettext = mock_ugettext
        msg = u'\N{LATIN SMALL LETTER A WITH DIAERESIS}'
        e = InvalidPattern(msg)
        expected_result = u'ugettext: ' + msg
        result = unicode(e)
        assert result == expected_result
    finally:
        ugettext = original_ugettext

# Generated at 2022-06-14 06:23:51.603773
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """Error messages in InvalidPattern are translated by __str__.

    They are translated in order to be readable by the user.
    This is the case at least when the user uses command bzr.
    """
    from bzrlib.i18n import gettext
    from bzrlib.i18n import set_gettext_output_encoding
    set_gettext_output_encoding('utf-8')

# Generated at 2022-06-14 06:24:05.921282
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Unit test for method __unicode__ of class InvalidPattern"""
    class BadPattern(InvalidPattern):
        _fmt = ('%(pattern)r matches nothing.')
    class GoodPattern(InvalidPattern):
        _fmt = ('%(pattern)s matches nothing.')
    from bzrlib.i18n import gettext
    _ = gettext
    for e in (BadPattern(pattern='abc'), GoodPattern(pattern='abc')):
        assert isinstance(e.__unicode__(), unicode)
        assert e.__unicode__() == _('abc matches nothing.')
        assert isinstance(e.__str__(), str)
        assert e.__str__() == 'abc matches nothing.'
        assert isinstance(e.__repr__(), str)

# Generated at 2022-06-14 06:24:22.482546
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """Ensure that InvalidPattern.__str__() is sane."""
    import locale
    locale.setlocale(locale.LC_ALL, '')
    e = InvalidPattern('a message')
    if isinstance(e, UnicodeEncodeError):
        print('e=%s' % e)


# Generated at 2022-06-14 06:24:30.866671
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """__str__ of class InvalidPattern returns ascii string"""
    try:
        raise InvalidPattern("ascii")
    except InvalidPattern as e:
        # e.__str__() should return ascii string
        assert isinstance(e.__str__(), str)


if __name__ == '__main__':
    install_lazy_compile()
    re.compile("foo")
    reset_compile()