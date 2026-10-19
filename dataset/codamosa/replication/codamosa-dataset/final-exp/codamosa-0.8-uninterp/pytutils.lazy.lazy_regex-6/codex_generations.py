

# Generated at 2022-06-14 06:14:52.823994
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """Unit test for method __str__ of class InvalidPattern"""
    from bzrlib.i18n import gettext
    import sys
    if 'bzrlib.tests' in sys.modules:
        from bzrlib.tests import TestCase
        from bzrlib import tests

        class TestInvalidPattern(TestCase):
            """Unit test for method __str__ of class InvalidPattern"""
            def test___str__(self):
                msg = 'hello, world'
                err = InvalidPattern('hello, world')
                self.assertEqualDiff(str(err),
                                            gettext(msg))
            def test___str__empty_message(self):
                err = InvalidPattern('')
                self.assertEqualDiff(str(err), '')

# Generated at 2022-06-14 06:15:06.073229
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Test __unicode__ method of class InvalidPattern."""
    def compare_unicode_result(expected, e):
        """Compare expected and e.__unicode__() results."""
        # must work
        s = e.__unicode__()
        # must return unicode object
        assert isinstance(s, unicode)
        # must return expected value
        assert expected == s

    def compare_unicode_result_exception(e):
        """Compare expected and e.__unicode__() results when e raises
        an exception while calling e._format()."""
        # must work
        s = e.__unicode__()
        # must return unicode object
        assert isinstance(s, unicode)
        # must return expected value
        assert isinstance(s, unicode)

    #
    # 1 - test for

# Generated at 2022-06-14 06:15:13.937625
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Unit test for method __unicode__ of class InvalidPattern.

    This tests that __unicode__() will always return a unicode object, e.g.
    __unicode__ does not return a str object in python2 or a str object in
    python3.
    """
    i = InvalidPattern("message")
    assert isinstance(str(i), str)
    assert isinstance(unicode(i), unicode)

# Generated at 2022-06-14 06:15:25.939233
# Unit test for method __getattr__ of class LazyRegex
def test_LazyRegex___getattr__():
    """Tests __getattr__ of class LazyRegex
    """
    # LazyRegex has a __getattr__ method which when called for the first time,
    # creates a real _sre.SRE_Pattern object and saves it in the _real_regex
    # attribute. This method is called only when the _real_regex attribute
    # has not been set yet.
    # __getattr__ uses getattr to get the attribute from the _real_regex
    # attribute and returns it.
    # This tests checks that trying to access an attribute of LazyRegex
    # before _real_regex has been set causes it to be created and saved.
    # It also checks that trying to access it again doesn't create a new one.
    # Finally, it checks that trying to access an attribute of the _real_regex
    #

# Generated at 2022-06-14 06:15:36.795792
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    import bzrlib.trace
    bzrlib.trace.enable_default_logging()

    # Verify that InvalidPattern.__unicode__() works well with a
    # UnicodeEncodeError error raised while formatting the final
    # message.
    # This works by making sure that the original exception
    # is wrapped in an InvalidPattern.
    msg = u"This is a test"
    e = ValueError(msg)

# Generated at 2022-06-14 06:15:51.019336
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    from bzrlib.i18n import gettext

    # If the class doesn't have a _fmt string, the method should return unicode
    # string "Unprintable exception InvalidPattern: dict={}, fmt=None, error=None"
    cls = InvalidPattern
    obj = InvalidPattern(None)
    setattr(cls, '_fmt', None)
    assert unicode(obj) == gettext(u'Unprintable exception InvalidPattern: dict={}, fmt=None, error=None')

    # If the class has a _fmt string, the method should return unicode string
    # "%(msg)s" with the dict attribute value substituted
    cls = InvalidPattern
    obj = InvalidPattern(u'\xe9')
    setattr(cls, '_fmt', u'%(msg)s')

# Generated at 2022-06-14 06:15:59.021325
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Test method __unicode__ of class InvalidPattern"""
    b = InvalidPattern('Message')
    assert str(b) == u'Message'
    b = InvalidPattern('')
    assert str(b) == u''
    import sys
    if sys.version_info[0] >= 3:
        b = InvalidPattern('a\N{LATIN SMALL LETTER A WITH GRAVE}')
        assert str(b) == u'a\u00E0'
        b = InvalidPattern('a\N{LATIN SMALL LETTER A WITH GRAVE}'.encode('utf-8'))
        assert str(b) == u'a\u00E0'

# Generated at 2022-06-14 06:16:11.092733
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    msg = "This is a unicode string with some unicode: àèìòù and latin-1: áéíóú.\n" \
        "Ach so. And some invalid UTF-8: \xfe\xfb"
    msg_utf8 = msg.encode('utf-8', 'replace')

    class BogusError(InvalidPattern):
        _fmt = "Bogus Error: %(msg)s"

    a = BogusError(msg)
    # We expect __unicode__ to return a unicode object, with the pre-encoded
    # characters as unicode.
    assert type(a.__unicode__()) is unicode
    assert a.__unicode__().endswith(u"And some invalid UTF-8: \ufffd\ufffd")

    # We expect __

# Generated at 2022-06-14 06:16:22.784024
# Unit test for method __str__ of class InvalidPattern

# Generated at 2022-06-14 06:16:29.442219
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """InvalidPattern.__unicode__ test"""
    error = InvalidPattern("finditer expects a string")
    if not isinstance(unicode(error), unicode):
        raise AssertionError
    if not isinstance(str(error), str):
        raise AssertionError
    if unicode(error) != u'Invalid pattern(s) found. finditer expects a string':
        raise AssertionError
    if str(error) != "Invalid pattern(s) found. finditer expects a string":
        raise AssertionError

# Generated at 2022-06-14 06:16:40.337944
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    from bzrlib.tests import TestCase
    from bzrlib.trace import mutter
    def _test(msg, multi=False):
        """Test InvalidPattern and InvalidPattern.__unicode__"""
        try:
            raise InvalidPattern(msg)
        except InvalidPattern as e:
            if multi:
                mutter(e.msg)
            else:
                mutter(str(e))
            mutter(unicode(e))
            mutter(repr(e))
            mutter(e._format())
            mutter(e._get_format_string())
    class Test(TestCase):
        def test_unicode__utf8_string(self):
            """Test InvalidPattern.__unicode__ with a utf8-encoded message"""

# Generated at 2022-06-14 06:16:41.805900
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    assert str(InvalidPattern('Invalid regex')) == 'Invalid regex'

# Generated at 2022-06-14 06:16:50.507194
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Test that we can create a unicode exception message."""
    from bzrlib.i18n import gettext
    # gettext('a') returns a unicode string.
    e = InvalidPattern('a')
    assert isinstance(str(e), str)
    assert isinstance(unicode(e), unicode)
    # gettext('b') returns a unicode string.
    e = InvalidPattern('b')
    assert isinstance(str(e), str)
    assert isinstance(unicode(e), unicode)

# Generated at 2022-06-14 06:17:00.655116
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """Check InvalidPattern.__str__()"""
    _real_re_compile = re.compile

    # Test unicode strings as format string with unicode characters
    re.compile = lambda pat: _real_re_compile(pat, re.UNICODE)
    e = InvalidPattern('foo\x00bar')
    try:
        pattern = re.compile('(?P<name>.*)').match(None)
    except InvalidPattern as e:
        assert isinstance(str(e), str)
        assert isinstance(unicode(e), unicode)
        assert isinstance(str(e), str)
        assert isinstance(unicode(e), unicode)
        assert str(e) == 'Invalid pattern(s) found. "foo\x00bar"'

# Generated at 2022-06-14 06:17:07.814311
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Unit test for method __unicode__ of class InvalidPattern"""
    e = InvalidPattern('msg')
    import sys
    # Test if the method returns a unicode object
    if sys.version_info[0] >= 3:
        assert type(e.__unicode__()) == str
    else:
        assert type(e.__unicode__()) == unicode

# Generated at 2022-06-14 06:17:12.012830
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """__unicode__ for InvalidPattern"""
    e = InvalidPattern('test')
    eq = 'Unprintable exception InvalidPattern: dict={}, fmt=None, error=None'
    assert str(e) == eq



# Generated at 2022-06-14 06:17:16.529339
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """__unicode__ should return the error message if already in unicode."""
    from bzrlib.i18n import gettext
    iface = InvalidPattern(gettext(u'Unicode message'))
    s = unicode(iface)
    assert(isinstance(s, unicode))


# Generated at 2022-06-14 06:17:22.511566
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """__unicode__ of InvalidPattern should return a unicode

    It returns a unicode object, whatever the exception message is.
    """
    u = InvalidPattern('message').__unicode__()
    if not isinstance(u, unicode):
        raise AssertionError('__unicode__ must return unicode')



# Generated at 2022-06-14 06:17:32.091512
# Unit test for method __setstate__ of class LazyRegex
def test_LazyRegex___setstate__():
    import bzrlib.tests
    return_value = bzrlib.tests.SimpleTestCase.test_suite()
    import pickle
    from StringIO import StringIO

    regex = LazyRegex("foo")
    output = StringIO()
    pickle.dump(regex, output)
    output.seek(0)
    pickled_string = output.read()

    new_regex = LazyRegex("bar")
    new_regex.__setstate__(pickle.loads(pickled_string))
    output.close()
    return return_value

# Generated at 2022-06-14 06:17:46.131488
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """InvalidPattern.__str__() is a valid str or unicode object and contains
    self.msg."""
    import doctest
    # default format string
    d = {'msg': 'the message'}
    e = InvalidPattern(d['msg'])
    s = str(e)
    assert 'pattern(s)' in s
    assert d['msg'] in s
    e = InvalidPattern(d['msg'])
    assert 'pattern(s)' in unicode(e)
    assert d['msg'] in unicode(e)
    # custom format string
    d['_fmt'] = '%(msg)s custom format'
    e = InvalidPattern(**d)
    assert d['_fmt'] % d == str(e)
    e = InvalidPattern(**d)
    assert d['_fmt'] % d

# Generated at 2022-06-14 06:18:03.039917
# Unit test for method __getattr__ of class LazyRegex
def test_LazyRegex___getattr__():
    """LazyRegex getattr access works properly - bug #341185"""
    class MyLazyRegex(LazyRegex):
        def _real_re_compile(self, *args, **kwargs):
            return _real_re_compile(*args, **kwargs)
    lr = MyLazyRegex(('^a([0-9]+),b([^$]+),([0-9]+)$',))
    match = lr.match("a12,btext,345")
    if match.groups() != ('12', 'text', '345'):
        raise AssertionError('LazyRegex getattr access fails')


# Generated at 2022-06-14 06:18:08.432268
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """InvalidPattern:__str__ should return a string."""
    try:
        # If we do not raise an exception, it should return a string
        try:
            raise InvalidPattern('')
        except InvalidPattern as e:
            str(e)
    except TypeError:
        # Otherwise it should raise TypeError
        raise AssertionError('InvalidPattern:__str__ should return a string')

# Generated at 2022-06-14 06:18:20.806249
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """__unicode__() returns that string with default encoding

    If the encoding can't be determined, it chooses utf8.
    """
    import bzrlib
    bzrlib._ = lambda x:x
    e = InvalidPattern('foo')
    if e._get_format_string():
        return () # gettext is not enabled
    assert e.__unicode__() == unicode('foo')
    e.msg = u'foo'
    assert e.__unicode__() == unicode('foo')
    e._preformatted_string = u'bar'
    assert e.__unicode__() == unicode('bar')
    import locale
    locale.__dict__['getpreferredencoding'] = lambda: None
    e.msg = 'bar'
    assert e.__unicode__() == u'bar'

# Generated at 2022-06-14 06:18:29.227846
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    from bzrlib import tests
    from bzrlib.tests import TestCase
    from bzrlib.lazy_regex import InvalidPattern

    class Test_InvalidPattern___str__(TestCase):

        def test_invalid_pattern(self):
            ip = InvalidPattern("Invalid pattern(s) found. 'smith' is not a "
                "valid glob expression")
            self.assertEqual(str(ip),
                "Invalid pattern(s) found. 'smith' is not a valid "
                "glob expression")
            self.assertEqual(repr(ip),
                "InvalidPattern(Invalid pattern(s) found. 'smith' is not a "
                "valid glob expression)")

# Generated at 2022-06-14 06:18:42.886932
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    from bzrlib.i18n import gettext

    # test None message
    e = InvalidPattern(None)
    assert __str__(e) == 'Invalid pattern(s) found. '
    assert unicode(e) == u'Invalid pattern(s) found. '

    # test empty message
    e = InvalidPattern('')
    assert __str__(e) == 'Invalid pattern(s) found. '
    assert unicode(e) == u'Invalid pattern(s) found. '

    # test with a message
    e = InvalidPattern('something')
    assert __str__(e) == 'Invalid pattern(s) found. something'
    assert unicode(e) == u'Invalid pattern(s) found. something'

    # test with a utf-8 message

# Generated at 2022-06-14 06:18:49.081747
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """This method test if InvalidPattern.__str__ work as expected."""
    fmt = InvalidPattern._get_format_string()
    assert fmt == 'Invalid pattern(s) found. %(msg)s'
    msg = 'invalid pattern'
    obj = InvalidPattern(msg)
    assert obj.__str__() == 'Invalid pattern(s) found. ' + msg

# Generated at 2022-06-14 06:18:57.023903
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """InvalidPattern.__unicode__() should return a unicode object"""
    class X(InvalidPattern):
        pass
    x = X('foo')
    assert isinstance(unicode(x), unicode), '__unicode__ should return unicode'
    x._preformatted_string = 'a\xc3\xb1' # 'a\xf1' = a.encode('latin1')
    assert unicode(x) == x._preformatted_string, '__unicode__ should return unicode'

# Generated at 2022-06-14 06:19:00.805262
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """Method __str__ of class InvalidPattern must return str."""
    e = InvalidPattern("Error message")
    s = str(e)
    assert isinstance(s, str)


# Generated at 2022-06-14 06:19:07.035720
# Unit test for method __setstate__ of class LazyRegex
def test_LazyRegex___setstate__():
    """__setstate__ correctly sets arguments."""
    l = LazyRegex()
    l.__setstate__({'args':('1',), 'kwargs':{}})
    assert l._real_regex is None
    assert l._regex_args == ('1',)
    assert l._regex_kwargs == {}



# Generated at 2022-06-14 06:19:10.561405
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """InvalidPattern.__str__() returns a str object"""
    err = InvalidPattern('message')
    res = err.__str__()
    assert isinstance(res, str)



# Generated at 2022-06-14 06:19:27.462864
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Test InvalidPattern.__unicode__ and __str__.

    As a side effect, test that pre-formatted unicode messages
    are handled as well as ascii messages.
    """
    from bzrlib.i18n import gettext
    i = InvalidPattern(gettext('something'))
    assert isinstance(i.__unicode__(), unicode)
    assert unicode(i) == 'something'
    assert i._get_format_string() == 'something'

    i = InvalidPattern(u'hello')
    assert isinstance(i.__unicode__(), unicode)
    assert unicode(i) == 'hello'
    assert i._get_format_string() is None

    i = InvalidPattern('\xa3') # non-ascii character

# Generated at 2022-06-14 06:19:38.297001
# Unit test for method __getattr__ of class LazyRegex
def test_LazyRegex___getattr__():
    """Test the proxy behaviour of LazyRegex, when accessing an attribute
    that is not defined in the LazyRegex class.

    The attribute is retrieved from the proxy object sentinel.
    """
    # In this test we must use a new function to be sure that it is not
    # already set in the re module.
    def my_compile(*args, **kwargs):
        return object()
    original_compile = re.compile
    re.compile = my_compile
    lr = LazyRegex()
    assert lr.foo is not None
    re.compile = original_compile



# Generated at 2022-06-14 06:19:42.684048
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """Verify that the __str__ method returns the correct str object"""
    e = InvalidPattern("invalid pattern found")
    s = unicode("Invalid pattern(s) found. invalid pattern found")
    assert(str(e) == s)

# Generated at 2022-06-14 06:19:49.934453
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """InvalidPattern.__unicode__() should format the message according to a translation table

    This tests if the translation of the string given by the user is
    done.
    """
    from bzrlib.i18n import _translate
    from bzrlib.i18n import ustranslate
    from bzrlib.i18n import install_gettext_translations
    from bzrlib.i18n import get_install_translation
    # create a translation setup
    newtrans = get_install_translation()
    newtrans.install()
    # have a translation table
    newtrans.add_domain("bzrlib")
    newtrans.add_messages("""
        _("invalid pattern %(pattern)s"),
        """)
    # translate using the translation table

# Generated at 2022-06-14 06:20:01.668542
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """InvalidPattern.__unicode__() -> unicode"""
    from bzrlib.i18n import gettext

    foo = InvalidPattern('test')
    foo._fmt = 'test'
    foo._preformatted_string = 'test'
    assert foo.__unicode__() == 'test'

    foo = InvalidPattern('test')
    foo._fmt = 'test'
    assert foo.__unicode__() == gettext(u'test')

    foo = InvalidPattern('test')
    foo._preformatted_string = u'test'
    assert foo.__unicode__() == u'test'

    foo = InvalidPattern('test')
    assert foo.__unicode__() == u'Unprintable exception InvalidPattern: dict={}, fmt=None, error=None'
    foo._fmt = 'test'

# Generated at 2022-06-14 06:20:10.923951
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """Test the method __unicode__"""
    from bzrlib.i18n import gettext
    # Get the current translation
    _ = gettext
    # We create the instance of InvalidPattern with a _fmt attributes that
    # uses % operations and that is translated by _().
    ip = InvalidPattern('foo.txt')
    ip._fmt = 'The file "%(msg)s" does not exist'
    ip._preformatted_string = None
    # The method __str__ should return a str object as follows:
    expected_str = 'The file "foo.txt" does not exist'
    # Check that the str object returned by __str__ is equal to expected_str
    # object:
    str_unicode = ip.__str__()
    if str_unicode != expected_str:
        raise AssertionError

# Generated at 2022-06-14 06:20:21.676707
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    from io import BytesIO
    from pipes import quote
    msg = 'this is a test of method InvalidPattern._get_format_string'
    s = 'KeyError: %s' % quote(msg)
    e = InvalidPattern(msg)
    # Test that __unicode__ gives the same result as
    # InvalidPattern._get_format_string()
    assert(unicode(e) == unicode(e._format()))
    # Test that __unicode__ and InvalidPattern._format() can handle a
    # UnicodeDecodeError
    exc = UnicodeDecodeError('utf8', BytesIO(s), 0, 1, 'bad')
    e = InvalidPattern(exc)
    assert(unicode(e) == unicode(e._format()))

# Generated at 2022-06-14 06:20:35.002565
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """__str__ for InvalidPattern should return a str, encoded in utf8."""
    from bzrlib.i18n import gettext
    from bzrlib.trace import mutter
    old_mutter = mutter
    def new_mutter(s):
        pass

# Generated at 2022-06-14 06:20:47.275584
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Test that class InvalidPattern convert to str and unicode correctly."""
    class TestException(InvalidPattern):
        """A test exception class to test invalid patterns."""

        _fmt = 'Test exception with %(msg)s and %(foo)s'

        def __init__(self, msg, foo):
            InvalidPattern.__init__(self, msg)
            self.foo = foo

    err = TestException('my message', 'foo')

    # Ensure that str() and unicode() work
    str(err)
    unicode(err)

    # Ensure that the test exception contains the two variables
    u = unicode(err)
    assert 'my message' in u
    assert 'foo' in u

test_suite = TestSuite()
test_suite.addTest(DocTestSuite(__name__))

# Generated at 2022-06-14 06:20:51.424935
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """__str__ should return unicode."""
    # __str__() should be implemented as __unicode__()
    error = InvalidPattern('test message')
    assert isinstance(unicode(error), unicode)
    assert isinstance(str(error), str)

# Generated at 2022-06-14 06:21:05.476534
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    from bzrlib.tests.per_regex import TestCase
    class TestCase_InvalidPattern_str(TestCase):

        class Test_InvalidPattern(InvalidPattern):
            """Test class for InvalidPattern"""

            def __init__(self, start, end, txt):
                self.start = start
                self.end = end
                self.txt = txt

        def get_format_string(self):
            return 'Something bad occurs between byte %(start)s and byte ' + \
                '%(end)s having this content: %(txt)s'

        def test_str(self):
            err = self.Test_InvalidPattern(8, 18, 'some content')

# Generated at 2022-06-14 06:21:10.234448
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Test method __unicode__ of class InvalidPattern"""
    exc = InvalidPattern('Not an empty string')
    assert unicode(exc) == "Invalid pattern(s) found. Not an empty string"


# Generated at 2022-06-14 06:21:19.934439
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Test __unicode__ works even with formatting errors"""

    # First, we abuse the format specification of the class to make sure
    # it returns a unicode object.
    e = InvalidPattern('__unicode__')
    e._preformatted_string = u'Jabberw\xf6cky'
    assert isinstance(unicode(e), unicode), 'Expected a unicode object'
    assert str(e) == 'Jabberw\xc3\xb6cky', 'Expected the message to be utf8 encoded'

    # Second, let's try to make a mess.
    e = InvalidPattern('__unicode__')

    # Don't let it find the default format string
    e._fmt = False

    # Our dict has values that can't be used in formatting
    def f(): pass
    e.__

# Generated at 2022-06-14 06:21:32.614087
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Unit test for method __unicode__ of class InvalidPattern

    Test that InvalidPattern.__unicode__ returns a unicode string. Test that
    InvalidPattern.__unicode__ can decode a str object. Test that
    InvalidPattern.__unicode__ can make a unicode object from an object which
    is not unicode, str or object which implements method __unicode__.
    """
    class Foo(object):
        def __unicode__(self):
            return u'Unicode of Foo'

    class FooNoUnicode(object):
        pass

    u = InvalidPattern('Error message')
    # Check that __unicode__ returns a unicode string.
    assert isinstance(unicode(u), unicode)
    # Check that __unicode__ can decode a str object.

# Generated at 2022-06-14 06:21:45.338837
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """Test the method that returns the exception string representation."""
    ipe = InvalidPattern('Invalid pattern(s) found. %(msg)s')
    expected = 'Unprintable exception InvalidPattern: dict={}, fmt=None, error=None'
    actual = ipe.__str__()
    assert expected == actual
    #
    ipe = InvalidPattern('Invalid pattern(s) found. %(msg)s')

# Generated at 2022-06-14 06:21:51.611465
# Unit test for method __getattr__ of class LazyRegex
def test_LazyRegex___getattr__():
    """__getattr__ must return a member from the proxied regex object"""
    proxy = LazyRegex((r"[a-z]", 0))
    # The regex is not compiled yet so __getattr__ will return an AttributeError
    # which will be raised by next line
    try:
        proxy.flags
        raise AssertionError(
            "flags was not raised AttributeError because the proxied object is not created")
    except AttributeError:
        # The exception is expected here
        pass
    # Then the regex is compiled
    regex = proxy.match("")
    # The proxy will return the members from the proxied regex object
    assert regex.flags == 0, "flags must be 0"
    assert regex.groups == 0, "groups must be 0"

# Generated at 2022-06-14 06:22:02.992860
# Unit test for method __getattr__ of class LazyRegex
def test_LazyRegex___getattr__():
    """Check the getattr method of LazyRegex class, which will compile the
    regex if it is not compiled yet.
    """
    class MockRegex(object):
        """A fake regex class to mock the real regex class."""

        def __init__(self, arg, arg2):
            self.arg = arg
            self.arg2 = arg2

        def __eq__(self, other):
            if self.__class__ is not other.__class__:
                return NotImplemented
            return self.__dict__ == other.__dict__

    # When the regex is not compiled yet, a call to any of its methods
    # will call compile_and_collapse, which will compile the regex and
    # copy its methods to the current LazyRegex object.

# Generated at 2022-06-14 06:22:14.636498
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    from bzrlib.tests import TestCase
    from bzrlib import i18n
    i18n.install_gettext_translations()

    class TestCase_InvalidPattern___unicode__(TestCase):

        def test_InvalidPattern___unicode__(self):
            invalid_pattern = InvalidPattern('msg_1')
            wanted = u'msg_1'
            got = unicode(invalid_pattern)
            self.assertEqual(wanted, got)

    TestCase_InvalidPattern___unicode__('test_InvalidPattern___unicode__').test_InvalidPattern___unicode__()
    i18n.uninstall_gettext_translations()

# Generated at 2022-06-14 06:22:20.048245
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """__str__ returns a python 8-bit string object by default.

    This is a str in Python 2.x and a bytes object in Python 3.  In Python 2.x
    a call to unicode() will decode it according to the default encoding.
    """
    assert isinstance(InvalidPattern('foo').__str__(), str)



# Generated at 2022-06-14 06:22:25.285673
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    # invalid pattern raises InvalidPattern, not re.error
    try:
        _real_re_compile(r'abc[\s*')
    except InvalidPattern as ip:
        assert str(ip) == 'Invalid pattern(s) found. "abc[\s*" unbalanced parenthesis'
    else:
        raise AssertionError('Invalid pattern should be detected')

# Generated at 2022-06-14 06:22:34.576522
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    from bzrlib import tests
    t = tests.TestCase('test_InvalidPattern___str__')
    t.assertEqual(str(InvalidPattern("some message")), "Invalid pattern(s) found. some message")

# Generated at 2022-06-14 06:22:47.090031
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    # Test case where the exception contains a preformatted message
    e = InvalidPattern("foo")
    e._preformatted_string = "bar"
    expected = "bar"
    assert unicode(e) == expected

    # Test case where the exception must format its message using
    # a format string.
    #
    # Unfortunately, the easiest way to test this code path is to
    # force _format() to raise an exception. Since it is hard to
    # get it to raise an exception, we must monkey patch it to raise
    # one.
    def _format(self):
        raise ValueError("expected exception")
    e = InvalidPattern("foo")
    e._format = _format
    expected = "Unprintable exception InvalidPattern: dict={}, fmt='%(msg)s', error=ValueError('expected exception',)"
    assert unic

# Generated at 2022-06-14 06:22:53.330157
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    import sys
    if sys.version_info[:2] != (2, 4):
        # test broken in python 2.4
        # because UnicodeError is not catched.
        # This is also tested in test_errors.py
        try:
            error = InvalidPattern('Invalid pattern(s) found. %(msg)s')
            error.msg = u'\U0001f41e'
            error.__unicode__()
        except UnicodeDecodeError:
            raise AssertionError("__unicode__ should return a unicode object")


# vim: set ft=python fileencoding=utf8 :

# Generated at 2022-06-14 06:23:05.097481
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """Test __str__ method of class InvalidPattern"""
    from bzrlib.i18n import gettext
    test_class = InvalidPattern("test")
    test_class._fmt = "testing"
    test_class._locale_exception_str = "testing %s"
    test_class._preformatted_string = "testing %s"
    assert test_class._get_format_string() == "testing"
    setattr(gettext, '_translations', {})
    assert test_class._get_format_string() == "testing %s"
    assert test_class._format() == "testing %s"
    assert unicode(test_class) == "testing %s"
    assert str(test_class) == "testing %s"

# Generated at 2022-06-14 06:23:17.046830
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """__str__ must return a str, not a unicode"""
    # It should return a str if the message is a unicode string
    ip = InvalidPattern(u'str')
    result = str(ip)
    # The returned type is really str, not unicode
    assert type(result) == str
    assert result == 'str'

    # It should return a unicode if the message is a non-unicode string
    ip = InvalidPattern('str')
    result = str(ip)
    # The returned type is really unicode, not str
    assert type(result) == str
    assert result == 'str'

    # It should return a unicode if the message is a non-unicode string
    ip = InvalidPattern('str')
    result = unicode(str(ip))
    # The returned type is really unicode, not str


# Generated at 2022-06-14 06:23:29.811661
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """This test case makes sure that __unicode__ of class InvalidPattern
    returns a unicode object and not a string (which would happen if we would
    just return self._fmt % self.__dict__)
    """
    fmt = "This is a format string with some %(attrib)s"
    e = InvalidPattern(fmt % {'attrib': 'args'})
    # Try different ways to get at the unicode object
    for f in (str, unicode, e.__str__, e.__unicode__):
        u = f()
        # __unicode__ and __str__ must return a unicode or string object
        if not isinstance(u, str):
            raise AssertionError("%s() returned %r instead of string" % (f.__name__, u))
        # But they must not return

# Generated at 2022-06-14 06:23:34.637843
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    import os

    e = InvalidPattern('foo bar')
    assert str(e) == 'Invalid pattern(s) found. foo bar'
    assert unicode(e) == u'Invalid pattern(s) found. foo bar'

    # create a unicode string in the str path
    e = InvalidPattern(u'foo bar')
    assert str(e) == 'Invalid pattern(s) found. foo bar'
    assert unicode(e) == u'Invalid pattern(s) found. foo bar'

# Generated at 2022-06-14 06:23:48.580925
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    """Test the InvalidPattern.__str__ method.

    This method should return a str object of printable characters.
    """
    klass = InvalidPattern
    error = klass('msg')
    # If the string is a valid unicode object, the __str__ method should
    # convert it to a string object.
    unicode_str = '\u2600\u2605'
    error._preformatted_string = unicode_str
    str_object = error.__str__()
    assert isinstance(str_object, str), "%s.__str__() returned %s" \
           % (klass.__name__, type(str_object))
    assert str_object == unicode_str.encode('utf8')
    # And if the string is already a string object, the __str__ method
    # should keep

# Generated at 2022-06-14 06:23:54.350191
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    msg = "test message"
    u = InvalidPattern(msg).__unicode__()
    assert type(u) is unicode, "%r is not a unicode object" % u
    assert u == msg, "expecting %r to equal %r" % (u, msg)



# Generated at 2022-06-14 06:24:06.744549
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """Test unicode output of InvalidPattern class.

    We should have a test for this because this was once converted to string
    without checking the encoding, so a file encoded with "iso-8859-1"
    (latin1) would fail as the pattern was not valid in utf-8. This is also
    important for py3k. See https://bugs.launchpad.net/bzr/+bug/363551
    """
    # Helper function to iter over passed args.
    def to_unicode(s):
        try:
            # This will succeed in py3k
            return unicode(s)
        except NameError:
            # This is what happens in py2k
            return str(s)


# Generated at 2022-06-14 06:24:18.438575
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():
    """`InvalidPattern.__unicode__` returns utf-8 message

    The method is implemented to give a Unicode object in Python 2 and
    bytes in Python 3.

    :return: a tuple is returned, consisting of a message and the Python
        version.
    """
    e = InvalidPattern('This is an error message.')
    if (sys.version_info[0] < 3):
        return '%s %s' % (e.__unicode__(), sys.version_info[0])
    else:
        return '%s %s' % (e.__unicode__(), sys.version_info[0])

# Generated at 2022-06-14 06:24:28.325614
# Unit test for method __str__ of class InvalidPattern
def test_InvalidPattern___str__():
    from bzrlib.trace import mutter
    from StringIO import StringIO
    exception = InvalidPattern('foo %(bar)s baz')
    exception.bar = 'quux'
    # Check that the unicode string is correctly converted to a byte string
    # when printed
    sio = StringIO()
    mutter('%r', exception, file=sio)
    s = sio.getvalue()
    # The output should be a byte string
    assert isinstance(s, str)
    # It should contain an encoded unicode string
    assert 'foo quux baz' in s

# Generated at 2022-06-14 06:24:34.554855
# Unit test for method __unicode__ of class InvalidPattern
def test_InvalidPattern___unicode__():

    class TestError(InvalidPattern):
        _fmt = u"Error code %(code)s"

    err = TestError(code=u"E4")
    assert unicode(err) == u"Error code E4"
    assert str(err) == "Error code E4"