

# Generated at 2022-06-14 06:14:51.200278
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """__unicode__ must return a unicode object and be able to handle
    objects without a _fmt attribute (eg. objects of the class
    UnprintableException which do not have a _fmt attribute set.
    """
    import bzrlib.trace
    exc1 = InvalidPattern("error message")
    if isinstance(exc1.__unicode__(), str):
        # can't use 'raise AssertionError' to raise an AssertionError because
        # it uses unicode.
        raise AssertionError("__unicode__ should return a unicode object")
    exc2 = bzrlib.trace.UnprintableException('foo')
    if isinstance(exc2.__unicode__(), str):
        raise AssertionError("__unicode__ should return a unicode object")

# Generated at 2022-06-14 06:14:57.784615
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """converting to unicode should be a noop"""
    ie = InvalidPattern(u'test')
    assert ie.__unicode__() == u'test'
    ie = InvalidPattern(u"""This is a test
    with a newline""")
    assert ie.__unicode__() == u"""This is a test
    with a newline"""


# Generated at 2022-06-14 06:15:08.957463
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """Test the method __str__ of the class InvalidPattern.

    As this is a class with special methods for formatting as a string,
    let's test that too. These methods come from bzrlib.trace.
    """

    from bzrlib.i18n import gettext
    from bzrlib.tests.i18n_tests import install_gettext_calls
    from StringIO import StringIO
    import sys

    # The strings we are going to test are all ascii, therefore we don't
    # need to set any locale to get English out of gettext

    # Let's override the default format string, which is a unicode string. We
    # force a unicode instance to test that it works with unicode.
    message = u'Test message %(msg)s'
    e = InvalidPattern(message)
    e._

# Generated at 2022-06-14 06:15:16.641915
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    from bzrlib import osutils
    enc = osutils._get_user_encoding()
    msg = unicode("Exception message", "utf-8")
    i = InvalidPattern("%s")
    i.msg = msg
    i._preformatted_string = ''
    exp = msg.encode(enc)
    obs = str(i)
    assert exp == obs, "%r != %r" % (exp, obs)

# Generated at 2022-06-14 06:15:27.496431
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Unit tests for method __unicode__ of class InvalidPattern"""
    # XXX: the following tests might fail on some systems if the
    #      gettext library is not properly configured.
    def call__unicode__(exc):
        """Helper function to return __unicode__ for an exception"""
        try:
            return unicode(exc)
        except:
            # python 2.6 does not have exc.__unicode__()
            return unicode(exc.__str__())
    exc = InvalidPattern('error message')
    u = call__unicode__(exc)
    if u != 'error message':
        raise AssertionError('Default behaviour for InvalidPattern.__unicode__'
                             ' is not to return _fmt message')
    exc.msg = None

# Generated at 2022-06-14 06:15:41.255685
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """InvalidPattern can be converted to unicode without crashing"""
    def _check_unicode(s):
        # We use s.startswith(u'Unprintable') rather than just bool(s) to
        # be defensive.
        if isinstance(s, unicode):
            if s.startswith(u'Unprintable'):
                return
        #if not isinstance(s, unicode):
        #   print 'test_InvalidPattern___unicode__: s=%r is not unicode' % (s,)
        raise AssertionError('test_InvalidPattern___unicode__: s=%r is not '
            'a unicode object starting with "Unprintable"' % (s,))
    invalid_regex_msg = 'Invalid regular expression'

# Generated at 2022-06-14 06:15:47.414039
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    import bzrlib.trace
    try:
        raise InvalidPattern('foobar')
    except InvalidPattern as e:
        # This is the expected output when run on a machine with a
        # UTF-8 locale.
        assert unicode(e) == u'Invalid pattern(s) found. foobar'
        # Now set a system encoding which is not UTF-8, and try again
        oldenc = bzrlib.trace._system_encoding
        bzrlib.trace._system_encoding = 'ascii'
        try:
            assert unicode(e) == u'Invalid pattern(s) found. foobar'
        finally:
            bzrlib.trace._system_encoding = oldenc

# Generated at 2022-06-14 06:15:58.360676
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """Unit test for method __str__ of class InvalidPattern"""
    import sys
    import StringIO
    # StringIO object to redirect sys.stderr
    sio = StringIO.StringIO()
    # save current sys.stdout
    old_stdout = sys.stderr
    # assign StringIO object to sys.stdout
    sys.stderr = sio

# Generated at 2022-06-14 06:16:05.479522
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """str(InvalidPattern) returns a correct string.

    This test ensures that the method __str__ of class InvalidPattern
    returns a correct string.
    """
    error = 'Text'
    msg = InvalidPattern(error)
    expected_result = 'Invalid pattern(s) found. "' + error + '"'
    result = str(msg)
    assert result == expected_result, 'Message is %s' % result

# Generated at 2022-06-14 06:16:14.565555
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """An invalid regex is reported as an InvalidPattern

    When a regex fails to compile, an InvalidPattern should be raised,
    with the invalid regex provided in the message. This is different
    to a re.error being raised, and was done so that the message is
    different for the user.

    The InvalidPattern object can be cast to unicode and this should
    provide the message.
    """
    # re.error is actually a subclass of ValueError
    # so we know that InvalidPattern is also a subclass of ValueError
    # and will therefore be caught here.
    try:
        _real_re_compile(r"a(b")
    except ValueError as e:
        pass
    else:
        raise AssertionError("Invalid regex did not raise an error.")
    if not isinstance(e, InvalidPattern):
        raise AssertionError

# Generated at 2022-06-14 06:16:27.083604
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    from bzrlib.i18n import gettext
    import StringIO
    try:
        _real_re_compile('[' + gettext('abc') + ']')
    except InvalidPattern as e:
        sio = StringIO.StringIO()
        e.write_invalid_reasons(sio)
        sio.seek(0)
        assert sio.read() == str(e)
    else:
        raise AssertionError('Expected InvalidPattern')


# Unit tests for method __str__ of class InvalidPattern and its subclasses

# Generated at 2022-06-14 06:16:39.825850
# Unit test for method __setstate__ of class LazyRegex
def test_LazyRegex___setstate__():
    """Test for LazyRegex.__setstate__

    This test checks that the state of the class LazyRegex, can be
    pickled. This is important to be able to pickle these objects.
    """
    import pickle
    lr = LazyRegex(args=("(.*)", ), kwargs={"flags": 0})
    lr_state = lr.__getstate__()
    lr.__setstate__(lr_state)
    assert lr._regex_args == ("(.*)", )
    assert lr._regex_kwargs == {"flags": 0}
    assert lr._real_regex is None
    lr.__getattr__('match')
    assert lr._real_regex is not None
    # Check that we still can get the attributes form the collapsed
    # regex

# Generated at 2022-06-14 06:16:44.646110
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Unit test for method __unicode__ of class InvalidPattern"""
    msg = "a message"
    s = InvalidPattern(msg)
    u = unicode(s)
    expected = _fmt%{'msg':msg}
    assert u == expected, 'Expected "%s", but got "%s"' % (expected, u)

# Generated at 2022-06-14 06:16:58.290668
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    import doctest
    if "setUp" in doctest.DocTestCase.setUp.im_func.func_globals:
        # We need to "reimport" doctest to avoid the setUp method of
        # DocTestCase that was defined in bzrlib.tests.
        # This will not work with python <= 2.4.
        del doctest.DocTestCase.setUp
        import doctest
    test = doctest.DocTestSuite('bzrlib.regex_lazy')
    suite = doctest.DocTestSuite('bzrlib.tests.test_regex_lazy')
    suite.addTest(test)
    runner = doctest.DocTestRunner()
    if runner.run(suite).failed:
        return 1
    else:
        return 0

# Generated at 2022-06-14 06:17:11.784628
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    from bzrlib.i18n import gettext

    class _InvalidPattern(InvalidPattern):
        _fmt = """The pattern '%(pattern)s' is invalid: %(msg)s"""

    def test_pattern(pattern, msg):
        """Test InvalidPattern.__unicode__ with parameters (pattern, msg).

        :param pattern: The value of parameter pattern
        :param msg: The value of parameter msg
        :return: True if the test was successful and False otherwise
        """
        # Don't translate this string so we can test automatic translation.
        ip = _InvalidPattern(pattern=pattern, msg=msg)
        u = ip.__unicode__()
        t = gettext(unicode(ip.__class__.__name__))

# Generated at 2022-06-14 06:17:16.269571
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    class MyInvalidPattern(InvalidPattern):
        _fmt = 'Error, %(msg)s'
    exc = MyInvalidPattern(msg='this is a message')
    if sys.version_info[0] == 2:
        assert isinstance(unicode(exc), unicode)
        assert isinstance(str(exc), str)
    else:
        assert isinstance(str(exc), str)


# Generated at 2022-06-14 06:17:22.890550
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    class InvalidPatternTest(InvalidPattern):
        _fmt = 'Test string %(non_ascii)s'
    i = InvalidPatternTest('abc')
    i.non_ascii = u'\N{SNOWMAN}'
    assert str(i) == 'Test string \xe2\x98\x83'

# Generated at 2022-06-14 06:17:31.940876
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Test that InvalidPattern.__unicode__ works correctly."""
    # setup
    exception = InvalidPattern('Exception message is unicode.')
    # call
    result = unicode(exception)
    # check
    # This test doesn't make sense, because it doesn't test the string
    # returned by exception. In fact it creates a _gettext_wrapper class
    # which is not pyrexed and has no __eq__ method.
    #self.assertEquals('Exception message is unicode.', unicode(exception))
    pass


# Generated at 2022-06-14 06:17:45.913414
# Unit test for method __getattr__ of class LazyRegex
def test_LazyRegex___getattr__():
    """Unit test method __getattr__ of class LazyRegex."""
    import testtools

    # Test all public methods are treated, including __getitem__
    lazy = LazyRegex(('^ab$',))
    for attr in LazyRegex._regex_attributes_to_copy + ['__getitem__']:
        testtools.TestCase.assertRaises(
            testtools.TestCase, getattr(lazy, attr))

    # Test access to private methods
    lazy = LazyRegex(('^ab$',))
    testtools.TestCase.assertRaises(testtools.TestCase,
        getattr(lazy, '_compile_and_collapse'))

    # Test the private attribute _real_regex
    lazy = LazyRegex(('^ab$',))
    test

# Generated at 2022-06-14 06:17:58.630133
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Method __unicode__ of class InvalidPattern must return a unicode object.

    We want to ensure that method __unicode__ always returns a unicode object.
    This is to avoid that the string returned is a str object in Python 2 and
    an unicode object in Python 3.
    """
    from bzrlib.i18n import gettext
    gettext(unicode('message')) # Force gettext to use unicode() for
                                # the default encoding.
    e = InvalidPattern('message')
    assert isinstance(e.__unicode__(), unicode)
    e._preformatted_string = 'message'
    assert isinstance(e.__unicode__(), unicode)
    e._preformatted_string = u'message'
    assert isinstance(e.__unicode__(), unicode)

# Generated at 2022-06-14 06:18:12.178955
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Test for InvalidPattern._format().

    This test is needed for coverage. It is not clear why InvalidPattern.__str__
    is not called from tests.
    """
    from bzrlib.i18n import gettext

    def check_exception(msg, exp_msg):
        e = InvalidPattern(msg)
        # override the message, so that the test is independent of gettext
        e._preformatted_string = exp_msg
        u = unicode(e)
        if gettext.get_translation().__class__.__name__ == 'NullTranslations':
            # if gettext is disabled, _format() will return the default msg
            assert(u == exp_msg)
        else:
            assert(u == unicode(gettext(exp_msg)))


# Generated at 2022-06-14 06:18:25.004294
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """Test for InvalidPattern.__str__

    Ensure that repr, str and unicode return a non empty string and
    that repr, str and unicode return all a str, unicode or
    utf-8-encoded unicode object.
    """
    e = InvalidPattern("foo")
    r = repr(e)
    s = str(e)
    u = unicode(e)
    assert len(r) > 0
    assert isinstance(r, str)
    assert len(s) > 0
    assert isinstance(s, str)
    assert len(u) > 0
    assert isinstance(u, unicode)
    # str and repr should give the same result
    assert r == s
    # str and unicode should not give the same result (they should not be
    # a utf-8-encoded unicode

# Generated at 2022-06-14 06:18:32.292703
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """This test fails if there is an error in the unicode format string

    It would be a good idea to add a test for every format string
    """
    error = InvalidPattern('None of the patterns %(pat1)s or %(pat2)s match'
                           ' the given string, so it can not be parsed.')
    error.pat1 = 'A'
    error.pat2 = 'B'

# Generated at 2022-06-14 06:18:38.585794
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    import doctest
    from bzrlib.i18n import gettext
    from bzrlib.i18n import set_output_encoding
    set_output_encoding('utf-8')
    doctest.testmod(optionflags=doctest.ELLIPSIS,
                    extraglobs={'gettext': gettext})

# Generated at 2022-06-14 06:18:45.972301
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    ip = InvalidPattern('Test message')
    expected_str = """Unprintable exception InvalidPattern: dict={'msg': 'Test message'}, fmt=None, error=None"""
    assert str(ip) == expected_str
    expected_unicode = """Unprintable exception InvalidPattern: dict={'msg': 'Test message'}, fmt=None, error=None"""
    assert unicode(ip) == expected_unicode

# Generated at 2022-06-14 06:18:57.798674
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Unit test for method __unicode__ of class InvalidPattern"""

    # try with a normal call
    try:
        raise InvalidPattern('msg')
    except InvalidPattern as e:
        assert unicode(e) == u'msg'
        assert str(e) == 'msg'
        assert repr(e) == "InvalidPattern(u'msg')"

    #  raise with a preformatted message
    try:
        raise InvalidPattern('msg')
    except InvalidPattern as e:
        f = e._fmt
        e._fmt = 'Invalid pattern(s) found. %(msg)s'
        assert unicode(e) == u'Invalid pattern(s) found. msg'
        assert str(e) == 'Invalid pattern(s) found. msg'
        # __repr__ must return a ascii string

# Generated at 2022-06-14 06:19:09.317762
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """__unicode__ must return a unicode object.

    The method __unicode__ must return a unicode object.
    """
    from bzrlib.tests import TestCase
    from bzrlib import errors
    # We need to set an environment that will ensure that we are using
    # a unicode gettext function.
    self = TestCase()
    errors._set_unicode_gettext_for_testing(self)
    e = InvalidPattern('msg')
    self.assertTrue(isinstance(unicode(e), unicode))
    # Now we remove the patches on gettext
    errors._unset_unicode_gettext_for_testing(self)

# Generated at 2022-06-14 06:19:18.086366
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    from bzrlib import i18n
    msg = 'You can only register when you are logged in.'
    e = InvalidPattern(msg)
    # change current locale to 'en_AU'
    old_locale = i18n.set_user_option('locale', 'en_AU')
    try:
        # check __unicode__
        unicode_e = unicode(e)
        if unicode_e != msg:
            raise AssertionError(
                "__unicode__ must return the original message in en_AU locale")
    finally:
        i18n.set_user_option('locale', old_locale)



# Generated at 2022-06-14 06:19:22.451422
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """Method __str__ of class InvalidPattern should return a str object

    This test verifies that the implementation of __str__() always returns a
    str object, even if the _preformatted_string attribute is set to a unicode
    object.
    """
    message = "An error occurred"
    e = InvalidPattern(message)
    assert message == str(e)
    e._preformatted_string = u"\u20ac"
    assert "u'\\u20ac'" == repr(str(e))

# Generated at 2022-06-14 06:19:34.749274
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Test method __unicode__ of class InvalidPattern.

    This is used to verify that the cached information
    is valid when the exception is created in one thread
    and the __unicode__ method is called in another.
    """
    from bzrlib import tests
    from bzrlib.i18n import gettext
    from bzrlib.i18n import install_gettext_translations
    from bzrlib.i18n import LazyIndexedTranslations
    from bzrlib.i18n import set_context
    from bzrlib.i18n import get_context
    from bzrlib.i18n import get_thread_translations
    from bzrlib.i18n import set_thread_translations
    from bzrlib.i18n import setup_translation_logging

   

# Generated at 2022-06-14 06:19:44.843021
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """Test for method __str__ of class InvalidPattern"""
    from bzrlib.tests import TestCase
    error = InvalidPattern('error message')
    TestCase.assertEqual(str(error), 'error message')
    TestCase.assertEqual(unicode(error), u'error message')

# Generated at 2022-06-14 06:19:53.383407
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    # Unicode format string
    class Foo(InvalidPattern):
        _fmt = u"format %(invalid)s"
    msg = Foo(msg="invalid")
    msg.invalid = u"invalid"
    str(msg)
    msg.invalid = "invalid"
    str(msg)
    msg.invalid = u"invalid".encode("utf8")
    str(msg)
    # ASCII format string
    class Bar(InvalidPattern):
        _fmt = "format %(invalid)s"
    msg = Bar(msg="invalid")
    msg.invalid = u"invalid"
    str(msg)
    msg.invalid = "invalid"
    str(msg)
    msg.invalid = u"invalid".encode("utf8")
    str(msg)


# Generated at 2022-06-14 06:19:57.973037
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    class MyException(InvalidPattern):
        _fmt = 'This is my exception: %(msg)s'
    e = MyException('there is a bug')
    u = unicode(e)
    assert u == u'This is my exception: there is a bug', u


# Generated at 2022-06-14 06:20:06.017249
# Unit test for method __getattr__ of class LazyRegex
def test_LazyRegex___getattr__():
    """Ensure that LazyRegex.__getattr__ works properly"""
    # Create a dummy subclass of LazyRegex in order to test __getattr__,
    # its aim is to track all calls made to the _real_regex member.
    class DummyRegex(LazyRegex):
        calls = 0
        def __getattr__(self, attr):
            self.calls += 1
            return LazyRegex.__getattr__(self, attr)

    # Check that the __getattr__ method is called once to get an attribute
    # value, and that the proxy object is collapsed into a _sre.SRE_Pattern
    # object.
    regex = DummyRegex(("foo", ))
    result = getattr(regex, "pattern")
    assert result == "foo"
    assert Dummy

# Generated at 2022-06-14 06:20:13.433587
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """__unicode__ for InvalidPattern should return a unicode object

    :expected: str object
    """
    expected_msg = u'Unprintable exception InvalidPattern: dict={}, fmt=None, error=None'
    ip = InvalidPattern('')
    actual_msg = ip.__unicode__()
    assert actual_msg == expected_msg, 'expected unicode return'

# Generated at 2022-06-14 06:20:20.414756
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    from bzrlib.i18n import _i18n_string
    from bzrlib.i18n import gettext
    try:
        raise InvalidPattern('PARSE_ERROR: ...')
    except InvalidPattern as exc:
        # __unicode__ must return unicode, not str
        # exc is already a unicode because gettext returns unicode
        assert isinstance(exc, unicode)
        assert exc == u'PARSE_ERROR: ...'



# Generated at 2022-06-14 06:20:34.283830
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """test method __str__ of class InvalidPattern

    This is also a test of method _format of this class which is
    used by __str__.
    """
    # Create an exception with a non-ASCII message.
    e = InvalidPattern(u'Non-ASCII message: \u1234.')
    # Use the default encoding to test __str__().
    def_encoding = 'utf8'
    # __str__() must return a str object.
    assert isinstance(e.__str__(), str)
    # Use default encoding to get a unicode object from a str object.
    unicode_def_encoding = unicode(e.__str__(), def_encoding)
    # __unicode__() must return a unicode object.
    assert isinstance(e.__unicode__(), unicode)
    #

# Generated at 2022-06-14 06:20:46.617355
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Test method __unicode__ of class InvalidPattern"""
    # Create an InvalidPattern instance
    ip = InvalidPattern('msg')
    # Check that __unicode__() returns a unicode object
    assert isinstance(ip.__unicode__(), unicode), \
        "InvalidPattern.__unicode__() didn't return a unicode object"
    # Check that __unicode__() returns the expected value
    assert ip.__unicode__() == 'Invalid pattern(s) found. msg', \
        "InvalidPattern.__unicode__() didn't return the expected value"
    # Set the preformatted_string attribute
    ip._preformatted_string = 'test value'
    # Check that __unicode__() returns the expected value

# Generated at 2022-06-14 06:20:53.820395
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """Check that InvalidPattern.__str__ returns a str, not a unicode"""
    import locale
    locale.setlocale(locale.LC_ALL, 'en_GB.UTF-8')
    try:
        enc = locale.nl_langinfo(locale.CODESET)
    except AttributeError:
        enc = locale.getdefaultlocale()[1]

    x = InvalidPattern('foo')
    assert isinstance(x.__str__(), str), x.__str__()

# Generated at 2022-06-14 06:21:03.278804
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    from bzrlib import trace
    try:
        import StringIO
    except ImportError:
        from io import StringIO
    # 'u' is unset
    exception = InvalidPattern('')
    trace.enable_default_logging()
    trace.basic_config()
    # To catch what trace.warning write on stderr
    stderr = StringIO.StringIO()
    fd2 = trace._sys.stderr
    trace._sys.stderr = stderr
    try:
        unicode(exception)
    finally:
        trace._sys.stderr = fd2

# Generated at 2022-06-14 06:21:19.872668
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    # Regression test for launching error:
    # InvalidPattern('"%(a)s" "b%(c)s"' % {'c': 'd', 'a': 'e'})
    # which was accepted by the corrupt _format() of the bzr 0.18
    # and crashes python 2.6
    #
    # The next 3 lines used to launch a crash before the fix of bug #113404
    # ('InvalidPattern.__unicode__() failed to handle unicode pattern'):
    f = InvalidPattern('"%(a)s" "b%(c)s"')
    x = {'c': 'd', 'a': 'e'}
    f % x


# We want to use the lazy compile by default, but we also want to be able
# to test with the regular compile.
install_lazy_comp

# Generated at 2022-06-14 06:21:32.578631
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """A test for method __unicode__ of class InvalidPattern"""
    # It should work with any Unicode character in message
    u = InvalidPattern(u'\u1234').__unicode__()
    # No exception should be raised
    u = InvalidPattern(u'\u1234').__unicode__()
    # It should work with any Unicode character in exception
    try:
        raise InvalidPattern(u'\u1234')
    except InvalidPattern as e:
        u = e.__unicode__()
        # No exception should be raised
        u = e.__unicode__()
    # It should work with any Unicode character in exception, format string,
    # and message

# Generated at 2022-06-14 06:21:45.288782
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    from bzrlib.i18n import gettext
    e = InvalidPattern('test message')
    e._preformatted_string = u'Preformated test message'
    assert e.__unicode__() == u'Preformated test message'
    e._preformatted_string = u'Преформатированное сообщение'
    assert e.__unicode__() == u'Преформатированное сообщение'
    e._fmt = 'Test message: %(msg)s'
    gettext(u'Test message: %(msg)s', 'regex')

# Generated at 2022-06-14 06:21:47.757249
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    from testtools import TestCase
    class TestInvalidPattern(TestCase):
        def test_InvalidPattern(self):
            """InvalidPattern.__str__() works"""
            self.assertEquals('invalid', str(InvalidPattern('invalid')))

# Generated at 2022-06-14 06:22:01.117565
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    from bzrlib.i18n import gettext
    from StringIO import StringIO
    import sys
    # Patch stdout for testing
    old_stdout = sys.stdout
    sys.stdout = StringIO()

# Generated at 2022-06-14 06:22:06.000389
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """InvalidPattern needs to override __unicode__ as well as __str__"""
    class MyException(InvalidPattern):
        _fmt = "MyException: %(msg)s"
        def __init__(self, msg):
            self.msg = msg
    e = MyException('foo')
    str(e)
    unicode(e)

# Generated at 2022-06-14 06:22:17.625829
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    from bzrlib.i18n import gettext
    from bzrlib.tests.i18n import get_localizations
    from bzrlib import _i18n_pyx

    for translation_func in (gettext, _i18n_pyx.gettext):
        e = InvalidPattern(b'error')
        assert str(e).startswith('Unprintable exception')
        e = InvalidPattern('foo')
        assert str(e).startswith('Unprintable exception')
        e = InvalidPattern(u'foo')
        assert str(e).startswith('Unprintable exception')
        e = InvalidPattern('foo')
        e._preformatted_string = 'foo'
        assert str(e) == 'foo'
        e._preformatted_string = 'bar'

# Generated at 2022-06-14 06:22:26.275021
# Unit test for method __getattr__ of class LazyRegex

# Generated at 2022-06-14 06:22:37.975927
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """InvalidPattern.__str__ should allow unicode formatting string

    This test checks that the Python 2.x and Python 3.x versions of __str__
    handle unicode the same way. The __unicode__ method allows use of unicode
    formatting strings, but the __str__ method will only allow unicode strings
    if the UTF-8 encoding of the unicode string can be interpreted as ascii.
    """
    class Subclass(InvalidPattern):
        _fmt = u'Unicode format string: %(msg)s'

    exc1 = Subclass(u'Unicode string 1')
    exc2 = Subclass(u'Unicode string 2')
    exc3 = Subclass(u'Unicode string 3 \u1234')

# Generated at 2022-06-14 06:22:49.545021
# Unit test for method __getattr__ of class LazyRegex
def test_LazyRegex___getattr__():
    """Unit test for method __getattr__ of class LazyRegex.

    This test will check if method __getattr__ of class LazyRegex invokes
    _collapse_and_compile() method. Plus, it will check if method
    _collapse_and_compile() actually copies attributes of real regex to proxy
    regex.
    """

    # Create a proxy regex
    def fake_compile(*args, **kwargs):
        """Fake real compile method of module re.
        """
        pass

    saved_compile = _real_re_compile
    _real_re_compile = fake_compile
    proxy_regex = LazyRegex()


# Generated at 2022-06-14 06:23:06.906533
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """This is a test for the correctness of the method __unicode__ of
    class InvalidPattern.
    """
    from bzrlib.i18n import gettext
    from bzrlib import osutils

    msg = u'a message'
    i = InvalidPattern(msg=msg)
    result = i.__unicode__()
    expected = msg
    assert result == expected

    # We continue to check that the method __unicode__ returns a unicode
    # object, not a str.
    msg = 'a message'
    i = InvalidPattern(msg=msg)
    result = i.__unicode__()
    expected = osutils.safe_unicode(msg)
    assert result == expected

    msg = 123
    i = InvalidPattern(msg=msg)
    result = i.__unicode__()
    expected

# Generated at 2022-06-14 06:23:16.954155
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Encoding of InvalidPattern(_fmt) has been changed

    Should be change in Python 3.0 to solve a bug (not raising an
    UnicodeEncodeError).
    """
    import locale
    if locale.getpreferredencoding() == 'UTF-8':
        # this test is not applicable
        return
    locale.setlocale(locale.LC_ALL, 'fr_FR.ISO8859-15')

# Generated at 2022-06-14 06:23:21.001401
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """test that we can run InvalidPattern.__str__
    """
    from bzrlib import errors
    from bzrlib.lazy_regex import InvalidPattern

# Generated at 2022-06-14 06:23:27.620518
# Unit test for method __getattr__ of class LazyRegex
def test_LazyRegex___getattr__():
    """LazyRegex.__getattr__() returns attribute from _real_regex"""
    from bzrlib.tests import TestCase
    foo = LazyRegex(["hello"])
    foo._real_regex = "hello"
    foo.__getattr__("_real_regex")

test_LazyRegex___getattr__.__test__ = False # not a test



# Generated at 2022-06-14 06:23:39.738801
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Test method `__unicode__` of class InvalidPattern."""
    from bzrlib.i18n import gettext
    from bzrlib.i18n import set_strategy

    class TestInvalidPattern(InvalidPattern):
        _fmt = 'This is a test. %(msg)s'

    # __unicode__ must return a unicode object
    set_strategy('unittest') # to avoid changing the default encoding

    t = TestInvalidPattern('Error')
    # without calling gettext
    assert t.__unicode__() == u'This is a test. Error'
    # gettext is called
    assert gettext(t.__unicode__()) == u'This is a test. Error'

    # unknown exception while calling _format

# Generated at 2022-06-14 06:23:50.887877
# Unit test for method __unicode__ of class InvalidPattern

# Generated at 2022-06-14 06:23:55.899038
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """InvalidPattern.__unicode__ must return a unicode object."""
    e = InvalidPattern('test')
    assert isinstance(unicode(e), unicode)


# Generated at 2022-06-14 06:24:07.133240
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """Check __str__() return value of InvalidPattern."""
    # InvalidPattern._fmt is a unicode string
    e = InvalidPattern('msg')
    # Check if __str__() returns a unicode string.
    result = e.__str__()
    if isinstance(result, unicode):
        pass
    else:
        raise AssertionError('__str__() should return a unicode string')

    # InvalidPattern._fmt is a string
    e._preformatted_string = 'preformatted_msg'
    # Check if __str__() returns a unicode string.
    result = e.__str__()
    if isinstance(result, unicode):
        pass
    else:
        raise AssertionError('__str__() should return a unicode string')

# Generated at 2022-06-14 06:24:20.396996
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """Tests for method __str__ of class InvalidPattern:

    * Unicode characters are allowed as message for exceptions
    * Unicode characters are allowed in exception args when using __str__
    * str characters are allowed as message for exceptions
    * str characters are allowed in exception args when using __str__
    """
    from bzrlib import ui

    # Unicode in message
    if isinstance("exception message", unicode):
        msg = u'exception\u2014message'
    else:
        msg = 'exception\xe2\x80\x94message'
    e = InvalidPattern(msg)
    ui.ui_factory.show_error(e)

    # Unicode in exception arguments
    if isinstance("exception message", unicode):
        msg = u'exception\u2014message'

# Generated at 2022-06-14 06:24:31.746179
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """__str__ of InvalidPattern should always return an ascii string.

    Even if the underlying exception string isn't ascii.
    """
    from bzrlib.i18n import gettext
    from bzrlib.patiencediff import PatienceSequenceMatcher
    # create a string that is neither ascii nor utf8 encoded
    non_ascii_string = '\x82'
    # create a Patience sequence matcher with this string
    matcher = PatienceSequenceMatcher(None, non_ascii_string, '')