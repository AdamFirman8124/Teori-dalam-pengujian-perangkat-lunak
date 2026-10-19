

# Generated at 2022-06-13 12:23:19.739884
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%C3%9C') == '\xc3\x9c'


# Generated at 2022-06-13 12:23:32.269562
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode(u"/") == u"%2F"
    assert unicode_urlencode({u"x": u"y"}) == u"x=y"
    assert unicode_urlencode({u"x": u"y", u"z": u"1"}) == u"x=y&z=1"
    assert unicode_urlencode([u"x", u"y"]) == u"x=y"
    assert unicode_urlencode([u"x", u"y", u"z"]) == u"x=y&x=z"
    assert unicode_urlencode([(u"x", u"y"), (u"z", u"1")]) == u"x=y&z=1"


# Generated at 2022-06-13 12:23:34.066207
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
        f = FilterModule()
        assert f.filters()

# Generated at 2022-06-13 12:23:36.322322
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    # test FilterModule.filters()
    assert isinstance(FilterModule().filters(), dict) == True

# Generated at 2022-06-13 12:23:46.986869
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    assert do_urldecode('abc') == 'abc'
    assert do_urldecode('%41') == 'A'
    assert do_urldecode('%41%42%43') == 'ABC'
    assert do_urldecode('%41%42%43%21%24%26%28%29%2A%2B%2C%3B%3D%3F%40%5B%5D') == 'ABC!$&()*+,;=?@[]'

# Generated at 2022-06-13 12:23:56.739596
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'abcd') == u'abcd'
    assert unicode_urldecode(u'%26') == u'&'
    assert unicode_urldecode(u'%3F') == u'?'
    assert unicode_urldecode(u'ab%2Bcd') == u'ab+cd'
    assert unicode_urldecode(u'ab%2bcd') == u'ab+cd'
    assert unicode_urldecode(u'abcd%26efgh') == u'abcd&efgh'
    assert unicode_urldecode(u'abcd%3Fefgh') == u'abcd?efgh'


# Generated at 2022-06-13 12:24:00.508690
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    y = unicode_urldecode('How+are+you%3F+%C3%85re+you+ok%3F+%C3%89%C3%89%C3%A5%E2%82%AC%C2%A3%C2%A5')
    assert y == u'How are you? Åre you ok? ÉÈå€£¥'


# Generated at 2022-06-13 12:24:03.487235
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('kött') == 'k%C3%B6tt'
    assert unicode_urlencode('/') == '/'
    assert unicode_urlencode('kött', for_qs=True) == 'k%C3%B6tt'
    assert unicode_urlencode('/', for_qs=True) == '%2F'


# Generated at 2022-06-13 12:24:13.388698
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert ' ' == unicode_urldecode('%20')
    assert ' !' == unicode_urldecode('%20!')
    assert '?x=y&z=1&z=2' == unicode_urldecode('?x=y&z=1&z=2')
    assert u'\u2713' == unicode_urldecode(u'%E2%9C%93')
    assert u'\u2713q' == unicode_urldecode(u'%E2%9C%93q')
    assert u'\u2713' == unicode_urldecode(b'%E2%9C%93')
    assert u'\u2713q' == unicode_urldecode(b'%E2%9C%93q')


# Generated at 2022-06-13 12:24:15.685103
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    flt = FilterModule()
    assert flt.filters()['urldecode'] == do_urldecode


# Generated at 2022-06-13 12:24:22.603253
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode("%C3%A9") == u"\u00E9"
    assert unicode_urldecode("%2F") == u"/"
    assert unicode_urldecode("%2B") == u"+"
    assert unicode_urldecode("%25") == u"%"


# Generated at 2022-06-13 12:24:26.747177
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filters = FilterModule().filters()
    assert type(filters) == dict
    assert u'urldecode' in filters
    assert filters[u'urldecode'] == do_urldecode
    if not HAS_URLENCODE:
        assert u'urlencode' in filters
        assert filters[u'urlencode'] == do_urlencode


# Generated at 2022-06-13 12:24:31.663246
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%C3%A9') == '\xe9'
    assert unicode_urldecode('%E2%82%AC') == '\u20ac'
    assert unicode_urldecode('%F0%A4%AD%A2') == '\U00024b62'

# Generated at 2022-06-13 12:24:33.765056
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    string = u'%E2%98%83%E2%98%83'
    assert unicode_urldecode(string) == u'☃☃'


# Generated at 2022-06-13 12:24:41.299870
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    _test_unicode_urlencode(b'', '')
    _test_unicode_urlencode(b'foo', 'foo')
    _test_unicode_urlencode(b'foo/bar', 'foo/bar')
    _test_unicode_urlencode(b'foo?bar', 'foo%3Fbar')
    _test_unicode_urlencode(b'foo&bar', 'foo%26bar')
    _test_unicode_urlencode(b'foo+bar', 'foo%2Bbar')
    _test_unicode_urlencode(b'foo bar', 'foo+bar')
    _test_unicode_urlencode(b'foo%20bar', 'foo%20bar')

# Generated at 2022-06-13 12:24:43.370563
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode("%20") == u" "


# Generated at 2022-06-13 12:24:47.448270
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    fm = FilterModule()
    filters = fm.filters()
    assert filters['urldecode'] == do_urldecode
    assert filters['urlencode'] == do_urlencode

# Generated at 2022-06-13 12:24:50.045046
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%C3%A9') == u'é'



# Generated at 2022-06-13 12:24:58.178743
# Unit test for function do_urlencode
def test_do_urlencode():
    assert do_urlencode('foo') == 'foo'
    assert do_urlencode({'foo': 'bar'}) == 'foo=bar'
    assert do_urlencode({'foo': 'b ar', 'ba z': 'buz'}) == 'ba+z=buz&foo=b+ar'
    assert do_urlencode('f/o') == 'f%2Fo'
    assert do_urlencode('f/o', for_qs=True) == 'f%2Fo'



# Generated at 2022-06-13 12:25:01.901650
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('Rémi') == 'R%C3%A9mi'
    assert unicode_urlencode('/foo#bar') == '/foo%23bar'
    assert unicode_urlencode('/foo#bar', for_qs=True) == '%2Ffoo%23bar'


# Generated at 2022-06-13 12:25:13.905894
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('a=b') == 'a%3Db'
    assert unicode_urlencode(b'a=b') == 'a%3Db'
    assert unicode_urlencode('name') == 'name'
    assert unicode_urlencode(b'name') == 'name'
    assert unicode_urlencode('/') == '%2F'
    assert unicode_urlencode(b'/') == '%2F'
    assert unicode_urlencode('/', for_qs=True) == '%2F'
    assert unicode_urlencode(b'/', for_qs=True) == '%2F'
    assert unicode_urlencode('a=b', for_qs=True) == 'a%3Db'
    assert unicode_urlencode

# Generated at 2022-06-13 12:25:18.644321
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    data = {
        '%C3%A4%20%E2%98%83': u'\u00e4 \u2603',
        'blah': 'blah',
    }
    for k in data:
        assert unicode_urldecode(k) == data[k]


# Generated at 2022-06-13 12:25:22.049003
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    assert FilterModule().filters()['urldecode'] is do_urldecode
    if not HAS_URLENCODE:
        assert FilterModule().filters()['urlencode'] is do_urlencode



# Generated at 2022-06-13 12:25:29.238898
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    now1 = u'\u4f60\u597d\u4e16\u754c'
    then1 = unicode_urldecode(u'%E4%BD%A0%E5%A5%BD%E4%B8%96%E7%95%8C')
    assert(now1 == then1)
    now2 = u'%E4%BD%A0%E5%A5%BD%E4%B8%96%E7%95%8C'
    then2 = unicode_urldecode(u'%25E4%25BD%25A0%25E5%25A5%25BD%25E4%25B8%2596%25E7%2595%258C')
    assert(now2 == then2)

# Generated at 2022-06-13 12:25:33.817675
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    utf8 = '%E4%F6%FC%DF%C4%D6%DC%DF'
    latin1 = '%E4%F6%FC%DF%C4%D6%DC%DF'.decode('utf-8').encode('latin-1')

    assert unicode_urldecode(utf8).encode('utf-8') == latin1
    assert unicode_urldecode(latin1).encode('utf-8') == latin1



# Generated at 2022-06-13 12:25:39.917220
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('') == u''
    assert unicode_urlencode('abc') == u'abc'
    assert unicode_urlencode('abc def') == u'abc%20def'
    assert unicode_urlencode('abc def/') == u'abc%20def%2F'
    assert unicode_urlencode('abc def', for_qs=True) == u'abc+def'
    assert unicode_urlencode('abc def/', for_qs=True) == u'abc+def%2F'
    assert unicode_urlencode('/abc def') == u'%2Fabc%20def'
    assert unicode_urlencode('/abc def/') == u'%2Fabc%20def%2F'

# Generated at 2022-06-13 12:25:49.898358
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert u'%E6%88%91' == unicode_urlencode(u'我')
    assert u'%E6%88%91%E8%83%BD' == unicode_urlencode(u'我能')
    assert u'%E6%88%91%E8%83%BD%E5%90%88' == unicode_urlencode(u'我能合')

    assert u'%E6%88%91%20%E8%83%BD' == unicode_urlencode(u'我 能')
    assert u'%E6%88%91%E8%83%BD%20' == unicode_urlencode(u'我能 ')

# Generated at 2022-06-13 12:25:58.341602
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'foo%20bar') == u'foo bar'
    assert unicode_urldecode(u'foo+bar') == u'foo bar'
    assert unicode_urldecode(u'foo+p%C3%B6p') == u'foo pöp'
    assert unicode_urldecode(u'foo%2Bbar') == u'foo+bar'
    assert unicode_urldecode(u'foo%25bar') == u'foo%bar'
    assert unicode_urldecode(u'%') == u'%'
    assert unicode_urldecode(u'%2') == u'%2'
    assert unicode_urldecode(u'%2%') == u'%2%'
    assert unic

# Generated at 2022-06-13 12:26:04.722548
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode("abcd") == "abcd"
    assert unicode_urlencode("abcd:123") == "abcd%3A123"
    assert unicode_urlencode("abcd:123", for_qs=True) == "abcd%3A123"
    assert unicode_urlencode("abcd/123") == "abcd%2F123"
    assert unicode_urlencode("abcd/123", for_qs=True) == "abcd%2F123"
    assert unicode_urlencode("abcd?123") == "abcd%3F123"
    assert unicode_urlencode("abcd?123", for_qs=True) == "abcd%3F123"

# Generated at 2022-06-13 12:26:06.460987
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%C3%B6') == u'ö'



# Generated at 2022-06-13 12:26:16.736871
# Unit test for function unicode_urldecode

# Generated at 2022-06-13 12:26:26.270989
# Unit test for function unicode_urlencode

# Generated at 2022-06-13 12:26:28.528512
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%C3%A9') == u'\u00e9'


# Generated at 2022-06-13 12:26:37.285859
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    test = FilterModule()
    assert test.filters()['urldecode']('url+encoded+string') == u'url encoded string'

    assert test.filters()['urldecode']({'a': 'b', 'c': 'd'}) == u'a=b&c=d'

    import io
    import collections
    assert test.filters()['urldecode']((y for y in (1, 2, 3))) == u'1&2&3'
    assert test.filters()['urldecode'](io.BytesIO(b'1\0002\0003')) == u'1&2&3'
    assert test.filters()['urldecode'](collections.deque((1, 2, 3))) == u'1&2&3'
    assert test.fil

# Generated at 2022-06-13 12:26:40.591234
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u"%C3%A4") == u"ä"

    utf8_encoded = u"%C3%A4".encode('utf-8')
    assert unicode_urldecode(utf8_encoded) == u"ä"



# Generated at 2022-06-13 12:26:47.709365
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    fm = FilterModule()
    assert fm.filters()['urldecode']('hello%2C+world!') == 'hello, world!'
    if not HAS_URLENCODE:
        assert fm.filters()['urlencode']('hello, world!') == 'hello%2C%20world%21'

# Generated at 2022-06-13 12:26:52.493249
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filter = FilterModule()
    filters = filter.filters()
    assert filters != {}
    assert filters.keys() == {'urldecode', 'urlencode'}
    assert filters['urldecode'] == do_urldecode
    if not HAS_URLENCODE:
        assert filters['urlencode'] == do_urlencode
    else:
        assert filters['urlencode'] == do_urlencode

# Generated at 2022-06-13 12:27:03.428575
# Unit test for function do_urlencode
def test_do_urlencode():
    assert do_urlencode(u'foo') == u'foo'
    assert do_urlencode(u'foo bar') == u'foo%20bar'
    assert do_urlencode([u'foo', u'bar']) == u'foo&bar'
    assert do_urlencode({u'foo': u'bar', u'abc': u'def'}) == u'foo=bar&abc=def'
    assert do_urlencode({u'foo bar': u'abc def'}) == u'foo%20bar=abc%20def'
    assert do_urlencode(u'\u21b5') == u'%E2%86%B5'



# Generated at 2022-06-13 12:27:06.929733
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    f = FilterModule()
    assert f.filters() == {'urldecode': do_urldecode}



# Generated at 2022-06-13 12:27:09.701488
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    import jinja2
    template = '{{ "a=b" | urldecode }}'
    template = jinja2.Template(template)

    assert "a=b" == template.render()

# Generated at 2022-06-13 12:27:21.786088
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode(u'%29%28') == '%2529%2528'
    assert unicode_urlencode(u'%29') == '%2529'
    assert unicode_urlencode(u'%28') == '%2528'
    assert unicode_urlencode(u'abc') == 'abc'
    assert unicode_urlencode(u'æøåÆØÅ') == '%C3%A6%C3%B8%C3%A5%C3%86%C3%98%C3%85'

# Generated at 2022-06-13 12:27:28.674567
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    from ansible.module_utils.jinja2.filters import FilterModule as fm
    f = fm().filters()
    assert f['urldecode'](u'%2C') == u',', "urldecode function failed"
    if not HAS_URLENCODE:
        assert f['urlencode'](u',') == u'%2C', "urlencode function failed"

# Generated at 2022-06-13 12:27:35.947463
# Unit test for function do_urlencode
def test_do_urlencode():
    print("Testing do_urlencode")
    assert do_urlencode("/\\@:") == "/%2F%5C%40%3A"
    assert do_urlencode({"a": "b"}) == "a=b"
    assert do_urlencode({"a": 1}) == "a=1"
    assert do_urlencode({"a": True}) == "a=True"
    assert do_urlencode(["a", "b"]) == "a&b"
    assert do_urlencode(["a", 1]) == "a&1"
    assert do_urlencode(["a", True]) == "a&True"


# Generated at 2022-06-13 12:27:46.916506
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    import pytest
    filter_module = FilterModule()
    filters = filter_module.filters()

    assert 'urldecode' in filters
    assert 'urlencode' in filters

    # Test urldecode
    # Check the filter works
    assert filters['urldecode']('foo+bar%2fbla') == 'foo bar/bla'

    # Check the filter handles unicode
    assert filters['urldecode']('pouet+pouet+%e9') == 'pouet pouet é'

    # Check the filter handles unicode with Python 2
    import sys
    if sys.version_info[0] < 3:
        assert filters['urldecode'](u'pouet+pouet+%e9') == 'pouet pouet é'

    # Check

# Generated at 2022-06-13 12:27:49.199159
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    a = FilterModule()
    assert a.filters()['urldecode']('a%2Bb') == u'a+b'



# Generated at 2022-06-13 12:27:53.649511
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'nom%C3%A9%20d%C3%A9fil%C3%A9') == u'nomé défilé'
    assert unicode_urldecode(u'%F0%9F%90%93') == u'\U0001F513'
    assert unicode_urldecode(u'%00') == u'\x00'


# Generated at 2022-06-13 12:28:00.506225
# Unit test for function do_urlencode
def test_do_urlencode():
    assert do_urlencode('hello world') == 'hello%20world'
    assert do_urlencode('hello/world') == 'hello%2Fworld'
    assert do_urlencode('hello world, this is dog') == 'hello%20world%2C%20this%20is%20dog'
    assert do_urlencode(u'hello world, this is dog') == 'hello%20world%2C%20this%20is%20dog'

    assert do_urlencode({'name': 'test', 'age': 32}) == 'name=test&age=32'

    assert do_urlencode(['name=test', 'age=32']) == 'name=test&age=32'

# Generated at 2022-06-13 12:28:07.411591
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    # test_str = '%E7%89%B9%E5%88%A5%E5%AD%97%E7%AC%A6%E8%99%9A%E6%8B%9F'
    test_str = '%E7%89%B9%E5%88%A5'
    print(unicode_urldecode(test_str)) # test



# Generated at 2022-06-13 12:28:12.116380
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%21%7E%2A%27%28%29%3B%3A%40%26%3D%2B%24%2C%2F%3F%25%23%5B%5D') == '!~*\'()\';:@&=+$,/?%#[]'


# Generated at 2022-06-13 12:28:15.544761
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('http://www.example.com/?b=foo bar') == 'http%3A%2F%2Fwww.example.com%2F%3Fb%3Dfoo%20bar'
    assert unicode_urlencode('http://www.example.com/?b=foo+bar') == 'http%3A%2F%2Fwww.example.com%2F%3Fb%3Dfoo%2Bbar'


# Generated at 2022-06-13 12:28:20.461379
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert(unicode_urlencode(u"http://www.example.com/?foo=bar+baz&blah=blah") == u"http%3A%2F%2Fwww.example.com%2F%3Ffoo%3Dbar%2Bbaz%26blah%3Dblah")



# Generated at 2022-06-13 12:28:29.396586
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    # some of these tests are python 2 specific because
    # the python 2 codec of urllib unquote can not accept unicode
    # that's why we need to use bytes

    # the most basic test.
    assert unicode_urldecode(u'a') == u'a'
    # test a simple %20 case
    assert unicode_urldecode(u'hello%20world') == u'hello world'
    # make sure we decode in utf-8
    assert unicode_urldecode(u'gr%C3%BC%C3%9Fe') == u'grüße'
    # test a simple + case
    assert unicode_urldecode(u'hello+world') == u'hello world'
    # make sure we decode in utf-8
    assert unicode_urldec

# Generated at 2022-06-13 12:28:35.854488
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert ' ' == unicode_urldecode('+')
    assert ' ' == unicode_urldecode('%20')
    assert 'a b' == unicode_urldecode('a+b')
    assert 'a b' == unicode_urldecode('a%20b')
    assert 'à b' == unicode_urldecode('à%20b')
    assert 'à b' == unicode_urldecode('%C3%A0%20b')
    assert 'à b' == unicode_urldecode('%C3%A0+b')
    assert 'à b' == unicode_urldecode('à b')

# Generated at 2022-06-13 12:28:41.948000
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode(u"hi there") == u"hi%20there"
    assert unicode_urlencode(u"hi there", for_qs=True) == u"hi+there"
    assert unicode_urlencode(u"i am a boy") == u"i%20am%20a%20boy"
    assert unicode_urlencode(u"i am a boy", for_qs=True) == u"i+am+a+boy"
    assert unicode_urlencode(u"i am a boy") == u"i%20am%20a%20boy"
    assert unicode_urlencode(u"i am a boy", for_qs=True) == u"i+am+a+boy"
    assert unicode_urlencode(u"/foo/bar") == u

# Generated at 2022-06-13 12:28:44.199340
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('foo') == u'foo'
    assert unicode_urldecode('%20') == u' '
    assert unicode_urldecode('%2B') == u'+'


# Generated at 2022-06-13 12:28:51.769103
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'%E4%B8%AD%E6%96%87') == u'中文'
    assert unicode_urldecode(u'%E4%B8%AD%E6%96%87%EF%BC%8C%E6%96%BD%E5%85%89%E9%93%9C') == u'中文，旽光铜'
    assert unicode_urldecode(u'%E4%B8%AD%E6%96%87%EF%BC%8C%E6%96%BD%E5%85%89%E9%93%9C%26aaa%3Dbbb') == u'中文，旽光铜&aaa=bbb'

# Generated at 2022-06-13 12:29:01.468268
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('/') == '/'
    assert unicode_urlencode('/', for_qs=True) == '/'
    assert unicode_urlencode('/foo') == '/foo'
    assert unicode_urlencode('/foo', for_qs=True) == '/foo'
    assert unicode_urlencode('/foo bar') == '/foo%20bar'
    assert unicode_urlencode('/foo bar', for_qs=True) == '/foo+bar'
    assert unicode_urlencode('/foo+bar') == '/foo+bar'
    assert unicode_urlencode('/foo+bar', for_qs=True) == '/foo+bar'
    assert unicode_urlencode('/foo%20bar') == '/foo%20bar'
    assert unicode_

# Generated at 2022-06-13 12:29:03.917132
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    if not PY3:
        assert unicode_urldecode(u'foo%3Dbar+tar') == u'foo=bar tar'
    assert unicode_urldecode(u'foo%3Dbar+tar') == 'foo=bar tar'


# Generated at 2022-06-13 12:29:06.079320
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    fm = FilterModule()
    assert fm is not None
    assert fm.filters() is not None
    assert fm.filters() == {'urldecode': do_urldecode, 'urlencode': do_urlencode}


# Generated at 2022-06-13 12:29:11.187135
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    test_data = [
        (u'unicode', u'unicode'),
        (u'München', u'M%C3%BCnchen')
    ]
    for test in test_data:
        assert unicode_urlencode(test[0]) == test[1]

# Generated at 2022-06-13 12:29:24.222056
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    ''' Test unicode_urlencode '''
    from nose.tools import assert_equal
    assert_equal(unicode_urlencode(u'hello'), u'hello')
    assert_equal(unicode_urlencode(u'hi there'), u'hi+there')
    assert_equal(unicode_urlencode(u'http://www.python.org'), u'http%3A//www.python.org')
    assert_equal(unicode_urlencode(u'http://www.python.org', for_qs=True), u'http%3A%2F%2Fwww.python.org')
    assert_equal(unicode_urlencode(u'foo@bar'), u'foo%40bar')

# Generated at 2022-06-13 12:29:30.274534
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    # type: () -> None
    urldecode = unicode_urldecode
    assert urldecode('%26%23x6A%3B') == u'&#x6A;'
    assert urldecode('%26%23x6a%3b') == u'&#x6a;'
    assert urldecode('%26%23106%3b') == u'&#106;'



# Generated at 2022-06-13 12:29:40.487193
# Unit test for function unicode_urldecode

# Generated at 2022-06-13 12:29:49.245695
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    module = FilterModule()

    # Module function
    assert module.filters()

    # Unit tests
    assert module.filters()['urldecode']('%7F%7F') == '~~'

    if not HAS_URLENCODE:
        # Unit tests
        assert module.filters()['urlencode']('~~') == '%7F%7F'
        assert module.filters()['urlencode']('%%') == '%%25'
        assert module.filters()['urlencode']('%') == '%25'
        assert module.filters()['urlencode']('%test') == '%25test'

# Generated at 2022-06-13 12:29:54.187796
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    assert do_urldecode("a") == "a"
    assert do_urldecode("%20") == " "
    assert do_urldecode("%2B") == "+"
    assert do_urldecode("%3D") == "="

    assert do_urlencode("a") == "a"
    assert do_urlencode(" ") == "%20"
    assert do_urlencode("+") == "%2B"
    assert do_urlencode("=") == "%3D"

# Generated at 2022-06-13 12:29:56.856359
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filter_module = FilterModule()
    assert type(filter_module).filters.__name__ == 'function'
    assert filter_module.filters().__class__.__name__ == 'dict'


# Generated at 2022-06-13 12:29:59.863488
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('http://ansible.cc/') == 'http%3A//ansible.cc/'
    assert unicode_urlencode('http://ansible.cc/', for_qs=True) == 'http%3A%2F%2Fansible.cc%2F'



# Generated at 2022-06-13 12:30:05.134685
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    assert do_urldecode('a%20b') == u'a b'
    assert do_urldecode('a+b') == u'a b'
    assert do_urldecode('%C2%A9') == u'\xa9'

    assert do_urlencode('b cád') == u'b%20c%C3%A1d'
    assert do_urlencode('b cád') == do_urlencode(u'b cád')
    assert do_urlencode({'c': 'a&b'}) == u'c=a%26b'
    assert do_urlencode(['a', 'c', 'b&d']) == u'a&c&b%26d'

# Generated at 2022-06-13 12:30:08.358456
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    # FilterModule.filters()
    fm = FilterModule()
    result = fm.filters()
    assert(result['urldecode'])
    #assert(result['urlencode'])


# Generated at 2022-06-13 12:30:15.113469
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    # Test with Jinja2.6 backward compat
    module = FilterModule()
    assert 'urldecode' in module.filters()
    assert 'urlencode' in module.filters()
    assert module.filters()['urlencode'] == module.filters()['urldecode']

    # Test with Jinja2.7
    module = FilterModule()
    module.filters()['urlencode'] = do_urlencode
    assert 'urldecode' in module.filters()
    assert 'urlencode' in module.filters()
    assert module.filters()['urlencode'] != module.filters()['urldecode']


# Generated at 2022-06-13 12:30:21.108941
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    """
    Test unicode_urldecode
    """
    assert unicode_urldecode(u'%F0%9F%98%83') == u'\U0001F603'



# Generated at 2022-06-13 12:30:28.451251
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    import datetime
    assert unicode_urldecode(u'%21%23%24%26%27%28%29%2A%2B%2C%2F%3A%3B%3D%3F%40%5B%5D') == u'!#$&\'()*+,/:;=?@[]'
    assert unicode_urldecode(u'%61%62%63') == u'abc'
    assert unicode_urldecode(u'%E2%82%AC') == u'€'
    assert unicode_urldecode(u'a%cc%88') == u'ä'

# Generated at 2022-06-13 12:30:36.512437
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('unicode!') == u'unicode%21'
    assert unicode_urlencode('unicode!', for_qs=True) == u'unicode%21'
    assert unicode_urlencode('unicode!(%%)') == u'unicode%21(%25)%25'
    assert unicode_urlencode('unicode!(%%)', for_qs=True) == u'unicode%21%28%25%25%29'



# Generated at 2022-06-13 12:30:39.958363
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode(u'abcABC/:') == 'abcABC%2F%3A'
    assert unicode_urlencode(u'abcABC/:', for_qs=True) == 'abcABC%2F%3A'


# Generated at 2022-06-13 12:30:46.788326
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'') == u''
    assert unicode_urldecode(u'abc') == u'abc'
    assert unicode_urldecode(u'd') == u'd'
    assert unicode_urldecode(u'%20') == u' '
    assert unicode_urldecode(u'%2f') == u'/'
    assert unicode_urldecode(u'%2F') == u'/'
    assert unicode_urldecode(u'%25') == u'%'
    assert unicode_urldecode(u'%3D') == u'='
    assert unicode_urldecode(u'a%20b') == u'a b'
    assert unicode_urldecode(u'a+b')

# Generated at 2022-06-13 12:30:53.433105
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    '''
    Test function unicode_urldecode
    '''
    # Test urldecode when no unicode characters are present
    ret = unicode_urldecode('dagwieers')
    assert ret == 'dagwieers'

    # Test urldecode with regular ASCII characters
    ret = unicode_urldecode('%68%65%6C%6C%6F')
    assert ret == 'hello'

    # Test urldecode with unicode characters
    ret = unicode_urldecode('%68%65%6C%6C%F4')
    assert ret == 'hello\xf4'

if __name__ == '__main__':
    test_unicode_urldecode()



# Generated at 2022-06-13 12:30:59.506094
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('') == ''
    assert unicode_urlencode('abc') == 'abc'
    assert unicode_urlencode('abc%def') == 'abc%25def'
    assert unicode_urlencode('/') == '%2F'
    assert unicode_urlencode('/', for_qs=True) == '%2F'
    assert unicode_urlencode('https://www.redhat.com?a&b=c') == 'https%3A%2F%2Fwww.redhat.com%3Fa%26b%3Dc'

# Generated at 2022-06-13 12:31:09.449206
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    valid_tests = {
        u'foo': u'foo',
        u'foo/bar': u'foo%2Fbar',
        u'foo/bar': u'foo%2Fbar',
        u'från': u'fr%C3%A5n',
        u' ': u'%20',
        u'?': u'%3F',
        u'&': u'%26',
        u'$': u'%24',
        u'?': u'%3F',
        u'&': u'%26',
        u'$': u'%24',
    }

    for value, result in iteritems(valid_tests):
        assert unicode_urlencode(value) == result


# Generated at 2022-06-13 12:31:18.521488
# Unit test for method filters of class FilterModule

# Generated at 2022-06-13 12:31:27.796941
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    try:
        from jinja2.filters import do_urlencode as jinja2_urlencode
    except ImportError:
        jinja2_urlencode = lambda text, *args, **kwargs: text

    def test(input, expected):
        assert unicode_urlencode(input) == expected
        assert jinja2_urlencode(input) == expected

    test(u'The quick brown fox jumped over the lazy dog.',
         'The%20quick%20brown%20fox%20jumped%20over%20the%20lazy%20dog.')

    test(u'Citroën',
         'Citro%C3%ABn')

# Generated at 2022-06-13 12:31:39.552604
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    if PY3:
        assert unicode_urldecode('%7B%22a%22%3A+1%7D') == '{\\"a\\": 1}'
    else:
        assert unicode_urldecode('%7B%22a%22%3A+1%7D') == u'{\\"a\\": 1}'



# Generated at 2022-06-13 12:31:42.339047
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filter_module = FilterModule()
    filters = filter_module.filters()

    assert 'urldecode' in filters
    assert 'urlencode' in filters

# Generated at 2022-06-13 12:31:46.576126
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    import sys
    if sys.version_info[0] == 2:
        assert unicode_urldecode(u'á') == u'\xc3\xa1'
    else:
        assert unicode_urldecode(u'á') == 'á'



# Generated at 2022-06-13 12:31:49.210550
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    fm = FilterModule()
    filters = fm.filters()

    assert isinstance(filters, dict)
    assert 'urldecode' in filters
    assert 'urlencode' in filters

# Generated at 2022-06-13 12:31:53.075245
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filter_module = FilterModule()
    filters = filter_module.filters()
    assert filters['urldecode'] == do_urldecode
    if HAS_URLENCODE:
        assert filters['urlencode'] == do_urlencode



# Generated at 2022-06-13 12:31:57.962224
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode("a%20string%20with%20spaces") == "a string with spaces"
    assert unicode_urldecode("%C3%BCmlaut+%E2%82%AC+unencoded") == u"ümlaut € unencoded"


# Generated at 2022-06-13 12:32:04.570536
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('http%3A%2F%2Fwww.wikipedia.org%2Fwiki%2FURL_encoding') == u'http://www.wikipedia.org/wiki/URL_encoding'
    assert unicode_urldecode('http%3A%2F%2Fwww.wikipedia.org%2Fwiki%2FURL_encoding') == b'http://www.wikipedia.org/wiki/URL_encoding'


# Generated at 2022-06-13 12:32:09.789795
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('abc') == u'abc'
    assert unicode_urldecode('abc%20def') == u'abc def'
    assert unicode_urldecode('abc+def') == u'abc def'
    assert unicode_urldecode('%E4%B8%AD%E6%96%87') == u'中文'


# Generated at 2022-06-13 12:32:14.345135
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode(u'test/test') == 'test%2Ftest'
    assert unicode_urlencode(u'test/test', for_qs=True) == 'test%2Ftest'
    assert unicode_urlencode(b'test/test') == b'test%2Ftest'
    assert unicode_urlencode(b'test/test', for_qs=True) == b'test%2Ftest'
    assert unicode_urlencode(1) == '1'


# Generated at 2022-06-13 12:32:17.034652
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('C\xE2te+d%27Ivoire') == u'Côte d\'Ivoire'


# Generated at 2022-06-13 12:32:31.147990
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode(u'abc@abc.com') == u'abc%40abc.com'
    assert unicode_urlencode(u'abc+abc.com') == u'abc%2Babc.com'
    assert unicode_urlencode(u'abc:abc.com') == u'abc:abc.com'
    assert unicode_urlencode(u'abc;abc.com') == u'abc;abc.com'
    assert unicode_urlencode(u'abc&abc.com') == u'abc%26abc.com'
    assert unicode_urlencode(u'abc=abc.com') == u'abc=abc.com'


# Generated at 2022-06-13 12:32:37.382616
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    instance = FilterModule()

    assert do_urldecode('test%20%26%20test') == u'test & test'
    assert do_urlencode('test & test') == u'test%20%26%20test'
    assert do_urlencode('test & test') == u'test%20%26%20test'
    assert do_urlencode({'test': 'test & test'}) == u'test=test%20%26%20test'



# Generated at 2022-06-13 12:32:40.689657
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    tests = (
        (u'foo+bar', u'foo bar'),
        (u'foo%20bar', u'foo bar'),
    )
    for i, o in tests:
        assert unicode_urldecode(i) == o

# Generated at 2022-06-13 12:32:50.302090
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    # strings are passed through unchanged
    assert unicode_urlencode('foo') == 'foo'
    assert unicode_urlencode(u'foo') == u'foo'
    assert unicode_urlencode('/foo') == '/foo'
    assert unicode_urlencode(u'/foo') == u'/foo'
    assert unicode_urlencode('/foo/') == '/foo/'
    assert unicode_urlencode(u'/foo/') == u'/foo/'
    assert unicode_urlencode('foo/') == 'foo/'
    assert unicode_urlencode(u'foo/') == u'foo/'
    assert unicode_urlencode('/foo/bar') == '/foo/bar'

# Generated at 2022-06-13 12:32:53.557813
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    u = u'http://www.example.com'
    e = u'http%3A%2F%2Fwww.example.com'

    assert e == unicode_urlencode(u)


# Generated at 2022-06-13 12:32:54.778097
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%20') == ' '
    assert unicode_urldecode('%26') == '&'

# Generated at 2022-06-13 12:33:04.883569
# Unit test for function unicode_urldecode
def test_unicode_urldecode():

    tests = [
        (b'foobar', 'foobar'),
        (b'foo+bar', 'foo bar'),
        (b'foo+%2B+bar', 'foo + bar'),
        (u'foobar', u'foobar'),
        (u'foo+bar', u'foo bar'),
        (u'foo+%2B+bar', u'foo + bar'),
        (b'foo+%2B+bar', u'foo + bar'),
        (b'foo+%2B+bar', 'foo + bar'),
        (u'foo+%2B+bar', 'foo + bar'),
        (u'foo+%2B+bar', u'foo + bar'),
    ]

    for (param, expected_result) in tests:
        assert unicode_urldecode(param) == expected_

# Generated at 2022-06-13 12:33:19.312668
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'%s%s') == u'%s%s'
    assert unicode_urldecode(u'%41') == u'A'
    assert unicode_urldecode(u'%41A') == u'AA'
    assert unicode_urldecode(u'$%41A') == u'$AA'
    assert unicode_urldecode(u'$%41A%41') == u'$AAAA'
    assert unicode_urldecode(u'A%41') == u'AA'
    assert unicode_urldecode(u'A%41A') == u'AAA'
    assert unicode_urldecode(u'A%41A%41') == u'AAAA'