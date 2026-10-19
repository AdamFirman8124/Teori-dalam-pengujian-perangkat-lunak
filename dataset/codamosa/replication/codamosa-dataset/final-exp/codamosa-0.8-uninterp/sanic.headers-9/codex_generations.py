

# Generated at 2022-06-14 07:11:29.721769
# Unit test for function fwd_normalize_address
def test_fwd_normalize_address():
    s = {
        "foo": "foo",
        "127.0.0.1": "127.0.0.1",
        "::1": "[::1]",
        "www.example.com": "www.example.com",
        "__private_addr": "_private_addr",
        "unknown": ValueError(),
    }
    for k, v in s.items():
        if isinstance(v, ValueError):
            with pytest.raises(ValueError):
                fwd_normalize_address(k)
        else:
            assert fwd_normalize_address(k) == v

# Generated at 2022-06-14 07:11:34.822611
# Unit test for function parse_content_header
def test_parse_content_header():
    value = "form-data; name=upload; filename=\"file.txt\""
    ct, params = parse_content_header(value)
    print(ct, params)
    assert ct == "form-data"
    assert params == {'name': 'upload', 'filename': 'file.txt'}

if __name__ == "__main__":
    test_parse_content_header()

# Generated at 2022-06-14 07:11:49.682884
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    from collections import namedtuple

    SanicHeaders = namedtuple('SanicHeaders', 'headers')
    headers = {
        'x-forwarded-for': '192.168.1.1, 192.168.1.2',
        'x-forwarded-host': 'example.com',
        'x-forwarded-port': '8080',
        'x-forwarded-proto': 'https',
        'x-forwarded-path': '/path/'
    }
    res = parse_xforwarded(SanicHeaders(headers), None)
    assert res['for'] == '192.168.1.1'
    assert res['host'] == 'example.com'
    assert res['port'] == 8080
    assert res['proto'] == 'https'

# Generated at 2022-06-14 07:12:02.301757
# Unit test for function fwd_normalize_address
def test_fwd_normalize_address():
    addr = '127.0.0.1'
    assert fwd_normalize_address(addr) == '127.0.0.1'

    addr = '[::]'
    assert fwd_normalize_address(addr) == '[::]'

    addr = '[:::1'
    assert fwd_normalize_address(addr) == '[:::1'

    addr = '[::1]'
    assert fwd_normalize_address(addr) == '[::1]'

    addr = '::1'
    assert fwd_normalize_address(addr) == '[::1]' 

    addr = '::'
    assert fwd_normalize_address(addr) == '::'

    addr = '::1'
    assert fwd_normalize_address(addr) == '[::1]'

    addr = '::1]'


# Generated at 2022-06-14 07:12:12.305247
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {
        "x-scheme":"http",
        "x-forwarded-path":"/api/v1/test",
        "x-forwarded-host":"localhost",
        "x-forwarded-port": "80",
    }
    config = Config()
    config.FORWARDED_FOR_HEADER = "x-forwarded-for"
    config.FORWARDED_PORT_HEADER = "x-forwarded-port"
    config.FORWARDED_SCHEME_HEADER = "x-forwarded-scheme"
    config.FORWARDED_HOST_HEADER = "x-forwarded-host"
    config.REAL_IP_HEADER = "x-real-ip"
    config.PROXIES_COUNT = 1

# Generated at 2022-06-14 07:12:16.846188
# Unit test for function fwd_normalize_address
def test_fwd_normalize_address():
    addr = "\n\t0:0:0:0:0:0:0:1:80\n"
    assert fwd_normalize_address(addr) == "0:0:0:0:0:0:0:1"

# Generated at 2022-06-14 07:12:26.218217
# Unit test for function parse_forwarded
def test_parse_forwarded():
    import time
    import timeit
    import argparse
    from collections import defaultdict
    from itertools import count
    import multiprocessing
    from os import environ
    try:
        from ..worker import create_worker
    except ImportError:
        from worker import create_worker
    from ..router import Router
    from ..config import Config
    from ..request import Request
    from ..response import HTTPResponse

    def parse(headers, count_repeat=100000):
        env = dict(environ)
        env.update(
            {
                "REQUEST_METHOD": "GET",
                "SERVER_PROTOCOL": "HTTP/1.1",
                "SERVER_NAME": "server",
            }
        )

# Generated at 2022-06-14 07:12:30.361497
# Unit test for function parse_host
def test_parse_host():
    assert parse_host("localhost") == ('localhost', None)
    assert parse_host("localhost:80") == ('localhost', 80)
    assert parse_host("::1:80") == ('[::1]', 80)


# Generated at 2022-06-14 07:12:41.239279
# Unit test for function parse_host

# Generated at 2022-06-14 07:12:49.073537
# Unit test for function parse_forwarded
def test_parse_forwarded():
    assert(
        parse_forwarded(
            {
                "forwarded": ["By=bot.example.com; For=192.0.2.60; Host=example.com; Proto=https; Path=/mypath",
                              "By=bot.example.com; For=192.0.2.60; Host=example.com; Proto=https; Path=/mypath"]

            },
            {"FORWARDED_SECRET": "bot.example.com"}
        )
        == {"by": "bot.example.com", "for": "192.0.2.60", "host": "example.com", "proto": "https", "path": "/mypath"}
    )

# Generated at 2022-06-14 07:13:05.219838
# Unit test for function parse_forwarded

# Generated at 2022-06-14 07:13:12.398452
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = [
        ('x-scheme', 'https'),
        ('x-forwarded-host', 'host.com:3000'),
        ('x-forwarded-port', '3000'),
        ('x-forwarded-path', '/foo/bar'),
    ]
    res = parse_xforwarded(headers, "0.0.0.0")
    print(res)



# Generated at 2022-06-14 07:13:18.295537
# Unit test for function fwd_normalize
def test_fwd_normalize():
    import pytest
    def o(**kw):
        return kw

    assert fwd_normalize([]) == {}

# Generated at 2022-06-14 07:13:31.279294
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    class DictMock:
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)

    config = DictMock(
        PROXIES_COUNT=3, REAL_IP_HEADER="X-Forwarded-For", FORWARDED_SECRET="secret"
    )

    class HeadersMock:
        def get(self, key):
            return key

        def getall(self, key):
            return key

    headers_mock = HeadersMock()


# Generated at 2022-06-14 07:13:35.583231
# Unit test for function parse_forwarded
def test_parse_forwarded():
    assert parse_forwarded(['foo, by=bar, for="192.168.1.1", secret="secret"'], ['secret']) == {'by': 'bar', 'for': '192.168.1.1'}

# Generated at 2022-06-14 07:13:49.024382
# Unit test for function fwd_normalize_address
def test_fwd_normalize_address():
    assert fwd_normalize_address("_some_weird_string") == "_some_weird_string"
    assert fwd_normalize_address("Unknown") == "unknown"
    assert fwd_normalize_address("unknown") == "unknown"
    assert fwd_normalize_address("127.0.0.1") == "127.0.0.1"
    assert fwd_normalize_address("127.0.0.1.") == "127.0.0.1."
    assert fwd_normalize_address("127.0.0.1.0") == "127.0.0.1.0"
    assert fwd_normalize_address("127.0.0.1.1") == "127.0.0.1.1"

# Generated at 2022-06-14 07:14:03.262776
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    """Unit test for function parse_xforwarded"""
    from sanic.config import Config
    from sanic.request import RequestParameters

    config = Config()


# Generated at 2022-06-14 07:14:15.678767
# Unit test for function parse_forwarded
def test_parse_forwarded():
    names = {'by': '192.168.1.1', 'for': '192.168.1.1', 'host': 'example.com', 'proto': 'https', 'port': '80', 'path': '/upgrade'}
    forwarded = 'by=192.168.1.1; for="192.168.1.1"; host=example.com; proto=https; port=80; path=/upgrade'
    # chained keys work
    key = 'by, for'
    secret = 'abcdef'
    fwd = parse_forwarded({'forwarded': f'{key}={secret}; {forwarded}'}, type('', (object,), {'PROXIES_COUNT': 0, 'FORWARDED_SECRET': secret}))
    assert fwd == names
    # chained values work

# Generated at 2022-06-14 07:14:28.118084
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {
        "x-forwarded-proto": "https",
        "x-scheme": "http",
        "x-forwarded-host": "host",
        "x-forwarded-port": "11111",
        "x-forwarded-for": "1.1.1.1, 2.2.2.2, 3.3.3.3",
        "x-forwarded-path": "path",
    }
    config = MockConfig(
        REAL_IP_HEADER=None,
        FORWARDED_FOR_HEADER="x-forwarded-for",
        PROXIES_COUNT=None,
    )
    fwd = parse_xforwarded(headers, config)
    assert fwd["for"] == "3.3.3.3"
    assert fwd["proto"]

# Generated at 2022-06-14 07:14:40.012929
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {
        "X-FORWARDED-FOR": "127.0.0.1",
        "X-FORWARDED-HOST": "localhost:8000",
        "X-FORWARDED-PORT": "8000",
        "X-FORWARDED-PROTO": "https",
        "X-FORWARDED-PATH": "/test path"
    }
    result = parse_xforwarded(headers)
    assert result["for"] == "127.0.0.1"
    assert result["proto"] == "https"
    assert result["host"] == "localhost:8000"

# Generated at 2022-06-14 07:14:58.807813
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    from sanic import Sanic
    from sanic.request import RequestParameters
    from sanic.exceptions import InvalidUsage
    from sanic.server import H2Protocol

    app = Sanic(__name__)

    @app.route("/")
    async def handler(request):
        proto = request.scheme
        host = request.host
        port = request.port
        paths = request.path
        return f"{proto}://{host}:{port}/{paths}"

    headers = {
        "X-Forwarded-Scheme": "http",
        "X-Forwarded-Host": "localhost:8888",
        "X-Forwarded-Port": "8888",
        "X-Forwarded-Path": "test",
    }

    request, response = H2Protocol(app).get_request

# Generated at 2022-06-14 07:15:05.514796
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    from sanic.config import Config
    from sanic.response import HTTPResponse
    config = Config()
    config.REAL_IP_HEADER = "real_ip"
    config.FORWARDED_FOR_HEADER = "x-forwarded-for"
    config.PROXIES_COUNT = 2
    response = HTTPResponse(status=200, headers={"real_ip": "1.1.1.1"})
    assert response.headers.get("real_ip") == "1.1.1.1"
    assert parse_xforwarded(response.headers, config) == {
        "for": "1.1.1.1"
    }

# Generated at 2022-06-14 07:15:08.020848
# Unit test for function parse_content_header
def test_parse_content_header():
    assert parse_content_header("form-data; name=upload; filename=\"file.txt\"") == ('form-data', {'name': 'upload', 'filename': 'file.txt'})


# Generated at 2022-06-14 07:15:15.363215
# Unit test for function parse_forwarded
def test_parse_forwarded():
    import random, time
    from . import config

    def getHeader(ip, secret):
        return [
            "By=%s;For=%s;Host=%s;Proto=%s;Path=%s"
            % (secret, ip, 'example.com', 'https', '/path')
        ]

    # Random secret
    secret = "%x" % (random.getrandbits(128))
    print("secret: %s" % secret)

    # Random IPs
    remote_addr = random.randint(0, (1 << 32) - 1)
    forwarded_for = random.randint(0, (1 << 32) - 1)


# Generated at 2022-06-14 07:15:25.631321
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    assert parse_xforwarded({}, {}) is None

    assert parse_xforwarded({"x-real-ip": "192.0.2.123"}, {}) == {
        "for": "192.0.2.123"
    }

    assert parse_xforwarded(
        {"x-real-ip": "192.0.2.123", "x-scheme": "https"}, {}
    ) == {"for": "192.0.2.123", "proto": "https"}

    assert parse_xforwarded(
        {"x-real-ip": "192.0.2.123", "x-forwarded-for": "192.0.2.123"}, {}
    ) == {"for": "192.0.2.123"}


# Generated at 2022-06-14 07:15:30.496787
# Unit test for function parse_content_header
def test_parse_content_header():
    header_value = 'form-data; name=upload; filename="file.txt"'
    header_value_result = ('form-data', {'name': 'upload', 'filename': 'file.txt'})
    result = parse_content_header(header_value)
    assert result == header_value_result



# Generated at 2022-06-14 07:15:38.385431
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    import sanic
    sanic.config.REAL_IP_HEADER = "X-Real-Ip"
    sanic.config.FORWARDED_FOR_HEADER = "X-Forwarded-For"
    sanic.config.PROXIES_COUNT = 3

    headers = {"X-Forwarded-For": "1.2.3.4, 3.4.5.6"}
    ret = parse_xforwarded(headers, sanic.config)
    assert ret["for"] == "1.2.3.4"
    assert not ret.get("host")

    headers = {"X-Forwarded-For": "1.2.3.4, 3.4.5.6, localhost, 7.8.9.10"}
    ret = parse_xforwarded(headers, sanic.config)

# Generated at 2022-06-14 07:15:48.251692
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {'x-forwarded-for': '192.168.1.1, 192.168.1.2, 192.168.1.3, 192.168.1.4', 'x-forwarded-host': 'www.example.com', 'x-forwarded-proto': 'http', 'x-scheme': 'http', 'x-forwarded-port': '80'}
    config = {'REAL_IP_HEADER': 'X-Forwarded-For', 'FORWARDED_FOR_HEADER': 'X-Forwarded-For', 'PROXIES_COUNT': 1}
    assert parse_xforwarded(headers, config) == {'for': '192.168.1.4', 'proto': 'http', 'host': 'www.example.com', 'port': 80, 'path': ''}

# Generated at 2022-06-14 07:15:56.293509
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {
        'X-Forwarded-For': '1.1.1.1',
        'X-Forwarded-Host': 'abc.com:80',
        'X-Forwarded-Proto': 'https',
        'X-Forwarded-Port': '8080'
    }

    opts = {
        'for': '1.1.1.1',
        'host': 'abc.com:80',
        'proto': 'https',
        'port': 8080
    }

    assert parse_xforwarded(headers, None) == opts

# Generated at 2022-06-14 07:16:04.039507
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {"X-Forwarded-For": "1.2.3.4, 1.2.3.4, 1.2.3.4, 1.2.3.4"}
    assert parse_xforwarded(headers=headers, proxies_count=2) is not None
    assert parse_xforwarded(headers=headers, proxies_count=3) is not None
    assert parse_xforwarded(headers=headers, proxies_count=4) is not None
    assert parse_xforwarded(headers=headers, proxies_count=5) is None

# Generated at 2022-06-14 07:16:23.385735
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    request = mock.Mock()
    request.headers = {
        "x-forwarded-host": "localhost:8080",
        "x-forwarded-path": "/api",
        "x-forwarded-port": "8080",
        "x-real-ip": "127.0.0.1",
        "x-forwarded-for": "127.0.0.1,127.0.0.1",
        "x-scheme": "http",
    }
    config = mock.Mock()
    config.REAL_IP_HEADER = "x-real-ip"
    config.FORWARDED_FOR_HEADER = "x-forwarded-for"
    config.FORWARDED_SECRET = None
    config.FORWARDED_PORT = None
    config.FORWARDED_PREF

# Generated at 2022-06-14 07:16:33.577535
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {
        "X-Forwarded-For": "10.0.0.1, 10.0.0.2, 10.0.0.3",
        "X-Forwarded-Port": "80, 8080, 8000",
        "X-Forwarded-Proto": "http, https, http",
        "X-Forwarded-Path": "/path1, /path2, /path3",
    }
    for i in range(4):
        assert parse_xforwarded(headers, config={
            "PROXIES_COUNT": i
        }) == {
            "for": "10.0.0.1",
            "port": 80,
            "proto": "http",
            "path": "/path1",
        }

# Generated at 2022-06-14 07:16:45.185579
# Unit test for function parse_forwarded
def test_parse_forwarded():
    headers = {'Forwarded': ['for=192.0.2.60;proto=http;by=158.158.158.158;secret=super-secret']}
    config = MagicMock()
    config.FORWARDED_SECRET = 'super-secret'
    result = parse_forwarded(headers,config)
    assert result['by'] == '192.0.2.60'
    assert result['for'] == '192.0.2.60'
    assert result['proto'] == 'http'
    assert result['by'] == '158.158.158.158'


# Unit tests for function parse_xforwarded

# Generated at 2022-06-14 07:16:57.058447
# Unit test for function parse_forwarded

# Generated at 2022-06-14 07:17:07.929323
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {
        "x-real-ip": "1.1.1.1",
        "x-forwarded-for": "2.2.2.2",
        "x-forwarded-scheme": "https"
    }
    config = {
        "PROXIES_COUNT": 1,
        "FORWARDED_FOR_HEADER": "x-forwarded-for",
        "FORWARDED_SECRET": "",
        "REAL_IP_HEADER": "x-real-ip",
    }

    ret = parse_xforwarded(headers, config)
    assert ret == {'for': '2.2.2.2', 'proto': 'https'}


if __name__ == "__main__":
    test_parse_xforwarded()

# Generated at 2022-06-14 07:17:15.877579
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    """Test the parse_xforwarded function."""
    from collections import OrderedDict

    from sanic.config import Config
    from sanic.request import Headers

    config = Config()
    config.FORWARDED_FOR_HEADER = "X-Forwarded-For"
    config.REAL_IP_HEADER = "X-Real-Ip"

    headers = Headers(dict(X_Forwarded_For="127.0.0.1, 10.0.0.1, 8.8.8.8"))
    assert parse_xforwarded(headers, config)["for"] == "8.8.8.8"

    headers = Headers(dict(X_Forwarded_For="127.0.0.1, 10.0.0.1, 8.8.8.8"))

# Generated at 2022-06-14 07:17:28.157559
# Unit test for function fwd_normalize
def test_fwd_normalize():
    assert fwd_normalize([
        ('for', '192.0.2.60'),
        ('by', '192.0.2.60'),
        ('proto', 'http')
    ]) == {
        'for': '192.0.2.60',
        'by': '192.0.2.60',
        'proto': 'http'
    }

    assert fwd_normalize([
        ('for', '192.0.2.60'),
        ('proto', 'http')
    ]) == {
        'for': '192.0.2.60',
        'proto': 'http'
    }


# Generated at 2022-06-14 07:17:41.651799
# Unit test for function parse_forwarded
def test_parse_forwarded():
    from sanic.request import Request
    class MockRequest(Request):
        def __init__(self, headers):
            self.headers = headers
        @property
        def app(self):
            class MockApp:
                FORWARDED_SECRET = "nothing-to-see-here"
            return MockApp

# Generated at 2022-06-14 07:17:55.093709
# Unit test for function parse_forwarded
def test_parse_forwarded():
    headers = [
        "by=_secret",
        "for=10.0.0.1;proto=https, for=10.10.0.1",
        "for=_do-not-trust, for=10.0.0.2;by=_secret",
        "for=_secret;by=_secret",
        "proto=ftp, for=192.0.2.60;by=_secret",
        "for=10.0.0.3;by=_secret, for=10.10.0.1",
        "for=\"[2001:db8:cafe::17]\";by=_secret",
    ]

# Generated at 2022-06-14 07:18:06.946815
# Unit test for function fwd_normalize
def test_fwd_normalize():
    assert fwd_normalize([]) == {}
    assert fwd_normalize([("foo", "bar")]) == {"foo": "bar"}
    assert fwd_normalize([("foo", None)]) == {}
    assert fwd_normalize([("for", "127.0.0.1:2000")]) == {"for": "127.0.0.1:2000"}
    assert fwd_normalize([("for", "[::1]:2000")]) == {"for": "[::1]:2000"}
    assert fwd_normalize([("port", 2000)]) == {"port": 2000}
    assert fwd_normalize([("port", "2000")]) == {"port": 2000}
    assert fwd_normalize([("port", "foo")]) == {}

# Generated at 2022-06-14 07:18:21.322685
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    from aiohttp import web
    app = web.Application()
    headers = {'X-Forwarded-Protocol': 'https', 'X-Forwarded-For': '127.0.0.1', 'X-Forwarded-Host': 'example.com',
               'X-Forwarded-Port': '443', 'X-Forwarded-Path': '/test/test'}
    assert parse_xforwarded(headers, app.config) == {'proto': 'https', 'for': '127.0.0.1', 'host': 'example.com',
                                                     'port': 443, 'path': '/test/test'}


# TESTING ONE HEADER AT A TIME


# Generated at 2022-06-14 07:18:33.406528
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {
        'x-forwarded-for': '1.1.1.1, 2.2.2.2, 3.3.3.3',
        'x-forwarded-host': 'testhost.com',
        'x-forwarded-port': '80',
        'x-forwarded-proto': 'https',
        'x-forwarded-path': '/'
    }
    config = {'REAL_IP_HEADER': None, 'PROXIES_COUNT': 2, 'FORWARDED_FOR_HEADER': 'x-forwarded-for'}

# Generated at 2022-06-14 07:18:48.034817
# Unit test for function parse_forwarded
def test_parse_forwarded():
    # Now parse
    assert parse_forwarded({"forwarded": ["seccret, for=_proxy", "by=_other"]}) == {}
    assert parse_forwarded({"forwarded": ["By=_other, for=_proxy, seccret"]}) == {}
    assert parse_forwarded({"forwarded": ["for=_proxy, secret, by=_other"]}) == {"for":"_proxy", "by":"_other"}
    assert parse_forwarded({"forwarded": ["for=_proxy, secret, by=_other,foo=bar, by=_singular", "for=_another"]}) == {"for":"_another", "by":"_singular", "foo":"bar"}

# Generated at 2022-06-14 07:19:00.094094
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    from sanic import Sanic
    from sanic.request import Request
    from sanic.config import DEFAULT_CONFIG

    config = DEFAULT_CONFIG
    config.FORWARDED_FOR_HEADER = "ForwardedFor"
    app = Sanic(__name__, config=config)


# Generated at 2022-06-14 07:19:08.231504
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    from sanic.config import Config
    headers = {'x-forwarded-for': 'hello', 'x-forwarded-proto': 'world',
               'x-forwarded-host': '1234.com', 'x-forwarded-path': 'abc'}
    config = Config(PROXIES_COUNT=1, FORWARDED_FOR_HEADER='x-forwarded-for',
                    REAL_IP_HEADER='x-forwarded-for', PROXY_HEADERS_PORT='x-forwarded-port',
                    PROXY_HEADERS_HOST='x-forwarded-host', PROXY_HEADERS_PROTO='x-forwarded-proto')
    print(parse_xforwarded(headers, config))

# Generated at 2022-06-14 07:19:21.860660
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    """Testing the function parse_xforwarded."""
    headers = {"x-forwarded-for": "1.2.3.4",
               "x-scheme": "http",
               "x-forwarded-host": "example.com",
               "x-forwarded-port": "80",
               "x-forwarded-path": "/foo%20bar",
               }
    xforwarded = parse_xforwarded(headers, None)
    assert xforwarded is not None
    assert xforwarded["for"] == "1.2.3.4"
    assert xforwarded["proto"] == "http"
    assert xforwarded["host"] == "example.com"
    assert xforwarded["port"] == 80
    assert xforwarded["path"] == "/foo bar"


# Generated at 2022-06-14 07:19:33.010426
# Unit test for function parse_forwarded
def test_parse_forwarded():
    from sanic.config import Config
    from sanic import Sanic

    app = Sanic('test_parse_forwarded')
    app.config.FORWARDED_SECRET = 'test-test-test'
    request = app.test_client.get('/',
                                  headers={
                                      'Forwarded': 'by=192.168.1.1; secret="test-test-test", for=192.168.1.2; secret="test-test-test"'
                                  })

    assert request.forwarded == {
        'for': '192.168.1.2',
        'by': '192.168.1.1',
        'secret': 'test-test-test'
    }


if __name__ == '__main__':
    test_parse_forwarded()

# Generated at 2022-06-14 07:19:33.645542
# Unit test for function parse_forwarded
def test_parse_forwarded():
    pass

# Generated at 2022-06-14 07:19:40.218929
# Unit test for function parse_forwarded
def test_parse_forwarded():
    d = parse_forwarded(["for=_kd9sd9s9d9s9_, secret=x"])
    assert d == {"for": "_kd9sd9s9d9s9_", "secret": "x"}

    d = parse_forwarded(["secret=y, for=_jd9d9kd9k9d9_"])
    assert d == {"for": "_jd9d9kd9k9d9_", "secret": "y"}

    # "for" without secret should not be found
    d = parse_forwarded(["for=_kd9sd9s9d9s9_"])
    assert d == None

    # "by" with secret is allowed

# Generated at 2022-06-14 07:19:49.945130
# Unit test for function parse_forwarded
def test_parse_forwarded():
    config = {}
    config['FORWARDED_SECRET'] = "weaksecret"
    headers = []
    headers.append("for=192.0.2.60; proto=https, by=203.0.113.43; secret=weaksecret, for=127.0.0.1")
    headers.append("for=192.0.2.43, for=198.51.100.17; secret=weaksecret")
    ret = parse_forwarded(headers, config)
    assert ret == {'by': '203.0.113.43', 'for': '127.0.0.1', 'proto': 'https', 'secret': 'weaksecret'}

# Generated at 2022-06-14 07:20:05.755319
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    headers = {
        'X-Forwarded-Path': '/home/yuejie',
        'X-Forwarded-Proto': 'https',
        'X-Forwarded-Port': '443'
    }
    print(parse_xforwarded(headers, None))

# Generated at 2022-06-14 07:20:16.093579
# Unit test for function parse_xforwarded
def test_parse_xforwarded():
    from sanic.config import Config
    from sanic.request import HeaderMap
    config = Config()
    config.REAL_IP_HEADER = "X-Forwarded-For"
    config.FORWARDED_FOR_HEADER = "X-Forwarded-For"
    config.PROXIES_COUNT = 2
    test_map = {
        "X-Forwarded-For": "1.2.3.4, 111.222.33.44",
        "X-Forwarded-Host": "foo.com:8080",
        "X-Forwarded-Proto": "https",
        "X-Forwarded-Port": "8080",
        "X-Forwarded-Path": "/api",
    }
    map = HeaderMap(test_map)
    fwd = parse_xforwarded(map, config)

# Generated at 2022-06-14 07:20:27.877318
# Unit test for function parse_forwarded
def test_parse_forwarded():
    assert parse_forwarded({"forwarded": "for=192.0.2.60;proto=http;by=203.0.113.43,for=192.0.2.61"}, "") == {"for": "192.0.2.60", "proto": "http", "by": "203.0.113.43"}
    assert parse_forwarded({"forwarded": ""}, "") == None
    assert parse_forwarded({"forwarded": "for=192.0.2.60;proto=http;by=203.0.113.43,for=192.0.2.61"}, "203.0.113.43") == {"for": "192.0.2.60", "proto": "http", "by": "203.0.113.43"}

# Generated at 2022-06-14 07:20:41.824469
# Unit test for function parse_forwarded

# Generated at 2022-06-14 07:20:51.233968
# Unit test for function parse_xforwarded
def test_parse_xforwarded():

    class Headers(object):
        def get(self, key):
            return self.get_value.get(key)

        def getall(self, key):
            return self.get_all_values.get(key)

    class Config(object):
        REAL_IP_HEADER = 'X-Real-IP'
        FORWARDED_FOR_HEADER = 'X-Forwarded-For'
        PROXIES_COUNT = 1
        FORWARDED_SECRET = ''

    class TestCase(object):
        def __init__(self, real_ip, forwarded_for, expected):
            self.headers = Headers()
            self.headers.get_value = {
                'X-Real-IP': real_ip,
            }

# Generated at 2022-06-14 07:21:04.698781
# Unit test for function parse_forwarded
def test_parse_forwarded():
    from sanic.config import Config
    from sanic.request import Headers
    import json

    config = Config()
    config.FORWARDED_SECRET = "test_secret"


# Generated at 2022-06-14 07:21:12.669469
# Unit test for function parse_forwarded
def test_parse_forwarded():
    value = 'for=192.0.2.0;by=203.0.113.0;proto=http;host=example.com'
    options = parse_forwarded(value)
    assert options['for'] == '192.0.2.0'
    assert options['by'] == '203.0.113.0'
    assert options['proto'] == 'http'
    assert options['host'] == 'example.com'