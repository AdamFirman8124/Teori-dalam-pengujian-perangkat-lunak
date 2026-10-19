

# Generated at 2022-06-14 06:14:46.472138
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """InvalidPattern.__str__ is able to produce valid str object"""

    class InvalidPatternWithFmt(InvalidPattern):
        _fmt = u"%(msg)s"

    ex = InvalidPatternWithFmt(u"123")
    assert isinstance(str(ex), str)



# Generated at 2022-06-14 06:14:51.016705
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """InvalidPattern.__unicode__ should produce an unicode string."""
    msg = "my exception"
    e = InvalidPattern(msg)
    assert(isinstance(unicode(e), unicode))

# Generated at 2022-06-14 06:14:57.185287
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """Test that method __str__ of class InvalidPattern always returns a str.

    This method is intended not to be used directly.
    """

    msg = 'Invalid pattern(s) found. test'
    def test(e, expected_result):
        s = str(e)
        if s != expected_result:
            print(('str(%s) returns %s instead of %s' %
                                 (e.__class__.__name__, s, expected_result)))
        u = unicode(e)
        if u != expected_result:
            print(('unicode(%s) returns %s instead of %s' %
                                 (e.__class__.__name__, u, expected_result)))

    test(InvalidPattern(msg), msg)

# Generated at 2022-06-14 06:15:09.220382
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Test for method __unicode__ of class InvalidPattern
    """
    from bzrlib.tests import TestCase
    # test for ascii string in _fmt
    class Test1(TestCase):
        _fmt = 'Invalid pattern(s) found. %(msg)s'
        def test___unicode__(self):
            e = InvalidPattern('test')
            self.assertEqual(unicode(e), 'Invalid pattern(s) found. test')

    # test for unicode string in _fmt
    class Test2(TestCase):
        _fmt = u'Invalid pattern(s) found. %(msg)s'
        def test___unicode__(self):
            e = InvalidPattern('test')
            self.assertEqual(unicode(e), u'Invalid pattern(s) found. test')

# Generated at 2022-06-14 06:15:22.445673
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """Test __str__ on InvalidPattern class."""
    # All the following tests check that the __str__ methods on
    # InvalidPattern returns a str object. It is not a good idea to cause
    # the __str__ to return unicode because some code assumes that it is
    # a str.
    class MatchableThing(object):
        """Thing that can be compared to strings."""

        def __init__(self, string):
            self.string = string

        def __eq__(self, other):
            return self.string == other

    def check_str_returned(error):
        if not isinstance(error, str):
            raise AssertionError("Error (%s) is not a str object." % error)

    # These tests are not necessary needed but it is good to have them.
    # - __init__ method is

# Generated at 2022-06-14 06:15:29.886992
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """InvalidPattern.__unicode__() should return unicode object"""
    error = InvalidPattern('msg')
    try:
        unicode(error)
    except UnicodeDecodeError:
        # this would be raised in Python 3.2
        raise AssertionError('InvalidPattern.__unicode__() should return'
            ' unicode object')
    else:
        # in Python 2.7 __unicode__() must return a unicode object
        pass

# Generated at 2022-06-14 06:15:38.075503
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    import sys
    class Foo(InvalidPattern):
        pass

    fmt = 'Hello %(foo)s'
    foo = Foo('bar')
    foo._fmt = fmt
    foo.foo = 'bar'
    assert str(foo) == fmt % foo.__dict__
    assert unicode(foo) == unicode(fmt % foo.__dict__)

    foo = Foo('bar')
    foo._fmt = 'Hello %(foo)s'
    foo.foo = 'b\xc3\xa1r'
    assert str(foo) == 'Hello b\xc3\xa1r'
    if sys.version_info < (3,):
        assert unicode(foo) == u'Hello b\xe1r'
    else:
        assert unicode(foo) == 'Hello b\xe1r'



# Generated at 2022-06-14 06:15:47.592606
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Ensure this method returns a unicode object."""
    class msg(object):
        def __str__(self):
            return 'xxx'
        def __unicode__(self):
            return u'xxx_u'
    pat = InvalidPattern(msg())
    pat._fmt = u'%(msg)s'
    if not isinstance(pat.__unicode__(), unicode):
        raise AssertionError('__unicode__() should return a unicode object')



# Generated at 2022-06-14 06:15:55.359900
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    from bzrlib.tests import TestNotApplicable
    import sys
    import traceback
    test = InvalidPattern("test")
    try:
        str(test)
    except UnicodeDecodeError:
        # In Python 2.x, test has a unicode string. But because of
        # sys.getdefaultencoding(), the call to unicode() fails.
        # In this case, we don't really care about the output of __str__.
        # It should be just fine.
        raise TestNotApplicable('sys.getdefaultencoding() not utf-8')

# Generated at 2022-06-14 06:16:02.770892
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """InvalidPattern must provide a fully working __unicode__.

    This is done by providing a __str__ that does the same as __unicode__, so
    the test is not repeated.
    """
    # Empty instance
    e = InvalidPattern("")
    unicode(e)
    e = InvalidPattern("foo")
    unicode(e)
    e = InvalidPattern("foo")
    unicode(e)


# Generated at 2022-06-14 06:16:07.395083
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 06:16:15.368341
# Unit test for method __setstate__ of class LazyRegex
def test_LazyRegex___setstate__():
    import pickle

    lr = LazyRegex([r'(?P<a>foo)'], {'flags': re.VERBOSE})
    lr2 = pickle.loads(pickle.dumps(lr))
    if lr._regex_args != lr2._regex_args:
        raise AssertionError("_regex_args was not set correctly during"
                             " unpickling")
    if lr._regex_kwargs != lr2._regex_kwargs:
        raise AssertionError("_regex_kwargs was not set correctly during"
                             " unpickling")

# Generated at 2022-06-14 06:16:23.986102
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """InvalidPattern.__str__() should return a str, not a unicode object
    """
    from bzrlib import trace
    trace.set_verbosity_level(trace.TRACE_ALL_NO_IO)
    try:
        raise InvalidPattern("foo")
    except InvalidPattern as e:
        type(str(e))
    else:
        raise Exception("InvalidPattern.__str__() returned unicode")
    trace.set_verbosity_level(trace.NO_TRACE)

# Generated at 2022-06-14 06:16:32.584772
# Unit test for method __getattr__ of class LazyRegex
def test_LazyRegex___getattr__():
    """Test that LazyRegex.__getattr__() handles all the attributes
       which could be returned.
    """
    from bzrlib.patiencediff import IS_DEFAULT
    import bzrlib.patiencediff as patiencediff
    # Import this to get the LazyRegex in the module namespace
    import bzrlib.patiencediff_regex as patiencediff_regex
    # This list is the intersection of LazyRegex._regex_attributes_to_copy
    # and the special methods mentioned in
    # http://docs.python.org/2/reference/datamodel.html#specialnames
    # (which should be returned instead of calling __getattribute__)

# Generated at 2022-06-14 06:16:38.455744
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """InvalidPattern.__unicode__() should return a unicode object."""
    # Create an instance of InvalidPattern.
    invalid_pattern = InvalidPattern('foo')
    # Test that the unicode representation of the InvalidPattern object
    # is a unicode object.
    if not isinstance(unicode(invalid_pattern), unicode):
        raise AssertionError(
            "unicode(invalid_pattern) should be of type unicode.")

# Generated at 2022-06-14 06:16:45.441572
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    import bzrlib.osutils as osutils
    from bzrlib.i18n import gettext

    # should always return a str object never a unicode object.
    def check_str_type(pattern):
        pat = InvalidPattern(pattern)
        u = unicode(pat)
        s = str(pat)
        # unicode(s) must fail
        try:
            unicode(s)
        except UnicodeDecodeError:
            # pass
            pass
        else:
            raise AssertionError(
                "str(InvalidPattern) must return a str object")
        # unicode(s) must be equal to unicode(pat)
        if u != unicode(s):
            raise AssertionError(
                "unicode(str(InvalidPattern)) must be equal to unicode(InvalidPattern)")
       

# Generated at 2022-06-14 06:16:49.426833
# Unit test for method __getattr__ of class LazyRegex
def test_LazyRegex___getattr__():
    """Test LazyRegex.__getattr__."""
    r = LazyRegex([r'\d'], {})
    assert r.pattern == '\\d'


# Generated at 2022-06-14 06:16:59.812253
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    # This test is here as a sample to check that a pattern that uses __unicode__
    # and __str__ on the same exception class can work. Every pattern that
    # implements its own exception should have a test like this.
    # The test uses the exception InvalidPattern that is defined in this module.
    # This exception has its own format string, __unicode__ and __str__ methods.
    u = u'This is the message'
    class MyException(InvalidPattern):
        def _format(self):
            return u


    class TestInvalidPattern___str__(tests.TestCase):

        def test_get_message(self):
            e = MyException('This is the message')
            # The next line will call __str__ of the exception which
            # will return unicode. We check that the returned unicode
            # object is the correct one

# Generated at 2022-06-14 06:17:13.310773
# Unit test for method __getattr__ of class LazyRegex
def test_LazyRegex___getattr__():
    """LazyRegex.__getattr__ method should compile regex on demand

    only if is actually needed.
    """
    # The proxy object should not be compiled at all
    # if nothing is required from it.
    proxy = LazyRegex(regex_args='a')
    assert proxy._real_regex is None

    for attr in LazyRegex._regex_attributes_to_copy:
        # Ask for an attribute that is expected to be copied from the
        # compiled regex.
        getattr(proxy, attr)
        # Now the proxy object should be compiled.
        assert proxy._real_regex is not None

        # The proxy object should not be compiled again if we ask for the
        # same attribute again.
        proxy._real_regex = None
        getattr(proxy, attr)
        assert proxy

# Generated at 2022-06-14 06:17:24.188562
# Unit test for method __getattr__ of class LazyRegex
def test_LazyRegex___getattr__():
    """method __getattr__ of class LazyRegex"""
    lr = LazyRegex(("(?ms)(?P<name>.*?)\\.(?P<type>[^\\.]+)$",), {})
    lr_name = lr.__getattr__("groupindex")
    lr_type = lr.__getattr__("pattern")

    # lr_name and lr_type should be equal to re.compile
    assert lr_name == re.compile("(?ms)(?P<name>.*?)\\.(?P<type>[^\\.]+)$",).groupindex
    assert lr_type == re.compile("(?ms)(?P<name>.*?)\\.(?P<type>[^\\.]+)$",).pattern


# Generated at 2022-06-14 06:17:39.835499
# Unit test for method __setstate__ of class LazyRegex
def test_LazyRegex___setstate__():
    r = LazyRegex()
    # We will call __setstate__ with a dict having the keys:
    # ['args', 'kwargs']
    # ... and we need to create a dict with keys:
    # ['_regex_args', '_regex_kwargs']
    # ...
    # That's why we replace 'args' with '_regex_args',
    # and 'kwargs' with '_regex_kwargs' keys
    state = dict(r.__getstate__(), args='_regex_args', kwargs='_regex_kwargs')
    r.__setstate__(state)
    # This doesn't really test anything

# Generated at 2022-06-14 06:17:48.133999
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Ensure InvalidPattern.__unicode__() gives a unicode object

    This test is checking for the following scenario:

    >>> u = u'hello world'
    >>> str(u)
    'hello world'

    Now we will convert the unicode string to a str
    in a different encoding:

    >>> from bzrlib.tests import test_pyutils
    >>> e = test_pyutils.TestCase.encode_as('unicode-internal', u)
    >>> str(e)
    'hello world'
    >>> type(e)
    <type 'str'>
    >>> test_pyutils.TestCase.decode_as('unicode-internal', e)
    u'hello world'
    """
    import bzrlib.osutils
    # Test the unicode path through __unicode__
    e = Invalid

# Generated at 2022-06-14 06:17:59.185493
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    string = u"\xe3\xb3\xab\xe3\xb3\xab"
    msg = "Foo"
    # This will still be a Python 2 str, not a Python 3 bytes.
    fmt = "%(msg)s (str %(string)s)"
    e = InvalidPattern(msg)
    expected = "Foo (str %s)" % repr(string)
    if isinstance(expected, unicode):
        expected = expected.encode('utf-8')
    e._fmt = fmt
    e.string = string
    # __unicode__ must return unicode
    observed = e.__unicode__()
    if isinstance(observed, unicode):
        observed = observed.encode('utf-8')
    assert expected == observed
    # __str__ must return str
    observed = e

# Generated at 2022-06-14 06:18:04.764672
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """test_InvalidPattern___unicode__
    check that InvalidPattern.__unicode__ always returns a unicode object"""
    from bzrlib import i18n

    i18n.install_gettext_translations()

    ip = InvalidPattern("something invalid")
    assert isinstance(unicode(ip), unicode)

    ip = InvalidPattern("something else invalid")
    assert isinstance(unicode(ip), unicode)

# Generated at 2022-06-14 06:18:12.997320
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """InvalidPattern.__unicode__ should return a unicode object"""
    # Test that __unicode__ returns a unicode object
    e = InvalidPattern('a')
    u = e.__unicode__()
    assert isinstance(u, unicode), ("__unicode__ returned a %r instead of "
                                     "unicode" % type(u))
    # Test that __unicode__ returns the same string as __str__
    s = e.__str__()
    assert isinstance(s, str), ("__str__ returned a %r instead of "
                                 "str" % type(s))
    assert s == u.encode('utf-8'), ("__unicode__ returned '%s' instead of '%s'" %
                                    (u.encode('utf-8'), s))



# Generated at 2022-06-14 06:18:18.040351
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """InvalidPattern objects should be able to be unicode"""
    try:
        raise InvalidPattern('test')
    except InvalidPattern as e:
        if not isinstance(unicode(e), unicode):
            raise AssertionError('InvalidPattern.__unicode__() is broken')

# Generated at 2022-06-14 06:18:21.333648
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    e = InvalidPattern(None)
    e._fmt = 'MSG: %(msg)s'

    assert str(e) == 'MSG: None'

# Generated at 2022-06-14 06:18:24.686196
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    msg = u"Invalid pattern: 'a'"
    ip = InvalidPattern(msg)
    # It is a unicode string
    assertEqual(ip.__str__(), msg)

# Generated at 2022-06-14 06:18:29.089085
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    from bzrlib import (
        errors,
        )
    from bzrlib.i18n import gettext
    errors.escape_exception_message('foo')
    gettext('foo')

# Generated at 2022-06-14 06:18:40.182490
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """Test method __str__ of class InvalidPattern

    The test is a bit "artificial" because it doesn't raise an exception
    but it is checking that exceptions pass through the __str__ of
    InvalidPattern"""
    # Create a dummy string
    s = 'A' * 1024  # 1k
    # Create a message
    msg = 'Pattern is too long'
    e = InvalidPattern(msg)
    # Add it directly to the exception
    e._preformatted_string = s
    # Check that the message is not truncated
    r = str(e)
    assert(len(r) == len(s))
    assert(r == s)

# Generated at 2022-06-14 06:18:51.304793
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Test method __unicode__ of class InvalidPattern

    Test what is in bug #1491:
    http://bugs.launchpad.net/bzr/+bug/1491
    """
    testee = InvalidPattern("1 %(msg)s", msg="2 %(msg)s", msg="3")
    # should not raise an exception
    str(testee)

# Generated at 2022-06-14 06:18:58.461608
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    try:
        raise InvalidPattern('test\n')
    except InvalidPattern as e:
        assert str(e) == 'Invalid pattern(s) found. "test\n"'
    try:
        raise InvalidPattern('test%s')
    except InvalidPattern as e:
        assert str(e) == 'Unprintable exception InvalidPattern:' \
            ' dict={\'msg\': \'test%s\'}, fmt=\'Invalid pattern(s) found. %(msg)s\', error=KeyError("msg",)'

# Generated at 2022-06-14 06:19:02.978889
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """__unicode__ should return a unicode object."""
    msg = 'a message'
    e = InvalidPattern(msg)
    u = e.__unicode__()
    assert isinstance(u, unicode)
    assert u == msg

# Generated at 2022-06-14 06:19:05.446553
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)

# Generated at 2022-06-14 06:19:14.729927
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Test InvalidPattern unicode conversion

    :return What the method returns
    """
    from bzrlib.i18n import gettext
    # start with a non-unicode message
    e = InvalidPattern('foo')
    assert e._format() == 'foo'
    # now give it a unicode message
    e = InvalidPattern('\xc9')
    assert isinstance(e._format(), unicode)
    # preformatted messages are already formatted
    e._preformatted_string = 'bar'
    assert e._format() == 'bar'
    assert e._get_format_string() is None
    # check gettext support works
    e._fmt = '%(msg)s'
    assert e._get_format_string() == '%(msg)s'

# Generated at 2022-06-14 06:19:19.931245
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    try:
        raise InvalidPattern('message')
    except InvalidPattern as e:
        actual = str(e)
        expected = 'Unprintable exception InvalidPattern: dict={}, fmt=None, error=None'
        assert actual == expected

# Generated at 2022-06-14 06:19:33.156737
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """This test was added because the output of InvalidPattern has changed.
    The test will fail if it doesn't contain the substring "Invalid pattern(s) found."
    """
    from bzrlib.i18n import (
        gettext,
        set_output_encoding,
        )
    set_output_encoding('utf8')
    test_msg = gettext(u'Invalid pattern(s) found.')
    # Note: InvalidPattern will get the msg from LazyRegex and then use it
    # to construct the full message.
    # So we have to construct the same msg here.
    # TODO: Just test the full msg.

# Generated at 2022-06-14 06:19:35.804043
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    try:
        raise InvalidPattern("It doesn't work.")
    except BaseException as e:
        assert str(e) == "It doesn't work."

# Generated at 2022-06-14 06:19:46.763534
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    import sys
    def check(expected, input, description):
        if sys.version_info[0] == 2:
            test_kind = 'unicode'
        else:
            test_kind = 'str'
        def format_error(m, kind, error):
            return ("invalid %s from %s.%s: %s"
                    % (kind, description, m, error))
        actual = getattr(input, m)()
        if isinstance(expected, str):
            try:
                expected = expected.decode('utf8')
            except UnicodeDecodeError:
                raise AssertionError(
                    format_error(
                        m, test_kind,
                        'expected str can not be decoded: %r' % expected))

# Generated at 2022-06-14 06:19:53.366650
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    # without localized messages
    e = InvalidPattern('foo')
    s = str(e)
    u = unicode(e)
    # with formatted localized messages
    e._fmt = 'bar %(msg)s'
    s = str(e)
    u = unicode(e)


# Generated at 2022-06-14 06:20:04.857968
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    # Tests that __str__() does not raise an exception.
    # All other aspects of InvalidPattern should be tested by
    # test_lazy_compile or test_regex.
    import traceback
    from bzrlib.i18n import gettext

    _fmt = ('An invalid regular expression was encountered: "%(bad_regex)s"')
    e = InvalidPattern('invalid')
    e._fmt = _fmt
    e.bad_regex = 'foo.*'
    e.offset = 1
    try:
        raise e
    except InvalidPattern:
        traceback.print_exc()
        gettext(_fmt)

# Generated at 2022-06-14 06:20:10.877316
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    from bzrlib.i18n import gettext
    ignored_exception = InvalidPattern(gettext('exception ignored'))
    unicode(ignored_exception)
    ignored_exception._fmt = gettext('exception %(msg)s ignored')
    unicode(ignored_exception)

# Generated at 2022-06-14 06:20:16.663302
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    from bzrlib.i18n import gettext
    t = InvalidPattern('foo')
    assert t._get_format_string() is None
    t = InvalidPattern(_fmt='bar')
    assert t._get_format_string() == gettext(u'bar')
    assert unicode(t) == gettext(u'bar')

# Generated at 2022-06-14 06:20:21.148834
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Test for method __unicode__ of class InvalidPattern"""
    from bzrlib.i18n import gettext
    gettext('abcd')
    from bzrlib.i18n import fix_user_option_unicode_errors
    fix_user_option_unicode_errors()
    ip = InvalidPattern('abcd')
    unicode(ip)


# Generated at 2022-06-14 06:20:34.705053
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Test method __unicode__

    Invoke with a guess at the available encodings to produce a variety of
    unicode objects.
    """
    import codecs
    for codec_name in ['ascii', 'utf8', 'utf16', 'utf32']:
        codec = codecs.lookup(codec_name)
        utf8_s = 'hello world'
        u = unicode(utf8_s, encoding=codec_name)
        e = InvalidPattern(u)
        expected_u = unicode(utf8_s + ' ' + str(e.msg), encoding=codec_name)
        s = str(e)
        expected_s = codec.encode(expected_u)[0]

# Generated at 2022-06-14 06:20:41.131435
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Test that InvalidPattern.__unicode__() don't fail.

    There is a problem when using a pattern with non-ascii chars.
    https://bugs.launchpad.net/bzr/+bug/404532
    """
    pat = u'\u6d77\u5916\u8499'
    e = InvalidPattern(pat)
    unicode(e)
    str(e)

# Generated at 2022-06-14 06:20:54.306754
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    import sys
    import bzrlib.errors
    from bzrlib.i18n import _i18n_enabled
    class bzrlog(object):
        def __init__(self):
            self.log = []
        def info(self, message):
            self.log.append(message)
    logger = bzrlib.errors._get_exception_logger()
    log_handler = bzrlog()
    logger.addHandler(log_handler)

# Generated at 2022-06-14 06:20:59.595576
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    # test that the various __str__ methods are consistent
    err = InvalidPattern('foo')
    s = str(err)
    u = unicode(err)
    assert s == u.encode('UTF8')

# Generated at 2022-06-14 06:21:11.819132
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    from bzrlib.i18n import gettext
    from bzrlib.i18n import _get_cached_translation_functions
    # InvalidPattern changes the way its instance is displayed, do not
    # confuse it with a _fmt parameter set to None
    class MyInvalidPattern(InvalidPattern):
        _fmt = None

    class MyInvalidPattern2(MyInvalidPattern):
        _fmt = Mock(side_effect=AttributeError())

    class MyInvalidPattern3(MyInvalidPattern):
        _fmt = Mock(return_value=None)

    class MyInvalidPattern4(MyInvalidPattern):
        _fmt = Mock(return_value="")

    class MyInvalidPattern5(MyInvalidPattern):
        _fmt = None
        _preformatted_string = Mock(return_value="")


# Generated at 2022-06-14 06:21:22.222920
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Test method __unicode__ of class InvalidPattern"""

    class MyBadError(InvalidPattern):
        _fmt = 'My bad error %(msg)s'

    e = MyBadError('oops')
    assert str(e) == str('My bad error oops')
    assert unicode(e) == unicode('My bad error oops')

    e = MyBadError(u'oops \u1234')
    assert str(e) == str('My bad error oops \xe1\x88\xb4')
    assert unicode(e) == unicode('My bad error oops \u1234')

# Generated at 2022-06-14 06:21:37.428165
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Test method InvalidPattern.__unicode__ for string and unicode patterns.

    This is a regression test for bug #836033.
    """

# Generated at 2022-06-14 06:21:45.490452
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """InvalidPattern.__str__ should return a 'str' object."""
    error_msg = 'hello'
    e = InvalidPattern(error_msg)
    s = str(e)
    assert isinstance(s, str), "%r is not a str instance" % s
    assert error_msg in s, "%r should contain '%s'" % (s, error_msg)


# Generated at 2022-06-14 06:21:51.489998
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    from bzrlib.i18n import gettext
    old_gettext = gettext

    def localgettext(s):
        return s

    def localugettext(s):
        return s

    gettext = localgettext

    try:
        try:
            e = InvalidPattern('msg1')
            # This should return a utf8 encoded string
            e._get_format_string = lambda : '%(msg)s'
            str(e)
            # This should return a unicode object
            e._get_format_string = lambda : u'%(msg)s'
            unicode(e)
        except UnicodeDecodeError:
            raise AssertionError('This should not raise an UnicodeDecodeError')
    finally:
        gettext = old_gettext

# Generated at 2022-06-14 06:21:53.729173
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    msg = 'Test message'
    exc = InvalidPattern(msg)
    assert str(exc) == msg

# Generated at 2022-06-14 06:21:59.145117
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """InvalidPattern method __str__ keeps __init__ params"""
    exc = InvalidPattern('bad pattern')
    assert str(exc) == 'Invalid pattern(s) found. bad pattern'
    assert unicode(exc) == u'Invalid pattern(s) found. bad pattern'

# Generated at 2022-06-14 06:22:09.911389
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    from bzrlib.i18n import _i18n_plugin

    _i18n_plugin.set_output_encoding('utf8')
    err = InvalidPattern('error_message')
    assert str(err) == 'error_message'

    err._preformatted_string = unicode('preformatted_message')
    assert str(err) == 'preformatted_message'

    err._preformatted_string = 'preformatted_string'
    assert str(err) == 'preformatted_string'

    err._preformatted_string = unicode('preformatted_message')
    assert str(err) == 'preformatted_string'

    err._fmt = _i18n_plugin.ugettext(u'fmt_message')
    err.msg = unicode('msg_message')


# Generated at 2022-06-14 06:22:13.085506
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """InvalidPattern.__unicode__ does not fail on bytes and unicode."""
    # test for valid unicode and bytes
    m = 'invalid unicode'
    e = InvalidPattern(m)
    unicode(e)
    m = b'invalid bytes'
    e = InvalidPattern(m)
    unicode(e)
test_InvalidPattern___unicode__.__test__ = False


# Generated at 2022-06-14 06:22:17.147314
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """InvalidPattern.__unicode__ should return an unicode object."""
    class_ = InvalidPattern
    e = class_("Test")
    u = e.__unicode__()
    assert isinstance(u, unicode)

# Generated at 2022-06-14 06:22:20.068614
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """InvalidPattern.__unicode__() should return a unicode object"""
    ip = InvalidPattern("foo")
    assert isinstance(ip.__unicode__(), unicode)



# Generated at 2022-06-14 06:22:26.144945
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    from bzrlib.i18n import gettext
    gettext('Invalid pattern(s) found. Pattern "%(pattern)s" did not match')
    i = InvalidPattern('Pattern "pattern" did not match')
    s = gettext('Invalid pattern(s) found. %(msg)s') % {'msg': 'Pattern "pattern" did not match'}
    assert type(s) is str
    assert i.__str__() == s

# Generated at 2022-06-14 06:22:41.516885
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """Test for methods __str__ and __unicode__ of class InvalidPattern."""
    e = InvalidPattern(u'msg')
    e._preformatted_string = u'preformatted'
    assert str(e).decode('utf-8') == u'preformatted'
    assert unicode(e) == u'preformatted'

    e = InvalidPattern(u'msg')
    assert str(e).decode('utf-8') == u"Unprintable exception InvalidPattern: " \
                                     u"dict={'msg': u'msg'}, " \
                                     u"fmt=%(msg)s, error=None"

# Generated at 2022-06-14 06:22:44.793177
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 06:22:50.735024
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    from bzrlib.i18n import gettext
    old_gettext = gettext
    # Now we need to patch gettext so that we can test when the translation
    # is done.

# Generated at 2022-06-14 06:23:03.996446
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    for method in ('__str__', '__repr__', '__unicode__'):
        msg = 'pattern foo is invalid'
        try:
            raise InvalidPattern(msg)
        except InvalidPattern as e:
            s = getattr(e, method)()
            assert isinstance(s, str) # encoded as utf-8
            assert msg in s

    # Now check that custom format strings work
    e = InvalidPattern(msg)
    e._preformatted_string = 'preformatted message'
    s = e.__str__()
    assert s == 'preformatted message'

    # Check that format strings provided by the class work
    e = InvalidPattern('')
    e._fmt = 'Error %(msg)s'
    s = e.__str__()
    assert s == 'Error '

   

# Generated at 2022-06-14 06:23:12.187229
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    from bzrlib.i18n import gettext
    original_gettext = gettext
    def no_gettext(string):
        # Return the original string
        return string
    try:
        gettext = no_gettext
        pattern = InvalidPattern(
            "The pattern '%(pattern)s' is not valid: %(msg)s")
        pattern.pattern = 'abc'
        pattern.msg = 'all okay'
        # This should not raise a TypeError.
        pattern.__unicode__()
    finally:
        gettext = original_gettext

# Generated at 2022-06-14 06:23:17.783259
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    from bzrlib.i18n import gettext
    gettext("Invalid")
    gettext("pattern found.")
    gettext("pattern(s) found. %(msg)s")
    InvalidPattern("abc")
    e = InvalidPattern("abc")
    str(e)
    unicode(e)

# Generated at 2022-06-14 06:23:24.636431
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    import sys
    if sys.version_info < (3, 0):
        assert (InvalidPattern('test')) == InvalidPattern(u'test')
        assert str(InvalidPattern('test')) == str(u'test')
    else:
        assert (InvalidPattern('test')) == InvalidPattern('test')
        assert str(InvalidPattern('test')).encode('ascii') == b'test'

# Generated at 2022-06-14 06:23:32.674165
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """InvalidPattern.__str__ returns a str object."""
    class SomeError(Exception):
        """Dummy class for testing purposes"""

    # message ends with '\n'

# Generated at 2022-06-14 06:23:42.882132
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    # Test that __str__() always return a 'str' object
    str_unicode_encoded = "unicode str"
    foreign_language_encoded = u"hello".encode("utf-8")
    fmt = InvalidPattern(str_unicode_encoded)
    assert isinstance(str(fmt), str)
    fmt = InvalidPattern(foreign_language_encoded)
    assert isinstance(str(fmt), str)
    fmt = InvalidPattern(None)
    assert isinstance(str(fmt), str)

# Generated at 2022-06-14 06:23:47.027110
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """str(InvalidPattern) should return str, not unicode."""
    exc = InvalidPattern('invalid pattern')
    exc.foo = 'bar'
    assert isinstance(str(exc), str), str(exc)

# Generated at 2022-06-14 06:24:06.059766
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Test unicode conversion of InvalidPattern."""
    from bzrlib.tests import TestCase
    from bzrlib.i18n import gettext

    class Test(TestCase):
        """Test class for InvalidPattern unicode conversion"""

        def test_1(self):
            """Test unicode behavior of InvalidPattern."""
            exc = InvalidPattern('message2')
            # mock _get_format_string which returns a unicode object
            exc._get_format_string = lambda: unicode('message1 %(msg)s')
            self.assertEqual(unicode(exc), u'message1 message2')

        def test_2(self):
            """Test unicode behavior of InvalidPattern."""
            exc = InvalidPattern(u'message3')
            # mock _get_format_string which returns a str object
            exc._

# Generated at 2022-06-14 06:24:10.425329
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    u = InvalidPattern(u'test message')
    assert str(u) == 'test message'

    u = InvalidPattern(u'\xa7')
    assert str(u) == '\xc2\xa7'

# Generated at 2022-06-14 06:24:14.260722
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    e = InvalidPattern(u'bogus: %s')
    e.msg = u'\u001F'
    str(e) # Check that no exception is raised


from . import tests


# Generated at 2022-06-14 06:24:21.843748
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """Tests that InvalidPatterns are correctly printed"""
    import sys
    if sys.version_info[0] >= 3:
        # With Python 3, the __str__ method is called all the time, just like
        # the __unicode__ method was before.
        # So the real python3 test will be in test_InvalidPattern___unicode__
        return
    e = InvalidPattern('\xc3\xa7a va')
    assert str(e) == unicode(e).encode('utf-8')



# Generated at 2022-06-14 06:24:28.749198
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """Ensure that InvalidPattern can be stringified."""
    # This test ensures that the InvalidPattern class can be stringified.

    # create an InvalidPattern object
    invalid_pattern = InvalidPattern('This is a test.')
    # stringify the object
    message = str(invalid_pattern)
    # ensure that the stringified object is equal to the string message
    # attribute in the InvalidPattern object
    assert message == invalid_pattern.msg

# Generated at 2022-06-14 06:24:40.473024
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    from bzrlib.i18n import gettext
    gettext('foo')

    import sys
    if sys.version_info[0] > 2:
        exc = InvalidPattern('foo')
        expected = 'foo'
        result = str(exc)
    else:
        exc = InvalidPattern('foo')
        expected = 'foo'
        result = str(exc)
    assert result == expected

    # we don't want to translate _fmt strings in InvalidPattern
    if sys.version_info[0] > 2:
        exc = InvalidPattern('foo')
        expected = 'bar'
        exc._fmt = 'bar'
        result = str(exc)
    else:
        exc = InvalidPattern('foo')
        expected = 'bar'
        exc._fmt = 'bar'
        result = str(exc)
