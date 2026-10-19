

# Generated at 2022-06-13 12:23:20.174740
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    '''
    Unit test for method filters of class FilterModule
    '''
    FilterModule().filters()

# Generated at 2022-06-13 12:23:23.540899
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('a%2Bb') == u'a+b'
    assert unicode_urldecode('a%20b') == u'a b'
    assert unicode_urldecode('a%C3%A1b') == u'aáb'
    assert unicode_urldecode('foo=bar&baz=fizz') == u'foo=bar&baz=fizz'


# Generated at 2022-06-13 12:23:32.837005
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert ('{}' == unicode_urldecode('%7B%7D'))
    assert ('1, 2' == unicode_urldecode('1%2C%202'))
    assert ('this+is/a test' == unicode_urldecode('this%2Bis%2Fa+test'))
    assert ('this is a test' == unicode_urldecode('this is a test'))
    assert ('this=is=a test' == unicode_urldecode('this=is=a+test'))


# Generated at 2022-06-13 12:23:42.871538
# Unit test for function unicode_urldecode
def test_unicode_urldecode():

    assert unicode_urldecode('%2a') == '*'
    assert unicode_urldecode('%7E') == '~'
    assert unicode_urldecode('%25') == '%'
    assert unicode_urldecode('%20') == ' '
    assert unicode_urldecode('%2B') == '+'
    assert unicode_urldecode('%3A') == ':'
    assert unicode_urldecode('%2A') == '*'
    assert unicode_urldecode('%7F') == '\x7f'

    assert unicode_urldecode(u'%2a') == u'*'
    assert unicode_urldecode(u'%7E') == u'~'
    assert unicode

# Generated at 2022-06-13 12:23:45.144399
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%C3%A9') == u'é'



# Generated at 2022-06-13 12:23:55.970265
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'"foo"') == u'"foo"'
    assert unicode_urldecode(u'"f%6Fo"') == u'"foo"'
    assert unicode_urldecode(u'"f%6Fo"') == u'"foo"'
    assert unicode_urldecode(u'"f%6Fo%41"') == u'"fooA"'
    assert unicode_urldecode(u'"f%6Fo%41%42"') == u'"fooAB"'
    assert unicode_urldecode(u'"f%6Fo%41%42%43"') == u'"fooABC"'
    assert unicode_urldecode(u'"f%6Fo%41%42%43%44"') == u'"fooABCD"'
    assert unic

# Generated at 2022-06-13 12:24:05.879843
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    """
    Test method filters of class FilterModule
    """
    from ansible.module_utils.six import PY3

    # Test filters for class FilterModule
    # Test urldecode when PY3 is True
    assert FilterModule().filters()['urldecode']("%40%41%42") == "@AB"
    # Test urldecode when PY3 is False
    assert FilterModule().filters()['urldecode'](b"%40%41%42") == b"@AB"
    # Test urldecode when value is dict
    assert FilterModule().filters()['urldecode']({"a": "b"}) == "a=b"
    # Test urldecode when value is not string
    val = FilterModule().filters()['urldecode'](iter("abc"))

# Generated at 2022-06-13 12:24:09.110679
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
  filters = FilterModule().filters()
  assert filters['urldecode']('a%20b') == 'a b'
  assert filters['urldecode']('a+b') == 'a+b'

# Generated at 2022-06-13 12:24:18.560609
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'a') == u'a'
    assert unicode_urldecode(u'%C3%A0') == u'à'
    assert unicode_urldecode(u'%20') == u' '
    assert unicode_urldecode(u'a%20b') == u'a b'
    assert unicode_urldecode(u'a+b') == u'a b'
    assert unicode_urldecode(u'a%2Bb') == u'a+b'
    assert unicode_urldecode(u'a+%2B+b') == u'a  +b'


# Generated at 2022-06-13 12:24:27.169365
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%25dag') == u'%dag'
    assert unicode_urldecode('%7B%22a%22%3A1%2C%22b%22%3A2%7D') == u'{"a":1,"b":2}'
    assert unicode_urldecode('+++') == u'+++'
    assert unicode_urldecode('%%25%35dag') == u'%5dag'
    assert unicode_urldecode('%C3%A9') == u'é'
    assert unicode_urldecode('%E2%82%AC%0A') == u'€\n'


# Generated at 2022-06-13 12:24:38.197395
# Unit test for function unicode_urlencode

# Generated at 2022-06-13 12:24:44.037747
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    fm = FilterModule()
    filters = fm.filters()
    assert filters["urldecode"]("%7B%22status%22%3A%20%22UP%22%7D") == "{\"status\": \"UP\"}"
    assert filters["urlencode"]("{\"status\": \"UP\"}") == "%7B%22status%22%3A+%22UP%22%7D"
    assert filters["urlencode"]("{\"status\": \"UP\"}") == "%7B%22status%22%3A+%22UP%22%7D"

# Generated at 2022-06-13 12:24:48.945003
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    if not PY3:
        assert unicode_urldecode(u'%E2%89%A0%20%E2%89%A4') == u'≠ ≤'



# Generated at 2022-06-13 12:24:56.270103
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    fm = FilterModule()
    assert do_urldecode('a+b%2Fc') == fm.filters()['urldecode']('a+b%2Fc')
    if not HAS_URLENCODE:
        assert do_urlencode('a+b%2Fc') == fm.filters()['urlencode']('a+b%2Fc')

# Generated at 2022-06-13 12:25:04.482470
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'%E4%BD%A0%E5%A5%BD%E4%B8%96%E7%95%8C') == u'你好世界'
    assert unicode_urldecode(u'%25') == u'%'
    assert unicode_urldecode(u'%5E') == u'^'
    assert unicode_urldecode(u'%5e') == u'^'
    assert unicode_urldecode(u'%26%25') == u'&%'
    assert unicode_urldecode(u'https://en.wikipedia.org/wiki/%C3%96resund_Bridge') == u'https://en.wikipedia.org/wiki/Öresund_Bridge'

# Generated at 2022-06-13 12:25:13.861899
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    assert do_urldecode("this+is%20a+test%21") == "this is a test!"
    assert do_urlencode("this is a test!") == "this+is+a+test%21"
    assert do_urlencode(dict(key="this is a test!")) == "key=this+is+a+test%21"
    assert do_urlencode(["key=this is a test!"]) == "key%3Dthis+is+a+test%21"
    assert do_urlencode(["key=this is a test!", "key2=another+test%21"]) == "key%3Dthis+is+a+test%21&key2%3Danother%2Btest%2521"

# Generated at 2022-06-13 12:25:24.171908
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert "foo=bar" == unicode_urlencode('foo=bar')
    assert "foo%20bar" == unicode_urlencode('foo bar')
    assert "foo" == unicode_urlencode('foo')
    assert "a%2Bb%2Bc" == unicode_urlencode('a+b+c')
    assert "%C3%A9" == unicode_urlencode('é')
    assert "a%2Bb%2B%C3%A9" == unicode_urlencode('a+b+é')
    assert "%2Ffoo%2Fbar" == unicode_urlencode('/foo/bar')
    assert "%2Ffoo%2F%C3%A9" == unicode_urlencode('/foo/é')

# Generated at 2022-06-13 12:25:25.808210
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    assert FilterModule().filters()['urlencode'] == do_urlencode
    assert FilterModule().filters()['urldecode'] == do_urldecode

# Generated at 2022-06-13 12:25:30.491475
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode(u'привет') == '%D0%BF%D1%80%D0%B8%D0%B2%D0%B5%D1%82'
    assert unicode_urlencode(u'привет', for_qs=True) == '%D0%BF%D1%80%D0%B8%D0%B2%D0%B5%D1%82'


# Generated at 2022-06-13 12:25:33.116450
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode(u"/foo bar/") == u"/foo%20bar/"
    assert unicode_urlencode(u"/foo bar/", for_qs=True) == u"%2Ffoo%20bar%2F"



# Generated at 2022-06-13 12:25:39.022679
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode(u'http://foo/\u2665') == u'http%3A//foo/%E2%99%A5'
    assert unicode_urlencode(u'http://foo/\u2665', for_qs=True) == u'http%3A%2F%2Ffoo%2F%E2%99%A5'



# Generated at 2022-06-13 12:25:49.832794
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    import json

    # Ansible jinja2 filters
    ansible_filters = FilterModule().filters()

    # Python3 jinja2 filters
    python_filters = {}

    # Python2 jinja2 filters
    python_filters_py2 = {}

    if HAS_URLENCODE:
        python_filters['urlencode'] = do_urlencode
        python_filters_py2['urlencode'] = do_urlencode

    # Check if we have a python3 jinja2 filter
    import sys

    if sys.version_info.major > 2:
        python_filters['urldecode'] = do_urldecode
    else:
        python_filters_py2['urldecode'] = do_urldecode

    # We use unittest for the

# Generated at 2022-06-13 12:25:52.916874
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    fm = FilterModule()
    filters = fm.filters()
    assert filters['urldecode'] == do_urldecode
    if not HAS_URLENCODE:
        assert filters['urlencode'] == do_urlencode

# Generated at 2022-06-13 12:25:56.120343
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('foo%2Fbar%2Fbaz') == 'foo/bar/baz'
    assert unicode_urldecode('foo%2Fbar+baz') == 'foo/bar baz'



# Generated at 2022-06-13 12:26:03.059740
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc') == u'abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc'

# Generated at 2022-06-13 12:26:11.431401
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():

    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.six import PY3

    module = basic.AnsibleModule(argument_spec={})
    module.params['foo'] = 'bar'
    fm = FilterModule()
    fm_items = fm.filters().items()

    assert ('urldecode' in dict(fm_items))
    assert ('urlencode' in dict(fm_items))

    assert ('urldecode' in module._filter_loader._filters)
    assert ('urlencode' in module._filter_loader._filters)

    assert (module._filter_loader.filters()['urldecode'] == do_urldecode)

# Generated at 2022-06-13 12:26:19.807005
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('1 2 3') == '1%202%203'
    assert unicode_urlencode('1 2 3', for_qs=True) == '1+2+3'
    assert unicode_urlencode('1+2+3', for_qs=True) == '1%2B2%2B3'
    assert unicode_urlencode(u'あいうえお'.encode('utf8')) == '%E3%81%82%E3%81%84%E3%81%86%E3%81%88%E3%81%8A'

# Generated at 2022-06-13 12:26:22.766685
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    fm = FilterModule()
    assert fm.filters()['urldecode']('a') == 'a'

# Generated at 2022-06-13 12:26:24.617052
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode(u'a b') == u'a%20b'


# Generated at 2022-06-13 12:26:30.662539
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%7B%22hello%22%3A+%22world%22%7D') == '{"hello": "world"}'
    assert unicode_urldecode('%2B') == '+'
    assert unicode_urldecode('%2F') == '/'
    assert unicode_urldecode('') == ''
    assert unicode_urldecode('%') == '%'


# Generated at 2022-06-13 12:26:40.904390
# Unit test for function unicode_urldecode

# Generated at 2022-06-13 12:26:43.431729
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    assert FilterModule().filters()['urldecode'] == do_urldecode



# Generated at 2022-06-13 12:26:44.752918
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%3F') == '?'


# Generated at 2022-06-13 12:26:56.615824
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    import unittest

    class TestUnicodeUrldecode(unittest.TestCase):
        def test_unicode_urldecode(self):
            self.assertEqual(unicode_urldecode(''), u'')
            self.assertEqual(unicode_urldecode('+'), u' ')
            self.assertEqual(unicode_urldecode('%20'), u' ')
            self.assertEqual(unicode_urldecode('%21'), u'!')
            self.assertEqual(unicode_urldecode('%2F'), u'/')
            self.assertEqual(unicode_urldecode('%3F'), u'?')
            self.assertEqual(unicode_urldecode('%3D'), u'=')

# Generated at 2022-06-13 12:27:00.781461
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    fm = FilterModule()
    d = fm.filters()
    assert d['urldecode'] == do_urldecode
    if not HAS_URLENCODE:
        assert d['urlencode'] == do_urlencode


# Generated at 2022-06-13 12:27:06.841233
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('') == ''
    assert unicode_urlencode('/') == '/'
    assert unicode_urlencode(u'string') == 'string'
    assert unicode_urlencode(b'string') == 'string'
    assert unicode_urlencode(u'string with blanks') == 'string%20with%20blanks'
    assert unicode_urlencode({b'string': b'with blanks'}) == 'string=with%20blanks'
    assert unicode_urlencode([b'string', b'with blanks']) == 'string&with%20blanks'

# Generated at 2022-06-13 12:27:15.752633
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    # Test the urldecode filter method
    assert do_urldecode('%20a%22b+%27c%27+d%22%20') == u' a"b \'c\' d" '
    # Test the urlencode filter method
    assert do_urlencode(u' a"b \'c\' d" ') == '%20a%22b+%27c%27+d%22%20'
    assert do_urlencode(b' a"b \'c\' d" ') == '%20a%22b+%27c%27+d%22%20'

# Generated at 2022-06-13 12:27:25.210231
# Unit test for function unicode_urldecode

# Generated at 2022-06-13 12:27:30.995149
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    fm = FilterModule()
    filters = fm.filters()
    assert filters['urldecode']('one%20two%3Dthree%26four%3D%2Bfive') == 'one two=three&four=+five'
    if not HAS_URLENCODE:
        assert filters['urlencode']('one two=three&four=+five') == 'one+two%3Dthree%26four%3D%2Bfive'

# Generated at 2022-06-13 12:27:36.880415
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode("http://example.com/%C3%A5%C3%A5%5B%C3%A5%5D%5B%C3%A5%5D") == "http://example.com/åå[å][å]"
    assert unicode_urldecode("http://example.com/%c3%a5%c3%a5%5b%c3%a5%5d%5b%c3%a5%5d") == "http://example.com/åå[å][å]"



# Generated at 2022-06-13 12:27:42.999091
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(b'foo%20bar%40baz') == u'foo bar@baz'
    assert unicode_urldecode(u'foo%20bar%40baz') == u'foo bar@baz'


# Generated at 2022-06-13 12:27:51.775252
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    from ansible.module_utils._text import to_unicode
    assert unicode_urlencode(to_unicode(b'http://www.perdu.com/')) == u'http%3A//www.perdu.com/'
    assert unicode_urlencode(to_unicode(b'http://www.perdu.com/'), for_qs=True) == u'http%3A%2F%2Fwww.perdu.com%2F'
    assert unicode_urlencode(to_unicode(b'12345')) == u'12345'
    assert unicode_urlencode(to_unicode(b'12345'), for_qs=True) == u'12345'

# Generated at 2022-06-13 12:27:59.855251
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    import sys
    assert unicode_urlencode(u'abc def') == b'abc+def'
    assert unicode_urlencode(u'föö bär') == b'f%C3%B6%C3%B6+b%C3%A4r'
    if not PY3:
        assert type(unicode_urlencode(u'abc def')) == unicode
        assert type(unicode_urlencode(u'föö bär')) == unicode
    else:
        assert type(unicode_urlencode(u'abc def')) == bytes
        assert type(unicode_urlencode(u'föö bär')) == bytes
    assert type(unicode_urlencode('föö bär')) == unicode


# Unit

# Generated at 2022-06-13 12:28:12.071516
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    import sys, os
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))
    from ansible import context
    from units.mock.procenv import swap_stdin_and_argv

    context._init_global_context(
        connection='local',
        remote_addr=None,
        runner_type='action',
        module_name=None,
        module_args=[],
        ansible_vars={},
        ansible_version=None,
        ansible_play_batch=None,
    )

    f = FilterModule()
    a = f.filters()

    def u(string):
        return string if PY3 else to_text(string)


# Generated at 2022-06-13 12:28:18.618679
# Unit test for function do_urlencode
def test_do_urlencode():

    test_values = dict(
        dict=dict(
            empty={},
            simple={'1': '&'},
            deep={'httpd': 'nginx', 'os': 'FreeBSD'}
        ),
        list=dict(
            empty=[],
            simple=['1', '&'],
            deep=['httpd', 'nginx', 'os', 'FreeBSD']
        ),
        tuple=dict(
            empty=(),
            simple=('1', '&'),
            deep=('httpd', 'nginx', 'os', 'FreeBSD')
        ),
    )

    assert do_urlencode(None) == ''

    assert do_urlencode(1) == '1'
    assert do_urlencode('1') == '1'

# Generated at 2022-06-13 12:28:25.763961
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('http://example.com/foo') == 'http%3A%2F%2Fexample.com%2Ffoo'
    assert unicode_urlencode('http://example.com/foo', True) == 'http%3A%2F%2Fexample.com%2Ffoo'
    assert unicode_urlencode('http://example.com/~foo') == 'http%3A%2F%2Fexample.com%2F~foo'
    assert unicode_urlencode('http://example.com/~foo', True) == 'http%3A%2F%2Fexample.com%2F~foo'
    assert unicode_urlencode('http://example.com/foo', False) == 'http%3A%2F%2Fexample.com%2Ffoo'

# Generated at 2022-06-13 12:28:34.008241
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
  from ansible.module_utils import basic
  from ansible.module_utils._text import to_bytes, to_native

  option_vals = basic.AnsibleModule(argument_spec=dict()).params
  test_filter = FilterModule().filters()['urldecode']
  assert test_filter('%2Fusr%2Flocal%2Fbin').lower() == '/usr/local/bin'.lower(), "%s != %s" % (test_filter('%2Fusr%2Flocal%2Fbin').lower(), '/usr/local/bin'.lower())

# Generated at 2022-06-13 12:28:36.287847
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    """ Unit test for module FilterModule """
    result = FilterModule().filters()
    assert 'urldecode' in result
    assert not HAS_URLENCODE or 'urlencode' in result

# Generated at 2022-06-13 12:28:39.957446
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%20%2B%2F%3D%26%3F%23%24%25') == ' +/=&?#%24%25'


# Generated at 2022-06-13 12:28:42.262327
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    module = FilterModule()
    filters = module.filters()
    # test urldecode method
    assert filters['urldecode']('CentOS%205.9') == 'CentOS 5.9'
    # test urlencode method
    assert filters['urlencode']('CentOS 5.9') == 'CentOS%205.9'

# Generated at 2022-06-13 12:28:52.296733
# Unit test for method filters of class FilterModule

# Generated at 2022-06-13 12:28:55.248867
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    f = FilterModule()
    try:
        result = f.filters()
        assert 'urldecode' in result
    finally:
        pass


# Generated at 2022-06-13 12:29:02.637919
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%40%40') == '@@'
    assert unicode_urldecode(u'%40%40') == u'@@'
    assert unicode_urldecode(b'%40%40') == '@@'
    assert unicode_urldecode('%40') == '@'
    assert unicode_urldecode(u'%40') == u'@'
    assert unicode_urldecode(b'%40') == '@'
    assert unicode_urldecode('%2A') == '*'
    assert unicode_urldecode(u'%2A') == u'*'
    assert unicode_urldecode(b'%2A') == '*'

# Generated at 2022-06-13 12:29:12.831889
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode(u"café") == u'caf%C3%A9'
    assert unicode_urlencode({u"café": u"café"}) == u'caf%C3%A9=caf%C3%A9'
    assert unicode_urlencode([u"café"]) == u'caf%C3%A9'
    assert unicode_urlencode([{u"café": u"café"}]) == u'caf%C3%A9=caf%C3%A9'
    assert unicode_urlencode({u"café": [u"café"]}) == u'caf%C3%A9=caf%C3%A9'
    assert unicode_urlencode

# Generated at 2022-06-13 12:29:19.067958
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    t = FilterModule()
    filters = t.filters()
    assert filters is not None
    assert all(f in filters for f in [
        'urldecode'])
    if not HAS_URLENCODE:
        assert all(f in filters for f in [
            'urlencode'])

# Generated at 2022-06-13 12:29:28.123696
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    # NOTE: We only test our implementation of unicode_urlencode
    if HAS_URLENCODE:
        return

    assert unicode_urlencode(u'foo/bar') == u'foo%2Fbar'
    assert unicode_urlencode(u'foo/bar', for_qs=True) == u'foo%2Fbar'
    assert unicode_urlencode(u'foo bar') == u'foo%20bar'
    assert unicode_urlencode(u'foo bar', for_qs=True) == u'foo+bar'
    assert unicode_urlencode(u'foo=bar') == u'foo=bar'
    assert unicode_urlencode(u'foo=bar', for_qs=True) == u'foo%3Dbar'



# Generated at 2022-06-13 12:29:34.057054
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'%20') == u' '
    assert unicode_urldecode(b'%20') == u' '
    assert unicode_urldecode(u'%E6%97%A5%E6%9C%AC%E8%AA%9E') == u'日本語'
    assert unicode_urldecode(b'%E6%97%A5%E6%9C%AC%E8%AA%9E') == u'日本語'
    assert unicode_urldecode(u'%E6%97%A5^%E6%9C%AC%E8%AA%9E') == u'日^本語'

# Generated at 2022-06-13 12:29:39.405242
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%21%24%26%27%28%29%2A%2B%2C%3B%3D%3F%40') == '!$&\'()*+,;=?@'
    assert unicode_urldecode('%20') == ' '
    assert unicode_urldecode('') == ''



# Generated at 2022-06-13 12:29:48.528349
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('abc') == 'abc'
    assert unicode_urldecode(u'abc') == u'abc'
    if PY3:
        assert unicode_urldecode(b'abc') == 'abc'
        assert unicode_urldecode(b'%61%62%63') == 'abc'
    else:
        assert unicode_urldecode(b'abc') == u'abc'
        assert unicode_urldecode(b'%61%62%63') == u'abc'
    assert unicode_urldecode(u'%61%62%63') == u'abc'
    assert unicode_urldecode(u'%61%62%63%20%64') == u'abc d'
    assert unicode_urldec

# Generated at 2022-06-13 12:29:51.504840
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    fm = FilterModule()
    filters = fm.filters()
    assert filters['urldecode'] == do_urldecode
    if not HAS_URLENCODE:
        assert filters['urlencode'] == do_urlencode

# Generated at 2022-06-13 12:30:03.564945
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    from ansible.module_utils.six.moves.urllib.parse import parse_qs

    assert do_urldecode("bar") == do_urldecode("bar")
    assert do_urldecode("bo%C3%B4z") == do_urldecode("boôz")

    # NOTE: We use parse_qs here because we can't predict the order of the
    #       items in the string returned from do_urlencode.
    assert parse_qs(do_urlencode("bar")) == parse_qs(do_urlencode("bar"))
    assert parse_qs(do_urlencode("boôz")) == parse_qs(do_urlencode("boôz"))

# Generated at 2022-06-13 12:30:05.389608
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('') == ''
    assert unicode_urldecode('abc') == 'abc'
    assert unicode_urldecode('abc+123') == 'abc 123'
    assert unicode_urldecode('abc%20déf') == 'abc déf'

# Generated at 2022-06-13 12:30:13.162879
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    # Note: this is not a full test, it is just for demonstration purposes
    # We expect urllib.unquote_plus to do the right thing
    assert unicode_urldecode('foo') == u'foo'
    assert unicode_urldecode('foo%2Fbar') == u'foo/bar'
    assert unicode_urldecode('foo%2Fbar%20baz') == u'foo/bar baz'
    assert unicode_urldecode('%7B%220%22%3A%5B%22a%22%2C%22b%22%5D%7D') == u'{"0":["a","b"]}'


# Generated at 2022-06-13 12:30:15.537519
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    test_file = FilterModule()
    filters = test_file.filters()
    assert filters['urldecode'] == do_urldecode
    if not HAS_URLENCODE:
        assert filters['urlencode'] == do_urlencode

# Generated at 2022-06-13 12:30:19.308167
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(None) is None
    assert unicode_urldecode(b'test') == u'test'
    assert unicode_urldecode('test') == u'test'



# Generated at 2022-06-13 12:30:23.171112
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%E5%A3%AE%E5%93%89%E4%BE%9D%E4%B8%93%E8%B5%84') == u'壮哉我专资'



# Generated at 2022-06-13 12:30:28.794328
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('test') == u'test'
    assert unicode_urlencode('test?&=') == u'test%3F%26%3D'
    assert unicode_urlencode('test?&=/') == u'test?&=%2F'
    assert unicode_urlencode(u"∑ért") == u'%E2%88%91%C3%A9rt'
    assert unicode_urlencode(u"∑ért", for_qs=True) == u'%E2%88%91%C3%A9rt'



# Generated at 2022-06-13 12:30:36.165271
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    f = FilterModule().filters()

    assert f['urldecode']('hello%20world') == 'hello world'
    assert f['urldecode']('hello+world') == 'hello world'
    assert f['urldecode']('foo%2Fbar') == 'foo%2Fbar'

    assert f['urlencode']('hello world') == 'hello+world'
    assert f['urlencode']('foo/bar') == 'foo%2Fbar'

# Generated at 2022-06-13 12:30:44.223963
# Unit test for function do_urlencode
def test_do_urlencode():
    # Test valid input values
    assert do_urlencode(1) == u'1'
    assert do_urlencode([1, 2, 3]) == u'1&2&3'
    assert do_urlencode({1: 2, 3: 4}) == u'1=2&3=4'
    assert do_urlencode(u'word') == u'word'
    assert do_urlencode('word') == u'word'
    assert do_urlencode('sp ace') == u'sp+ace'
    assert do_urlencode({1: 'sp ace'}) == u'1=sp+ace'
    assert do_urlencode(u'sp+ace') == u'sp%2Bace'
    assert do_urlencode('sp+ace') == u'sp%2Bace'


# Generated at 2022-06-13 12:30:45.652024
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('a+b%20c') == u'a b c'


# Generated at 2022-06-13 12:31:05.121807
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('foobar') == 'foobar'
    assert unicode_urldecode('a+b%2B') == 'a b+'
    assert unicode_urldecode('%C3%A9') == u'é'
    assert unicode_urldecode('%E2%82%AC') == u'€'


# Generated at 2022-06-13 12:31:07.344120
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    module = FilterModule()
    assert module.filters() == {'urldecode':do_urldecode}

# Generated at 2022-06-13 12:31:14.265629
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('a') == 'a'
    assert unicode_urldecode('%41') == 'A'
    assert unicode_urldecode('%04%01') == 'A'
    assert unicode_urldecode('%61') == 'a'
    assert unicode_urldecode('%04%01') == 'A'
    assert unicode_urldecode('%26') == '&'
    assert unicode_urldecode('%3d') == '='



# Generated at 2022-06-13 12:31:22.272758
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    f = FilterModule()
    filters = f.filters()
    assert type(filters) is dict
    assert len(filters) == 2
    assert 'urldecode' in filters
    assert 'urlencode' in filters
    assert filters['urldecode'] is do_urldecode
    assert filters['urlencode'] is do_urlencode


# Generated at 2022-06-13 12:31:30.404231
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode(u'foo bar baz') == 'foo%20bar%20baz'
    assert unicode_urlencode(u'foo+bar+baz') == 'foo%2Bbar%2Bbaz'
    assert unicode_urlencode(u'foo/bar/baz') == 'foo%2Fbar%2Fbaz'
    assert unicode_urlencode(u'foo?bar?baz') == 'foo%3Fbar%3Fbaz'
    assert unicode_urlencode(u'foo@bar@baz') == 'foo%40bar%40baz'
    assert unicode_urlencode(u'foo&bar&baz') == 'foo%26bar%26baz'

# Generated at 2022-06-13 12:31:34.620800
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    # PY3
    assert unicode_urldecode('http%3A//test') == 'http://test'
    assert unicode_urldecode('%7B%22test%22%3A+1%7D') == '{"test": 1}'
    # PY2
    assert unicode_urldecode(u'http%3A//test') == u'http://test'
    assert unicode_urldecode(u'%7B%22test%22%3A+1%7D') == u'{"test": 1}'


# Generated at 2022-06-13 12:31:42.750700
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    string = 'http://www.ansible.com/test@example.com?a=b&b=c&c=d'

    assert do_urldecode(string) == u'http://www.ansible.com/test@example.com?a=b&b=c&c=d'

    if not HAS_URLENCODE:
        assert do_urlencode(string) == 'http%3A//www.ansible.com/test%40example.com%3Fa%3Db%26b%3Dc%26c%3Dd'

# Generated at 2022-06-13 12:31:46.619552
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    i = FilterModule()
    f = i.filters()

    assert f['urldecode'] == do_urldecode
    if not HAS_URLENCODE:
        assert f['urlencode'] == do_urlencode

# Generated at 2022-06-13 12:31:54.057679
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filter_module = FilterModule()
    filters = filter_module.filters()

    assert filters['urldecode'](u'http%3A//example.org') == u'http://example.org'
    assert filters['urldecode'](u'http%3a%2f%2fexample.org') == u'http://example.org'

    params = {'q': 'é'}
    assert filters['urlencode'](params) == 'q=%C3%A9'
    params = {'q': 'é', 'r': 'f'}
    assert filters['urlencode'](params) == 'q=%C3%A9&r=f'
    params = ['a=b', 'c=d']

# Generated at 2022-06-13 12:32:03.125294
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    # strings without a "%" fail without a fix
    # See https://github.com/ansible/ansible/issues/16576
    assert u'日本語' == unicode_urldecode('日本語')

    # Regular ASCII string
    assert u'foo' == unicode_urldecode('foo')

    # Percent-encoded string
    assert u'\u65e5\u672c\u8a9e' == unicode_urldecode('%E6%97%A5%E6%9C%AC%E8%AA%9E')

# Generated at 2022-06-13 12:32:18.518985
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    f = FilterModule()
    filters = f.filters()
    assert filters['urldecode'] is do_urldecode
    if not HAS_URLENCODE:
        assert filters['urlencode'] is do_urlencode

# Generated at 2022-06-13 12:32:20.723714
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    x = FilterModule()
    assert '<' in x.filters().keys()


# Generated at 2022-06-13 12:32:23.709230
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    string = '%41%42%43'
    assert(unicode_urldecode('%41%42%43') == 'ABC')


# Generated at 2022-06-13 12:32:29.822226
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('test') == u'test'
    assert unicode_urldecode('%20test%23') == u' test#'
    assert unicode_urldecode('%E4%BD%A0%E5%A5%BD') == u'你好'
    assert unicode_urldecode({'a': '你好'}) == u'a=\u4f60\u597d'



# Generated at 2022-06-13 12:32:31.632910
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    myFilters = FilterModule()
    myFilters.filters()


# Generated at 2022-06-13 12:32:40.820946
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    # This is no real test, but just shows what the filters are doing

    from ansible.module_utils.common._collections_compat import Mapping

    test_data = {
        'unicode_string': u'a%20b',
        'unicode_string_for_qs': u'a%22b',
        'dict': {b'k1': u'v1', 'k2': [{'k3': u'v3'}, b'k4']},
        'tuple': (Mapping({u'k1': u'v1'}), 'k2', [1, 2, b'k3']),
        'list': [
            Mapping({b'k1': u'v1', 'k2': u'v2'}),
            (1, 2, 3),
        ],
    }

# Generated at 2022-06-13 12:32:43.436366
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    ansible_filter = FilterModule()
    assert ansible_filter.filters() is not None

# Generated at 2022-06-13 12:32:49.330250
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    expected = 'https://user%40example.com:password%21@example.com?query=foo%26bar&a=1%2B2&b=2%2B2&c=%5B1%5D%2B%5B2%5D'
    actual = unicode_urlencode(u'https://user@example.com:password!@example.com?query=foo&bar&a=1+2&b=2+2&c=[1]+[2]')
    assert expected == actual


# Generated at 2022-06-13 12:32:55.779209
# Unit test for function do_urlencode
def test_do_urlencode():
    """
    >>> test_input = {'a': 'a', 'b': 'b', 'c': 'c'}
    >>> test_output = u'a=a&c=c&b=b'
    >>> do_urlencode(test_input) == test_output
    True
    >>> test_input = ['a', 'b', 'c']
    >>> test_output = u'a&c&b'
    >>> do_urlencode(test_input) == test_output
    True

    """


# Generated at 2022-06-13 12:32:57.550366
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    # TODO: Better unit tests, but at least it tests the basics
    assert FilterModule().filters()['urldecode']('a=%20') == 'a= '

# Generated at 2022-06-13 12:33:14.815204
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    ''' urldecode should be jinja2 compatible '''
    fm = FilterModule()
    filters = fm.filters()
    assert filters['urldecode']('foo+bar%21') == 'foo bar!'
    if not HAS_URLENCODE:
        assert filters['urlencode']({'foo': 'bar baz'}) == 'foo=bar+baz'
        assert filters['urlencode']('foo bar') == 'foo+bar'

# Generated at 2022-06-13 12:33:23.693738
# Unit test for function do_urlencode
def test_do_urlencode():
    assert do_urlencode("foo=bar") == "foo%3Dbar"
    assert do_urlencode("foo bar") == "foo+bar"
    assert do_urlencode("/foo /bar") == "%2Ffoo+%2Fbar"
    assert do_urlencode("/foo /bar=baz") == "%2Ffoo+%2Fbar%3Dbaz"
    assert do_urlencode("foo bar baz") == "foo+bar+baz"
    assert do_urlencode("foo&bar=baz") == "foo%26bar%3Dbaz"
    assert do_urlencode({'foo': 'bar', 'baz': 'qux'}) == "foo=bar&baz=qux"