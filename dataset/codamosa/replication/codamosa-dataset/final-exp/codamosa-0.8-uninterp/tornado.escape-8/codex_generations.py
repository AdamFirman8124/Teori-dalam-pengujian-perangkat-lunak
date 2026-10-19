

# Generated at 2022-06-14 12:05:28.347089
# Unit test for function linkify
def test_linkify():
    text = "You can link to http://www.tornadoweb.org/en/stable/ or " + \
        "to https://github.com/tornadoweb/tornado"
    result = linkify(text)
    assert '<a href="http://www.tornadoweb.org/en/stable/">http://www.tornadoweb.org/en/stable/</a>' in result
    assert '<a href="https://github.com/tornadoweb/tornado">https://github.com/tornadoweb/tornado</a>' in result
    result = linkify(text, shorten=True)
    assert '<a href="http://www.tornadoweb.org/en/stable/" title="http://www.tornadoweb.org/en/stable/">' in result

# Generated at 2022-06-14 12:05:31.609121
# Unit test for function linkify
def test_linkify():
    text = "Hey I'm a link to http://www.example.com/ so click me"
    expected = "Hey I'm a link to <a href=\"http://www.example.com/\">http://www.example.com/</a> so click me"
    assert linkify(text) == expected

# Generated at 2022-06-14 12:05:43.054272
# Unit test for function linkify

# Generated at 2022-06-14 12:05:50.138416
# Unit test for function linkify
def test_linkify():
    text = "Hello http://www.facebook.com/world!"
    expected_link_text = "Hello <a href=\"http://www.facebook.com/world\">http://www.facebook.com/world</a>!"
    assert(linkify(text) == expected_link_text)

test_linkify()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import boto3
import botocore
import os
import json
import time
import datetime
from datetime import timedelta
import yaml

# Enable to have a backfill days of data from AWS
# (does not work with Lambda as it has a limited time)
# Otherwise, it will just process the current day
# Note: set this to a negative number to get
# the number of days from the last available record
BACK

# Generated at 2022-06-14 12:05:55.085209
# Unit test for function linkify
def test_linkify():
    text1 = 'Hello world http://www.baidu.com'
    text2 = '\n<script>https://www.google.com</script>'
    text3 = '<img src="https://www.google.com">'
    text4 = '创讯：https://www.google.com'
  

# Generated at 2022-06-14 12:06:00.387708
# Unit test for function linkify
def test_linkify():
    '''This test is not complete because the linkify() function's second argument is 
    a callable extra_params. And thus the function extra_params() is tested separately'''
    import doctest
    doctest.testmod(extraglobs={'linkify': linkify})    
    

# Generated at 2022-06-14 12:06:08.484988
# Unit test for function linkify
def test_linkify():
    assert linkify("http://www.example.com") == '<a href="http://www.example.com">http://www.example.com</a>'
    assert linkify("https://www.example.com") == '<a href="https://www.example.com">https://www.example.com</a>'
    assert linkify("www.example.com") == '<a href="http://www.example.com">www.example.com</a>'
    assert linkify("ftp://ftp.example.com") == '<a href="ftp://ftp.example.com">ftp://ftp.example.com</a>'

# Generated at 2022-06-14 12:06:24.681783
# Unit test for function linkify
def test_linkify():
    # Test that we've escaped any characters that would be confusable with our
    # linkification regex.
    test_strings = (
        "http://www.google.com/?q=foo&bar",
        "http://www.google.com/?q=foo&amp;bar",
        "http://www.google.com/?q=foo&quot;bar&quot;",
        "http://www.google.com/?q=foo&#34;bar",
        "http://www.google.com/&#34;",
        "http://www.google.com/&#x22;",
    )
    for test_string in test_strings:
        assert (
            linkify(test_string) == '<a href="%s">%s</a>' % (test_string, test_string)
        )



# Generated at 2022-06-14 12:06:40.253616
# Unit test for function linkify
def test_linkify():
    text_test = 'The test string is "http://www.test.com/test" for my test. ' \
                'The test string is "www.test.com" for my test. ' \
                'The test string is "www.test.com/test" for my test. ' \
                'The test string is "http://www.test.com/index.html" for my test. ' \
                'The test string is "Https://www.test.com/index.html" for my test.'

    text_out = linkify(text=text_test, shorten=True, extra_params="target='_blank'")


# Generated at 2022-06-14 12:06:53.030622
# Unit test for function linkify

# Generated at 2022-06-14 12:07:11.119720
# Unit test for function linkify
def test_linkify():
    #to_unicode(text)
    text = [
        "Hello http://tornadoweb.org!",
        "Hello @alice, how are you doing today?",
        "Howdy, @bob!",
    ]
    #print(to_unicode(text))
    print("to_unicode: ", to_unicode(text))
    #https://api.ipify.org/?format=json
    print("linkify: \n", linkify("Hello http://tornadoweb.org!"))
    print("linkify: \n", linkify("Hello @alice, how are you doing today?"))
    print("linkify: \n", linkify("Howdy, @bob!"))
    l = 'https://api.ipify.org/?format=json'
    print("linkify: \n", linkify(l))

# Generated at 2022-06-14 12:07:21.480336
# Unit test for function linkify
def test_linkify(): 
    assert linkify('my website: http://example.com') == 'my website: <a href="http://example.com">http://example.com</a>' 
    assert linkify('example.com') == 'example.com' 
    assert linkify('example.com', require_protocol=True) == 'example.com' 
    assert linkify('foo.com/blah_blah') == '<a href="http://foo.com/blah_blah">foo.com/blah_blah</a>' 
    assert linkify('foo.com/blah_blah') == '<a href="http://foo.com/blah_blah">foo.com/blah_blah</a>' 

# Generated at 2022-06-14 12:07:34.514951
# Unit test for function linkify
def test_linkify():
    text = 'http://www.baidu.com http://www.baidu.com'
    print(linkify(text))
    print(linkify(text, extra_params='rel="nofollow" class="external"'))
    def extra_params_cb(url):
        if url.startswith("http://www.baidu.com"):
            return 'class="internal"'
        else:
            return 'class="external" rel="nofollow"'
    print(linkify(text, extra_params=extra_params_cb))
    print(linkify(text, shorten=True))
    print(linkify(text, permitted_protocols=["http","https"]))


# Generated at 2022-06-14 12:07:40.080894
# Unit test for function linkify
def test_linkify():
    assert linkify("http://google.com") == '<a href="http://google.com">http://google.com</a>'
    assert linkify("Hello http://google.com") == 'Hello <a href="http://google.com">http://google.com</a>'
    assert linkify("Hello http://google.com, and http://yahoo.com") == 'Hello <a href="http://google.com">http://google.com</a>, and <a href="http://yahoo.com">http://yahoo.com</a>'
    

# Generated at 2022-06-14 12:07:47.415058
# Unit test for function linkify
def test_linkify():
    text = "hello http://tornadoweb.org"
    print(linkify(text))
    # Are you a web developer? We'll pay you $$$ to work at Tornado! http://tornadoweb.org/contact/careers
    # Are you a web developer? We'll pay you $$$ to work at Tornado! <a href="http://tornadoweb.org/contact/careers">http://tornadoweb.org/contact/careers</a>


# Generated at 2022-06-14 12:07:54.990198
# Unit test for function linkify
def test_linkify():
    if not linkify("https://codecod.cn/")=='<a href="https://codecod.cn/">https://codecod.cn/</a>':
        return False
    if not linkify('<a href="https://codecod.cn/">https://codecod.cn/</a>')=='<a href="https://codecod.cn/">https://codecod.cn/</a>':
        return False
    return True
assert test_linkify()

# Testing for function recursive_unicode

# Generated at 2022-06-14 12:07:58.403244
# Unit test for function linkify
def test_linkify():
    t=linkify("Hello http://tornadoweb.org!")
    assert t == 'Hello <a href="http://tornadoweb.org">http://tornadoweb.org</a>!'
test_linkify()


# Generated at 2022-06-14 12:08:07.571550
# Unit test for function linkify
def test_linkify():
    assert linkify(u"Hello http://tornadoweb.org!") == \
        'Hello <a href="http://tornadoweb.org">http://tornadoweb.org</a>!'
    assert linkify(u"Visit http://tornadoweb.org/!") == \
        'Visit <a href="http://tornadoweb.org/">http://tornadoweb.org/</a>!'
    assert linkify(u"Visit http://tornadoweb.org/\n"
                   u"and http:// friendfeed.com/") == \
        'Visit <a href="http://tornadoweb.org/">http://tornadoweb.org/</a>\n' \
        'and <a href="http://friendfeed.com/">http://friendfeed.com/</a>'

# Generated at 2022-06-14 12:08:19.394804
# Unit test for function linkify
def test_linkify():
    text = linkify("http://www.baidu.com")
    assert text == """<a href="http://www.baidu.com">http://www.baidu.com</a>"""
    text = linkify("http://www.baidu.com/")
    assert text == """<a href="http://www.baidu.com/">http://www.baidu.com/</a>"""
    text = linkify("www.baidu.com")
    assert text == """<a href="http://www.baidu.com">www.baidu.com</a>"""
    text = linkify("Hello www.baidu.com")
    assert text == """Hello <a href="http://www.baidu.com">www.baidu.com</a>"""
    text

# Generated at 2022-06-14 12:08:24.055230
# Unit test for function linkify
def test_linkify():
    text = "Hello http://tornadoweb.org!"
    assert linkify(text) == u'Hello <a href="http://tornadoweb.org">http://tornadoweb.org</a>!'
    assert linkify("WoW Gold zu Goldpreisen. http://www.wowgolds.ch") == 'WoW Gold zu Goldpreisen. <a href="http://www.wowgolds.ch">http://www.wowgolds.ch</a>'

# Generated at 2022-06-14 12:09:06.231077
# Unit test for function linkify
def test_linkify():
    assert linkify("http://example.com") == '<a href="http://example.com">http://example.com</a>'
    assert linkify("http://example.com/foo?bar=baz&inga=42&quux") == '<a href="http://example.com/foo?bar=baz&amp;inga=42&amp;quux">http://example.com/foo?bar=baz&amp;inga=42&amp;quux</a>'
    assert linkify("hello http://example.com") == 'hello <a href="http://example.com">http://example.com</a>'
    assert linkify("https://example.com") == '<a href="https://example.com">https://example.com</a>'
    assert linkify("ftp://example.com")

# Generated at 2022-06-14 12:09:09.099121
# Unit test for function linkify
def test_linkify():
    print(linkify("123456www.baidu.com"))
    print(linkify("http://www.baidu.com","baidu.com"))
    print(linkify("https://www.baidu.com","baidu.com"))

#test_linkify()



# Generated at 2022-06-14 12:09:17.940619
# Unit test for function linkify

# Generated at 2022-06-14 12:09:20.894265
# Unit test for function linkify
def test_linkify():
    assert linkify('www.test.com') == '<a href="http://www.test.com">www.test.com</a>'
test_linkify()



# Generated at 2022-06-14 12:09:28.426762
# Unit test for function linkify
def test_linkify():
    text="Hello http://tornadoweb.org!"
    expected = 'Hello <a href="http://tornadoweb.org">http://tornadoweb.org</a>!'
    assert(linkify(text)==expected)

test_linkify()

_EMAIL_RE = re.compile(
    r'(?<!//)([\w.+-]+@[\w.-]+\.\w+)[\s]*'
)

# Generated at 2022-06-14 12:09:35.369813
# Unit test for function linkify
def test_linkify():
    print(linkify(
        """I like http://www.tornadoweb.org and http://www.tornadoweb.org.com and http://www.twitter.com!
        I also like https://github.com/tornadoweb/tornado. I even like www.google.com
        But without no http://, it don't work.
        And with just http://, it still don't work.
        But with http://www.google.com, works!"""
    ))
if __name__ == '__main__':
    test_linkify()

# Generated at 2022-06-14 12:09:38.815340
# Unit test for function linkify
def test_linkify():
    print(linkify("www.google.com"))
    print(linkify("http://www.google.com"))
    print(linkify("http://www.google.com/"))
    
test_linkify()


# Generated at 2022-06-14 12:09:46.989547
# Unit test for function linkify

# Generated at 2022-06-14 12:10:01.346978
# Unit test for function linkify
def test_linkify():
    text = "This is a test www.example.com and http://example.com and http://example.com:80/?q=1 and http://example.com:80/?q=1 and https://example.com:80/?q=1 and ftp://example.com:21/?q=2 and ftps://example.com:21/?q=3&foo=bar and mailto:root@example.com and javascript:alert(document.cookie) and <a href='http://example.com'>Link</a>"

# Generated at 2022-06-14 12:10:11.709744
# Unit test for function linkify
def test_linkify():
    """Test the function linkify"""
    text = "Hello http://tornadoweb.org!"
    href = "Hello <a href=\"http://tornadoweb.org\">http://tornadoweb.org</a>!"
    extra_params = "rel=\"nofollow\" class=\"external\""
    result = linkify(text, extra_params=extra_params)
    assert result == href
    def extra_params_cb(url):
        if url.startswith("http://example.com"):
            return 'class="internal"'
        else:
            return 'class="external" rel="nofollow"'
    text = "Visit my blog at http://example.com/blog"
    href = "Visit my blog at <a href=\"http://example.com/blog\" class=\"internal\">http://example.com/blog</a>"
   

# Generated at 2022-06-14 12:10:22.343261
# Unit test for function linkify
def test_linkify():
    # linkify basic test
    text = 'Hello http://tornadoweb.org!'
    result = linkify(text)
    if result != 'Hello <a href="http://tornadoweb.org">http://tornadoweb.org</a>!':
        sys.stderr.write("Wrong output!" + '\n')
        sys.exit(1)

test_linkify()


# Generated at 2022-06-14 12:10:25.646032
# Unit test for function linkify
def test_linkify():
    a = linkify("http://xueba.in/index.php?gid=1")
    print(a)
    a = linkify("www.xueba.in")
    print(a)

#test_linkify()



# Generated at 2022-06-14 12:10:36.190840
# Unit test for function linkify
def test_linkify():
    # urls with no protocol
    assert (
        linkify(
            "www.google.com",
            require_protocol=True,
            permitted_protocols=["http", "https"],
        )
        == "www.google.com"
    )
    # url without protocol and require_protocol set to False
    assert (
        linkify(
            "www.google.com",
            require_protocol=False,
            permitted_protocols=["http", "https"],
        )
        == '<a href="http://www.google.com" >www.google.com</a>'
    )
    # url with protocol and protocol not in permitted protocols

# Generated at 2022-06-14 12:10:40.125222
# Unit test for function linkify
def test_linkify():
    # if linkify("").replace("\n", "") != "":
    if linkify("Hello world"):
        print("Failed")
    else:
        print("Passed")



# Generated at 2022-06-14 12:10:50.581585
# Unit test for function linkify
def test_linkify():
    assert linkify("http://www.example.com") == '<a href="http://www.example.com">http://www.example.com</a>'
    assert linkify("Hello http://www.example.com") == 'Hello <a href="http://www.example.com">http://www.example.com</a>'
    assert linkify("http://www.example.com/extra 'stuff'") == '<a href="http://www.example.com/extra">http://www.example.com/extra</a> \'stuff\''
    assert linkify("http://www.example.com/extra_stuff") == '<a href="http://www.example.com/extra_stuff">http://www.example.com/extra_...</a>'

# Generated at 2022-06-14 12:11:02.563767
# Unit test for function linkify
def test_linkify():
    def check(text, expected):
        got = linkify(text, require_protocol=True)
        if expected != got:
            raise Exception("%r != %r" % (expected, got))

    check("http://example.com/", '<a href="http://example.com/">http://example.com/</a>')
    check("http://example.com/foo?", '<a href="http://example.com/foo?">http://example.com/foo?</a>')
    check("http://example.com/foo?bar", '<a href="http://example.com/foo?bar">http://example.com/foo?bar</a>')

# Generated at 2022-06-14 12:11:13.770845
# Unit test for function linkify
def test_linkify():
    print(linkify('http://www.google.com', shorten=True))
    print(linkify('http://www.google.com/search?q=linkify', shorten=True))
    print(linkify('http://www.google.com/search?q=linkify extra_params="nofollow"', shorten=True))
    print(linkify('www.google.com', shorten=True))
    print(linkify('http://www.google.com', shorten=True))
    print(linkify('http://www.google.com/search?q=linkify', shorten=True))
    print(linkify('http://www.google.com/search?q=linkify extra_params="nofollow"', shorten=True))
    print(linkify('www.google.com', shorten=True))

# Generated at 2022-06-14 12:11:15.730973
# Unit test for function linkify
def test_linkify():
    text = """Hello http://www.baidu.com, and http://example.com"""
    print(linkify(text))


# Generated at 2022-06-14 12:11:27.963460
# Unit test for function linkify
def test_linkify():
    assert linkify('') == ''
    assert linkify('hello') == 'hello'
    assert linkify('hello http://tornadoweb.org') == 'hello <a href="http://tornadoweb.org">http://tornadoweb.org</a>'
    assert linkify('hello https://tornadoweb.org') == 'hello <a href="https://tornadoweb.org">https://tornadoweb.org</a>'
    assert linkify('hello http://tornadoweb.org/', require_protocol=True) == 'hello <a href="http://tornadoweb.org/">http://tornadoweb.org/</a>'

# Generated at 2022-06-14 12:11:31.867319
# Unit test for function linkify
def test_linkify():
    text_input = "Hello http://tornadoweb.org!"
    text_output = "Hello <a href=\"http://tornadoweb.org\">http://tornadoweb.org</a>!"
    assert linkify(text_input) == text_output

if __name__ == "__main__":
    test_linkify()

# Generated at 2022-06-14 12:11:59.079440
# Unit test for function linkify
def test_linkify():
    text = '''Hello www.tornadoweb.org!
              http://facebook.com/
              ftp://example.com/
              hi@example.com
              example@localhost
              javascript:alert(document.cookie)
              '''
    text = linkify(text,permitted_protocols=['http','ftp','mailto'])
    print(text)

# Generated at 2022-06-14 12:12:14.455524
# Unit test for function linkify
def test_linkify():
  text=r'这是测试www.baidu.com'
  print(linkify(text, shorten=False, extra_params="", require_protocol=False,
                permitted_protocols=["http", "https"]))
  print('\n')
  text=r'这是测试www.baidu.com https://www.bing.com'
  print(linkify(text, shorten=False, extra_params="", require_protocol=False,
                permitted_protocols=["http", "https"]))
  print('\n')
  text=r'这是测试ftp://test.test.test.com'

# Generated at 2022-06-14 12:12:23.893120
# Unit test for function linkify
def test_linkify():
    assert(linkify("Hello http://tornadoweb.org!") == 'Hello <a href="http://tornadoweb.org">http://tornadoweb.org</a>!' )
    assert(linkify("Hello http://tornadoweb.org!") == 'Hello <a href="http://tornadoweb.org">http://tornadoweb.org</a>!' )
    assert(linkify("Hello www.facebook.com!") == 'Hello <a href="http://www.facebook.com">www.facebook.com</a>!' )

# Generated at 2022-06-14 12:12:34.359465
# Unit test for function linkify
def test_linkify():
    text1 = """
        http://www.tornadoweb.org/documentation
        user@example.com
        http://www.tornadoweb.org/documentation
        http://www.tornadoweb.org/en/stable/guide/templates.html#variables-in-templates
    """

# Generated at 2022-06-14 12:12:47.667890
# Unit test for function linkify
def test_linkify():
    assert linkify("Hello http://example.com") == 'Hello <a href="http://example.com">http://example.com</a>'
    assert linkify("Hello http://example.com", require_protocol=False) == 'Hello <a href="http://example.com">http://example.com</a>'
    assert linkify("Hello http://example.com", require_protocol=False, permitted_protocols=["http", "https"]) == 'Hello <a href="http://example.com">http://example.com</a>'
    assert linkify("Hello http://example.com", require_protocol=False, permitted_protocols=set(["http", "https"])) == 'Hello <a href="http://example.com">http://example.com</a>'

# Generated at 2022-06-14 12:12:55.895784
# Unit test for function linkify
def test_linkify():
    assert linkify(u'Hello http://www.microsoft.com !') == \
        u'Hello <a href="http://www.microsoft.com">http://www.microsoft.com</a> !'
    assert linkify(u'Hello www.microsoft.com !') == \
        u'Hello <a href="http://www.microsoft.com">www.microsoft.com</a> !'
    assert linkify(u'Hello http://en.wikipedia.org/wiki/URL !') == \
        u'Hello <a href="http://en.wikipedia.org/wiki/URL">http://en.wikipedia.org/wiki/URL</a> !'

# Generated at 2022-06-14 12:13:06.560774
# Unit test for function linkify
def test_linkify():
    assert linkify("http://xkcd.com/353/") == \
        '<a href="http://xkcd.com/353/">http://xkcd.com/353/</a>'
    assert linkify("www.facebook.com") == \
        '<a href="http://www.facebook.com">www.facebook.com</a>'
    assert linkify("Hello http://www.facebook.com") == \
        'Hello <a href="http://www.facebook.com">http://www.facebook.com</a>'

# Generated at 2022-06-14 12:13:18.285792
# Unit test for function linkify
def test_linkify():
    s = "https://www.google.com/webhp?sourceid=chrome-instant&amp;ion=1&amp;espv=2&amp;ie=UTF-8#q=alphago"
    ans = linkify(s)
    print("Test 1: " + ans)
    s = "https://www.google.com/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q=alphago"
    ans = linkify(s)
    print("Test 2: " + ans)

# Generated at 2022-06-14 12:13:24.314645
# Unit test for function linkify
def test_linkify():
    text = '''Hello http://tornadoweb.org!
    Yes hello http://tornadoweb.org/en/stable/!
    Also hello http://github.com/tornadoweb/tornado'''
    expected_result = '''Hello <a href="http://tornadoweb.org">http://tornadoweb.org</a>!
    Yes hello <a href="http://tornadoweb.org/en/stable/">http://tornadoweb.org/en/stable/</a>!
    Also hello <a href="http://github.com/tornadoweb/tornado">http://github.com/tornadoweb/tornado</a>'''
    assert linkify(text) == expected_result

# Generated at 2022-06-14 12:13:35.720016
# Unit test for function linkify
def test_linkify():
    """test for linkify"""
    assert linkify(
        "http://fac.book.com",
        shorten=True
    ) == '<a href="http://fac.book.com">http://fac.book.com</a>'

    assert linkify(
        "http://fac.book.com",
        shorten=False
    ) == '<a href="http://fac.book.com">http://fac.book.com</a>'

    assert linkify(
        "https://fac.book.com",
        shorten=True
    ) == '<a href="https://fac.book.com">https://fac.book.com</a>'


# Generated at 2022-06-14 12:14:04.524972
# Unit test for function linkify
def test_linkify():
    assert (linkify("http://www.google.com") == '<a href="http://www.google.com">http://www.google.com</a>')
    assert (linkify("www.google.com") == '<a href="http://www.google.com">www.google.com</a>')
    assert (linkify("Hello http://www.google.com", shorten=True) == 'Hello <a href="http://www.google.com">http://www.google.com</a>')
    assert (linkify("Hello http://www.google.com", shorten=True, extra_params='class="bar"') == 'Hello <a href="http://www.google.com" class="bar">http://www.google.com</a>')

# Generated at 2022-06-14 12:14:15.723283
# Unit test for function linkify
def test_linkify():
  assert "<a href='http://a.b/c'>" in linkify('http://a.b/c')
  assert linkify('http://a.b/c') == linkify('<>http://a.b/c')
  assert "<a href='http://a.b/c'>" in linkify('<>http://a.b/c')
  assert linkify('http://a.b/c') == linkify('<>http://a.b/c<>')
  assert "<a href='http://a.b/c'>" in linkify('<>http://a.b/c<>')
  assert linkify('http://a.b/c') == linkify('<http://a.b/c>')

# Generated at 2022-06-14 12:14:24.413738
# Unit test for function linkify
def test_linkify():
    assert linkify("http://x.com") == '<a href="http://x.com">http://x.com</a>'
    assert linkify("x.com") == '<a href="http://x.com">x.com</a>'
    assert (
        linkify("Go to http://www.facebook.com/tornadoweb")
        == 'Go to <a href="http://www.facebook.com/tornadoweb">www.facebook.com/tornadoweb</a>'
    )

# Generated at 2022-06-14 12:14:39.508620
# Unit test for function linkify
def test_linkify():
    for i in range(4):
        random_test = "".join(random.sample(string.ascii_letters * 10, 100))
        print(random_test, "\n", linkify(random_test), "\n")
# test_linkify()

# This print function can output the final result in style-preserving way
# def print_beautiful(line):
#     print(linkify(line.replace("\n", " \\line ")))
# Unit Test for function print_beautiful
# def test_print_beautiful():
#     random_test = "".join(random.sample(string.ascii_letters * 10, 100))
#     print(random_test, "\n", linkify(random_test), "\n")
# test_print_beautiful()

# This class is the main part!

# Generated at 2022-06-14 12:14:47.436495
# Unit test for function linkify
def test_linkify():
    assert linkify("http://example.com/foo+bar") == '<a href="http://example.com/foo+bar">http://example.com/foo+bar</a>'
    assert linkify("http://example.com/foo+bar", require_protocol=False) == '<a href="http://example.com/foo+bar">example.com/foo+bar</a>'
    assert linkify("www.example.com/foo+bar", require_protocol=False) == '<a href="http://www.example.com/foo+bar">www.example.com/foo+bar</a>'
    assert linkify("foo+bar@example.com", require_protocol=False) == '<a href="mailto:foo+bar@example.com">foo+bar@example.com</a>'
   

# Generated at 2022-06-14 12:14:58.956835
# Unit test for function linkify
def test_linkify():
    assert linkify("http://example.com") == '<a href="http://example.com">http://example.com</a>'
    assert linkify("Hello http://example.com!") == 'Hello <a href="http://example.com">http://example.com</a>!'
    assert linkify("Hello http://example.com:8000/foo") == 'Hello <a href="http://example.com:8000/foo">http://example.com:8000/foo</a>'
    assert linkify("www.example.com") == '<a href="http://www.example.com">www.example.com</a>'
    assert linkify("Hello www.example.com!") == 'Hello <a href="http://www.example.com">www.example.com</a>!'

# Generated at 2022-06-14 12:15:07.921822
# Unit test for function linkify
def test_linkify():
    linkify("Hello!")
    linkify("Hello http://tornadoweb.org!")
    linkify("Hello http://tornadoweb.org/!")
    linkify("Hello http://tornadoweb.org/", shorten=True)
    linkify("Hello http://tornadoweb.org/!")
    linkify("Hello http://tornadoweb.org/!")
 
test_linkify()

# Regular expression used to match urls in plain text