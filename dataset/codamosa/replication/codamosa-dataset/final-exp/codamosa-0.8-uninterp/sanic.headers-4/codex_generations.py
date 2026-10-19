

# Generated at 2022-06-14 07:11:31.214980
# Unit test for function parse_forwarded
def test_parse_forwarded():
    import asynctest
    from asynctest.mock import CoroutineMock, patch
    from sanic.config import Config
    from sanic.request import Request
    from sanic.response import HTTPResponse
    from sanic.server import HttpProtocol

    config = Config()
    config.FORWARDED_SECRET = "super_secret"
    # pylint: disable=unused-variable
    @asynctest.mock.patch("sanic.server.HttpProtocol.write_response")
    @asynctest.mock.patch("sanic.server.HttpProtocol.write_error")
    async def test(mock_write_response, mock_write_error, app):
        http_protocol = HttpProtocol(None, None, None, loop=app.loop)



# Generated at 2022-06-14 07:11:37.590182
# Unit test for function fwd_normalize_address
def test_fwd_normalize_address():
    assert fwd_normalize_address("0.0.0.0") == "0.0.0.0"
    assert fwd_normalize_address("[::1]") == "[::1]"
    assert fwd_normalize_address("_123") == "_123"
    assert fwd_normalize_address("unknown") == None

# Generated at 2022-06-14 07:11:51.638820
# Unit test for function parse_forwarded
def test_parse_forwarded():
    header_list = ["secret=a; by=127.0.0.1; for=127.0.0.1; proto=https; host=foo.bar.com"]
    headers = CaseInsensitiveMultidict(header_list)
    config = Config()
    config.FORWARDED_SECRET = "a"
    config.FORWARDED_FOR_HEADER = "X-Forwarded-For"
    config.FORWARDED_PROTO_HEADER = "X-Forwarded-Proto"
    config.FORWARDED_HOST_HEADER = "X-Forwarded-Host"
    config.FORWARDED_PORT_HEADER = "X-Forwarded-Port"
    config.FORWARDED_PREFIX_HEADER = "X-Forwarded-Prefix"
    config.FORWARDED_PATH_HEAD

# Generated at 2022-06-14 07:11:58.718148
# Unit test for function fwd_normalize
def test_fwd_normalize():
    """Tests for function fwd_normalize"""
    from sanic import Config, Sanic

    app = Sanic()
    config = Config()
    config.FORWARDED_SECRET = "secret"
    config.FORWARDED_FOR_HEADER = "X-Forwarded-For"
    config.REAL_IP_HEADER = "X-Real-IP"
    config.PROXIES_COUNT = 1

    assert fwd_normalize(parse_forwarded({'Forwarded': 'secret=test;'}, config)) == {
        'secret': 'test'
    }
    assert fwd_normalize(
        parse_forwarded({'Forwarded': 'secret=test, by=test;'}, config)
    ) == {'secret': 'test', 'by': 'test'}
    assert fwd_normal

# Generated at 2022-06-14 07:12:10.907721
# Unit test for function parse_forwarded
def test_parse_forwarded():
    options = parse_forwarded(
        {'Forwarded': ['for=198.51.100.17,for=198.51.100.17;by=203.0.113.43;proto=http', 'for=198.51.100.17;by=203.0.113.43']},
        {'FORWARDED_SECRET': 'stuart_mclure_rules_the_world'}
    )
    assert options == {'for': '198.51.100.17', 'by': '203.0.113.43', 'proto': 'http'}


# Generated at 2022-06-14 07:12:23.856223
# Unit test for function parse_forwarded
def test_parse_forwarded():
    # testcase 1
    print("testcase 1")
    headers = {"Forwarded": "for=127.0.0.1;proto=http;by=127.0.0.1, for=192.168.1.1;by=127.0.0.1"}
    config = {"FORWARDED_SECRET": "127.0.0.1"}
    print(parse_forwarded(headers, config))

    # testcase 2
    print("testcase 2")
    headers = {"Forwarded": "for=\"[127.0.0.1]\";by=192.168.1.1;for=\"192.168.1.1\""}
    config = {"FORWARDED_SECRET": "127.0.0.1"}
    print(parse_forwarded(headers, config))

test_parse_forward

# Generated at 2022-06-14 07:12:32.064156
# Unit test for function fwd_normalize

# Generated at 2022-06-14 07:12:45.645371
# Unit test for function parse_forwarded
def test_parse_forwarded():
    headers = {"Forwarded" : [
        "for=192.0.2.60;proto=http;by=203.0.113.43,for=198.51.100.17",
        "for=\"[2001:db8:cafe::17]\",for=unknown,for=192.0.2.43",
        "for=192.0.2.43;by=127.0.0.1;proto=https;host=example.com;port=8080"]}

    options = parse_forwarded(headers, {"FORWARDED_SECRET" : None})
    print(options)
    #assert options == {'for': '198.51.100.17', 'by': '127.0.0.1',
    #'proto': 'https', 'host': 'example.com', 'port': 80

# Generated at 2022-06-14 07:12:51.532090
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    # headers = {'x-scheme': 'https', 'x-forwarded-host': 'www.example.com', 'x-forwarded-port': '443', 'x-forwarded-path': '/test', 'x-forwarded-proto': 'https'}
    headers = {'x-scheme': 'https', 'x-forwarded-host': 'www.example.com', 'x-forwarded-path': '/test', 'x-forwarded-proto': 'https'}
    config = Dict(PROXIES_COUNT=1, FORWARDED_FOR_HEADER='x-forwarded-for')
    ret = parse_xforwarded(headers, config)
    print(ret)

if __name__ == '__main__':
    test_parse_xforwarded()

# Generated at 2022-06-14 07:13:00.027373
# Unit test for function fwd_normalize_address
def test_fwd_normalize_address():
    import pytest
    assert fwd_normalize_address("_162.13.1.1") == "_162.13.1.1"
    assert fwd_normalize_address("1:2:3:4:5:6:1.2.3.4") == "[1:2:3:4:5:6:1.2.3.4]"
    with pytest.raises(ValueError):
        fwd_normalize_address("unknown")

# Generated at 2022-06-14 07:13:20.872923
# Unit test for function parse_forwarded
def test_parse_forwarded():
    from sanic.request import Request
    from sanic.config import Config
    config = Config()
    config.FORWARDED_SECRET = 'prod-secret'
    req = Request("GET", "/test", headers={'Forwarded': 'secret=prod-secret; by=mweibel; proto=https; host=localhost; for=192.168.1.2'})
    assert parse_forwarded(req.headers, config) == {'secret': 'prod-secret', 'by': 'mweibel', 'proto': 'https', 'host': 'localhost', 'for': '192.168.1.2'}

# Generated at 2022-06-14 07:13:31.522861
# Unit test for function parse_host
def test_parse_host():
    assert parse_host('localhost:80') == ('localhost', 80)
    assert parse_host('127.0.0.1:80') == ('127.0.0.1', 80)
    assert parse_host('127.0.0.1') == ('127.0.0.1', None)
    assert parse_host('localhost') == ('localhost', None)
    assert parse_host('[::1]:80') == ('[::1]', 80)
    assert parse_host('[::1]') == ('[::1]', None)
    assert parse_host('[::1') is (None, None)
    assert parse_host('::1]:80') is (None, None)
    assert parse_host(']::1') is (None, None)

# Generated at 2022-06-14 07:13:45.529206
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    """
    Test parse_xforwarded function
    """
    headers = [('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:68.0) Gecko/20100101 Firefox/68.0'),
    ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    ('Accept-Language', 'en-US,en;q=0.5'),
    ('Accept-Encoding', 'gzip, deflate, br'),
    ('Upgrade-Insecure-Requests', '1'),
    ('If-None-Match', 'W/"2a4-4d6460c017fb3"')]

# Generated at 2022-06-14 07:13:57.498055
# Unit test for function parse_forwarded
def test_parse_forwarded():
    headers = {"forwarded": "secret=123;for=192.168.1.1;proto=https"}
    config = MagicMock()
    config.FORWARDED_SECRET = "123"
    assert parse_forwarded(headers, config) == {"for": "192.168.1.1", "proto": "https"}
    headers = {"forwarded": "for=192.168.1.1;proto=https"}
    assert parse_forwarded(headers, config) == None
    headers = {"forwarded": "secret=abc;for=192.168.1.1;proto=https"}
    assert parse_forwarded(headers, config) == None
    headers = {"forwarded": "secret=123, secret=222;for=192.168.1.1;proto=https"}
    assert parse_forward

# Generated at 2022-06-14 07:14:09.705175
# Unit test for function fwd_normalize
def test_fwd_normalize():
    test_dict = {
        "for": "test",
        "host": "testhost.com",
        "proto": "testproto",
        "port": "testport",
        "path": "testpath",
        "other": "other"
    }
    normalize_dict = fwd_normalize(test_dict.items())
    assert test_dict["for"] == normalize_dict["for"]
    assert test_dict["host"] == normalize_dict["host"]
    assert test_dict["proto"] == normalize_dict["proto"]
    assert test_dict["port"] == normalize_dict["port"]
    assert test_dict["path"] == normalize_dict["path"]
    assert not "other" in normalize_dict


# Generated at 2022-06-14 07:14:20.397715
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    # Make a dummy request
    class DummyReq():
        def __init__(self, headers):
            self.headers = headers
    # Set custom headers
    custom_headers = {'X-Forwarded-Path': '/testing', 'X-Real-Host': '1.2.3.4'}
    req = DummyReq(custom_headers)
    # Without a real ip header, it should return none
    assert parse_xforwarded(req.headers, None) == None
    # With X-Real-Ip header, it should return the data
    assert parse_xforwarded(req.headers, 'X-Real-Ip') == None

# Generated at 2022-06-14 07:14:29.373194
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    # Scenario 1: X-Real-IP header is set
    class Headers1:
        def get(self, header):
            if header == "x-real-ip":
                return "192.168.1.100"
            else:
                return None
    class Config1:
        REAL_IP_HEADER = "x-real-ip"
        PROXIES_COUNT = 0
    headers1 = Headers1()
    config1 = Config1()
    result1 = parse_xforwarded(headers1, config1)
    assert result1["for"] == "192.168.1.100"
    # Scenario 2: X-Real-IP and X-Forwarded-For headers are set
    class Headers2:
        def get(self, header):
            if header == "x-real-ip":
                return

# Generated at 2022-06-14 07:14:41.752590
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    from sanic import Sanic
    app = Sanic("test_app")

    app.config.REAL_IP_HEADER = "X-Real-Ip"
    app.config.FORWARDED_FOR_HEADER = "X-Forwarded-For"
    app.config.PROXIES_COUNT = 1

    class MockRequest:
        def __init__(self, headers):
            self.headers = headers

    fake_request = MockRequest({"X-Forwarded-For": "127.0.0.1, 192.168.0.1"})

    result = parse_xforwarded(fake_request.headers, app.config)
    assert result["for"] == "192.168.0.1"

    result = parse_host(result["for"])

# Generated at 2022-06-14 07:14:54.186532
# Unit test for function parse_forwarded
def test_parse_forwarded():
    import re
    import requests
    import sanic
    import sanic_utils

    app = sanic.Sanic('test_parse_forwarded')
    #app.config['FORWARDED_SECRET'] = '123456'
    app.config['SERVER_NAME'] = '127.0.0.1:8000'
    app.config['FORWARDED_SECRET'] = '123456'

    app.add_route(sanic_utils.parse_forwarded, '/')


# Generated at 2022-06-14 07:15:03.239073
# Unit test for function parse_forwarded

# Generated at 2022-06-14 07:15:15.556827
# Unit test for function parse_forwarded
def test_parse_forwarded():
    class Request:
        def __init__(self, headers=None, config=None):
            if headers:
                self.headers = headers.copy()
            else:
                self.headers = {}
            if config:
                self.config = config
            else:
                self.config = {}

        def getall(self, name):
            return self.headers.get(name)

    # Sanic's default config

# Generated at 2022-06-14 07:15:25.273917
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {"x-forwarded-host": "192.168.1.1:8888",
               "x-forwarded-path": "/path",
               "x-forwarded-proto": "https",
               "x-scheme": "http"}
    config = Config()
    config.REAL_IP_HEADER = "x-forwarded-for"
    config.FORWARDED_FOR_HEADER = "x-forwarded-for"
    config.PROXIES_COUNT = 1

    returned = parse_xforwarded(headers, config)
    assert returned
    assert returned["host"] == "192.168.1.1:8888"
    assert returned["path"] == "/path"
    assert returned["proto"] == "https"



# Generated at 2022-06-14 07:15:36.364011
# Unit test for function fwd_normalize
def test_fwd_normalize():
    from sanic.utils import sanic_endpoint_test
    from sanic.request import ProxyRequest, RequestParameters
    from sanic import Sanic
    from sanic.app import Sanic, SanicConfig
    from sanic.response import text, json
    def test_fwd_normalize(request: ProxyRequest):
        return text(fwd_normalize(request.forwarded))
    app = Sanic(__name__)
    app.add_route(test_fwd_normalize, '/fwd_addr')
    app.websocket_enabled = False
    app.forwarded_enabled = True
    app.config.FORWARDED_SECRET = 'secret'
    app.config.FORWARDED_FOR_HEADER = 'X-Forwarded-For'

# Generated at 2022-06-14 07:15:50.709070
# Unit test for function parse_forwarded
def test_parse_forwarded():
    headers = {
        "Forwarded": "for=\"_mdnx\", for=192.0.2.60; proto=https, for=192.0.2.43, for=198.51.100.17; by=\"_mdnx\"; host=example.com",
        "X-Forwarded-Host": "example.com",
        "X-Forwarded-Proto": "https",
        "X-Forwarded-Path": "/t/s"
    }
    options = parse_forwarded(headers, "SECRET")
    assert options is None


# Generated at 2022-06-14 07:15:57.026581
# Unit test for function fwd_normalize

# Generated at 2022-06-14 07:16:08.322418
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    """
    这个代码没有问题
    """
    headers = {
        "X-Forwarded-For": "192.168.1.1, 192.168.1.2, 192.168.1.3, "
    }
    config = {

    }
    real_ip_header = "X-Forwarded-For"
    proxies_count = 3

    # real_ip_header = config.REAL_IP_HEADER
    # proxies_count = config.PROXIES_COUNT

    print(parse_xforwarded(headers, config))


if __name__ == '__main__':
    test_parse_xforwarded()

# Generated at 2022-06-14 07:16:21.596457
# Unit test for function fwd_normalize
def test_fwd_normalize():
    import pytest

    testvec = [
        ("RHaG9zdC0xCg==", (None, "host-1")),
        ("RHaG9zdC0yCg==", (None, "host-2")),
        ("RHaG9zdC0zCg==", (None, "host-3")),
        ("RHaG9zdC0xCg==_1Zj0xMC4yMC4zMA==", (None, "host-1_1f10.20.30")),  # underscore
        #dot
        ("RHaG9zdC0xCg==_1Zj0xMC4yMC4zMC4K", (None, "host-1_1f10.20.30."))
    ]

# Generated at 2022-06-14 07:16:28.021147
# Unit test for function fwd_normalize

# Generated at 2022-06-14 07:16:38.611908
# Unit test for function parse_forwarded
def test_parse_forwarded():
    # 1. No Forwarded header => bail
    test_headers = {
        'host': '127.0.0.1:8000'
    }
    assert(parse_forwarded(test_headers, None) is None)
    # 2. Forwarded header exists, but secret does not match => bail
    test_headers = {
        'host': '127.0.0.1:8000',
        'forwarded': 'by=127.0.0.1;proto=http;secret=1234'
    }
    assert(parse_forwarded(test_headers, None) is None)
    # 3. Forwarded header exists, but secret is None => bail

# Generated at 2022-06-14 07:16:50.184462
# Unit test for function parse_forwarded
def test_parse_forwarded():
    # test data
    secret_header='Forwarded';
    secret="dasdfasdfasdf"
    url="https://192.168.1.0:80"
    # {BY}<https|http>://<host>:<port><path>; <params>
    header1="by=192.168.1.1; for=192.168.1.0; proto=https; host=192.168.1.0; path=/test/1"
    header2="by=192.168.1.1; for=192.168.1.0; proto=https; host=192.168.1.0; path=/test/1; k1=v1"

# Generated at 2022-06-14 07:17:07.233219
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    import json
    import aiohttp
    from sanic import Sanic
    from sanic.response import text
    app = Sanic(__name__)

    @app.route("/test")
    async def test(request):
        return text(json.dumps(parse_xforwarded(request.headers, app.config)))

    client = aiohttp.ClientSession()


# Generated at 2022-06-14 07:17:20.042613
# Unit test for function fwd_normalize
def test_fwd_normalize():
    assert fwd_normalize([]) == {}
    assert fwd_normalize([("for", "192.0.2.1")]) == {"for": "192.0.2.1"}
    assert fwd_normalize([("for", "192.0.2.1"), ("by", "2001:db8::1")]) == {
        "for": "192.0.2.1",
        "by": "[2001:db8::1]",
    }
    assert fwd_normalize([("host", "example.com")]) == {"host": "example.com"}
    assert fwd_normalize([("proto", "https")]) == {"proto": "https"}
    assert fwd_normalize([("path", "/")]) == {"path": "/"}

# Generated at 2022-06-14 07:17:30.261393
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {"x-forwarded-host": "host", "x-scheme": "scheme", "x-forwarded-proto": "proto", "x-forwarded-port": "port",
        "x-forwarded-path": "path"}
    config = type('FakeConfig', (object,), {})
    config.REAL_IP_HEADER = "x-real-ip"
    config.PROXIES_COUNT = 3
    config.FORWARDED_FOR_HEADER = "forwarded"
    fwd = parse_xforwarded(headers, config)
    assert fwd is not None
    assert fwd["for"] == "127.0.0.1"
    assert fwd["proto"] == "proto"
    assert fwd["port"] == "port"
    assert fwd["host"]

# Generated at 2022-06-14 07:17:43.404914
# Unit test for function parse_forwarded
def test_parse_forwarded():
    assert parse_forwarded(["secret=foo", "by=_bar"], MagicMock(FORWARDED_SECRET="foo")) == {
        "by": "_bar"
    }
    assert parse_forwarded(["secret=bar", "by=_bar"], MagicMock(FORWARDED_SECRET="foo")) == None
    assert parse_forwarded(["by=_bar", "secret=foo"], MagicMock(FORWARDED_SECRET="foo")) == {
        "by": "_bar"
    }
    assert parse_forwarded(["for=_bar", "secret=foo"], MagicMock(FORWARDED_SECRET="foo")) == {
        "for": "_bar"
    }

# Generated at 2022-06-14 07:17:56.330650
# Unit test for function parse_forwarded
def test_parse_forwarded():
    class Test:
        FORWARDED_SECRET = 'secret'

    assert parse_forwarded(
        {'forwarded': ['for="_abc";proto=https']},
        Test,
    ) == {'for': '_abc', 'proto': 'https'}
    assert parse_forwarded(
        {'forwarded': ['secret="secret";for="_abc";proto=https']},
        Test,
    ) == {'for': '_abc', 'proto': 'https'}
    assert parse_forwarded(
        {'forwarded': ['for="_abc";secret="secret";proto=https']},
        Test,
    ) == {'for': '_abc', 'proto': 'https'}

# Generated at 2022-06-14 07:18:07.537399
# Unit test for function parse_forwarded
def test_parse_forwarded():
    def _test(**headers):
        return parse_forwarded(headers, "secret")
    assert _test(forwarded="secret=42") is None
    assert _test(forwarded="for=1.2.3.4; secret=42") == {"for": "1.2.3.4"}
    assert _test(
        forwarded="by=_; for=_; host=example; secret=42",
        forwarded="by=_; for=_; host=_; secret=42",
    ) == {"by": "_", "for": "_", "host": "example"}

# Generated at 2022-06-14 07:18:19.354284
# Unit test for function parse_forwarded
def test_parse_forwarded():
    # RFC example: https://tools.ietf.org/html/rfc7239#section-4
    assert parse_forwarded({'Forwarded': 'for=192.0.2.60; proto=http; by=203.0.113.43'}, None) == {'for': '192.0.2.60', 'proto': 'http', 'by': '203.0.113.43'}
    assert parse_forwarded({'Forwarded': 'for=192.0.2.43, for=198.51.100.17'}, None) == {'for': '192.0.2.43'}

# Generated at 2022-06-14 07:18:30.618538
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    import pprint

    headers = {"X-Forwarded-For": "127.0.0.1"}
    pprint.pprint(parse_xforwarded(headers, None))
    headers = {"Real-Ip": "127.0.0.1"}
    pprint.pprint(parse_xforwarded(headers, None))
    headers = {
        "X-Forwarded-For": "127.0.0.1, 192.168.1.1",
        "X-Forwarded-Host": "example.com",
        "X-Forwarded-Port": "443",
    }
    pprint.pprint(parse_xforwarded(headers, None))

# Generated at 2022-06-14 07:18:41.192995
# Unit test for function fwd_normalize
def test_fwd_normalize():
    assert fwd_normalize([]) == {}
    assert fwd_normalize([("key", "val")]) == {"key": "val"}
    assert fwd_normalize([("key", "")]) == {"key": ""}
    assert fwd_normalize([("by", "0.0.0.0")]) == {"by": "0.0.0.0"}
    assert fwd_normalize([("by", "::0")]) == {"by": "[::0]"}
    assert fwd_normalize([("by", "_mysecret")]) == {"by": "_mysecret"}
    assert fwd_normalize([("for", "1.2.3.4")]) == {"for": "1.2.3.4"}
    assert fwd_normali

# Generated at 2022-06-14 07:18:51.279168
# Unit test for function fwd_normalize
def test_fwd_normalize():
    assert fwd_normalize(
            [('by', 'http://localhost:8080/test/?test=123'),
             ('for', '192.168.0.1'),
             ('host', 'example.com:8080'),
             ('proto', 'http'),
             ('port', '8080'),
             ('path', '/test/?test=123')]) == {
                     'by': 'http://localhost:8080/test/?test=123',
                     'for': '192.168.0.1',
                     'host': 'example.com:8080',
                     'proto': 'http',
                     'port': 8080,
                     'path': '/test/?test=123'}

# Generated at 2022-06-14 07:19:09.971508
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {
        "x-scheme": "http",
        "x-forwarded-host": "localhost:8000",
        "x-forwarded-port": "8000",
        "x-forwarded-path": "",
        "x-forwarded-for": "1.1.1.1, 2.2.2.2, 3.3.3.3",
    }
    config = type(
        "FakeConfig", (), {
            "FORWARDED_FOR_HEADER": "X-Forwarded-For",
            "REAL_IP_HEADER": "X-Forwarded-For",
            "PROXIES_COUNT": 3,
            "FORWARDED_SECRET": None,
        }
    )
    config = config()

# Generated at 2022-06-14 07:19:23.233914
# Unit test for function parse_forwarded
def test_parse_forwarded():
    from sanic.request import Headers
    headers = Headers([("Forwarded", "by=10.10.10.2")])
    config = Config()
    config.FORWARDED_SECRET = "secret"
    config.PROXIES_COUNT = 2
    config.REAL_IP_HEADER = "X-Forwarded-For"
    assert parse_forwarded(headers, config) == {"by": "10.10.10.2"}
    headers = Headers(
        [
            ("Forwarded", "For=10.10.10.2, for=10.10.10.3; secret=secret"),
            ("Forwarded", "For=10.10.10.4, for=10.10.10.5; secret=secret"),
        ]
    )
    assert parse_forwarded(headers, config)

# Generated at 2022-06-14 07:19:34.046335
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {
    404: {"X-Forwarded-Host":"localhost:5000",
         "X-Forwarded-Port":"5000",
         "X-Forwarded-Path":"",
         "X-Scheme":"http",
         "X-Forwarded-For":"127.0.0.1",
         "X-Forwarded-Protocol":"https"
         },
    }

# Generated at 2022-06-14 07:19:47.006266
# Unit test for function parse_forwarded
def test_parse_forwarded():
    url = "https://python.org/test_url"
    sample_headers = [
        (b"Forwarded", b"for=192.0.2.60;proto=http;by=203.0.113.43, for=192.0.2.60;proto=https;by=203.0.113.43"),
        (b"Forwarded", b"for=192.0.2.60;proto=http;by=203.0.113.43, for=192.0.2.60;proto=https;by=203.0.113.43")
    ]
    config = Config()
    config.FORWARDED_SECRET = None

# Generated at 2022-06-14 07:19:51.113042
# Unit test for function parse_forwarded
def test_parse_forwarded():
    assert parse_forwarded(["by=127.0.0.1,for=127.0.0.1"], config) == {"secret": "127.0.0.1", "by": "127.0.0.1", "for": "127.0.0.1"}

# Generated at 2022-06-14 07:19:56.905212
# Unit test for function parse_forwarded
def test_parse_forwarded():
    assert parse_forwarded({"forwarded":"secret=yoyoyo;by=127.0.0.1, secret=yoyoyo;by=127.0.0.1"},MagicMock(FORWARDED_SECRET="secret=yoyoyo")) == {'by': '127.0.0.1', 'secret': 'secret=yoyoyo'}

# Generated at 2022-06-14 07:20:04.129498
# Unit test for function parse_forwarded
def test_parse_forwarded():
    d = parse_forwarded({"Forwarded": "For=192.0.2.60;proto=https"}, None)
    assert d == {"for":"192.0.2.60","proto":"https"}
    d = parse_forwarded({"Forwarded": "For=\"_gazonk\""}, None)
    assert d == {"for":"_gazonk"}
    d = parse_forwarded({"Forwarded": "For=192.0.2.43, for=198.51.100.17"}, None)
    assert d == {"for":"198.51.100.17"}
    d = parse_forwarded({"Forwarded": "For=\"[2001:db8:cafe::17]:4711\""}, None)
    assert d == {"for":"[2001:db8:cafe::17]:4711"}

# Generated at 2022-06-14 07:20:15.719993
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    from socket import socket
    sock = socket()
    sock.bind(("127.0.0.1", 0))

# Generated at 2022-06-14 07:20:22.459366
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    request_headers = {'X-Forwarded-For': 'www.example.com', 'X-Scheme': 'http',
                        'X-Forwarded-Host': 'example.com', 'X-Forwarded-Path': 'example/path'}
    print(parse_xforwarded(request_headers))


if __name__ == "__main__":
    test_parse_xforwarded()

# Generated at 2022-06-14 07:20:30.479192
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    from sanic.config import Config
    cfg = Config()
    h = {
        'x-forwarded-for': '1.1.1.1', 
        'x-scheme': 'https', 
        'x-forwarded-host': 'www.example.org', 
        'x-forwarded-port': '443', 
        'x-forwarded-path': '/new/path'
    }
    
    assert parse_xforwarded(h, cfg) == {'for': '1.1.1.1', 'proto': 'https', 'host': 'www.example.org', 'port': 443, 'path': '/new/path'}

# Generated at 2022-06-14 07:20:48.950998
# Unit test for function parse_forwarded
def test_parse_forwarded():
    assert parse_forwarded({"forwarded": "for=192.0.2.60;proto=http;by=203.0.113.43"}, {"FORWARDED_SECRET": None}) == {"for": "192.0.2.60", "proto":"http", "by":"203.0.113.43"}
    assert parse_forwarded({"forwarded": "for=\"_gazonk\";proto=http;by=203.0.113.43"}, {"FORWARDED_SECRET": None}) == {"for": "_gazonk", "proto":"http", "by":"203.0.113.43"}

# Generated at 2022-06-14 07:21:01.531596
# Unit test for function parse_forwarded
def test_parse_forwarded():
    headers = {"forwarded": "FOR=192.0.2.60;proto=http;host=www.example.com;secret=FORWARDED_SECRET,for=192.0.2.30;proto=http;host=www.example.com, for=192.0.2.20;proto=http;host=www.example.com"}
    config = type('ForwardedSecretTest', (object, ), {})
    config.FORWARDED_SECRET = "FORWARDED_SECRET"
    expected_result = {"for": '192.0.2.60', "proto": 'http', "host": 'www.example.com'}
    assert parse_forwarded(headers, config) == expected_result

# Generated at 2022-06-14 07:21:14.694127
# Unit test for function parse_forwarded
def test_parse_forwarded():
    assert parse_forwarded({'forwarded': ['for=12345,by=localhost']}, {'FORWARDED_SECRET': 'localhost'}) == {'for': '12345', 'by': 'localhost'}
    assert parse_forwarded({'forwarded': ['for=12345,secret=localhost']}, {'FORWARDED_SECRET': 'localhost'}) == {'for': '12345', 'secret': 'localhost'}
    assert parse_forwarded({'forwarded': ['for=12345,secret=localhost']}, {'FORWARDED_SECRET': 'anothersecret'}) == None
    assert parse_forwarded({'forwarded': ['for=12345,secret=localhost']}, {}) == None


if __name__ == '__main__':
    test_parse_forwarded()