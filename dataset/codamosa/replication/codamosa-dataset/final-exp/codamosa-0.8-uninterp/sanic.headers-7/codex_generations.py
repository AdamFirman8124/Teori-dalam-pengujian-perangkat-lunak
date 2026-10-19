

# Generated at 2022-06-14 07:11:18.972024
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {"x-forwarded-for":"192.168.0.1, 127.0.0.1"}
    config = type("", (), {"PROXIES_COUNT": 0, "FORWARDED_FOR_HEADER": "x-forwarded-for", "REAL_IP_HEADER": "x-forwarded-for"})
    assert parse_xforwarded(headers, config) == {'for': '192.168.0.1'}

# Generated at 2022-06-14 07:11:29.768784
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {'x-forwarded-host':"localhost:8443", 'x-forwarded-proto':"https", 
               'x-forwarded-path':"/test", 'x-forwarded-port':"8443"}
    config = pipeye.pipeline_config.PipelineConfig()
    config.REAL_IP_HEADER = None
    config.PROXIES_COUNT = 0
    config.FORWARDED_FOR_HEADER = None
    result = parse_xforwarded(headers, config)
    assert result == {'host':'localhost:8443', 'proto':'https', 'path':'/test', 'port':8443}


# Generated at 2022-06-14 07:11:41.421699
# Unit test for function parse_forwarded
def test_parse_forwarded():
    assert not parse_forwarded({"Forwarded": "A"}, None)
    assert not parse_forwarded({"Forwarded": "by=userA"}, None)
    assert not parse_forwarded({"Forwarded": "by=userA;by=userB"}, None)
    assert not parse_forwarded({"Forwarded": "by=userA;by=userB;host=host:80"}, None)
    assert parse_forwarded({"Forwarded": "by=userA;host=host:80"}, None) == {'host': 'host', 'by': 'userA'}
    assert parse_forwarded({"Forwarded": "by=userA;host=host:80;"}, None) == {'host': 'host', 'by': 'userA'}

# Generated at 2022-06-14 07:11:54.300299
# Unit test for function parse_forwarded
def test_parse_forwarded():
    from sanic.config import Config
    class MyConfig(Config):
        FORWARDED_SECRET = "testsecret"
    config = MyConfig()

# Generated at 2022-06-14 07:12:07.809267
# Unit test for function parse_forwarded
def test_parse_forwarded():
    # Params with and without quotes
    result = parse_forwarded({"forwarded": "for=127.0.0.1; by=\"[::1]\""}, {"FORWARDED_SECRET": "test"})
    assert result == {"for": "[127.0.0.1]", "by": "[::1]"}

    result = parse_forwarded({"forwarded": "for=127.0.0.1; by=::1"}, {"FORWARDED_SECRET": "test"})
    assert result == {"for": "[127.0.0.1]", "by": "[::1]"}

    result = parse_forwarded({"forwarded": "for=127.0.0.1; by=\"[::1]\""}, {"FORWARDED_SECRET": "wrong"})
    assert result is None


# Generated at 2022-06-14 07:12:21.877811
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    raw_headers = [
        'Host: localhost:80',
        'User-Agent: curl/7.54.0',
        'Accept: */*',
        'X-Forwarded-Proto: https',
        'X-Forwarded-Path: /',
        'X-Real-Ip: 81.4.0.1',
        'Forwarded: for=81.4.0.1',
        'X-Forwarded-For: 81.4.0.1, 10.0.0.1',
        'X-Forwarded-Port: 80',
        'Connection: close'
    ]

# Generated at 2022-06-14 07:12:35.108966
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {
        "X-Forwarded-For": "10.0.0.1,192.168.1.1",
        "X-Forwarded-Host": "example.org",
        "X-Forwarded-Port": "1234",
        "X-Forwarded-Path": "/test",
    }
    config = MagicMock()  # type: Any
    config.FORWARDED_SECRET = None
    config.REAL_IP_HEADER = None
    config.PROXIES_COUNT = 10
    config.FORWARDED_FOR_HEADER = "X-Forwarded-For"

    options = parse_xforwarded(headers, config)

# Generated at 2022-06-14 07:12:38.048801
# Unit test for function parse_content_header
def test_parse_content_header():
    value = r'application/json; charset="utf8"'
    parse_content_header(value)
    assert True
    pass

# Generated at 2022-06-14 07:12:45.382590
# Unit test for function parse_forwarded
def test_parse_forwarded():
    data = {
        "secret": "123123123",
        "by": "127.0.0.1",
        "for": "127.0.0.1",
        "proto": "http",
        "host": "127.0.0.1",
        "port": "80",
    }

    # Test case 1
    request_headers = {
        "Forwarded": "by=127.0.0.1;secret=123123123;for=127.0.0.1;proto=http;host=127.0.0.1;port=80",
    }
    ret = parse_forwarded(request_headers, config=None)
    assert ret == data

    # Test case 2

# Generated at 2022-06-14 07:12:56.788862
# Unit test for function fwd_normalize_address
def test_fwd_normalize_address():
    # Check if IPV6 addresses are normalized properly
    assert fwd_normalize_address("fe80::1%lo0") == "[fe80::1%lo0]"
    assert fwd_normalize_address("FE80::1%LO0") == "[fe80::1%lo0]"
    assert fwd_normalize_address("Ff80:0000:0:0:0:0:0:0001%LO0") == "[ff80::1%lo0]"
    # Check if IPv4 addresses are normalized properly
    assert fwd_normalize_address("10.0.0.1") == "10.0.0.1"
    assert fwd_normalize_address("10.0.0.11") == "10.0.0.11"

# Generated at 2022-06-14 07:13:12.723068
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    from sanic.testing import HttpProtocol

    HttpProtocol.parse_xforwarded(None, None)

# Generated at 2022-06-14 07:13:25.921205
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    from sanic.response import HTTPResponse
    import io
    import asyncio
    from sanic.request import RequestParameters

    class MockRequest:
        def __init__(self, headers: dict, port: int = 8000, app = None):
            self.headers = headers
            self.port = port
            self.ip = "127.0.0.1"
            self.path = "/"
            self.query_string = ""
            self.app = app
            self.raw_path = "/"
            self.args = RequestParameters()
            self.url = "http://127.0.0.1:8000/"
            self.host = "127.0.0.1"
            self.method = "GET"
            self.content = None  # TODO: fill out
            self.stream = None
            self

# Generated at 2022-06-14 07:13:35.199204
# Unit test for function parse_content_header
def test_parse_content_header():
    value = 'form-data; name=upload; filename=\"file.txt\"'
    expected_value = ('form-data', {'name': 'upload', 'filename': 'file.txt'})
    assert parse_content_header(value) == expected_value

    # value = 'form-data; name=upload; filename="file.txt"'
    # expected_value = ('form-data', {'name': 'upload', 'filename': 'file.txt'})
    # assert parse_content_header(value) == expected_value



# Generated at 2022-06-14 07:13:41.493038
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    _headers = {'x-forwarded-for': '10.0.0.0, 10.0.0.1, 10.0.0.2' }
    _parsed_headers = parse_xforwarded(_headers, 2)
    assert _parsed_headers['for'] == '10.0.0.2'

# Generated at 2022-06-14 07:13:54.690965
# Unit test for function parse_forwarded
def test_parse_forwarded():
    assert parse_forwarded("By=127.0.0.1;Secret=xx;For=myip", "xx") == {'by': '127.0.0.1', 'for': 'myip'}
    assert parse_forwarded("By=127.0.0.1;Secret=xx;For=_0;", "xx") == {'by': '127.0.0.1', 'for': '_0'}
    assert parse_forwarded("By=127.0.0.1;Secret=xx;For=_0;For=myip", "xx") == {'by': '127.0.0.1', 'for': 'myip'}

# Generated at 2022-06-14 07:14:02.658071
# Unit test for function parse_content_header
def test_parse_content_header():
    value = 'form-data; name="upload"; filename="file.txt"; \
    filename*="file%20%2F%20txt.txt"'
    assert parse_content_header(value) == (
        'form-data',
        {
            'name': 'upload',
            'filename': 'file.txt',
            'filename*': 'file%20%2F%20txt.txt'
        }
    )

# Generated at 2022-06-14 07:14:09.416265
# Unit test for function parse_host
def test_parse_host():
    # default port
    assert parse_host("example.com") == ("example.com", None)
    # valid address:port
    assert parse_host("example.com:8080") == ("example.com", 8080)
    # invalid port
    assert parse_host("example.com:999999") == ("example.com", None)
    # IPv4 address
    assert parse_host("255.255.255.255:8080") == ("255.255.255.255", 8080)
    # IPv6 address (depends on system)
    assert parse_host("[::1]") == ("[::1]", None)
    assert parse_host("[::1]:8080") == ("[::1]", 8080)
    # brackets in host name

# Generated at 2022-06-14 07:14:22.269787
# Unit test for function parse_forwarded
def test_parse_forwarded():
    headers = {
        'Forwarded': 'for=192.0.2.60; proto=http; by=203.0.113.43'
    }
    config = {
        'FORWARDED_SECRET': '',
    }
    assert parse_forwarded(headers, config) == {
        'for': '192.0.2.60',
        'proto': 'http',
        'by': '203.0.113.43'
    }

    config = {
        'FORWARDED_SECRET': 's3cr3t',
    }
    assert parse_forwarded(headers, config) is None

    headers = {
        'Forwarded': ['for=192.0.2.43, for=198.51.100.17']
    }

# Generated at 2022-06-14 07:14:36.090469
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    request_headers = {}
    request_headers["x-forwarded-for"] = "127.0.0.1"
    request_headers["x-scheme"] = "https"
    request_headers["x-forwarded-proto"] = "https"
    request_headers["x-forwarded-host"] = "127.0.0.1"
    request_headers["x-forwarded-port"] = "443"
    request_headers["x-forwarded-path"] = "/test"

    forwarded_for_option = request_headers["x-forwarded-for"]
    scheme_option = request_headers["x-scheme"]
    proto_option = request_headers["x-forwarded-proto"]
    host_option = request_headers["x-forwarded-host"]

# Generated at 2022-06-14 07:14:45.905736
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {
        'X-Forwarded-For': 'this,that,192.168.1.2',
        'X-Forwarded-Host': 'some-site.com',
        'X-Forwarded-Proto': 'https',
        'X-Forwarded-Port': '443',
        'X-Forwarded-Path': '/some_path',
        'X-Real-Ip': '192.168.1.3',
    }
    expected_result = {
        'for': '192.168.1.2',
        'host': 'some-site.com',
        'proto': 'https',
        'port': 443,
        'path': '/some_path',
    }

# Generated at 2022-06-14 07:14:57.868160
# Unit test for function parse_forwarded
def test_parse_forwarded():
    """
    content = 'IP=192.168.1.1, By=host.domain.com, For=192.168.1.100, For=198.51.100.17'
    headers = CaseInsensitiveDict()
    headers['Forwarded'] = content;
    config = Config()
    config.FORWARDED_SECRET = 'host.domain.com'
    parsed = parse_forwarded(headers,config)
    assert(parsed)
    """
    print("test")


if __name__ == "__main__":
    test_parse_forwarded()

# Generated at 2022-06-14 07:15:11.981489
# Unit test for function parse_forwarded
def test_parse_forwarded():
    headers = {'Forwarded': ''}
    config = {'FORWARDED_SECRET': ''}
    assert parse_forwarded(headers, config) == {}

    headers = {'Forwarded': 'for=127.0.0.1'}
    config = {'FORWARDED_SECRET': ''}
    assert parse_forwarded(headers, config) == {'for': '127.0.0.1'}

    headers = {'Forwarded': 'For=127.0.0.1'}
    config = {'FORWARDED_SECRET': ''}
    assert parse_forwarded(headers, config) == {'for': '127.0.0.1'}

    headers = {'Forwarded': 'for=127.0.0.1, for=127.0.0.2'}
    config

# Generated at 2022-06-14 07:15:19.512450
# Unit test for function parse_forwarded
def test_parse_forwarded():
    headers = {'forwarded':
        ['for=192.0.2.60;proto=http;by=203.0.113.43,for=192.0.2.60,for=192.0.2.60;by=203.0.113.43,for=192.0.2.60;by=203.0.113.43']
    }
    config = {'FORWARDED_SECRET':'secret'}

    options = parse_forwarded(headers, config)
    assert options == {'for': '192.0.2.60', 'by': 'secret'}

# Generated at 2022-06-14 07:15:33.348523
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    from sanic.response import json
    from sanic import Sanic
    from sanic_session import Session, InMemorySessionInterface

    app = Sanic(__name__)
    session = Session(app, interface=InMemorySessionInterface())

    @app.middleware("request")
    async def add_session_to_request(request):
        await session.open(request)

    @app.middleware("response")
    async def add_header(request, response):
        response.headers['new_header'] = 'header_value'

    @app.route("/")
    async def test(request):
        return json(request.headers)


# Generated at 2022-06-14 07:15:47.519406
# Unit test for function parse_forwarded

# Generated at 2022-06-14 07:15:56.285293
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    # Make the function workable in testing environment
    from sanic import Sanic
    from sanic.config import Config
    app = Sanic("TestApp")
    app.config = Config()
    app.config.FORWARDED_FOR_HEADER = ""

    class TmpRequest:
        headers = {}

    req = TmpRequest()
    req.headers = {"x-forwarded-for": "10.0.2.2"}
    assert parse_xforwarded(req.headers, app.config) == {"for": "10.0.2.2"}

    req.headers = {"x-forwarded-for": "10.0.2.2, 10.0.3.3"}
    assert parse_xforwarded(req.headers, app.config) == {"for": "10.0.3.3"}


# Generated at 2022-06-14 07:16:08.694744
# Unit test for function parse_forwarded
def test_parse_forwarded():
    assert parse_forwarded(["proto=http", "by=9.8.7.6", "secret=my-secret"], {}) == {'proto': 'http', 'by': '9.8.7.6'}
    assert parse_forwarded(['proto=http', 'by=9.8.7.6'], {}) is None
    assert parse_forwarded(["proto=http", "by=9.8.7.6", "secret=9.8.7.6"], {}) is None
    assert parse_forwarded(["by=9.8.7.6;secret=my-secret"], {}) is None
    assert parse_forwarded([";by=9.8.7.6;secret=my-secret;"], {}) == {'by': '9.8.7.6'}



# Generated at 2022-06-14 07:16:21.938584
# Unit test for function parse_forwarded

# Generated at 2022-06-14 07:16:29.718172
# Unit test for function parse_forwarded

# Generated at 2022-06-14 07:16:39.629924
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    from sanic.exceptions import InvalidUsage
    from sanic import Sanic
    sanic = Sanic(__name__)
    sanic.config.FORWARDED_FOR_HEADER = "x-forwarded-for"
    sanic.config.REAL_IP_HEADER = "x-real-ip"

    class DummyRequest:
        def __init__(self):
            self.headers = {}

    request = DummyRequest()

    request.headers = {"x-forwarded-for": "1.1.1.1", "x-real-ip": "2.2.2.2", "x-scheme": "http", "x-forwarded-host": "127.0.0.1", "x-forwarded-port": "443", "x-forwarded-path": "/somepath"}
    assert parse

# Generated at 2022-06-14 07:17:20.042541
# Unit test for function parse_forwarded
def test_parse_forwarded():
    env, config = {}, type("", (), {})()
    config.FORWARDED_SECRET = "secret"

    def test(h, fwd=None):
        env["headers"] = [("Forwarded", h)]
        assert parse_forwarded(env, config) == fwd

    test(r"for=\"[::1]:59880\";host=example.com;proto=https", {
        "for": "[::1]:59880",
        "proto": "https",
        "host": "example.com",
    })

# Generated at 2022-06-14 07:17:30.290511
# Unit test for function parse_forwarded
def test_parse_forwarded():
    headers = {
        "Forwarded": "by=_secret;for=1.2.3.4;proto=https,for=_secret;proto=http;for=_secret",
        "X-Forwarded-Host": "127.0.0.1",
        "X-Forwarded-Proto": "http",
        "X-Forwarded-Port": "80",
        "X-Forwarded-Path": "/test",
    }
    options = parse_forwarded(headers)
    assert options["for"] == "1.2.3.4"
    assert options["secret"] == "_secret"
    assert options["proto"] == "https"
    assert options["host"] == "127.0.0.1"
    assert options["port"] == 80
    assert options["path"] == "/test"



# Generated at 2022-06-14 07:17:38.281505
# Unit test for function fwd_normalize

# Generated at 2022-06-14 07:17:47.306671
# Unit test for function fwd_normalize
def test_fwd_normalize():
    assert fwd_normalize([("by","1.1.1.1")]) == {"by": "1.1.1.1"}
    assert fwd_normalize([("for","1.1.1.1")]) == {"for": "1.1.1.1"}
    assert fwd_normalize([("by","1.1.1.1"),("for","2.2.2.2")]) == {"by": "1.1.1.1", "for": "2.2.2.2"}
    assert fwd_normalize([("by","1.1.1.1"),("for","2.2.2.2"),("proto","tcp")]) == {"by": "1.1.1.1", "for": "2.2.2.2", "proto": "tcp"}

# Generated at 2022-06-14 07:18:00.465451
# Unit test for function parse_forwarded
def test_parse_forwarded():
    """Test unit for function parse_forwarded"""
    from chilero.web.config import Config
    config = Config(FORWARDED_SECRET='foobar')

    assert(parse_forwarded({'forwarded': 'for=1.2.3.4'}, config) == {'for': '1.2.3.4'})
    assert(parse_forwarded({'forwarded': 'for=1.2.3.4, by=_wibble'}, config) == {'for': '1.2.3.4', 'by': '_wibble'})

# Generated at 2022-06-14 07:18:03.453705
# Unit test for function parse_forwarded
def test_parse_forwarded():
    print(parse_forwarded({'Forwarded': 'for=192.0.2.43, for="[2001:db8:cafe::17]"'}, None))

# Generated at 2022-06-14 07:18:10.710474
# Unit test for function parse_forwarded
def test_parse_forwarded():
    from sanic import Sanic
    app = Sanic(__name__)
    app.config.FORWARDED_SECRET = 'asdf'

# Generated at 2022-06-14 07:18:20.914668
# Unit test for function parse_forwarded

# Generated at 2022-06-14 07:18:30.132721
# Unit test for function parse_forwarded
def test_parse_forwarded():
    headers = {'Forwarded': ['for=120.0.0.1;proto=http;by=[::]','for=120.0.0.2;proto=https;by=[::]','for=120.0.0.3;proto=https;by=[::]','for=120.0.0.4;proto=https;by=[::]','for=120.0.0.5;proto=https;by=[::]','for=120.0.0.6;proto=https;by=[::]','for=120.0.0.7;proto=https;by=[::]','for=120.0.0.8;proto=https;by=[::]']}

    real_ip_header = 'X-Forwarded-For'
    proxies_count = 1
    addr = real_

# Generated at 2022-06-14 07:18:37.348858
# Unit test for function parse_forwarded

# Generated at 2022-06-14 07:18:52.629581
# Unit test for function fwd_normalize_address
def test_fwd_normalize_address():
    fwd_normalize_address('127.0.0.1')
    fwd_normalize_address('REVERSE PROXY A')
    fwd_normalize_address('UNKNOWN')

# Generated at 2022-06-14 07:18:57.098621
# Unit test for function parse_forwarded
def test_parse_forwarded():
    assert parse_forwarded({"forwarded": ["for=10.0.0.1; by=secret; host=localhost"]}, "secret") == {'for': '10.0.0.1', 'by': 'secret', 'host': 'localhost'}


# Generated at 2022-06-14 07:19:06.493979
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {"X-Real-IP": "1.2.3.4", "X-Forwarded-Host": "testhost"}
    c = type("", (), {})()
    c.REAL_IP_HEADER = "X-Real-IP"
    c.FORWARDED_FOR_HEADER = "X-Forwarded-For"
    c.PROXIES_COUNT = 0
    options = parse_xforwarded(headers, c)
    assert options["for"] == "1.2.3.4"
    assert options["host"] == "testhost"
    assert options["path"] is None
    assert options["proto"] is None
    assert options["port"] is None

# Generated at 2022-06-14 07:19:20.789543
# Unit test for function parse_forwarded
def test_parse_forwarded():
    import pytest
    # General test case
    # We want to test that basic RFC 7239 forwarding works as expected.

# Generated at 2022-06-14 07:19:32.442054
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    assert None == parse_xforwarded(None, None)
    assert None == parse_xforwarded([], None)
    assert None == parse_xforwarded({}, None)
    assert None == parse_xforwarded(["asdf"], None)
    assert None == parse_xforwarded({"asdf": "xxx"}, None)
    assert None == parse_xforwarded({"x-forwarded-for": ""}, None)
    assert None == parse_xforwarded({"x-forwarded-for": " "}, None)


# Generated at 2022-06-14 07:19:45.532076
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {
        "real-ip": "123.123.123.123",
        "x-scheme": "https",
        "x-forwarded-host": "test",
        "x-forwarded-port": "1234",
        "x-forwarded-path": "/test"
    }

    # Case with real-ip header set
    result = parse_xforwarded(headers, None)
    assert result["for"] == "123.123.123.123"
    assert result["proto"] == "https"
    assert result["host"] == "test"
    assert result["port"] == 1234
    assert result["path"] == "/test"

    # Case with real-ip header unset
    headers["real-ip"] = None
    result = parse_xforwarded(headers, None)

# Generated at 2022-06-14 07:19:57.984204
# Unit test for function fwd_normalize
def test_fwd_normalize():
    class config:
        PROXIES_COUNT = 1
        FORWARDED_FOR_HEADER = "x-forwarded-for"
    class headers:
        def get(self, key):
            return {
                "x-real-ip": "10.0.0.1",
                "x-forwarded-for": "1.2.3.4, 10.0.0.1, 192.168.1.1",
                "x-scheme": "http",
                "x-forwarded-proto": "https",
                "x-forwarded-host": "example.com",
                "x-forwarded-port": "443",
                "x-forwarded-path": "/foo%20bar",
            }.get(key, None)

# Generated at 2022-06-14 07:20:05.186133
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    h1 = {'X-FORWARDED-FOR': '10.0.0.1'}
    h2 = {'X-FORWARDED-FOR': '10.0.0.1,192.168.0.1;proto=http'}
    h3 = {'X-FORWARDED-FOR': '10.0.0.1,192.168.0.1;proto=http,proto=http'}
    h4 = {'X-FORWARDED-FOR': ';proto=http,proto=http'}
    h5 = {'X-FORWARDED-FOR': '10.0.0.1,192.168.0.1;"=";proto=http'}

# Generated at 2022-06-14 07:20:16.863157
# Unit test for function parse_forwarded
def test_parse_forwarded():
    assert parse_forwarded(
        {"forwarded": "for=192.0.2.60;proto=http,for=192.0.2.43;proto=http"},
        123
    ) == {"for": "192.0.2.60", "proto": "http"}
    assert parse_forwarded(
        {
            "forwarded": "secret=123;for=192.0.2.60;proto=http,for=192.0.2.43;proto=http"
        },
        123
    ) == {"for": "192.0.2.60", "proto": "http"}
    assert parse_forwarded({"forwarded": "for=192.0.2.60;proto=http"}, 123) is None

# Generated at 2022-06-14 07:20:27.235353
# Unit test for function parse_forwarded
def test_parse_forwarded():
    headers = {
        'Forwarded': (
            'by=_hidden,for=10.0.2.2;host=myhost.com;proto=https,for=10.0.2.2;host=myhost2.com;proto=https'
        ),
    }
    config = MagicMock()
    config.FORWARDED_SECRET = 'foobar'

    normalized = parse_forwarded(headers, config)
    assert(normalized == {
        'by': '_hidden',
        'for': '10.0.2.2',
        'host': 'myhost.com',
        'proto': 'https'
    })

# Generated at 2022-06-14 07:21:04.161992
# Unit test for function fwd_normalize
def test_fwd_normalize():
    assert fwd_normalize([("unknown", None), ("for", "example")]) \
        == {"for": "example"}
    assert fwd_normalize([("for", "192.0.2.1")]) == {"for": "192.0.2.1"}
    assert fwd_normalize([("for", "192.0.2.1"), ("host", "example")]) \
        == {"for": "192.0.2.1", "host": "example"}
    assert fwd_normalize([("for", "192.0.2.1"), ("unknown", "example")]) \
        == {"for": "192.0.2.1"}