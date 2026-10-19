

# Generated at 2022-06-14 07:11:29.768731
# Unit test for function fwd_normalize
def test_fwd_normalize():
    def check(pair):
        assert fwd_normalize([pair])[pair[0]] == pair[1]

    check(('by', '1.2.3.4'))
    check(('for', '1.2.3.4'))
    check(('by', 'example.com'))
    check(('for', 'example.com'))
    check(('by', 'example.com'))
    check(('for', 'example.com'))
    check(('proto', 'http'))
    check(('host', 'example.com'))
    check(('port', '8080'))
    check(('path', '/hello/world'))

# Generated at 2022-06-14 07:11:33.940944
# Unit test for function parse_forwarded
def test_parse_forwarded():
    # Test case 1
    test_pairs: OptionsIterable = [("By", "192.0.2.43"), ("Foo", "Bar"), ("Foo", "baz")]
    assert fwd_normalize(test_pairs) == {"by": "192.0.2.43", "foo": "baz"}

    # Test case 2
    test_pairs = [("Foo", "Bar"), ("Bazz", "quux")]
    assert fwd_normalize(test_pairs) == {"foo": "Bar", "bazz": "quux"}

    # Test case 3
    test_pairs = [("For", "192.0.2.43"), ("For", "198.51.100.17")]

# Generated at 2022-06-14 07:11:49.682286
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    from sanic.config import Config
    config = Config()
    config.REAL_IP_HEADER = 'X-Real-Ip'
    config.FORWARDED_FOR_HEADER = 'X-Forwarded-For'
    
    headers = {
        'X-Real-Ip': '192.168.1.1',
        'X-Forwarded-For': '192.168.1.2'
    }
    assert parse_xforwarded(headers, config) == parse_forwarded(headers, config)
    headers = {
        'X-Real-Ip': '192.168.1.1',
        'X-Forwarded-For': '192.168.1.2, 192.168.1.3'
    }

# Generated at 2022-06-14 07:11:56.510198
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers={"x-real-ip": "123.45.67.89",
             "x-forwarded-for": "123.45.67.89, 127.0.0.1",
             "x-scheme": "http",
             "x-forwarded-proto": "https",
             "x-forwarded-host": "example.com",
             "x-forwarded-port": "443",
             "x-forwarded-path": "/path/to/root"}
    config = base.Config()
    config.PROXIES_COUNT = 0
    print(parse_xforwarded(headers, config))

# Generated at 2022-06-14 07:12:09.483076
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    from sanic.exceptions import InvalidUsage
    import warnings
    import pytest
    from sanic.server import HttpProtocol
    from sanic.testing import HOST, PORT
    from sanic import Sanic
    from sanic.response import redirect
    from sanic.request import Request

    app = Sanic("test_parse_xforwarded")

    @app.route("/")
    async def handler(request):
        return await request.app.loop.run_in_executor(
            None,
            parse_xforwarded,
            request.headers,
            request.app.config,
        )

    request, response = app.test_client.get(
        "/", headers={"x-forwarded-host": "host"}
    )
    assert response.json["host"] == "host"
    assert response

# Generated at 2022-06-14 07:12:22.710107
# Unit test for function fwd_normalize_address
def test_fwd_normalize_address():
    assert fwd_normalize_address("[0:0:0:0:0:0:0:0]") == "[::]"
    assert fwd_normalize_address("[::]") == "[::]"
    assert fwd_normalize_address("0:0:0:0:0:0:0:0") == "[::]"
    assert fwd_normalize_address("localhost") == "localhost"
    assert fwd_normalize_address("::1") == "[::1]"
    assert fwd_normalize_address("::1") == "[::1]"
    assert fwd_normalize_address("127.0.0.1") == "127.0.0.1"
    assert fwd_normalize_address("127.0.0.1:8000") == "127.0.0.1"


# Generated at 2022-06-14 07:12:31.662027
# Unit test for function parse_forwarded
def test_parse_forwarded():
    print('-----test_parse_forwarded-----')
    print('parse_forwarded({}, {})'.format(None, None))
    print(parse_forwarded(None, None))
    print('-----')
    print('parse_forwarded({}, {})'.format(None, 'hello'))
    print(parse_forwarded(None, 'hello'))
    print('-----')
    print('parse_forwarded({}, {})'.format('hello', 'hello'))
    print(parse_forwarded('hello', 'hello'))
    print('-----')
    print('parse_forwarded({}, {})'.format(None, 'hello'))
    print(parse_forwarded(None, 'hello'))
    print('-----')
    print('parse_forwarded({}, {})'.format('hello', 'hello'))
   

# Generated at 2022-06-14 07:12:45.228944
# Unit test for function fwd_normalize
def test_fwd_normalize():
    assert fwd_normalize([]) == {}
    assert fwd_normalize([("by", "1.1.1.1"), ("host", "host")]) == {
        "host": "host",
        "by": "1.1.1.1",
    }
    assert fwd_normalize({"proto": "scheme", "host": "host"}) == {
        "proto": "scheme",
        "host": "host",
    }
    assert fwd_normalize([("proto", "scheme"), ("host", "host")]) == {
        "proto": "scheme",
        "host": "host",
    }

# Generated at 2022-06-14 07:12:56.621775
# Unit test for function parse_forwarded
def test_parse_forwarded():
    from sanic import Sanic
    from sanic.config import Config
    from sanic.request import Request
    app = Sanic(__name__)
    config = Config()
    # Basic with by and secret
    req = Request(
        "GET",
        "/",
        headers={"forwarded": 'host="blah.com"; secret="top secret"; by=_me'},
        config=config,
        app=app,
    )
    assert parse_forwarded(req.headers, config) == {
        "host": "blah.com",
        "by": "_me",
    }
    # Basic with by and secret, reversed

# Generated at 2022-06-14 07:13:08.559899
# Unit test for function parse_forwarded
def test_parse_forwarded():
    headers = [
        "for=192.0.2.60; proto=http; host=",
        "by=203.0.113.43; secret=\"secret\"; for=192.0.2.43",
        "by=203.0.113.43; secret=\"secret\",for=192.0.2.43",
        "for=192.0.2.43,for=198.51.100.17",
        "secret=\"secret\"",
        "secret=\"secret\",by=203.0.113.43; for=192.0.2.43",
        "secret=\"secret\",by=203.0.113.43; for=192.0.2.43,for=",
        "secret=\"secret\",for=192.0.2.43,by=203.0.113.43",
    ]
   

# Generated at 2022-06-14 07:13:26.869241
# Unit test for function parse_content_header
def test_parse_content_header():
    assert parse_content_header('form-data; name=upload; filename="file.txt"') == (
        'form-data',
        {'name': 'upload', 'filename': 'file.txt'}
    )
    assert parse_content_header('form-data; name=upload; filename=file.txt') == (
        'form-data',
        {'name': 'upload', 'filename': 'file.txt'}
    )
    assert parse_content_header('form-data') == (
        'form-data',
        {}
    )
    assert parse_content_header('form-data; name=upload; filename="file.txt"; a=b') == (
        'form-data',
        {'name': 'upload', 'filename': 'file.txt', 'a': 'b'}
    )
   

# Generated at 2022-06-14 07:13:39.280991
# Unit test for function fwd_normalize
def test_fwd_normalize():
    assert fwd_normalize("") == {}
    assert fwd_normalize("    ") == {}
    assert fwd_normalize(";") == {}
    assert fwd_normalize("  ;  ") == {}
    assert fwd_normalize("; ") == {}
    assert fwd_normalize(" ;") == {}
    assert fwd_normalize(";;") == {}
    assert fwd_normalize("key=v") == {"key": "v"}
    assert fwd_normalize("foo=42") == {"foo": "42"}
    assert fwd_normalize("foo=bar") == {"foo": "bar"}
    assert fwd_normalize("p=42;foo=bar") == {"foo": "bar", "p": "42"}

# Generated at 2022-06-14 07:13:49.445315
# Unit test for function fwd_normalize
def test_fwd_normalize():
    assert fwd_normalize([('for', 'foobar')]) == {'for': 'foobar'}
    assert fwd_normalize([('proto', 'HTTP')]) == {'proto': 'http'}
    assert fwd_normalize([('proto', 'HTTP'), ('proto', 'HTTPS')]) == {'proto': 'https'}
    assert fwd_normalize([('port', '80')]) == {'port': 80}
    assert fwd_normalize([('path', '/foo')]) == {'path': '/foo'}
    assert fwd_normalize([('path', '/foo%2Fbar')]) == {'path': '/foo/bar'}
    assert fwd_normalize([('foo', 'bar')]) == {}
    
    

# Generated at 2022-06-14 07:14:03.669921
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    class FakeHeaders:
        def __init__(self, headers):
            self._headers = headers
        def get(self, name):
            return self._headers[name] if name in self._headers else None
        def getall(self, name):
            return self._headers[name] if name in self._headers else []
    config = FakeConfig()
    config.FORWARDED_SECRET = ''
    config.REAL_IP_HEADER = 'x-real-ip'
    config.PROXIES_COUNT = 1
    config.FORWARDED_FOR_HEADER = 'x-forwarded-for'

# Generated at 2022-06-14 07:14:09.273368
# Unit test for function parse_forwarded
def test_parse_forwarded():
    _, options = parse_forwarded(
        {
            "forwarded": [
                r"for=192.0.2.60;proto=http;by=203.0.113.43",
                r"For=\"[2001:db8:cafe::17]:4711\";By=_mdn-127\\.0\\.0\\.1",
            ]
        },
        {
            "FORWARDED_SECRET": "secret"
        },
    )
    assert options == {
        "for": "192.0.2.60",
        "proto": "http",
        "by": "203.0.113.43",
    }

# Generated at 2022-06-14 07:14:17.743281
# Unit test for function parse_forwarded
def test_parse_forwarded():
    headers = {'Forwarded': 'for=192.0.2.43, for=198.51.100.17;proto=https, for="[2001:db8:cafe::17]";secret="{{secret}}"'}
    config = {'FORWARDED_SECRET': '{{secret}}'}
    options = {'for': '198.51.100.17', 'proto': 'https'}
    assert parse_forwarded(headers, config) == options

# Generated at 2022-06-14 07:14:21.088282
# Unit test for function parse_content_header
def test_parse_content_header():
    assert parse_content_header('foo/bar; name="upload"; filename="file.txt"') == ('foo/bar', {'name': 'upload', 'filename': 'file.txt'})

# Generated at 2022-06-14 07:14:31.284855
# Unit test for function fwd_normalize
def test_fwd_normalize():
    assert fwd_normalize([("for", "1")]) == {"for": "1"}
    assert fwd_normalize([("for", "1.2.3.4")]) == {"for": "1.2.3.4"}
    assert fwd_normalize([("for", "[::1]")]) == {"for": "[::1]"}
    assert fwd_normalize([("for", "::1")]) == {"for": "[::1]"}
    assert fwd_normalize([("for", "unknown")]) == {}
    assert fwd_normalize([("for", "1.2.3.4")]) == {"for": "1.2.3.4"}
    assert fwd_normalize([("for", "unknown")]) == {}

# Generated at 2022-06-14 07:14:43.619970
# Unit test for function parse_forwarded
def test_parse_forwarded():
    def forward(header):
        return parse_forwarded({'Forwarded':header}, Config(FORWARDED_SECRET='xxx'))
    assert forward(
        'secret=no,proto=https,for=192.0.2.60:443;host=example.com') is None
    assert forward(
        'secret=xxx,proto=https,for=192.0.2.60:443;host=example.com') == {
        'proto': 'https', 'for': '192.0.2.60', 'host': 'example.com'}

# Generated at 2022-06-14 07:14:47.425265
# Unit test for function parse_content_header
def test_parse_content_header():
    content_type = "application/json; charset=utf-8"
    assert parse_content_header(content_type) == ('application/json', {'charset': 'utf-8'})

# Generated at 2022-06-14 07:15:05.445149
# Unit test for function parse_forwarded
def test_parse_forwarded():
    """Unit test for parse_forwarded()"""

    class Headers(object):
        getall = lambda self, key, default=None: getattr(self, key, default)

    class Conf(object):
        FORWARDED_SECRET = None
        PROXIES_COUNT = None
        FORWARDED_FOR_HEADER = None
        REAL_IP_HEADER = None

    assert parse_forwarded(Headers(), Conf()) is None

    class Conf(object):
        FORWARDED_SECRET = "secret"
        PROXIES_COUNT = None
        FORWARDED_FOR_HEADER = None
        REAL_IP_HEADER = None

    assert parse_forwarded(Headers(forwarded="secret=secret"), Conf()) is None
    assert parse_forwarded(Headers(forwarded="other=secret"), Conf())

# Generated at 2022-06-14 07:15:13.669421
# Unit test for function parse_forwarded
def test_parse_forwarded():
    assert parse_forwarded({
        'forwarded': [
            'for=127.0.0.1; proto=https; by=192.168.1.1'
        ]
    }, {
        'FORWARDED_SECRET': 'secret'
    }) == {
        'by': '192.168.1.1',
        'for': '127.0.0.1',
        'proto': 'https'
    }

# Generated at 2022-06-14 07:15:19.837601
# Unit test for function parse_forwarded
def test_parse_forwarded():
    test_input = "kafka=wurst, by=192.168.0.1; secret=sauce"
    output = parse_forwarded(test_input)
    if output is not None:
        if output['secret'] == "sauce" and output['kafka'] == "wurst" and output['by'] == "192.168.0.1":
            print("test_parse_forwarded passed")
        else:
            print("test_parse_forwarded failed")

# Generated at 2022-06-14 07:15:33.557840
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    req = {
        'headers': {
            'x-forwarded-path': '/',
            'x-forwarded-for': '192.168.1.1',
            'x-forwarded-proto': 'https',
            'x-forwarded-port': '443',
            'x-forwarded-host':  '127.0.0.1',
        },
        'host': '127.0.0.1',
        'port': 443
    }

# Generated at 2022-06-14 07:15:47.814956
# Unit test for function parse_forwarded
def test_parse_forwarded():
    a = "secret=\"foo\"; for=\"194.1.2.3\", for=192.0.2.43, for=198.51.100.17, for=2001:db8:cafe::17"

    print("a = ", a)
    print("---------------------------")
    for m in _rparam.finditer(a[::-1]):
        print("start() = ", m.start(), "; end() = ", m.end())
        print("groups() = ", m.groups())

    # print("---------------------------")
    # # Loop over <separator><key>=<value> elements from right to left
    # sep = pos = None
    # options: List[Tuple[str, str]] = []
    # found = False
    # for m in _rparam.finditer(a[::-1]):

# Generated at 2022-06-14 07:15:55.682606
# Unit test for function parse_forwarded
def test_parse_forwarded():
    from .response import HTTPResponse

    headers = HTTPResponse.headers_class([
        ("Forwarded", "For=\"_mdnh\"; By=\"10.0.0.1\"; Proto=https; "
                     "Host=proxy.example.com; FOO=BAR"),
        ("Forwarded", "for=192.0.2.43; proxy, by=\"[2001:db8:cafe::17]\""),
        ("Forwarded", "for=192.0.2.60; proto=http; host=example.com"),
        ("Forwarded", "for=192.0.2.43, for=198.51.100.17")
    ])

    config = lambda: None  # type: ignore
    config.FORWARDED_SECRET = None
    assert parse_forwarded(headers, config)

# Generated at 2022-06-14 07:16:03.198292
# Unit test for function parse_forwarded
def test_parse_forwarded():
    headers = {'Forwarded': ['by=www.example.org;secret=xyz,for=192.0.2.43;secret=xyz']}
    options = parse_forwarded(headers, 'xyz')
    assert options['by'] == 'www.example.org'
    assert options['for'] == '192.0.2.43'
    assert options['secret'] == 'xyz'


# Generated at 2022-06-14 07:16:16.335873
# Unit test for function parse_forwarded
def test_parse_forwarded():
    import unittest


# Generated at 2022-06-14 07:16:29.257780
# Unit test for function parse_forwarded
def test_parse_forwarded():
    # test data
    header = 'for=192.0.2.60;proto=http;host=example.com;by=203.0.113.43'
    secret = '123'
    options = {'for': '192.0.2.60', 'proto': 'http', 'host': 'example.com', 'by': '203.0.113.43'}

    def get_header(header, secret=None):
        headers = CIMultiDict({'forwarded': header})
        config = SimpleNamespace(FORWARDED_SECRET=secret)
        return parse_forwarded(headers, config)

    assert options == get_header(header, secret)
    assert None == get_header(header, secret='1234')
    assert None == get_header(header, secret=None)
    assert None

# Generated at 2022-06-14 07:16:32.236563
# Unit test for function parse_forwarded
def test_parse_forwarded():
    assert parse_forwarded({"Forwarded": "foo, for=_, by=bar"}, {}) == {"for": "_", "by": "bar"}

# Generated at 2022-06-14 07:16:56.431387
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    import sanic
    app = sanic.Sanic(__name__)

    headers = {"X-Forwarded-Proto": "https",
        "x-forwarded-host": "a.com", 
        "x-forwarded-port": "8888", 
        "x-forwarded-path": "/b/c", 
        "real-ip-header": "127.0.0.1", 
        "x-forwarded-for": "127.0.0.1"}
    
    print(parse_xforwarded(headers, app.config))

# Generated at 2022-06-14 07:17:04.774956
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {
        "X-Forwarded-For": "2001:0db8:85a3:0000:0000:8a2e:0370:7334",
        "X-Forwarded-Proto": "https",
        "X-Forwarded-Host": "someserver.com",
        "X-Forwarded-Port": "443",
        "X-Forwarded-Path": "/test.html"
    }
    print(parse_xforwarded(headers))


# Generated at 2022-06-14 07:17:14.491109
# Unit test for function parse_forwarded
def test_parse_forwarded():
    cfg = Config()
    cfg.FORWARDED_SECRET = "secret"
    f1 = 'for="_gazonk";proto=http;by=_gazonk, for="[2001:db8:cafe::17]:4711" ; by=_gazonk;host=example.com'
    f2 = 'for="_gazonk"; host=example.com; by=_gazonk'
    f3 = ' for="[192.0.2.60]";host=example.com;proto=http;by=_gazonk, for="[2001:db8:cafe::17]:4711" ; by=_gazonk'

# Generated at 2022-06-14 07:17:19.396829
# Unit test for function parse_forwarded
def test_parse_forwarded():
    forwarded = parse_forwarded(
        "secret=foo; for=127.0.0.1, secret=bar; for=\"[::1]\"", "foo"
    )
    assert forwarded == {"for": "127.0.0.1"}



# Generated at 2022-06-14 07:17:28.218549
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {
        'X-Forwarded-Proto': 'http',
        'X-Forwarded-Host': '127.0.0.1:5000',
        'X-Forwarded-Port': '5000',
        'X-Forwarded-Path': '/',
        'X-Forwarded-For': '127.0.0.1, [2001:db8::1], [::1]',
    }
    assert parse_xforwarded(headers, {}) == {
        'proto': 'http',
        'host': '127.0.0.1:5000',
        'port': 5000,
        'path': '/',
        'for': '127.0.0.1'
    }

# Generated at 2022-06-14 07:17:33.224758
# Unit test for function parse_forwarded
def test_parse_forwarded():
    test_dict = {'host': 'example.com', 'proto': 'https', 'for': '10.0.0.1'}
    assert parse_forwarded(['for = 10.0.0.1;by = "secret";host = example.com;proto = https'], Dict) == test_dict

# Generated at 2022-06-14 07:17:44.773787
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    class MockHeaders():
        def __init__(self):
            self.real_ip_header = "X-Forwarded-For"
            self.proxies_count = 1
            self.forwarded_for_header = "X-Forwarded-For"
            self.headers = {
                "X-Forwarded-For": ["127.0.0.1"],
                "X-Forwarded-Path": "/test"
            }
        def get(self, key):
            return self.headers.get(key)
        def getall(self, key):
            return self.headers.get(key)
    ret = parse_xforwarded(MockHeaders(), "")
    assert ret.get("for") == "127.0.0.1"
    assert ret.get("path") == "/test"

# Generated at 2022-06-14 07:17:50.238554
# Unit test for function parse_forwarded
def test_parse_forwarded():
    d = {'forwarded': 'for=192.0.2.43, for="[2001:db8:cafe::17]";proto=https;host="test.org:8301",secret=1a2b3c'}
    print(d['forwarded'])
    print(parse_forwarded(d, None))

# Generated at 2022-06-14 07:17:57.628303
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {"X-Forwarded-For": "1.1.1.1, 2.2.2.2, 3.3.3.3"}
    config = SanicConfig(FORWARDED_FOR_HEADER="X-Forwarded-For")
    result = parse_xforwarded(headers, config)
    assert "for" in result
    assert result["for"] == "3.3.3.3"

# Generated at 2022-06-14 07:18:08.140030
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    forwarded_for = [
        'for=192.0.2.60;proto=http;by=203.0.113.43',
        'for=192.0.2.43,for=198.51.100.17',
        'for=192.0.2.43;proto=http;by=203.0.113.43',
        'for=192.0.2.43;proto=http;by=203.0.113.43,for=198.51.100.17'
    ]

    # Test case 1
    # 1 element
    headers = {
        "X-Forwarded-For": forwarded_for[0],
        "Real-Ip-Header": "test",
        "Proxies-Count": 1,
    }


# Generated at 2022-06-14 07:18:51.596506
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {
        'X-Forwarded-For': '70.123.233.0',
        'X-Forwarded-Host': 'mlp.com',
        'X-Forwarded-Port': '8080',
        'X-Forwarded-Proto': 'https',
        'X-Forwarded-Path': '/',
        'X-Scheme': 'http',
        'X-Real-IP': '70.123.233.0',
        'Forwarded': 'for=70.123.233.0;by=133.4.4.4;proto=https;host=mlp.com;port=8080;path=/;',
        'Forwarded': 'for=2.2.2.2;'
    }
    class Config:
        PROXIES_COUNT = 100
        REAL_IP_HEAD

# Generated at 2022-06-14 07:19:04.991040
# Unit test for function parse_forwarded
def test_parse_forwarded():
    import sys
    sys.path.append('..')
    from utils.web.requests import parse_forwarded
    from utils.common.exceptions import SanicException
    from utils.web.config import Config
    
    print(parse_forwarded({'forwarded': 'by=10.0.0.1; host=localhost:8000; for=192.168.0.1; proto=http'}, Config(FORWARDED_SECRET='')))
    print(parse_forwarded({'forwarded': 'host=localhost:8000; by=10.0.0.1; for=192.168.0.1; proto=http'}, Config(FORWARDED_SECRET='yuer')))

# Generated at 2022-06-14 07:19:09.976573
# Unit test for function parse_forwarded
def test_parse_forwarded():
    headers = {"forwarded": ["secret=foo; by=[2001:db8::1]:99;for=127.0.0.1"]}
    config = {"FORWARDED_SECRET": "foo"}
    assert parse_forwarded(headers, config) == {'for': '127.0.0.1', 'by': '[2001:db8::1]:99'}

# Generated at 2022-06-14 07:19:19.168604
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {
        u'x-scheme': u'https',
        u'x-forwarded-host': u'example.com',
        u'x-forwarded-path': u'/%E6%B5%8B%E8%AF%95%E6%96%B0%E6%77%83%E6%9C%89',
        u'x-forwarded-proto': u'http',
        u'x-forwarded-port': u'8080',
        u'x-real-ip': u'127.0.0.1'
    }
    ret = parse_xforwarded(headers)

# Generated at 2022-06-14 07:19:20.383785
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    print(parse_xforwarded('test',1))

# Generated at 2022-06-14 07:19:32.332198
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    from sanic.response import HTTPResponse
    from sanic.server import HttpProtocol
    from sanic.config import Config
    config = Config()
    protocol = HttpProtocol(self_check_host=False, loop=None, config=config)
    request = protocol.request_parser.parse_request(
        b"GET / HTTP/1.1\r\n"
        b"Host: example.com\r\n"
        b"X-Real-IP: 127.0.0.1\r\n"
        b"X-Forwarded-For: 127.0.0.1,127.0.0.2\r\n"
        b"\r\n",
        socket_buffer=b"",
        protocol=protocol,
        payload=None,
    )

# Generated at 2022-06-14 07:19:45.411872
# Unit test for function parse_forwarded
def test_parse_forwarded():
    from sanic import Sanic
    app = Sanic("Parse Forwarded Test")
    app.config.FORWARDED_SECRET = "v3ryS3cr3t"
    app.config.REAL_IP_HEADER = "X-Real-IP"
    app.config.FORWARDED_FOR_HEADER = "X-Forwarded-For"
    app.config.PROXIES_COUNT = 2


# Generated at 2022-06-14 07:19:57.916030
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    config=Config()
    config.REAL_IP_HEADER="X-Forwarded-For"
    config.FORWARDED_FOR_HEADER="X-Forwarded-For"
    config.PROXIES_COUNT=2

# Generated at 2022-06-14 07:20:08.358358
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    xheaders = {'X-Forwarded-Host': 'tss.com',
                'X-Forwarded-Port': '8888',
                'X-Forwarded-For': '127.0.0.1,172.17.0.1',
                'X-Forwarded-Proto': 'https',
                'x-scheme': 'http'}
    options = parse_xforwarded(xheaders, 'test')
    assert options['host'] == 'tss.com'
    assert options['port'] == 8888
    assert options['for'] == '127.0.0.1'
    assert options['proto'] == 'https'

# Generated at 2022-06-14 07:20:14.612662
# Unit test for function parse_forwarded
def test_parse_forwarded():
  headers = {
    'Forwarded': 'for="_gazonk"',
    'Forwarded': 'for=192.0.2.43, for=198.51.100.17'
  }
  result = parse_forwarded(headers)
  assert result['for'] == '192.0.2.43', result['for']

if __name__ == "__main__":
  test_parse_forwarded()