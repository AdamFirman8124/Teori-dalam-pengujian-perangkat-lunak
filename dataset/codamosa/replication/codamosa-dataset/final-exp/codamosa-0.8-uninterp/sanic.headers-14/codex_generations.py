

# Generated at 2022-06-14 07:11:22.600891
# Unit test for function fwd_normalize
def test_fwd_normalize():
    result = fwd_normalize((("by", "127.0.0.1"), ("port", "80")))
    assert result == {"by": "127.0.0.1", "port": 80}

    result = fwd_normalize((("by", "127.0.0.1"), ("port", "8080")))
    assert result == {"by": "127.0.0.1", "port": 8080}

    result = fwd_normalize((("for", "_bob"), ("port", "80")))
    assert result == {"for": "_bob", "port": 80}

    result = fwd_normalize((("by", "unknown")))
    assert result == {}


# Generated at 2022-06-14 07:11:24.219483
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    assert parse_xforwarded({},{}) == None
    

# Generated at 2022-06-14 07:11:30.506643
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {"x-forwarded-for": "192.168.1.1", "x-forwarded-host": "test.com"}
    config = {"PROXIES_COUNT": 1}
    assert parse_xforwarded(headers, config) == {
        'for': '192.168.1.1', 'host': 'test.com'
    }

# Generated at 2022-06-14 07:11:44.204117
# Unit test for function fwd_normalize
def test_fwd_normalize():
    # Test function fwd_normalize
    options = [('for', '::1'), ('by', '::1'), ('proto', 'https'), ('host', 'foo.com'), ('port', 1234), ('path', 'FooBar')]
    options_dict = fwd_normalize(options)
    assert options_dict['for'] == '::1'
    assert options_dict['by'] == '::1'
    assert options_dict['proto'] == 'https'
    assert options_dict['host'] == 'foo.com'
    assert options_dict['port'] == 1234
    assert options_dict['path'] == 'FooBar'

# Generated at 2022-06-14 07:11:55.651594
# Unit test for function parse_forwarded
def test_parse_forwarded():
    blueprint = {"host": "host", "path": "path", "proto": "proto", "port": "port"}

# Generated at 2022-06-14 07:12:07.608669
# Unit test for function parse_forwarded
def test_parse_forwarded():
    from sanic.config import Config
    from sanic.request import RequestParameters

    # Create a configuration object and assign this to the server
    config = Config()

    # Example of a Forwarded header string for testing
    # Forwarded: for=192.0.2.43, for=\"[2001:db8:cafe::17]\";by=203.0.113.60;proto=https;host=example.com
    header_string = "forwarded: for=192.0.2.43,for=\"[2001:db8:cafe::17]\";by=203.0.113.60;proto=https;host=example.com"

    # Create an empty RequestParameters object
    request_parameters = RequestParameters({})

    # Create a dummy 'headers' object that is similar to a sanic.request.Request object


# Generated at 2022-06-14 07:12:21.819347
# Unit test for function parse_forwarded
def test_parse_forwarded():
    headers = {'Forwarded': 'By=r2.sanic.app;For=127.0.0.1;Proto=http'}
    config = {'FORWARDED_SECRET':'r2.sanic.app'}
    ret = parse_forwarded(headers, config)
    print(ret) # {'by': 'r2.sanic.app', 'for': '127.0.0.1', 'proto': 'http'}

    headers = {'Forwarded': 'By=r2.sanic.app;For=127.0.0.1;Proto=http, By=r2.sanic.app;For=127.0.0.1;Proto=http'}
    config = {'FORWARDED_SECRET':'r2.sanic.app'}

# Generated at 2022-06-14 07:12:31.850370
# Unit test for function parse_forwarded
def test_parse_forwarded():
    for header in [
        "host=example.com,by=proxy1",
        "host=example.com; by=proxy1",
        'host=example.com; by="proxy1"',
        'host=example.com; by="\"proxy1\""',
        "host=example.com, by, proxy1",
        "host=example.com, by, \"proxy1",
        "host=example.com, by=proxy1, secret=test1234, proto=https",
    ]:
        print(parse_forwarded({'FORWARDED': header}, None).get("secret", None))

# Generated at 2022-06-14 07:12:44.520621
# Unit test for function parse_host
def test_parse_host():
    assert parse_host('[::1]:80') == ('[::1]', 80)
    assert parse_host(':80') == ('', 80)
    assert parse_host('[::1]') == ('[::1]', None)
    assert parse_host('[::1') is None
    assert parse_host('') is None
    assert parse_host('[') is None
    assert parse_host('[]:80') is None
    assert parse_host('[::1]:') == ('[::1]', None)
    assert parse_host('[::1]:-1') is None
    assert parse_host('[::1]:65536') is None
    assert parse_host('[::1]:65537') is None



# Generated at 2022-06-14 07:12:56.127620
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    from sanic.exceptions import InvalidUsage
    config = Mock()
    config.PROXIES_COUNT = 1
    config.FORWARDED_FOR_HEADER = 'x-forwarded-for'
    config.REAL_IP_HEADER = None
    headers = {
        'x-forwarded-for': '127.0.0.1,127.0.0.2'
    }
    expected_options = {
        'for': '127.0.0.1'
    }
    options = parse_xforwarded(headers, config)
    assert options == expected_options

    config.PROXIES_COUNT = 2
    config.FORWARDED_FOR_HEADER = 'x-forwarded-for'
    config.REAL_IP_HEADER = None

# Generated at 2022-06-14 07:13:12.382147
# Unit test for function parse_forwarded

# Generated at 2022-06-14 07:13:14.643961
# Unit test for function parse_forwarded
def test_parse_forwarded():
    pass



if __name__ == "__main__":
    test_parse_forwarded()

# Generated at 2022-06-14 07:13:26.726710
# Unit test for function parse_forwarded

# Generated at 2022-06-14 07:13:39.183460
# Unit test for function parse_forwarded
def test_parse_forwarded():
    from sanic.response import HTTPResponse
    from sanic import Sanic
    from sanic.request import Request
    app = Sanic('test_parse_forwarded')
    app.config.FORWARDED_SECRET = None
    @app.route("/")
    async def test(request):
        print(request.headers)
        print(request.forwarded)
        return HTTPResponse("OK")

# Generated at 2022-06-14 07:13:49.376543
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {"X-Forwarded-For": "192.168.0.1"}
    assert ("for", "192.168.0.1") == parse_xforwarded(headers, config)[0]
    config.PROXIES_COUNT = 2
    headers = {
        "X-Forwarded-For": "192.168.0.1, 192.168.0.2, 192.168.0.3"
    }
    assert ("for", "192.168.0.2") == parse_xforwarded(headers, config)[0]
    headers = {"X-Forwarded-For": "192.168.0.1"}
    config.PROXIES_COUNT = -1
    assert ("for", "192.168.0.1") == parse_xforwarded(headers, config)[0]

# Generated at 2022-06-14 07:14:00.179881
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    """Test parsing of xforwarded headers."""
    from sanic import Sanic, Config
    from sanic.request import Headers

    def options(**kwargs):
        for key, value in kwargs.items():
            if value is not None:
                yield key, value

    app = Sanic()
    config = Config(app)
    config.REAL_IP_HEADER = "x-real-ip"
    config.PROXIES_COUNT = 2
    # Test with real_ip_header
    headers = Headers([("x-real-ip", "192.168.0.1:80")])
    assert parse_xforwarded(headers, config) == dict(
        for_="192.168.0.1", port=80
    )
    # Test with real_ip_header and forwarded_protocol

# Generated at 2022-06-14 07:14:12.689872
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    # Test forwarded-for
    headers = {
        'x-real-ip': '127.0.0.1',
        'x-forwarded-for': '127.0.0.2, 127.0.0.1; by=192.168.0.1'
    }
    config = {
        'REAL_IP_HEADER': 'x-real-ip',
        'FORWARDED_FOR_HEADER': 'x-forwarded-for',
    }
    options = parse_xforwarded(headers, config)
    assert options == {'for': '127.0.0.2'}

    # Test x-scheme

# Generated at 2022-06-14 07:14:26.153732
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    from sanic.server import FakeSocket

    r = FakeSocket("GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")
    assert parse_xforwarded(r.headers, r.server.config) == None

    r = FakeSocket("GET / HTTP/1.1\r\nHost: example.com\r\nX-Forwarded-For: 1.1.1.1\r\n\r\n")
    assert parse_xforwarded(r.headers, r.server.config) == {'for': "1.1.1.1"}


# Generated at 2022-06-14 07:14:31.920428
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {
        'x-scheme': 'http',
        'x-forwarded-proto': 'http',
        'x-forwarded-host': 'localhost:8000',
        'x-forwarded-port': '8000',
        'x-forwarded-path': '/'
    }
    expected = {
        'for': 'localhost:8000',
        'proto': 'http',
        'host': 'localhost:8000',
        'port': 8000,
        'path': '/'
    }
    assert parse_xforwarded(headers, {}) == expected

# Generated at 2022-06-14 07:14:44.010245
# Unit test for function fwd_normalize
def test_fwd_normalize():

    #test fwd_normalize_address
    assert fwd_normalize_address("192.168.0.1") == "192.168.0.1"
    assert fwd_normalize_address("192.168.0.1:443") == "192.168.0.1:443"
    assert fwd_normalize_address("_192.168.0.1") == "_192.168.0.1"
    
    #test fwd_normalize
    assert fwd_normalize([("key", "192.168.0.1")]) == {"key": "192.168.0.1"}
    assert fwd_normalize([("key", "192.168.0.1:443")]) == {"key": "192.168.0.1:443"}

# Generated at 2022-06-14 07:14:57.992932
# Unit test for function fwd_normalize
def test_fwd_normalize():
    assert fwd_normalize({"by": "127.0.0.1", "proto": "http", "host": "localhost"}) == {"by": "127.0.0.1", "proto": "http", "host": "localhost"}
    assert fwd_normalize({"by": "::1", "proto": "http", "host": "localhost"}) == {"by": "[::1]", "proto": "http", "host": "localhost"}

test_fwd_normalize()

# Generated at 2022-06-14 07:15:04.393205
# Unit test for function parse_forwarded
def test_parse_forwarded():
    # Test
    options = parse_forwarded({
        "Forwarded": [
            "host=abcde:14, for=192.168.1.1;proto=https, by=192.168.1.1:81, secret=\"12345\", for=127.0.0.1, for=\"[2001:db8:a0b:12f0::1]\""
        ]
    },
                              config=None)
    # Verify
    assert(options == {
        'host': 'abcde:14', 
        'for': '127.0.0.1', 
        'proto': 'https', 
        'by': '192.168.1.1:81', 
        'secret': '12345'
    })

# Generated at 2022-06-14 07:15:14.024666
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {
        "x-forwarded-host": "192.168.2.1:5000, 192.168.2.3:5000",
        "x-forwarded-scheme": "https, http",
        "x-forwarded-proto": "https, http",
        "x-forwarded-path": "%2Fschedule%2Ftest",
    }
    config = {
        "REAL_IP_HEADER": None,
        "PROXIES_COUNT": 3,
        "FORWARDED_FOR_HEADER": "x-forwarded-host",
    }

# Generated at 2022-06-14 07:15:18.026094
# Unit test for function parse_forwarded
def test_parse_forwarded():
    headers = {'forwarded':'secret=a; by=b, secret=a; by=b'}
    config = MagicMock()
    config.FORWARDED_SECRET = 'a'
    assert parse_forwarded(headers, config)[0][1] == 'b'


# Generated at 2022-06-14 07:15:31.428554
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    config = FakeConfig()
    config.REAL_IP_HEADER = "X-Real-Ip"
    config.FORWARDED_FOR_HEADER = "X-Forwarded-For"
    config.PROXIES_COUNT = 1
    _headers = {"X-Real-Ip" : "192.168.1.1"}
    assert parse_xforwarded(_headers, config) == {"for":"192.168.1.1"}
    _headers = {"X-Forwarded-For" : "192.168.0.1, 192.168.0.2, 192.168.0.3"}
    assert parse_xforwarded(_headers, config) == {"for":"192.168.0.3"}
    _headers = {}
    assert parse_xforwarded(_headers, config) == None
    config.PROXIES

# Generated at 2022-06-14 07:15:38.685645
# Unit test for function fwd_normalize
def test_fwd_normalize():
    fwd_normalize([])
    fwd_normalize([("foo", "bar")])
    fwd_normalize([("foo", "bar"), ("for", "127.0.0.1")])
    assert (
        fwd_normalize([("foo", "bar"), ("for", "127.0.0.1")]) == {"for": "127.0.0.1"}
    )
    assert fwd_normalize([("foo", "bar"), ("for", "127.0.0.1")])["for"] == "127.0.0.1"
    assert fwd_normalize([("foo", "bar"), ("for", "127.0.0.1")])["for"] == "127.0.0.1"

# Generated at 2022-06-14 07:15:51.706594
# Unit test for function parse_content_header
def test_parse_content_header():
    import pytest

    def test_header(h, expect):
        ret = parse_content_header(h)
        assert ret == expect, (h, ret)

    test_header("", ("", {}))
    test_header(";", ("", {}))
    test_header(";name=value", ("", {"name": "value"}))
    test_header(";name=", ("", {"name": ""}))
    test_header("; name=value", ("", {"name": "value"}))
    test_header("; name=value;", ("", {"name": "value"}))
    test_header(";name=value;", ("", {"name": "value"}))
    test_header(";name=\"value\"", ("", {"name": "value"}))

# Generated at 2022-06-14 07:16:06.166076
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {'X-Forwarded-For': '127.0.0.1'}
    config = {}
    config['REAL_IP_HEADER'] = None
    config['PROXIES_COUNT'] = 2
    config['FORWARDED_FOR_HEADER'] = 'X-Forwarded-For'
    ret = parse_xforwarded(headers, config)
    assert ret['for'] == '127.0.0.1'
    
    headers = {'X-Forwarded-For': '127.0.0.1'}
    config = {}
    config['REAL_IP_HEADER'] = None
    config['PROXIES_COUNT'] = None
    config['FORWARDED_FOR_HEADER'] = 'X-Forwarded-For'

# Generated at 2022-06-14 07:16:17.391024
# Unit test for function parse_xforwarded

# Generated at 2022-06-14 07:16:30.263830
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    example_header = {
        "x-forwarded-host": "example.com",
        "x-forwarded-for": "192.192.192.192",
        "x-scheme":"foo",
        "x-forwarded-path": "bar",
        "x-forwarded-port": "8080",
    }
    config = {
        "PROXIES_COUNT": 0,
        "REAL_IP_HEADER": "x-forwarded-for",
        "FORWARDED_FOR_HEADER": "x-forwarded-for",
    }

# Generated at 2022-06-14 07:16:48.472120
# Unit test for function parse_forwarded
def test_parse_forwarded():
    """Test parse_forwarded function."""

    # Setup
    import json
    import requests
    import multipart
    from sanic import Sanic
    from sanic.request import RequestParameters
    from sanic.response import HTTPResponse
    from sanic.config import Config
    from sanic.exceptions import InvalidUsage
    from werkzeug.datastructures import Headers

    config = Config()
    config.FORWARDED_SECRET = "_foobar_"

    app = Sanic("test_parse_forwarded")

    def client_parse_forwarded(**options):
        """Test send request with parse_forwarded function."""
        body = json.dumps(options)
        headers = {"content-type": "application/json"}
        url = "http://test.test/test_parse_forwarded"

# Generated at 2022-06-14 07:16:58.843844
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    header = {'x-scheme':'https', 'x-forwarded-host':'*', \
              'x-forwarded-for':'192.168.1.1', 'x-forwarded-path':'/api'}
    config = {'PROXIES_COUNT': 2, 'REAL_IP_HEADER': 'x-forwarded-for', \
              'FORWARDED_FOR_HEADER': 'x-forwarded-for', \
              'FORWARDED_SECRET': None}
    result = {'for': '192.168.1.1', 'proto': 'https', 'host': '*', \
              'path': '/api'}
    assert parse_xforwarded(header, config) == result

if __name__ == '__main__':
    test_parse_xforwarded()

# Generated at 2022-06-14 07:17:12.267942
# Unit test for function parse_forwarded
def test_parse_forwarded():
    import copy
    def parse_check(key:str, val:str):
        print("%s %s" % (key, val))
        return key, val

# Generated at 2022-06-14 07:17:25.557668
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    from sanic import Sanic
    sanicapp = Sanic('Sanic')
    sanicapp.config.PROXIES_COUNT = 2
    sanicapp.config.REAL_IP_HEADER = 'X-Forwarded-For'
    sanicapp.config.FORWARDED_FOR_HEADER = 'X-Forwarded-For'
    test_headers={
        "X-Forwarded-For": "192.168.0.177, 192.168.0.1",
        "X-Forwarded-Host": "mydomain.com",
        "X-Forwarded-Path": "%2Fmypath",
        "X-Forwarded-Proto": "https",
        "X-Scheme": "http",
        "X-Forwarded-Port": "80"
    }

# Generated at 2022-06-14 07:17:32.376319
# Unit test for function parse_forwarded
def test_parse_forwarded():
    config = Mock()
    config.FORWARDED_SECRET = "secret"

    def t(headers, expected):
        assert parse_forwarded(headers, config) == expected

    t(
        {"Forwarded": "for=12.34.56.78,secret=secret"},
        {"for": "12.34.56.78", "secret": "secret"},
    )

    t(
        {"Forwarded": "for=12.34.56.78;by=0123456789"},
        {"for": "12.34.56.78", "by": "0123456789"},
    )


# Generated at 2022-06-14 07:17:39.135738
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {
        'x-forwarded-for': '1',
        'x-forwarded-port': '2',
        'x-forwarded-proto': '3',
        'x-forwarded-host': '4',
    }
    print(parse_xforwarded(headers, config = 0))

if __name__ == '__main__':
    test_parse_xforwarded()

# Generated at 2022-06-14 07:17:47.643508
# Unit test for function parse_forwarded
def test_parse_forwarded():
    from collections import namedtuple
    from sanic import Sanic
    from sanic.request import Request

    headers= {'Forwarded': 'for=123.123.123.123;by=mysecret;proto=http;host=foo.com;port=3000;path=/'}
    config = namedtuple('Config', ['PROXIES_COUNT' , 'FORWARDED_SECRET', 'FORWARDED_FOR_HEADER', 'REAL_IP_HEADER'])(3, 'mysecret', 'Forwarded', None)
    app = Sanic('test_app')
    
    assert parse_forwarded(headers, config) == {'for': '123.123.123.123', 'by': 'mysecret', 'proto': 'http', 'host': 'foo.com', 'port': 3000, 'path': '/'}

# Generated at 2022-06-14 07:17:53.250522
# Unit test for function parse_forwarded
def test_parse_forwarded():
    headers = {
        "Forwarded": [
            "for=\"[2001:db8:cafe::17]:4711\";proto=https;by=203.0.113.43",
            "for=192.0.2.60;proto=http;by=203.0.113.43",
        ]
    }
    config = type("Config", (), {"FORWARDED_SECRET": "secret"})
    assert (
        parse_forwarded(headers, config)
        == {
            "for": "2001:db8:cafe::17:4711",
            "proto": "https",
            "by": "203.0.113.43",
        }
    )



# Generated at 2022-06-14 07:18:02.550308
# Unit test for function parse_forwarded
def test_parse_forwarded():
    from sanic.config import Config
    c=Config()
    c.FORWARDED_SECRET = "abc"
    a={"Forwarded": ['for=192.0.2.43; proto=https; host=example.com', 'for=_hidden; proto=https; host=example.com', 'for=192.0.2.43; proto=https; host=example.com', 'for=192.0.2.43; proto=https; host=example.com', 'for=192.0.2.43; proto=https; host=example.com']}
    print(parse_forwarded(a,c))

if __name__ == '__main__':
    test_parse_forwarded()

# Generated at 2022-06-14 07:18:06.973508
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    from sanic.request import Request
    from .response import HTTPResponse
    from .server import HttpProtocol

    http_proto = HttpProtocol()

    request_headers = [
        (b"GET", b"/test HTTP/1.1"),
        (b"Host", b"localhost:8000"),
        (b"Connection", b"close"),
        (b"Accept", b"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"),
        (b"Accept-Encoding", b"gzip"),
        (b"Accept-Language", b"en-us"),
        (b"Content-Length", b"0"),
        (b"X-Request-Start", b"1518299082284")
    ]

    request_headers

# Generated at 2022-06-14 07:18:29.317363
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {'X-Forwarded-For': '10.2.2.1, 192.168.1.1'}
    config = {'PROXIES_COUNT': 1, 'REAL_IP_HEADER': 'X-Forwarded-For'}
    print(parse_xforwarded(headers, config))



# Generated at 2022-06-14 07:18:37.063251
# Unit test for function parse_forwarded
def test_parse_forwarded():
    import os


# Generated at 2022-06-14 07:18:50.291157
# Unit test for function parse_forwarded
def test_parse_forwarded():
    from sanic import Sanic
    from sanic.config import Config
    from sanic.request import RequestParameters

    app = Sanic("test")
    config = Config()
    config.FORWARDED_SECRET = "mysecret"


# Generated at 2022-06-14 07:19:03.549398
# Unit test for function parse_forwarded
def test_parse_forwarded():
    assert parse_forwarded({'Forwarded': ['"secret=abcdef;"']}, None) == {'secret': 'abcdef'}
    assert parse_forwarded({'Forwarded': ['"secret=abcdef"']}, None) == {'secret': 'abcdef'}
    assert parse_forwarded({'Forwarded': ['"by=secret;secret=abcdef;"']}, None) == {'by': 'secret', 'secret': 'abcdef'}
    assert parse_forwarded({'Forwarded': ['"by=secret;secret=abcdef"']}, None) == {'by': 'secret', 'secret': 'abcdef'}
    assert parse_forwarded({'Forwarded': ['"by=secret;secret=abcdef;for=192.0.2.60;proto=http;host=example.com"']}, None)

# Generated at 2022-06-14 07:19:08.983051
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {
        'X-Forwarded-Host': 'localhost:5000',
        'X-Forwarded-Path': '/path',
        'X-Forwarded-Proto': 'http'
    }
    config = {
        'FORWARDED_FOR_HEADER': 'X-Forwarded-For',
        'PROXIES_COUNT': 1
    }
    results = parse_xforwarded(headers, config)

    assert results == {
        'for': 'localhost',
        'proto': 'http',
        'host': 'localhost:5000',
        'path': '/path'
    }

# Generated at 2022-06-14 07:19:18.525419
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {"x-forwarded-Host": "test.com", "x-scheme": "https", "x-forwarded-path": "/test"}
    xforwarded = parse_xforwarded(headers, {"FORWARDED_FOR_HEADER": "x-forwarded-for", "PROXIES_COUNT": 1, "REAL_IP_HEADER": None})
    assert xforwarded['path'] == "/test"
    assert xforwarded['host'] == "test.com"
    assert xforwarded['proto'] == "https"

# Generated at 2022-06-14 07:19:26.165811
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {"X-Forwarded-For": "diego"}
    config = {
        "PROXIES_COUNT": 1,
        "FORWARDED_FOR_HEADER": "X-Forwarded-For",
        "REAL_IP_HEADER": "X-Real-Ip"
    }
    test = parse_xforwarded(headers, config)
    assert test == {"for": "diego"}


if __name__ == "__main__":
    test_parse_xforwarded()

# Generated at 2022-06-14 07:19:34.665519
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {"real_ip_header": "ip", "PROXIES_COUNT": 2, 
                "FORWARDED_FOR_HEADER": 'Forwarded-For'}
    addr = "dummy_addr"

    def mock_get(header):
        if header == "ip":
            return addr
        elif header == "Forwarded-For":
            return "dummy_addr1, dummy_addr2, dummy_addr3"

    assert parse_xforwarded(mock_get, headers) == {'for': 'dummy_addr', 'proto': None, 'host': None, 'port': None, 'path': None}

# Generated at 2022-06-14 07:19:43.717735
# Unit test for function parse_forwarded
def test_parse_forwarded():
    config = {'PROXIES_COUNT': 2, 'FORWARDED_FOR_HEADER': 'x-forwarded-for', 'REAL_IP_HEADER': 'x-real-ip', 'FORWARDED_SECRET': 'my_secret'}
    headers = {'x-forwarded-for': '10.0.0.1, 192.168.0.1', 'x-real-ip': '127.0.0.1'}
    ret_val = parse_forwarded(headers, config)
    print (ret_val)
    
if __name__ == '__main__':
    test_parse_forwarded()

# Generated at 2022-06-14 07:19:56.905472
# Unit test for function parse_forwarded
def test_parse_forwarded():
    from sanic import Sanic, SanicConfig
    from sanic.websocket import WebSocketProtocol
    app = Sanic(
        __name__,
        load_env=False,
        server_settings=(WebSocketProtocol,),
        config_override=SanicConfig,
    )
    app.FORWARDED_FOR_HEADER = 'X-Forwarded-For'
    app.FORWARDED_SECRET = 'secret'
    app.REAL_IP_HEADER = 'X-Real-IP'
    app.PROXIES_COUNT = 0

    # test whether the parse_forwarded works
    headers = {'X-Forwarded-For': '1.1.1.1', 'Forwarded': 'for=1.1.1.1; secret=a_secret'}

# Generated at 2022-06-14 07:21:12.609282
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {
        "X-Forwarded-Host": "host.com",
        "X-Forwarded-Port": "88",
        "X-Forwarded-Path": "/path",
        "X-Forwarded-Proto": "wss",
        "Real-Ip": "ip"
    }

    options = parse_xforwarded(headers, "")

    assert options["host"] == "host.com"
    assert options["port"] == 88
    assert options["path"] == "/path"
    assert options["for"] == "ip"
    assert options["proto"] == "wss"